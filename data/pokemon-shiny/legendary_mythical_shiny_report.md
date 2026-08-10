# Legendary & Mythical Pokémon — Shiny-Hunt Database & Report

**Compiled / current as of:** 2026-08-09  
**Scope:** Generations I–IX, including *Pokémon Legends: Z-A* + *Mega Dimension* DLC, Pokémon HOME, and Pokémon GO through early August 2026.  
**Companion files:** `legendary_mythical_shiny_master.csv`, `legendary_mythical_shiny_master.xlsx` (filterable, one Pokémon per row), `sources.md`.

> **Data-collection caveat.** In this environment the org egress policy blocked direct page-fetching of Bulbapedia, Serebii, LeekDuck, and the Fandom wikis. Data was gathered via web-search extracts of those primary sources plus reachable secondary outlets (RotomLabs, PokémonDB, ScreenRant, Dexerto, GameRant, Game8, official pokemon.com / pokemongo.com blog posts), cross-checked across ≥2 sources for disputed cases. Post-Jan-2026 Pokémon GO specifics were verified by search where possible; a few exact 2026 dates remain approximate and are flagged. See `sources.md`.

## Classification & counting rules
- **Legendary vs Mythical** follows Bulbapedia's canonical split. **Type: Null & Silvally** are counted as Legendary (Bulbapedia includes them; officially 'Synthetic Pokémon'). **Phione** is counted as Mythical (Bulbapedia lists it, with caveats — it is the only breedable Mythical).
- **Ultra Beasts** (11) and **Paradox Pokémon** are their own classes and are **NOT** counted in the Legendary/Mythical totals. Ultra Beasts are included as a labeled appendix (rows in the CSV/XLSX with Category = 'Ultra Beast') because of their GO/DA/USUM shiny relevance. Paradox Pokémon are all shiny-locked in the main series and not covered as full rows (Koraidon & Miraidon, the two Paradox-associated box **Legendaries**, are included under Legendary).
- Alternate formes (Deoxys formes, Origin formes, Therian formes, etc.) are folded into their base species row with notes, not counted as separate species.

## Summary (COMPUTED from the database — not hand-typed)

| Metric | Count |
|---|---:|
| Total **Legendary** Pokémon | 71 |
| Total **Mythical** Pokémon | 23 |
| **Total combined** (Legendary + Mythical) | 94 |
| …with a legitimately obtainable **shiny form** | 65 |
| …with at least one **true RNG shiny hunt** (ever) | 58 |
| …**currently** shiny-huntable (as of Aug 2026) | 54 |
| …historically huntable but **no longer normally accessible** | 4 |
| …shiny exists **only via distribution / guaranteed reward** (never a hunt) | 7 |
| …shiny has **never** been legitimately obtainable | 29 |
| *(Appendix)* Ultra Beasts total / currently huntable | 11 / 9 |
| *(Appendix)* Distinct alternate-form rows (e.g. Galarian birds) / huntable | 3 / 3 |

*Integrity checks (asserted at build time): shiny-exists + shiny-never = total; RNG-hunt-ever = currently-huntable + historical-only.*

---

# PART 1 — MASTER TABLE

Bucket key: **A** = true hunt available now · **E** = hunt historical only · **B** = guaranteed reward (not a hunt) · **C** = event distribution (not a hunt) · **D** = shiny unavailable.

| Pokémon | Gen | Category | Shiny? | RNG Hunt? | Huntable Now? | Bucket | GO Shiny (RNG?) | HOME Guar.? | Event-Only? | Key Methods |
|---|:--:|---|:--:|:--:|:--:|:--:|---|:--:|:--:|---|
| Articuno | I | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box |
| Zapdos | I | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box |
| Moltres | I | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box |
| Mewtwo | I | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | USUM, BDSP, GO-raid/box |
| Mew | I | Mythical | Yes | No | No | B | Yes (guar.) | No | Yes | — |
| Raikou | II | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Entei | II | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Suicune | II | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Lugia | II | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Ho-Oh | II | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Celebi | II | Mythical | Yes | Yes | No (historical only) | E | Yes (guar.) | No | No | legacy |
| Regirock | III | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, SwSh-static, GO-raid/box, legacy |
| Regice | III | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, SwSh-static, GO-raid/box, legacy |
| Registeel | III | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, SwSh-static, GO-raid/box, legacy |
| Latias | III | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, Z-A, GO-raid/box, legacy |
| Latios | III | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, Z-A, GO-raid/box, legacy |
| Kyogre | III | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Groudon | III | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Rayquaza | III | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box, legacy |
| Jirachi | III | Mythical | Yes | Yes | No (historical only) | E | Yes (guar.) | No | No | legacy |
| Deoxys | III | Mythical | Yes | Yes | Yes | A | Yes (RNG) | No | No | GO-raid/box, legacy |
| Uxie | IV | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Mesprit | IV | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Azelf | IV | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Dialga | IV | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Palkia | IV | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Heatran | IV | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Regigigas | IV | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | BDSP, GO-raid/box, legacy |
| Giratina | IV | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Cresselia | IV | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, BDSP, GO-raid/box, legacy |
| Phione | IV | Mythical | Yes | Yes | Yes | A | No | No | No | — |
| Manaphy | IV | Mythical | Yes | Yes | No (historical only) | E | No | No | No | legacy |
| Darkrai | IV | Mythical | Yes | Yes | Yes | A | Yes (RNG) | No | No | GO-raid/box, legacy |
| Shaymin | IV | Mythical | Yes | Yes | No (historical only) | E | Yes (guar.) | No | No | legacy |
| Arceus | IV | Mythical | No | No | No | D | No | No | No | — |
| Victini | V | Mythical | No | No | No | D | No | No | No | — |
| Cobalion | V | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, Z-A, GO-raid/box, legacy |
| Terrakion | V | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, Z-A, GO-raid/box, legacy |
| Virizion | V | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, Z-A, GO-raid/box, legacy |
| Tornadus | V | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, SwSh-static, GO-raid/box, legacy |
| Thundurus | V | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, SwSh-static, GO-raid/box, legacy |
| Landorus | V | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, SwSh-static, GO-raid/box, legacy |
| Reshiram | V | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box, legacy |
| Zekrom | V | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box, legacy |
| Kyurem | V | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box, legacy |
| Keldeo | V | Mythical | Yes | No | No | B | Yes (guar.) | Yes | Yes | — |
| Meloetta | V | Mythical | Yes | No | No | B | Yes (guar.) | Yes | Yes | — |
| Genesect | V | Mythical | Yes | Yes | Yes | A | Yes (RNG) | No | No | GO-raid/box |
| Xerneas | VI | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box |
| Yveltal | VI | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box |
| Zygarde | VI | Legendary | No | No | No | D | No | No | No | — |
| Diancie | VI | Mythical | Yes | No | No | B | Yes (guar.) | No | Yes | — |
| Hoopa | VI | Mythical | No | No | No | D | No | No | No | — |
| Volcanion | VI | Mythical | Yes | No | No | B | No | Yes | Yes | — |
| Type: Null | VII | Legendary | No | No | No | D | No | No | No | — |
| Silvally | VII | Legendary | No | No | No | D | No | No | No | — |
| Tapu Koko | VII | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, GO-raid/box |
| Tapu Lele | VII | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, GO-raid/box |
| Tapu Bulu | VII | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, GO-raid/box |
| Tapu Fini | VII | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, GO-raid/box |
| Cosmog | VII | Legendary | No | No | No | D | No | No | No | — |
| Cosmoem | VII | Legendary | No | No | No | D | No | No | No | — |
| Solgaleo | VII | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, GO-raid/box |
| Lunala | VII | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, GO-raid/box |
| Necrozma | VII | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, GO-raid/box |
| Magearna | VII | Mythical | No | No | No | D | No | No | No | — |
| Marshadow | VII | Mythical | No | No | No | D | No | No | No | — |
| Zeraora | VII | Mythical | No | No | No | D | No | No | No | — |
| Meltan | VII | Mythical | Yes | Yes | Yes | A | Yes (RNG) | Yes | No | GO-raid/box |
| Melmetal | VII | Mythical | Yes | Yes | Yes | A | Yes (RNG) | No | No | GO-raid/box |
| Zacian | VIII | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | GO-raid/box |
| Zamazenta | VIII | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | GO-raid/box |
| Eternatus | VIII | Legendary | No | No | No | D | No | No | No | — |
| Kubfu | VIII | Legendary | No | No | No | D | No | No | No | — |
| Urshifu | VIII | Legendary | No | No | No | D | No | No | No | — |
| Regieleki | VIII | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | SwSh-static, GO-raid/box |
| Regidrago | VIII | Legendary | Yes | Yes | Yes | A | No | No | No | SwSh-static |
| Glastrier | VIII | Legendary | No | No | No | D | No | No | No | — |
| Spectrier | VIII | Legendary | No | No | No | D | No | No | No | — |
| Calyrex | VIII | Legendary | No | No | No | D | No | No | No | — |
| Enamorus | VIII | Legendary | No | No | No | D | No | No | No | — |
| Zarude | VIII | Mythical | No | No | No | D | No | No | No | — |
| Koraidon | IX | Legendary | Yes | No | No | C | No | No | Yes | — |
| Miraidon | IX | Legendary | Yes | No | No | C | No | No | Yes | — |
| Wo-Chien | IX | Legendary | No | No | No | D | No | No | No | — |
| Chien-Pao | IX | Legendary | No | No | No | D | No | No | No | — |
| Ting-Lu | IX | Legendary | No | No | No | D | No | No | No | — |
| Chi-Yu | IX | Legendary | No | No | No | D | No | No | No | — |
| Okidogi | IX | Legendary | No | No | No | D | No | No | No | — |
| Munkidori | IX | Legendary | No | No | No | D | No | No | No | — |
| Fezandipiti | IX | Legendary | No | No | No | D | No | No | No | — |
| Ogerpon | IX | Legendary | No | No | No | D | No | No | No | — |
| Terapagos | IX | Legendary | No | No | No | D | No | No | No | — |
| Pecharunt | IX | Mythical | No | No | No | D | No | No | No | — |
| Nihilego | VII | Ultra Beast | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box |
| Buzzwole | VII | Ultra Beast | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box |
| Pheromosa | VII | Ultra Beast | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box |
| Xurkitree | VII | Ultra Beast | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box |
| Celesteela | VII | Ultra Beast | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box |
| Kartana | VII | Ultra Beast | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box |
| Guzzlord | VII | Ultra Beast | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box |
| Stakataka | VII | Ultra Beast | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box |
| Blacephalon | VII | Ultra Beast | Yes | Yes | Yes | A | Yes (RNG) | No | No | DA, USUM, GO-raid/box |
| Poipole | VII | Ultra Beast | No | No | No | D | No | No | No | — |
| Naganadel | VII | Ultra Beast | No | No | No | D | No | No | No | — |
| Galarian Articuno | VIII | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | GO-raid/box |
| Galarian Zapdos | VIII | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | GO-raid/box |
| Galarian Moltres | VIII | Legendary | Yes | Yes | Yes | A | Yes (RNG) | No | No | GO-raid/box |

