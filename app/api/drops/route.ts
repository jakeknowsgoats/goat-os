import { NextResponse } from "next/server";
import { SAMPLE_DROPS } from "@/lib/drops";
import { fetchLiveDrops } from "@/lib/discordDrops";

export const dynamic = "force-dynamic";
export const revalidate = 0;

export async function GET() {
  const token = process.env.DISCORD_BOT_TOKEN;
  if (token) {
    try {
      const drops = await fetchLiveDrops(token);
      if (drops.length) return NextResponse.json({ drops, source: "discord" });
    } catch {
      /* fall through */
    }
  }
  const url = process.env.MOONITOR_DROPS_URL;
  if (url) {
    try {
      const r = await fetch(url, { cache: "no-store" });
      if (r.ok) {
        const data = await r.json();
        if (Array.isArray(data?.drops)) return NextResponse.json({ drops: data.drops, source: "url" });
      }
    } catch {
      /* fall through */
    }
  }
  return NextResponse.json({ drops: SAMPLE_DROPS, source: "sample" });
}
