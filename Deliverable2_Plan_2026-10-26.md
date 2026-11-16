# Deliverable 2 — Preliminary LCA Model and Initial Results: work plan

Plan written 26 October 2026. Nothing has been built yet. This plan says what will be built, how, in what order, and what is needed from you first.

---

## 0. The project thesis stays fixed

Deliverable 2 is built directly on the reworked proposal, `Group_Project_Deliverable1_v2_2026-10-12.docx`. These points are carried over unchanged:

| Fixed element | Value carried into D2 |
|---|---|
| Research question (instructor-approved, verbatim) | *For mowing one existing full-size natural-grass football pitch for one maintenance year, how do combustion-powered and battery-electric mowing compare in climate-change and fossil-resource impacts?* |
| Alternatives | A: diesel ride-on rotary mower (Toro Groundsmaster 3200 as technical reference). B: battery-electric equivalent (Groundsmaster e3200). Petrol is a sensitivity inside A (S3), not a third alternative. |
| Functional unit | Mowing one 105 × 68 m pitch (7 140 m²) for one year: 30 cuts at 30–40 mm, 1.52 m rotary deck, clippings returned, temperate Europe |
| Reference flows (preliminary) | A ≈ 63 kg (76 L) diesel per pitch-year; B ≈ 313 kWh at the socket per pitch-year |
| Boundary | Energy carrier from resource to mower. Construction, artificial turf, irrigation, fertilisation, other maintenance, labour, shed and charging point excluded. Capital goods excluded in the baseline (in for both or out for both; S4 only). |
| Database | ELCD 3.2, instructor file `elcd_3_2_greendelta_v2_18_correction_20220908.zolca`, newer 2008–2015 data generation on both sides, EU-27. No secondary database in the baseline. |
| LCIA | CML-IA baseline as bundled: Global warming (GWP100a), kg CO₂-eq; Abiotic depletion (fossil fuels), MJ. No other categories, no normalisation or weighting. |
| Foreground | Four processes per alternative (A1–A4, B1–B4), as in Figure 1 of D1 |
| Committed sensitivities | S1 electricity mix, S2 energy per cut. S3–S5 if time permits. |
| Headline outputs | Break-even grid intensity and break-even charging efficiency |

Anything that would change the question, the categories, the database or the approved exclusions needs instructor approval first. The plan does not touch them.

