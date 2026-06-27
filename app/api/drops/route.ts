import { NextResponse } from "next/server";
import { SAMPLE_DROPS, Drop } from "@/lib/drops";

export const dynamic = "force-dynamic";
export const revalidate = 0;

// The live 🐄 monitor channels in your GOAT server. Add/remove as you like.
const CHANNELS: { id: string; store: string; tag: string }[] = [
  { id: "933258704999039006", store: "Target", tag: "🎯 Target" },
  { id: "933258893692379186", store: "Walmart", tag: "🛒 Walmart" },
  { id: "1029931616715419728", store: "Pokémon Center", tag: "⚡ Pokémon" },
  { id: "933786774084415498", store: "New Cards In Stock", tag: "🃏 Cards" },
  { id: "933785315037032478", store: "New Sports Cards", tag: "🏈 Sports" },
  { id: "933257381486411806", store: "Best Buy", tag: "🔵 Best Buy" },
  { id: "933257584570425354", store: "Costco", tag: "📦 Costco" },
];

const PRICE_RE = /\$\s?(\d[\d,]*(?:\.\d{1,2})?)/;
function parsePrice(text: string): number {
  const m = text.match(PRICE_RE);
  return m ? parseFloat(m[1].replace(/,/g, "")) || 0 : 0;
}

type Embed = {
  title?: string;
  description?: string;
  url?: string;
  timestamp?: string;
  fields?: { name: string; value: string }[];
};
type Msg = { id: string; timestamp: string; embeds?: Embed[] };

async function fetchChannel(
  token: string,
  ch: { id: string; store: string; tag: string }
): Promise<(Drop & { ts: string })[]> {
  const res = await fetch(
    `https://discord.com/api/v10/channels/${ch.id}/messages?limit=8`,
    { headers: { Authorization: `Bot ${token}` }, cache: "no-store" }
  );
  if (!res.ok) return [];
  const msgs = (await res.json()) as Msg[];
  const out: (Drop & { ts: string })[] = [];
  for (const m of msgs) {
    for (const e of m.embeds ?? []) {
      const blob = [e.title, e.description, ...(e.fields?.flatMap((f) => [f.name, f.value]) ?? [])]
        .filter(Boolean)
        .join(" \n ");
      const name = (e.title || e.description || "").split("\n")[0].slice(0, 140).trim();
      if (!name) continue;
      out.push({
        store: ch.store,
        name,
        price: parsePrice(blob),
        tag: ch.tag,
        url: e.url || undefined,
        ts: e.timestamp || m.timestamp,
      });
    }
  }
  return out;
}

export async function GET() {
  const token = process.env.DISCORD_BOT_TOKEN;
  if (token) {
    try {
      const results = await Promise.all(
        CHANNELS.map((c) => fetchChannel(token, c).catch(() => []))
      );
      const drops = results
        .flat()
        .sort((a, b) => (a.ts < b.ts ? 1 : -1))
        .slice(0, 40)
        .map(({ ts, ...d }) => d);
      if (drops.length) return NextResponse.json({ drops, source: "discord" });
    } catch {
      /* fall through to fallbacks */
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
