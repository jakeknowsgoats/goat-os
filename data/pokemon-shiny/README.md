# Legendary & Mythical Pokémon — Shiny-Hunt Database

Complete database of every Legendary and Mythical Pokémon (Gens I–IX) and whether/where their
shiny form can be **legitimately shiny-hunted**, current as of **August 9, 2026** — including
**Pokémon GO as a first-class hunting platform** and the 2026 additions (Legends Z-A *Mega
Dimension* Hyperspace hunts, GO Shiny Solgaleo/Lunala, shiny Koraidon/Miraidon distribution,
HOME guaranteed-shiny dex rewards).

## Files
| File | What it is |
|---|---|
| `legendary_mythical_shiny_report.md` | Full human-readable report: computed summary, Part 1 master table, Part 2 per-Pokémon detail, 10 filtered lists, validation pass. |
| `legendary_mythical_shiny_master.csv` | One row per Pokémon, the 14-column master schema. |
| `legendary_mythical_shiny_master.xlsx` | Same data + **per-method columns** (Dynamax Adventure, Ultra Wormhole, Ramanas Park, SwSh static, Z-A Hyperspace, GO raid/box/research…) with auto-filter + a `Legend` sheet. Built for filtering. |
| `sources.md` | Every source with access dates + the egress caveat + disputed-case notes. |
| `build_db.py` | The generator. All data lives here; all summary counts are **computed** (never hand-typed) with build-time integrity asserts. |

## Regenerate
```bash
pip install openpyxl
python3 build_db.py
```

## The distinction this database enforces (buckets A–E)
- **A — TRUE SHINY HUNT** (currently possible): roll/reset/raid/breed the RNG yourself.
- **E — hunt existed but NOT currently accessible** (discontinued service / expired event).
- **B — GUARANTEED SHINY REWARD** (HOME dex reward, GO Masterwork): *not* a hunt.
- **C — SHINY EVENT DISTRIBUTION** (predetermined shiny code/gift): *not* a hunt.
- **D — SHINY UNAVAILABLE**: no legitimate shiny ever obtainable.

## Headline counts (computed)
71 Legendary + 23 Mythical = **94**. Shiny exists: **65**. At least one true RNG hunt ever: **58**.
Currently huntable (Aug 2026): **54**. Historical-only: **4**. Guaranteed/event-only shiny: **7**.
Never legitimately shiny: **29**. (Ultra Beasts tracked separately: 11, of which 9 huntable.)