**Sources reviewed for this plan:** `Downloads\Group_Project_Instructions_and_Milestone_Deliverables.pdf` (§8 items 38–49, §3 evidence hierarchy and naming, §5 placeholders, §6 compatibility, §10 submission rules, §12 quality gate); D1 v2 (full text, tables and Figure 1); `screening_check\` outputs; the Lab 2 model-building scripts.

---

## 1. What D2 must contain, and how each item will be met

| # | Requirement (instructions §8) | What we will deliver |
|---|---|---|
| 38 | Recoverable openLCA model/database file, named with group, project and date | A separate project database exported as `Group_Project_Deliverable2_v1_<date>.zolca`. If the upload limit is too small for ~175 MB, a JSON-LD export of our foreground processes, flows, parameters, product systems and project, which re-imports into ELCD 3.2 (format to be confirmed, see §12). |
| 39 | Model screenshot/export and a readable system diagram | openLCA model-graph captures of both product systems, plus an updated Figure 1 (regenerated from `make_diagram.py`) that names the exact ELCD datasets and shows the background links |
| 40 | Goal/scope update | Final functional unit, recomputed reference flows, boundary, **quantified** cut-offs, allocation and biogenic-carbon rules |
| 41 | Inventory structure and foreground inventory table | One row per foreground exchange with every field of the "minimum inventory evidence" table: process/exchange, amount and unit, provider, data type, source, geography/year, uncertainty/limitation |
| 42 | Data-source register | Every important item classified as database-supplied, adapted proxy, student-created process or placeholder |
| 43 | Cross-database compatibility check | Stated as not applicable (single database), with the three intra-ELCD checks from D1 §9 re-done in the model: data generation, flow identity, biogenic carbon |
| 44 | LCIA method, categories, settings, reasons | CML-IA baseline (version string read from the method in the database), the two categories, full calculation settings, and the reasons already argued in D1 §10 |
| 45 | Preliminary absolute results with units and comparison basis | Per pitch-year and per cut, both categories, both alternatives, before any relative chart |
| 46 | Hotspot/contribution analysis, ≥ 2 categories | By process and by elementary flow, both categories, both alternatives |
| 47 | Model-validation evidence | Database validation, linking check, residual product/waste flows, LCIA unmapped-flow list, plus an independent recalculation |
| 48 | ≥ 1 preliminary sensitivity or bounding analysis | S1 and S2 (both committed), the placeholder bound, delivery distance; S5 and S3 if time allows |
| 49 | Difficulties, risks, corrective action plan with owners | Table: element, symptom, checks attempted, decision required, owner, due date |

---

## 2. Corrections to D1 found while preparing this plan

The D2 report will say plainly what changed since D1 and why.

1. **B2 is a student-created process, not an "adapted" one.** In the instructions (§3.2) an adapted proxy is a copied database dataset renamed `PROXY - …`. B2 (battery charging) is built from scratch, so it is a `STUDENT MODEL`. The minimum design is still met: two student-created processes (A2, B2).
2. **Placeholder name format.** D1 wrote `DATAGAP-engine lubricating oil-ZERO-BURDEN PLACEHOLDER`. The required format is `DATA GAP - engine lubricating oil - ZERO-BURDEN PLACEHOLDER`.
3. **Biogenic carbon at the tailpipe.** D1's screening counted all 3.16 kg CO₂ per kg diesel as fossil. The ELCD diesel mix contains 5.75 wt.% bio-components and records an uptake of 0.129 kg CO₂ per kg. A2 will split the tailpipe CO₂ into fossil (3.031 kg) and biogenic (0.129 kg), so the bio-carbon nets to zero under every method (CML, EF 3.0 and ILCD alike). Effect, by my arithmetic, still to be confirmed in openLCA:
   - Alternative A per kg diesel: 3.67 → 3.56 kg CO₂-eq (−3 %, with delivery now included)
   - B/A on the EU-27 mix at η = 0.75: 0.66 → 0.68
   - Break-even efficiency: 0.50 → 0.51; break-even grid intensity: 0.74 → 0.72 kg CO₂-eq/kWh
   - **Bulgaria (0.74) moves above the break-even line**, so H4's "six national mixes" becomes seven. The hypothesis table in D2 will report this, together with the fact that Bulgaria lies only 3 % above the line.
   - (Updated 26 Oct after phase 3: values from the calculation sheet, which also uses the unrounded time per cut.)
4. **One lorry dataset, used consistently.** D1's table names the 22 t lorry (0.066 kg CO₂-eq per t·km), but the "< 1 %" check used the 7.5 t small lorry (0.137). The baseline will use the 22 t lorry (bulk fuel delivery); the small lorry goes into the distance sensitivity. Either way delivery is about 0.3 % of A.
5. **Roles.** D1 promised to confirm roles in D2; three rows still say `[Name]`.
6. **Values marked † (unverified)** must be checked against the original source or kept visibly marked (see §4).

---

## 3. The openLCA model

### 3.1 Database and backups
- Create a **new database** from the instructor's `.zolca` (openLCA: restore/import as a new database), named `Group_Project_Mowing_LCA`. The Lab 1/Lab 2 database is left untouched, and the submitted file holds only ELCD plus our foreground.
- Take a JSON-LD backup of the foreground before each structural step (the Lab 2 method), and freeze a copy of the submitted version before any later correction (instructions §8 advice).
- Build through the openLCA IPC server with a re-runnable script (`d2_build_model.py`, same approach as `Lab 2 - openLCA\build_lab2_model.py`), then check everything visually in the app, as you asked for Lab 2.

### 3.2 Global parameters (one place for every assumption)

| Parameter | Baseline | Unit | Source / status |
|---|---|---|---|
| `n_cuts` | 30 | cuts/yr | [4] maintenance programme |
| `area` | 7 140 | m² | 105 × 68 m |
| `width` | 1.52 | m | Toro spec [5] |
| `speed` | 7 | km/h | † to verify |
| `field_eff` | 0.80 | – | † to verify (ASABE D497) |
| `t_cut` | `area/(width*speed*1000*field_eff)` = 0.839 | h | derived |
| `P_rated` | 18.4 | kW | Toro spec [5] |
| `load` | 0.50 | – | † to verify |
| `sfc` | 0.270 | kg/kWh | EMEP/EEA Table 3-6 [2], re-read |
| `eta` | 0.75 | – | † to verify |
| `d_km` | 150 | km | † to justify |
| `mix_EU27`, `mix_SE`, `mix_FR`, `mix_DE`, `mix_PL`, `mix_EE` | 1, 0, 0, 0, 0, 0 | – | S1 switches |
| `lube_kg_per_kg` | to be researched (≈ 0.005–0.01) | kg/kg diesel | for the placeholder bound only |

### 3.3 Foreground processes (names follow the instructions' formats)

| ID | openLCA process name | Reference output | Inputs (provider) | Data type |
|---|---|---|---|---|
| A1 | `STUDENT MODEL - Diesel delivered to the club - EU-27/2008-2015` | 1 kg diesel at club tank | 1 kg Diesel (ELCD *Diesel mix at refinery … 5.75 wt.% bio {EU-27}*); `d_km/1000` t·km (ELCD *Lorry transport … 22 t … {RER}*) | Student model on database data |
| A2 | `STUDENT MODEL - Diesel combustion in ride-on mower engine, 8-19 kW - EU/2023` | 1 kg diesel burned | 1 kg diesel at club tank (A1). Emissions to air on ELCD's own lorry flows: CO₂ fossil 3.031 kg, CO₂ biogenic 0.129 kg, CH₄, N₂O, NOₓ, CO, NMVOC, PM2.5 (EMEP/EEA 2023 Table 3-1) | **Student model (constructed)** |
| A3 | `STUDENT MODEL - One cut of the pitch, diesel ride-on mower - EU/2026` | 1 cut | `t_cut*P_rated*load*sfc` kg diesel burned (A2); lube oil (placeholder) | Student model |
| A4 | `STUDENT MODEL - Mowing service, one pitch-year, diesel - EU/2026` | 1 pitch-year | `n_cuts` cuts (A3) | Student model (reference process) |
| B1 | `STUDENT MODEL - Electricity at the club socket - EU-27/2008-2015` | 1 kWh at socket | 1 kWh × `mix_XX` from each ELCD *Electricity grid mix, at consumer, < 1kV {XX}* (6 inputs, providers set by hand) | Student model on database data |
| B2 | `STUDENT MODEL - Battery charging and electric drive losses, ride-on mower - EU/2026` | 1 kWh delivered to the drive | `1/eta` kWh at socket (B1) | **Student model (constructed)** |
| B3 | `STUDENT MODEL - One cut of the pitch, battery-electric ride-on mower - EU/2026` | 1 cut | `t_cut*P_rated*load` kWh delivered (B2) | Student model |
| B4 | `STUDENT MODEL - Mowing service, one pitch-year, battery-electric - EU/2026` | 1 pitch-year | `n_cuts` cuts (B3) | Student model (reference process) |
| Gap | `DATA GAP - engine lubricating oil - ZERO-BURDEN PLACEHOLDER` | 1 kg lube oil | none (burden omitted, not zero; documentation tab filled) | Placeholder 1 of max. 2 |
| Bound | `PROXY - engine lubricating oil - based on Light fuel oil at refinery {EU-27}` | 1 kg lube oil | 1 kg Light fuel oil (ELCD) | Adapted proxy, used only in the bound |

Every process gets its documentation tab completed (sources, geography, time, technology, calculation reference).

### 3.4 Product systems, comparison project and settings
- `PS-A Diesel ride-on mowing, one pitch-year` and `PS-B Battery-electric ride-on mowing, one pitch-year`. Providers set explicitly; no automatic linking left unchecked (ELCD has 64 providers of the product flow *Electricity*).
- An openLCA **Project** comparing both, with one variant per scenario (parameter redefinitions). The scenarios are then visible and re-runnable inside the app, not only in scripts.
- Calculation settings, reported in D2: openLCA 2.7.0; CML-IA baseline as bundled; allocation as defined in processes (no multi-output process in the baseline); no regionalisation, costs, uncertainty, normalisation or weighting.

---

## 4. Checking the open assumptions (the † items)

Each item will be checked against the original source. Anything that cannot be verified stays marked † in D2, with the sensitivity range that covers it.

| Item | D1 value | What to look for | Where |
|---|---|---|---|
| Mowing speed | 7 km/h | Typical rotary-mower operating speed | Toro GM3200/e3200 specifications; ASABE D497 machinery data |
| Field efficiency | 0.80 | Typical value for rotary mowers | ASABE D497 |
| Engine load factor | 0.50 | Load factor for commercial turf diesel equipment | US EPA NONROAD documentation; EMEP/EEA 1.A.4 |
| Specific fuel consumption | 270 g/kWh | Re-read the 8–19 kW Stage V row | EMEP/EEA 2023 Table 3-6 |
| Socket-to-work efficiency η | 0.75 | Charger, battery round-trip, inverter and motor efficiencies | Manufacturer data; peer-reviewed or technical sources |
| e3200 battery capacity and runtime | "one cut fits one charge" | Pack kWh and runtime per charge | Toro product literature |
| Delivery distance | 150 km | A defensible refinery/depot-to-site distance | EU fuel-logistics sources, or keep as an assumption bounded at 50–500 km |
| Lube-oil use | ≈ 1 % of fuel | Sump capacity and change interval for the engine class | Engine operator manual |
| Tailpipe emission factors | Table 3-1 | Re-read every number | EMEP/EEA 2023 [2]; IPCC 2006 Vol. 2 Ch. 3 [3] as cross-check |
| References [4] (Sport England), [7], [9], [10] | † | Retrieve and confirm bibliographic details and values | Original publications |
| Present-day EU grid intensity | † | Latest value, for the S1 discussion only | EEA indicator [10] |

---

## 5. Calculation sheet

`Group_Project_Deliverable2_v1_<date>_calculation_sheet.xlsx`, with live formulas and original values and units kept (instructions §3.3 step 14 and §10):

1. **Parameters** — the §3.2 table with sources
2. **Activity data** — time per cut, work, diesel and electricity per cut and per year
3. **A2 inventory** — EMEP factors per tonne → per kg; fossil/biogenic CO₂ split; carbon balance check
4. **Placeholder bound** — lube oil: low (zero), central (light-fuel-oil proxy), high (proxy plus full oxidation of the used oil)
5. **Independent check** — ELCD values × CML factors, compared with the openLCA results
6. **Scenarios and break-evens** — S1 across all 31 ELCD mixes, S2 ranges, break-even formulas

---

## 6. Validation (item 47)

| Check | How | Pass condition |
|---|---|---|
| Database validation | openLCA Database → Validate, screenshot | No errors on our objects; any pre-existing ELCD warnings listed separately |
| Linking | Model graph plus a script listing every foreground input and its provider | Every input linked to the intended provider; electricity country confirmed |
| Residual flows | Inventory result scanned for product or waste flows | None left (all technosphere flows linked) |
| LCIA coverage | Inventory elementary flows with no factor in each category, with amounts | Only the expected ones (e.g. biogenic CO₂ by design, uranium under the fossil category by definition, NOₓ/CO under GWP); anything else is investigated |
| Units and signs | Spot checks, e.g. A2 output per kg, 1 kWh = 3.6 MJ | Match the calculation sheet |
| Independent recalculation | Python/Excel from ELCD values | Within 0.5 % of openLCA |
| Scaling | `n_cuts` = 60 | Both results exactly double (H6) |
| Plausibility | vs D1 screening values and Saidani & Kim (2021): 32 % lower CO₂ for an electric riding mower | Differences explained |

---

## 7. Results, hotspots and sensitivity (items 45, 46, 48)

- **Baseline table:** A and B per pitch-year and per cut, GWP100a (kg CO₂-eq) and ADP fossil (MJ), absolute values first. Next to it, the inventory flows D1 promised: NOₓ, CO, NMVOC and PM2.5 in g per pitch-year, emitted at the pitch for A and at power stations for B. Then one bar chart per category, never mixing units.
- **Contributions:** by process (A: diesel supply / delivery / tailpipe; B: grid mix) and by flow (fossil CO₂, CH₄, N₂O; crude oil, natural gas, hard coal, lignite) for both categories. This tests H3 (≈ 87 % tailpipe, ≈ 13 % fuel supply, < 1 % delivery).
- **S1 grid mix (committed):** six mixes as project variants (EU-27, SE, FR, DE, PL, EE), plus a 31-mix table and the break-even grid intensity, read from the model results.
- **S2 energy per cut (committed):** load 0.4/0.5/0.6, time per cut 0.52/0.84/1.0 h (low end widened after phase 2, see the source log), η 0.65/0.75/0.85, and the break-even η for both categories. Load and time per cut scale A and B equally, so they move the absolute values but not the ratio; only η can change the ranking. D2 will state this.
- **Placeholder bound:** lube oil low/central/high, with a statement of whether the ranking holds.
- **Delivery distance:** 50/150/500 km, 22 t and 7.5 t lorry.
- **If time allows:** S5 (EF 3.0 instead of CML-IA; cheap, only the method changes) and S3 (petrol variant; needs one more combustion process). S4 (capital goods) stays an off-model literature bound, labelled as such, under fallback F3, unless the instructor asks otherwise.
- **Hypotheses H1–H6:** one table of what was expected and what the model shows.

---

## 8. The D2 report

Same look as D1, generated by Python (`d2_content.py` reusing `_docx_helpers.py`) and render-checked in Word with `word_safe.ps1`.

1. Title block, version, file name; group members and **confirmed** roles; changes since D1 (§2 of this plan) and any instructor conditions on D1
2. Goal and scope update (item 40)
3. Model and system diagram (items 38, 39): database, files, process list, model graphs, updated Figure 1
4. Inventory: structure and foreground inventory table (item 41)
5. Data-source register (item 42)
6. Database compatibility (item 43)
7. LCIA method and calculation settings (item 44)
8. Preliminary results (item 45)
9. Contribution analysis (item 46)
10. Model validation (item 47)
11. Sensitivity and bounding (item 48), with the hypothesis table
12. Difficulties, risks and corrective action plan with owners (item 49)
13. References, each with its verification status; AI-assistance declaration (updated)

Appendix: calculation sheet, list of submitted files.

---

## 9. Files

All new work goes in a folder `Deliverable 2\` inside this project folder:

- `Group_Project_Deliverable2_v1_<date>.docx` and `.pdf` — the report
- `Group_Project_Deliverable2_v1_<date>.zolca` (or JSON-LD `.zip`) — the model
- `Group_Project_Deliverable2_v1_<date>_calculation_sheet.xlsx`
- `figures\` — model-graph captures, system diagram, result and contribution charts
- `scripts\` — `d2_build_model.py`, `d2_verify_model.py`, `d2_results.py`, `make_diagram_d2.py`, `d2_content.py`
- `backups\` — JSON-LD backups and the frozen submitted model

---

## 10. Order of work

| Phase | What happens | Who |
|---|---|---|
| 0 | Answer the questions in §12 | You |
| 1 | Create the project database in openLCA and start the IPC server (Tools → Developer tools → IPC Server, port 8080) | You (two minutes), or me with your OK |
| 2 | Check the † items (§4) and fix the parameter values | Me |
| 3 | Build the calculation sheet (§5) | Me |
| 4 | Build the model through IPC; check it in the app; capture the model graphs | Me |
| 5 | Validation (§6) | Me |
| 6 | Results, contributions, sensitivities (§7) | Me |
| 7 | Figures and report draft; render check in Word | Me |
| 8 | Full double-check: every number in the report against openLCA and the calculation sheet; every reference; every remaining †. Then freeze and export the model | Me |
| 9 | Review, then submit through the course form | You (I do not submit anything) |

---

## 11. Known risks and fallbacks

| Risk | Fallback |
|---|---|
| No published energy use for either mower | F1: keep the engineering estimate and widen S2. The B/A ratio depends only on η and verified per-unit values, so the comparison stays answerable. |
| The bundled CML-IA factors fail the coverage check | F4: switch to EF 3.0 with the uranium and CO caveats from D1 §10 |
| `.zolca` too large for the upload form | JSON-LD export of the foreground, with re-import instructions |
| Word PDF export hangs (seen on 19 Oct) | Render page by page with `word_page_emf.ps1`; check numbers in the .docx text |
| IPC writes not visible in the navigator | Refresh (F5) and re-open, as in Lab 2 |

---

## 12. Questions to answer before starting

1. **Group members and roles.** Full names of the other members and who takes which role (the corrective-action owners depend on it). Is there a group number or name for file naming?
2. **Deadline** for Deliverable 2. This decides whether S5 and S3 are included.
3. **Instructor feedback on D1 v2.** Was it approved, or approved with conditions? Any condition must be answered in D2.
4. **The submission form.** Does the course page ask for anything beyond the instructions PDF: specific fields, a page limit, a required model format (`.zolca` or JSON-LD), a file-size limit?
5. **Database creation.** Will you create the new openLCA database yourself, or do you want me to do it?
