# Phase 3 Setup — Accounts, Cloud Sync & Live Drops

Phase 3 turns the `goat-os` app into a real product: **members log in**, their **collection syncs to the cloud** (across devices), and **drops come from a live feed**. It's built so it **still runs with no setup** (local-only mode) — you add the cloud pieces when ready.

> Note: Phase 3 needs a **server** (login + database + live API), so it runs as a hosted Next.js app — not the drag-and-drop single file. The single-file version (`goat-os-mvp`) stays as your quick demo.

---

## What's new in the code
- **Login** (email magic-link) in the header — `components/AuthButton.tsx`
- **Cloud collection** — `lib/collection.ts` saves to Supabase when signed in, to the browser otherwise
- **Synced Collection tab** — `components/Collection.tsx` (live valuation, P/L, concentration, per-item sell-timing)
- **Grade-or-Sell tab** — `components/GradeTool.tsx`
- **Live drops API** — `app/api/drops/route.ts` reads `MOONITOR_DROPS_URL`, falls back to samples
- **Database schema** — `supabase-schema.sql` (with per-user security)

---

## Run it locally (works now, no keys)
```bash
npm install
npm run dev      # http://localhost:3000  → everything works in local mode
```

---

## Turn on the cloud (≈15 min)

### 1) Create the database (Supabase)
1. Sign up at **supabase.com** → **New project** (free). Pick a password, wait ~2 min.
2. Left menu → **SQL Editor** → **New query** → paste the contents of **`supabase-schema.sql`** → **Run**. (Creates the `collections` table + security.)
3. Left menu → **Project Settings → API** → copy two values: the **Project URL** and the **anon public key**.
4. **Authentication → Providers → Email** → make sure **Email** is enabled (magic link is on by default).

### 2) Add your keys
In the `goat-os` folder, copy `.env.example` to **`.env.local`** and fill in:
```
NEXT_PUBLIC_SUPABASE_URL=...your Project URL...
NEXT_PUBLIC_SUPABASE_ANON_KEY=...your anon key...
```
Restart `npm run dev`. Now the header shows a **Sign in** box — log in with your email, and your collection saves to the cloud. 🎉

### 3) (Optional) Live drops
Pick one:
- **Easiest:** set `MOONITOR_DROPS_URL` in `.env.local` to a URL on your Moonitor backend that returns `{ "drops": [ {store,name,price,tag,url}, ... ] }`.
- **Or:** have Moonitor insert rows into the Supabase `drops` table (schema included) and I'll point the API at it.

---

## Deploy it (server host needed)
Since Phase 3 has login + a database, use a host that runs Next.js (not drag-drop). Easiest options:
- **Netlify (full):** create a free GitHub repo, push `goat-os`, then on Netlify **"Import from Git"** → it auto-detects Next.js. Add your env vars in Netlify → Site settings → Environment. (This is different from the drag-drop "Drop" — it runs the server.)
- **Render:** New → **Web Service** → connect the repo → build `npm run build`, start `npm start` → add env vars.
- **Your Virtualmin server:** install Node, `npm run build`, run `npm start` with **PM2**, and reverse-proxy your subdomain to port 3000 (I can give exact commands).

Then point **os.thegoatmonitor.com** at whichever host.

---

## What I need from you to finish Phase 3
1. **Create the Supabase project** and paste me (or into `.env.local`) the **Project URL + anon key**. *(I can't create the account or hold keys.)*
2. **Pick a host** (Netlify-from-Git, Render, or Virtualmin+Node) — tell me which and I'll give you the exact click-by-click.
3. **Drops:** either a **Moonitor feed URL**, or say "use the Supabase drops table" and I'll wire it.

Once I have #1 and #2, the synced, logged-in site goes live.
