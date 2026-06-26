"use client";
import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabase";

export default function AuthButton() {
  const [email, setEmail] = useState("");
  const [user, setUser] = useState<string | null>(null);
  const [sent, setSent] = useState(false);

  useEffect(() => {
    if (!supabase) return;
    supabase.auth.getUser().then(({ data }) => setUser(data.user?.email ?? null));
    const { data: listener } = supabase.auth.onAuthStateChange((_e, s) =>
      setUser(s?.user?.email ?? null)
    );
    return () => listener.subscription.unsubscribe();
  }, []);

  if (!supabase)
    return <span className="text-xs text-mut">Local mode (add Supabase keys to sync)</span>;

  if (user)
    return (
      <div className="flex items-center gap-2 text-sm">
        <span className="text-mut">{user}</span>
        <button
          onClick={() => supabase!.auth.signOut()}
          className="rounded border border-line px-2 py-1 text-xs"
        >
          Sign out
        </button>
      </div>
    );

  return (
    <div className="flex items-center gap-2">
      <input
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="you@email.com"
        className="rounded border border-line bg-card2 px-2 py-1 text-sm"
      />
      <button
        onClick={async () => {
          if (!email) return;
          await supabase!.auth.signInWithOtp({ email });
          setSent(true);
        }}
        className="rounded bg-goat px-3 py-1 text-sm font-bold text-[#1a1206]"
      >
        {sent ? "Check email ✉️" : "Sign in"}
      </button>
    </div>
  );
}
