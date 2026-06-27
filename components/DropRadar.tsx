"use client";
import { useEffect, useMemo, useState } from "react";
import type { Drop } from "@/lib/drops";
import { SAMPLE_DROPS } from "@/lib/drops";

const money = (n: number) =>
  n > 0 ? "$" + n.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }) : "—";

const MKEY = "goat_muted_stores";

export default function DropRadar({
  onScore,
  onOwn,
}: {
  onScore: (name: string, price: number) => void;
  onOwn: (name: string, price: number) => void;
}) {
  const [drops, setDrops] = useState<Drop[]>(SAMPLE_DROPS);
  const [source, setSource] = useState("sample");
  const [muted, setMuted] = useState<string[]>([]);

  // load saved muted stores
  useEffect(() => {
    try {
      setMuted(JSON.parse(localStorage.getItem(MKEY) || "[]"));
    } catch {
      /* ignore */
    }
  }, []);
  useEffect(() => {
    try {
      localStorage.setItem(MKEY, JSON.stringify(muted));
    } catch {
      /* ignore */
    }
  }, [muted]);

  // live feed: load now + refresh every 45s
  useEffect(() => {
    let alive = true;
    const load = () =>
      fetch("/api/drops", { cache: "no-store" })
        .then((r) => r.json())
        .then((d) => {
          if (alive && Array.isArray(d?.drops)) {
            setDrops(d.drops);
            setSource(d.source || "sample");
          }
        })
        .catch(() => {});
    load();
    const t = setInterval(load, 45000);
    return () => {
      alive = false;
      clearInterval(t);
    };
  }, []);

  const stores = useMemo(() => Array.from(new Set(drops.map((d) => d.store))), [drops]);
  const shown = drops.filter((d) => !muted.includes(d.store));
  const toggle = (s: string) =>
    setMuted((m) => (m.includes(s) ? m.filter((x) => x !== s) : [...m, s]));

  const live = source === "discord";

  return (
    <div>
      <div className="mb-3 flex items-center gap-2 text-xs">
        <span
          className={`inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 font-semibold ${
            live ? "bg-green-500/15 text-green-300" : "bg-yellow-500/15 text-yellow-300"
          }`}
        >
          <span className={`h-2 w-2 rounded-full ${live ? "bg-green-400" : "bg-yellow-400"}`} />
          {live ? "LIVE from your Discord" : source === "url" ? "Live feed" : "Sample data — connect your Discord to go live"}
        </span>
        <span className="text-mut">· auto-refreshing every 45s</span>
      </div>

      <div className="mb-4 rounded-xl border border-line bg-card p-3">
        <div className="mb-2 text-[11px] font-semibold uppercase tracking-wide text-mut">
          Your alerts — tap a store to turn it on/off
        </div>
        <div className="flex flex-wrap gap-2">
          {stores.map((s) => {
            const on = !muted.includes(s);
            return (
              <button
                key={s}
                onClick={() => toggle(s)}
                className={`rounded-full border px-3 py-1 text-sm font-semibold ${
                  on ? "border-goat bg-goat text-[#1a1206]" : "border-line bg-card2 text-mut line-through"
                }`}
              >
                {on ? "🔔" : "🔕"} {s}
              </button>
            );
          })}
        </div>
      </div>

      <div className="space-y-2">
        {shown.map((d, i) => (
          <div
            key={i}
            className="flex items-center justify-between gap-3 rounded-lg border border-line bg-card2 px-4 py-3"
          >
            <div>
              <div>
                <span className="font-bold">{d.store}</span> · {d.name}
              </div>
              <div className="mt-1 text-xs text-mut">
                <span className="mr-2 rounded-full border border-line px-2 py-0.5">{d.tag}</span>
                {money(d.price)}
              </div>
            </div>
            <div className="flex shrink-0 gap-2">
              <a
                href={d.url || "#"}
                target="_blank"
                rel="noopener noreferrer"
                className="rounded-lg border border-line px-3 py-2 text-sm font-bold"
              >
                Buy
              </a>
              <button
                onClick={() => onOwn(d.name, d.price)}
                className="rounded-lg border border-line px-3 py-2 text-sm font-bold"
              >
                + Own
              </button>
              <button
                onClick={() => onScore(d.name, d.price)}
                className="rounded-lg bg-goat px-3 py-2 text-sm font-bold text-[#1a1206]"
              >
                Score it →
              </button>
            </div>
          </div>
        ))}
        {shown.length === 0 && (
          <div className="rounded-lg border border-line bg-card2 px-4 py-6 text-center text-sm text-mut">
            All stores are turned off — tap a store above to see its drops.
          </div>
        )}
      </div>
    </div>
  );
}
