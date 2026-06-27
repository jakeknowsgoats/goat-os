import { supabase } from "./supabase";

const VAPID_PUBLIC = process.env.NEXT_PUBLIC_VAPID_PUBLIC_KEY || "";

function toUint8(base64String: string): Uint8Array {
  const padding = "=".repeat((4 - (base64String.length % 4)) % 4);
  const base64 = (base64String + padding).replace(/-/g, "+").replace(/_/g, "/");
  const raw = atob(base64);
  const arr = new Uint8Array(raw.length);
  for (let i = 0; i < raw.length; i++) arr[i] = raw.charCodeAt(i);
  return arr;
}

export function pushSupported(): boolean {
  return (
    typeof window !== "undefined" &&
    "serviceWorker" in navigator &&
    "PushManager" in window &&
    "Notification" in window &&
    !!VAPID_PUBLIC
  );
}

export async function pushIsOn(): Promise<boolean> {
  if (!pushSupported()) return false;
  const reg = await navigator.serviceWorker.getRegistration();
  const sub = await reg?.pushManager.getSubscription();
  return !!sub;
}

export async function enablePush(stores: string[]): Promise<{ ok: boolean; error?: string }> {
  if (!pushSupported()) return { ok: false, error: "unsupported" };
  if (!supabase) return { ok: false, error: "no-auth" };
  const perm = await Notification.requestPermission();
  if (perm !== "granted") return { ok: false, error: "denied" };
  const reg = await navigator.serviceWorker.register("/sw.js");
  await navigator.serviceWorker.ready;
  const sub = await reg.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: toUint8(VAPID_PUBLIC),
  });
  const json = sub.toJSON();
  const { data: u } = await supabase.auth.getUser();
  await supabase.from("push_subs").upsert(
    {
      user_id: u.user?.id,
      endpoint: json.endpoint,
      p256dh: json.keys?.p256dh,
      auth: json.keys?.auth,
      stores,
    },
    { onConflict: "endpoint" }
  );
  return { ok: true };
}

export async function updatePushStores(stores: string[]): Promise<void> {
  if (!pushSupported() || !supabase) return;
  const reg = await navigator.serviceWorker.getRegistration();
  const sub = await reg?.pushManager.getSubscription();
  if (!sub) return;
  await supabase.from("push_subs").update({ stores }).eq("endpoint", sub.toJSON().endpoint);
}

export async function disablePush(): Promise<void> {
  if (!pushSupported() || !supabase) return;
  const reg = await navigator.serviceWorker.getRegistration();
  const sub = await reg?.pushManager.getSubscription();
  if (!sub) return;
  const endpoint = sub.toJSON().endpoint;
  await sub.unsubscribe();
  if (endpoint) await supabase.from("push_subs").delete().eq("endpoint", endpoint);
}
