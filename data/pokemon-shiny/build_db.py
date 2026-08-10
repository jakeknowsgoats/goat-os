#!/usr/bin/env python3
"""
Build the Legendary & Mythical Pokémon shiny-hunting database.

Emits into this directory:
  - legendary_mythical_shiny_master.csv
  - legendary_mythical_shiny_master.xlsx   (one Pokémon per row; per-method columns for filtering)
  - legendary_mythical_shiny_report.md      (Part 1 master table + Part 2 detailed entries + summary + filtered lists)
  - sources.md

ALL summary counts are COMPUTED from the dataset (never hand-typed), per the spec.
Data current as of 2026-08-09. See sources.md for per-source access dates and the
network/verification caveat (Bulbapedia/Serebii direct-fetch was egress-blocked; data
was gathered via web-search extracts of those + reachable secondary sources, cross-checked).

Category legend (the spec's A–E buckets are derived, not stored):
  A TRUE SHINY HUNT           -> rng_hunt True
  B GUARANTEED SHINY REWARD   -> a method with cat="B"
  C SHINY EVENT DISTRIBUTION  -> a method with cat="C"
  D SHINY UNAVAILABLE         -> shiny_exists False
  E SHINY EXISTS, NOT HUNTABLE NOW -> rng_hunt True and huntable_now False, OR shiny_exists and not huntable_now
"""

import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ACCESS_DATE = "2026-08-09"

# --- odds constants ---------------------------------------------------------
FULL = "1/4096"        # Gen 6+ full odds
CHARM = "1/1365"       # Gen 6+ full odds + Shiny Charm
FULL_OLD = "1/8192"    # Gen 2-5 full odds (no Shiny Charm existed pre-Gen5; ~1/2731 w/ charm in Gen5)
DA_B, DA_C = "1/300", "1/100"      # Dynamax Adventure (Charm DOES apply, incl. boss)
GO_R = "~1/20"                      # legendary/mega raid boss shiny (permaboosted)
GO_W = "~1/125"                     # Daily Adventure Incense / Mystery Box wild-style
ZA = "up to ~1/585"                 # Z-A Mega Dimension Hyperspace w/ Shiny Charm + Sparkling Power Lv3

METHOD_COLS = [
    "SwSh Dynamax Adventure",
    "USUM Ultra Wormhole",
    "BDSP Ramanas Park",
    "SwSh Static/Gift",
    "ORAS Mirage/Static",
    "Legends Z-A Hyperspace",
    "Other Main-Series (legacy/roamer/breeding)",
    "GO Raid (RNG)",
    "GO Wild/Box (RNG)",
    "GO Research (guaranteed)",
]


def M(game, encounter, locked, base, charm, charm_eff, accessible, cat, note=""):
    return dict(game=game, encounter=encounter, shiny_locked=locked, odds_base=base,
                odds_charm=charm, charm=charm_eff, accessible=accessible, cat=cat, note=note)


# --- reusable method builders ----------------------------------------------
def da():
    return M("Sword/Shield (Crown Tundra)", "Dynamax Adventure boss (soft-resettable reward)",
             False, DA_B, DA_C, "Yes (1/300 -> 1/100; applies to boss)", True, "A",
             "Requires Crown Tundra DLC; best modern odds")

def uw():
    return M("Ultra Sun/Ultra Moon", "Ultra Space Wilds static (soft-reset)", False, FULL, CHARM,
             "Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)", True, "A",
             "Requires 3DS cartridge (eShop closed Mar 2023)")

def rp():
    return M("Brilliant Diamond/Shining Pearl", "Ramanas Park slate static (soft-reset)", False,
             FULL, FULL, "No effect (BDSP Charm boosts Masuda eggs only)", True, "A",
             "Flat 1/4096 regardless of Charm")

def oras():
    return M("Omega Ruby/Alpha Sapphire", "Mirage Spot static / Soaring (soft-reset)", False,
             FULL, CHARM, "Yes (1/4096 -> 1/1365)", True, "A",
             "Requires 3DS cartridge (eShop closed Mar 2023)")

def go_raid(first, extra=""):
    return M("Pokémon GO", "Legendary 5-star raid (RNG per raid)", False, GO_R, "n/a",
             "n/a (GO has no Shiny Charm)", True, "A",
             f"Shiny since {first}; rotates through raids{('; ' + extra) if extra else ''}")

def go_mw(name, first):
    return M("Pokémon GO", f"{name} (guaranteed shiny reward)", False, "100% (guaranteed)", "n/a",
             "n/a", False, "B", f"Shiny since {first}; one guaranteed shiny, NOT rollable")

def za():
    return M("Legends: Z-A (Mega Dimension DLC, 2026)", "5-star Hyperspace Distortion (run-back reroll)",
             False, "~1/4096 base", ZA, "Yes; stacks with Sparkling Power Lv3 donut (-> ~1/585)", True, "A",
             "Post Main Mission 12; one of only 5 non-locked legendaries in Z-A")

def home_shiny(name, first, req):
    return M("Pokémon HOME", f"{name} dex-completion Mystery Gift (guaranteed shiny)", False,
             "100% (guaranteed)", "n/a", "n/a", True, "B", f"Since {first}; requires {req}")


# ============================================================================
# DATA
# ============================================================================
DATA = []

def add(**kw):
    DATA.append(kw)


# ---------- GENERATION I ----------
add(name="Articuno", gen="I", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(),
             M("Let's Go Pikachu/Eevee", "Overworld static (soft-reset)", False, FULL, CHARM,
               "Yes", True, "A", "Not shiny-locked in LGPE"),
             go_raid("Jul 2019")],
    go="Legendary raids (shiny since Jul 2019); ~1/20; rotates",
    notes="Kanto birds broadly huntable. Galarian Articuno (Gen 8) is a separate, shiny-locked static in SwSh but shiny via GO Daily Adventure Incense.")
add(name="Zapdos", gen="I", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(),
             M("Let's Go Pikachu/Eevee", "Overworld static (soft-reset)", False, FULL, CHARM, "Yes", True, "A"),
             go_raid("Jul 2019")],
    go="Legendary raids (shiny since Jul 2019); ~1/20; rotates",
    notes="See Articuno note re: Galarian form.")
add(name="Moltres", gen="I", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(),
             M("Let's Go Pikachu/Eevee", "Overworld static (soft-reset)", False, FULL, CHARM, "Yes", True, "A"),
             go_raid("Jul 2019")],
    go="Legendary raids (shiny since Jul 2019); ~1/20; rotates",
    notes="See Articuno note re: Galarian form.")
add(name="Mewtwo", gen="I", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[uw(), rp(),
             M("Let's Go Pikachu/Eevee", "Cerulean Cave static (soft-reset)", False, FULL, CHARM, "Yes", True, "A",
               "Not shiny-locked in LGPE"),
             M("Sword/Shield (Crown Tundra)", "Dynamax Adventure special boss", True, "n/a", "n/a", "n/a", True, "C",
               "Mewtwo's Dynamax Adventure appearance is SHINY-LOCKED (unlike other DA bosses)"),
             go_raid("Sep 16 2019", "Mega Mewtwo X/Y shiny debuted GO Fest 2026")],
    go="Legendary raids (shiny since Sep 2019); Mega X/Y shiny GO Fest 2026; ~1/20",
    notes="Huntable via USUM, Ramanas Park, LGPE, and GO raids. NOTE its Dynamax Adventure form is shiny-locked.")
add(name="Mew", gen="I", category="Mythical",
    shiny_exists=True, rng_hunt=True, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=False,
    methods=[M("Emerald (Japan, Old Sea Map)", "Faraway Island static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A",
               "The Old Sea Map (Japan-only, 2005) unlocks Faraway Island; that Mew is NOT shiny-locked -> genuine "
               "soft-reset hunt at 1/8192. Item never released in the West (historical)"),
             go_mw("Masterwork Research 'All-in-One #151'", "Jul 6 2023"),
             M("Other events", "Distribution", True, "n/a", "n/a", "n/a", False, "C",
               "Other event Mew are shiny/IV-locked")],
    go="Shiny via 'All-in-One #151' Masterwork (guaranteed; $5). Not RNG-huntable in GO.",
    notes="Correction: shiny Mew IS a (historical) self-catch hunt via the Japan-only Old Sea Map (Faraway Island, "
          "Emerald), 1/8192 — long discontinued. Also a guaranteed GO Masterwork shiny.")

# ---------- GENERATION II ----------
add(name="Raikou", gen="II", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(), oras(),
             M("Crystal (Virtual Console) / HGSS", "Roaming (DVs/PID lock on first sighting)", False,
               FULL_OLD, "n/a", "No charm pre-Gen6", False, "A",
               "Historical; save before first battle. VC eShop closed Mar 2023"),
             go_raid("Jun 29 2019")],
    go="Legendary raids (shiny since Jun 2019); ~1/20; rotates",
    notes="Legendary beasts huntable via many modern routes.")
add(name="Entei", gen="II", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(), oras(),
             M("Crystal (VC) / HGSS", "Roaming (locks on first sighting)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Historical; VC discontinued"),
             go_raid("Jul 14 2019")],
    go="Legendary raids (shiny since Jul 2019); ~1/20; rotates",
    notes="")
add(name="Suicune", gen="II", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(), oras(),
             M("Crystal (VC)", "Tin Tower static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Static in Crystal; VC discontinued (historical)"),
             go_raid("Aug 17 2019")],
    go="Legendary raids (shiny since Aug 2019); ~1/20; rotates",
    notes="Static (soft-resettable) in Crystal, roams in G/S.")
add(name="Lugia", gen="II", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(),
             M("Gen 3 (event) / HGSS / Crystal", "Navel Rock / Whirl Islands static (soft-reset)", False,
               FULL_OLD, "n/a", "No charm pre-Gen6", False, "A", "Gen3 Navel Rock needed MysticTicket (event over)"),
             go_raid("Mar 16 2018", "FIRST shiny legendary released in GO")],
    go="Legendary raids (shiny since Mar 2018 — first shiny legendary in GO); ~1/20",
    notes="Ramanas Park (Squall Slate, Shining Pearl).")
add(name="Ho-Oh", gen="II", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(),
             M("Gen 3 (event) / HGSS / Crystal", "Navel Rock / Tin Tower static (soft-reset)", False,
               FULL_OLD, "n/a", "No charm pre-Gen6", False, "A", "Gen3 Navel Rock needed MysticTicket (event over)"),
             go_raid("May 19 2018")],
    go="Legendary raids (shiny since May 2018); ~1/20; rotates",
    notes="Ramanas Park (Rainbow Slate, Brilliant Diamond).")
add(name="Celebi", gen="II", category="Mythical",
    shiny_exists=True, rng_hunt=True, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=False,
    methods=[M("Crystal (Virtual Console)", "GS Ball event static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A",
               "GS-Ball Celebi in VC Crystal is NOT shiny-locked -> genuine soft-reset hunt. eShop closed Mar 2023 (historical)"),
             go_mw("Special Research 'Distracted by Something Shiny' (re-run as Masterwork)", "Dec 14 2020")],
    go="Shiny via Special/Masterwork Research (guaranteed). Not RNG in GO.",
    notes="Rare Mythical with a real (historical) RNG hunt: VC Crystal GS-Ball Celebi. No longer accessible (VC discontinued).")

# ---------- GENERATION III ----------
for nm, first in [("Regirock", "Nov 2019"), ("Regice", "Nov 2019"), ("Registeel", "Nov 2019")]:
    add(name=nm, gen="III", category="Legendary",
        shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
        home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
        methods=[da(), uw(), rp(), oras(),
                 M("Sword/Shield (Crown Tundra)", "Regi puzzle static (soft-reset)", False, FULL, CHARM,
                   "Yes (1/4096 -> 1/1365)", True, "A", "Crown Tundra ruins; not shiny-locked"),
                 M("Ruby/Sapphire/Emerald", "Sealed chamber static (soft-reset)", False, FULL_OLD, "n/a",
                   "No charm pre-Gen6", False, "A", "Historical cartridge"),
                 go_raid(first)],
        go=f"Legendary raids (shiny since {first}); ~1/20; rotates",
        notes="One of the most route-rich hunts (DA, USUM, BDSP, ORAS, SwSh static, GO).")
add(name="Latias", gen="III", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), oras(), za(),
             M("Ruby/Sapphire/Emerald", "Roaming / Southern Island static", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Historical"),
             M("Scarlet/Violet (Indigo Disk)", "Static", True, "n/a", "n/a", "n/a", True, "C",
               "SHINY-LOCKED in SV DLC"),
             go_raid("Feb 22 2019")],
    go="Legendary raids (shiny since Feb 2019); ~1/20; rotates",
    notes="NEW 2026: shiny-huntable in Legends Z-A Mega Dimension Hyperspace Distortions (first found shiny there).")
add(name="Latios", gen="III", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), oras(), za(),
             M("Ruby/Sapphire/Emerald", "Roaming / Southern Island static", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Historical"),
             M("Scarlet/Violet (Indigo Disk)", "Static", True, "n/a", "n/a", "n/a", True, "C", "SHINY-LOCKED in SV DLC"),
             go_raid("Apr 15 2019", "Shadow Latios shiny in 2026 Shadow Raids")],
    go="Legendary raids (shiny since Apr 2019); ~1/20; rotates",
    notes="NEW 2026: shiny-huntable in Legends Z-A Mega Dimension Hyperspace Distortions.")
