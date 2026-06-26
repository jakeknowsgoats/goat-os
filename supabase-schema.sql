-- GOAT OS — Supabase schema (Phase 3)
-- Run this in your Supabase project: SQL Editor → New query → paste → Run.

-- Each member's collection. Row Level Security ensures users only see their own rows.
create table if not exists public.collections (
  id          uuid primary key default gen_random_uuid(),
  user_id     uuid not null references auth.users (id) on delete cascade,
  name        text not null,
  type        text not null default 'Sealed',
  qty         integer not null default 1,
  cost        numeric not null default 0,
  comp        numeric not null default 0,
  release     date,
  acquired    date not null default now(),
  created_at  timestamptz not null default now()
);

alter table public.collections enable row level security;

create policy "owner can read"   on public.collections for select using (auth.uid() = user_id);
create policy "owner can insert" on public.collections for insert with check (auth.uid() = user_id);
create policy "owner can update" on public.collections for update using (auth.uid() = user_id);
create policy "owner can delete" on public.collections for delete using (auth.uid() = user_id);

-- Optional: live drops table (Moonitor can write here instead of using MOONITOR_DROPS_URL).
create table if not exists public.drops (
  id         uuid primary key default gen_random_uuid(),
  store      text not null,
  name       text not null,
  price      numeric not null,
  tag        text,
  url        text,
  created_at timestamptz not null default now()
);
alter table public.drops enable row level security;
create policy "drops are public read" on public.drops for select using (true);
