import { NextResponse } from "next/server";
import { SAMPLE_DROPS } from "@/lib/drops";

export const dynamic = "force-dynamic";

// Set MOONITOR_DROPS_URL to your backend's JSON endpoint ({ drops: [...] }) to serve
// live data. Falls back to sample drops when unset/unreachable.
export async function GET() {
  const url = process.env.MOONITOR_DROPS_URL;
  if (url) {
    try {
      const res = await fetch(url, { cache: "no-store" });
      if (res.ok) {
        const data = await res.json();
        if (Array.isArray(data?.drops)) {
          return NextResponse.json({ drops: data.drops, source: "moonitor" });
        }
      }
    } catch {
      // fall through to sample
    }
  }
  return NextResponse.json({ drops: SAMPLE_DROPS, source: "sample" });
}
