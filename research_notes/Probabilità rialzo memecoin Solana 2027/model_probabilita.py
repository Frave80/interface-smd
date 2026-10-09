#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
model_probabilita.py
====================
Transparent, reproducible 12-month probability model (8 Oct 2026 -> 8 Oct 2027)
for the upside of six memecoins conditional on a Solana (or, for WOJAK, an
Ethereum/altcoin) rally.

Tokens: CHILLGUY, CHILLHOUSE, TROLL, TRIPLE T (TripleT/TRIPLET), CUPSEY (Solana)
        WOJAK (Ethereum original, wojakcto.com contract 0x8De3...)

Everything is computed from the research notes in this folder and the sibling
folders (see probability_model.md for the full documentation and the mapping of
every number to a note). No web access is used.

Run:  python3 -I model_probabilita.py   (from this folder)
Outputs: risultati_probabilita.md, risultati_probabilita.csv, output_modello.txt

Dependencies: numpy only (pandas is not required).
"""
import csv
import math
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_MD = os.path.join(HERE, "risultati_probabilita.md")
OUT_CSV = os.path.join(HERE, "risultati_probabilita.csv")
OUT_TXT = os.path.join(HERE, "output_modello.txt")

SEED = 20261009
N_PATHS = 100_000

# ----------------------------------------------------------------------------
# 0. Helpers
# ----------------------------------------------------------------------------
def N(x):
    """Standard normal CDF (scalar or array)."""
    x = np.asarray(x, dtype=float)
    return 0.5 * np.vectorize(math.erfc)(-x / math.sqrt(2.0))


def p_above(S0, K, mu, sigma, T):
    """Lognormal: P(S_T > K) with price drift mu (expected log return mu - sigma^2/2)."""
    d2 = (math.log(S0 / K) + (mu - 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    return float(N(d2))


def bucket_probs_lognormal(S0, edges, mu, sigma, T):
    """Probabilities of the price buckets defined by `edges` (ascending)."""
    cdf_above = [p_above(S0, k, mu, sigma, T) for k in edges]
    probs = []
    prev = 1.0
    for a in cdf_above:
        probs.append(prev - a)
        prev = a
    probs.append(prev)
    return np.array(probs)


def odds_mult(p, m):
    """Multiply the odds p/(1-p) by m and return the new probability."""
    p = min(max(p, 1e-9), 1 - 1e-9)
    o = p / (1 - p) * m
    return o / (1 + o)


class Tee:
    """Write to stdout and to a file at the same time."""
    def __init__(self, path):
        self.f = open(path, "w", encoding="utf-8")
        self.out = sys.stdout
    def write(self, s):
        self.out.write(s)
        self.f.write(s)
    def flush(self):
        self.out.flush()
        self.f.flush()

sys.stdout = Tee(OUT_TXT)

md_lines = []   # collected markdown for risultati_probabilita.md
csv_rows = []   # collected rows for risultati_probabilita.csv

def emit(s=""):
    print(s)
    md_lines.append(s)

def md_table(header, rows, fmt=None):
    emit("| " + " | ".join(header) + " |")
    emit("|" + "|".join(["---"] * len(header)) + "|")
    for r in rows:
        emit("| " + " | ".join(str(x) for x in r) + " |")
    emit()

def pct(x, d=1):
    return f"{100*x:.{d}f}%"

# ----------------------------------------------------------------------------
# 1. SOL 12-month scenario distribution
# ----------------------------------------------------------------------------
SOL_SPOT = 110.0          # sol_probability_inputs.md Q1: ~$109-110 on 8-9 Oct 2026
SOL_ATH = 294.85          # sol_probability_inputs.md Q1 (Coinbase, 19 Jan 2025)
T = 1.0                   # years
SIGMA_SOL = 0.55          # sol_probability_inputs.md Q2: 55% flat vol used in the notes (RV 57%, IV 53%)
SIGMA_SOL_STRESS = 0.70   # stress vol used in the notes

# Fine price buckets (so that the +50% = $165 and +100% = $220 thresholds are exact)
FINE_EDGES = [70, 110, 150, 165, 220, 250]
FINE_NAMES = ["<70", "70-110", "110-150", "150-165", "165-220", "220-250", ">250"]
# Mapping fine buckets -> 5 display scenarios
SCEN_OF_FINE = ["A", "B", "C", "D", "D", "D", "E"]
SCEN_NAMES = {
    "A": "Crollo (<$70, peggio di -36%)",
    "B": "Ribasso ($70-110, da -36% a 0%)",
    "C": "Laterale/moderato ($110-150, da 0 a +36%)",
    "D": "Rialzo forte ($150-250, da +36% a +127%)",
    "E": "Euforia (>$250, oltre +127%)",
}
SCEN_ORDER = ["A", "B", "C", "D", "E"]

def to5(fine):
    out = {k: 0.0 for k in SCEN_ORDER}
    for p, s in zip(fine, SCEN_OF_FINE):
        out[s] += p
    return out

# (a) lognormal / IV-based (notes: zero price drift, 55% vol)
comp_a = bucket_probs_lognormal(SOL_SPOT, FINE_EDGES, mu=0.0, sigma=SIGMA_SOL, T=T)
comp_a_stress = bucket_probs_lognormal(SOL_SPOT, FINE_EDGES, mu=0.0, sigma=SIGMA_SOL_STRESS, T=T)

# (b) prediction markets: Kalshi year-end-2026 close ladder captured late Sep 2026
#     (SOL ~ $121): P(>=100)=71%, P(>=150)=34%, P(>=200)=27%  [sol_probability_inputs.md Q3]
#     We fit a lognormal (drift mu_b, vol sigma_b) to these three points over
#     T_k ~ 0.26 y (late Sep -> 1 Jan 2027), then project the SAME (mu_b, sigma_b)
#     over 12 months from $110. This is the only way to turn a 3-month ladder into
#     a 12-month view; it inherits the ladder's long-shot bias (see notes).
KALSHI = [(100, 0.71), (150, 0.34), (200, 0.27)]
KALSHI_S0, KALSHI_T = 121.0, 0.26

def fit_kalshi():
    best = None
    for mu in np.arange(-1.0, 2.01, 0.02):
        for sg in np.arange(0.20, 2.01, 0.02):
            sse = sum((p_above(KALSHI_S0, k, mu, sg, KALSHI_T) - p) ** 2 for k, p in KALSHI)
            if best is None or sse < best[0]:
                best = (sse, mu, sg)
    return best

sse_b, mu_b, sigma_b = fit_kalshi()

def bucket_probs_two_stage(S0, edges, mu1, s1, T1, mu2, s2, T2):
    """Two-stage lognormal: (mu1, s1) for the first T1 years (prediction-market
    regime), then (mu2, s2) for the remaining T2 years (implied-vol regime).
    The sum of two independent normal log-returns is normal, so this is a
    lognormal with combined mean and variance."""
    m = (mu1 - 0.5 * s1 ** 2) * T1 + (mu2 - 0.5 * s2 ** 2) * T2
    v = s1 ** 2 * T1 + s2 ** 2 * T2
    above = [float(N((math.log(S0 / k) + m) / math.sqrt(v))) for k in edges]
    probs, prev = [], 1.0
    for a in above:
        probs.append(prev - a)
        prev = a
    probs.append(prev)
    return np.array(probs), m, v

# Prediction markets only cover ~the next quarter (no 2027 SOL markets exist, notes Q3),
# so (mu_b, sigma_b) are applied for KALSHI_T years and the IV lognormal (a) for the rest.
comp_b, LOG_MEAN_B, LOG_VAR_B = bucket_probs_two_stage(
    SOL_SPOT, FINE_EDGES, mu_b, sigma_b, KALSHI_T, 0.0, SIGMA_SOL, T - KALSHI_T)
SIGMA_B_EFF = math.sqrt(LOG_VAR_B)   # effective 12-month vol of component (b)

# (c) historical 12-month base rates (sol_probability_inputs.md Q4, MY CALC on an
#     approximate monthly series, 57 rolling windows): P(>0)=49%, P(>+50%)=33%,
#     P(>+100%)=31% (32% full sample), P(>+200%)=28%, P(<-50%)=25%.
#     We linearly interpolate the survival function F(r)=P(return>r) between these points.
HIST_POINTS = [(-1.0, 1.00), (-0.5, 0.75), (0.0, 0.49), (0.5, 0.33), (1.0, 0.31), (2.0, 0.28)]

def F_hist(r):
    xs = [p[0] for p in HIST_POINTS]
    ys = [p[1] for p in HIST_POINTS]
    if r <= xs[0]:
        return 1.0
    if r >= xs[-1]:
        return ys[-1]
    return float(np.interp(r, xs, ys))

def bucket_probs_hist(S0, edges):
    above = [F_hist(k / S0 - 1.0) for k in edges]
    probs, prev = [], 1.0
    for a in above:
        probs.append(prev - a)
        prev = a
    probs.append(prev)
    return np.array(probs)

comp_c = bucket_probs_hist(SOL_SPOT, FINE_EDGES)

# (d) macro tilt: Fed hiking (16 Sep 2026, more hikes priced, no 2027 cuts in dots),
#     CLARITY Act cloture failed 15 Sep 2026, BTC ETF -$487M on 7 Oct, SOL ETF outflows
#     5-7 Oct, Solana network revenue -87% y/y, DAT companies at 0.3-0.5x mNAV
#     [sol_probability_inputs.md Q6]. Encoded as a NEGATIVE price drift on the
#     55%-vol lognormal. Base -15%/yr; sensitivity -25% (pessimistic) and 0% (optimistic).
MU_MACRO_BASE, MU_MACRO_PESS, MU_MACRO_OPT = -0.15, -0.25, 0.0
comp_d = bucket_probs_lognormal(SOL_SPOT, FINE_EDGES, mu=MU_MACRO_BASE, sigma=SIGMA_SOL, T=T)
comp_d_pess = bucket_probs_lognormal(SOL_SPOT, FINE_EDGES, mu=MU_MACRO_PESS, sigma=0.60, T=T)
comp_d_opt = bucket_probs_lognormal(SOL_SPOT, FINE_EDGES, mu=MU_MACRO_OPT, sigma=SIGMA_SOL, T=T)

BLENDS = {
    # name: (w_a, w_b, w_c, w_d, component_d)
    "Ottimistico":  (0.30, 0.30, 0.30, 0.10, comp_d_opt),
    "Base":         (0.35, 0.20, 0.20, 0.25, comp_d),
    "Pessimistico": (0.30, 0.10, 0.10, 0.50, comp_d_pess),
}

def blend(name):
    wa, wb, wc, wd, cd = BLENDS[name]
    return wa * comp_a + wb * comp_b + wc * comp_c + wd * cd

sol_fine = {k: blend(k) for k in BLENDS}
sol5 = {k: to5(v) for k, v in sol_fine.items()}

# Touch probabilities from the notes (driftless reflection: 2 x terminal prob at 55% vol)
TOUCH_NOTES = {150: 2 * p_above(SOL_SPOT, 150, 0, SIGMA_SOL, T),
               200: 2 * p_above(SOL_SPOT, 200, 0, SIGMA_SOL, T),
               250: 2 * p_above(SOL_SPOT, 250, 0, SIGMA_SOL, T),
               300: 2 * p_above(SOL_SPOT, 300, 0, SIGMA_SOL, T)}

# ---- ETH (for WOJAK) ----------------------------------------------------------
ETH_SPOT = 2600.0     # wojak_ethereum.md: ETH $2,694 on 29 Sep, $2,547 on 7 Oct 2026
ETH_ATH = 4950.0      # wojak_ethereum.md: ATH near $4,950 (Aug 2025)
SIGMA_ETH = 0.50      # ASSUMPTION: no ETH vol in the notes; set slightly below SOL's 55%
ETH_EDGES = [round(ETH_SPOT * k / SOL_SPOT) for k in FINE_EDGES]   # same RETURN buckets
comp_a_eth = bucket_probs_lognormal(ETH_SPOT, ETH_EDGES, 0.0, SIGMA_ETH, T)
comp_d_eth = bucket_probs_lognormal(ETH_SPOT, ETH_EDGES, MU_MACRO_BASE, SIGMA_ETH, T)
comp_d_eth_p = bucket_probs_lognormal(ETH_SPOT, ETH_EDGES, MU_MACRO_PESS, 0.55, T)
comp_d_eth_o = bucket_probs_lognormal(ETH_SPOT, ETH_EDGES, MU_MACRO_OPT, SIGMA_ETH, T)
# (b) and (c) are SOL-specific; reused for ETH as an "altcoin proxy" (stated caveat)
eth_fine = {
    "Ottimistico": 0.30 * comp_a_eth + 0.30 * comp_b + 0.30 * comp_c + 0.10 * comp_d_eth_o,
    "Base":        0.35 * comp_a_eth + 0.20 * comp_b + 0.20 * comp_c + 0.25 * comp_d_eth,
    "Pessimistico": 0.30 * comp_a_eth + 0.10 * comp_b + 0.10 * comp_c + 0.50 * comp_d_eth_p,
}
eth5 = {k: to5(v) for k, v in eth_fine.items()}

# ----------------------------------------------------------------------------
# 2. Conditional response of an ESTABLISHED memecoin (generic, pre-adjustment)
# ----------------------------------------------------------------------------
# Outcomes over 12 months (price multiple m = P_T / P_0):
#   up50: m >= 1.5 | x2: m >= 2 | x3: m >= 3 | x5: m >= 5 | x10: m >= 10
#   dn50: m <= 0.5 | dead: m <= 0.2 ("effectively dead", < -80%)
# Every number is an ESTIMATE anchored on memecoin_base_rates.md and
# solana_altcoin_outlook.md; the reasoning is in probability_model.md section 2.
OUTS = ["up50", "x2", "x3", "x5", "x10", "dn50", "dead"]
OUT_LABEL = {"up50": ">= +50%", "x2": ">= 2x", "x3": ">= 3x", "x5": ">= 5x",
             "x10": ">= 10x", "dn50": "<= -50%", "dead": "<= -80% (dead)"}
COND = {
    #      up50   x2     x3     x5     x10    dn50   dead
    "A": [0.03, 0.015, 0.008, 0.003, 0.001, 0.85, 0.55],
    "B": [0.08, 0.040, 0.022, 0.010, 0.003, 0.65, 0.35],
    "C": [0.18, 0.100, 0.055, 0.025, 0.008, 0.45, 0.20],
    "D": [0.40, 0.250, 0.150, 0.080, 0.030, 0.28, 0.12],
    "E": [0.65, 0.500, 0.350, 0.200, 0.080, 0.15, 0.06],
}
COND = {k: dict(zip(OUTS, v)) for k, v in COND.items()}

def uncond_from(scen_probs, cond):
    return {o: sum(scen_probs[s] * cond[s][o] for s in SCEN_ORDER) for o in OUTS}

generic_uncond = uncond_from(sol5["Base"], COND)

# ----------------------------------------------------------------------------
# 3. Per-token adjustments
# ----------------------------------------------------------------------------
# For each token: current price, ATH price (-> multiple needed for a new ATH),
# current market cap (USD), linkage lambda to the chain, and a dictionary of
# (upside odds multiplier, downside odds multiplier) per factor. The product of
# the factor multipliers is clipped to [0.5, 2.0]. Sources per token are listed
# in probability_model.md section 3.
TOKENS = {
    "CHILLGUY": dict(
        chain="SOL", price=0.0125, ath=0.665, cap_musd=13.0, lam=0.80,
        factors={
            "cycle_age (2024-cycle, ATH Nov 2024)":            (0.70, 1.15),
            "drawdown -98% (decay phase)":                      (0.85, 1.10),
            "holders 118K / liq $1.2M / vol $3-5M":             (1.10, 0.90),
            "CEX ladder: Binance perp 75x + 5 spot (delist risk)": (1.15, 1.10),
            "catalysts: none found 2026":                       (0.90, 1.00),
            "concentration: >20% bundled, top-10 52%":          (0.90, 1.10),
            "IP: Banks copyright claim (dormant)":              (0.90, 1.00),
        }),
    "CHILLHOUSE": dict(
        chain="SOL", price=0.0015, ath=0.02919, cap_musd=1.5, lam=0.50,
        factors={
            "cycle_age (2025 stunts, ATH Oct 2025)":            (0.70, 1.15),
            "drawdown -95% (decay phase)":                      (0.85, 1.10),
            "holders 19K / liq $0.4M / vol ~$20K DEX":          (0.80, 1.30),
            "CEX ladder: Kraken + MEXC (thin)":                 (1.00, 1.00),
            "catalysts: no team activity since Nov 2025":       (0.60, 1.20),
            "concentration: bundles flagged (unverified)":      (0.95, 1.10),
            "IP: Chill Guy image (Banks)":                      (0.90, 1.00),
        }),
    "TROLL": dict(
        chain="SOL", price=0.050, ath=0.282, cap_musd=50.0, lam=0.80,
        factors={
            "cycle_age (ATH Aug 2025 but own 2026 cycle, May 2026 peak)": (1.00, 1.00),
            "drawdown -82%":                                    (0.95, 1.05),
            "holders 65-70K rising / liq $1.7-3.9M":            (1.15, 0.90),
            "CEX ladder: Coinbase, Binance.US, KuCoin, MEXC perp, Alpha tag": (1.25, 0.90),
            "catalysts: airdrop Sep 2026, Binance global optionality, IP license": (1.20, 1.00),
            "concentration: 10 whales + Ramirez bag, opaque":   (0.95, 1.05),
            "IP: exclusive Trollface license":                  (1.10, 0.95),
        }),
    "TRIPLE T": dict(
        chain="SOL", price=0.0085, ath=0.027, cap_musd=8.0, lam=0.50,
        factors={
            "cycle_age (2026 launch, ATH Jul 2026)":            (1.10, 0.95),
            "drawdown -70%":                                    (1.00, 1.00),
            "holders 22-25K rising / liq $0.7M":                (1.00, 1.00),
            "CEX ladder: BitMart spot + MEXC perp only":        (0.90, 1.05),
            "catalysts: Ramadan 2027 (Feb), brainrot meta":     (1.15, 1.00),
            "concentration: top-10 16%, LP burned":             (1.05, 0.95),
            "IP: public-domain character":                      (1.00, 1.00),
        }),
    "CUPSEY": dict(
        chain="SOL", price=0.0065, ath=0.021, cap_musd=6.5, lam=0.50,
        factors={
            "cycle_age (relaunch Jan 2026, ATH Aug 2026)":      (1.10, 0.95),
            "drawdown -70% (blow-off, momentum negative)":      (1.00, 1.00),
            "holders 15K / liq $0.5M":                          (0.95, 1.05),
            "CEX ladder: Gate, MEXC, WEEX, Bitrue Alpha (2nd tier)": (0.90, 1.05),
            "catalysts: pump.fun mascot claim (unverified)":    (1.00, 1.00),
            "concentration: 16.8% project wallet + 8% KOL unlocked, migration": (0.85, 1.15),
            "IP/reputation: unowned, trader not involved, phishing scams": (0.95, 1.05),
        }),
    "WOJAK (ETH)": dict(
        chain="ETH", price=5.92e-8, ath=1.74e-7, cap_musd=18.4, lam=0.60,
        factors={
            "cycle_age (new contract 2026, ATH Jun 2026)":      (1.10, 0.95),
            "drawdown -65%":                                    (1.00, 1.00),
            "holders 12.3K / liq $0.4-0.9M / vol falling":      (0.90, 1.10),
            "CEX ladder: Kraken, HTX, Gate perp, MEXC, LBank":  (1.10, 0.95),
            "catalysts: MiCAR whitepaper, 27% burn, no CEX moment yet": (1.10, 1.00),
            "concentration: 68% dust wallets, low float, no top-10 table": (0.95, 1.05),
            "IP: unowned Wojak brand, clones, brand war won":   (0.95, 1.05),
        }),
}

for name, t in TOKENS.items():
    mu_up = float(np.prod([f[0] for f in t["factors"].values()]))
    mu_dn = float(np.prod([f[1] for f in t["factors"].values()]))
    t["M_up_raw"], t["M_dn_raw"] = mu_up, mu_dn
    t["M_up"] = float(np.clip(mu_up, 0.5, 2.0))
    t["M_dn"] = float(np.clip(mu_dn, 0.5, 2.0))
    t["k_ath"] = t["ath"] / t["price"]

def token_cond(t, scen5_base):
    """Scenario-conditional outcome probabilities for a token.
    1) linkage: lam * table[s] + (1-lam) * unconditional(table)
    2) odds multipliers on upside and downside outcomes
    3) consistency: P(>=+50%) + P(<=-50%) <= 1 (rescale downside if needed)."""
    unc = uncond_from(scen5_base, COND)
    out = {}
    for s in SCEN_ORDER:
        row = {}
        for o in OUTS:
            base = t["lam"] * COND[s][o] + (1 - t["lam"]) * unc[o]
            m = t["M_up"] if o in ("up50", "x2", "x3", "x5", "x10") else t["M_dn"]
            row[o] = odds_mult(base, m)
        if row["up50"] + row["dn50"] > 0.98:
            k = (0.98 - row["up50"]) / row["dn50"]
            row["dn50"] *= k
            row["dead"] = min(row["dead"], row["dn50"])
        out[s] = row
    return out

# ----------------------------------------------------------------------------
# 4a. Scenario-table computations: unconditional, conditional, EV, ATH
# ----------------------------------------------------------------------------
EV_CAP = 30.0   # cap on the mean of the >=10x tail (and on MC multiples) for EV

def tail_alpha(p5, p10):
    """Pareto tail exponent from P(>=5x) and P(>=10x): P(>=k) ~ k^-alpha."""
    p5, p10 = max(p5, 1e-9), max(p10, 1e-12)
    a = math.log(p5 / p10) / math.log(2.0)
    return max(a, 1.05)

def p_at_least(row, k):
    """P(m >= k) from the threshold probabilities, log-linear interpolation,
    Pareto extrapolation beyond 10x."""
    pts = [(1.0, 1.0 - row["dn50"] - (1.0 - row["dn50"] - row["up50"]) * 0.5),  # rough P(m>=1): midpoint of the 0.5-1.5 band
           (1.5, row["up50"]), (2.0, row["x2"]), (3.0, row["x3"]), (5.0, row["x5"]), (10.0, row["x10"])]
    if k <= 1.0:
        return pts[0][1]
    if k >= 10.0:
        a = tail_alpha(row["x5"], row["x10"])
        return row["x10"] * (k / 10.0) ** (-a)
    xs = [math.log(p[0]) for p in pts]
    ys = [math.log(max(p[1], 1e-12)) for p in pts]
    return math.exp(float(np.interp(math.log(k), xs, ys)))

def ev_multiple(row):
    """Expected multiple from the threshold probabilities (band midpoints,
    Pareto mean for the >=10x tail, capped at EV_CAP)."""
    p_dead = row["dead"]
    p_dn = row["dn50"] - row["dead"]
    p_mid = 1.0 - row["dn50"] - row["up50"]
    p15 = row["up50"] - row["x2"]
    p2 = row["x2"] - row["x3"]
    p3 = row["x3"] - row["x5"]
    p5 = row["x5"] - row["x10"]
    p10 = row["x10"]
    a = tail_alpha(row["x5"], row["x10"])
    tail_mean = min(10.0 * a / (a - 1.0), EV_CAP) if a > 1.0 else EV_CAP
    return (p_dead * 0.10 + p_dn * 0.35 + p_mid * 0.95 + p15 * 1.72 + p2 * 2.4
            + p3 * 3.8 + p5 * 6.8 + p10 * tail_mean)

def cond_on_threshold(fine_probs, cond5, thr_bucket_index):
    """Condition on the chain finishing at or above a fine-bucket boundary.
    thr_bucket_index = index of the first fine bucket that is entirely above the threshold."""
    w = {s: 0.0 for s in SCEN_ORDER}
    for i in range(thr_bucket_index, len(FINE_NAMES)):
        w[SCEN_OF_FINE[i]] += fine_probs[i]
    tot = sum(w.values())
    w = {s: v / tot for s, v in w.items()}
    return {o: sum(w[s] * cond5[s][o] for s in SCEN_ORDER) for o in OUTS}, tot

IDX_P50 = FINE_NAMES.index("165-220")   # SOL >= +50%  (>= $165)
IDX_P100 = FINE_NAMES.index("220-250")  # SOL >= +100% (>= $220)

def table_results(t, blend_name="Base"):
    fine = sol_fine[blend_name] if t["chain"] == "SOL" else eth_fine[blend_name]
    s5 = to5(fine)
    cond5 = token_cond(t, sol5["Base"] if t["chain"] == "SOL" else eth5["Base"])
    unc = uncond_from(s5, cond5)
    c50, p50 = cond_on_threshold(fine, cond5, IDX_P50)
    c100, p100 = cond_on_threshold(fine, cond5, IDX_P100)
    res = {"uncond": unc, "cond50": c50, "cond100": c100,
           "p_chain50": p50, "p_chain100": p100}
    for key in ("uncond", "cond50", "cond100"):
        r = res[key]
        r["ath"] = p_at_least(r, t["k_ath"])
        r["ev"] = ev_multiple(r)
    # scenario-by-scenario EV and ATH
    res["by_scen"] = {}
    for s in SCEN_ORDER:
        r = dict(cond5[s])
        r["ath"] = p_at_least(r, t["k_ath"])
        r["ev"] = ev_multiple(r)
        res["by_scen"][s] = r
    res["cond5"] = cond5
    return res

# ----------------------------------------------------------------------------
# 4b. Monte Carlo cross-check
# ----------------------------------------------------------------------------
rng = np.random.default_rng(SEED)
T_idio = rng.standard_t(df=3, size=N_PATHS) / math.sqrt(3.0)   # unit-variance t(3): heavy tails

def fit_lognormal_to_buckets(S0, edges, target, sig_grid, mu_grid):
    best = None
    for mu in mu_grid:
        for sg in sig_grid:
            p = bucket_probs_lognormal(S0, edges, mu, sg, T)
            sse = float(np.sum((p - target) ** 2))
            if best is None or sse < best[0]:
                best = (sse, mu, sg)
    return best

# A single lognormal cannot reproduce the bimodal blend; it is fitted only to give
# the "effective" drift/vol for the touch-probability sensitivity.
sse_s, MU_MC_SOL, SIG_MC_SOL = fit_lognormal_to_buckets(
    SOL_SPOT, FINE_EDGES, sol_fine["Base"], np.arange(0.40, 1.21, 0.01), np.arange(-0.60, 0.61, 0.01))
sse_e, MU_MC_ETH, SIG_MC_ETH = fit_lognormal_to_buckets(
    ETH_SPOT, ETH_EDGES, eth_fine["Base"], np.arange(0.35, 1.21, 0.01), np.arange(-0.60, 0.61, 0.01))

def sample_chain(S0, edges, fine_probs, sigma, n, n_base=2_000_000):
    """Terminal price draws whose fine-bucket frequencies equal the blended
    probabilities EXACTLY (in expectation): draw a large driftless lognormal
    sample (vol = sigma), split it by bucket, then resample each bucket with
    the blended weight. Within a bucket the shape is the IV lognormal."""
    base = S0 * np.exp(-0.5 * sigma ** 2 + sigma * rng.standard_normal(n_base))
    idx = np.digitize(base, edges)           # 0..len(edges)
    counts = rng.multinomial(n, fine_probs / fine_probs.sum())
    out = []
    for b, c in enumerate(counts):
        pool = base[idx == b]
        out.append(rng.choice(pool, size=c, replace=True))
    out = np.concatenate(out)
    rng.shuffle(out)
    return out

S_sol = sample_chain(SOL_SPOT, FINE_EDGES, sol_fine["Base"], SIGMA_SOL, N_PATHS)
S_eth = sample_chain(ETH_SPOT, ETH_EDGES, eth_fine["Base"], SIGMA_ETH, N_PATHS)
r_sol = np.log(S_sol / SOL_SPOT)
r_eth = np.log(S_eth / ETH_SPOT)
P_SOL_ATH_A = p_above(SOL_SPOT, SOL_ATH, 0.0, SIGMA_SOL, T) / p_above(SOL_SPOT, 250, 0.0, SIGMA_SOL, T)  # share of the >250 bucket above the ATH under (a)

def scen_of_price(S, S0):
    rel = S / S0 * SOL_SPOT
    cuts = [70, 110, 150, 250]
    idx = np.digitize(rel, cuts)
    return np.array(SCEN_ORDER)[idx]

scen_sol = scen_of_price(S_sol, SOL_SPOT)
scen_eth = scen_of_price(S_eth, ETH_SPOT)

def meme_multiple(r_chain, beta_up, beta_dn, delta, s_idio):
    r = beta_up * np.maximum(r_chain, 0) + beta_dn * np.minimum(r_chain, 0) + delta + s_idio * T_idio
    return np.exp(r)

def probs_from_multiples(m, mask=None):
    if mask is not None:
        m = m[mask]
    n = len(m)
    return {"up50": np.mean(m >= 1.5), "x2": np.mean(m >= 2), "x3": np.mean(m >= 3),
            "x5": np.mean(m >= 5), "x10": np.mean(m >= 10), "dn50": np.mean(m <= 0.5),
            "dead": np.mean(m <= 0.2)}

def calibrate_generic():
    """Find (beta_up, beta_dn, delta, s) so that the MC reproduces the generic
    scenario table (COND) as closely as possible (weighted by scenario probability)."""
    best = None
    w = sol5["Base"]
    masks = {s: scen_sol == s for s in SCEN_ORDER}
    for bu in [0.6, 0.8, 1.0, 1.2, 1.5, 1.8]:
        for bd in [1.0, 1.3, 1.6, 2.0, 2.4]:
            for delta in np.arange(-1.2, 0.21, 0.1):
                for s in np.arange(0.4, 1.61, 0.1):
                    m = meme_multiple(r_sol, bu, bd, delta, s)
                    err = 0.0
                    for sc in SCEN_ORDER:
                        p = probs_from_multiples(m, masks[sc])
                        err += w[sc] * sum((p[o] - COND[sc][o]) ** 2 for o in OUTS)
                    if best is None or err < best[0]:
                        best = (err, bu, bd, float(delta), float(s))
    return best

err_g, BU_G, BD_G, DELTA_G, S_G = calibrate_generic()

def calibrate_token(t, target_unc):
    """Per token: beta = lam * generic beta; find (delta, s) matching the token's
    scenario-table unconditional P(>=+50%), P(>=2x), P(<=-50%)."""
    r_chain = r_sol if t["chain"] == "SOL" else r_eth
    best = None
    for delta in np.arange(-2.0, 0.41, 0.05):
        for s in np.arange(0.3, 3.01, 0.05):
            m = meme_multiple(r_chain, BU_G * t["lam"], BD_G * t["lam"], delta, s)
            p = probs_from_multiples(m)
            err = ((p["up50"] - target_unc["up50"]) ** 2 + (p["x2"] - target_unc["x2"]) ** 2
                   + (p["dn50"] - target_unc["dn50"]) ** 2)
            if best is None or err < best[0]:
                best = (err, float(delta), float(s))
    return best

def mc_results(t, delta, s):
    r_chain = r_sol if t["chain"] == "SOL" else r_eth
    S_chain = S_sol if t["chain"] == "SOL" else S_eth
    S0 = SOL_SPOT if t["chain"] == "SOL" else ETH_SPOT
    scen = scen_sol if t["chain"] == "SOL" else scen_eth
    m = meme_multiple(r_chain, BU_G * t["lam"], BD_G * t["lam"], delta, s)
    out = {}
    for key, mask in (("uncond", None), ("cond50", S_chain >= 1.5 * S0), ("cond100", S_chain >= 2.0 * S0)):
        p = probs_from_multiples(m, mask)
        mm = m if mask is None else m[mask]
        p["ath"] = float(np.mean(mm >= t["k_ath"]))
        p["ev"] = float(np.mean(np.minimum(mm, EV_CAP)))
        p["median"] = float(np.median(mm))
        out[key] = p
    out["by_scen"] = {}
    for sc in SCEN_ORDER:
        mask = scen == sc
        p = probs_from_multiples(m, mask)
        p["ath"] = float(np.mean(m[mask] >= t["k_ath"]))
        p["ev"] = float(np.mean(np.minimum(m[mask], EV_CAP)))
        out["by_scen"][sc] = p
    return out

# Touch probabilities by daily simulation of SOL (fitted MC drift/vol)
def touch_probs(S0, mu, sig, levels, n=N_PATHS, steps=252, chunk=20_000):
    hits = {k: 0 for k in levels}
    dt = 1.0 / steps
    done = 0
    while done < n:
        c = min(chunk, n - done)
        z = rng.standard_normal((c, steps)).astype(np.float32)
        lr = np.cumsum((mu - 0.5 * sig ** 2) * dt + sig * math.sqrt(dt) * z, axis=1)
        mx = S0 * np.exp(lr.max(axis=1))
        for k in levels:
            hits[k] += int(np.sum(mx >= k))
        done += c
    return {k: v / n for k, v in hits.items()}

TOUCH_MC = touch_probs(SOL_SPOT, MU_MC_SOL, SIG_MC_SOL, [150, 200, 250, 300])
TOUCH_MC_DRIFTLESS = touch_probs(SOL_SPOT, 0.0, SIGMA_SOL, [150, 200, 250, 300])

# ----------------------------------------------------------------------------
# 5. Report
# ----------------------------------------------------------------------------
emit("# Risultati del modello probabilistico (8 ott 2026 -> 8 ott 2027)")
emit()
emit(f"Generated by model_probabilita.py (seed {SEED}, {N_PATHS:,} Monte Carlo paths). "
     "All figures are model ESTIMATES built from the research notes; see probability_model.md.")
emit()

# 5.1 SOL components
emit("## 1. SOL: component distributions on 8 Oct 2027 (S0 = $110)")
emit()
emit(f"(b) Kalshi fit: drift mu_b = {mu_b:+.2f}/yr, vol sigma_b = {sigma_b:.2f}, SSE = {sse_b:.4f} "
     f"(fitted on P(>=100)=71%, P(>=150)=34%, P(>=200)=27% at T={KALSHI_T}y from ${KALSHI_S0:.0f}; "
     f"fit reproduces: " + ", ".join(f"P(>={k})={pct(p_above(KALSHI_S0, k, mu_b, sigma_b, KALSHI_T))}" for k, _ in KALSHI) + "). "
     f"Applied for the first {KALSHI_T} y, then the 55% IV lognormal for the remaining {T-KALSHI_T:.2f} y: "
     f"effective 12-month vol {SIGMA_B_EFF:.2f}, mean log-return {LOG_MEAN_B:+.3f}.")
emit()
hdr = ["Bucket"] + ["(a) lognormal 55%", "(a') stress 70%", "(b) Kalshi-fitted", "(c) historical", "(d) macro -15%", "(d) macro -25%/60%", "(d) macro 0%"]
rows = []
for i, nm in enumerate(FINE_NAMES):
    rows.append([nm] + [pct(x[i]) for x in (comp_a, comp_a_stress, comp_b, comp_c, comp_d, comp_d_pess, comp_d_opt)])
md_table(hdr, rows)

emit("## 2. SOL: blended scenario probabilities (sensitivity)")
emit()
hdr = ["Scenario", "Ottimistico (a.30/b.30/c.30/d.10, d=0%)", "Base (a.35/b.20/c.20/d.25, d=-15%)", "Pessimistico (a.30/b.10/c.10/d.50, d=-25%, vol 60%)"]
rows = []
for s in SCEN_ORDER:
    rows.append([f"{s}: {SCEN_NAMES[s]}"] + [pct(sol5[b][s]) for b in ("Ottimistico", "Base", "Pessimistico")])
rows.append(["P(SOL >= +50%, >= $165)"] + [pct(sum(sol_fine[b][IDX_P50:])) for b in ("Ottimistico", "Base", "Pessimistico")])
rows.append(["P(SOL >= +100%, >= $220)"] + [pct(sum(sol_fine[b][IDX_P100:])) for b in ("Ottimistico", "Base", "Pessimistico")])
rows.append(["P(SOL >= ATH $294.85) [= P(>250) x share of the >250 bucket above $294.85 under the 55% lognormal]"] + [pct(sum(sol_fine[b][6:]) * P_SOL_ATH_A) for b in ("Ottimistico", "Base", "Pessimistico")])
md_table(hdr, rows)
for b in ("Ottimistico", "Base", "Pessimistico"):
    csv_rows.append(["SOL_scenario", b, "", ""] + [f"{sol5[b][s]:.4f}" for s in SCEN_ORDER])

emit("Fine buckets, Base blend: " + ", ".join(f"{n}: {pct(p)}" for n, p in zip(FINE_NAMES, sol_fine['Base'])))
emit()
emit(f"Single lognormal best-fitting the Base blend (used only for the touch sensitivity): drift {MU_MC_SOL:+.2f}/yr, vol {SIG_MC_SOL:.2f} (SSE {sse_s:.5f}). "
     f"Monte Carlo terminal SOL draws (bucket-resampled, so they match the blend): median = ${np.median(S_sol):.0f}, mean = ${np.mean(S_sol):.0f}, "
     f"share by scenario = " + ", ".join(f"{s}: {pct(np.mean(scen_sol == s))}" for s in SCEN_ORDER) + ".")
emit()
emit("## 3. SOL: probability of TOUCHING a level at any time in the 12 months")
emit()
hdr = ["Level", "Notes (2 x terminal, 55% vol, driftless)", "MC daily paths, driftless 55%", "MC daily paths, Base-blend drift/vol"]
rows = [[f"${k}", pct(TOUCH_NOTES[k]), pct(TOUCH_MC_DRIFTLESS[k]), pct(TOUCH_MC[k])] for k in (150, 200, 250, 300)]
md_table(hdr, rows)

emit("## 4. ETH (for WOJAK): blended scenario probabilities, same return buckets")
emit()
hdr = ["Scenario (ETH, S0 = $2,600)", "Ottimistico", "Base", "Pessimistico"]
rows = []
for s, nm in zip(SCEN_ORDER, [f"A: <${ETH_EDGES[0]:,}", f"B: ${ETH_EDGES[0]:,}-{ETH_EDGES[1]:,}", f"C: ${ETH_EDGES[1]:,}-{ETH_EDGES[2]:,}", f"D: ${ETH_EDGES[2]:,}-{ETH_EDGES[5]:,} (ATH $4,950 inside)", f"E: >${ETH_EDGES[5]:,}"]):
    rows.append([nm] + [pct(eth5[b][s]) for b in ("Ottimistico", "Base", "Pessimistico")])
rows.append(["P(ETH >= +50%)"] + [pct(sum(eth_fine[b][IDX_P50:])) for b in ("Ottimistico", "Base", "Pessimistico")])
rows.append(["P(ETH >= +100%)"] + [pct(sum(eth_fine[b][IDX_P100:])) for b in ("Ottimistico", "Base", "Pessimistico")])
md_table(hdr, rows)
emit(f"Monte Carlo lognormal fitted to the ETH Base blend: drift {MU_MC_ETH:+.2f}/yr, vol {SIG_MC_ETH:.2f}.")
emit()

# 5.2 Conditional table (generic)
emit("## 5. Conditional response of a GENERIC established Solana memecoin (12 months)")
emit()
emit("Rows: SOL scenario. Columns: probability that the memecoin reaches the outcome. ESTIMATES (see probability_model.md s.2).")
emit()
hdr = ["SOL scenario"] + [OUT_LABEL[o] for o in OUTS]
rows = [[f"{s}: {SCEN_NAMES[s]}"] + [pct(COND[s][o]) for o in OUTS] for s in SCEN_ORDER]
rows.append(["Unconditional (Base SOL blend)"] + [pct(generic_uncond[o]) for o in OUTS])
md_table(hdr, rows)
for s in SCEN_ORDER:
    csv_rows.append(["generic_conditional", s, "", ""] + [f"{COND[s][o]:.4f}" for o in OUTS])
emit(f"Sanity check vs Coin Metrics: implied generic P(reclaim ATH | ATH is ~5x away) = "
     f"{pct(p_at_least(generic_uncond, 5.0))}, (10x away) = {pct(p_at_least(generic_uncond, 10.0))}, "
     f"(20x away) = {pct(p_at_least(generic_uncond, 20.0))}; Coin Metrics multi-year reclaim rate = 3.3%.")
emit()

# 5.3 Per-token adjustments
emit("## 6. Per-token adjustment factors (odds multipliers: upside / downside)")
emit()
for name, t in TOKENS.items():
    emit(f"### {name}  (chain {t['chain']}, price {t['price']:g}, ATH {t['ath']:g} -> new ATH needs {t['k_ath']:.1f}x; cap ${t['cap_musd']}M; linkage lambda = {t['lam']})")
    emit()
    hdr = ["Factor", "Upside odds x", "Downside odds x"]
    rows = [[k, f"{v[0]:.2f}", f"{v[1]:.2f}"] for k, v in t["factors"].items()]
    rows.append(["**Product (raw)**", f"{t['M_up_raw']:.2f}", f"{t['M_dn_raw']:.2f}"])
    rows.append(["**Applied (clipped to [0.5, 2.0])**", f"{t['M_up']:.2f}", f"{t['M_dn']:.2f}"])
    md_table(hdr, rows)

# 5.4 Per-token results
emit("## 7. Per-token results: scenario table vs Monte Carlo")
emit()
emit(f"Generic MC calibration: beta_up = {BU_G}, beta_down = {BD_G}, decay drift delta = {DELTA_G:+.2f}/yr, "
     f"idiosyncratic scale s = {S_G:.2f} (Student-t, 3 d.o.f.); weighted SSE vs table = {err_g:.4f}.")
emit()
ALL = {}
summary_rows = []
for name, t in TOKENS.items():
    tr = table_results(t, "Base")
    tgt = tr["uncond"]
    err_t, d_t, s_t = calibrate_token(t, tgt)
    mr = mc_results(t, d_t, s_t)
    ALL[name] = (tr, mr, d_t, s_t)
    chain = t["chain"]
    emit(f"### {name}")
    emit()
    emit(f"MC token parameters: beta_up = {BU_G*t['lam']:.2f}, beta_down = {BD_G*t['lam']:.2f}, delta = {d_t:+.2f}, s = {s_t:.2f}; "
         f"P({chain} >= +50%) = {pct(tr['p_chain50'])}, P({chain} >= +100%) = {pct(tr['p_chain100'])}.")
    emit()
    hdr = ["Outcome", "Uncond. (table)", "Uncond. (MC)", f"given {chain} >= +50% (table)", f"given {chain} >= +50% (MC)", f"given {chain} >= +100% (table)", f"given {chain} >= +100% (MC)"]
    rows = []
    for o in OUTS + ["ath"]:
        lab = OUT_LABEL.get(o, f"New ATH (>= {t['k_ath']:.1f}x)")
        rows.append([lab, pct(tr["uncond"][o]), pct(mr["uncond"][o]), pct(tr["cond50"][o]), pct(mr["cond50"][o]), pct(tr["cond100"][o]), pct(mr["cond100"][o])])
        csv_rows.append([name, o, "table", "", f"{tr['uncond'][o]:.4f}", f"{tr['cond50'][o]:.4f}", f"{tr['cond100'][o]:.4f}"])
        csv_rows.append([name, o, "mc", "", f"{mr['uncond'][o]:.4f}", f"{mr['cond50'][o]:.4f}", f"{mr['cond100'][o]:.4f}"])
    rows.append(["Expected multiple (EV, tail capped at 30x)", f"{tr['uncond']['ev']:.2f}x", f"{mr['uncond']['ev']:.2f}x", f"{tr['cond50']['ev']:.2f}x", f"{mr['cond50']['ev']:.2f}x", f"{tr['cond100']['ev']:.2f}x", f"{mr['cond100']['ev']:.2f}x"])
    rows.append(["Prob.-weighted market cap ($M)", f"{t['cap_musd']*tr['uncond']['ev']:.1f}", f"{t['cap_musd']*mr['uncond']['ev']:.1f}", f"{t['cap_musd']*tr['cond50']['ev']:.1f}", f"{t['cap_musd']*mr['cond50']['ev']:.1f}", f"{t['cap_musd']*tr['cond100']['ev']:.1f}", f"{t['cap_musd']*mr['cond100']['ev']:.1f}"])
    rows.append(["Median multiple (MC only)", "-", f"{mr['uncond']['median']:.2f}x", "-", f"{mr['cond50']['median']:.2f}x", "-", f"{mr['cond100']['median']:.2f}x"])
    md_table(hdr, rows)
    csv_rows.append([name, "ev", "table", "", f"{tr['uncond']['ev']:.3f}", f"{tr['cond50']['ev']:.3f}", f"{tr['cond100']['ev']:.3f}"])
    csv_rows.append([name, "ev", "mc", "", f"{mr['uncond']['ev']:.3f}", f"{mr['cond50']['ev']:.3f}", f"{mr['cond100']['ev']:.3f}"])
    # scenario-by-scenario
    emit(f"Scenario-by-scenario ({chain} scenario -> outcome), scenario table / MC:")
    emit()
    hdr = ["Scenario", "P(scen)"] + [OUT_LABEL[o] for o in ("up50", "x2", "x5", "x10", "dn50", "dead")] + ["New ATH", "EV"]
    rows = []
    s5 = sol5["Base"] if chain == "SOL" else eth5["Base"]
    for s in SCEN_ORDER:
        a, b = tr["by_scen"][s], mr["by_scen"][s]
        rows.append([s, pct(s5[s])] + [f"{pct(a[o],0)} / {pct(b[o],0)}" for o in ("up50", "x2", "x5", "x10", "dn50", "dead")] + [f"{pct(a['ath'])} / {pct(b['ath'])}", f"{a['ev']:.2f}x / {b['ev']:.2f}x"])
        csv_rows.append([name, "scenario_" + s, "table", f"{s5[s]:.4f}"] + [f"{a[o]:.4f}" for o in OUTS] + [f"{a['ath']:.4f}", f"{a['ev']:.3f}"])
        csv_rows.append([name, "scenario_" + s, "mc", f"{s5[s]:.4f}"] + [f"{b[o]:.4f}" for o in OUTS] + [f"{b['ath']:.4f}", f"{b['ev']:.3f}"])
    md_table(hdr, rows)
    summary_rows.append([name, f"${t['cap_musd']}M", f"{t['k_ath']:.1f}x",
                         pct(tr["uncond"]["up50"]), pct(tr["uncond"]["x2"]), pct(tr["uncond"]["x3"]), pct(tr["uncond"]["x5"]), pct(tr["uncond"]["x10"]),
                         pct(tr["uncond"]["ath"]), pct(tr["uncond"]["dn50"]), pct(tr["uncond"]["dead"]),
                         f"{tr['uncond']['ev']:.2f}x", f"{t['cap_musd']*tr['uncond']['ev']:.1f}",
                         pct(tr["cond50"]["x2"]), pct(tr["cond100"]["x2"]), pct(tr["cond100"]["x5"]), pct(tr["cond100"]["ath"])])

emit("## 8. Summary table (scenario-table method, Base blend)")
emit()
hdr = ["Token", "Cap now", "ATH needs", "P(>=+50%)", "P(>=2x)", "P(>=3x)", "P(>=5x)", "P(>=10x)", "P(new ATH)", "P(<=-50%)", "P(dead <=-80%)", "EV multiple", "Prob.-wtd cap $M", "P(2x | chain>=+50%)", "P(2x | chain>=+100%)", "P(5x | chain>=+100%)", "P(ATH | chain>=+100%)"]
md_table(hdr, summary_rows)

emit("## 9. Summary table (Monte Carlo, Base blend)")
emit()
hdr = ["Token", "P(>=+50%)", "P(>=2x)", "P(>=3x)", "P(>=5x)", "P(>=10x)", "P(new ATH)", "P(<=-50%)", "P(dead)", "EV", "Median", "P(2x | chain>=+50%)", "P(2x | chain>=+100%)", "P(5x | chain>=+100%)", "P(ATH | chain>=+100%)"]
rows = []
for name, (tr, mr, d_t, s_t) in ALL.items():
    u = mr["uncond"]
    rows.append([name, pct(u["up50"]), pct(u["x2"]), pct(u["x3"]), pct(u["x5"]), pct(u["x10"]), pct(u["ath"]), pct(u["dn50"]), pct(u["dead"]), f"{u['ev']:.2f}x", f"{u['median']:.2f}x",
                 pct(mr["cond50"]["x2"]), pct(mr["cond100"]["x2"]), pct(mr["cond100"]["x5"]), pct(mr["cond100"]["ath"])])
md_table(hdr, rows)

emit("## 10. Sensitivity of the unconditional token probabilities to the SOL/ETH blend")
emit()
hdr = ["Token", "Blend", "P(SOL/ETH >= +50%)", "P(>=+50%)", "P(>=2x)", "P(>=5x)", "P(new ATH)", "P(<=-50%)", "P(dead)", "EV"]
rows = []
for name, t in TOKENS.items():
    for b in ("Ottimistico", "Base", "Pessimistico"):
        tr = table_results(t, b)
        u = tr["uncond"]
        rows.append([name, b, pct(tr["p_chain50"]), pct(u["up50"]), pct(u["x2"]), pct(u["x5"]), pct(u["ath"]), pct(u["dn50"]), pct(u["dead"]), f"{u['ev']:.2f}x"])
        csv_rows.append([name, "sensitivity_" + b, "table", f"{tr['p_chain50']:.4f}"] + [f"{u[o]:.4f}" for o in OUTS] + [f"{u['ath']:.4f}", f"{u['ev']:.3f}"])
md_table(hdr, rows)

emit("## 11. Linkage effect: what a rally buys you (Base blend, scenario table)")
emit()
emit("Difference between P(>=2x | chain >= +100%) and P(>=2x | chain <= 0%) shows how much of each token's upside actually depends on the chain.")
emit()
hdr = ["Token", "lambda", "P(2x | chain <= 0%, scen. A+B)", "P(2x | uncond.)", "P(2x | chain >= +100%)", "Ratio rally/no-rally"]
rows = []
for name, t in TOKENS.items():
    tr, mr, _, _ = ALL[name]
    s5 = sol5["Base"] if t["chain"] == "SOL" else eth5["Base"]
    wA, wB = s5["A"], s5["B"]
    p_norally = (wA * tr["cond5"]["A"]["x2"] + wB * tr["cond5"]["B"]["x2"]) / (wA + wB)
    rows.append([name, t["lam"], pct(p_norally), pct(tr["uncond"]["x2"]), pct(tr["cond100"]["x2"]), f"{tr['cond100']['x2']/max(p_norally,1e-9):.1f}x"])
md_table(hdr, rows)

# write files
with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines) + "\n")
with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["token_or_block", "item", "method", "p_scenario_or_chain50", "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9"])
    w.writerow(["# SOL_scenario rows: v1..v5 = P(A..E); generic_conditional rows: v1..v7 = up50,x2,x3,x5,x10,dn50,dead;"])
    w.writerow(["# token outcome rows (method table/mc): v1 = unconditional, v2 = | chain>=+50%, v3 = | chain>=+100%;"])
    w.writerow(["# token scenario_X rows: p_scenario, v1..v7 = up50,x2,x3,x5,x10,dn50,dead, v8 = new ATH, v9 = EV;"])
    w.writerow(["# token sensitivity rows: p_chain50, v1..v7 outcomes, v8 = new ATH, v9 = EV"])
    for r in csv_rows:
        w.writerow(r)
print(f"\nWritten: {OUT_MD}\nWritten: {OUT_CSV}\nWritten: {OUT_TXT}")
