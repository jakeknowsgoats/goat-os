"use client";
import { useEffect, useState } from "react";
import { scoreBuy, Ratings } from "@/lib/engine";
import { FEES, MARKETPLACES } from "@/lib/fees";
import VerdictBadge from "./VerdictBadge";

const money = (n: number) =>
  "$" + n.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const pct = (n: number) => (n * 100).toFixed(1) + "%";

const FACTORS: { key: keyof Ratings; label: string }[] = [
  { key: "rookie", label: "Rookie / Chase strength" },
  { key: "scarcity", label: "Print / Scarcity" },
  { key: "brand", label: "Brand tier" },
  { key: "velocity", label: "Sales velocity / liquidity" },
  { key: "hype", label: "Hype / catalyst" },
];

export type BuyPrefill = { name: string; retail: number; comp: number } | null;

export default function BuyTool({ prefill }: { prefill: BuyPrefill }) {
  const [name, setName] = useState("2025 Donruss Optic NFL Blaster");
  const [retail, setRetail] = useState(29.99);
  const [comp, setComp] = useState(45);
  const [mkt, setMkt] = useState("eBay");
  const [r, setR] = useState<Ratings>({ rookie: 4, scarcity: 2, brand: 4, velocity: 4, hype: 4 });

  useEffect(() => {
    if (prefill) {
      setName(prefill.name);
      setRetail(prefill.retail);
      setComp(prefill.comp);
    }
  }, [prefill]);

  const [fee, po] = FEES[mkt] ?? [0, 0];
  const res = scoreBuy(retail, comp, fee, po, r);

  const label = "block text-xs uppercase tracking-wide text-mut font-semibold mt-3 mb-1";
  const input =
    "w-full bg-card2 border border-line rounded-lg px-3 py-2 text-[#e7e9ee]";

  return (
    <div className="grid gap-4 md:grid-cols-2">
      <div className="rounded-xl border border-line bg-card p-4">
        <label className={label}>Product</label>
        <input className={input} value={name} onChange={(e) => setName(e.target.value)} />
        <div className="grid grid-cols-2 gap-3">
          <div>
            <label className={label}>Retail $ / unit</label>
            <input type="number" className={input} value={retail}
              onChange={(e) => setRetail(+e.target.value)} />
          </div>
          <div>
            <label className={label}>Live comp $</label>
            <input type="number" className={input} value={comp}
              onChange={(e) => setComp(+e.target.value)} />
          </div>
        </div>
        <label className={label}>Marketplace</label>
        <select className={input} value={mkt} onChange={(e) => setMkt(e.target.value)}>
          {MARKETPLACES.map((m) => (
            <option key={m} value={m}>{m}</option>
          ))}
        </select>
        {FACTORS.map((f) => (
          <div key={f.key}>
            <label className={label}>{f.label}</label>
            <div className="flex items-center gap-3">
              <input type="range" min={1} max={5} value={r[f.key]} className="w-full"
                onChange={(e) => setR({ ...r, [f.key]: +e.target.value })} />
              <span className="w-4 text-center font-bold text-goat2">{r[f.key]}</span>
            </div>
          </div>
        ))}
      </div>

      <div className="rounded-xl border border-line bg-card p-4">
        <div className="text-center">
          <div className="text-mut text-sm">{name}</div>
          <div className="my-2"><VerdictBadge verdict={res.verdict} /></div>
          <div className="text-4xl font-extrabold">Score {res.score}/100</div>
        </div>
        <div className="mt-3 space-y-1 text-sm">
          <Row k="Net sale (after fees)" v={money(res.net)} />
          <Row k="Margin / unit" v={money(res.margin)} good={res.margin >= 0} />
          <Row k="ROI" v={pct(res.roi)} />
          <Row k="Fee applied" v={`${pct(fee)} + ${money(po)}`} />
        </div>
        <p className="text-mut text-xs mt-3">
          Margin (up to 40 pts from ROI) + Quality (up to 60 from your 1-5 ratings).
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
