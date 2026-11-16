"""Deliverable 1 (revised topic) — Project Proposal: diesel vs battery-electric
mowing of one natural-grass football pitch for one maintenance year. ELCD primary."""

from _docx_helpers import *          # noqa: F401,F403  (doc, styles, helpers)
from _docx_helpers import (doc, rich, para, heading, bullet, build_table, rule,
                           GREY, NAVY, SLATE, Cm, Inches, Pt,
                           WD_ALIGN_PARAGRAPH)

# ================================================================== TITLE BLOCK
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(1)
r = p.add_run("LCA LABORATORY  ·  GROUP PROJECT  ·  DELIVERABLE 1  ·  REVISED TOPIC")
r.bold = True
r.font.size = Pt(8.5)
r.font.color.rgb = GREY

p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
r = p.add_run("Project Proposal — Independent Comparative LCA")
r.bold = True
r.font.size = Pt(17)
r.font.color.rgb = NAVY

para("Football-pitch mowing systems: a comparative screening LCA of combustion-powered and "
     "battery-electric mowing of one natural-grass pitch for one maintenance year",
     size=11.5, color=SLATE, space_after=4)
para("Version 2, 12 October 2026. Replaces version 1 (natural grass versus 3G artificial turf, "
     "21 September 2026) following instructor approval of the revised topic. Primary database: ELCD.",
     size=8.5, color=GREY, space_after=6)
rule()

# ================================================================== 1. ADMIN
heading("1  Project title, group members and provisional roles", 1)
build_table(
    ["Role", "Member", "Responsibility in this project"],
    [["Goal & scope lead", "[Name]",
      "Functional unit, reference flows, system boundary, the equal-cutting-service argument"],
     ["Inventory & data lead", "Tal Mizrahi",
      "ELCD dataset inspection, data-source register, fuel and electricity per cut, calculation sheets"],
     ["Constructed-process lead", "Tal Mizrahi",
      "Mower combustion process (A2) from EMEP/EEA emission factors; battery charging process (B2)"],
     ["Modelling & LCIA lead", "[Name]",
      "openLCA build, provider linking, flow and method coverage checks, contribution analysis"],
     ["Sensitivity & interpretation lead", "[Name]",
      "Scenarios S1–S5, the two break-even values, presentation and defense coordination"]],
    widths=[2200, 1700, 5964], font=8.2)
para("All members contribute to the final presentation and defense. Roles are provisional and will "
     "be confirmed in Deliverable 2. Software and data on record: openLCA 2.7.0; ELCD 3.2 as the "
     "instructor-provided file `elcd_3_2_greendelta_v2_18_correction_20220908.zolca` (608 processes, "
     "44 bundled LCIA methods); CML-IA baseline as bundled in that file.",
     size=8.5, color=GREY, space_after=4)
para("**Markers used throughout.** † a value or source not yet verified against the original. "
     "‡ a screening value computed outside openLCA from the ELCD inventories and the bundled "
     "characterisation factors, to be reproduced in openLCA before it is used as a result. "
     "Numbers in square brackets refer to §13.",
     size=8.5, color=GREY, space_after=4)

# ================================================================== 2. SYSTEM
heading("2  Product system and context", 1)
para("An existing natural-grass pitch has to be mown whatever else is done to it. A generic "
     "community-pitch programme allows for **at least 30 cuts a year**, weekly or twice weekly in "
     "the growing season, at a 30–40 mm height of cut [4]. The pitch, the grass and the cutting "
     "regime are fixed; the one thing the grounds manager chooses is the machine. This study "
     "compares the two ways of powering it: **Alternative A**, a diesel ride-on rotary mower, and "
     "**Alternative B**, its battery-electric equivalent.")
para("The two exist as a matched pair. The Toro Groundsmaster 3200 (18.4 kW diesel) and the "
     "Groundsmaster e3200 (11 lithium-ion battery modules, 3.3 kW on-board charger) share the same "
     "chassis, mowing deck and controls [5]. That is what lets the cutting service be held "
     "constant: the same deck, the same width of cut, the same number of passes. The machines "
     "serve as a technical reference for the two powertrains, not as a brand comparison.")
para("A battery mower emits nothing at the pitch, which is where the intuitive answer comes from. "
     "Over the life cycle its burden moves to the power stations that charge it, so the comparison "
     "turns on two things: how much energy each machine needs for the same cut, and how the "
     "electricity is made. The national electricity mixes in ELCD differ by a factor of about 75 "
     "in carbon intensity (0.02 to 1.33 kg CO₂-eq per kWh‡), so the answer is not settled in advance.")
para("The question is current. Regulation (EU) 2016/1628 (Stage V) tightened exhaust limits for "
     "non-road engines, including the small diesel class used here [8]; the battery version of this "
     "mower was introduced in 2023 [5]; and clubs and municipalities replacing a mower now face "
     "exactly this choice.", space_after=4)

# ================================================================== 3. RQ
heading("3  Research question", 1)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
p.paragraph_format.space_after = Pt(6)
rich(p, "*For mowing one existing full-size natural-grass football pitch for one maintenance year, "
        "how do combustion-powered and battery-electric mowing compare in climate-change and "
        "fossil-resource impacts?*", size=10.5, color=SLATE)
