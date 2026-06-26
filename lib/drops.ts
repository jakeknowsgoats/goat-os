export type Drop = {
  store: string;
  name: string;
  price: number;
  tag: string;
  url?: string;
};

// Sample feed for the Phase-1 demo. Phase 2 (Step 5) swaps this for the live Moonitor feed.
export const SAMPLE_DROPS: Drop[] = [
  { store: "Target", name: "2025 Donruss Optic NFL Blaster", price: 29.99, tag: "🏈 Football" },
  { store: "Topps", name: "Topps NOW — Darryn Peterson RC", price: 11.99, tag: "🏀 Basketball" },
  { store: "Amazon", name: "MTG Marvel Spider-Man Collector Box", price: 332.49, tag: "🃏 TCG" },
  { store: "Amazon", name: "MTG Marvel Super Heroes Bundle (preorder)", price: 74.99, tag: "🃏 TCG" },
  { store: "Walmart", name: "Pokémon Prismatic Evolutions Poster Collection", price: 19.87, tag: "⚡ Pokémon" },
  { store: "Pokémon Center", name: "151 Booster Bundle 2-Pack", price: 50.0, tag: "⚡ Pokémon" },
  { store: "Target", name: "2025 Topps Chrome Platinum Value Box", price: 24.99, tag: "⚾ Baseball" },
];
