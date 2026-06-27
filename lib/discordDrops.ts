import { Drop } from "./drops";

// The live 🐄 monitor channels in your GOAT server.
export const CHANNELS: { id: string; store: string; tag: string }[] = [
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
function cleanName(s: string): string {
  let n = s.replace(/\s+/g, " ").trim();
  for (let i = 0; i < 3; i++) n = n.replace(/\s+(NEW[MW]?|N\d+)$/i, "").trim();
  return n.slice(0, 140);
}
function storeFromUrl(url: string | undefined, fallback: string): string {
  if (!url) return fallback;
  const u = url.toLowerCase();
  if (u.includes("walmart.")) return "Walmart";
  if (u.includes("bestbuy.")) return "Best Buy";
  if (u.includes("target.")) return "Target";
  if (u.includes("amazon.")) return "Amazon";
  if (u.includes("pokemoncenter.")) return "Pokémon Center";
  if (u.includes("costco.")) return "Costco";
  if (u.includes("gamestop.")) return "GameStop";
  if (u.includes("samsclub.")) return "Sam's Club";
  return fallback;
}

type Embed = { title?: string; description?: string; url?: string; timestamp?: string; fields?: { name: string; value: string }[] };
type Msg = { id: string; timestamp: string; embeds?: Embed[] };
type DropTs = Drop & { ts: string };

async function fetchChannel(token: string, ch: { id: string; store: string; tag: string }): Promise<DropTs[]> {
  const res = await fetch(`https://discord.com/api/v10/channels/${ch.id}/messages?limit=8`, {
    headers: { Authorization: `Bot ${token}` },
    cache: "no-store",
  });
  if (!res.ok) return [];
  const msgs = (await res.json()) as Msg[];
  const out: DropTs[] = [];
  for (const m of msgs) {
    for (const e of m.embeds ?? []) {
      const blob = [e.title, e.description, ...(e.fields?.flatMap((f) => [f.name, f.value]) ?? [])].filter(Boolean).join(" \n ");
      const name = cleanName(e.title || e.description || "");
      if (!name) continue;
      out.push({ store: storeFromUrl(e.url, ch.store), name, price: parsePrice(blob), tag: ch.tag, url: e.url || undefined, ts: e.timestamp || m.timestamp });
    }
  }
  return out;
}

export const dropKey = (d: Drop) => (d.url || d.name).toLowerCase();

/** Pull recent drops from all channels, newest first, deduped. */
export async function fetchLiveDrops(token: string): Promise<Drop[]> {
  const results = await Promise.all(CHANNELS.map((c) => fetchChannel(token, c).catch(() => [] as DropTs[])));
  const seen = new Set<string>();
  return results
    .flat()
    .sort((a, b) => (a.ts < b.ts ? 1 : -1))
    .filter((d) => {
      const k = dropKey(d);
      if (seen.has(k)) return false;
      seen.add(k);
      return true;
    })
    .slice(0, 30)
    .map(({ ts, ...d }) => d);
}
