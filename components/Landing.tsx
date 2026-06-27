"use client";
import { supabase } from "@/lib/supabase";

function signInWithDiscord() {
  if (!supabase) return;
  supabase.auth.signInWithOAuth({
    provider: "discord",
    options: {
      redirectTo: typeof window !== "undefined" ? window.location.origin : undefined,
    },
  });
}

const FEATURES = [
  { icon: "📡", title: "Live drop radar", body: "Every buyable restock from Target, Walmart, Pokémon Center, Best Buy & more — the moment it goes live, straight from our monitors." },
  { icon: "🧮", title: "Should-I-Buy engine", body: "Instant verdict on any drop — net margin after fees, ROI, and BUY-FLIP / HOLD / PASS. Stop guessing." },
  { icon: "⏱️", title: "Sell-timing + Grade-or-Sell", body: "Know exactly when to flip vs hold, and whether a card is worth grading in 2026." },
  { icon: "📦", title: "Your collection, valued live", body: "Track every box & card, see real-time P/L, and your cost basis auto-logs from the drop you bought." },
];

export default function Landing() {
  return (
    <div className="min-h-screen">
      <header className="flex items-center gap-3 px-6 py-5">
        <div className="text-3xl">🐐</div>
        <div className="font-bold">The Goat Monitor — Collector OS</div>
        <button
          onClick={signInWithDiscord}
          className="ml-auto rounded-lg border border-line px-4 py-2 text-sm font-bold"
        >
          Sign in
        </button>
      </header>

      <section className="mx-auto max-w-3xl px-6 pb-10 pt-10 text-center">
        <div className="mb-3 inline-block rounded-full border border-line bg-card2 px-3 py-1 text-xs text-mut">
          For serious card collectors & resellers
        </div>
        <h1 className="text-4xl font-extrabold leading-tight md:text-5xl">
          Find the drop. Know what to buy.<br />Know when to sell.
        </h1>
        <p className="mx-auto mt-4 max-w-xl text-mut">
          GOAT Cards turns our real-time restock monitors into one tool: live drops, instant buy/sell
          intelligence, and a collection that values itself — all in one place.
        </p>
        <div className="mt-7 flex flex-col items-center gap-3">
          <button
            onClick={signInWithDiscord}
            className="rounded-xl bg-[#5865F2] px-7 py-3.5 text-lg font-bold text-white shadow-lg"
          >
            Continue with Discord →
          </button>
          <div className="text-xs text-mut">Members get full access · just $5/month</div>
        </div>
      </section>

      <section className="mx-auto grid max-w-4xl gap-4 px-6 pb-12 md:grid-cols-2">
        {FEATURES.map((f) => (
          <div key={f.title} className="rounded-xl border border-line bg-card p-5">
            <div className="text-2xl">{f.icon}</div>
            <div className="mt-2 font-bold">{f.title}</div>
            <div className="mt-1 text-sm text-mut">{f.body}</div>
          </div>
        ))}
      </section>

      <section className="mx-auto max-w-md px-6 pb-16">
        <div className="rounded-2xl border border-goat bg-card p-6 text-center">
          <div className="text-sm font-semibold uppercase tracking-wide text-goat2">Membership</div>
          <div className="mt-1 text-4xl font-extrabold">$5<span className="text-lg font-medium text-mut">/month</span></div>
          <ul className="mx-auto mt-4 space-y-1.5 text-left text-sm text-mut">
            <li>✅ Live drop radar from all our monitors</li>
            <li>✅ Buy / sell / grade decision tools</li>
            <li>✅ Cloud collection + portfolio tracking</li>
            <li>✅ The full GOAT Cards Discord community</li>
          </ul>
          <button
            onClick={signInWithDiscord}
            className="mt-5 w-full rounded-xl bg-goat px-6 py-3 font-bold text-[#1a1206]"
          >
            Continue with Discord →
          </button>
          <div className="mt-2 text-xs text-mut">
            Already a member? Sign in with the Discord account that holds your membership.
          </div>
        </div>
      </section>

      <footer className="border-t border-line py-6 text-center text-xs text-mut">
        🐐 The Goat Monitor · thegoatmonitor.com
      </footer>
    </div>
  );
}
