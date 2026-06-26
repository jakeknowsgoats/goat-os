import { supabase } from "./supabase";

export type Item = {
  id: string;
  name: string;
  type: string;
  qty: number;
  cost: number;
  comp: number;
  release: string | null;
  acquired: string;
};

export type NewItem = Omit<Item, "id" | "acquired">;

const LKEY = "goat_collection_v1";

async function uid(): Promise<string | null> {
  if (!supabase) return null;
  const { data } = await supabase.auth.getUser();
  return data.user?.id ?? null;
}

function localList(): Item[] {
  if (typeof window === "undefined") return [];
  try {
    return JSON.parse(localStorage.getItem(LKEY) || "[]");
  } catch {
    return [];
  }
}
function localSave(items: Item[]) {
  try {
    localStorage.setItem(LKEY, JSON.stringify(items));
  } catch {
    /* ignore */
  }
}

/** True when the user is signed in and data is syncing to the cloud. */
export async function isSynced(): Promise<boolean> {
  return (await uid()) !== null;
}

export async function listItems(): Promise<Item[]> {
  const u = await uid();
  if (u && supabase) {
    const { data } = await supabase
      .from("collections")
      .select("*")
      .order("created_at", { ascending: true });
    return (data ?? []) as Item[];
  }
  return localList();
}

export async function addItem(it: NewItem): Promise<void> {
  const u = await uid();
  if (u && supabase) {
    await supabase.from("collections").insert({ ...it, user_id: u });
    return;
  }
  const items = localList();
  items.push({
    ...it,
    id: `${Date.now()}-${Math.floor(Math.random() * 1e6)}`,
    acquired: new Date().toISOString().slice(0, 10),
  });
  localSave(items);
}

export async function updateItem(id: string, patch: Partial<Item>): Promise<void> {
  const u = await uid();
  if (u && supabase) {
    await supabase.from("collections").update(patch).eq("id", id);
    return;
  }
  localSave(localList().map((x) => (x.id === id ? { ...x, ...patch } : x)));
}

export async function removeItem(id: string): Promise<void> {
  const u = await uid();
  if (u && supabase) {
    await supabase.from("collections").delete().eq("id", id);
    return;
  }
  localSave(localList().filter((x) => x.id !== id));
}
