"use client";
import { useEffect, useState } from "react";
import DropRadar from "@/components/DropRadar";
import BuyTool, { BuyPrefill } from "@/components/BuyTool";
import SellTool from "@/components/SellTool";
import Collection from "@/components/Collection";
import GradeTool from "@/components/GradeTool";
import Landing from "@/components/Landing";
import Paywall from "@/components/Paywall";
import { addItem } from "@/lib/collection";
import { supabase } from "@/lib/supabase";

type Tab = "radar" | "buy" | "sell" | "coll" | "grade";
const TABS: { id: Tab; label: string }[] = [
  { id: "radar", label: "📡 Drop Radar" },
  { id: "buy", label: "🧮 Should-I-Buy" },
  { id: "sell", label: "⏱️ Sell Timing" },
  { id: "coll", label: "📦 Collection" },
  { id: "grade", label: "🎖️ Grade-or-Sell" },
];

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function discordIdOf(user: any): string | null {
  const id = user?.identities?.find((i: any) => i.provider === "discord")?.id;
  return id || user?.user_metadata?.provider_id || user?.user_metadata?.sub || null;
}
// eslint-disable-next-line @typescript-eslint/no-explicit-any
function nameOf(user: any): string {
  return user?.user_metadata?.full_name || user?.user_metadata?.name || user?.email || "";
}

export default function Home() {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const [user, setUser] = useState<any | null | undefined>(undefined); // undefined = loading
  const [member, setMember] = useState<boolean | null>(null);
  const [tier, setTier] = useState<string | null>(null);
  const [tab, setTab] = useState<Tab>("radar");
  const [prefill, setPrefill] = useState<BuyPrefill>(null);

  useEffect(() => {
    if (!supabase) {
      setUser(null);
      return;
    }
    supabase.auth.getUser().then(({ data }) => setUser(data.user ?? null));
    const { data: l } = supabase.auth.onAuthStateChange((_e, s) => setUser(s?.user ?? null));
    return () => l.subscription.unsubscribe();
  }, []);

  useEffect(() => {
    if (user === undefined) return;
    if (!user) {
      setMember(null);
      return;
    }
    const did = discordIdOf(user);
    if (!did) {
      setMember(false);
      return;
    }
    fetch(`/api/membership?discordId=${did}`)
      .then((r) => r.json())
      .then((d) => {
        setMember(!!d.member);
        setTier(d.tier ?? null);
      })
      .catch(() => setMember(false));
  }, [user]);

  function scoreFromDrop(name: string, price: number) {
    setPrefill({ name, retail: price, comp: +(price * 1.5).toFixed(2) });
    setTab("buy");
  }
  async function ownDrop(name: string, price: number) {
    await addItem({ name, type: "Sealed", qty: 1, cost: price, comp: price, release: null });
    setTab("coll");
  }

  // --- gating ---
  if (supabase) {
    if (user === undefined) return <Splash text="Loading…" />;
    if (!user) return <Landing />;
    if (member === null) return <Splash text="Checking your membership…" />;
    if (!member) return <Paywall name={nameOf(user).split("#")[0]} />;
  }

  // --- the member app ---
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
        {user && (
          <div className="flex items-center gap-2 text-sm">
            {tier && (
              <span className="rounded-full border border-goat bg-card2 px-2 py-0.5 text-xs font-semibold text-goat2">
                {tier}
              </span>
            )}
            <span className="text-mut">{nameOf(user)}</span>
            <button
              onClick={() => supabase?.auth.signOut()}
              className="rounded border border-line px-2 py-1 text-xs"
            >
              Sign out
            </button>
          </div>
        )}
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
          <Section title="Drop Radar" sub="Live drops from your monitors. Tap a store to turn its alerts on/off.">
            <DropRadar onScore={scoreFromDrop} onOwn={ownDrop} />
          </Section>
        )}
        {tab === "buy" && (
          <Section title="Should-I-Buy" sub="Enter the drop + live comp, rate the 5 factors, get a verdict.">
            <BuyTool prefill={prefill} />
          </Section>
        )}
        {tab === "sell" && (
          <Section title="Sell Timing" sub="When to exit a hold — phase + action vs today's date.">
            <SellTool />
          </Section>
        )}
        {tab === "coll" && (
          <Section title="Collection" sub="Your holdings, valued live. Cost basis from the drop you bought.">
            <Collection active={tab === "coll"} />
          </Section>
        )}
        {tab === "grade" && (
          <Section title="Grade-or-Sell" sub="Grade a raw card or sell as-is? Real 2026 grading math.">
            <GradeTool />
          </Section>
        )}
      </main>
    </div>
  );
}

function Splash({ text }: { text: string }) {
  return (
    <div className="flex min-h-screen items-center justify-center text-mut">
      <div className="text-center">
        <div className="mb-2 text-3xl">🐐</div>
        {text}
      </div>
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
