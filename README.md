# GOAT OS — Collector OS (Phase 1)

The production starter for thegoatmonitor.com. Next.js + TypeScript + Tailwind.
Includes a working **Drop Radar**, **Should-I-Buy**, and **Sell-Timing** tool, wired to the verified GOAT buy/sell engine.

## Run it locally
```bash
npm install
npm run dev
```
Open http://localhost:3000

## Build for production
```bash
npm run build
npm start
```

## How it's wired
- `lib/engine.ts` — `scoreBuy()` + `sellTiming()` (verified vs BUY_SELL_TOOL.xlsx)
- `lib/fees.ts` — marketplace fee table
- `lib/drops.ts` — sample drops feed
- `app/api/drops/route.ts` — serves drops. Set `MOONITOR_DROPS_URL` in `.env.local` to your live feed.
- `components/` — DropRadar, BuyTool, SellTool, VerdictBadge
- `app/page.tsx` — the dashboard (tab nav)

## Next steps (see ../BUILD_GUIDE.md)
1. Point `MOONITOR_DROPS_URL` at your Moonitor backend (or push drops into Supabase).
2. Add Whop login + tier gating.
3. Deploy to Vercel, connect thegoatmonitor.com.
4. Phase 2: Collection manager + cost-basis-from-the-drop.
