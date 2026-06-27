-- GOAT OS — Web Push schema. Run in Supabase SQL Editor (New query → paste → Run).

-- Each browser/phone subscription, tied to a member + their store preferences.
create table if not exists public.push_subs (
  endpoint   text primary key,
  user_id    uuid references auth.users (id) on delete cascade,
  p256dh     text not null,
  auth       text not null,
  stores     text[] not null default '{}',
  created_at timestamptz not null default now()
);
alter table public.push_subs enable row level security;
create policy "own subs read"   on public.push_subs for select using (auth.uid() = user_id);
create policy "own subs insert" on public.push_subs for insert with check (auth.uid() = user_id);
create policy "own subs update" on public.push_subs for update using (auth.uid() = user_id);
create policy "own subs delete" on public.push_subs for delete using (auth.uid() = user_id);

-- Tracks which drops have already been pushed (so members aren't spammed twice).
-- Server-only: no RLS policies, so only the service role (the sender) can touch it.
create table if not exists public.push_state (
  id   text primary key,
  seen text[] not null default '{}'
);
alter table public.push_state enable row level security;