---

# PART 2 — DETAILED ENTRY FOR EVERY POKÉMON


## Legendary & Mythical

### Articuno

- **Classification:** Legendary
- **Generation:** I
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Galarian Articuno — see its own row (Gen VIII, GO-only shiny)

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Let's Go Pikachu/Eevee** — Overworld static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Not shiny-locked in LGPE
5. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jul 2019; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Jul 2019); ~1/20; rotates

**Notes:** Kanto birds broadly huntable. Galarian Articuno (Gen 8) is a separate, shiny-locked static in SwSh but shiny via GO Daily Adventure Incense.

### Mew

- **Classification:** Mythical
- **Generation:** I
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** No
- **Bucket:** B (guaranteed reward)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** Yes

**Hunting / shiny methods:**

1. **Pokémon GO** — Masterwork Research 'All-in-One #151' (guaranteed shiny reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 100% (guaranteed)
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: B (guaranteed reward)
    - Note: Shiny since Jul 6 2023; one guaranteed shiny, NOT rollable
2. **Main series** — Event distributions
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: C (event distribution)
    - Note: All legit main-series Mew are shiny/IV-locked; no soft-reset hunt

**Pokémon GO:** Shiny via 'All-in-One #151' Masterwork (guaranteed; $5). Not RNG-huntable.

**Notes:** No legitimate main-series shiny Mew has ever existed. Shiny exists only as a guaranteed GO reward.

### Mewtwo

- **Classification:** Legendary
- **Generation:** I
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
2. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
3. **Let's Go Pikachu/Eevee** — Cerulean Cave static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Not shiny-locked in LGPE
4. **Sword/Shield (Crown Tundra)** — Dynamax Adventure special boss
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: Mewtwo's Dynamax Adventure appearance is SHINY-LOCKED (unlike other DA bosses)
5. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Sep 16 2019; rotates through raids; Mega Mewtwo X/Y shiny debuted GO Fest 2026

**Pokémon GO:** Legendary raids (shiny since Sep 2019); Mega X/Y shiny GO Fest 2026; ~1/20

**Notes:** Huntable via USUM, Ramanas Park, LGPE, and GO raids. NOTE its Dynamax Adventure form is shiny-locked.

### Moltres

- **Classification:** Legendary
- **Generation:** I
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Galarian Moltres — see its own row (Gen VIII, GO-only shiny)

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Let's Go Pikachu/Eevee** — Overworld static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
5. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jul 2019; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Jul 2019); ~1/20; rotates

**Notes:** See Articuno note re: Galarian form.

### Zapdos

- **Classification:** Legendary
- **Generation:** I
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Galarian Zapdos — see its own row (Gen VIII, GO-only shiny)

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Let's Go Pikachu/Eevee** — Overworld static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
5. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jul 2019; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Jul 2019); ~1/20; rotates

**Notes:** See Articuno note re: Galarian form.

### Celebi

- **Classification:** Mythical
- **Generation:** II
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** No (historical only)
- **Bucket:** E (hunt, historical only)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Crystal (Virtual Console)** — GS Ball event static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: GS-Ball Celebi in VC Crystal is NOT shiny-locked -> genuine soft-reset hunt. eShop closed Mar 2023 (historical)
2. **Pokémon GO** — Special Research 'Distracted by Something Shiny' (re-run as Masterwork) (guaranteed shiny reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 100% (guaranteed)
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: B (guaranteed reward)
    - Note: Shiny since Dec 14 2020; one guaranteed shiny, NOT rollable

**Pokémon GO:** Shiny via Special/Masterwork Research (guaranteed). Not RNG in GO.

**Notes:** Rare Mythical with a real (historical) RNG hunt: VC Crystal GS-Ball Celebi. No longer accessible (VC discontinued).

### Entei

- **Classification:** Legendary
- **Generation:** II
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
5. **Crystal (VC) / HGSS** — Roaming (locks on first sighting)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical; VC discontinued
6. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jul 14 2019; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Jul 2019); ~1/20; rotates

**Notes:** 

### Ho-Oh

- **Classification:** Legendary
- **Generation:** II
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Gen 3 (event) / HGSS / Crystal** — Navel Rock / Tin Tower static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Gen3 Navel Rock needed MysticTicket (event over)
5. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since May 19 2018; rotates through raids

**Pokémon GO:** Legendary raids (shiny since May 2018); ~1/20; rotates

**Notes:** Ramanas Park (Rainbow Slate, Brilliant Diamond).

### Lugia

- **Classification:** Legendary
- **Generation:** II
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Gen 3 (event) / HGSS / Crystal** — Navel Rock / Whirl Islands static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Gen3 Navel Rock needed MysticTicket (event over)
5. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Mar 16 2018; rotates through raids; FIRST shiny legendary released in GO

**Pokémon GO:** Legendary raids (shiny since Mar 2018 — first shiny legendary in GO); ~1/20

**Notes:** Ramanas Park (Squall Slate, Shining Pearl).

### Raikou

- **Classification:** Legendary
- **Generation:** II
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
5. **Crystal (Virtual Console) / HGSS** — Roaming (DVs/PID lock on first sighting)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical; save before first battle. VC eShop closed Mar 2023
6. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jun 29 2019; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Jun 2019); ~1/20; rotates

**Notes:** Legendary beasts huntable via many modern routes.

### Suicune

- **Classification:** Legendary
- **Generation:** II
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
5. **Crystal (VC)** — Tin Tower static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Static in Crystal; VC discontinued (historical)
6. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Aug 17 2019; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Aug 2019); ~1/20; rotates

**Notes:** Static (soft-resettable) in Crystal, roams in G/S.

### Deoxys

- **Classification:** Mythical
- **Generation:** III
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Normal, Attack, Defense, Speed — all four shiny in GO raids (separate 2020–2022 dates); main-series forme is set by in-game meteorites/version, all huntable

**Hunting / shiny methods:**

1. **FireRed/LeafGreen/Emerald** — Birth Island static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Needed AuroraTicket (event over). Not shiny-locked (Gen3)
2. **Omega Ruby/Alpha Sapphire** — Sky Pillar static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: ORAS Deoxys is shiny-LOCKED
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Aug 7 2020; rotates through raids; All 4 formes shiny (Normal/Attack/Defense/Speed)

**Pokémon GO:** Legendary/mythical raids — all 4 formes shiny (RNG); ~1/20

**Notes:** Officially Mythical but treated as a raid boss in GO. Genuine RNG hunt via GO raids and historically via Birth Island.

### Groudon

- **Classification:** Legendary
- **Generation:** III
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Ruby/Sapphire/Emerald** — Story static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical; ORAS Groudon shiny-LOCKED
5. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jan 15 2019; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Jan 2019); ~1/20; rotates

**Notes:** ORAS encounter shiny-locked; huntable via DA/USUM/BDSP/GO + Gen3 originals.

### Jirachi