add(name="Kyogre", gen="III", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(),
             M("Ruby/Sapphire/Emerald", "Story static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Historical; ORAS Kyogre is shiny-LOCKED"),
             go_raid("2019 (exact date disputed)")],
    go="Legendary raids (shiny 2019); ~1/20; rotates",
    notes="ORAS weather-trio encounter is shiny-locked; Gen3 originals + DA/USUM/BDSP/GO are huntable.")
add(name="Groudon", gen="III", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(),
             M("Ruby/Sapphire/Emerald", "Story static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Historical; ORAS Groudon shiny-LOCKED"),
             go_raid("Jan 15 2019")],
    go="Legendary raids (shiny since Jan 2019); ~1/20; rotates",
    notes="ORAS encounter shiny-locked; huntable via DA/USUM/BDSP/GO + Gen3 originals.")
add(name="Rayquaza", gen="III", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(),
             M("Ruby/Sapphire/Emerald", "Sky Pillar static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Historical; ORAS Rayquaza shiny-LOCKED (Delta Episode)"),
             go_raid("2019", "Mega Rayquaza shiny available")],
    go="Legendary raids (shiny 2019); Mega Rayquaza shiny; ~1/20",
    notes="Not in BDSP. ORAS story encounter shiny-locked. Huntable via DA, USUM, GO, Gen3.")
add(name="Jirachi", gen="III", category="Mythical",
    shiny_exists=True, rng_hunt=True, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=False,
    methods=[M("Colosseum Bonus Disc (WISHMKR)", "Distribution encounter (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A",
               "US 'WISHMKR' Jirachi is NOT shiny-locked -> genuine soft-reset hunt (historical, disc long discontinued)"),
             go_mw("Masterwork Research 'Wish Granted'", "Feb 20 2023")],
    go="Shiny via 'Wish Granted' Masterwork (guaranteed). Not RNG in GO.",
    notes="Mythical with a real (historical) RNG hunt via the WISHMKR bonus disc. No longer accessible.")
add(name="Deoxys", gen="III", category="Mythical",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[M("FireRed/LeafGreen/Emerald", "Birth Island static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Needed AuroraTicket (event over). Not shiny-locked (Gen3)"),
             M("Omega Ruby/Alpha Sapphire", "Sky Pillar static", True, "n/a", "n/a", "n/a", True, "C",
               "ORAS Deoxys is shiny-LOCKED"),
             go_raid("Aug 7 2020", "All 4 formes shiny (Normal/Attack/Defense/Speed)")],
    go="Legendary/mythical raids — all 4 formes shiny (RNG); ~1/20",
    notes="Officially Mythical but treated as a raid boss in GO. Genuine RNG hunt via GO raids and historically via Birth Island.")

# ---------- GENERATION IV ----------
for nm, first in [("Uxie", "Sep 14 2021"), ("Mesprit", "Sep 14 2021"), ("Azelf", "Sep 14 2021")]:
    static = "Static (soft-reset)" if nm != "Mesprit" else "Roaming"
    add(name=nm, gen="IV", category="Legendary",
        shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
        home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
        methods=[da(), uw(), rp(), oras(),
                 M("Diamond/Pearl/Platinum", static, False, FULL_OLD, "n/a", "No charm pre-Gen6", False, "A",
                   "Historical cartridge"),
                 M("Brilliant Diamond/Shining Pearl", "Post-game lake " + ("static" if nm != "Mesprit" else "roamer"),
                   False, FULL, FULL, "No effect (BDSP)", True, "A", "In-wild BDSP encounter (separate from Ramanas)"),
                 go_raid(first, "regional raid boss")],
        go=f"Legendary raids (regional; shiny since {first}); ~1/20",
        notes="Lake trio. Mesprit roams (harder). Regional GO raid availability.")
add(name="Dialga", gen="IV", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(),
             M("Diamond/Pearl/Platinum", "Spear Pillar static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Historical"),
             M("Brilliant Diamond", "Story static", True, "n/a", "n/a", "n/a", True, "C",
               "BDSP story Dialga shiny-LOCKED (use Ramanas Park route instead)"),
             M("Legends: Arceus", "Origin Forme story static", True, "n/a", "n/a", "n/a", True, "C", "PLA shiny-locked"),
             go_raid("~2021", "Origin Forme shiny also available")],
    go="Legendary raids (Altered + Origin shiny); ~1/20; rotates",
    notes="Story catches locked (BDSP/PLA); huntable via Ramanas Park, DA, USUM, GO.")
add(name="Palkia", gen="IV", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(),
             M("Diamond/Pearl/Platinum", "Spear Pillar static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Historical"),
             M("Shining Pearl", "Story static", True, "n/a", "n/a", "n/a", True, "C", "BDSP story Palkia shiny-LOCKED"),
             M("Legends: Arceus", "Origin Forme story static", True, "n/a", "n/a", "n/a", True, "C", "PLA shiny-locked"),
             go_raid("~2021", "Origin Forme shiny also available; Shadow Palkia 2026")],
    go="Legendary raids (Altered + Origin shiny); ~1/20; rotates",
    notes="Story catches locked; huntable via Ramanas Park, DA, USUM, GO.")
add(name="Heatran", gen="IV", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(), oras(),
             M("Platinum/HGSS", "Stark Mountain static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Historical"),
             go_raid("Jan 7 2020")],
    go="Legendary raids (shiny since Jan 2020); ~1/20; rotates",
    notes="")
add(name="Regigigas", gen="IV", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[rp(),
             M("Brilliant Diamond/Shining Pearl", "Ramanas/Snowpoint static (soft-reset)", False, FULL, FULL,
               "No effect (BDSP)", True, "A", "Not shiny-locked in BDSP"),
             M("Platinum/HGSS", "Snowpoint Temple static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Historical"),
             go_raid("Jun 17 2021", "raids / Elite Raids")],
    go="Legendary/Elite raids (shiny since Jun 2021); ~1/20",
    notes="Not in Dynamax Adventures or USUM wormholes. Huntable via BDSP soft-reset and GO.")
add(name="Giratina", gen="IV", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(),
             M("Platinum/HGSS", "Turnback Cave static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Historical"),
             M("Legends: Arceus", "Origin Forme story static", True, "n/a", "n/a", "n/a", True, "C", "PLA shiny-locked"),
             go_raid("~2019", "Altered + Origin Forme shiny")],
    go="Legendary raids (Altered + Origin shiny); ~1/20; rotates",
    notes="Ramanas Park (Distortion Slate) is huntable. PLA Origin locked.")
add(name="Cresselia", gen="IV", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(), rp(), oras(),
             M("Diamond/Pearl/Platinum", "Roaming", False, FULL_OLD, "n/a", "No charm pre-Gen6", False, "A", "Historical"),
             go_raid("May 27 2019", "Shadow Cresselia shiny in 2025-26 Shadow Raids")],
    go="Legendary raids (shiny since May 2019); ~1/20; rotates",
    notes="")
add(name="Phione", gen="IV", category="Mythical",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("BDSP / any breeding game", "Breeding (Manaphy/Phione x Ditto), Masuda method", False,
               FULL, CHARM, "Yes (BDSP: Masuda + Charm applies to eggs)", True, "A",
               "The ONLY Mythical with normal breeding shiny odds; Masuda-eligible. Requires a Manaphy/Phione parent first")],
    go="Not in Pokémon GO.",
    notes="Uniquely, Phione is bred (not caught) and follows ordinary shiny/Masuda odds — a genuine, repeatable RNG hunt.")
add(name="Manaphy", gen="IV", category="Mythical",
    shiny_exists=True, rng_hunt=True, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Pokémon Ranger -> Gen 4", "Egg hatch after trade (PID vs TSV RNG)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A",
               "Ranger egg is shiny-locked until TRADED to another Gen4 game, then rolls on hatch. Ranger/distribution discontinued (historical)")],
    go="Base Manaphy via research; shiny NOT released in GO.",
    notes="The classic 'Manaphy egg' hunt. No current access (Pokémon Ranger connectivity discontinued). Manaphy itself cannot be bred (produces Phione).")
add(name="Darkrai", gen="IV", category="Mythical",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[M("Diamond/Pearl/Platinum", "Newmoon Island static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Needed Member Card event (over). Not shiny-locked (Gen4) -> historical hunt"),
             go_raid("Mar 6 2020", "Mythical but RNG-huntable in 5-star raids (Halloween)")],
    go="5-star raids (shiny since Mar 2020) — RNG; ~1/20",
    notes="Mythical that IS a true RNG hunt (GO raids now; Gen4 Newmoon Island historically).")
add(name="Shaymin", gen="IV", category="Mythical",
    shiny_exists=True, rng_hunt=True, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=False,
    methods=[M("Diamond/Pearl/Platinum", "Flower Paradise static (soft-reset)", False, FULL_OLD, "n/a",
               "No charm pre-Gen6", False, "A", "Needed Oak's Letter event (over). Not shiny-locked (Gen4) -> historical hunt"),
             go_mw("Masterwork Research 'Glimmers of Gratitude' (Land Forme)", "Feb 16 2024")],
    go="Shiny (Land) via Masterwork (guaranteed). Not RNG in GO.",
    notes="Historical Gen4 RNG hunt (Flower Paradise) no longer accessible; GO shiny is guaranteed-only.")
add(name="Arceus", gen="IV", category="Mythical",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Brilliant Diamond/Shining Pearl", "Hall of Origin static (soft-reset)", False, FULL, FULL,
               "No effect (BDSP Charm boosts Masuda eggs only)", True, "A",
               "NOT shiny-locked -> genuine soft-reset hunt. Requires the Azure Flute: have Legends: Arceus save "
               "data with all missions done + BDSP updated to v1.3.0 + be in the Hall of Fame; flute appears in "
               "Twinleaf Town, played at Spear Pillar after catching Dialga/Palkia + National Dex"),
             M("Legends: Arceus", "Story static", True, "n/a", "n/a", "n/a", True, "C", "PLA Arceus is shiny-locked"),
             M("Events (Toys R Us, etc.)", "Distribution", True, "n/a", "n/a", "n/a", False, "C",
               "All event Arceus were shiny-locked")],
    go="Not in Pokémon GO.",
    notes="Shiny Arceus IS legitimately huntable — the BDSP Hall of Origin encounter (Azure Flute) is not shiny-locked, "
          "so you can soft-reset for it (flat 1/4096; BDSP Shiny Charm does not help). PLA and all distributions are locked.")

# ---------- GENERATION V ----------
add(name="Victini", gen="V", category="Mythical",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Black/White + events", "Liberty Garden static / distribution", True, "n/a", "n/a", "n/a", True, "D",
               "Shiny-locked in every distribution; shiny still NOT released in GO (confirmed Jul 2026)")],
    go="In GO (research), but shiny NOT released.",
    notes="No legitimate shiny Victini exists anywhere as of Aug 2026. SHINY UNAVAILABLE.")
for nm, first in [("Cobalion", "Mar 17 2020"), ("Terrakion", "May 19 2020"), ("Virizion", "May 12 2020")]:
    add(name=nm, gen="V", category="Legendary",
        shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
        home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
        methods=[da(), uw(), oras(), za(),
                 M("Black/White/B2W2", "Static (soft-reset)", False, FULL_OLD, "~1/2731", "Yes (Gen5 charm)", False, "A",
                   "Historical cartridge; Swords of Justice not shiny-locked"),
                 go_raid(first)],
        go=f"Legendary raids (shiny since {first}); ~1/20; rotates",
        notes="Swords of Justice. NEW 2026: shiny-huntable in Legends Z-A Mega Dimension Hyperspace Distortions.")
add(name="Tornadus", gen="V", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(),
             M("Sword/Shield (Crown Tundra)", "Roaming (soft-reset)", False, FULL, CHARM, "Yes", True, "A",
               "Forces of Nature roam the Crown Tundra; not shiny-locked"),
             M("Black2/White2", "Static", False, FULL_OLD, "~1/2731", "Yes", False, "A", "Historical"),
             go_raid("Incarnate 2021 / Therian Mar 15 2022")],
    go="Legendary raids (Incarnate + Therian shiny); ~1/20",
    notes="Forces of Nature. Huntable via SwSh roamer, DA, USUM, GO.")
add(name="Thundurus", gen="V", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(),
             M("Sword/Shield (Crown Tundra)", "Roaming (soft-reset)", False, FULL, CHARM, "Yes", True, "A",
               "Not shiny-locked"),
             M("Black2/White2", "Static", False, FULL_OLD, "~1/2731", "Yes", False, "A", "Historical"),
             go_raid("Incarnate 2021 / Therian Apr 5 2022")],
    go="Legendary raids (Incarnate + Therian shiny); ~1/20",
    notes="Forces of Nature.")
add(name="Landorus", gen="V", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(),
             M("Sword/Shield (Crown Tundra)", "Roaming (soft-reset)", False, FULL, CHARM, "Yes", True, "A", "Not shiny-locked"),
             M("Black2/White2", "Static", False, FULL_OLD, "~1/2731", "Yes", False, "A", "Historical"),
             go_raid("Incarnate 2021 / Therian Apr 26 2022")],
    go="Legendary raids (Incarnate + Therian shiny); ~1/20",
    notes="Forces of Nature.")
