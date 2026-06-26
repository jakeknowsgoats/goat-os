"use client";
import { useCallback, useEffect, useState } from "react";
import {
  Item,
  listItems,
  addItem,
  updateItem,
  removeItem,
  isSynced,
} from "@/lib/collection";
import { sellTiming } from "@/lib/engine";
import { supabase } from "@/lib/supabase";

const money = (n: number) =>
  "$" + (+n).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });

const blank = { name: "", type: "Sealed", qty: 1, cost: 0, comp: 0, release: "" };

export default function Collection({ active }: { active: boolean }) {
  const [items, setItems] = useState<Item[]>([]);
  const [synced, setSynced] = useState(false);
  const [form, setForm] = useState({ ...blank });

  const load = useCallback(async () => {
    setItems(await listItems());
    setSynced(await isSynced());
  }, []);

  useEffect(() => {
    load();
  }, [load]);
  useEffect(() => {
    if (active) load();
  }, [active, load]);
  useEffect(() => {
    if (!supabase) return;
    const { data: l } = supabase.auth.onAuthStateChange(() => load());
    return () => l.subscription.unsubscribe();
  }, [load]);

  async function add() {
    if (!form.name.trim()) return;
    await addItem({
      name: form.name.trim(),
      type: form.type,
      qty: +form.qty || 1,
      cost: +form.cost || 0,
      comp: +form.comp || 0,
      release: form.release || null,
    });
    setForm({ ...blank });
    load();
  }

  const tc = items.reduce((a, it) => a + +it.cost * +it.qty, 0);
  const tv = items.reduce((a, it) => a + +it.comp * +it.qty, 0);
  const tp = tv - tc;
  let topPct = 0,
    topName = "";
  items.forEach((it) => {
    const v = +it.comp * +it.qty;
    if (tv > 0 && v / tv > topPct) {
      topPct = v / tv;
      topName = it.name;
    }
  });

  const label = "block text-[11px] uppercase tracking-wide text-mut font-semibold mb-1";
  const input = "w-full bg-card2 border border-line rounded-lg px-2 py-1.5 text-sm text-[#e7e9ee]";

  return (
    <div>
      <div className="mb-3 text-xs text-mut">
        {synced ? "☁️ Synced to your account" : "💾 Saved on this device — sign in (top right) to sync across devices"}
      </div>

      <div className="mb-4 flex flex-wrap gap-2.5">
        <Stat l="Holdings" v={String(items.length)} />
        <Stat l="Cost basis" v={money(tc)} />
        <Stat l="Market value" v={money(tv)} />
        <Stat
          l="Total P/L"
          v={`${money(tp)} (${tc > 0 ? Math.round((tp / tc) * 100) : 0}%)`}
          color={tp >= 0 ? "text-green-400" : "text-red-400"}
        />
      </div>

      {topPct > 0.3 && items.length > 1 && (
        <div className="mb-3 rounded-lg border border-red-800 bg-red-500/10 px-3 py-2 text-sm text-red-300">
          ⚠️ Concentration: <b>{topName}</b> is {Math.round(topPct * 100)}% of your portfolio value. Consider trimming to rebalance.
        </div>
      )}

      <div className="rounded-xl border border-line bg-card p-4">
        <table className="w-full border-collapse text-sm">
          <thead>
            <tr className="text-left text-mut">
              <th className="border-b border-line p-2">Item</th>
              <th className="border-b border-line p-2">Qty</th>
              <th className="border-b border-line p-2">Cost/ea</th>
              <th className="border-b border-line p-2">Comp/ea</th>
              <th className="border-b border-line p-2">Value</th>
              <th className="border-b border-line p-2">P/L</th>
              <th className="border-b border-line p-2"></th>
            </tr>
          </thead>
          <tbody>
            {items.map((it) => {
              const value = +it.comp * +it.qty;
              const pl = value - +it.cost * +it.qty;
              const plp = +it.cost > 0 ? pl / (+it.cost * +it.qty) : 0;
              const timing = it.release ? sellTiming(it.release, +it.cost, +it.comp, 0) : null;
              return (
                <tr key={it.id}>
                  <td className="border-b border-line p-2">
                    {it.name}
                    <div className="text-xs text-mut">
                      {it.type}
                      {timing && (
                        <span className="ml-1 rounded-full border border-line px-1.5 py-0.5 text-[10px]">
                          {timing.phase} · {timing.action}
                        </span>
                      )}
                    </div>
                  </td>
                  <td className="border-b border-line p-2">{it.qty}</td>
                  <td className="border-b border-line p-2">{money(it.cost)}</td>
                  <td className="border-b border-line p-2">
                    <input
                      type="number"
                      defaultValue={it.comp}
                      onBlur={async (e) => {
                        await updateItem(it.id, { comp: +e.target.value });
                        load();
                      }}
                      className="w-20 rounded border border-line bg-card2 px-1.5 py-1 text-sm"
                    />
                  </td>
                  <td className="border-b border-line p-2">{money(value)}</td>
                  <td className={`border-b border-line p-2 ${pl >= 0 ? "text-green-400" : "text-red-400"}`}>
                    {money(pl)}
                    <div className="text-xs text-mut">{Math.round(plp * 100)}%</div>
                  </td>
                  <td className="border-b border-line p-2">
                    <button
                      onClick={async () => {
                        await removeItem(it.id);
                        load();
                      }}
                      className="rounded border border-line px-2 py-1 text-xs"
                    >
                      ✕
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
        {items.length === 0 && (
          <div className="p-2 text-xs text-mut">
            No holdings yet — add one below, or hit &quot;+ Own&quot; on a drop in Drop Radar.
          </div>
        )}
      </div>

      <div className="mt-4 rounded-xl border border-line bg-card p-4">
        <div className="mb-2 text-[11px] font-semibold uppercase tracking-wide text-mut">Add a holding</div>
        <div className="grid grid-cols-2 gap-2.5 md:grid-cols-6">
          <div className="col-span-2">
            <label className={label}>Product</label>
            <input className={input} value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} placeholder="2024 Prizm Football Hobby" />
          </div>
          <div>
            <label className={label}>Type</label>
            <select className={input} value={form.type} onChange={(e) => setForm({ ...form, type: e.target.value })}>
              <option>Sealed</option><option>Single</option><option>Slab</option>
            </select>
          </div>
          <div>
            <label className={label}>Qty</label>
            <input type="number" className={input} value={form.qty} onChange={(e) => setForm({ ...form, qty: +e.target.value })} />
          </div>
          <div>
            <label className={label}>Cost/ea</label>
            <input type="number" className={input} value={form.cost} onChange={(e) => setForm({ ...form, cost: +e.target.value })} />
          </div>
          <div>
            <label className={label}>Comp/ea</label>
            <input type="number" className={input} value={form.comp} onChange={(e) => setForm({ ...form, comp: +e.target.value })} />
          </div>
          <div className="col-span-2">
            <label className={label}>Release (optional)</label>
            <input type="date" className={input} value={form.release} onChange={(e) => setForm({ ...form, release: e.target.value })} />
          </div>
          <div className="flex items-end">
            <button onClick={add} className="rounded-lg bg-goat px-4 py-2 font-bold text-[#1a1206]">Add</button>
          </div>
        </div>
      </div>
    </div>
  );
}

function Stat({ l, v, color }: { l: string; v: string; color?: string }) {
  return (
    <div className="min-w-[140px] flex-1 rounded-lg border border-line bg-card2 p-3">
      <div className="text-[11px] uppercase tracking-wide text-mut">{l}</div>
      <div className={`mt-0.5 text-xl font-extrabold ${color ?? ""}`}>{v}</div>
    </div>
  );
}
