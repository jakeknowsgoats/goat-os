"use client";
import { useState } from "react";
import DropRadar from "@/components/DropRadar";
import BuyTool, { BuyPrefill } from "@/components/BuyTool";
import SellTool from "@/components/SellTool";
import Collection from "@/components/Collection";
import GradeTool from "@/components/GradeTool";
import AuthButton from "@/components/AuthButton";
import { addItem } from "@/lib/collection";

type Tab = "radar" | "buy" | "sell" | "coll" | "grade";

const TABS: { id: Tab; label: string }[] = [
  { id: "radar", label: "📡 Drop Radar" },
  { id: "buy", label: "🧮 Should-I-Buy" },
  { id: "sell", label: "⏱️ Sell Timing" },
  { id: "coll", label: "📦 Collection" },
  { id: "grade", label: "🎖️ Grade-or-Sell" },
];

export default function Home() {
  const [tab, setTab] = useState<Tab>("radar");
  const [prefill, setPrefill] = useState<BuyPrefill>(null);

  function scoreFromDrop(name: string, price: number) {
    setPrefill({ name, retail: price, comp: +(price * 1.5).toFixed(2) });
    setTab("buy");
  }
  async function ownDrop(name: string, price: number) {
    await addItem({ name, type: "Sealed", qty: 1, cost: price, comp: price, release: null });
    setTab("coll");
  }

  return (
    <div>
      <header className="flex flex-wrap items-center gap-3 border-b border-line px-6 py-4">
        <div className="text-3xl">🐐</div>
        <div className="mr-auto">
          <h1 className="text-[17px] font-bold">The Goat Monitor — Collector OS</h1>
          <div className="text-xs text-mut">
            Drop Radar · Should-I-Buy · Sell-Timing · Collection · Grade-or-Sell
          </div>
        </div>
        <AuthButton />
      </header>

      <nav className="flex flex-wrap gap-1.5 border-b border-line px-6 py-3">
        {TABS.map((t) => (
          <button
            key={t.id}
            onClick={() => setTab(t.id)}
            className={`rounded-lg border px-3.5 py-2 font-semibold ${
              tab === t.id ? "border-goat bg-goat text-[#1a1206]" : "border-line bg-card text-mut"
            }`}
          >
            {t.label}
          </button>
        ))}
      </nav>

      <main className="mx-auto max-w-5xl px-6 py-6">
        {tab === "radar" && (
          <Section title="Drop Radar" sub='Live buyable drops (set MOONITOR_DROPS_URL for your real feed). "Score it" runs the buy math; "+ Own" logs it to your collection at this cost.'>
            <DropRadar onScore={scoreFromDrop} onOwn={ownDrop} />
          </Section>
        )}
        {tab === "buy" && (
          <Section title="Should-I-Buy" sub="Enter the drop + the live comp, rate the 5 factors, get a verdict. Same engine as the GOAT buy/sell spreadsheet.">
            <BuyTool prefill={prefill} />
          </Section>
        )}
        {tab === "sell" && (
          <Section title="Sell Timing" sub="When should you exit a hold? Phase & action update against today's date using the 5-phase scarcity clock.">
            <SellTool />
          </Section>
        )}
        {tab === "coll" && (
          <Section title="Collection" sub="Your holdings, valued live. Cost basis comes straight from the drop you bought — the GOAT moat. Sign in to sync across devices.">
            <Collection active={tab === "coll"} />
          </Section>
        )}
        {tab === "grade" && (
          <Section title="Grade-or-Sell" sub="Should you grade a raw card or sell it as-is? Real 2026 grading-cost math.">
            <GradeTool />
          </Section>
        )}

        <div className="mt-6 text-center text-xs text-mut">
          Phase 3 — accounts + cloud sync + live feed. See PHASE3_SETUP.md.
        </div>
      </main>
    </div>
  );
}

function Section({ title, sub, children }: { title: string; sub: string; children: React.ReactNode }) {
  return (
    <section>
      <h2 className="text-xl font-bold">{title}</h2>
      <p className="mb-4 text-[13px] text-mut">{sub}</p>
      {children}
    </section>
  );
}