para("This is the instructor-approved wording, reproduced unchanged. We expect a conditional answer "
     "rather than a single winner: battery-electric mowing should be preferable below a **break-even "
     "grid carbon intensity** and above a **break-even charging efficiency**. Reporting those two "
     "values tells a grounds manager whether the result applies to their own grid and machine.",
     space_after=4)

# ================================================================== 4. JUSTIFICATION
heading("4  Justification: environmental relevance, audience and intended use", 1)
bullet("**Environmental relevance.** Burning 1 kg of diesel in the mower carries about "
       "**3.7 kg CO₂-eq**‡: 87 % leaves the exhaust at the pitch and 13 % was emitted making the "
       "fuel. The same work done electrically carries anything from almost nothing to nearly twice "
       "that, depending on the grid. The two systems have opposite profiles, one emitting where it "
       "works and the other where its electricity is generated.")
bullet("**Decision relevance.** One pitch-year is small, on the order of 60–80 kg of diesel†, but "
       "mowers are bought as fleets, kept for about a decade, and the choice of powertrain is made "
       "once at purchase.")
bullet("**Intended audience.** Grounds managers of clubs and municipalities choosing a replacement "
       "mower, and the sports associations that part-fund equipment.")
bullet("**Intended use.** Instructional screening LCA for internal learning and discussion. It is "
       "explicitly **not** an ISO 14044-conformant comparative assertion intended for public "
       "disclosure [12], and no such claim will be made.")
_rel = para("**Relation to existing studies.** Published LCAs compare petrol and electric mowers "
     "for household lawns. Saidani and Kim (2021) report 32 % lower life-cycle CO₂ for an electric "
     "riding mower in the United States [6]; an earlier comparison is Sivaraman and Lindner "
     "(2004)† [7]. We will use them **only as plausibility benchmarks** for our own results, never "
     "as an inventory source. Our own contribution is the pitch-year functional unit for a "
     "sports-turf machine, a model built on ELCD alone, and explicit break-even values for grid "
     "intensity and charging efficiency.", space_after=4)
_rel.paragraph_format.space_before = Pt(8)

# ================================================================== 5. FU
heading("5  Preliminary functional unit and reference flows", 1)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.5)
p.paragraph_format.space_after = Pt(6)
rich(p, "**Functional unit.** *The mowing of one existing full-size natural-grass football pitch "
        "(105 × 68 m, 7 140 m² mown area) for one maintenance year: 30 cuts at a 30–40 mm height "
        "of cut with a ride-on rotary mower of 1.52 m cutting width, clippings returned, in a "
        "temperate European climate.*", size=10)
para("“Same cutting service” is the equivalence condition set in the approved scope: the same "
     "pitch area, the same number of cuts and the same finish. The shared deck makes it concrete. "
     "Qualities that differ and are **not** captured by the functional unit are stated rather than "
     "hidden: noise, exhaust at the pitch, and refuelling versus overnight charging. Range is not a "
     "constraint, since one cut needs roughly 8 kWh of work†, well within one charge†.")

build_table(
    ["Alternative", "Reference flow (preliminary)", "Basis of the assumption"],
    [["**A** — Diesel ride-on mowing",
      "≈ **63 kg (76 L) of diesel** burned in the mower per pitch-year = 30 cuts × 0.85 h† × "
      "9.2 kW mean engine output† × 270 g/kWh",
      "18.4 kW Stage V engine [5] at 50 % load†; specific fuel consumption for an 8–19 kW "
      "Stage V engine from EMEP/EEA Table 3-6 [2]"],
     ["**B** — Battery-electric ride-on mowing",
      "≈ **313 kWh of electricity** drawn at the socket per pitch-year = 30 cuts × 0.85 h† × "
      "9.2 kW† ÷ 0.75†",
      "The same work at the mower as A. This is conservative for B if, as expected, it avoids the "
      "losses of A's hydraulic traction drive and of idling†. Socket-to-work efficiency of 75 %† "
      "to be replaced by manufacturer or metered data"]],
    widths=[2100, 4100, 3664], font=8.0, keep_together=True)

para("Time per cut follows from 7 140 m² ÷ (1.52 m × 7 km/h† × 0.8 field efficiency†) ≈ 0.85 h, "
     "about 25 machine-hours a year. The mown area excludes run-offs, which scale both alternatives "
     "identically. The number of cuts multiplies both reference flows by the same factor, so it "
     "changes the absolute results but not the ranking. The programme [4] prefers a cylinder cut "
     "and accepts a rotary mower with roller; we model the rotary pair because it is the one "
     "available with both powertrains on one platform. Both flows will be re-derived in a "
     "calculation sheet kept with the model.",
     size=8.5, color=GREY, space_after=4)