- **Classification:** Mythical
- **Generation:** III
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** No (historical only)
- **Bucket:** E (hunt, historical only)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Colosseum Bonus Disc (WISHMKR)** — Distribution encounter (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: US 'WISHMKR' Jirachi is NOT shiny-locked -> genuine soft-reset hunt (historical, disc long discontinued)
2. **Pokémon GO** — Masterwork Research 'Wish Granted' (guaranteed shiny reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 100% (guaranteed)
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: B (guaranteed reward)
    - Note: Shiny since Feb 20 2023; one guaranteed shiny, NOT rollable

**Pokémon GO:** Shiny via 'Wish Granted' Masterwork (guaranteed). Not RNG in GO.

**Notes:** Mythical with a real (historical) RNG hunt via the WISHMKR bonus disc. No longer accessible.

### Kyogre

- **Classification:** Legendary
- **Generation:** III
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Ruby/Sapphire/Emerald** — Story static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical; ORAS Kyogre is shiny-LOCKED
5. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since 2019 (exact date disputed); rotates through raids

**Pokémon GO:** Legendary raids (shiny 2019); ~1/20; rotates

**Notes:** ORAS weather-trio encounter is shiny-locked; Gen3 originals + DA/USUM/BDSP/GO are huntable.

### Latias

- **Classification:** Legendary
- **Generation:** III
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
4. **Legends: Z-A (Mega Dimension DLC, 2026)** — 5-star Hyperspace Distortion (run-back reroll)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/4096 base  |  with Shiny Charm: up to ~1/585
    - Shiny Charm: Yes; stacks with Sparkling Power Lv3 donut (-> ~1/585)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Post Main Mission 12; one of only 5 non-locked legendaries in Z-A
5. **Ruby/Sapphire/Emerald** — Roaming / Southern Island static
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical
6. **Scarlet/Violet (Indigo Disk)** — Static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: SHINY-LOCKED in SV DLC
7. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Feb 22 2019; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Feb 2019); ~1/20; rotates

**Notes:** NEW 2026: shiny-huntable in Legends Z-A Mega Dimension Hyperspace Distortions (first found shiny there).

### Latios

- **Classification:** Legendary
- **Generation:** III
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
4. **Legends: Z-A (Mega Dimension DLC, 2026)** — 5-star Hyperspace Distortion (run-back reroll)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/4096 base  |  with Shiny Charm: up to ~1/585
    - Shiny Charm: Yes; stacks with Sparkling Power Lv3 donut (-> ~1/585)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Post Main Mission 12; one of only 5 non-locked legendaries in Z-A
5. **Ruby/Sapphire/Emerald** — Roaming / Southern Island static
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical
6. **Scarlet/Violet (Indigo Disk)** — Static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: SHINY-LOCKED in SV DLC
7. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Apr 15 2019; rotates through raids; Shadow Latios shiny in 2026 Shadow Raids

**Pokémon GO:** Legendary raids (shiny since Apr 2019); ~1/20; rotates

**Notes:** NEW 2026: shiny-huntable in Legends Z-A Mega Dimension Hyperspace Distortions.

### Rayquaza

- **Classification:** Legendary
- **Generation:** III
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Ruby/Sapphire/Emerald** — Sky Pillar static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical; ORAS Rayquaza shiny-LOCKED (Delta Episode)
4. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since 2019; rotates through raids; Mega Rayquaza shiny available

**Pokémon GO:** Legendary raids (shiny 2019); Mega Rayquaza shiny; ~1/20

**Notes:** Not in BDSP. ORAS story encounter shiny-locked. Huntable via DA, USUM, GO, Gen3.

### Regice

- **Classification:** Legendary
- **Generation:** III
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
5. **Sword/Shield (Crown Tundra)** — Regi puzzle static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Crown Tundra ruins; not shiny-locked
6. **Ruby/Sapphire/Emerald** — Sealed chamber static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical cartridge
7. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Nov 2019; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Nov 2019); ~1/20; rotates

**Notes:** One of the most route-rich hunts (DA, USUM, BDSP, ORAS, SwSh static, GO).

### Regirock

- **Classification:** Legendary
- **Generation:** III
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
5. **Sword/Shield (Crown Tundra)** — Regi puzzle static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Crown Tundra ruins; not shiny-locked
6. **Ruby/Sapphire/Emerald** — Sealed chamber static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical cartridge
7. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Nov 2019; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Nov 2019); ~1/20; rotates

**Notes:** One of the most route-rich hunts (DA, USUM, BDSP, ORAS, SwSh static, GO).

### Registeel

- **Classification:** Legendary
- **Generation:** III
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
5. **Sword/Shield (Crown Tundra)** — Regi puzzle static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Crown Tundra ruins; not shiny-locked
6. **Ruby/Sapphire/Emerald** — Sealed chamber static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical cartridge
7. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Nov 2019; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Nov 2019); ~1/20; rotates

**Notes:** One of the most route-rich hunts (DA, USUM, BDSP, ORAS, SwSh static, GO).

### Arceus

- **Classification:** Mythical
- **Generation:** IV
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Legends: Arceus / events** — Story static / distribution
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Shiny-locked in PLA and all distributions; not in GO. (One BDSP Azure-Flute claim exists but is disputed/unreliable)

**Pokémon GO:** Not in Pokémon GO.

**Notes:** No legitimate shiny Arceus as of Aug 2026 (a disputed BDSP claim aside). Classified SHINY UNAVAILABLE.

### Azelf

- **Classification:** Legendary
- **Generation:** IV
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
5. **Diamond/Pearl/Platinum** — Static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical cartridge
6. **Brilliant Diamond/Shining Pearl** — Post-game lake static
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: In-wild BDSP encounter (separate from Ramanas)
7. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Sep 14 2021; rotates through raids; regional raid boss

**Pokémon GO:** Legendary raids (regional; shiny since Sep 14 2021); ~1/20

**Notes:** Lake trio. Mesprit roams (harder). Regional GO raid availability.

### Cresselia

- **Classification:** Legendary
- **Generation:** IV
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
5. **Diamond/Pearl/Platinum** — Roaming
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical
6. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since May 27 2019; rotates through raids; Shadow Cresselia shiny in 2025-26 Shadow Raids

**Pokémon GO:** Legendary raids (shiny since May 2019); ~1/20; rotates

**Notes:** 

### Darkrai

- **Classification:** Mythical
- **Generation:** IV
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Diamond/Pearl/Platinum** — Newmoon Island static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Needed Member Card event (over). Not shiny-locked (Gen4) -> historical hunt
2. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Mar 6 2020; rotates through raids; Mythical but RNG-huntable in 5-star raids (Halloween)

**Pokémon GO:** 5-star raids (shiny since Mar 2020) — RNG; ~1/20

**Notes:** Mythical that IS a true RNG hunt (GO raids now; Gen4 Newmoon Island historically).

### Dialga

- **Classification:** Legendary
- **Generation:** IV
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Origin Forme — shiny available (GO; main-series via Adamant Crystal in PLA, shiny-locked there)

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Diamond/Pearl/Platinum** — Spear Pillar static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical
5. **Brilliant Diamond** — Story static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: BDSP story Dialga shiny-LOCKED (use Ramanas Park route instead)
6. **Legends: Arceus** — Origin Forme story static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: PLA shiny-locked
7. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since ~2021; rotates through raids; Origin Forme shiny also available

**Pokémon GO:** Legendary raids (Altered + Origin shiny); ~1/20; rotates

**Notes:** Story catches locked (BDSP/PLA); huntable via Ramanas Park, DA, USUM, GO.

### Giratina

- **Classification:** Legendary
- **Generation:** IV
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Altered Forme & Origin Forme — both shiny in GO

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Platinum/HGSS** — Turnback Cave static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical
5. **Legends: Arceus** — Origin Forme story static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: PLA shiny-locked
6. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since ~2019; rotates through raids; Altered + Origin Forme shiny

**Pokémon GO:** Legendary raids (Altered + Origin shiny); ~1/20; rotates

**Notes:** Ramanas Park (Distortion Slate) is huntable. PLA Origin locked.

### Heatran

- **Classification:** Legendary
- **Generation:** IV
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
5. **Platinum/HGSS** — Stark Mountain static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical
6. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jan 7 2020; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Jan 2020); ~1/20; rotates

**Notes:** 

### Manaphy

- **Classification:** Mythical
- **Generation:** IV
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** No (historical only)
- **Bucket:** E (hunt, historical only)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Pokémon Ranger -> Gen 4** — Egg hatch after trade (PID vs TSV RNG)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Ranger egg is shiny-locked until TRADED to another Gen4 game, then rolls on hatch. Ranger/distribution discontinued (historical)

**Pokémon GO:** Base Manaphy via research; shiny NOT released in GO.

**Notes:** The classic 'Manaphy egg' hunt. No current access (Pokémon Ranger connectivity discontinued). Manaphy itself cannot be bred (produces Phione).

### Mesprit

- **Classification:** Legendary
- **Generation:** IV
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
5. **Diamond/Pearl/Platinum** — Roaming
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical cartridge
6. **Brilliant Diamond/Shining Pearl** — Post-game lake roamer
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: In-wild BDSP encounter (separate from Ramanas)
7. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Sep 14 2021; rotates through raids; regional raid boss

**Pokémon GO:** Legendary raids (regional; shiny since Sep 14 2021); ~1/20

**Notes:** Lake trio. Mesprit roams (harder). Regional GO raid availability.

### Palkia

- **Classification:** Legendary
- **Generation:** IV
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Origin Forme — shiny available in GO (Lustrous Globe in PLA is shiny-locked)

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Diamond/Pearl/Platinum** — Spear Pillar static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical
5. **Shining Pearl** — Story static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: BDSP story Palkia shiny-LOCKED
6. **Legends: Arceus** — Origin Forme story static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: PLA shiny-locked
7. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since ~2021; rotates through raids; Origin Forme shiny also available; Shadow Palkia 2026

**Pokémon GO:** Legendary raids (Altered + Origin shiny); ~1/20; rotates

**Notes:** Story catches locked; huntable via Ramanas Park, DA, USUM, GO.

### Phione

- **Classification:** Mythical
- **Generation:** IV
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **BDSP / any breeding game** — Breeding (Manaphy/Phione x Ditto), Masuda method
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (BDSP: Masuda + Charm applies to eggs)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: The ONLY Mythical with normal breeding shiny odds; Masuda-eligible. Requires a Manaphy/Phione parent first

**Pokémon GO:** Not in Pokémon GO.

**Notes:** Uniquely, Phione is bred (not caught) and follows ordinary shiny/Masuda odds — a genuine, repeatable RNG hunt.

### Regigigas

- **Classification:** Legendary
- **Generation:** IV
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
2. **Brilliant Diamond/Shining Pearl** — Ramanas/Snowpoint static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Not shiny-locked in BDSP
3. **Platinum/HGSS** — Snowpoint Temple static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical
4. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jun 17 2021; rotates through raids; raids / Elite Raids

**Pokémon GO:** Legendary/Elite raids (shiny since Jun 2021); ~1/20

**Notes:** Not in Dynamax Adventures or USUM wormholes. Huntable via BDSP soft-reset and GO.

### Shaymin

- **Classification:** Mythical
- **Generation:** IV
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** No (historical only)
- **Bucket:** E (hunt, historical only)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Land Forme — shiny (GO Masterwork, guaranteed). Sky Forme — shiny status unconfirmed

