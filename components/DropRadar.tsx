"use client";
import { useEffect, useState } from "react";
import type { Drop } from "@/lib/drops";
import { SAMPLE_DROPS } from "@/lib/drops";

const money = (n: number) =>
  "$" + n.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });

export default function DropRadar({
  onScore,
  onOwn,
}: {
  onScore: (name: string, price: number) => void;
  onOwn: (name: string, price: number) => void;
}) {
  const [drops, setDrops] = useState<Drop[]>(SAMPLE_DROPS);
  const [store, setStore] = useState("");

  useEffect(() => {
    // Reads the live feed from /api/drops (set MOONITOR_DROPS_URL to your backend).
    fetch("/api/drops", { cache: "no-store" })
      .then((r) => r.json())
      .then((d) => {
        if (Array.isArray(d?.drops)) setDrops(d.drops);
      })
      .catch(() => {});
  }, []);

  const stores = Array.from(new Set(drops.map((d) => d.store)));
  const shown = drops.filter((d) => !store || d.store === store);
  const input = "w-full bg-card2 border border-line rounded-lg px-3 py-2 text-[#e7e9ee]";

  return (
    <div className="rounded-xl border border-line bg-card p-4">
      <label className="block text-xs uppercase tracking-wide text-mut font-semibold mb-1">
        Filter store
      </label>
      <select className={input} value={store} onChange={(e) => setStore(e.target.value)}>
        <option value="">All stores</option>
        {stores.map((s) => (
          <option key={s} value={s}>{s}</option>
        ))}
      </select>

      <div className="mt-4 space-y-2">
        {shown.map((d, i) => (
          <div key={i}
            className="flex items-center justify-between gap-3 rounded-lg border border-line bg-card2 px-4 py-3">
            <div>
              <div><span className="font-bold">{d.store}</span> · {d.name}</div>
              <div className="text-xs text-mut mt-1">
                <span className="mr-2 rounded-full border border-line px-2 py-0.5">{d.tag}</span>
                {money(d.price)}
              </div>
            </div>
            <div className="flex gap-2">
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
      </div>
    </div>
  );
}