add(name="Reshiram", gen="V", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(),
             M("Black/White/B2W2", "Story static (soft-reset)", False, FULL_OLD, "~1/2731", "Yes (Gen5 charm)", False, "A",
               "Gen5 box legend NOT shiny-locked -> historical hunt"),
             go_raid("~2020-21")],
    go="Legendary raids; ~1/20; rotates",
    notes="Tao trio. Huntable via DA, USUM, GO, and Gen5 originals.")
add(name="Zekrom", gen="V", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(),
             M("Black/White/B2W2", "Story static (soft-reset)", False, FULL_OLD, "~1/2731", "Yes", False, "A",
               "Gen5 box legend NOT shiny-locked -> historical hunt"),
             go_raid("~2020-21")],
    go="Legendary raids; ~1/20; rotates",
    notes="Tao trio.")
add(name="Kyurem", gen="V", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(),
             M("Black/White/B2W2", "Giant Chasm static (soft-reset)", False, FULL_OLD, "~1/2731", "Yes", False, "A",
               "Historical"),
             go_raid("~2021", "Black/White Kyurem via fusion (Fusion Raid Day Jan 10 2026)")],
    go="Legendary raids; ~1/20; rotates",
    notes="Tao trio. Fused formes via GO fusion events.")
add(name="Keldeo", gen="V", category="Mythical",
    shiny_exists=True, rng_hunt=False, huntable_now=False, event_only=True,
    home_guaranteed=True, go_shiny=True, go_rng_hunt=False,
    methods=[home_shiny("Shiny Keldeo", "Feb 12 2025", "complete Galar + IoA + Crown Tundra dexes (SwSh)"),
             go_mw("Masterwork Research 'Pony Tales' (Final Justice)", "Nov 25 2025"),
             M("Main series", "Distribution", True, "n/a", "n/a", "n/a", False, "C", "All distributions shiny-locked")],
    go="Shiny via 'Pony Tales' Masterwork (guaranteed). Not RNG.",
    notes="First legit shiny Keldeo was the HOME dex reward (Feb 2025). Guaranteed only — never RNG-huntable.")
add(name="Meloetta", gen="V", category="Mythical",
    shiny_exists=True, rng_hunt=False, huntable_now=False, event_only=True,
    home_guaranteed=True, go_shiny=True, go_rng_hunt=False,
    methods=[home_shiny("Shiny Meloetta", "Oct 2024", "complete Paldea + Kitakami + Blueberry dexes (SV)"),
             go_mw("Masterwork Research 'A Dazzling Aria' (GO Tour Unova)", "Feb 21 2025"),
             M("Main series", "Distribution", True, "n/a", "n/a", "n/a", False, "C", "All distributions shiny-locked")],
    go="Shiny (Aria) via Masterwork (guaranteed). Not RNG.",
    notes="Guaranteed only (HOME reward + GO Masterwork). Never RNG-huntable.")
add(name="Genesect", gen="V", category="Mythical",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[M("Main series", "Distribution", True, "n/a", "n/a", "n/a", False, "C", "All distributions shiny-locked"),
             go_raid("May 2 2023", "Mythical but RNG in 5-star raids; rotates by Drive")],
    go="5-star raids (shiny since May 2023) — RNG; ~1/20",
    notes="Mythical that IS a true RNG hunt (GO raids). Different Drives rotate.")

# ---------- GENERATION VI ----------
add(name="Xerneas", gen="VI", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(),
             M("X/Y", "Story static", True, "n/a", "n/a", "n/a", False, "C", "XY box legend shiny-LOCKED"),
             go_raid("Oct 8 2022")],
    go="Legendary raids (shiny since Oct 2022); ~1/20; rotates",
    notes="Story catch locked; huntable via DA, USUM, GO.")
add(name="Yveltal", gen="VI", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(), uw(),
             M("X/Y", "Story static", True, "n/a", "n/a", "n/a", False, "C", "XY box legend shiny-LOCKED"),
             go_raid("Sep 27 2022")],
    go="Legendary raids (shiny since Sep 2022); ~1/20; rotates",
    notes="Story catch locked; huntable via DA, USUM, GO.")
add(name="Zygarde", gen="VI", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[da(),
             M("X/Y, USUM, SV, Legends Z-A", "Story static / cell assembly", True, "n/a", "n/a", "n/a", True, "C",
               "All story/static/cell-assembly encounters are shiny-locked (incl. Z-A Main Mission 42 and the SV "
               "Indigo Disk)")],
    go="In GO (Routes/cells); shiny NOT released.",
    notes="Correction: shiny Zygarde IS huntable — Sword/Shield Dynamax Adventures (Max Lair) is the only game where "
          "you can catch it, 1/300 (1/100 with Shiny Charm). Every story/static/cell-assembly encounter is "
          "shiny-locked; no guaranteed shiny Zygarde has ever been officially distributed.")
add(name="Diancie", gen="VI", category="Mythical",
    shiny_exists=True, rng_hunt=False, huntable_now=False, event_only=True,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=False,
    methods=[M("XY/ORAS", "Event distribution (guaranteed shiny)", True, "n/a", "n/a", "n/a", False, "C",
               "Guaranteed shiny Diancie distributed 2016 (e.g. Korea/Pokémon Center)"),
             go_mw("Masterwork 'Sparkle and Shine' (GO Tour Kalos)", "Feb 2026")],
    go="Shiny via 'Sparkle and Shine' Masterwork (guaranteed, Feb 2026). Not RNG.",
    notes="Guaranteed/event only. GO shiny debuted Feb 2026 (newest guaranteed Mythical shiny).")
add(name="Hoopa", gen="VI", category="Mythical",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Main series / GO", "Distribution / research", True, "n/a", "n/a", "n/a", True, "D",
               "Shiny-locked everywhere; shiny not released in GO (confirmed Jul 2026)")],
    go="In GO (research); shiny NOT released.",
    notes="No legitimate shiny Hoopa as of Aug 2026. SHINY UNAVAILABLE.")
add(name="Volcanion", gen="VI", category="Mythical",
    shiny_exists=True, rng_hunt=False, huntable_now=False, event_only=True,
    home_guaranteed=True, go_shiny=False, go_rng_hunt=False,
    methods=[home_shiny("Shiny Volcanion", "Apr 2026",
                        "complete Lumiose + Hyperspace Lumiose + Mega dexes (Legends Z-A)"),
             M("Main series", "Distribution", True, "n/a", "n/a", "n/a", False, "C", "Prior distributions shiny-locked")],
    go="In GO (GO Fest research); shiny NOT released in GO.",
    notes="First-ever legit shiny Volcanion is the HOME dex reward (Apr 2026). Guaranteed only.")

# ---------- GENERATION VII ----------
add(name="Type: Null", gen="VII", category="Legendary",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Sun/Moon/USUM/SwSh", "Gift (Aether / Battle Tower)", True, "n/a", "n/a", "n/a", True, "D",
               "Gift is shiny-locked in every game; only source; not in GO")],
    go="Not in Pokémon GO.",
    notes="Officially 'Synthetic Pokémon'; Bulbapedia counts it as Legendary. No legit shiny Type: Null: the gift is "
          "shiny-locked everywhere, and the 2017 event distributed the already-evolved Shiny SILVALLY (you cannot "
          "devolve it). So shiny Silvally exists, but shiny Type: Null does not.")
add(name="Silvally", gen="VII", category="Legendary",
    shiny_exists=True, rng_hunt=False, huntable_now=False, event_only=True,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False, home_event=True,
    methods=[M("Event (GameStop/GAME/EB Games)", "Serial-code guaranteed shiny", False, "n/a", "n/a", "n/a", False, "C",
               "A battle-ready Shiny Silvally was officially distributed Oct 23–Nov 13 2017 (for Sun/Moon); event over"),
             M("Sun/Moon/USUM/SwSh", "Evolves from Type: Null gift", True, "n/a", "n/a", "n/a", True, "C",
               "The in-game Type: Null gift is shiny-locked in every game")],
    go="Not in Pokémon GO.",
    notes="Correction: a legit shiny Silvally EXISTS via the official 2017 GameStop/GAME/EB event distribution "
          "(already evolved) — but it is NOT RNG-huntable. The in-game Type: Null gift is shiny-locked everywhere.")
for nm, first in [("Tapu Koko", "Jan 25 2023"), ("Tapu Lele", "Feb 8 2023"),
                  ("Tapu Bulu", "Apr 17 2023"), ("Tapu Fini", "May 9 2023")]:
    add(name=nm, gen="VII", category="Legendary",
        shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
        home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
        methods=[da(),
                 M("Sun/Moon/USUM", "Ruins guardian static — respawn (soft-reset)", False, FULL, CHARM,
                   "Yes (first story encounter is locked; the RESPAWN is huntable)", True, "A",
                   "Requires 3DS cartridge"),
                 go_raid(first)],
        go=f"Legendary raids (shiny since {first}); ~1/20; rotates",
        notes="Guardian deities. First story encounter shiny-locked; defeat it and the respawn is huntable.")
add(name="Cosmog", gen="VII", category="Legendary",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Sun/Moon/USUM/GO", "Gift / research", True, "n/a", "n/a", "n/a", True, "D",
               "Gift shiny-locked; shiny Cosmog not obtainable (final forms Solgaleo/Lunala are shiny separately)")],
    go="In GO (Special Research, evolves to Solgaleo/Lunala); shiny Cosmog not released.",
    notes="Shiny Cosmog/Cosmoem UNAVAILABLE (cannot evolve a shiny backward from Solgaleo/Lunala). Verify if GO ever releases shiny Cosmog.")
add(name="Cosmoem", gen="VII", category="Legendary",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Sun/Moon/USUM/GO", "Evolves from Cosmog", True, "n/a", "n/a", "n/a", True, "D",
               "Only from shiny-locked Cosmog line")],
    go="In GO (evolution stage); shiny not released.",
    notes="Shiny UNAVAILABLE for the same reason as Cosmog.")
add(name="Solgaleo", gen="VII", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(),
             M("Sun/USUM", "From Cosmog / Necrozma fusion", True, "n/a", "n/a", "n/a", True, "C",
               "Main-series Solgaleo (via locked Cosmog) is effectively locked"),
             go_raid("Jul 22 2026", "NEW in 2026")],
    go="5-star raids — shiny NEW Jul 22 2026 (RNG); ~1/20",
    notes="Shiny huntable via Dynamax Adventures and (new 2026) GO raids.")
add(name="Lunala", gen="VII", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(),
             M("Moon/USUM", "From Cosmog / Necrozma fusion", True, "n/a", "n/a", "n/a", True, "C",
               "Main-series Lunala (via locked Cosmog) effectively locked"),
             go_raid("~Jul 2026 (GO Fest)", "NEW in 2026")],
    go="5-star raids — shiny NEW ~Jul 2026 (RNG); ~1/20",
    notes="Shiny huntable via Dynamax Adventures and (new 2026) GO raids.")
add(name="Necrozma", gen="VII", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[da(),
             M("Sun/Moon/USUM", "Story static", True, "n/a", "n/a", "n/a", True, "C", "Main-series Necrozma shiny-locked"),
             go_raid("Aug 25 2025", "GO Fest 2024 ticket -> 5-star raids Aug 2025; Dusk Mane/Dawn Wings via fusion")],
    go="5-star raids (shiny since Aug 2025) — RNG; ~1/20",
    notes="Main-series locked; huntable via Dynamax Adventures and GO raids.")
add(name="Magearna", gen="VII", category="Mythical",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("QR distribution / HOME", "Serial / dex reward", True, "n/a", "n/a", "n/a", True, "D",
               "Both regular and 'Original Color' forms are shiny-locked; Original Color is a FORM, not a shiny; not in GO")],
    go="Not in Pokémon GO.",
    notes="No legitimate shiny Magearna. The HOME National-Dex reward is Original-Color Magearna (a form), NOT a shiny. SHINY UNAVAILABLE.")
add(name="Marshadow", gen="VII", category="Mythical",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Distribution / GO", "Serial / research", True, "n/a", "n/a", "n/a", True, "D",
               "Shiny-locked; shiny not released in GO (base Marshadow in GO May 2024)")],
    go="In GO (research); shiny NOT released.",
    notes="No legitimate shiny Marshadow as of Aug 2026. SHINY UNAVAILABLE.")
add(name="Zeraora", gen="VII", category="Mythical",
    shiny_exists=True, rng_hunt=False, huntable_now=False, event_only=True,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Pokémon HOME (2020)", "Raid-milestone Mystery Gift (guaranteed shiny)", False, "n/a", "n/a", "n/a",
               False, "C", "Shiny Zeraora distributed via Pokémon HOME Jun 30–Jul 6 2020 after trainers won 1M+ "
                            "Max Raids (-> Sword/Shield); event over"),
             M("Other distributions / GO", "Serial / raids", True, "n/a", "n/a", "n/a", True, "C",
               "Other Zeraora distributions are shiny-locked; shiny not released in GO")],
    go="In GO (GO Fest 2026); shiny NOT released.",
    notes="Correction: a legit shiny Zeraora EXISTS via the 2020 Pokémon HOME raid-milestone distribution "
          "(guaranteed, event over) — but it is NOT RNG-huntable. Not shiny in GO as of Aug 2026.")
