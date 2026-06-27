import { NextResponse } from "next/server";

export const dynamic = "force-dynamic";

const GUILD = process.env.GOAT_GUILD_ID || "798512090809368627";

// Paid membership-tier roles in the GOAT server. Holding ANY = member.
const ROLE_NAMES: Record<string, string> = {
  // staff/owner — always have access
  "817149188835508244": "Admin",
  "883550138302361712": "Staff",
  "882796255590375465": "The GOAT",
  // paid membership tiers
  "1016734067171000360": "GOATs",
  "1016734278677180446": "Legends",
  "860707731467272192": "Hall of Famers",
  "860708062481743882": "MVPs",
  "817565721096749096": "All Stars",
  "883320882506919986": "OnlyCards",
  "825802671393996910": "Bench Warmers",
  "860707445995601941": "Starters",
  "915135003992662026": "1 Hour Trial",
};
const PAID_ROLES = new Set(Object.keys(ROLE_NAMES));

export async function GET(req: Request) {
  const token = process.env.DISCORD_BOT_TOKEN;
  const params = new URLSearchParams(req.url.split("?")[1] || "");
  const discordId = params.get("discordId");
  if (!token || !discordId) {
    return NextResponse.json({ member: false, reason: "no-discord" });
  }
  try {
    const res = await fetch(
      `https://discord.com/api/v10/guilds/${GUILD}/members/${discordId}`,
      { headers: { Authorization: `Bot ${token}` }, cache: "no-store" }
    );
    if (res.status === 404) return NextResponse.json({ member: false, reason: "not-in-server" });
    if (!res.ok) return NextResponse.json({ member: false, reason: "error" });
    const m = (await res.json()) as { roles?: string[] };
    const held = (m.roles ?? []).filter((r) => PAID_ROLES.has(r));
    return NextResponse.json({
      member: held.length > 0,
      tier: held.length ? ROLE_NAMES[held[0]] : null,
    });
  } catch {
    return NextResponse.json({ member: false, reason: "error" });
  }
}