# ================================================================== 6. BOUNDARY
heading("6  Preliminary system boundary and explicit exclusions", 1)
para("The study covers **the energy carrier from resource to mower, for one pitch-year**. For "
     "Alternative A that is crude-oil extraction and refining, delivery to the club, and combustion "
     "in the mower engine with its direct emissions. For Alternative B it is fuel extraction, power "
     "generation, transmission and distribution to the socket, and the losses of charging; there "
     "are no direct emissions at the pitch. Figure 1 shows the boundary.")
para("**Explicit exclusions, as approved:** pitch construction, artificial turf, irrigation, "
     "fertilisation and all other maintenance (aeration, topdressing, overseeding, line marking). "
     "They are identical under both alternatives and outside the mowing decision. Operator labour "
     "and travel, the machinery shed and the charging point are excluded on the same ground. "
     "Clippings are returned to the turf in both alternatives and are not modelled.")
para("**Mower and battery manufacture are conditional.** The approved scope admits them only if "
     "datasets can be imported and allocated reliably, and we add one rule: they are included for "
     "both alternatives or for neither. The baseline excludes them. ELCD has no lithium-ion cell, "
     "electric motor or electronics dataset, and its only battery entry, `Dummy_Battery`, is an "
     "empty dummy process with one product output and no inputs or emissions. Because the pair "
     "shares chassis and deck, what actually differs is the powertrain: engine and hydraulic drive "
     "against battery pack, motors and charger.")
para("**This exclusion is not neutral, and we say so.** It probably favours Alternative B, because "
     "a battery pack is more burdensome to make than a small diesel engine. Its size depends "
     "almost entirely on allocation: one pitch-year uses about 25 hours† of a machine that may work "
     "several hundred hours a year†. A pack of 20–40 kWh† at 61–106 kg CO₂-eq per kWh [9] "
     "embodies 1–4 t CO₂-eq, against an expected use-phase saving of roughly 80 kg CO₂-eq per "
     "pitch-year‡. Dedicated to one pitch, the pack could cancel the saving; shared across a fleet's "
     "workload it shrinks to a few percent. Scenario S4 tests this.")
para("**Common conventions applied to both alternatives:** one system boundary, one LCIA method, "
     "one geography (EU-27), and one generation of ELCD data (the 2008–2015 datasets, §9). No "
     "allocation arises in the baseline, because neither system yields a co-product. It arises "
     "only in S4, where a machine shared between pitches is allocated by machine-hours.",
     space_after=4)

doc.add_picture("system_boundary.png", width=Inches(5.9))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.paragraphs[-1].paragraph_format.space_after = Pt(3)
doc.paragraphs[-1].paragraph_format.keep_with_next = True
cap = doc.add_paragraph()
cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
cap.paragraph_format.space_after = Pt(10)
rich(cap, "**Figure 1.** Preliminary system boundary. Four foreground processes per alternative, "
          "converging on a common functional unit; quantities are preliminary.",
     size=8, color=GREY)

# ================================================================== 7. HYPOTHESES
heading("7  Expected comparison and initial hypotheses", 1)
para("These are **expectations to be tested**, not conclusions. They rest on the screening values "
     "below‡ and on provisional activity data†.", space_after=5)
build_table(
    ["Quantity", "Climate change (kg CO₂-eq)", "Fossil resource (MJ)", "Basis"],
    [["Diesel at the refinery gate, per kg", "0.47", "48.9",
      "ELCD diesel mix {EU-27} × CML-IA baseline"],
     ["Diesel burned in the mower, per kg", "3.20", "—",
      "EMEP/EEA Table 3-1 [2]: CO₂ 3 160, CH₄ 0.083, N₂O 0.135 g per kg of fuel"],
     ["**Alternative A, per kg of diesel**", "**3.67**", "**48.9**",
      "Sum of the two rows. At 270 g/kWh, 1 kg of diesel yields 3.7 kWh of engine work"],
     ["**Alternative B, per kWh at the socket**", "**0.49**", "**5.5**",
      "ELCD grid mix {EU-27}, < 1 kV × CML-IA baseline"]],
    widths=[3000, 1750, 1500, 3614], font=8.0, keep_together=True)
para("", space_after=2)
build_table(
    ["", "Expectation", "How it will be tested"],
    [["H1", "**On the EU-27 mix, B has the lower climate-change impact**, by about one third. With "
            "equal work at the mower the ratio B/A is 0.50 ÷ η, where η is B's socket-to-work "
            "efficiency: 0.66 at η = 0.75†.",
      "Baseline; S2"],
     ["H2", "**B has the lower fossil-resource impact by a wider margin**, about 45 % (B/A is "
            "0.42 ÷ η), because part of the grid is non-fossil while diesel is entirely fossil "
            "apart from its bio-blend.",
      "Baseline; S2"],
     ["H3", "**A is dominated by the exhaust.** About 87 % of A's climate impact is tailpipe CO₂ "
            "and about 13 % is fuel supply; delivery to the club is below 1 %.",
      "Contribution analysis, both categories"],
     ["H4", "**The electricity mix governs the ranking.** The break-even grid intensity is about "
            "0.99 × η kg CO₂-eq/kWh, or 0.74 at η = 0.75†. Six of ELCD's 30 national mixes lie "
            "above it (CZ, CY, GR, PL, MT, EE: 0.83–1.33), where A would rank better; on the "
            "French or Swedish mix B would be 85–92 % lower.",
      "S1, with the break-even reported"],
     ["H5", "**B wins unless it wastes half its electricity.** On the EU-27 mix the break-even "
            "socket-to-work efficiency is about 50 % for climate change and 42 % for fossil "
            "resource.",
      "S2, with the break-even reported"],
     ["H6", "**Mowing frequency does not change the ranking**: it scales both alternatives "
            "equally. It matters only once capital goods are included, because fixed burdens are "
            "then spread over more or fewer hours.",
      "Scaling check at 60 cuts; S4"]],
    widths=[560, 6304, 3000], font=8.0)