add(name="Meltan", gen="VII", category="Mythical",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=True, go_shiny=True, go_rng_hunt=True,
    methods=[M("Pokémon GO", "Mystery Box (RNG, timed windows)", False, GO_W, "n/a", "n/a", True, "A",
               "Shiny Meltan RNG-rollable during announced Shiny Meltan windows (~1/125)"),
             home_shiny("Shiny Meltan", "Feb 12 2025", "complete Kanto dex (Let's Go P/E)")],
    go="Mystery Box (shiny since Feb 5 2019) — RNG during shiny windows; ~1/125",
    notes="Mythical with a real RNG hunt (Mystery Box). Also a guaranteed HOME dex reward since Feb 2025.")
add(name="Melmetal", gen="VII", category="Mythical",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[M("Pokémon GO", "Evolve a shiny Meltan (400 candy)", False, GO_W, "n/a", "n/a", True, "A",
               "Shiny Melmetal obtained by evolving a hunted shiny Meltan; Gigantamax shiny via GO->HOME->SwSh")],
    go="Evolve shiny Meltan (RNG via Mystery Box). ~1/125 at the Meltan step.",
    notes="Evolution case: not encountered directly — hunt shiny Meltan, then evolve.")

# ---------- GENERATION VIII ----------
add(name="Zacian", gen="VIII", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[M("Sword/Shield", "Story static", True, "n/a", "n/a", "n/a", True, "C", "SwSh box legend shiny-LOCKED"),
             go_raid("Sep 26 2024")],
    go="5-star raids (shiny since Sep 2024) — RNG; ~1/20",
    notes="Main-series locked; the RNG hunt is GO raids.")
add(name="Zamazenta", gen="VIII", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[M("Sword/Shield", "Story static", True, "n/a", "n/a", "n/a", True, "C", "SwSh box legend shiny-LOCKED"),
             go_raid("Oct 4 2024")],
    go="5-star raids (shiny since Oct 2024) — RNG; ~1/20",
    notes="Main-series locked; RNG hunt is GO raids.")
add(name="Eternatus", gen="VIII", category="Legendary",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Sword/Shield / GO", "Story static / raids", True, "n/a", "n/a", "n/a", True, "D",
               "SwSh shiny-locked; shiny not released in GO (debuted Aug 2025)")],
    go="In GO (raids since Aug 2025); shiny NOT released.",
    notes="No legitimate shiny Eternatus as of Aug 2026. SHINY UNAVAILABLE.")
add(name="Kubfu", gen="VIII", category="Legendary",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Sword/Shield (Isle of Armor) / GO", "Gift / research", True, "n/a", "n/a", "n/a", True, "D",
               "IoA gift shiny-locked; shiny not available in GO")],
    go="In GO; shiny NOT available.",
    notes="Classification debated (some group with Legendaries). Shiny UNAVAILABLE.")
add(name="Urshifu", gen="VIII", category="Legendary",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Sword/Shield (Isle of Armor) / GO", "Evolves from Kubfu", True, "n/a", "n/a", "n/a", True, "D",
               "Only from shiny-locked Kubfu; shiny not available in GO")],
    go="In GO; shiny NOT available.",
    notes="Shiny UNAVAILABLE (only from shiny-locked Kubfu).")
add(name="Regieleki", gen="VIII", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[M("Sword/Shield (Crown Tundra)", "Split-Decision Ruins static (soft-reset)", False, FULL, CHARM,
               "Yes (1/4096 -> 1/1365)", True, "A", "Choose Regieleki OR Regidrago per save; NOT shiny-locked"),
             go_raid("Nov 27 2024")],
    go="5-star raids (shiny since Nov 2024) — RNG; ~1/20",
    notes="One of only two SwSh-introduced legendaries that can be shiny (with Regidrago). Static soft-reset.")
add(name="Regidrago", gen="VIII", category="Legendary",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Sword/Shield (Crown Tundra)", "Split-Decision Ruins static (soft-reset)", False, FULL, CHARM,
               "Yes (1/4096 -> 1/1365)", True, "A", "Choose Regieleki OR Regidrago per save; NOT shiny-locked")],
    go="In GO; shiny not confirmed released (as of Aug 2026).",
    notes="Shiny huntable via SwSh Split-Decision Ruins soft-reset. GO shiny status uncertain/unreleased.")
add(name="Glastrier", gen="VIII", category="Legendary",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Sword/Shield (Crown Tundra) / GO", "Story static / raids", True, "n/a", "n/a", "n/a", True, "D",
               "Crown Tundra encounter shiny-locked; shiny not released in GO")],
    go="In GO; shiny NOT released.",
    notes="No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.")
add(name="Spectrier", gen="VIII", category="Legendary",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Sword/Shield (Crown Tundra) / GO", "Story static / raids", True, "n/a", "n/a", "n/a", True, "D",
               "Crown Tundra encounter shiny-locked; shiny not released in GO")],
    go="In GO; shiny NOT released.",
    notes="No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.")
add(name="Calyrex", gen="VIII", category="Legendary",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Sword/Shield (Crown Tundra) / GO", "Gift / raids", True, "n/a", "n/a", "n/a", True, "D",
               "Crown Tundra gift shiny-locked; shiny not released in GO")],
    go="In GO; shiny NOT released.",
    notes="No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.")
add(name="Enamorus", gen="VIII", category="Legendary",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Legends: Arceus / GO", "Story static / Elite Raids", True, "n/a", "n/a", "n/a", True, "D",
               "PLA story catch shiny-locked; shiny not released in GO (Incarnate or Therian)")],
    go="In GO (Elite Raids); shiny NOT released.",
    notes="Fourth Force of Nature. No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.")
add(name="Zarude", gen="VIII", category="Mythical",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Distribution / GO", "Serial / event", True, "n/a", "n/a", "n/a", True, "D",
               "All distributions shiny-locked; shiny not released in GO (both GO appearances non-shiny)")],
    go="In GO (non-shiny); shiny NOT released.",
    notes="No legitimate shiny Zarude anywhere as of Aug 2026. SHINY UNAVAILABLE.")

# ---------- GENERATION IX ----------
add(name="Koraidon", gen="IX", category="Legendary",
    shiny_exists=True, rng_hunt=False, huntable_now=False, event_only=True,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Scarlet/Violet", "Story ride legendary", True, "n/a", "n/a", "n/a", True, "C",
               "SV story Koraidon shiny-LOCKED"),
             M("Distribution (GameStop/EB code)", "Serial-code gift (guaranteed shiny)", False, "n/a", "n/a", "n/a",
               False, "C", "Shiny Koraidon distributed Sep 26–Oct 15 2025 via GameStop/EB Games codes (guaranteed, not a roll); event over")],
    go="Not in Pokémon GO.",
    notes="Shiny exists ONLY via the 2025 guaranteed retail-code distribution (Sep 26–Oct 15 2025). Never RNG-huntable.")
add(name="Miraidon", gen="IX", category="Legendary",
    shiny_exists=True, rng_hunt=False, huntable_now=False, event_only=True,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Scarlet/Violet", "Story ride legendary", True, "n/a", "n/a", "n/a", True, "C",
               "SV story Miraidon shiny-LOCKED"),
             M("Distribution (GameStop/EB code)", "Serial-code gift (guaranteed shiny)", False, "n/a", "n/a", "n/a",
               False, "C", "Shiny Miraidon distributed Sep 26–Oct 15 2025 via GameStop/EB Games codes (guaranteed, not a roll); event over")],
    go="Not in Pokémon GO.",
    notes="Shiny exists ONLY via the 2025 guaranteed retail-code distribution (Sep 26–Oct 15 2025). Never RNG-huntable.")
for nm in ["Wo-Chien", "Chien-Pao", "Ting-Lu", "Chi-Yu"]:
    add(name=nm, gen="IX", category="Legendary",
        shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
        home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
        methods=[M("Scarlet/Violet", "Unbound-stakes static", True, "n/a", "n/a", "n/a", True, "D",
                   "SV encounter shiny-locked; no distribution; not in GO")],
        go="Not in Pokémon GO.",
        notes="Treasures of Ruin. No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.")
for nm in ["Okidogi", "Munkidori", "Fezandipiti"]:
    add(name=nm, gen="IX", category="Legendary",
        shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
        home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
        methods=[M("Scarlet/Violet (Teal Mask)", "Static", True, "n/a", "n/a", "n/a", True, "D",
                   "Teal Mask encounter shiny-locked; not in GO")],
        go="Not in Pokémon GO.",
        notes="Loyal Three. No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.")
add(name="Ogerpon", gen="IX", category="Legendary",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Scarlet/Violet (Teal Mask)", "Gift", True, "n/a", "n/a", "n/a", True, "D",
               "Teal Mask gift shiny-locked; not in GO")],
    go="Not in Pokémon GO.",
    notes="No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.")
add(name="Terapagos", gen="IX", category="Legendary",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Scarlet/Violet (Indigo Disk)", "Story gift", True, "n/a", "n/a", "n/a", True, "D",
               "Indigo Disk story gift shiny-locked; not in GO")],
    go="Not in Pokémon GO.",
    notes="No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.")
add(name="Pecharunt", gen="IX", category="Mythical",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("Scarlet/Violet (Mochi Mayhem)", "Epilogue static", True, "n/a", "n/a", "n/a", True, "D",
               "SV epilogue shiny-locked; not in GO")],
    go="Not in Pokémon GO.",
    notes="No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.")

# ---------- ULTRA BEASTS (separate class; not Legendary/Mythical) ----------
UB_HUNTABLE = [
    ("Nihilego", "Jul 2024"), ("Buzzwole", "Jul 5 2024"), ("Pheromosa", "Jun 14 2024"),
    ("Xurkitree", "May 30 2024"), ("Celesteela", "Jul 2024"), ("Kartana", "Jul 2024"),
    ("Guzzlord", "Jul 2024"), ("Stakataka", "Apr 2025"), ("Blacephalon", "Apr 2025"),
]
for nm, first in UB_HUNTABLE:
    methods = [uw(),
               M("Sword/Shield (Crown Tundra)", "Dynamax Adventure boss (soft-resettable)", False, DA_B, DA_C,
                 "Yes (1/300 -> 1/100)", True, "A", "UB path unlocks after returning legendaries"),
               go_raid(first, "Ultra Beast raids")]
    add(name=nm, gen="VII", category="Ultra Beast",
        shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
        home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
        methods=methods,
        go=f"Ultra Beast raids (shiny since {first}); ~1/20",
        notes="Ultra Beast (own class). Shiny-locked in SM; unlocked in USUM wormholes, Dynamax Adventures, and GO raids.")
add(name="Poipole", gen="VII", category="Ultra Beast",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("USUM / GO", "Gift / research", True, "n/a", "n/a", "n/a", True, "D",
               "USUM gift shiny-locked; confirmed shiny-locked in GO")],
    go="In GO; shiny-LOCKED.",
    notes="Ultra Beast. Shiny UNAVAILABLE (shiny-locked in both USUM and GO).")
add(name="Naganadel", gen="VII", category="Ultra Beast",
    shiny_exists=False, rng_hunt=False, huntable_now=False, event_only=False,
    home_guaranteed=False, go_shiny=False, go_rng_hunt=False,
    methods=[M("USUM / GO", "Evolves from Poipole", True, "n/a", "n/a", "n/a", True, "D",
               "Only from shiny-locked Poipole")],
    go="In GO; shiny-LOCKED.",
    notes="Ultra Beast. Shiny UNAVAILABLE (only from shiny-locked Poipole).")


# ---------- REGIONAL FORMS (distinct shiny status -> own rows) ----------
def go_dai(first):
    return M("Pokémon GO", "Daily Adventure Incense wild spawn (RNG)", False, "~1/20 per encounter", "n/a",
             "n/a (GO has no Shiny Charm)", True, "A",
             f"Shiny since {first}; wild-ONLY via Daily Adventure Incense (never in raids). Boosted ~1/20 shiny rate, "
             f"but DAI yields only ~1 bird encounter per day, so it is a slow grind")

def galar_lock():
    return M("Sword/Shield (Crown Tundra)", "Roaming static (Legendary Clue 1)", True, "n/a", "n/a", "n/a",
             True, "C", "Galarian bird roamer is shiny-LOCKED in the main series")

_GAL = [("Galarian Articuno", "Articuno", "Psychic/Flying"),
        ("Galarian Zapdos", "Zapdos", "Fighting/Flying"),
        ("Galarian Moltres", "Moltres", "Dark/Flying")]
for nm, base, typ in _GAL:
    add(name=nm, gen="VIII", category="Legendary", is_form=True, base=base,
        shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
        home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
        methods=[galar_lock(), go_dai("Oct 4 2024")],
        go="Daily Adventure Incense wild (shiny since Oct 2024) — RNG, wild-only (not raids)",
        notes=f"Galarian form of {base} ({typ}) — a distinct Pokémon introduced in Gen VIII, NOT the Kanto bird. "
              f"Main-series Crown Tundra roamer is shiny-locked; the ONLY shiny route is Pokémon GO Daily "
              f"Adventure Incense wild spawns.")

