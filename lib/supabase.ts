import { createClient, SupabaseClient } from "@supabase/supabase-js";

const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
const key = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

// Null when keys aren't set — the app then runs in local-only mode (no cloud sync).
export const supabase: SupabaseClient | null =
  url && key ? createClient(url, key) : null;

export const cloudEnabled = !!supabase;