para("**Two limitations stated up front.** First, the two approved categories do not register "
     "NOₓ, CO, NMVOC or particulates, the pollutants for which small engines are regulated. "
     "Alternative A emits them at ground level beside the pitch; Alternative B emits them at power "
     "stations. We will report them as inventory flows in grams per pitch-year next to the LCIA "
     "results, and state that our conclusion does not cover local air quality or noise. Second, "
     "the ELCD datasets are valid for 2008–2015, and the European grid has since become markedly "
     "less carbon-intensive [10]. The baseline is therefore conservative for Alternative B, and "
     "S1 reports results across the full range of grid intensities so that a present-day value "
     "can be read off.", size=8.5, color=GREY, space_after=4)

# ================================================================== 8. FEASIBILITY
heading("8  Data feasibility table", 1)
para("ELCD dataset names, quantitative references, geographies and validity periods below were "
     "**read from the course database itself**, not recalled. Each dataset will still be opened and "
     "inspected in openLCA (quantitative reference, geography, reference year, technology, "
     "providers) before it is accepted, in line with the evidence hierarchy. Emission factors were "
     "read from the cited EMEP/EEA tables.",
     size=8.5, color=GREY, space_after=5)

build_table(
    ["Required element", "Data strategy", "Exact dataset / source", "Main mismatch or gap", "Fallback"],
    [
     ["Main product / reference flow — A", "Existing + constructed",
      "No single dataset; assembled from A1–A4. ELCD has no machinery-operation dataset for turf or "
      "agriculture: its only off-road entries are a 100 kW construction excavator, a 500 kW mining "
      "excavator and a 220 t mining truck",
      "Fuel per cut is an engineering estimate (rated power × load factor × specific consumption), "
      "not a measurement",
      "S2 varies load factor and time per cut; metered fuel logs from a club or municipality if "
      "obtainable (F1)"],
     ["Main product / reference flow — B", "Existing + adapted",
      "Assembled from B1–B4; no battery-mower dataset exists",
      "Electricity per cut assumed from equal work ÷ efficiency. The manufacturer publishes battery "
      "count and charger power [5] but no energy use per hour",
      "S2 bounds the efficiency; manufacturer data request; metered charger energy (F1)"],
     ["Principal energy carrier — A (diesel)", "Existing",
      "*Diesel mix at refinery, production mix, at refinery, from crude oil and bio components, fuel "
      "supply, 10 ppm sulphur, 5.75 wt.% bio components* {EU-27}. LCI result; reference 1 kg; valid "
      "2008–2015",
      "Ends at the refinery gate. Contains 5.75 wt.% bio components, so tailpipe CO₂ must be split "
      "into fossil and biogenic to match",
      "Split by the dataset's own carbon uptake (0.129 kg CO₂ per kg fuel‡). Bound: *Diesel, "
      "consumption mix, at refinery, from crude oil, 200 ppm sulphur* {EU-15}, fossil only"],
     ["Principal energy carrier — B (electricity)", "Existing",
      "*Electricity grid mix, consumption mix, at consumer, AC, < 1kV* {EU-27}. LCI result; "
      "reference 3.6 MJ (1 kWh); valid 2008–2015",
      "Vintage: today's grid is less carbon-intensive [10]. 64 processes supply the product flow "
      "`Electricity`, so automatic linking can select the wrong country",
      "Default provider set by hand and checked in the model graph; S1 sweeps the national mixes"],
     ["Direct emissions — A (combustion in the mower)", "**Construct**",
      "Group-built process A2: 1 kg `Diesel` in, emissions to air out, on the elementary flows that "
      "ELCD's own *Small lorry transport* {RER} unit process uses. Factors from EMEP/EEA 2023 "
      "Table 3-1, diesel, NFR 1.A.4.a.ii [2], per tonne of fuel: CO₂ 3 160 kg; CH₄ 83 g; N₂O 135 g; "
      "NOₓ 32 629 g; CO 10 774 g; NMVOC 3 377 g; PM2.5 2 104 g",
      "Tier 1 factors are fleet averages over engine ages, not a Stage V mower. The CO₂ factor "
      "assumes complete oxidation of fuel carbon",
      "Tier 3 Stage V factors from Table 3-6 (8–19 kW: NOₓ 6.08, CO 3.96, PM 0.40 g/kWh). "
      "IPCC 2006 defaults† [3] as a cross-check on CO₂ (F2)"],
     ["Charging — B", "**Adapt**",
      "Group-built process B2: socket electricity in, electricity delivered as work out, with "
      "charger, battery and drive losses (η ≈ 0.75†)",
      "No measured efficiency for this machine class; standby draw of the on-board charger unknown",
      "Bound η at 0.65 / 0.75 / 0.85 and report the break-even efficiency (S2)"],
     ["Transport — A (fuel delivery)", "Existing",
      "*Lorry transport, Euro 0, 1, 2, 3, 4 mix, 22 t total weight, 17,3t max payload* {RER}. LCI "
      "result; reference 1 t·km; valid 2005–2010; 150 km† from refinery to club",
      "Pre-Euro 5 fleet; distance assumed; fuel retail stage not represented",
      "Expected below 1 % of A‡; tested at 50 / 150 / 500 km"],
     ["Transport — B", "Not applicable",
      "Transmission and distribution down to < 1 kV are inside the ELCD “at consumer” dataset",
      "Losses are an EU-27 average, not those of a specific network",
      "None needed"],
     ["Use / end-of-life — A + B", "Existing (use); excluded (end-of-life)",
      "The use phase is the mowing itself, covered by the rows above. The energy carriers leave no "
      "waste to treat; clippings are returned to the turf in both alternatives",
      "End-of-life belongs to the capital goods, which the baseline excludes",
      "Enters only with S4"],
     ["Capital goods — powertrain and battery pack", "**Excluded (conditional)**",
      "ELCD holds steel, aluminium, copper and polymer datasets (e.g. *Steel hot rolled coil* {RER}, "
      "*Aluminium sheet* {RER}, *Polypropylene granulate (PP)* {RER}) but no lithium-ion cell, "
      "motor or electronics dataset",
      "The battery pack is a possible hotspot for B, so it may **not** be entered as a zero-burden "
      "placeholder",
      "Import only with documented flow mapping; otherwise an off-model literature bound (S4, F3)"],
     ["Engine lubricating oil — A", "**Placeholder 1 of 1**",
      "`DATAGAP-engine lubricating oil-ZERO-BURDEN PLACEHOLDER`",
      "No lubricant dataset in ELCD; mass about 1 % of the fuel†. Burden is **omitted, not zero**, "
      "and the omission favours A",
      "Bounded with *Light fuel oil at refinery* {EU-27} mass-for-mass as a refinery-product proxy"],
    ],
    widths=[1750, 1150, 2900, 2250, 1814], font=7.3)

