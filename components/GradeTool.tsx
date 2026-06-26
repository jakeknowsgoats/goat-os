"use client";
import { useState } from "react";
import { gradeOrSell } from "@/lib/engine";
import { verdictClass } from "./VerdictBadge";

const money = (n: number) =>
  "$" + n.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });

export default function GradeTool() {
  const [raw, setRaw] = useState(60);
  const [psa, setPsa] = useState(160);
  const [cost, setCost] = useState(45);
  const [fee, setFee] = useState(13.6);

  const res = gradeOrSell(raw, psa, cost, fee / 100);
  const label = "block text-xs uppercase tracking-wide text-mut font-semibold mt-3 mb-1";
  const input = "w-full bg-card2 border border-line rounded-lg px-3 py-2 text-[#e7e9ee]";

  return (
    <div className="grid gap-4 md:grid-cols-2">
      <div className="rounded-xl border border-line bg-card p-4">
        <div className="grid grid-cols-2 gap-3">
          <div>
            <label className={label}>Raw comp $</label>
            <input type="number" className={input} value={raw} onChange={(e) => setRaw(+e.target.value)} />
          </div>
          <div>
            <label className={label}>PSA 10 comp $</label>
            <input type="number" className={input} value={psa} onChange={(e) => setPsa(+e.target.value)} />
          </div>
        </div>
        <div className="grid grid-cols-2 gap-3">
          <div>
            <label className={label}>Grading all-in $</label>
            <input type="number" className={input} value={cost} onChange={(e) => setCost(+e.target.value)} />
          </div>
          <div>
            <label className={label}>Sell fee %</label>
            <input type="number" step="0.1" className={input} value={fee} onChange={(e) => setFee(+e.target.value)} />
          </div>
        </div>
      </div>
      <div className="rounded-xl border border-line bg-card p-4">
        <div className="text-center my-1">
          <span className={`inline-block rounded-lg px-4 py-2 text-lg font-extrabold ${verdictClass(res.verdict)}`}>
            {res.verdict}
          </span>
        </div>
        <div className="mt-3 space-y-1 text-sm">
          <Row k="Net if sold raw" v={money(res.rawNet)} />
          <Row k="Net if graded PSA 10" v={money(res.gradedNet)} />
          <Row k="Grading upside" v={money(res.delta)} good={res.delta >= 0} />
        </div>
        <p className="text-mut text-xs mt-3">
          Grade when the upside clearly beats the time + risk of a wrong grade (~$20+ is a typical bar).
          Only the PSA-10 outcome is modeled — use a PSA-9 comp for a conservative read.
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