# ---------- alternate FORMES broken out as their own rows (separate shiny collectibles) ----------
def go_raid_form(first, label):
    return M("Pokémon GO", f"Raid — {label} (RNG)", False, GO_R, "n/a", "n/a (GO has no Shiny Charm)", True, "A",
             f"Shiny {label} since {first}; a separate raid encounter/shiny from the base forme")

def form_change(games, item, huntable_via):
    return M(games, f"Form change ({item})", False, "n/a", "n/a",
             f"Same shiny as the base — {huntable_via}", True, "A",
             "Not a separate main-series hunt: the form-change item just re-shapes your (huntable) base Pokémon")

# Deoxys formes (Attack/Defense/Speed) — 4 distinct shinies in GO; base row = Normal Forme
_DEO = [("Deoxys (Attack Forme)", "Feb 19 2022", "FireRed"),
        ("Deoxys (Defense Forme)", "Feb 22 2022", "LeafGreen"),
        ("Deoxys (Speed Forme)", "Feb 25 2022", "Emerald")]
for nm, first, g3 in _DEO:
    add(name=nm, gen="III", category="Mythical", is_form=True, base="Deoxys",
        shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
        home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
        methods=[go_raid_form(first, "this Forme"),
                 M(f"{g3} (Gen 3)", "Birth Island static (soft-reset)", False, FULL_OLD, "n/a",
                   "No charm pre-Gen6", False, "A",
                   f"This Forme was the {g3} version in Gen 3; Birth Island Deoxys is NOT shiny-locked -> historical "
                   f"soft-reset hunt. ORAS Deoxys is shiny-locked")],
        go=f"Forme-specific raids (shiny since {first}) — RNG; ~1/20",
        notes="Alternate Forme of Deoxys — a separate shiny collectible in GO (own release date). "
              "In the main series the Forme is fixed by game/meteorite.")

# Origin Formes (separate shiny raids in GO)
add(name="Giratina (Origin Forme)", gen="IV", category="Legendary", is_form=True, base="Giratina",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
    methods=[go_raid_form("~2021", "Origin Forme"),
             form_change("Platinum/BDSP/SwSh/PLA", "Griseous Orb/Core", "huntable via DA/USUM/Ramanas Park")],
    go="Origin Forme raids — RNG; ~1/20",
    notes="Separate shiny raid boss in GO; in the main series it's a Griseous Orb/Core form-change of your Giratina.")
add(name="Dialga (Origin Forme)", gen="IV", category="Legendary", is_form=True, base="Dialga",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True, go_form_only=True,
    methods=[go_raid_form("~2023", "Origin Forme"),
             M("Legends: Arceus (Adamant Crystal)", "Origin form-change", True, "n/a", "n/a", "n/a", True, "C",
               "The Adamant Crystal is PLA-exclusive and the PLA Dialga is shiny-locked, so a shiny Origin Dialga "
               "cannot be self-caught in the main series")],
    go="Origin Forme raids — RNG; ~1/20",
    notes="GO-ONLY shiny. Unlike Giratina, a shiny Origin Dialga can only come from Pokémon GO: the Adamant Crystal "
          "is PLA-exclusive and the PLA Dialga is shiny-locked, so it can't be paired with a huntable shiny.")
add(name="Palkia (Origin Forme)", gen="IV", category="Legendary", is_form=True, base="Palkia",
    shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
    home_guaranteed=False, go_shiny=True, go_rng_hunt=True, go_form_only=True,
    methods=[go_raid_form("~2023", "Origin Forme"),
             M("Legends: Arceus (Lustrous Globe)", "Origin form-change", True, "n/a", "n/a", "n/a", True, "C",
               "The Lustrous Globe is PLA-exclusive and the PLA Palkia is shiny-locked, so a shiny Origin Palkia "
               "cannot be self-caught in the main series")],
    go="Origin Forme raids — RNG; ~1/20",
    notes="GO-ONLY shiny. Unlike Giratina, a shiny Origin Palkia can only come from Pokémon GO: the Lustrous Globe "
          "is PLA-exclusive and the PLA Palkia is shiny-locked, so it can't be paired with a huntable shiny.")

# Therian Formes (separate shiny raids in GO, 2022)
for nm, base, first in [("Tornadus (Therian Forme)", "Tornadus", "Mar 15 2022"),
                        ("Thundurus (Therian Forme)", "Thundurus", "Apr 5 2022"),
                        ("Landorus (Therian Forme)", "Landorus", "Apr 26 2022")]:
    add(name=nm, gen="V", category="Legendary", is_form=True, base=base,
        shiny_exists=True, rng_hunt=True, huntable_now=True, event_only=False,
        home_guaranteed=False, go_shiny=True, go_rng_hunt=True,
        methods=[go_raid_form(first, "Therian Forme"),
                 form_change("Black2/White2 onward (Reveal Glass)", "Reveal Glass",
                             "huntable via Dynamax Adventures / SwSh roamer / GO")],
        go=f"Therian Forme raids (shiny since {first}) — RNG; ~1/20",
        notes="Separate shiny raid boss in GO; in the main series it's a Reveal Glass form-change of the Incarnate forme.")

# ---------- alternate FORMES (documented on the base species row, not split out) ----------
FORMS = {
    "Articuno": ["Galarian Articuno — see its own row (Gen VIII, GO-only shiny)"],
    "Zapdos": ["Galarian Zapdos — see its own row (Gen VIII, GO-only shiny)"],
    "Moltres": ["Galarian Moltres — see its own row (Gen VIII, GO-only shiny)"],
    "Deoxys": ["This row is the Normal Forme. Attack / Defense / Speed Formes each have their OWN row "
               "(each a separate GO shiny with its own release date)"],
    "Dialga": ["Origin Forme — see its own row (separate GO shiny)"],
    "Palkia": ["Origin Forme — see its own row (separate GO shiny)"],
    "Giratina": ["This row is the Altered Forme. Origin Forme — see its own row (separate GO shiny)"],
    "Shaymin": ["Land Forme — shiny (GO Masterwork, guaranteed). Sky Forme — shiny status unconfirmed"],
    "Tornadus": ["This row is the Incarnate Forme. Therian Forme — see its own row (separate GO shiny)"],
    "Thundurus": ["This row is the Incarnate Forme. Therian Forme — see its own row (separate GO shiny)"],
    "Landorus": ["This row is the Incarnate Forme. Therian Forme — see its own row (separate GO shiny)"],
    "Kyurem": ["Black Kyurem & White Kyurem — fusion formes (with Zekrom/Reshiram); shiny via the base Kyurem"],
    "Zacian": ["Hero of Many Battles & Crowned Sword — shiny carries across the form change"],
    "Zamazenta": ["Hero of Many Battles & Crowned Shield — shiny carries across the form change"],
    "Necrozma": ["Dusk Mane / Dawn Wings (fusions with Solgaleo/Lunala) & Ultra Necrozma — shiny via base Necrozma"],
    "Calyrex": ["Ice Rider / Shadow Rider (fusions with Glastrier/Spectrier) — all shiny-unavailable"],
    "Urshifu": ["Single Strike & Rapid Strike Style — both shiny-locked (from the locked Kubfu)"],
    "Zygarde": ["10% / 50% / Complete Forme — all shiny-unavailable"],
    "Hoopa": ["Confined & Unbound — both shiny-unavailable"],
    "Meloetta": ["Aria & Pirouette — shiny is guaranteed (HOME/GO), applies to both"],
    "Genesect": ["Normal/Shock/Burn/Chill/Douse Drives — shiny in GO raids; Drives are held-item variants (separate raid dates)"],
    "Enamorus": ["Incarnate & Therian — both shiny-unavailable as of Aug 2026 (GO shiny not released)"],
    "Keldeo": ["Ordinary & Resolute — shiny is guaranteed (HOME/GO Masterwork), applies to both"],
    "Ogerpon": ["Teal / Wellspring / Hearthflame / Cornerstone Mask — all shiny-locked"],
    "Terapagos": ["Normal / Terastal / Stellar Forme — shiny-locked"],
}

# Species with a GUARANTEED-SHINY EVENT DISTRIBUTION (serial code / Mystery Gift / in-person /
# HOME event distribution) — a predetermined shiny you could store in HOME, NOT a self-caught hunt.
# (Set from research; see sources.md. Species already flagged home_event=True in add() are unioned in.)
HOME_EVENT_SHINY = {
    "Raikou", "Entei", "Suicune",                       # 2011 shiny beasts (GameStop/GAME)
    "Genesect",                                          # 2013 movie (JP)
    "Diancie",                                           # 2016 serial
    "Tapu Koko", "Tapu Lele", "Tapu Bulu", "Tapu Fini",  # 2019 competition serials
    "Zeraora",                                           # 2020 HOME raid-milestone distribution
    "Celebi",                                            # 2021 movie promo (guaranteed shiny)
    "Zacian", "Zamazenta",                               # 2021-22 BDSP-launch serials
    "Galarian Articuno", "Galarian Zapdos", "Galarian Moltres",  # 2022 competition serials
    "Silvally",                                          # 2017 GameStop/GAME/EB distribution
    "Koraidon", "Miraidon",                              # Sep 26-Oct 15 2025 GameStop/EB codes
}  # confirmed guaranteed-shiny distributions (research audit; see sources.md). Zygarde has NO shiny distribution.

def _has_main_ot(p):
    """True if there is a legit main-series self-catch (OT) shiny — a non-GO/HOME, cat-A, not-locked method."""
    for m in p["methods"]:
        if m["game"] in ("Pokémon GO", "Pokémon HOME"):
            continue
        if m["cat"] == "A" and not m["shiny_locked"]:
            return True
    return False

# normalize: every entry gets is_form / base / forms + the four obtainment-source flags
_WARN = []
for _p in DATA:
    _p.setdefault("is_form", False)
    _p.setdefault("base", None)
    _p.setdefault("go_form_only", False)   # form exists only in GO; reverts on GO->HOME transfer (no HOME channel)
    _p.setdefault("forms", FORMS.get(_p["name"], []))
    _p["home_event"] = _p.get("home_event", False) or (_p["name"] in HOME_EVENT_SHINY)
    # four obtainment channels (for the collection tracker)
    _p["src_home_ot"] = _has_main_ot(_p)          # self-caught shiny in HOME
    _p["src_home_reward"] = _p["home_guaranteed"] # HOME Pokédex-completion reward shiny
    _p["src_home_event"] = _p["home_event"]       # event-distributed shiny (storable in HOME)
    _p["src_go"] = _p["go_shiny"]                 # shiny in Pokémon GO
    _derived = _p["src_home_ot"] or _p["src_home_reward"] or _p["src_home_event"] or _p["src_go"]
    if _p["shiny_exists"] and not _derived:
        _WARN.append(f"{_p['name']}: shiny_exists but no source channel")
    if _derived and not _p["shiny_exists"]:
        _WARN.append(f"{_p['name']}: has a source channel but shiny_exists=False")
    _p["shiny_exists"] = _p["shiny_exists"] or _derived

# targeted override: Manaphy also gets the Reward channel (per request) — the Manaphy Egg
# is received as a gift/reward (Pokémon Ranger), separate from the self-hatched OT shiny.
for _p in DATA:
    if _p["name"] == "Manaphy":
        _p["src_home_reward"] = True


# ============================================================================
# Derived helpers & emission
# ============================================================================
def yn(b):
    return "Yes" if b else "No"


def status_now(p):
    if p["huntable_now"]:
        return "Yes"
    if p["rng_hunt"]:
        return "No (historical only)"
    return "No"


def bucket(p):
    """The spec's A-E category for the master table."""
    if not p["shiny_exists"]:
        return "D (shiny unavailable)"
    if p["rng_hunt"] and p["huntable_now"]:
        return "A (true hunt, current)"
    if p["rng_hunt"] and not p["huntable_now"]:
        return "E (hunt, historical only)"
    if any(m["cat"] == "B" for m in p["methods"]):
        return "B (guaranteed reward)"
    return "C (event distribution only)"


def method_col_value(p, col):
    for m in p["methods"]:
        enc, game = m["encounter"], m["game"]
        if col == "SwSh Dynamax Adventure" and "Dynamax Adventure" in enc:
            return f"{m['odds_base']} ({m['odds_charm']} charm)"
        if col == "USUM Ultra Wormhole" and "Ultra Space" in enc:
            return f"{m['odds_base']} ({m['odds_charm']} charm)"
        if col == "BDSP Ramanas Park" and "Ramanas Park" in enc:
            return f"{m['odds_base']} (charm n/a)"
        if col == "SwSh Static/Gift" and game.startswith("Sword/Shield") and "Dynamax" not in enc:
            return "shiny-locked" if m["shiny_locked"] else f"{m['odds_base']} ({m['odds_charm']} charm)"
        if col == "ORAS Mirage/Static" and game.startswith("Omega Ruby"):
            return "shiny-locked" if m["shiny_locked"] else f"{m['odds_base']} ({m['odds_charm']} charm)"
        if col == "Legends Z-A Hyperspace" and "Hyperspace" in enc:
            return m["odds_charm"]
        if col == "GO Raid (RNG)" and game == "Pokémon GO" and "raid" in enc.lower():
            return m["odds_base"]
        if col == "GO Wild/Box (RNG)" and game == "Pokémon GO" and ("Mystery Box" in enc or "Evolve" in enc):
            return m["odds_base"]
        if col == "GO Research (guaranteed)" and game == "Pokémon GO" and m["cat"] == "B":
            return "guaranteed"
    if col == "Other Main-Series (legacy/roamer/breeding)":
        vals = []
        for m in p["methods"]:
            g = m["game"]
            if g in ("Pokémon GO", "Pokémon HOME"):
                continue
            if any(x in m["encounter"] for x in ("Dynamax Adventure", "Ultra Space", "Ramanas Park", "Hyperspace")):
                continue
            if g.startswith("Sword/Shield") or g.startswith("Omega Ruby"):
                continue
            if not m["shiny_locked"] and m["odds_base"] != "n/a":
                vals.append(f"{g.split('/')[0]}:{m['odds_base']}")
        return "; ".join(vals) if vals else "—"
    return "—"