para("The single placeholder sits on a **minor, non-hotspot** stream, satisfying the rule that a "
     "placeholder may not stand in for the principal material, principal energy source, dominant "
     "transport service, main waste treatment or an expected hotspot. It omits a burden from "
     "Alternative A only, so it works against the alternative we expect to rank better and cannot "
     "create that result. The item that *could* be a hotspot, the battery pack, is handled as a "
     "declared scope exclusion with a bounding scenario, never as a placeholder.",
     size=8.5, color=GREY, space_after=4)

# ================================================================== 9. DATABASES
heading("9  Databases and cross-database compatibility", 1)
para("**Primary background database:** ELCD 3.2 (European reference Life Cycle Database, European "
     "Commission JRC) in the GreenDelta conversion for openLCA, as provided by the instructor [1]; "
     "a backup will be taken before any import or method update. Every dataset the baseline needs "
     "is in ELCD. Its energy and transport datasets are aggregated cradle-to-gate LCI results, so "
     "contribution analysis can resolve our own processes, each linked dataset and each substance, "
     "but cannot look inside a dataset, for example to separate coal from gas within the "
     "electricity mix.")
para("Inspection showed three compatibility issues **inside ELCD itself**, which matter more here "
     "than any cross-database risk:")
bullet("**Two data generations.** ELCD carries an older set (*Electricity Mix*, 2002–2010; "
       "*Diesel, consumption mix*, 2003–2012) and a newer set (*Electricity grid mix* and *Diesel "
       "mix at refinery*, 2008–2015). The older EU-27 electricity mix is about 20 % more "
       "carbon-intensive (0.59 against 0.49 kg CO₂-eq/kWh‡). Mixing generations between the "
       "alternatives would bias the comparison, so the baseline uses the newer set on both sides.",
       size=9)
bullet("**Flow identity.** The generations use different product flows (`diesel` and `Diesel`; "
       "`electricity mix` and `Electricity`). ELCD's own lorry unit processes consume the older "
       "`diesel`. Every provider link will be set explicitly and checked for unlinked or wrongly "
       "linked inputs.", size=9)
bullet("**Biogenic carbon.** The diesel mix records an uptake of 0.129 kg CO₂ per kg for its "
       "bio-blend‡. CML-IA baseline and EF 3.0 give biogenic CO₂ and its uptake no weight; ILCD "
       "2011 Midpoint+ credits the uptake, scoring the same dataset at 0.34 instead of 0.47 kg "
       "CO₂-eq‡. Under a method of the second kind, a tailpipe that omitted the biogenic CO₂ "
       "would understate Alternative A.", size=9)