**Hunting / shiny methods:**

1. **Diamond/Pearl/Platinum** — Flower Paradise static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Needed Oak's Letter event (over). Not shiny-locked (Gen4) -> historical hunt
2. **Pokémon GO** — Masterwork Research 'Glimmers of Gratitude' (Land Forme) (guaranteed shiny reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 100% (guaranteed)
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: B (guaranteed reward)
    - Note: Shiny since Feb 16 2024; one guaranteed shiny, NOT rollable

**Pokémon GO:** Shiny (Land) via Masterwork (guaranteed). Not RNG in GO.

**Notes:** Historical Gen4 RNG hunt (Flower Paradise) no longer accessible; GO shiny is guaranteed-only.

### Uxie

- **Classification:** Legendary
- **Generation:** IV
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Brilliant Diamond/Shining Pearl** — Ramanas Park slate static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP Charm boosts Masuda eggs only)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Flat 1/4096 regardless of Charm
4. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
5. **Diamond/Pearl/Platinum** — Static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192
    - Shiny Charm: No charm pre-Gen6
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical cartridge
6. **Brilliant Diamond/Shining Pearl** — Post-game lake static
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/4096
    - Shiny Charm: No effect (BDSP)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: In-wild BDSP encounter (separate from Ramanas)
7. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Sep 14 2021; rotates through raids; regional raid boss

**Pokémon GO:** Legendary raids (regional; shiny since Sep 14 2021); ~1/20

**Notes:** Lake trio. Mesprit roams (harder). Regional GO raid availability.

### Cobalion

- **Classification:** Legendary
- **Generation:** V
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
4. **Legends: Z-A (Mega Dimension DLC, 2026)** — 5-star Hyperspace Distortion (run-back reroll)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/4096 base  |  with Shiny Charm: up to ~1/585
    - Shiny Charm: Yes; stacks with Sparkling Power Lv3 donut (-> ~1/585)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Post Main Mission 12; one of only 5 non-locked legendaries in Z-A
5. **Black/White/B2W2** — Static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192  |  with Shiny Charm: ~1/2731
    - Shiny Charm: Yes (Gen5 charm)
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical cartridge; Swords of Justice not shiny-locked
6. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Mar 17 2020; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Mar 17 2020); ~1/20; rotates

**Notes:** Swords of Justice. NEW 2026: shiny-huntable in Legends Z-A Mega Dimension Hyperspace Distortions.

### Genesect

- **Classification:** Mythical
- **Generation:** V
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Normal/Shock/Burn/Chill/Douse Drives — shiny in GO raids; Drives are held-item variants (separate raid dates)

**Hunting / shiny methods:**

1. **Main series** — Distribution
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: C (event distribution)
    - Note: All distributions shiny-locked
2. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since May 2 2023; rotates through raids; Mythical but RNG in 5-star raids; rotates by Drive

**Pokémon GO:** 5-star raids (shiny since May 2023) — RNG; ~1/20

**Notes:** Mythical that IS a true RNG hunt (GO raids). Different Drives rotate.

### Keldeo

- **Classification:** Mythical
- **Generation:** V
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** No
- **Bucket:** B (guaranteed reward)
- **HOME guaranteed-shiny reward:** Yes  |  **Event-only shiny:** Yes
- **Alternate forms:** Ordinary & Resolute — shiny is guaranteed (HOME/GO Masterwork), applies to both

**Hunting / shiny methods:**

1. **Pokémon HOME** — Shiny Keldeo dex-completion Mystery Gift (guaranteed shiny)
    - Shiny locked: Not shiny-locked
    - Odds (base): 100% (guaranteed)
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: B (guaranteed reward)
    - Note: Since Feb 12 2025; requires complete Galar + IoA + Crown Tundra dexes (SwSh)