def write_csv(path):
    cols = ["Pokémon", "Gen", "Category", "Form Of", "Shiny Exists?", "RNG Shiny Hunt Possible?",
            "Currently Huntable?", "Bucket(A-E)", "Games / Platforms", "Hunting Methods", "Odds",
            "Shiny Charm?", "Pokémon GO Method", "HOME Guaranteed Shiny?", "Event-Only Shiny?",
            "Notable Forms", "Notes"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for p in DATA:
            games = sorted({m["game"] for m in p["methods"]})
            methods = " | ".join(f"{m['game']}: {m['encounter']}"
                                 + (" [LOCKED]" if m["shiny_locked"] else "") for m in p["methods"])
            odds = " | ".join(
                f"{m['game']} {m['odds_base']}" + (f"->{m['odds_charm']}" if m['odds_charm'] not in ('n/a', '') else "")
                for m in p["methods"] if m["odds_base"] not in ("n/a", ""))
            charm = "; ".join(dict.fromkeys(m["charm"] for m in p["methods"] if m["charm"] not in ("n/a", "")))
            w.writerow([p["name"], p["gen"], p["category"], p["base"] or "—", yn(p["shiny_exists"]), yn(p["rng_hunt"]),
                        status_now(p), bucket(p), ", ".join(games), methods, odds or "n/a",
                        charm or "n/a", p["go"] or "—", yn(p["home_guaranteed"]), yn(p["event_only"]),
                        " ; ".join(p["forms"]) or "—", p["notes"]])
    return cols


def write_xlsx(path):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter

    wb = Workbook()
    ws = wb.active
    ws.title = "Master"
    base_cols = ["Pokémon", "Gen", "Category", "Form Of", "Shiny Exists?", "RNG Hunt Ever?", "Currently Huntable?",
                 "Bucket(A-E)", "Event-Only Shiny?", "HOME Guaranteed Shiny?", "GO Shiny?", "GO RNG-Huntable?"]
    cols = base_cols + METHOD_COLS + ["GO Summary", "Notable Forms", "Notes"]
    ws.append(cols)
    for p in DATA:
        row = [p["name"], p["gen"], p["category"], p["base"] or "—", yn(p["shiny_exists"]), yn(p["rng_hunt"]),
               status_now(p), bucket(p), yn(p["event_only"]), yn(p["home_guaranteed"]),
               yn(p["go_shiny"]), yn(p["go_rng_hunt"])]
        for col in METHOD_COLS:
            row.append(method_col_value(p, col))
        row.append(p["go"] or "—")
        row.append(" ; ".join(p["forms"]) or "—")
        row.append(p["notes"])
        ws.append(row)

    header_fill = PatternFill("solid", fgColor="1F3864")
    header_font = Font(bold=True, color="FFFFFF")
    for c in range(1, len(cols) + 1):
        cell = ws.cell(row=1, column=c)
        cell.fill, cell.font = header_fill, header_font
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{len(DATA)+1}"
    widths = {1: 15, 2: 5, 3: 12, 7: 22, len(cols): 60, len(cols) - 1: 40}
    for i in range(1, len(cols) + 1):
        ws.column_dimensions[get_column_letter(i)].width = widths.get(i, 18)
    # second sheet: legend
    leg = wb.create_sheet("Legend")
    for r in [["Bucket", "Meaning"],
              ["A", "TRUE SHINY HUNT currently possible (RNG roll/reset/raid/breed)"],
              ["E", "Shiny huntable historically but NOT currently accessible"],
              ["B", "GUARANTEED shiny reward (e.g. HOME dex reward, GO Masterwork) — not a hunt"],
              ["C", "SHINY EVENT DISTRIBUTION (predetermined shiny) — not a hunt"],
              ["D", "SHINY UNAVAILABLE — no legitimate shiny ever obtainable"],
              ["", ""],
              ["Odds ref", ""],
              ["Dynamax Adventure", "1/300 base, 1/100 with Shiny Charm (Charm applies to boss too)"],
              ["USUM Ultra Wormhole", "1/4096 base, 1/1365 charm (distance does NOT boost legendary odds)"],
              ["BDSP Ramanas Park", "1/4096 flat (Shiny Charm boosts Masuda eggs only, not legendaries)"],
              ["Z-A Hyperspace", "~1/4096 base; up to ~1/585 with Shiny Charm + Sparkling Power Lv3 donut"],
              ["GO legendary raid", "~1/20 (permaboosted)"],
              ["GO Mystery Box/DAI", "~1/125"],
              ["GO Masterwork research", "100% guaranteed (not a hunt)"],
              ["Gen 2-5 full odds", "1/8192 (no Shiny Charm pre-Gen5; ~1/2731 with charm in Gen5)"]]:
        leg.append(r)
    leg.column_dimensions["A"].width = 22
    leg.column_dimensions["B"].width = 70
    wb.save(path)
    return cols


def compute_summary():
    # species counts exclude alternate-form rows (e.g. Galarian birds) so the
    # canonical 71/23 species totals stay correct.
    core = [p for p in DATA if p["category"] in ("Legendary", "Mythical") and not p["is_form"]]
    leg = [p for p in core if p["category"] == "Legendary"]
    myth = [p for p in core if p["category"] == "Mythical"]
    ub = [p for p in DATA if p["category"] == "Ultra Beast" and not p["is_form"]]
    forms = [p for p in DATA if p["is_form"]]
    s = dict(
        total_legendary=len(leg),
        total_mythical=len(myth),
        total_combined=len(core),
        shiny_exists=sum(1 for p in core if p["shiny_exists"]),
        rng_hunt_ever=sum(1 for p in core if p["rng_hunt"]),
        huntable_now=sum(1 for p in core if p["huntable_now"]),
        historical_only=sum(1 for p in core if p["rng_hunt"] and not p["huntable_now"]),
        event_or_reward_only=sum(1 for p in core if p["shiny_exists"] and not p["rng_hunt"]),
        shiny_never=sum(1 for p in core if not p["shiny_exists"]),
        ub_total=len(ub),
        ub_huntable=sum(1 for p in ub if p["huntable_now"]),
        forms_total=len(forms),
        forms_huntable=sum(1 for p in forms if p["huntable_now"]),
    )
    # integrity check
    assert s["shiny_exists"] + s["shiny_never"] == s["total_combined"]
    assert s["rng_hunt_ever"] == s["huntable_now"] + s["historical_only"]
    return s, core, leg, myth, ub


# ---- filter predicates ----
def hunt_via(p, pred):
    return any(pred(m) and not m["shiny_locked"] and m["accessible"] and m["cat"] == "A" for m in p["methods"])

def in_da(p):
    return hunt_via(p, lambda m: "Dynamax Adventure" in m["encounter"])

def in_uw(p):
    return hunt_via(p, lambda m: "Ultra Space" in m["encounter"])

def in_bdsp(p):
    return hunt_via(p, lambda m: m["game"].startswith("Brilliant Diamond") or m["game"].startswith("Shining Pearl"))

def in_swsh_static(p):
    return hunt_via(p, lambda m: m["game"].startswith("Sword/Shield") and "Dynamax" not in m["encounter"])

def in_za(p):
    return hunt_via(p, lambda m: "Hyperspace" in m["encounter"])


def write_report(path, s, core, leg, myth, ub):
    L = []
    w = L.append
    w("# Legendary & Mythical Pokémon — Shiny-Hunt Database & Report")
    w(f"\n**Compiled / current as of:** {ACCESS_DATE}  ")
    w("**Scope:** Generations I–IX, including *Pokémon Legends: Z-A* + *Mega Dimension* DLC, "
      "Pokémon HOME, and Pokémon GO through early August 2026.  ")
    w("**Companion files:** `legendary_mythical_shiny_master.csv`, `legendary_mythical_shiny_master.xlsx` "
      "(filterable, one Pokémon per row), `sources.md`.\n")
    w("> **Data-collection caveat.** In this environment the org egress policy blocked direct page-fetching of "
      "Bulbapedia, Serebii, LeekDuck, and the Fandom wikis. Data was gathered via web-search extracts of those "
      "primary sources plus reachable secondary outlets (RotomLabs, PokémonDB, ScreenRant, Dexerto, GameRant, "
      "Game8, official pokemon.com / pokemongo.com blog posts), cross-checked across ≥2 sources for disputed "
      "cases. Post-Jan-2026 Pokémon GO specifics were verified by search where possible; a few exact 2026 dates "
      "remain approximate and are flagged. See `sources.md`.\n")

    w("## Classification & counting rules")
    w("- **Legendary vs Mythical** follows Bulbapedia's canonical split. **Type: Null & Silvally** are counted as "
      "Legendary (Bulbapedia includes them; officially 'Synthetic Pokémon'). **Phione** is counted as Mythical "
      "(Bulbapedia lists it, with caveats — it is the only breedable Mythical).")
    w("- **Ultra Beasts** (11) and **Paradox Pokémon** are their own classes and are **NOT** counted in the "
      "Legendary/Mythical totals. Ultra Beasts are included as a labeled appendix (rows in the CSV/XLSX with "
      "Category = 'Ultra Beast') because of their GO/DA/USUM shiny relevance. Paradox Pokémon are all shiny-locked "
      "in the main series and not covered as full rows (Koraidon & Miraidon, the two Paradox-associated box "
      "**Legendaries**, are included under Legendary).")
    w("- Alternate formes (Deoxys formes, Origin formes, Therian formes, etc.) are folded into their base species "
      "row with notes, not counted as separate species.\n")

    w("## Summary (COMPUTED from the database — not hand-typed)\n")
    w("| Metric | Count |")
    w("|---|---:|")
    w(f"| Total **Legendary** Pokémon | {s['total_legendary']} |")
    w(f"| Total **Mythical** Pokémon | {s['total_mythical']} |")
    w(f"| **Total combined** (Legendary + Mythical) | {s['total_combined']} |")
    w(f"| …with a legitimately obtainable **shiny form** | {s['shiny_exists']} |")
    w(f"| …with at least one **true RNG shiny hunt** (ever) | {s['rng_hunt_ever']} |")
    w(f"| …**currently** shiny-huntable (as of Aug 2026) | {s['huntable_now']} |")
    w(f"| …historically huntable but **no longer normally accessible** | {s['historical_only']} |")
    w(f"| …shiny exists **only via distribution / guaranteed reward** (never a hunt) | {s['event_or_reward_only']} |")
    w(f"| …shiny has **never** been legitimately obtainable | {s['shiny_never']} |")
    w(f"| *(Appendix)* Ultra Beasts total / currently huntable | {s['ub_total']} / {s['ub_huntable']} |")
    w(f"| *(Appendix)* Distinct alternate-form rows (e.g. Galarian birds) / huntable | {s['forms_total']} / {s['forms_huntable']} |")
    w("\n*Integrity checks (asserted at build time): shiny-exists + shiny-never = total; "
      "RNG-hunt-ever = currently-huntable + historical-only.*\n")

    # ---------------- PART 1 ----------------
    w("---\n\n# PART 1 — MASTER TABLE\n")
    w("Bucket key: **A** = true hunt available now · **E** = hunt historical only · "
      "**B** = guaranteed reward (not a hunt) · **C** = event distribution (not a hunt) · **D** = shiny unavailable.\n")
    w("| Pokémon | Gen | Category | Shiny? | RNG Hunt? | Huntable Now? | Bucket | GO Shiny (RNG?) | HOME Guar.? | Event-Only? | Key Methods |")
    w("|---|:--:|---|:--:|:--:|:--:|:--:|---|:--:|:--:|---|")
    for p in DATA:
        methods_short = []
        if in_da(p): methods_short.append("DA")
        if in_uw(p): methods_short.append("USUM")
        if in_bdsp(p): methods_short.append("BDSP")
        if in_swsh_static(p): methods_short.append("SwSh-static")
        if in_za(p): methods_short.append("Z-A")
        if p["go_rng_hunt"]: methods_short.append("GO-raid/box")
        for m in p["methods"]:
            if m["cat"] == "A" and m["accessible"] is False and not m["shiny_locked"]:
                methods_short.append("legacy")
                break
        go = "Yes" if p["go_shiny"] else "No"
        if p["go_shiny"]:
            go += " (RNG)" if p["go_rng_hunt"] else " (guar.)"
        w(f"| {p['name']} | {p['gen']} | {p['category']} | {yn(p['shiny_exists'])} | {yn(p['rng_hunt'])} | "
          f"{status_now(p)} | {bucket(p)[0]} | {go} | {yn(p['home_guaranteed'])} | {yn(p['event_only'])} | "
          f"{', '.join(dict.fromkeys(methods_short)) or '—'} |")

    # ---------------- PART 2 ----------------
    w("\n---\n\n# PART 2 — DETAILED ENTRY FOR EVERY POKÉMON\n")
    gen_order = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    form_rows_all = [p for p in DATA if p["is_form"]]
    for cat_label, group in [("Legendary & Mythical", core),
                             ("Ultra Beasts (appendix — separate class)", ub),
                             ("Alternate forms (appendix — distinct shiny status)", form_rows_all)]:
        w(f"\n## {cat_label}\n")
        ordered = sorted(group, key=lambda p: (gen_order.index(p["gen"]), p["name"]))
        for p in ordered:
            w(f"### {p['name']}\n")
            w(f"- **Classification:** {p['category']}")
            w(f"- **Generation:** {p['gen']}")
            w(f"- **Shiny exists:** {yn(p['shiny_exists'])}")
            w(f"- **Currently shiny-huntable (RNG):** {status_now(p)}")
            w(f"- **Bucket:** {bucket(p)}")
            w(f"- **HOME guaranteed-shiny reward:** {yn(p['home_guaranteed'])}  |  "
              f"**Event-only shiny:** {yn(p['event_only'])}")
            if p["is_form"]:
                w(f"- **Form of:** {p['base']} (distinct alternate form)")
            if p["forms"]:
                w(f"- **Alternate forms:** {'; '.join(p['forms'])}")
            w("\n**Hunting / shiny methods:**\n")
            for i, m in enumerate(p["methods"], 1):
                lock = "**Shiny-LOCKED**" if m["shiny_locked"] else "Not shiny-locked"
                acc = "Yes" if m["accessible"] else "No (historical / discontinued)"
                w(f"{i}. **{m['game']}** — {m['encounter']}")
                w(f"    - Shiny locked: {lock}")
                if m["odds_base"] not in ("n/a", ""):
                    w(f"    - Odds (base): {m['odds_base']}"
                      + (f"  |  with Shiny Charm: {m['odds_charm']}" if m['odds_charm'] not in ('n/a', '') else ""))
                w(f"    - Shiny Charm: {m['charm']}")
                w(f"    - Currently accessible: {acc}")
                cat_label_map = {"A": "true RNG hunt", "B": "guaranteed reward",
                                 "C": "event distribution", "D": "shiny unavailable"}
                w(f"    - Type: {m['cat']} ({cat_label_map.get(m['cat'], m['cat'])})")
                if m["note"]:
                    w(f"    - Note: {m['note']}")
            w(f"\n**Pokémon GO:** {p['go'] or 'Not in Pokémon GO.'}")
            w(f"\n**Notes:** {p['notes']}\n")

    # ---------------- FILTERED LISTS ----------------
    w("\n---\n\n# FILTERED LISTS\n")

    def names(pred, pool=DATA):
        return ", ".join(p["name"] for p in pool if pred(p)) or "(none)"

    w("### 1. Huntable through Sword/Shield **Dynamax Adventures**")
    da_list = [p for p in DATA if in_da(p)]
    w(f"*({len(da_list)} species — 1/300 base, 1/100 with Shiny Charm)*  \n" + ", ".join(p["name"] for p in da_list) + "\n")

    w("### 2. Huntable in **Ultra Sun / Ultra Moon** (Ultra Wormholes)")
    uw_list = [p for p in DATA if in_uw(p)]
    w(f"*({len(uw_list)} species — 1/4096, 1/1365 charm; distance does NOT boost legendary odds)*  \n"
      + ", ".join(p["name"] for p in uw_list) + "\n")

    w("### 3. Huntable in **Brilliant Diamond / Shining Pearl** (Ramanas Park & wild statics)")
    bd_list = [p for p in DATA if in_bdsp(p)]
    w(f"*({len(bd_list)} species — 1/4096 flat; Shiny Charm does NOT help wild/legendary hunts in BDSP)*  \n"
      + ", ".join(p["name"] for p in bd_list) + "\n")

    w("### 4. Huntable through **Sword/Shield static** encounters (non-DA)")
    ss_list = [p for p in DATA if in_swsh_static(p)]
    w(f"*({len(ss_list)} species — Crown Tundra Regis/Regieleki/Regidrago + roaming Forces of Nature; 1/4096, 1/1365 charm)*  \n"
      + ", ".join(p["name"] for p in ss_list) + "\n")

    w("### 4b. Huntable through **Legends: Z-A Mega Dimension** (Hyperspace Distortions, NEW 2026)")
    za_list = [p for p in DATA if in_za(p)]
    w(f"*({len(za_list)} species — up to ~1/585 with Shiny Charm + Sparkling Power Lv3 donut)*  \n"
      + ", ".join(p["name"] for p in za_list) + "\n")

    w("### 5. Ever genuinely **RNG shiny-huntable in Pokémon GO** (raids / Mystery Box / wild)")
    go_list = [p for p in DATA if p["go_rng_hunt"]]
    w(f"*({len(go_list)} species — mostly ~1/20 legendary raids; Meltan/Galarian birds ~1/125)*  \n"
      + ", ".join(p["name"] for p in go_list) + "\n")
    w("> Guaranteed-only GO shinies (NOT hunts): "
      + ", ".join(p["name"] for p in DATA if p["go_shiny"] and not p["go_rng_hunt"] and p["category"] in ("Legendary", "Mythical")) + ".\n")

    w("### 6. **Mythical** Pokémon that can legitimately be shiny-**hunted** (true RNG, ever)")
    myth_hunt = [p for p in myth if p["rng_hunt"]]
    w(f"*({len(myth_hunt)} of {len(myth)} Mythicals)*  \n"
      + ", ".join(f"{p['name']} ({'current' if p['huntable_now'] else 'historical'})" for p in myth_hunt) + "\n")

    w("### 7. Shiny **still completely unavailable** (no legitimate shiny ever)")
    never = [p for p in DATA if not p["shiny_exists"]]
    w(f"*({len(never)} species incl. Ultra Beasts)*  \n" + ", ".join(p["name"] for p in never) + "\n")

    w("### 8. Shiny **exists but only via guaranteed / event distribution** (never a hunt)")
    eo = [p for p in core if p["shiny_exists"] and not p["rng_hunt"]]
    w(f"*({len(eo)} species)*  \n" + ", ".join(p["name"] for p in eo) + "\n")

    w("### 9. **Currently huntable** without needing an expired event (as of Aug 2026)")
    now = [p for p in DATA if p["huntable_now"]]
    w(f"*({len(now)} species incl. Ultra Beasts; {sum(1 for p in core if p['huntable_now'])} core Legendary/Mythical)*  \n"
      + ", ".join(p["name"] for p in now) + "\n")

    w("### 9b. Distinct alternate **forms** with their own shiny status (broken out as separate rows)")
    form_rows = [p for p in DATA if p["is_form"]]
    w(f"*({len(form_rows)} forms)*  \n"
      + ", ".join(f"{p['name']} (form of {p['base']} — {status_now(p).split(' ')[0].lower()})" for p in form_rows)
      + ".  \nOther legendaries with alternate formes that share their base species' shiny status "
        "(documented in each entry, not split out): Deoxys, Dialga, Palkia, Giratina, Shaymin, "
        "Tornadus, Thundurus, Landorus, Kyurem, Zacian, Zamazenta, Necrozma, Calyrex, Urshifu, "
        "Zygarde, Hoopa, Meloetta, Genesect, Enamorus, Keldeo, Ogerpon, Terapagos.\n")

    w("### 10. Best games / platforms for hunting the most Legendary/Mythical shinies")
    plat = {
        "Pokémon GO (raids/box, RNG)": sum(1 for p in DATA if p["go_rng_hunt"]),
        "Sword/Shield Dynamax Adventures": len(da_list),
        "Ultra Sun/Ultra Moon Ultra Wormholes": len(uw_list),
        "Brilliant Diamond/Shining Pearl": len(bd_list),
        "Omega Ruby/Alpha Sapphire (Mirage Spots)": sum(1 for p in DATA if hunt_via(p, lambda m: m["game"].startswith("Omega Ruby"))),
        "Sword/Shield static (Crown Tundra)": len(ss_list),
        "Legends Z-A Mega Dimension": len(za_list),
    }
    w("| Rank | Platform | # Legendary/Mythical/UB shinies huntable |")
    w("|---:|---|---:|")
    for i, (k, v) in enumerate(sorted(plat.items(), key=lambda kv: -kv[1]), 1):
        w(f"| {i} | {k} | {v} |")
    w("\n**Takeaway:** *Pokémon GO* (raids) covers the largest raw number of species, but every GO raid shiny is a "
      "~1/20 roll with no Shiny Charm. *Dynamax Adventures* is the single best **main-series** platform — huge roster "
      "at the best odds (1/100 with charm). *Ultra Wormholes* cover the widest Gen 1–6 main-series set (though at "
      "1/1365). For the newest additions, *Legends Z-A Mega Dimension* (2026) is the only place to hunt shiny "
      "Lati@s / Swords of Justice in a modern main-series title.\n")

    # ---------------- VALIDATION ----------------
    w("\n---\n\n# VALIDATION PASS\n")
    seen = {}
    dups = []
    for p in DATA:
        seen[p["name"]] = seen.get(p["name"], 0) + 1
    dups = [n for n, c in seen.items() if c > 1]
    w(f"- **Every species appears exactly once:** {'PASS' if not dups else 'FAIL: ' + ', '.join(dups)} "
      f"({len(DATA)} rows, {len(seen)} unique names).")
    w(f"- **Counts reconcile:** shiny-exists ({s['shiny_exists']}) + shiny-never ({s['shiny_never']}) = "
      f"{s['shiny_exists'] + s['shiny_never']} = total ({s['total_combined']}) — PASS.")
    w(f"- **Hunt counts reconcile:** current ({s['huntable_now']}) + historical-only ({s['historical_only']}) = "
      f"{s['huntable_now'] + s['historical_only']} = RNG-hunt-ever ({s['rng_hunt_ever']}) — PASS.")
    w("- **Guaranteed rewards are never counted as hunts:** HOME dex-reward shinies (Meloetta, Keldeo, Meltan*, "
      "Volcanion) and GO Masterwork shinies (Mew, Celebi, Jirachi, Shaymin, Meloetta, Keldeo, Diancie) are recorded "
      "as Bucket B, and are excluded from `rng_hunt`. (*Meltan also has a real Mystery Box RNG hunt, so it is Bucket A.)")
    w("- **'Currently huntable' claims** are based on Aug-2026 game/service availability: SwSh+DLC, BDSP, USUM/ORAS "
      "(3DS cartridge; eShop closed Mar 2023 but carts play), Legends Z-A + Mega Dimension DLC, and GO raid rotations. "
      "Discontinued-only routes (Gen 2 VC, Gen 3/4 event-island tickets, Pokémon Ranger egg) are marked historical.")
    w("- **Known uncertainties (flagged in notes):** exact GO first-shiny dates for a few long-standing raid "
      "legendaries; Regidrago/Cosmog GO shiny status; the disputed BDSP Azure-Flute Arceus claim (treated as "
      "no-legit-shiny). Negative 'no shiny' claims for in-GO species can flip at any future event.")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


def write_sources(path):
    src = f"""# Sources & References

**All web sources accessed:** {ACCESS_DATE} (August 9, 2026).

## Environment / verification caveat
Direct page-fetching (WebFetch/curl) of **Bulbapedia, Serebii, LeekDuck, pokemongohub, and the Fandom wikis** was
**blocked by this session's egress policy** (HTTP 403 at the proxy). Their content was therefore obtained through
**web-search result extracts** that quote/summarize those same primary pages, corroborated with **reachable
secondary sources**. Every disputed data point was cross-checked against **at least two** independent results.
Where a fact could only be sourced to a single secondary outlet, or is a post-January-2026 GO detail that could
not be pinned to an exact date, it is flagged *(verify)* in the report notes.

## Primary references (game mechanics, classification, shiny locks)
- Bulbapedia — *Legendary Pokémon*, *Mythical Pokémon*, *Ultra Beast*, *Paradox Pokémon*, *List of unobtainable Shiny Pokémon*, *Shiny Pokémon (GO)* (via search extract; direct fetch egress-blocked)
- Serebii.net — legendary/event pages for USUM, ORAS, SwSh (Dynamax Adventure Pokémon), BDSP, SV, Legends Arceus, Legends Z-A, Pokémon GO, Mystery Box (via search extract)
- RotomLabs — Crown Tundra / Dynamax Adventure shiny-rate datamine; Legends Z-A Mega Dimension shiny rates
- PokémonDB PokéBase — USUM shiny-lock list; BDSP legendary shiny; Original-Color Magearna shiny-lock

## Dynamax Adventures (SwSh) — odds & roster
- ScreenRant — Crown Tundra shiny-odds datamine (SciresM): https://screenrant.com/pokemon-crown-tundra-shiny-odds-dynamax-adventure-sword-shield/
- RotomLabs — https://rotomlabs.net/guide/crown-tundra-shiny-legendary-hunting , https://rotomlabs.net/article/dynamax-adventures-shiny-rates-revealed-by-dataminers
- Dexerto — https://www.dexerto.com/pokemon/how-to-get-shiny-legendary-pokemon-in-crown-tundra-dynamax-adventures-1440964/
- Dot Esports — https://dotesports.com/pokemon/news/what-are-the-shiny-odds-in-pokemon-sword-and-shields-the-crown-tundra-dynamax-adventures
- RPGSite (full DA legendary list) — https://www.rpgsite.net/feature/10409-pokemon-sword-shield-all-legendary-pokemon-available-via-dynamax-adventure-pokemon-dens
- **Verified correction:** the Shiny Charm improves the DA legendary boss (1/300 → 1/100); it is not charm-independent.

## Ultra Wormholes (USUM)
- Gameranx — https://gameranx.com/features/id/128376/article/pokemon-ultra-sun-moon-how-to-catch-every-legendary-pokemon-ultra-wormholes-guide/
- RotomLabs — https://rotomlabs.net/guide/ultra-wormhole-shiny-hunting
- Smogon — Ultra Space guide (odds mechanics)
- **Verified:** legendaries roll at 1/4096 (1/1365 charm); wormhole distance does NOT boost legendary shiny odds.

## Ramanas Park (BDSP)
- Game8 — https://game8.co/games/Pokemon-Brilliant-Diamond-Shining-Pearl/archives/349609
- NintendoLife — https://www.nintendolife.com/guides/pokemon-brilliant-diamond-and-shining-pearl-legendary-pokemon-how-to-catch-17-legendaries-in-ramanas-park
- TheGamer / GamesLearningSociety — BDSP Shiny-Charm quirk (Masuda eggs only)
- **Verified:** Dialga/Palkia/Giratina are huntable in Ramanas Park; Charm does not aid wild/legendary hunts.

## Legends: Arceus / Scarlet-Violet / Legends Z-A shiny locks
- ScreenRant / Game8 — PLA shiny-locked list
- GameRant — https://gamerant.com/every-pokemon-scarlet-violet-shiny-locked-gen-9-legendary-mythical-paradox/
- NintendoEverything — every shiny-locked Pokémon (updated)
- VGC — https://www.videogameschronicle.com/guide/pokemon-legends-z-a-shiny-lock-all-shiny-locked-pokemon-in-pokemon-legends-z-a/
- Dexerto — https://www.dexerto.com/wikis/pokemon-legends-z-a/all-shiny-locked-pokemon-pokemon-legends-z-a/

## Legends: Z-A Mega Dimension (NEW 2026 shiny hunt)
- GameRant — "Catch Five Shiny Legendaries in Pokemon Legends Z-A Mega Dimension": https://gamerant.com/pokemon-legends-za-shiny-hunt-legendaries-mega-dimension-plza/
- TheGamer — https://www.thegamer.com/pokemon-legends-z-a-shiny-legendaries-mythical-sparkling-power-donut-guide/ , https://www.thegamer.com/pokemon-legends-z-a-mega-dimension-shiny-hunting-methods/
- Game8 — https://game8.co/games/Pokemon-Legends-Z-A/archives/571120 , https://game8.co/games/Pokemon-Legends-Z-A/archives/572829
- RotomLabs — Mega Dimension shiny rates: https://rotomlabs.net/article/shiny-rates-for-legends-z-a-mega-dimension-dlc
- Vice — https://www.vice.com/en/article/pokemon-legends-z-a-dlc-finally-adds-shiny-legendary-pokemon-full-list-explained/
- **Verified:** Latias, Latios, Cobalion, Terrakion, Virizion are the 5 non-shiny-locked legendaries; caught in 5-star
  Hyperspace Distortions (Philippe Special Scan, post Main Mission 12); ~1/585 with Shiny Charm + Sparkling Power Lv3.
  PokéBeach / pokemon.com confirm the DLC added Mega Evolutions only (incl. Mega Zeraora) — **no new species**.

## Pokémon HOME guaranteed-shiny dex rewards
- pokemon.com — "Complete Pokédexes to Earn Shiny Keldeo and Shiny Meltan in Pokémon HOME": https://www.pokemon.com/us/news/complete-pokedexes-to-earn-shiny-keldeo-and-shiny-meltan-in-pokemon-home
- NintendoEverything — HOME Shiny Meloetta distribution
- PokéGO Hub — HOME exclusive shiny distributions (Volcanion, Apr 2026): https://pokemongohub.net/post/sword-shield/pokemon-home-exclusive-shiny-distributions/
- PokémonDB / Inverse — Original-Color Magearna is a FORM (shiny-locked), not a shiny.

## Pokémon GO shiny releases (dates, methods, current status)
- Fandom — *List of Shiny Pokémon release dates*: https://pokemongo.fandom.com/wiki/List_of_Shiny_Pok%C3%A9mon_release_dates
- win.gg — all shiny Pokémon in GO (2026): https://win.gg/shiny-pokemon-go-list/
- LeekDuck GO Fest 2026 shiny list: https://leekduck.com/gofest/shiny/
- Shiny Lugia/Ho-Oh (first shiny legendary): https://comicbook.com/gaming/news/pokemon-go-shiny-lugia/
- Guaranteed Masterwork Mythicals: Mew (All-in-One #151), Celebi, Jirachi (Wish Granted), Shaymin (Glimmers of Gratitude), Meloetta (A Dazzling Aria), Keldeo (Pony Tales, Nov 2025), Diancie (Sparkle and Shine, GO Tour Kalos, Feb 2026) — LeekDuck / PokéGO Hub / pokemon.com event pages
- RNG raid Mythicals/legendaries: Darkrai, Genesect (by Drive), Deoxys (all formes), Necrozma (raids Aug 2025), Solgaleo (Jul 22 2026), Lunala (~Jul 2026), Zacian/Zamazenta (Sep/Oct 2024), Regieleki (Nov 2024)
- Ultra Beast shinies (GO Fest 2024 → Apr 2025): PokéGO Hub, Sportskeeda; Poipole/Naganadel shiny-locked
- Meltan / Mystery Box: https://www.dexerto.com/pokemon/how-to-get-shiny-meltan-in-pokemon-go-1456253/ , https://www.serebii.net/pokemongo/mysterybox.shtml
- 2026 events: GO Fest 2026 (Mega Mewtwo X/Y, Zeraora), Solgaleo/Mega Rayquaza raid weekend (Jul 2026) — pokemongo.com / pokemongohub.net / bristoledition.org

## Shiny Koraidon / Miraidon distribution (2025)
- pokemon.com — "Get Shiny Koraidon or Shiny Miraidon at GameStop and EB Games": https://www.pokemon.com/us/news/get-shiny-koraidon-or-shiny-miraidon-at-gamestop-and-eb-games
- GameSpot — Free Shiny Koraidon/Miraidon, Sep 26–Oct 15 2025: https://www.gamespot.com/articles/get-a-free-shiny-koraidon-and-miraidon-in-pokemon-scarlet-and-violet/1100-6534715/
- **Guaranteed serial-code distribution (Sep 26–Oct 15, 2025); shiny is fixed, not RNG-huntable.**

## Obtainment-channel audit — HOME rewards & event distributions (2026-08-10)
- HOME guaranteed-shiny rewards (4): Meloetta (Oct 2024), Keldeo + Meltan (Feb 2025), Volcanion (Apr 2026). Magearna's HOME reward is Original-Color (a form), NOT shiny.
  - pokemon.com — Shiny Volcanion for Legends Z-A dexes; Shiny Keldeo & Meltan; Pokémon Press — Shiny Meloetta.
- Guaranteed-shiny EVENT distributions (Legendary/Mythical): Shiny beasts Raikou/Entei/Suicune (2011), Genesect (2013), Diancie (2016), Tapu Koko/Lele/Bulu/Fini (2019 competitions), Zeraora (2020 HOME raid-milestone), Celebi (2021 movie promo), Zacian/Zamazenta (2021–22), Galarian Articuno/Zapdos/Moltres (2022 competitions), Silvally (2017 GameStop/GAME/EB), Koraidon/Miraidon (2025).
  - pocketmonsters.net / pokemonblog.com / mynintendonews / nintendowire — Shiny Silvally 2017 distribution (confirmed by 5+ outlets).
  - pokemonblog.com — Shiny Zeraora HOME distribution (Jun–Jul 2020); Dada Zarude & Shiny Celebi codes (2021).
  - Nintendo Life / PokéBeach — Shiny legendary beasts GameStop (2011).
- Random-shiny (self-caught, NOT guaranteed) distributions: Jirachi (WISHMKR bonus disc, 2003–04) and Mew (Old Sea Map / Faraway Island, JP Emerald 2005) are soft-reset RNG, not shiny-locked — genuine (historical) hunts, not guaranteed shinies.
- Verified NOT huntable / no shiny: Type: Null & Silvally's in-game gifts are shiny-locked in every game (SM/USUM/SwSh/SV Indigo Disk); Zygarde is shiny-locked in every story/static/cell encounter — BUT shiny Zygarde IS obtainable via Sword/Shield Dynamax Adventures (Max Lair), the sole hunt route.

## Older-game historical hunts
- PokéCommunity Daily — Gen 2 shiny guide (Crystal VC, roamers): https://daily.pokecommunity.com/2018/01/26/generation-2-shiny-guide/
- SuperCheats — Celebi shiny unlocked on Crystal VC (GS Ball): https://www.supercheats.com/articles/770/celebi-is-shiny-locked-no-more
- ScreenRant — Manaphy shiny hunt (Ranger egg): https://screenrant.com/pokemon-shiny-hunt-manaphy-guide/
- Gen 3 event islands (Navel Rock, Birth Island, Faraway Island) and Gen 4 event statics (Newmoon Island/Member Card, Flower Paradise/Oak's Letter) — Serebii event archives (via search); all pre-Gen-5, so not shiny-locked, but the distribution items are discontinued.
- ORAS Mirage Spot legendaries not shiny-locked — GameFAQs / Serebii.

## Notes on disputed cases
- **Dynamax Adventure Shiny Charm** — corrected: Charm DOES improve the boss (1/300→1/100).
- **Kubfu/Urshifu classification** — debated (some group with Legendaries); counted here as Legendary per Bulbapedia inclusion. Shiny is unavailable regardless.
- **Arceus shiny (BDSP Azure Flute)** — a single outlet claims it is not shiny-locked; widely disputed/unreliable, so treated as no-legit-shiny.
- **Shiny Kyogre GO first-release date** — sources split 2018 vs 2019; RNG-raid status is certain.
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(src)


def write_json(path, s):
    import json
    mons = []
    for p in DATA:
        mons.append(dict(
            name=p["name"], gen=p["gen"], category=p["category"],
            is_form=p["is_form"], base=p["base"], forms=p["forms"], go_form_only=p["go_form_only"],
            shiny_exists=p["shiny_exists"], rng_hunt=p["rng_hunt"], huntable_now=p["huntable_now"],
            event_only=p["event_only"], home_guaranteed=p["home_guaranteed"],
            go_shiny=p["go_shiny"], go_rng_hunt=p["go_rng_hunt"],
            src_home_ot=p["src_home_ot"], src_home_reward=p["src_home_reward"],
            src_home_event=p["src_home_event"], src_go=p["src_go"],
            bucket=bucket(p)[0], bucket_full=bucket(p), status=status_now(p),
            in_da=in_da(p), in_uw=in_uw(p), in_bdsp=in_bdsp(p), in_swsh=in_swsh_static(p), in_za=in_za(p),
            go=p["go"], notes=p["notes"],
            methods=[dict(game=m["game"], encounter=m["encounter"], locked=m["shiny_locked"],
                          base=m["odds_base"], charm=m["odds_charm"], charm_eff=m["charm"],
                          accessible=m["accessible"], cat=m["cat"], note=m["note"]) for m in p["methods"]],
        ))
    json.dump(dict(access_date=ACCESS_DATE, summary=s, mons=mons),
              open(path, "w", encoding="utf-8"), ensure_ascii=False)


if __name__ == "__main__":
    write_csv(os.path.join(HERE, "legendary_mythical_shiny_master.csv"))
    write_xlsx(os.path.join(HERE, "legendary_mythical_shiny_master.xlsx"))
    s, core, leg, myth, ub = compute_summary()
    write_report(os.path.join(HERE, "legendary_mythical_shiny_report.md"), s, core, leg, myth, ub)
    write_sources(os.path.join(HERE, "sources.md"))
    write_json(os.path.join(HERE, "data.json"), s)
    print(f"Total rows: {len(DATA)} (species core {len(core)}, UB {len(ub)}, forms {s['forms_total']})")
    for k, v in s.items():
        print(f"  {k}: {v}")
    # source-channel tallies (all rows)
    for key, lab in [("src_home_ot", "Home OT"), ("src_home_reward", "Home Reward"),
                     ("src_home_event", "Home Event"), ("src_go", "GO")]:
        print(f"  source[{lab}]: {sum(1 for p in DATA if p[key])}")
    if _WARN:
        print("WARNINGS:")
        for wln in _WARN:
            print("  ! " + wln)
    print("Wrote: CSV, XLSX, report.md, sources.md, data.json")