para("**Secondary database:** none in the baseline. A second source would be needed only for S4, "
     "for a lithium-ion battery pack and electric drive. Candidates will be screened and agreed "
     "with the instructor before any import†. Compatibility risks to be resolved and re-checked in "
     "Deliverable 2:")
bullet("**Flow identity** — another database's elementary flows may not map to ELCD's, and "
       "unmapped flows drop out of the LCIA silently.", size=9)
bullet("**System model and allocation** — battery datasets may follow allocation rules that "
       "differ from ELCD's aggregated results.", size=9)
bullet("**Geography and time** — cell manufacture is concentrated outside Europe and depends on "
       "the electricity used there.", size=9)
bullet("**LCIA coverage** — the method must characterise the imported flows; the coverage check "
       "run on ELCD will be repeated.", size=9)
bullet("**Licensing** — any database will be used only within permitted submission channels; "
       "nothing licensed is redistributed.", size=9)
para("**Mitigation:** any secondary dataset will be imported into a *copy* of the working database "
     "and used only inside the clearly labelled scenario S4. The baseline model stays "
     "single-database. A successful import will not be treated as evidence of methodological "
     "compatibility.", space_after=4)

# ================================================================== 10. LCIA
heading("10  Tentative LCIA method, categories and planned sensitivity analyses", 1)
para("**Method:** CML-IA baseline, as bundled in the course database [11]. Characterisation only; "
     "no normalisation or weighting, which would not be defensible at screening level. Results will "
     "be reported as **absolute values with units** per pitch-year and per cut before any relative "
     "chart is drawn, and magnitudes will never be compared across categories.")
build_table(
    ["Impact category (CML-IA baseline)", "Unit", "Why this category is decision-relevant here"],
    [["**Global warming (GWP100a)**", "kg CO₂-eq",
      "The climate-change half of the approved question. Registers tailpipe CO₂, CH₄ and N₂O on one "
      "side and power-station emissions on the other (CH₄ 28, N₂O 265)"],
     ["**Abiotic depletion (fossil fuels)**", "MJ",
      "The fossil-resource half. Counts crude oil, natural gas, hard coal and lignite by energy "
      "content, and nothing else"]],
    widths=[2500, 1100, 6264], font=8.0, keep_together=True)
para("These are exactly the two categories named in the approved question, and no others are "
     "added. **Why CML-IA baseline rather than EF 3.0.** A coverage check on the three principal "
     "datasets showed that both methods characterise them and agree closely (diesel 0.47 and 0.51 "
     "kg CO₂-eq per kg; electricity 0.49 and 0.50 kg CO₂-eq per kWh; fossil resource within "
     "0.3 %)‡. "
     "Two findings decided the choice. First, EF 3.0's *Resource use, fossils* is defined to "
     "include uranium, but in this database its uranium factors sit on flows that ELCD does not "
     "use, so the 2.96 MJ of uranium per kWh of EU-27 electricity would be dropped without warning. "
     "The CML category is fossil-only by definition, which is what the question asks. Second, "
     "EF 3.0 gives carbon monoxide a climate factor of 1.57 kg CO₂-eq/kg. Combined with a tailpipe "
     "CO₂ factor that already assumes all fuel carbon is oxidised, that counts carbon twice: a "
     "small error for diesel, a large one for petrol (770 g CO per kg of fuel [2]). EF 3.0 is kept "
     "as a robustness check in S5.", size=8.5, color=GREY, space_after=6)

heading("Planned sensitivity and bounding analyses", 2)
build_table(
    ["", "Analysis", "Range tested", "Purpose"],
    [["**S1**", "Electricity mix *(committed)*",
      "EU-27 (0.49) · SE (0.06) · FR (0.11) · DE (0.63) · PL (1.11) · EE (1.33 kg CO₂-eq/kWh‡), "
      "all from the 2008–2015 ELCD set",
      "Tests H4; reports the break-even grid intensity, the study's first main output"],
     ["**S2**", "Energy per cut *(committed)*",
      "Engine load factor 0.4 / 0.5 / 0.6 · time per cut 0.75 / 0.85 / 1.0 h · socket-to-work "
      "efficiency 0.65 / 0.75 / 0.85",
      "Tests H1, H2 and H5; reports the break-even efficiency, the second main output"],
     ["**S3**", "Fuel within Alternative A",
      "Petrol four-stroke: *Gasoline mix (regular) at refinery …* {EU-27} with EMEP/EEA Tier 1 "
      "factors (CO₂ 3 197 kg, CH₄ 665 g, N₂O 59 g per tonne)",
      "Tests whether the conclusion holds for the petrol variant named in the approved scope"],
     ["**S4**", "Capital goods *(conditional)*",
      "Powertrain and battery manufacture for both alternatives, allocated by machine-hours: "
      "dedicated to one pitch (≈ 25 h/yr†) against shared fleet use (≈ 500 h/yr†)",
      "Tests the direction and size of the bias from the approved exclusion"],
     ["**S5**", "Method and data generation",
      "EF 3.0 (adapted) in place of CML-IA baseline · the 2002–2012 ELCD set on both sides · "
      "fossil-only diesel · biogenic share of tailpipe CO₂",
      "Tests that the ranking is not produced by a method or dataset choice"]],
    widths=[560, 2400, 3500, 3404], font=7.8)