2. **Pokémon GO** — Masterwork Research 'Pony Tales' (Final Justice) (guaranteed shiny reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 100% (guaranteed)
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: B (guaranteed reward)
    - Note: Shiny since Nov 25 2025; one guaranteed shiny, NOT rollable
3. **Main series** — Distribution
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: C (event distribution)
    - Note: All distributions shiny-locked

**Pokémon GO:** Shiny via 'Pony Tales' Masterwork (guaranteed). Not RNG.

**Notes:** First legit shiny Keldeo was the HOME dex reward (Feb 2025). Guaranteed only — never RNG-huntable.

### Kyurem

- **Classification:** Legendary
- **Generation:** V
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Black Kyurem & White Kyurem — fusion formes (with Zekrom/Reshiram); shiny via the base Kyurem

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Black/White/B2W2** — Giant Chasm static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192  |  with Shiny Charm: ~1/2731
    - Shiny Charm: Yes
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical
4. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since ~2021; rotates through raids; Black/White Kyurem via fusion (Fusion Raid Day Jan 10 2026)

**Pokémon GO:** Legendary raids; ~1/20; rotates

**Notes:** Tao trio. Fused formes via GO fusion events.

### Landorus

- **Classification:** Legendary
- **Generation:** V
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Incarnate & Therian — both shiny in GO (Therian released 2022)

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Sword/Shield (Crown Tundra)** — Roaming (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Not shiny-locked
4. **Black2/White2** — Static
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192  |  with Shiny Charm: ~1/2731
    - Shiny Charm: Yes
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical
5. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Incarnate 2021 / Therian Apr 26 2022; rotates through raids

**Pokémon GO:** Legendary raids (Incarnate + Therian shiny); ~1/20

**Notes:** Forces of Nature.

### Meloetta

- **Classification:** Mythical
- **Generation:** V
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** No
- **Bucket:** B (guaranteed reward)
- **HOME guaranteed-shiny reward:** Yes  |  **Event-only shiny:** Yes
- **Alternate forms:** Aria & Pirouette — shiny is guaranteed (HOME/GO), applies to both

**Hunting / shiny methods:**

1. **Pokémon HOME** — Shiny Meloetta dex-completion Mystery Gift (guaranteed shiny)
    - Shiny locked: Not shiny-locked
    - Odds (base): 100% (guaranteed)
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: B (guaranteed reward)
    - Note: Since Oct 2024; requires complete Paldea + Kitakami + Blueberry dexes (SV)
2. **Pokémon GO** — Masterwork Research 'A Dazzling Aria' (GO Tour Unova) (guaranteed shiny reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 100% (guaranteed)
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: B (guaranteed reward)
    - Note: Shiny since Feb 21 2025; one guaranteed shiny, NOT rollable
3. **Main series** — Distribution
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: C (event distribution)
    - Note: All distributions shiny-locked

**Pokémon GO:** Shiny (Aria) via Masterwork (guaranteed). Not RNG.

**Notes:** Guaranteed only (HOME reward + GO Masterwork). Never RNG-huntable.

### Reshiram

- **Classification:** Legendary
- **Generation:** V
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Black/White/B2W2** — Story static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192  |  with Shiny Charm: ~1/2731
    - Shiny Charm: Yes (Gen5 charm)
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Gen5 box legend NOT shiny-locked -> historical hunt
4. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since ~2020-21; rotates through raids

**Pokémon GO:** Legendary raids; ~1/20; rotates

**Notes:** Tao trio. Huntable via DA, USUM, GO, and Gen5 originals.

### Terrakion

- **Classification:** Legendary
- **Generation:** V
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
4. **Legends: Z-A (Mega Dimension DLC, 2026)** — 5-star Hyperspace Distortion (run-back reroll)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/4096 base  |  with Shiny Charm: up to ~1/585
    - Shiny Charm: Yes; stacks with Sparkling Power Lv3 donut (-> ~1/585)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Post Main Mission 12; one of only 5 non-locked legendaries in Z-A
5. **Black/White/B2W2** — Static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192  |  with Shiny Charm: ~1/2731
    - Shiny Charm: Yes (Gen5 charm)
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical cartridge; Swords of Justice not shiny-locked
6. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since May 19 2020; rotates through raids

**Pokémon GO:** Legendary raids (shiny since May 19 2020); ~1/20; rotates

**Notes:** Swords of Justice. NEW 2026: shiny-huntable in Legends Z-A Mega Dimension Hyperspace Distortions.

### Thundurus

- **Classification:** Legendary
- **Generation:** V
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Incarnate & Therian — both shiny in GO (Therian released 2022)

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Sword/Shield (Crown Tundra)** — Roaming (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Not shiny-locked
4. **Black2/White2** — Static
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192  |  with Shiny Charm: ~1/2731
    - Shiny Charm: Yes
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical
5. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Incarnate 2021 / Therian Apr 5 2022; rotates through raids

**Pokémon GO:** Legendary raids (Incarnate + Therian shiny); ~1/20

**Notes:** Forces of Nature.

### Tornadus

- **Classification:** Legendary
- **Generation:** V
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Incarnate & Therian — both shiny in GO (Therian released 2022)

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Sword/Shield (Crown Tundra)** — Roaming (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Forces of Nature roam the Crown Tundra; not shiny-locked
4. **Black2/White2** — Static
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192  |  with Shiny Charm: ~1/2731
    - Shiny Charm: Yes
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical
5. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Incarnate 2021 / Therian Mar 15 2022; rotates through raids

**Pokémon GO:** Legendary raids (Incarnate + Therian shiny); ~1/20

**Notes:** Forces of Nature. Huntable via SwSh roamer, DA, USUM, GO.

### Victini

- **Classification:** Mythical
- **Generation:** V
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Black/White + events** — Liberty Garden static / distribution
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Shiny-locked in every distribution; shiny still NOT released in GO (confirmed Jul 2026)

**Pokémon GO:** In GO (research), but shiny NOT released.

**Notes:** No legitimate shiny Victini exists anywhere as of Aug 2026. SHINY UNAVAILABLE.

### Virizion

- **Classification:** Legendary
- **Generation:** V
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Omega Ruby/Alpha Sapphire** — Mirage Spot static / Soaring (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
4. **Legends: Z-A (Mega Dimension DLC, 2026)** — 5-star Hyperspace Distortion (run-back reroll)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/4096 base  |  with Shiny Charm: up to ~1/585
    - Shiny Charm: Yes; stacks with Sparkling Power Lv3 donut (-> ~1/585)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Post Main Mission 12; one of only 5 non-locked legendaries in Z-A
5. **Black/White/B2W2** — Static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192  |  with Shiny Charm: ~1/2731
    - Shiny Charm: Yes (Gen5 charm)
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Historical cartridge; Swords of Justice not shiny-locked
6. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since May 12 2020; rotates through raids

**Pokémon GO:** Legendary raids (shiny since May 12 2020); ~1/20; rotates

**Notes:** Swords of Justice. NEW 2026: shiny-huntable in Legends Z-A Mega Dimension Hyperspace Distortions.

### Zekrom

- **Classification:** Legendary
- **Generation:** V
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **Black/White/B2W2** — Story static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/8192  |  with Shiny Charm: ~1/2731
    - Shiny Charm: Yes
    - Currently accessible: No (historical / discontinued)
    - Type: A (true RNG hunt)
    - Note: Gen5 box legend NOT shiny-locked -> historical hunt
4. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since ~2020-21; rotates through raids

**Pokémon GO:** Legendary raids; ~1/20; rotates

**Notes:** Tao trio.

### Diancie

- **Classification:** Mythical
- **Generation:** VI
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** No
- **Bucket:** B (guaranteed reward)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** Yes

**Hunting / shiny methods:**

1. **XY/ORAS** — Event distribution (guaranteed shiny)
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: C (event distribution)
    - Note: Guaranteed shiny Diancie distributed 2016 (e.g. Korea/Pokémon Center)
2. **Pokémon GO** — Masterwork 'Sparkle and Shine' (GO Tour Kalos) (guaranteed shiny reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 100% (guaranteed)
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: B (guaranteed reward)
    - Note: Shiny since Feb 2026; one guaranteed shiny, NOT rollable

**Pokémon GO:** Shiny via 'Sparkle and Shine' Masterwork (guaranteed, Feb 2026). Not RNG.

**Notes:** Guaranteed/event only. GO shiny debuted Feb 2026 (newest guaranteed Mythical shiny).

### Hoopa

- **Classification:** Mythical
- **Generation:** VI
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Confined & Unbound — both shiny-unavailable

**Hunting / shiny methods:**

1. **Main series / GO** — Distribution / research
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Shiny-locked everywhere; shiny not released in GO (confirmed Jul 2026)

**Pokémon GO:** In GO (research); shiny NOT released.

**Notes:** No legitimate shiny Hoopa as of Aug 2026. SHINY UNAVAILABLE.

### Volcanion

- **Classification:** Mythical
- **Generation:** VI
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** No
- **Bucket:** B (guaranteed reward)
- **HOME guaranteed-shiny reward:** Yes  |  **Event-only shiny:** Yes

**Hunting / shiny methods:**

1. **Pokémon HOME** — Shiny Volcanion dex-completion Mystery Gift (guaranteed shiny)
    - Shiny locked: Not shiny-locked
    - Odds (base): 100% (guaranteed)
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: B (guaranteed reward)
    - Note: Since Apr 2026; requires complete Lumiose + Hyperspace Lumiose + Mega dexes (Legends Z-A)
2. **Main series** — Distribution
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: C (event distribution)
    - Note: Prior distributions shiny-locked

**Pokémon GO:** In GO (GO Fest research); shiny NOT released in GO.

**Notes:** First-ever legit shiny Volcanion is the HOME dex reward (Apr 2026). Guaranteed only.

### Xerneas

- **Classification:** Legendary
- **Generation:** VI
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **X/Y** — Story static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: C (event distribution)
    - Note: XY box legend shiny-LOCKED
4. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Oct 8 2022; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Oct 2022); ~1/20; rotates

**Notes:** Story catch locked; huntable via DA, USUM, GO.

### Yveltal

- **Classification:** Legendary
- **Generation:** VI
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
3. **X/Y** — Story static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: No (historical / discontinued)
    - Type: C (event distribution)
    - Note: XY box legend shiny-LOCKED
4. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Sep 27 2022; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Sep 2022); ~1/20; rotates

**Notes:** Story catch locked; huntable via DA, USUM, GO.

### Zygarde

- **Classification:** Legendary
- **Generation:** VI
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** 10% / 50% / Complete Forme — all shiny-unavailable

**Hunting / shiny methods:**

1. **X/Y, USUM, SV, Legends Z-A** — Static / cell assembly
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Shiny-locked in every game (incl. Z-A main story); no distribution; not shiny in GO

**Pokémon GO:** In GO (Routes/cells); shiny NOT released.

**Notes:** No legitimate shiny Zygarde exists anywhere as of Aug 2026. SHINY UNAVAILABLE.

### Cosmoem

- **Classification:** Legendary
- **Generation:** VII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sun/Moon/USUM/GO** — Evolves from Cosmog
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Only from shiny-locked Cosmog line

**Pokémon GO:** In GO (evolution stage); shiny not released.

**Notes:** Shiny UNAVAILABLE for the same reason as Cosmog.

### Cosmog

- **Classification:** Legendary
- **Generation:** VII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sun/Moon/USUM/GO** — Gift / research
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Gift shiny-locked; shiny Cosmog not obtainable (final forms Solgaleo/Lunala are shiny separately)

**Pokémon GO:** In GO (Special Research, evolves to Solgaleo/Lunala); shiny Cosmog not released.

**Notes:** Shiny Cosmog/Cosmoem UNAVAILABLE (cannot evolve a shiny backward from Solgaleo/Lunala). Verify if GO ever releases shiny Cosmog.

### Lunala

- **Classification:** Legendary
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Moon/USUM** — From Cosmog / Necrozma fusion
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: Main-series Lunala (via locked Cosmog) effectively locked
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since ~Jul 2026 (GO Fest); rotates through raids; NEW in 2026

**Pokémon GO:** 5-star raids — shiny NEW ~Jul 2026 (RNG); ~1/20

**Notes:** Shiny huntable via Dynamax Adventures and (new 2026) GO raids.

### Magearna

- **Classification:** Mythical
- **Generation:** VII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **QR distribution / HOME** — Serial / dex reward
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Both regular and 'Original Color' forms are shiny-locked; Original Color is a FORM, not a shiny; not in GO

**Pokémon GO:** Not in Pokémon GO.

**Notes:** No legitimate shiny Magearna. The HOME National-Dex reward is Original-Color Magearna (a form), NOT a shiny. SHINY UNAVAILABLE.

### Marshadow

- **Classification:** Mythical
- **Generation:** VII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Distribution / GO** — Serial / research
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Shiny-locked; shiny not released in GO (base Marshadow in GO May 2024)

**Pokémon GO:** In GO (research); shiny NOT released.

**Notes:** No legitimate shiny Marshadow as of Aug 2026. SHINY UNAVAILABLE.

### Melmetal

- **Classification:** Mythical
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Pokémon GO** — Evolve a shiny Meltan (400 candy)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/125
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny Melmetal obtained by evolving a hunted shiny Meltan; Gigantamax shiny via GO->HOME->SwSh

**Pokémon GO:** Evolve shiny Meltan (RNG via Mystery Box). ~1/125 at the Meltan step.

**Notes:** Evolution case: not encountered directly — hunt shiny Meltan, then evolve.

### Meltan

- **Classification:** Mythical
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** Yes  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Pokémon GO** — Mystery Box (RNG, timed windows)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/125
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny Meltan RNG-rollable during announced Shiny Meltan windows (~1/125)
2. **Pokémon HOME** — Shiny Meltan dex-completion Mystery Gift (guaranteed shiny)
    - Shiny locked: Not shiny-locked
    - Odds (base): 100% (guaranteed)
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: B (guaranteed reward)
    - Note: Since Feb 12 2025; requires complete Kanto dex (Let's Go P/E)

**Pokémon GO:** Mystery Box (shiny since Feb 5 2019) — RNG during shiny windows; ~1/125

**Notes:** Mythical with a real RNG hunt (Mystery Box). Also a guaranteed HOME dex reward since Feb 2025.

### Necrozma

- **Classification:** Legendary
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Dusk Mane / Dawn Wings (fusions with Solgaleo/Lunala) & Ultra Necrozma — shiny via base Necrozma

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Sun/Moon/USUM** — Story static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: Main-series Necrozma shiny-locked
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Aug 25 2025; rotates through raids; GO Fest 2024 ticket -> 5-star raids Aug 2025; Dusk Mane/Dawn Wings via fusion

**Pokémon GO:** 5-star raids (shiny since Aug 2025) — RNG; ~1/20

**Notes:** Main-series locked; huntable via Dynamax Adventures and GO raids.

### Silvally

- **Classification:** Legendary
- **Generation:** VII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sun/Moon/USUM** — Evolves from Type: Null
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Only from the shiny-locked Type: Null gift; not in GO

**Pokémon GO:** Not in Pokémon GO.

**Notes:** Gained Legendary status Oct 2017. Shiny UNAVAILABLE (only from shiny-locked Type: Null).

### Solgaleo

- **Classification:** Legendary
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Sun/USUM** — From Cosmog / Necrozma fusion
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: Main-series Solgaleo (via locked Cosmog) is effectively locked
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jul 22 2026; rotates through raids; NEW in 2026

**Pokémon GO:** 5-star raids — shiny NEW Jul 22 2026 (RNG); ~1/20

**Notes:** Shiny huntable via Dynamax Adventures and (new 2026) GO raids.

### Tapu Bulu

- **Classification:** Legendary
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Sun/Moon/USUM** — Ruins guardian static — respawn (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (first story encounter is locked; the RESPAWN is huntable)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Apr 17 2023; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Apr 17 2023); ~1/20; rotates

**Notes:** Guardian deities. First story encounter shiny-locked; defeat it and the respawn is huntable.

### Tapu Fini

- **Classification:** Legendary
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Sun/Moon/USUM** — Ruins guardian static — respawn (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (first story encounter is locked; the RESPAWN is huntable)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since May 9 2023; rotates through raids

**Pokémon GO:** Legendary raids (shiny since May 9 2023); ~1/20; rotates

**Notes:** Guardian deities. First story encounter shiny-locked; defeat it and the respawn is huntable.

### Tapu Koko

- **Classification:** Legendary
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Sun/Moon/USUM** — Ruins guardian static — respawn (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (first story encounter is locked; the RESPAWN is huntable)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jan 25 2023; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Jan 25 2023); ~1/20; rotates

**Notes:** Guardian deities. First story encounter shiny-locked; defeat it and the respawn is huntable.

### Tapu Lele

- **Classification:** Legendary
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable reward)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100; applies to boss)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires Crown Tundra DLC; best modern odds
2. **Sun/Moon/USUM** — Ruins guardian static — respawn (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (first story encounter is locked; the RESPAWN is huntable)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Feb 8 2023; rotates through raids

**Pokémon GO:** Legendary raids (shiny since Feb 8 2023); ~1/20; rotates

**Notes:** Guardian deities. First story encounter shiny-locked; defeat it and the respawn is huntable.

### Type: Null

- **Classification:** Legendary
- **Generation:** VII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sun/Moon/USUM** — Gift (Aether)
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Gift is shiny-locked; only source; not in GO

**Pokémon GO:** Not in Pokémon GO.

**Notes:** Officially 'Synthetic Pokémon'; Bulbapedia counts it as Legendary. Shiny UNAVAILABLE (gift is the only source and is locked).

### Zeraora

- **Classification:** Mythical
- **Generation:** VII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Distribution / GO** — Serial / raids
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Shiny-locked; shiny not released in GO (base in game GO Fest 2026); future paid Masterwork reportedly planned

**Pokémon GO:** In GO (GO Fest 2026); shiny NOT released.

**Notes:** No legitimate shiny Zeraora as of Aug 2026 (future GO release rumored). SHINY UNAVAILABLE currently.

### Calyrex

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Ice Rider / Shadow Rider (fusions with Glastrier/Spectrier) — all shiny-unavailable

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra) / GO** — Gift / raids
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Crown Tundra gift shiny-locked; shiny not released in GO

**Pokémon GO:** In GO; shiny NOT released.

**Notes:** No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.

### Enamorus

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Incarnate & Therian — both shiny-unavailable as of Aug 2026 (GO shiny not released)

**Hunting / shiny methods:**

1. **Legends: Arceus / GO** — Story static / Elite Raids
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: PLA story catch shiny-locked; shiny not released in GO (Incarnate or Therian)

**Pokémon GO:** In GO (Elite Raids); shiny NOT released.

**Notes:** Fourth Force of Nature. No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.

### Eternatus

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield / GO** — Story static / raids
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: SwSh shiny-locked; shiny not released in GO (debuted Aug 2025)

**Pokémon GO:** In GO (raids since Aug 2025); shiny NOT released.

**Notes:** No legitimate shiny Eternatus as of Aug 2026. SHINY UNAVAILABLE.

### Glastrier

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra) / GO** — Story static / raids
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Crown Tundra encounter shiny-locked; shiny not released in GO

**Pokémon GO:** In GO; shiny NOT released.

**Notes:** No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.

### Kubfu

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Isle of Armor) / GO** — Gift / research
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: IoA gift shiny-locked; shiny not available in GO

**Pokémon GO:** In GO; shiny NOT available.

**Notes:** Classification debated (some group with Legendaries). Shiny UNAVAILABLE.

### Regidrago

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Split-Decision Ruins static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Choose Regieleki OR Regidrago per save; NOT shiny-locked

**Pokémon GO:** In GO; shiny not confirmed released (as of Aug 2026).

**Notes:** Shiny huntable via SwSh Split-Decision Ruins soft-reset. GO shiny status uncertain/unreleased.

### Regieleki

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Split-Decision Ruins static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Choose Regieleki OR Regidrago per save; NOT shiny-locked
2. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Nov 27 2024; rotates through raids

**Pokémon GO:** 5-star raids (shiny since Nov 2024) — RNG; ~1/20

**Notes:** One of only two SwSh-introduced legendaries that can be shiny (with Regidrago). Static soft-reset.

### Spectrier

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra) / GO** — Story static / raids
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Crown Tundra encounter shiny-locked; shiny not released in GO

**Pokémon GO:** In GO; shiny NOT released.

**Notes:** No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.

### Urshifu

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Single Strike & Rapid Strike Style — both shiny-locked (from the locked Kubfu)

**Hunting / shiny methods:**

1. **Sword/Shield (Isle of Armor) / GO** — Evolves from Kubfu
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Only from shiny-locked Kubfu; shiny not available in GO

**Pokémon GO:** In GO; shiny NOT available.

**Notes:** Shiny UNAVAILABLE (only from shiny-locked Kubfu).

### Zacian

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Hero of Many Battles & Crowned Sword — shiny carries across the form change

**Hunting / shiny methods:**

1. **Sword/Shield** — Story static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: SwSh box legend shiny-LOCKED
2. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Sep 26 2024; rotates through raids

**Pokémon GO:** 5-star raids (shiny since Sep 2024) — RNG; ~1/20

**Notes:** Main-series locked; the RNG hunt is GO raids.

### Zamazenta

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Hero of Many Battles & Crowned Shield — shiny carries across the form change

**Hunting / shiny methods:**

1. **Sword/Shield** — Story static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: SwSh box legend shiny-LOCKED
2. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Oct 4 2024; rotates through raids

**Pokémon GO:** 5-star raids (shiny since Oct 2024) — RNG; ~1/20

**Notes:** Main-series locked; RNG hunt is GO raids.

### Zarude

- **Classification:** Mythical
- **Generation:** VIII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Distribution / GO** — Serial / event
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: All distributions shiny-locked; shiny not released in GO (both GO appearances non-shiny)

**Pokémon GO:** In GO (non-shiny); shiny NOT released.

**Notes:** No legitimate shiny Zarude anywhere as of Aug 2026. SHINY UNAVAILABLE.

### Chi-Yu

- **Classification:** Legendary
- **Generation:** IX
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Scarlet/Violet** — Unbound-stakes static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: SV encounter shiny-locked; no distribution; not in GO

**Pokémon GO:** Not in Pokémon GO.

**Notes:** Treasures of Ruin. No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.

### Chien-Pao

- **Classification:** Legendary
- **Generation:** IX
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Scarlet/Violet** — Unbound-stakes static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: SV encounter shiny-locked; no distribution; not in GO

**Pokémon GO:** Not in Pokémon GO.

**Notes:** Treasures of Ruin. No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.

### Fezandipiti

- **Classification:** Legendary
- **Generation:** IX
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Scarlet/Violet (Teal Mask)** — Static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Teal Mask encounter shiny-locked; not in GO

**Pokémon GO:** Not in Pokémon GO.

**Notes:** Loyal Three. No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.

### Koraidon

- **Classification:** Legendary
- **Generation:** IX
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** No
- **Bucket:** C (event distribution only)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** Yes

**Hunting / shiny methods:**

1. **Scarlet/Violet** — Story ride legendary
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: SV story Koraidon shiny-LOCKED
2. **Distribution (GameStop/EB code)** — Serial-code gift (guaranteed shiny)
    - Shiny locked: Not shiny-locked
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: Shiny Koraidon distributed Sep-Oct 2026 via retail codes (guaranteed, not a roll)

**Pokémon GO:** Not in Pokémon GO.

**Notes:** Shiny exists ONLY via the 2026 guaranteed retail-code distribution. Never RNG-huntable.

### Miraidon

- **Classification:** Legendary
- **Generation:** IX
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** No
- **Bucket:** C (event distribution only)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** Yes

**Hunting / shiny methods:**

1. **Scarlet/Violet** — Story ride legendary
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: SV story Miraidon shiny-LOCKED
2. **Distribution (GameStop/EB code)** — Serial-code gift (guaranteed shiny)
    - Shiny locked: Not shiny-locked
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: Shiny Miraidon distributed Sep-Oct 2026 via retail codes (guaranteed, not a roll)

**Pokémon GO:** Not in Pokémon GO.

**Notes:** Shiny exists ONLY via the 2026 guaranteed retail-code distribution. Never RNG-huntable.

### Munkidori

- **Classification:** Legendary
- **Generation:** IX
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Scarlet/Violet (Teal Mask)** — Static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Teal Mask encounter shiny-locked; not in GO

**Pokémon GO:** Not in Pokémon GO.

**Notes:** Loyal Three. No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.

### Ogerpon

- **Classification:** Legendary
- **Generation:** IX
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Teal / Wellspring / Hearthflame / Cornerstone Mask — all shiny-locked

**Hunting / shiny methods:**

1. **Scarlet/Violet (Teal Mask)** — Gift
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Teal Mask gift shiny-locked; not in GO

**Pokémon GO:** Not in Pokémon GO.

**Notes:** No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.

### Okidogi

- **Classification:** Legendary
- **Generation:** IX
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Scarlet/Violet (Teal Mask)** — Static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Teal Mask encounter shiny-locked; not in GO

**Pokémon GO:** Not in Pokémon GO.

**Notes:** Loyal Three. No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.

### Pecharunt

- **Classification:** Mythical
- **Generation:** IX
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Scarlet/Violet (Mochi Mayhem)** — Epilogue static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: SV epilogue shiny-locked; not in GO

**Pokémon GO:** Not in Pokémon GO.

**Notes:** No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.

### Terapagos

- **Classification:** Legendary
- **Generation:** IX
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Alternate forms:** Normal / Terastal / Stellar Forme — shiny-locked

**Hunting / shiny methods:**

1. **Scarlet/Violet (Indigo Disk)** — Story gift
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Indigo Disk story gift shiny-locked; not in GO

**Pokémon GO:** Not in Pokémon GO.

**Notes:** No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.

### Ting-Lu

- **Classification:** Legendary
- **Generation:** IX
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Scarlet/Violet** — Unbound-stakes static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: SV encounter shiny-locked; no distribution; not in GO

**Pokémon GO:** Not in Pokémon GO.

**Notes:** Treasures of Ruin. No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.

### Wo-Chien

- **Classification:** Legendary
- **Generation:** IX
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Scarlet/Violet** — Unbound-stakes static
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: SV encounter shiny-locked; no distribution; not in GO

**Pokémon GO:** Not in Pokémon GO.

**Notes:** Treasures of Ruin. No legitimate shiny as of Aug 2026. SHINY UNAVAILABLE.


## Ultra Beasts (appendix — separate class)

### Blacephalon

- **Classification:** Ultra Beast
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
2. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: UB path unlocks after returning legendaries
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Apr 2025; rotates through raids; Ultra Beast raids

**Pokémon GO:** Ultra Beast raids (shiny since Apr 2025); ~1/20

**Notes:** Ultra Beast (own class). Shiny-locked in SM; unlocked in USUM wormholes, Dynamax Adventures, and GO raids.

### Buzzwole

- **Classification:** Ultra Beast
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
2. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: UB path unlocks after returning legendaries
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jul 5 2024; rotates through raids; Ultra Beast raids

**Pokémon GO:** Ultra Beast raids (shiny since Jul 5 2024); ~1/20

**Notes:** Ultra Beast (own class). Shiny-locked in SM; unlocked in USUM wormholes, Dynamax Adventures, and GO raids.

### Celesteela

- **Classification:** Ultra Beast
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
2. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: UB path unlocks after returning legendaries
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jul 2024; rotates through raids; Ultra Beast raids

**Pokémon GO:** Ultra Beast raids (shiny since Jul 2024); ~1/20

**Notes:** Ultra Beast (own class). Shiny-locked in SM; unlocked in USUM wormholes, Dynamax Adventures, and GO raids.

### Guzzlord

- **Classification:** Ultra Beast
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
2. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: UB path unlocks after returning legendaries
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jul 2024; rotates through raids; Ultra Beast raids

**Pokémon GO:** Ultra Beast raids (shiny since Jul 2024); ~1/20

**Notes:** Ultra Beast (own class). Shiny-locked in SM; unlocked in USUM wormholes, Dynamax Adventures, and GO raids.

### Kartana

- **Classification:** Ultra Beast
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
2. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: UB path unlocks after returning legendaries
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jul 2024; rotates through raids; Ultra Beast raids

**Pokémon GO:** Ultra Beast raids (shiny since Jul 2024); ~1/20

**Notes:** Ultra Beast (own class). Shiny-locked in SM; unlocked in USUM wormholes, Dynamax Adventures, and GO raids.

### Naganadel

- **Classification:** Ultra Beast
- **Generation:** VII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **USUM / GO** — Evolves from Poipole
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: Only from shiny-locked Poipole

**Pokémon GO:** In GO; shiny-LOCKED.

**Notes:** Ultra Beast. Shiny UNAVAILABLE (only from shiny-locked Poipole).

### Nihilego

- **Classification:** Ultra Beast
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
2. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: UB path unlocks after returning legendaries
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jul 2024; rotates through raids; Ultra Beast raids

**Pokémon GO:** Ultra Beast raids (shiny since Jul 2024); ~1/20

**Notes:** Ultra Beast (own class). Shiny-locked in SM; unlocked in USUM wormholes, Dynamax Adventures, and GO raids.

### Pheromosa

- **Classification:** Ultra Beast
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
2. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: UB path unlocks after returning legendaries
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Jun 14 2024; rotates through raids; Ultra Beast raids

**Pokémon GO:** Ultra Beast raids (shiny since Jun 14 2024); ~1/20

**Notes:** Ultra Beast (own class). Shiny-locked in SM; unlocked in USUM wormholes, Dynamax Adventures, and GO raids.

### Poipole

- **Classification:** Ultra Beast
- **Generation:** VII
- **Shiny exists:** No
- **Currently shiny-huntable (RNG):** No
- **Bucket:** D (shiny unavailable)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **USUM / GO** — Gift / research
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: D (shiny unavailable)
    - Note: USUM gift shiny-locked; confirmed shiny-locked in GO

**Pokémon GO:** In GO; shiny-LOCKED.

**Notes:** Ultra Beast. Shiny UNAVAILABLE (shiny-locked in both USUM and GO).

### Stakataka

- **Classification:** Ultra Beast
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
2. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: UB path unlocks after returning legendaries
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Apr 2025; rotates through raids; Ultra Beast raids

**Pokémon GO:** Ultra Beast raids (shiny since Apr 2025); ~1/20

**Notes:** Ultra Beast (own class). Shiny-locked in SM; unlocked in USUM wormholes, Dynamax Adventures, and GO raids.

### Xurkitree

- **Classification:** Ultra Beast
- **Generation:** VII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No

**Hunting / shiny methods:**

1. **Ultra Sun/Ultra Moon** — Ultra Space Wilds static (soft-reset)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/4096  |  with Shiny Charm: 1/1365
    - Shiny Charm: Yes (1/4096 -> 1/1365; wormhole DISTANCE does NOT boost legendary odds)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Requires 3DS cartridge (eShop closed Mar 2023)
2. **Sword/Shield (Crown Tundra)** — Dynamax Adventure boss (soft-resettable)
    - Shiny locked: Not shiny-locked
    - Odds (base): 1/300  |  with Shiny Charm: 1/100
    - Shiny Charm: Yes (1/300 -> 1/100)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: UB path unlocks after returning legendaries
3. **Pokémon GO** — Legendary 5-star raid (RNG per raid)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since May 30 2024; rotates through raids; Ultra Beast raids

**Pokémon GO:** Ultra Beast raids (shiny since May 30 2024); ~1/20

**Notes:** Ultra Beast (own class). Shiny-locked in SM; unlocked in USUM wormholes, Dynamax Adventures, and GO raids.


## Alternate forms (appendix — distinct shiny status)

### Galarian Articuno

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Form of:** Articuno (distinct alternate form)

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Roaming static (Legendary Clue 1)
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: Galarian bird roamer is shiny-LOCKED in the main series
2. **Pokémon GO** — Daily Adventure Incense wild spawn (RNG)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20 per encounter
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Oct 4 2024; wild-ONLY via Daily Adventure Incense (never in raids). Boosted ~1/20 shiny rate, but DAI yields only ~1 bird encounter per day, so it is a slow grind

**Pokémon GO:** Daily Adventure Incense wild (shiny since Oct 2024) — RNG, wild-only (not raids)

**Notes:** Galarian form of Articuno (Psychic/Flying) — a distinct Pokémon introduced in Gen VIII, NOT the Kanto bird. Main-series Crown Tundra roamer is shiny-locked; the ONLY shiny route is Pokémon GO Daily Adventure Incense wild spawns.

### Galarian Moltres

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Form of:** Moltres (distinct alternate form)

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Roaming static (Legendary Clue 1)
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: Galarian bird roamer is shiny-LOCKED in the main series
2. **Pokémon GO** — Daily Adventure Incense wild spawn (RNG)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20 per encounter
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Oct 4 2024; wild-ONLY via Daily Adventure Incense (never in raids). Boosted ~1/20 shiny rate, but DAI yields only ~1 bird encounter per day, so it is a slow grind

**Pokémon GO:** Daily Adventure Incense wild (shiny since Oct 2024) — RNG, wild-only (not raids)

**Notes:** Galarian form of Moltres (Dark/Flying) — a distinct Pokémon introduced in Gen VIII, NOT the Kanto bird. Main-series Crown Tundra roamer is shiny-locked; the ONLY shiny route is Pokémon GO Daily Adventure Incense wild spawns.

### Galarian Zapdos

- **Classification:** Legendary
- **Generation:** VIII
- **Shiny exists:** Yes
- **Currently shiny-huntable (RNG):** Yes
- **Bucket:** A (true hunt, current)
- **HOME guaranteed-shiny reward:** No  |  **Event-only shiny:** No
- **Form of:** Zapdos (distinct alternate form)

**Hunting / shiny methods:**

1. **Sword/Shield (Crown Tundra)** — Roaming static (Legendary Clue 1)
    - Shiny locked: **Shiny-LOCKED**
    - Shiny Charm: n/a
    - Currently accessible: Yes
    - Type: C (event distribution)
    - Note: Galarian bird roamer is shiny-LOCKED in the main series
2. **Pokémon GO** — Daily Adventure Incense wild spawn (RNG)
    - Shiny locked: Not shiny-locked
    - Odds (base): ~1/20 per encounter
    - Shiny Charm: n/a (GO has no Shiny Charm)
    - Currently accessible: Yes
    - Type: A (true RNG hunt)
    - Note: Shiny since Oct 4 2024; wild-ONLY via Daily Adventure Incense (never in raids). Boosted ~1/20 shiny rate, but DAI yields only ~1 bird encounter per day, so it is a slow grind

**Pokémon GO:** Daily Adventure Incense wild (shiny since Oct 2024) — RNG, wild-only (not raids)

**Notes:** Galarian form of Zapdos (Fighting/Flying) — a distinct Pokémon introduced in Gen VIII, NOT the Kanto bird. Main-series Crown Tundra roamer is shiny-locked; the ONLY shiny route is Pokémon GO Daily Adventure Incense wild spawns.


---

# FILTERED LISTS

### 1. Huntable through Sword/Shield **Dynamax Adventures**
*(51 species — 1/300 base, 1/100 with Shiny Charm)*  
Articuno, Zapdos, Moltres, Raikou, Entei, Suicune, Lugia, Ho-Oh, Regirock, Regice, Registeel, Latias, Latios, Kyogre, Groudon, Rayquaza, Uxie, Mesprit, Azelf, Dialga, Palkia, Heatran, Giratina, Cresselia, Cobalion, Terrakion, Virizion, Tornadus, Thundurus, Landorus, Reshiram, Zekrom, Kyurem, Xerneas, Yveltal, Tapu Koko, Tapu Lele, Tapu Bulu, Tapu Fini, Solgaleo, Lunala, Necrozma, Nihilego, Buzzwole, Pheromosa, Xurkitree, Celesteela, Kartana, Guzzlord, Stakataka, Blacephalon

### 2. Huntable in **Ultra Sun / Ultra Moon** (Ultra Wormholes)
*(45 species — 1/4096, 1/1365 charm; distance does NOT boost legendary odds)*  
Articuno, Zapdos, Moltres, Mewtwo, Raikou, Entei, Suicune, Lugia, Ho-Oh, Regirock, Regice, Registeel, Latias, Latios, Kyogre, Groudon, Rayquaza, Uxie, Mesprit, Azelf, Dialga, Palkia, Heatran, Giratina, Cresselia, Cobalion, Terrakion, Virizion, Tornadus, Thundurus, Landorus, Reshiram, Zekrom, Kyurem, Xerneas, Yveltal, Nihilego, Buzzwole, Pheromosa, Xurkitree, Celesteela, Kartana, Guzzlord, Stakataka, Blacephalon

### 3. Huntable in **Brilliant Diamond / Shining Pearl** (Ramanas Park & wild statics)
*(23 species — 1/4096 flat; Shiny Charm does NOT help wild/legendary hunts in BDSP)*  
Articuno, Zapdos, Moltres, Mewtwo, Raikou, Entei, Suicune, Lugia, Ho-Oh, Regirock, Regice, Registeel, Kyogre, Groudon, Uxie, Mesprit, Azelf, Dialga, Palkia, Heatran, Regigigas, Giratina, Cresselia

### 4. Huntable through **Sword/Shield static** encounters (non-DA)
*(8 species — Crown Tundra Regis/Regieleki/Regidrago + roaming Forces of Nature; 1/4096, 1/1365 charm)*  
Regirock, Regice, Registeel, Tornadus, Thundurus, Landorus, Regieleki, Regidrago

### 4b. Huntable through **Legends: Z-A Mega Dimension** (Hyperspace Distortions, NEW 2026)
*(5 species — up to ~1/585 with Shiny Charm + Sparkling Power Lv3 donut)*  
Latias, Latios, Cobalion, Terrakion, Virizion

### 5. Ever genuinely **RNG shiny-huntable in Pokémon GO** (raids / Mystery Box / wild)
*(64 species — mostly ~1/20 legendary raids; Meltan/Galarian birds ~1/125)*  
Articuno, Zapdos, Moltres, Mewtwo, Raikou, Entei, Suicune, Lugia, Ho-Oh, Regirock, Regice, Registeel, Latias, Latios, Kyogre, Groudon, Rayquaza, Deoxys, Uxie, Mesprit, Azelf, Dialga, Palkia, Heatran, Regigigas, Giratina, Cresselia, Darkrai, Cobalion, Terrakion, Virizion, Tornadus, Thundurus, Landorus, Reshiram, Zekrom, Kyurem, Genesect, Xerneas, Yveltal, Tapu Koko, Tapu Lele, Tapu Bulu, Tapu Fini, Solgaleo, Lunala, Necrozma, Meltan, Melmetal, Zacian, Zamazenta, Regieleki, Nihilego, Buzzwole, Pheromosa, Xurkitree, Celesteela, Kartana, Guzzlord, Stakataka, Blacephalon, Galarian Articuno, Galarian Zapdos, Galarian Moltres

> Guaranteed-only GO shinies (NOT hunts): Mew, Celebi, Jirachi, Shaymin, Keldeo, Meloetta, Diancie.

### 6. **Mythical** Pokémon that can legitimately be shiny-**hunted** (true RNG, ever)
*(10 of 23 Mythicals)*  
Celebi (historical), Jirachi (historical), Deoxys (current), Phione (current), Manaphy (historical), Darkrai (current), Shaymin (historical), Genesect (current), Meltan (current), Melmetal (current)

### 7. Shiny **still completely unavailable** (no legitimate shiny ever)
*(31 species incl. Ultra Beasts)*  
Arceus, Victini, Zygarde, Hoopa, Type: Null, Silvally, Cosmog, Cosmoem, Magearna, Marshadow, Zeraora, Eternatus, Kubfu, Urshifu, Glastrier, Spectrier, Calyrex, Enamorus, Zarude, Wo-Chien, Chien-Pao, Ting-Lu, Chi-Yu, Okidogi, Munkidori, Fezandipiti, Ogerpon, Terapagos, Pecharunt, Poipole, Naganadel

### 8. Shiny **exists but only via guaranteed / event distribution** (never a hunt)
*(7 species)*  
Mew, Keldeo, Meloetta, Diancie, Volcanion, Koraidon, Miraidon

### 9. **Currently huntable** without needing an expired event (as of Aug 2026)
*(66 species incl. Ultra Beasts; 54 core Legendary/Mythical)*  
Articuno, Zapdos, Moltres, Mewtwo, Raikou, Entei, Suicune, Lugia, Ho-Oh, Regirock, Regice, Registeel, Latias, Latios, Kyogre, Groudon, Rayquaza, Deoxys, Uxie, Mesprit, Azelf, Dialga, Palkia, Heatran, Regigigas, Giratina, Cresselia, Phione, Darkrai, Cobalion, Terrakion, Virizion, Tornadus, Thundurus, Landorus, Reshiram, Zekrom, Kyurem, Genesect, Xerneas, Yveltal, Tapu Koko, Tapu Lele, Tapu Bulu, Tapu Fini, Solgaleo, Lunala, Necrozma, Meltan, Melmetal, Zacian, Zamazenta, Regieleki, Regidrago, Nihilego, Buzzwole, Pheromosa, Xurkitree, Celesteela, Kartana, Guzzlord, Stakataka, Blacephalon, Galarian Articuno, Galarian Zapdos, Galarian Moltres

### 9b. Distinct alternate **forms** with their own shiny status (broken out as separate rows)
*(3 forms)*  
Galarian Articuno (form of Articuno — yes), Galarian Zapdos (form of Zapdos — yes), Galarian Moltres (form of Moltres — yes).  
Other legendaries with alternate formes that share their base species' shiny status (documented in each entry, not split out): Deoxys, Dialga, Palkia, Giratina, Shaymin, Tornadus, Thundurus, Landorus, Kyurem, Zacian, Zamazenta, Necrozma, Calyrex, Urshifu, Zygarde, Hoopa, Meloetta, Genesect, Enamorus, Keldeo, Ogerpon, Terapagos.

### 10. Best games / platforms for hunting the most Legendary/Mythical shinies
| Rank | Platform | # Legendary/Mythical/UB shinies huntable |
|---:|---|---:|
| 1 | Pokémon GO (raids/box, RNG) | 64 |
| 2 | Sword/Shield Dynamax Adventures | 51 |
| 3 | Ultra Sun/Ultra Moon Ultra Wormholes | 45 |
| 4 | Brilliant Diamond/Shining Pearl | 23 |
| 5 | Omega Ruby/Alpha Sapphire (Mirage Spots) | 16 |
| 6 | Sword/Shield static (Crown Tundra) | 8 |
| 7 | Legends Z-A Mega Dimension | 5 |

**Takeaway:** *Pokémon GO* (raids) covers the largest raw number of species, but every GO raid shiny is a ~1/20 roll with no Shiny Charm. *Dynamax Adventures* is the single best **main-series** platform — huge roster at the best odds (1/100 with charm). *Ultra Wormholes* cover the widest Gen 1–6 main-series set (though at 1/1365). For the newest additions, *Legends Z-A Mega Dimension* (2026) is the only place to hunt shiny Lati@s / Swords of Justice in a modern main-series title.


---

# VALIDATION PASS

- **Every species appears exactly once:** PASS (108 rows, 108 unique names).
- **Counts reconcile:** shiny-exists (65) + shiny-never (29) = 94 = total (94) — PASS.
- **Hunt counts reconcile:** current (54) + historical-only (4) = 58 = RNG-hunt-ever (58) — PASS.
- **Guaranteed rewards are never counted as hunts:** HOME dex-reward shinies (Meloetta, Keldeo, Meltan*, Volcanion) and GO Masterwork shinies (Mew, Celebi, Jirachi, Shaymin, Meloetta, Keldeo, Diancie) are recorded as Bucket B, and are excluded from `rng_hunt`. (*Meltan also has a real Mystery Box RNG hunt, so it is Bucket A.)
- **'Currently huntable' claims** are based on Aug-2026 game/service availability: SwSh+DLC, BDSP, USUM/ORAS (3DS cartridge; eShop closed Mar 2023 but carts play), Legends Z-A + Mega Dimension DLC, and GO raid rotations. Discontinued-only routes (Gen 2 VC, Gen 3/4 event-island tickets, Pokémon Ranger egg) are marked historical.
- **Known uncertainties (flagged in notes):** exact GO first-shiny dates for a few long-standing raid legendaries; Regidrago/Cosmog GO shiny status; the disputed BDSP Azure-Flute Arceus claim (treated as no-legit-shiny). Negative 'no shiny' claims for in-GO species can flip at any future event.
