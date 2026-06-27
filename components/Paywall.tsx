"use client";
import { supabase } from "@/lib/supabase";

const CHECKOUT =
  process.env.NEXT_PUBLIC_CHECKOUT_URL ||
  "https://dashboard.thegoatmonitor.com/checkout/plan_WsGQtBFfanSOi?d2c=true";

export default function Paywall({ name }: { name?: string }) {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center px-6 py-12">
      <div className="w-full max-w-md rounded-2xl border border-line bg-card p-7 text-center">
        <div className="text-4xl">🔒🐐</div>
        <h1 className="mt-3 text-2xl font-extrabold">
          {name ? `Hey ${name} — ` : ""}you're almost in
        </h1>
        <p className="mt-2 text-sm text-mut">
          You signed in, but we don&apos;t see an active GOAT Cards membership on your Discord yet.
          Membership unlocks the live drop radar, the buy/sell tools, and your cloud collection.
        </p>

        <div className="my-5 rounded-xl border border-goat bg-card2 p-5">
          <div className="text-3xl font-extrabold">
            $5<span className="text-base font-medium text-mut">/month</span>
          </div>
          <ul className="mx-auto mt-3 space-y-1.5 text-left text-sm text-mut">
            <li>✅ Live drops from all our monitors</li>
            <li>✅ Should-I-Buy, Sell-Timing & Grade tools</li>
            <li>✅ Cloud collection + portfolio P/L</li>
            <li>✅ Full GOAT Cards Discord access</li>
          </ul>
          <a
            href={CHECKOUT}
            target="_blank"
            rel="noopener noreferrer"
            className="mt-4 block w-full rounded-xl bg-goat px-6 py-3 font-bold text-[#1a1206]"
          >
            Become a member →
          </a>
        </div>

        <p className="text-xs text-mut">
          Already paid? Make sure you signed in with the Discord account that has your membership,
          then{" "}
          <button
            onClick={() => location.reload()}
            className="underline"
          >
            refresh
          </button>
          .
        </p>
        <button
          onClick={() => supabase?.auth.signOut()}
          className="mt-4 rounded-lg border border-line px-4 py-2 text-xs text-mut"
        >
          Sign out
        </button>
      </div>
    </div>
  );
}