para("**S1 and S2 are committed**; S3–S5 will be run if time permits. The requirement is one "
     "justified sensitivity or bounding analysis, and S1 alone satisfies it by varying the "
     "parameter that determines the answer. Petrol is a variant inside Alternative A, not a third "
     "alternative. S4 will be run inside the model only if the data rule in §6 is met; otherwise it "
     "is reported as a literature bound outside the model and labelled as such.",
     size=8.5, color=GREY, space_after=4)

# ================================================================== 11. FALLBACK
heading("11  Fallback plan if essential data cannot be obtained", 1)
build_table(
    ["", "Trigger", "Fallback action", "Effect on the research question"],
    [["**F1**", "Fuel and electricity per cut cannot be obtained from the manufacturer or from an "
                "operator's records",
      "Keep the engineering estimate (rated power × load factor × specific consumption; equal work "
      "÷ efficiency) and widen S2",
      "Absolute values become less certain. The ratio B/A depends only on the efficiency and on "
      "verified per-unit values, so the comparison stays answerable"],
     ["**F2**", "The combustion process cannot be built at Tier 3 for a Stage V engine of this "
                "class",
      "Use the Tier 1 factors of EMEP/EEA Table 3-1, already retrieved",
      "Non-greenhouse pollutants become fleet averages. The climate result is unchanged, because "
      "CO₂ is fuel-based and dominates"],
     ["**F3**", "No battery or powertrain dataset can be imported and allocated reliably",
      "Capital goods stay excluded, as the approved scope allows; S4 becomes a literature bound "
      "outside the model",
      "The conclusion is limited to the operation of the two mowers and is stated in those words"],
     ["**F4**", "The bundled CML-IA baseline factors fail the coverage check when reproduced in "
                "openLCA",
      "Switch to EF 3.0 (adapted): *Climate change* and *Resource use, fossils*, with the uranium "
      "and carbon-monoxide caveats of §10 stated",
      "Category names change; the fossil-only meaning of the resource result must be explained"]],
    widths=[560, 2500, 3400, 3404], font=7.8)
para("Consistent with the guidance that a narrower complete model is stronger than a broad model "
     "dominated by undocumented gaps, we would rather report a complete operation-only comparison "
     "than carry an unsupported battery inventory into Deliverable 2.",
     size=8.5, color=GREY, space_after=4)

# ================================================================== 12. COMPLIANCE
heading("12  Check against the minimum project design and the approved scope", 1)
build_table(
    ["Requirement", "How this proposal meets it"],
    [["Approved topic and research question",
      "Football-pitch mowing systems; the research question is reproduced verbatim in §3"],
     ["Approved scope",
      "Same pitch area, mowing frequency and cutting service for both; diesel consumption and "
      "direct emissions for A, electricity consumption for B; construction, artificial turf, "
      "irrigation, fertilisation and other maintenance excluded; mower and battery manufacture "
      "conditional — §5, §6"],
     ["Two functionally comparable alternatives",
      "A (diesel ride-on) and B (battery-electric ride-on) on a shared chassis and deck. Petrol is "
      "a sensitivity inside A. No third alternative."],
     ["One quantified FU and a reference flow per alternative",
      "One pitch-year: 30 cuts of 7 140 m². Reference flows ≈ 63 kg of diesel (A) and ≈ 313 kWh at "
      "the socket (B) — §5"],
     ["≈ 4–8 foreground processes per alternative",
      "Four each: A1–A4 and B1–B4. This is the lower end, because the approved scope is narrow; "
      "each process isolates one parameter. A fifth is added on each side if S4 is run — Figure 1"],
     ["One designated primary background database",
      "ELCD 3.2, instructor-provided. No secondary database in the baseline — §9"],
     ["≥ 1 process created or substantively adapted by the group",
      "One constructed (A2, combustion in the mower engine) and one adapted (B2, battery "
      "charging) — §8"],
     ["≤ 2 unresolved zero-burden placeholders",
      "One: engine lubricating oil, minor and bounded. The battery pack is a scope exclusion, never "
      "a placeholder — §8"],
     ["≥ 2 decision-relevant impact categories",
      "The two named in the approved question: global warming and fossil-fuel depletion — §10"],
     ["≥ 1 justified sensitivity or bounding analysis",
      "Five planned; S1 and S2 committed — §10"],
     ["Common boundary, LCIA method and conventions across alternatives",
      "One boundary, one method, EU-27, one ELCD data generation on both sides; capital goods in "
      "for both or out for both — §6"]],
    widths=[3300, 6564], font=8.0)

# ================================================================== 13. REFS
heading("13  Key references", 1)
para("Sources marked † must be retrieved and verified against the original publication, standard or "
     "database documentation before Deliverable 2; the others were consulted directly in preparing "
     "this proposal. Data will be cited at the level actually used: database and version plus "
     "dataset name; report table and page; article DOI.", size=8.5, color=GREY, space_after=5)

