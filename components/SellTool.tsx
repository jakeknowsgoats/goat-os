"use client";
import { useState } from "react";
import { sellTiming } from "@/lib/engine";
import { verdictClass } from "./VerdictBadge";

const pct = (n: number) => (n * 100).toFixed(1) + "%";

export default function SellTool() {
  const [name, setName] = useState("2024 Bowman Chrome Baseball Hobby");
  const [rel, setRel] = useState("2024-05-01");
  const [mult, setMult] = useState(2);
  const [cost, setCost] = useState(300);
  const [comp, setComp] = useState(360);

  const res = sellTiming(rel, cost, comp, mult);

  const label = "block text-xs uppercase tracking-wide text-mut font-semibold mt-3 mb-1";
  const input = "w-full bg-card2 border border-line rounded-lg px-3 py-2 text-[#e7e9ee]";

  return (
    <div className="grid gap-4 md:grid-cols-2">
      <div className="rounded-xl border border-line bg-card p-4">
        <label className={label}>Product</label>
        <input className={input} value={name} onChange={(e) => setName(e.target.value)} />
        <div className="grid grid-cols-2 gap-3">
          <div>
            <label className={label}>Release date</label>
            <input type="date" className={input} value={rel} onChange={(e) => setRel(e.target.value)} />
          </div>
          <div>
            <label className={label}>Target multiple</label>
            <input type="number" step="0.1" className={input} value={mult}
              onChange={(e) => setMult(+e.target.value)} />
          </div>
        </div>
        <div className="grid grid-cols-2 gap-3">
          <div>
            <label className={label}>Buy cost $</label>
            <input type="number" className={input} value={cost} onChange={(e) => setCost(+e.target.value)} />
          </div>
          <div>
            <label className={label}>Current comp $</label>
            <input type="number" className={input} value={comp} onChange={(e) => setComp(+e.target.value)} />
          </div>
        </div>
      </div>

      <div className="rounded-xl border border-line bg-card p-4">
        <div className="text-center">
          <div className="text-mut text-sm">{name}</div>
          <div className="my-2">
            <span className={`inline-block rounded-lg px-4 py-2 text-lg font-extrabold ${verdictClass(res.action)}`}>
              {res.action}
            </span>
          </div>
        </div>
        <div className="mt-3 space-y-1 text-sm">
          <Row k="Months since release" v={String(res.months)} />
          <Row k="Current phase" v={res.phase} />
          <Row k="Gain vs cost" v={pct(res.gain)} good={res.gain >= 0} />
        </div>
        <p className="text-mut text-xs mt-3">
          5-phase clock: Pre-release → Launch → Saturation → Consolidation → Scarcity (optimal exit yr 5-7).
        </p>
      </div>
    </div>
  );
}

function Row({ k, v, good }: { k: string; v: string; good?: boolean }) {
  return (
    <div className="flex justify-between border-b border-dashed border-line py-1.5">
      <span className="text-mut">{k}</span>
      <b className={good === undefined ? "" : good ? "text-green-400" : "text-red-400"}>{v}</b>
    </div>
  );
}
