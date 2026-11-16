"""System-boundary diagram for Deliverable 1, revised topic (comparative screening
LCA: diesel vs battery-electric mowing of one football pitch for one maintenance year)."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

# ---------------------------------------------------------------- palette
FORE = dict(fc="#E7EEF5", ec="#3E6183")      # foreground process linked to ELCD / activity data
STUD = dict(fc="#FBEFD6", ec="#B4801F")      # constructed by the group
PROX = dict(fc="#EDE6F6", ec="#6A4FA3")      # adapted by the group
KEY = dict(fc="#DEF0F1", ec="#2C7A7B")       # annual service (reference process)
FUNC = dict(fc="#E4F1E8", ec="#2E7D4F")      # functional unit
COND = dict(fc="#FFFFFF", ec="#8A8A8A")      # conditional, scenario S4 only
EXCL = dict(fc="#F2F2F2", ec="#B8B8B8")      # outside the boundary
TXT = "#1F2933"
GREY = "#7A7A7A"
LINE = "#3E6183"

fig, ax = plt.subplots(figsize=(7.8, 7.2))
ax.set_xlim(0, 1)
ax.set_ylim(-0.035, 1.0)
ax.axis("off")


def box(x0, x1, y0, y1, text, style, size=6.8, weight="normal", color=TXT, ls="-"):
    ax.add_patch(FancyBboxPatch(
        (x0, y0), x1 - x0, y1 - y0,
        boxstyle="round,pad=0.004,rounding_size=0.008",
        linewidth=0.9, linestyle=ls, **style, zorder=2))
    ax.text((x0 + x1) / 2, (y0 + y1) / 2, text, ha="center", va="center",
            fontsize=size, color=color, weight=weight, zorder=3, linespacing=1.35)


def arrow(x0, y0, x1, y1, color=LINE, lw=1.1, style="-|>"):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), zorder=1,
                arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                                shrinkA=0, shrinkB=0))


AC, BC = 0.365, 0.810                       # column centres
AL, AR = AC - 0.165, AC + 0.165
BL, BR = BC - 0.165, BC + 0.165

# ------------------------------------------------- the boundary
ax.add_patch(Rectangle((0.185, 0.245), 0.805, 0.725, fill=False,
                       ec="#2F4858", lw=1.4, ls=(0, (5, 3)), zorder=1))
ax.text(0.193, 0.957, "SYSTEM BOUNDARY  —  energy carrier from resource to mower, one pitch-year",
        fontsize=6.6, style="italic", color="#2F4858", ha="left", va="center")
ax.text(0.982, 0.957, "EU-27  ·  ELCD 2008–2015",
        fontsize=6.6, style="italic", color="#2F4858", ha="right", va="center")

# ------------------------------------------------- column headers
ax.text(AC, 0.925, "ALTERNATIVE A", fontsize=7.4, weight="bold",
        ha="center", va="center", color="#2F4858")
ax.text(AC, 0.903, "Diesel ride-on rotary mower", fontsize=6.8, ha="center",
        va="center", color=TXT)
ax.text(BC, 0.925, "ALTERNATIVE B", fontsize=7.4, weight="bold",
        ha="center", va="center", color="#2F4858")
ax.text(BC, 0.903, "Battery-electric ride-on rotary mower", fontsize=6.8, ha="center",
        va="center", color=TXT)

TOPS = [0.875, 0.757, 0.639, 0.521]
H = 0.082

a_steps = [
    ("A1  Diesel supply and delivery\nELCD diesel mix at refinery {EU-27}\n+ lorry delivery to the club", FORE),
    ("A2  Combustion in the mower engine\ndirect emissions per kg of diesel burned\n(EMEP/EEA 2023 emission factors)", STUD),
    ("A3  One cut of the pitch, diesel mower\n0.85 h × 9.2 kW × 270 g/kWh\n≈ 2.1 kg (2.5 L) diesel", FORE),
    ("A4  Mowing service, one pitch-year\n× 30 cuts  ≈ 63 kg (76 L) diesel", KEY),
]
b_steps = [
    ("B1  Electricity supply at the socket\nELCD grid mix at consumer, < 1 kV {EU-27}\n(swap point for national mixes, S1)", FORE),
    ("B2  Battery charging\ncharger and battery losses\n(socket-to-work efficiency ≈ 75 %)", PROX),
    ("B3  One cut of the pitch, battery mower\nsame work as A3, no emissions at the pitch\n≈ 10.4 kWh at the socket", FORE),
    ("B4  Mowing service, one pitch-year\n× 30 cuts  ≈ 313 kWh at the socket", KEY),
]

for steps, L, R, C in ((a_steps, AL, AR, AC), (b_steps, BL, BR, BC)):
    for (label, style), top in zip(steps, TOPS):
        weight = "bold" if style is KEY else "normal"
        color = "#1F5F60" if style is KEY else TXT
        box(L, R, top - H, top, label, style, size=6.5, weight=weight, color=color)
    for i in range(len(TOPS) - 1):
        arrow(C, TOPS[i] - H, C, TOPS[i + 1])

# ------------------------------------------------- converge on the FU
Y4 = TOPS[-1] - H
arrow(AC, Y4, AC, 0.405, style="-")
arrow(BC, Y4, BC, 0.405, style="-")
arrow(AC, 0.405, BC, 0.405, style="-")
arrow(0.5875, 0.405, 0.5875, 0.375)

box(0.335, 0.840, 0.268, 0.375,
    "FUNCTIONAL UNIT\nMowing one existing full-size natural-grass football pitch\n"
    "(105 × 68 m, 7 140 m²) for one maintenance year:\n"
    "30 cuts at 30–40 mm, same 1.52 m rotary deck, clippings returned",
    FUNC, size=6.9, weight="bold", color="#1E5B39")

# ------------------------------------------------- background flows
box(0.005, 0.168, 0.600, 0.925,
    "BACKGROUND\nINPUTS\n(ELCD 3.2)\n\n• Crude oil and\n  refining\n• Lorry transport,\n  22 t\n• Fuels for power\n  generation\n• Transmission and\n  distribution\n  to < 1 kV",
    dict(fc="#FAFAFA", ec="#C6CDD4"), size=6.0)

box(0.005, 0.168, 0.268, 0.570,
    "OUTPUTS\n\n• A: exhaust at the\n  pitch — CO$_2$, CH$_4$,\n  N$_2$O, NO$_x$, CO,\n  NMVOC, PM\n• B: emissions at\n  power stations\n  (inside B1)\n• Engine oil (A)\n  → DATA GAP 1",
    dict(fc="#FDF0EE", ec="#D8A9A0"), size=6.0)

# ------------------------------------------------- conditional (S4)
box(0.185, 0.990, 0.150, 0.228,
    "CONDITIONAL — scenario S4 only, in for both alternatives or out for both\n"
    "diesel engine and hydraulic drive (A)  ·  battery pack, electric motors and charger (B)\n"
    "The pair shares chassis and deck, so only the powertrains differ. ELCD holds no lithium-ion cell dataset: the baseline excludes capital goods.",
    COND, size=6.0, color="#4A4A4A", ls=(0, (4, 2)))

# ------------------------------------------------- excluded
box(0.185, 0.990, 0.066, 0.138,
    "EXCLUDED (outside the mowing decision, identical for both alternatives): pitch construction  ·  artificial turf  ·  irrigation  ·  fertilisation\n"
    "aeration, topdressing, overseeding and line marking  ·  operator labour and travel  ·  machinery shed and charging point\n"
    "clippings (returned to the turf in both alternatives)",
    EXCL, size=6.0, color=GREY)

# ------------------------------------------------- legend + footnote
legend = [
    (FORE, "Foreground process", "-", 0.188),
    (STUD, "Constructed by the group", "-", 0.352),
    (PROX, "Adapted by the group", "-", 0.546),
    (KEY, "Reference process", "-", 0.716),
    (COND, "Conditional (S4)", (0, (4, 2)), 0.864),
]
for style, label, ls, lx in legend:
    ax.add_patch(FancyBboxPatch((lx, 0.030), 0.018, 0.013,
                                boxstyle="round,pad=0.002,rounding_size=0.004",
                                linewidth=0.8, linestyle=ls, **style))
    ax.text(lx + 0.024, 0.0365, label, fontsize=6.0, va="center", color=TXT)

ax.text(0.588, 0.004,
        "Cuts per year multiply both alternatives equally. The ranking is set by the energy each machine needs for the same cut "
        "and by the electricity mix (S1, S2).",
        fontsize=5.9, style="italic", ha="center", va="center", color=GREY)

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.savefig("system_boundary.png", dpi=240, facecolor="white",
            bbox_inches="tight", pad_inches=0.05)
print("written: system_boundary.png")