refs = [
    "European Commission, Joint Research Centre — ELCD 3.2, European reference Life Cycle Database, "
    "in the GreenDelta conversion for openLCA (file "
    "`elcd_3_2_greendelta_v2_18_correction_20220908.zolca`, instructor-provided). The primary "
    "background database; source of every dataset named in §8.",

    "Winther, M. and Dore, C. (lead authors) — EMEP/EEA air pollutant emission inventory guidebook "
    "2023, Part B, chapter 1.A.4 Non-road mobile machinery. European Environment Agency. Table 3-1 "
    "(Tier 1 emission factors) and Table 3-6 (Tier 3 baseline emission factors and fuel consumption "
    "for diesel engines). Source of the direct emission factors and the 270 g/kWh fuel consumption.",

    "IPCC (2006) — Guidelines for National Greenhouse Gas Inventories, Volume 2 Energy, Chapter 3 "
    "Mobile Combustion† — default off-road CO₂, CH₄ and N₂O factors, as a cross-check on [2].",

    "Generic Football Pitch Maintenance Programme, Appendix A to the Preliminary Feasibility Study "
    "for the Former Friends School Field Site (24 April 2025), published on GOV.UK — mowing "
    "frequency and height of cut. Its own source, Sport England (2011) *Natural Turf for Sport: "
    "Design Guidance Note*†, will be retrieved and cited directly.",

    "The Toro Company — product specifications for the Groundsmaster e3200 (battery) and "
    "Groundsmaster 3200 (diesel, model 31900A: Yanmar 18.4 kW, Stage V, hydraulic traction), and "
    "Reitman, J. (3 February 2023), “Toro introduces e3200 Groundsmaster rotary mower”, TurfNet — "
    "battery count, charger power, deck width, shared platform. Neither machine's energy use per "
    "hour is published; it remains to be obtained†.",

    "Saidani, M. and Kim, H. (2021) — Quantification of the environmental and economic benefits of "
    "the electrification of lawn mowers on the US residential market. *International Journal of "
    "Life Cycle Assessment* 26(6), 1267–1284. Used **only as a plausibility benchmark**.",

    "Sivaraman, D. and Lindner, A. S. (2004) — A comparative life cycle analysis of gasoline-, "
    "battery-, and electricity-powered lawn mowers. *Environmental Engineering Science*† — "
    "plausibility benchmark only.",

    "Regulation (EU) 2016/1628 of the European Parliament and of the Council on emission limits and "
    "type-approval for internal combustion engines for non-road mobile machinery (Stage V).",

    "Emilsson, E. and Dahllöf, L. (2019) — Lithium-Ion Vehicle Battery Production: Status 2019 on "
    "Energy Use, CO₂ Emissions, Use of Metals, Products Environmental Footprint, and Recycling. "
    "IVL Swedish Environmental Research Institute, report C 444 — 61–106 kg CO₂-eq per kWh of "
    "capacity, taken from published summaries; the report itself is still to be read†.",

    "European Environment Agency (25 October 2024) — indicator *Greenhouse gas emission intensity "
    "of electricity generation in Europe*, data for 1990–2023 — the fall in EU grid intensity "
    "since the ELCD reference years; the present-day value will be read from the indicator data†.",

    "CML-IA characterisation factors (Institute of Environmental Sciences, Leiden University) and "
    "Environmental Footprint 3.0 (European Commission, JRC), as implemented in the LCIA methods "
    "bundled with the course database.",

    "ISO 14040:2006 and ISO 14044:2006 — principles, framework and requirements. Used as the "
    "methodological frame; no conformant comparative assertion is claimed.",
]
for i, ref in enumerate(refs, 1):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.75)
    p.paragraph_format.first_line_indent = Cm(-0.75)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.02
    rich(p, f"[{i}]  {ref}", size=8.5)

rule(space_before=8, space_after=6)

heading("Declaration of AI assistance", 2)
para("An AI assistant was used to help structure and draft this proposal, to run a read-only "
     "script on a copy of the course ELCD database (listing dataset names and metadata, and "
     "multiplying inventory exchanges by the bundled characterisation factors to obtain the "
     "screening values marked ‡), and to retrieve the EMEP/EEA tables and the other sources not "
     "marked †. No value produced this way is treated as a result. Before anything enters the "
     "model in Deliverable 2, the group will reproduce every screening value in openLCA, re-read "
     "every cited table, and verify every item marked † against the original. Where a value rests "
     "on a standard, report or database record, that original source is what will be cited.",
     size=8.5, color=GREY)
para("**File naming convention in use:** `Group_Project_Deliverable1_v2_2026-10-12.docx`",
     size=8.5, color=GREY, space_after=2)

doc.core_properties.title = "Group Project Deliverable 1 — Project Proposal (v2): football-pitch mowing systems"
doc.core_properties.author = ""

out = "Group_Project_Deliverable1_v2_2026-10-12.docx"
doc.save(out)
print("written:", out)
