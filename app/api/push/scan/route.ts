import { NextResponse } from "next/server";
import webpush from "web-push";
import { createClient } from "@supabase/supabase-js";
import { fetchLiveDrops, dropKey } from "@/lib/discordDrops";

export const dynamic = "force-dynamic";

// Called on a schedule (cron). Detects NEW drops since last run and pushes them
// to subscribed members. Each push opens the store link on tap.
export async function GET() {
  const token = process.env.DISCORD_BOT_TOKEN;
  const SURL = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const SROLE = process.env.SUPABASE_SERVICE_ROLE_KEY;
  const VPUB = process.env.NEXT_PUBLIC_VAPID_PUBLIC_KEY;
  const VPRIV = process.env.VAPID_PRIVATE_KEY;
  if (!token || !SURL || !SROLE || !VPUB || !VPRIV) {
    return NextResponse.json({ ok: false, reason: "not-configured" });
  }

  webpush.setVapidDetails("mailto:alerts@thegoatmonitor.com", VPUB, VPRIV);
  const db = createClient(SURL, SROLE, { auth: { persistSession: false } });

  const drops = (await fetchLiveDrops(token)).filter((d) => d.url);

  const { data: stateRow } = await db.from("push_state").select("seen").eq("id", "drops").maybeSingle();
  const seen: string[] = stateRow?.seen ?? [];

  // First run: seed without spamming a backlog.
  if (seen.length === 0) {
    await db.from("push_state").upsert({ id: "drops", seen: drops.map(dropKey).slice(0, 300) });
    return NextResponse.json({ ok: true, initialized: true });
  }

  const seenSet = new Set(seen);
  const fresh = drops.filter((d) => !seenSet.has(dropKey(d)));
  await db.from("push_state").upsert({ id: "drops", seen: [...drops.map(dropKey), ...seen].slice(0, 300) });

  if (fresh.length === 0) return NextResponse.json({ ok: true, sent: 0 });

  const { data: subs } = await db.from("push_subs").select("*");
  let sent = 0;
  for (const d of fresh) {
    const payload = JSON.stringify({
      title: `🚨 ${d.store}`,
      body: `${d.name}${d.price ? " — $" + d.price.toFixed(2) : ""}`,
      url: d.url,
      tag: dropKey(d),
    });
    for (const s of subs ?? []) {
      const stores: string[] = s.stores ?? [];
      if (stores.length && !stores.includes(d.store)) continue;
      try {
        await webpush.sendNotification(
          { endpoint: s.endpoint, keys: { p256dh: s.p256dh, auth: s.auth } },
          payload
        );
        sent++;
      } catch (e) {
        const code = (e as { statusCode?: number })?.statusCode;
        if (code === 404 || code === 410) await db.from("push_subs").delete().eq("endpoint", s.endpoint);
      }
    }
  }
  return NextResponse.json({ ok: true, sent, fresh: fresh.length });
}
