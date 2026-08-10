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
71 Legendary + 23 Mythical = **94**. Shiny exists: **69**. At least one true RNG hunt ever: **61**.
Currently huntable (Aug 2026): **56**. Historical-only: **5**. Guaranteed/event-only shiny: **8**.
Never legitimately shiny: **25**. (Ultra Beasts tracked separately: 11 of which 9 huntable; plus 12 alternate-form rows.)

## Obtainment channels (collection tracker)
Each shiny is tagged by how it can be obtained, so the web tracker can offer the right toggles:
**Home OT** (self-caught main-series shiny) · **Home Reward** (HOME Pokédex-completion reward: Meloetta, Keldeo,
Meltan, Volcanion) · **Home Event** (guaranteed-shiny distribution — 19 species incl. shiny beasts, Tapus, Zacian/
Zamazenta, Diancie, Genesect, Zeraora, Celebi, Silvally, Galarian birds, Koraidon/Miraidon) · **GO** (shiny in Pokémon GO).
