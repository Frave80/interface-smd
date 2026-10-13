# Probability model, 8-token extension: CASHCAT (Robinhood Chain) and PEPE (Ethereum) added to the six-token model (8 Oct 2026 -> 8 Oct 2027)

Model date: 13 October 2026. Author: research agent (no web access; all inputs come from the notes listed below).

Files in this folder:
- `model_probabilita_8.py` — the extended model (Python 3, numpy only). Run from this folder with `python3 -I model_probabilita_8.py` (~75 s).
- `risultati_probabilita_8.md` — all result tables for the eight tokens, written by the script (same layout as the original `risultati_probabilita.md`, plus sections 5b, 5c and 12 and the per-state table for CASHCAT).
- `risultati_probabilita_8.csv` — the same results as machine-readable rows (new row types: `pepe_conditional`, `rh_<state>`).
- `output_modello_8.txt` — the verbatim console output of the run documented here.
- `probability_model_8.md` — this file. It documents **only what is new**: the two tokens' inputs, the PEPE-specific conditional table, the Robinhood Chain adoption factor, the two tokens' multipliers, their results and their specific caveats. Everything else (SOL/ETH scenario distributions, the generic conditional table, the six original tokens, the Monte Carlo design, the general caveats) is documented in `../Probabilità rialzo memecoin Solana 2027/probability_model.md` and is **unchanged**.

Input notes (cited as [CASHCAT-KQn], [PEPE-Qn], and the original labels [SOL-Qn], [BASE-KQn], [OUTLOOK-KQn]):
- [CASHCAT-KQn] `cashcat.md` (this folder), key questions KQ1–KQ8.
- [PEPE-Qn] `pepe.md` (this folder), questions Q1–Q9.
- [SOL-Qn], [BASE-KQn] `../Probabilità rialzo memecoin Solana 2027/{sol_probability_inputs,memecoin_base_rates}.md`.
- [OUTLOOK-KQn] `../Memecoin Solana Chillguy Chillhouse Troll/solana_altcoin_outlook.md` (via the original probability_model.md).

Label convention as in the original: **[NOTE]** = number taken from a note; **[ASSUMPTION]** = chosen by the modeller and justified in words; **[CALC]** = computed by the script. Nothing here is financial advice; see section 7.

---

## 0. What changed in the code, and what did not

**Unchanged (and verified):** seed (20261009), number of paths (100,000), the SOL and ETH scenario distributions and blends, the generic conditional table, the odds-multiplier mechanics and bounds [0.5, 2.0], the consistency rule, the EV band midpoints and the 30× cap, the ATH interpolation/Pareto tail, the Monte Carlo design (bucket-resampled chain draws, Student-t(3) shock, generic calibration grids, per-token (δ, s) grids), and every parameter of CHILLGUY, CHILLHOUSE, TROLL, TRIPLE T, CUPSEY and WOJAK. The script's section 12 reads the original `risultati_probabilita.csv` and compares all 1,154 numeric cells that concern the SOL scenario rows, the generic table and the six original tokens (unconditional, conditional on chain ≥ +50% / +100%, scenario-by-scenario, sensitivity, EV): **maximum absolute difference = 0.000000, i.e. the six original tokens' Base (and Ottimistico/Pessimistico) results are reproduced exactly** and the rows of sections 8–11 for those tokens are identical to `risultati_probabilita.md`.

**Added:**
1. `COND_PEPE`, a second conditional table for the sector bellwether (section 2), and `pepe_table_uncond`, its unconditional under the ETH Base blend.
2. `RH_STATES`, a three-state "Robinhood Chain adoption" factor (section 3.2), applied to CASHCAT as a mixture of odds multipliers in the scenario-table method and as a per-path log-shift of the drift in the Monte Carlo. The state draws use a **separate** random generator (seed 20261010) so that the original random stream (chain draws, idiosyncratic shocks, touch paths) is untouched.
3. Two entries in `TOKENS` (`CASHCAT (RH)`, `PEPE (ETH)`), appended after WOJAK; each token may now carry its own `table` (default: the generic one) and an optional `rh` factor.
4. `token_cond()` generalised: the linkage mixture may use the token's own table, is clipped to [0.0005, 0.995] (only relevant when λ > 1), and may apply the RH mixture. For the six original tokens (λ ≤ 1, generic table, no RH factor) the computation path is identical.
5. Monte Carlo: `calibrate_table()` generalises the generic calibration (called with exactly the original grids for the generic table, so β_up = 1.5, β_dn = 1.3, δ = −0.80, s = 1.60 as before) and is called a second time on the ETH draws for the PEPE table; token betas are λ × (betas of the token's table). `meme_multiple()` accepts a per-path drift (for the RH shift). The per-token s grid is the original 0.3–3.0 and is extended to 4.0 only for the token with the RH factor.
6. Report: sections 5b (PEPE table), 5c (RH factor), a per-state results table for CASHCAT in section 7, and the reproduction check in section 12.

---

## 1. Chain conditioning: both new tokens use the ETH distribution

Both tokens are conditioned on the ETH scenario distribution already built for WOJAK (ETH spot $2,600, vol 50%, SOL's prediction-market and historical components reused as an altcoin proxy; see original s.1.7). Base blend: A 30.2%, B 29.1%, C 17.1%, D 13.8%, E 9.8%; P(ETH ≥ +50%) = 19.3%, P(ETH ≥ +100%) = 11.9% [CALC, unchanged]. The generic table under this ETH blend gives an unconditional ≥ +50% of 18.2%, ≥ 2x 11.7%, ≥ 5x 3.9%, ≤ −50% 57.6%, dead 32.4% [CALC] — this is the reference against which both new tokens should be read.

Why ETH for CASHCAT, which lives on Robinhood Chain: Robinhood Chain is an Arbitrum Orbit L2 whose gas and bridge asset is ETH and whose main pool is CASHCAT/WETH [CASHCAT-KQ2, KQ6]; there is no "chain token" to condition on, and the note finds no evidence of any ETH-driven move in its history [CASHCAT-KQ8]. ETH therefore enters only as the *chain-return component* with a low linkage (section 3.1); the chain-specific drivers are modelled separately (section 3.2).

---

## 2. PEPE (Ethereum) — the sector bellwether

### 2.1 Inputs [NOTE]
| Item | Value | Source |
|---|---|---|
| Price | $0.0000041 (consensus of 10–13 Oct 2026 readings: Coinbase $0.00000405, Kraken ≈ $0.0000042, Bybit $0.00000423, MetaMask $0.00000419) | [PEPE-Q1] |
| Market cap | **$1,750M** (range $1.67–1.78B; Kraken $1.76B, Bybit $1.78B 12 Oct) — FDV = cap (420.69T fully circulating) | [PEPE-Q1] |
| ATH | $0.00002825 on 9 Dec 2024 (cap > $11B) → new ATH needs **6.9×** | [PEPE-Q2] |
| Drawdown | −85% to −86% from ATH; no new high in 22 months; 2025 −79%; 2026 roughly flat (−45% into June/July, +130% into late Sept) | [PEPE-Q2, Q6] |
| Holders | 592,524 (Etherscan, 2 Oct 2026), +0.9% since 13 Sep | [PEPE-Q1, Q5] |
| Volume / OI | spot $156–207M/day; futures OI $322.9M (CoinGlass, 2 Oct); OI/cap ≈ 0.19 | [PEPE-Q1] |
| Listings | Binance spot (5 May 2023) + 1000PEPE perps; Coinbase International perps (Apr 2024); Robinhood and Coinbase US spot (Nov 2024); Kraken Pro perps; Bybit; Valour SEK ETP | [PEPE-Q3] |
| ETF | Canary spot PEPE ETF: S-1 8 Apr 2026, S-1/A 2 Oct 2026 (Cboe BZX, BitGo custody); not effective, no launch date | [PEPE-Q3]; also [BASE-KQ5 ETF pipeline] |
| Beta to ETH | Jun→Sep 2026 leg: ETH +74% ($1,559 → $2,716), PEPE +89% to +136% → upside beta ≈ 1.2–1.8×; 2024 ≈ 18× in cap vs ETH ≈ +50%; downside: −13% on 24 Sep 2026 risk-off day, Oct 2025 crash to $0.0000065 with >$20M liquidations | [PEPE-Q6] |
| Concentration | top-10 ≈ 41% of circulating ex-exchanges (ETF filing, early 2026); 77% raw Etherscan top-10 (Sep 2026, includes CEX hot wallets); top-100 non-exchange wallets ≈ 86T ≈ 20%, net accumulating in 2026 | [PEPE-Q4] |
| Reputation | anonymous team; Aug 2023 multisig dump (16T, ~$15M, threshold changed 5/8 → 2/8); Binance's own listing note "no utility", insiders ≈ 7%; continuous "Pepeto" paid-promo noise; name confusion with PEPECOIN / Pepe Community | [PEPE-Q2, Q9] |

### 2.2 Why PEPE gets its own conditional table [ASSUMPTION, each row justified]
The generic table (original s.2) describes a small *established* meme in decay: a 2–2.5× downside amplification, a 33% chance of dying within a year, a thin but real 5–10× tail. PEPE does not fit that description: it is ~100× larger than the other seven tokens, has the deepest listing/product stack of any ERC-20 meme, 593K holders still rising after a −85% drawdown, and an upside beta to ETH that has *shrunk* to 1.2–1.8× [PEPE-Q3, Q5, Q6, Q9 inferences]. The table below keeps the five ETH scenarios and the seven outcomes and changes the cells:

| ETH scenario | ≥ +50% | ≥ 2x | ≥ 3x | ≥ 5x | ≥ 10x | ≤ −50% | ≤ −80% (dead) |
|---|---|---|---|---|---|---|---|
| A Crollo (< −36%) | 2% (3%) | 0.8% (1.5%) | 0.3% (0.8%) | 0.1% (0.3%) | 0.03% (0.1%) | 70% (85%) | 25% (55%) |
| B Ribasso (−36% to 0) | 7% (8%) | 3% (4%) | 1.2% (2.2%) | 0.4% (1%) | 0.1% (0.3%) | 50% (65%) | 12% (35%) |
| C Laterale (0 to +36%) | 20% (18%) | 8% (10%) | 3.5% (5.5%) | 1.2% (2.5%) | 0.3% (0.8%) | 30% (45%) | 6% (20%) |
| D Rialzo forte (+36% to +127%) | 55% (40%) | 30% (25%) | 15% (15%) | 5% (8%) | 1% (3%) | 15% (28%) | 3% (12%) |
| E Euforia (> +127%) | 85% (65%) | 70% (50%) | 45% (35%) | 20% (20%) | 5% (8%) | 8% (15%) | 1% (6%) |
| **Unconditional, Base ETH blend** [CALC] | **22.0%** (18.2%) | **13.5%** (11.7%) | **7.5%** (7.3%) | **3.0%** (3.9%) | **0.7%** (1.5%) | **43.7%** (57.6%) | **12.6%** (32.4%) |

(generic value in parentheses)

Adjustment-by-adjustment:
- **"Dead" (≤ −80%) cut to roughly half or less in every row.** A −80% from $1.75B is a ~$350M cap, below PEPE's January 2024 cap ($591M), below the Oct 2025 crash levels ($2.9B on 29 Oct 2025; ~$1.06–1.26B at the 2025 low) and below every reading of 2026 [PEPE-Q2]. PEPE went through the −79% 2025 year with holders still rising (+5K/month in a −85% drawdown) and CEX order-book depth that held even during the 2023 team dump [PEPE-Q5, Q9, Kaiko]. The Coin Metrics "two-thirds never have a second rally / 3.3% reclaim" statistics (E1 in the original) are drawn from 150 small Solana memes; PEPE already made a second-cycle ATH (Dec 2024, after a 2023 launch) [PEPE-Q2; OUTLOOK-KQ6]. Row A keeps 25% because an ETH crash of more than a third with a 1.3–1.8× downside beta and a liquidation-prone $323M perp book (OI/cap 0.19) [PEPE-Q1, Q6] can still produce a −80%.
- **"≤ −50%" lowered** (85/65/45/28/15 → 70/50/30/15/8). Same reasoning: PEPE's downside is a beta to ETH, not the decay-to-zero drift of a one-cycle meme. In A it remains the modal outcome (70%): 2025's −79% and the Oct 2025 crash show that a risk-off year is still devastating [PEPE-Q2, Q6]. In D/E a halving while ETH rises ≥ 36% is rare for a bellwether (15%/8%) but not impossible (Aug 2025: "memecoin sector underperforms broader crypto market" while BTC rose) [PEPE-Q6].
- **"≥ +50%" and "≥ 2x" raised in D and E, roughly flat in C.** With a beta of 1.2–1.8× [PEPE-Q6], ETH +36…+127% maps to PEPE ≈ +45…+230% and ETH > +127% to PEPE > +150%: hence 55%/30% in D and 85%/70% in E. The Jun→Sep 2026 leg (+89–136% in three months while ETH +74%) is the template [PEPE-Q6]. In C (ETH 0 to +36%) the table is close to generic (20%/8%): a 2026-style ETH +36% gives PEPE roughly +45–65%, so ≥ +50% is a coin-flip-minus, while ≥ 2x requires a leverage/short-squeeze episode like 21–22 Sep 2026 (+40–45% in a week with no project catalyst) [PEPE-Q2, Q6].
- **"≥ 5x" and "≥ 10x" lowered in every row except E's 5x.** 5× = $8.7B (near the Dec 2024 peak), 10× = $17.5B (above the $11.4B record) [PEPE-Q2]. Reflexivity has faded from ≈ 18× in 2024 to 1.2–1.8× in 2026 [PEPE-Q6]; the 2024-type 300% rallies ("PEPE +300% as ETH crossed $4k") belong to row E only, where 20% ≥ 5x is kept and ≥ 10x is 5% (a new record cap). For the 2.5× and 3.2× moves used in the small tokens' "new ATH" column, PEPE's analogue is a 6.9× — a return to the Dec 2024 record — which is why its new-ATH probability is low (section 2.5).
- A smaller **A/B upside** (2%/7% ≥ +50%) than generic: a bellwether cannot have a viral idiosyncratic run against a crashing ETH the way a $5M token can; its idiosyncratic component is small (confirmed by the MC calibration, s = 0.85 vs 1.3–2.4 for the small tokens).
- Monotonicity across columns and rows is imposed by construction, as in the original.

Sanity checks [CALC]: unconditional ≥ 2x = 13.5% (generic 11.7%) with P(ETH ≥ +100%) = 11.9%: PEPE doubles roughly as often as ETH does, slightly more because of its > 1 beta — consistent with "high-beta ETH proxy" [PEPE-Q6]. Unconditional dead = 12.6% vs 32.4% generic: one chance in eight of a −80%, which the DappRadar bearish model (−14%/yr) and the Cowen "most downside in tightening liquidity" view [PEPE-Q7, Q9] make plausible but not dominant.

### 2.3 Linkage λ = 1.10 [ASSUMPTION]
The mixture p = λ·T(o|s) + (1−λ)·T_unc(o) with λ = 1.1 means p = T(o|s) + 0.1·[T(o|s) − T_unc(o)]: the scenario dependence of the PEPE table is amplified by 10%. Rationale: the note finds correlation "positive and high during risk-off" and an upside beta > 1 on the 2026 leg [PEPE-Q6]; PEPE is the first memecoin institutions access and the one that "sets the tone" for ERC-20 memes [PEPE-Q8, Q9], i.e. it tracks ETH slightly *more* than the table built for it. The requested range was 1.0–1.2; 1.1 is the midpoint. The mixture is clipped to [0.05%, 99.5%]: the floor binds in scenario A for all five upside outcomes, in scenario B for ≥ 10x and in scenario E for "dead", where the amplified mixture (e.g. 1.1 × 2% − 0.1 × 22% = 0 for A/≥ +50%; 1.1 × 1% − 0.1 × 12.6% < 0 for E/dead) would be zero or negative — those cells are set to 0.05%, which is why PEPE's A row shows 0% upside and its E row 0% dead in the output. All other cells are unaffected. In the Monte Carlo the token betas are λ × the betas calibrated to the PEPE table on the ETH draws: β_up = 1.1 × 1.6 = **1.76**, β_dn = 1.1 × 0.8 = **0.88** (section 2.6) — the upside beta lands in the note's 1.2–1.8× range.

### 2.4 Odds multipliers [ASSUMPTION, each justified by a note]
Because the PEPE table already encodes the bellwether's survivorship and ETH-tracking, the multipliers only capture PEPE-specific deviations from "a generic bellwether" and are deliberately mild (no factor beyond 0.90–1.15), to avoid double counting.

| Factor | up | down | Source |
|---|---|---|---|
| cycle age: 2023 launch, ATH Dec 2024; a second-cycle ATH already proven (not a one-cycle meme) | 0.90 | 1.00 | [PEPE-Q2]; OUTLOOK-KQ6 |
| drawdown −85%, no new high in 22 months, 2026 lower highs until Sept | 0.95 | 1.05 | [PEPE-Q2, Q6] |
| 592K holders rising, $150–210M/day volume, $323M OI, CEX depth resilient | 1.05 | 0.90 | [PEPE-Q1, Q5, Q9] |
| CEX ladder: Binance, Coinbase, Kraken, Bybit, Robinhood spot + perps; Valour ETP; no delisting risk | 1.05 | 0.90 | [PEPE-Q3] |
| catalysts: Canary spot ETF (S-1/A 2 Oct 2026) — binary; US perpetuals pending CFTC | 1.15 | 1.05 | [PEPE-Q3, Q9]; [BASE-KQ5] |
| concentration: top-10 41% ex-CEX (77% raw); whales net-accumulating in 2026 | 0.95 | 1.05 | [PEPE-Q4] |
| reputation: anonymous team, Aug 2023 multisig dump, Pepeto promo noise, name confusion | 0.95 | 1.00 | [PEPE-Q2, Q9] |
| **product → applied** | **0.98 → 0.98** | **0.94 → 0.94** | |

The ETF factor is the only one above 1.10: approval would be the single largest structural catalyst (first US spot memecoin ETF after DOGE/BONK products [BASE-KQ5]), while rejection or indefinite delay "removes the main 2026 narrative" [PEPE-Q9], hence both an upside and a small downside multiplier. Net, the multipliers are close to neutral (0.98 / 0.94): PEPE's numbers come almost entirely from its table and its linkage, which is the intended reading.

### 2.5 Results (Base blend) [CALC]
| | Uncond. (table) | Uncond. (MC) | given ETH ≥ +50% (table / MC) | given ETH ≥ +100% (table / MC) |
|---|---|---|---|---|
| ≥ +50% | 21.8% | 20.4% | 74.8% / 74.3% | 85.5% / 87.7% |
| ≥ 2x | 13.5% | 15.2% | 53.7% / 60.7% | 67.8% / 78.2% |
| ≥ 3x | 7.6% | 9.4% | 32.2% / 39.7% | 42.7% / 55.3% |
| ≥ 5x | 3.0% | 4.4% | 13.4% / 18.5% | 18.6% / 26.7% |
| ≥ 10x | 0.7% | 1.4% | 3.2% / 5.3% | 4.6% / 7.4% |
| ≤ −50% | 42.5% | 43.2% | 7.7% / 3.2% | 5.4% / 1.7% |
| dead (≤ −80%) | 12.0% | 10.4% | 1.0% / 0.8% | 0.4% / 0.6% |
| New ATH (6.9×) | 1.6% | 2.6% | 6.9% / 10.3% | 9.7% / 14.8% |
| EV multiple (cap 30×) | 1.22× | 1.32× | 3.10× / 3.64× | 3.79× / 4.55× |
| Prob.-weighted cap | $2.13B | $2.32B | $5.4B / $6.4B | $6.6B / $8.0B |
| MC median multiple | — | 0.58× | — / 2.45× | — / 3.25× |

Sensitivity to the ETH blend (table method, unconditional): ≥ +50% 25.8% / 21.8% / 16.8%, ≥ 2x 16.7% / 13.5% / 9.8%, ≥ 5x 3.9% / 3.0% / 2.0%, new ATH 2.0% / 1.6% / 1.1%, ≤ −50% 40.0% / 42.5% / 46.8%, dead 11.2% / 12.0% / 13.6%, EV 1.37× / 1.22× / 1.03× (Ottimistico / Base / Pessimistico). PEPE is the token most sensitive to the ETH view (its P(≥ 2x) moves −27%/+24% relative between blends vs ±10–15% for the others), as a bellwether should be. Linkage table (section 11 of the output): P(≥ 2x | ETH ends ≤ 0%) = 1.0% vs 67.8% if ETH doubles — a 70× ratio; essentially all of PEPE's upside is ETH's upside.

### 2.6 Monte Carlo note [CALC]
The PEPE table was calibrated on the ETH draws with wider beta grids (0.8–2.0) and a lower idiosyncratic floor (0.2): β_up = 1.6, β_dn = 0.8, δ = −0.50/yr, s = 1.00 (weighted SSE 0.0043, vs 0.0037 for the generic table). The downside beta sits at the lower edge of its grid: as in the original model, the negative drift δ absorbs most of the downside, so the fitted β_dn understates the note's "1.3–1.8× downside" — read δ and β_dn together. The per-token refit gives δ = −0.50, s = 0.85, the smallest idiosyncratic scale of the eight tokens (small memes: 1.30–3.00), which is the quantitative counterpart of "bellwether". The MC's conditional figures are above the table's (P(2x | ETH ≥ +100%) 78% vs 68%; new ATH 2.6% vs 1.6%) because with β_up = 1.76 and a small s the MC is close to a pure beta play; quote the pair as a range.

---

## 3. CASHCAT (Robinhood Chain) — a three-month-old chain-mascot meme

### 3.1 Inputs [NOTE]
| Item | Value used | Range / conflicts | Source |
|---|---|---|---|
| Price | $0.115 (8 Oct 2026) | $0.18 (2 Oct), $0.1555 (~4 Oct), −14% day / −21% week / −40% month by 7 Oct; no 9–13 Oct reading | [CASHCAT-KQ2] |
| Market cap | **$115M** (8 Oct; ≈ FDV, 1B supply minus 1.17% burned) | $168M (1 Oct), $174.5M (2 Oct), $171.5M (undated OpenSea) → **$115–175M**; prob.-weighted caps below scale linearly with the chosen base | [CASHCAT-KQ2] |
| ATH | $0.3115 on 3 Sep 2026 → new ATH needs **2.7×** on price | ATH cap $254M (Tangem) vs ~$311M (price × supply) vs July peak $226–236M → on cap the multiple is 2.2–2.7× | [CASHCAT-KQ3] |
| Drawdown | −63% from ATH (8 Oct); three pumps and three 50–85% drawdowns in 14 weeks (ATL $0.033 on 28 Jul) | | [CASHCAT-KQ3] |
| Holders | 41–112K: 41.2K (DEXTools, Aug), > 61K (Arkham, 27 Jul), 112.6K (GeckoTerminal, undated) | conflicting methodologies | [CASHCAT-KQ2] |
| Liquidity | one Uniswap v3 CASHCAT/WETH pool $2.6M (GeckoTerminal) – $5.4M (DEX Screener) → 2–4% of cap; secondary v4 CASHCAT/USDG pool | | [CASHCAT-KQ2, KQ5] |
| Derivatives | Hyperliquid > 70% of futures volume; −60% perp flash crash in July; $611K liquidations in a 29% rally | | [CASHCAT-KQ2, KQ3] |
| Listings | Robinhood app + Legend (6 Aug 2026, +151% in 15 h); Binance Alpha 2.0 + Binance Wallet perps 10×; KuCoin spot (15 Jul), MEXC, Gate, Bitrue; perps on OKX, Hyperliquid, KuCoin, Gate, MEXC; no Coinbase/Kraken | | [CASHCAT-KQ4] |
| Concentration | top-1,000 addresses 89.1% (Arkham, 27 Jul); largest wallet 137.15M = 13.7% (unidentified, possibly CEX/bridge custody); vesting contract 1.37%; LP burned, 0/0 tax; Bubblemaps "Coordinated?" on pre-listing buys | | [CASHCAT-KQ5] |
| Chain | Robinhood Chain mainnet 1 Jul 2026 (Arbitrum Orbit, chain ID 4663); TVL ~$1.03B (1 Oct); $15B stock-token DEX volume in 100 days; daily fees −97% from the early-Sep peak; memecoin-stock-pair volume −96%; daily transactions −42% to 6.2M (early Oct); 90-day gas subsidy ended 29 Sep (one conflicting report of an extension to 31 Dec); Noxa launchpad (which launched CASHCAT) paused 11 Jul and vanished; $18.4M rug-pull ring (30 Sep); single Robinhood sequencer, 7-day exit window, 7-of-8 upgrade multisig; 14-minute outage 4 Sep | | [CASHCAT-KQ1, KQ5, KQ6] |
| Recent events | hack: 3.7M CASHCAT from a compromised wallet swapped to ETH/BNB/SOL (Lookonchain); airdrop-claim selling (the token "never ran a claim-based airdrop" per another source); Artificial Inu (AI) overtook CASHCAT as the chain's largest meme (early Sep); HOOD earnings 27 Oct | | [CASHCAT-KQ3, KQ6, KQ7] |
| Relation to ETH | no computed beta; week to 7 Oct: ETH −7%, CASHCAT −21% (≈ 3× downside); every large move coincided with a chain-level event, none with an ETH move | | [CASHCAT-KQ8] |

### 3.2 The "Robinhood Chain adoption" factor [ASSUMPTION, documented]
The note's central inference is that CASHCAT "is effectively a levered proxy on Robinhood Chain memecoin attention" [CASHCAT-KQ7]: its three pumps were the mainnet launch / Tenev follow (+1,700%), the Robinhood app listing (+151%) and the Pons / stock-paired meme season (ATH on 3 Sep, two days after the chain's record $1.595B DEX day), and its slide tracks the chain's activity collapse [CASHCAT-KQ3, KQ6, KQ8]. This driver is neither ETH nor the generic memecoin lottery, so it is modelled explicitly as a three-state factor, **independent of the ETH scenario**, that is part of the token's idiosyncratic component:

| State | What it means | Probability | Upside odds × | Downside odds × | MC log-shift |
|---|---|---|---|---|---|
| Revival | memecoin season returns to Robinhood Chain: HOOD/Tenev promotion, a new launchpad replacing Noxa/Pons, Robinhood-app retail flows; CASHCAT as the app-listed incumbent re-rates | 20% | 2.00 | 0.60 | +0.70 (≈ 2.0×) |
| Stable | chain settles at its post-subsidy level (TVL ~$1B, stock tokens growing, meme activity a fraction of September); CASHCAT keeps a niche as "the Robinhood meme" | 45% | 1.00 | 1.00 | 0 |
| Decay | activity keeps falling after the −42/−96/−97% drops, memecoin pairs die, attention migrates (as it did from Noxa to Pons to AI); CASHCAT follows the Coin Metrics decay path | 35% | 0.50 | 1.60 | −0.70 (≈ 0.5×) |

Why these probabilities: the chain is 14 weeks old and the memecoin mania that created the token "has largely passed" [CASHCAT-KQ6 inference]; fees −97%, pair volume −96%, transactions −42%, subsidy ended, launchpad gone, rug ring, PONS −71% from ATH [CASHCAT-KQ6] argue for Decay being at least as likely as Revival. Against that, the structural base is intact (TVL ~$1.03B, $15B stock-token volume, Robinhood retaining ~89% of fees, 190+ tokenized equities, daily active users that overtook Base in July) and Robinhood has an obvious commercial incentive to keep promoting its chain (HOOD earnings 27 Oct, Evercore/Truist initiations) [CASHCAT-KQ6, KQ7]. 20/45/35 encodes "more likely to fade than to revive, but a revival is a real one-in-five". The odds multipliers (2.0/0.6 and 0.5/1.6) are symmetric in log-odds (±0.69 and ∓0.51/+0.47) and the MC shifts (±0.70 in log, i.e. a 2× / 0.5× multiplicative shift of the whole distribution) are chosen to be of the same order as the Robinhood-listing move (+151% in 15 hours) and the Noxa-pause drop (−33% in 24 h, −60–70% in days) [CASHCAT-KQ3]; they are the modeller's calibration of "one chain-level event's worth of impact over a year". In the scenario table the factor is a mixture (P(o) = Σ_r P(r)·odds_mult(p(o), M_r)), so the unconditional numbers are the probability-weighted average of the three states; the per-state rows are reported separately (section 3.5).

### 3.3 Linkage λ = 0.45 [ASSUMPTION]
Requested range 0.4–0.5; 0.45 chosen. It is below every original token (0.5–0.8) because the note finds no ETH-driven move in CASHCAT's history [CASHCAT-KQ8], while ETH still matters mechanically (the main pool is CASHCAT/WETH; the chain's bridge and gas asset is ETH; a crypto-wide risk-off would hit a 2–4%-liquidity token hard — the 3× downside in the week to 7 Oct [CASHCAT-KQ2, KQ8]). The MC betas are 0.45 × (1.5, 1.3) = 0.68 / 0.59. The remaining 55% of the scenario dependence is replaced by the generic unconditional, on top of which the Robinhood Chain factor adds the chain-specific variance.

### 3.4 Odds multipliers [ASSUMPTION, each justified by a note]
| Factor | up | down | Source |
|---|---|---|---|
| cycle age: Jul 2026 launch, < 6 months old, ATH 3 Sep 2026 — a **current-cycle** token still inside its first attention cycle (the original scheme: 2024-cycle 0.70/1.15, 2025 own-cycle 1.00/1.00, 2026 launches 1.10/0.95; the youngest token gets the top of that ladder) | 1.15 | 0.95 | [CASHCAT-KQ1, KQ3]; original s.3.2 |
| drawdown −63% from ATH, −40% on the month, momentum negative after the hack-driven dump | 1.00 | 1.05 | [CASHCAT-KQ2, KQ3] |
| holders 41–112K (conflicting) but DEX liquidity only $2.6–5.4M (2–4% of cap) concentrated in one pool; Hyperliquid > 70% of futures with a −60% flash-crash precedent | 1.05 | 1.10 | [CASHCAT-KQ2, KQ5] |
| CEX ladder: in the Robinhood app and Legend (the only chain meme confirmed in-app: a durable US-retail distribution edge), Binance Alpha 2.0 + Wallet perps, KuCoin, MEXC, Gate, Bitrue, OKX/Hyperliquid perps; no Coinbase/Kraken | 1.20 | 0.95 | [CASHCAT-KQ4, KQ7] |
| catalysts: HOOD earnings 27 Oct, letscash.fun community launchpad, chain news flow; lost the #1 chain-meme slot to AI | 1.05 | 1.00 | [CASHCAT-KQ1, KQ6, KQ7] |
| concentration penalty: top-1,000 = 89.1%, largest wallet 13.7% unidentified, 1.37% vesting contract, Bubblemaps "Coordinated?" pre-listing buys, hack-driven dump | 0.90 | 1.15 | [CASHCAT-KQ5] |
| chain-risk penalty: 3-month-old single-sequencer L2 with 7-day exits and instant upgradeability, Noxa vanished, $18.4M rug ring, gas subsidy ended, memecoin activity −96/−97% | 0.90 | 1.15 | [CASHCAT-KQ5, KQ6] |
| **product → applied** | **1.23 → 1.23** | **1.38 → 1.38** | |

Both products are above 1: CASHCAT is a *higher-variance* token than the generic established meme (more upside odds through youth and distribution, more downside odds through concentration, chain risk and thin liquidity). The concentration and chain-risk penalties requested are the two 0.90/1.15 lines; they take 19% off the upside odds and add 32% to the downside odds before the RH factor.

### 3.5 Results (Base blend) [CALC]
| | Uncond. (table) | Uncond. (MC) | given ETH ≥ +50% (table / MC) | given ETH ≥ +100% (table / MC) |
|---|---|---|---|---|
| ≥ +50% | 20.8% | 18.6% | 36.8% / 25.9% | 40.3% / 27.2% |
| ≥ 2x | 13.7% | 15.6% | 26.4% / 21.9% | 30.1% / 23.0% |
| ≥ 3x | 8.8% | 12.2% | 17.9% / 17.2% | 21.0% / 18.2% |
| ≥ 5x | 4.7% | 9.0% | 10.2% / 12.6% | 12.2% / 13.4% |
| ≥ 10x | 1.8% | 6.1% | 4.1% / 8.5% | 5.0% / 8.9% |
| ≤ −50% | 65.8% | 65.6% | 50.8% / 54.4% | 48.9% / 52.6% |
| dead (≤ −80%) | 41.3% | 48.1% | 29.6% / 36.4% | 28.6% / 34.5% |
| New ATH (2.7×) | 9.8% | 13.0% | 19.7% / 18.4% | 23.0% / 19.4% |
| EV multiple (cap 30×) | 1.39× | 2.18× | 2.54× / 2.94× | 2.91× / 3.06× |
| Prob.-weighted cap (base $115M) | $160M | $251M | $292M / $338M | $335M / $352M |
| MC median multiple | — | 0.22× | — / 0.40× | — / 0.44× |

By Robinhood Chain state (unconditional on ETH; table / MC):

| State | P | ≥ +50% | ≥ 2x | ≥ 5x | ≥ 10x | ≤ −50% | dead | New ATH | EV | MC median |
|---|---|---|---|---|---|---|---|---|---|---|
| Revival | 20% | 34% / 28% | 24% / 24% | 9% / 14% | 3% / 9% | 53% / 51% | 29% / 33% | 17.5% / 19.8% | 2.28× / 3.19× | 0.47× |
| Stable | 45% | 21% / 19% | 14% / 16% | 5% / 9% | 2% / 6% | 65% / 64% | 40% / 46% | 9.9% / 13.5% | 1.40× / 2.25× | 0.25× |
| Decay | 35% | 12% / 12% | 8% / 10% | 2% / 6% | 1% / 4% | 74% / 76% | 51% / 60% | 5.3% / 8.6% | 0.87× / 1.52× | 0.12× |

Sensitivity to the ETH blend (table, unconditional): ≥ +50% 22.0% / 20.8% / 19.2%, ≥ 2x 14.7% / 13.7% / 12.5%, ≥ 5x 5.2% / 4.7% / 4.2%, new ATH 10.6% / 9.8% / 8.9%, ≤ −50% 64.7% / 65.8% / 67.6%, dead 40.5% / 41.3% / 42.9%, EV 1.48× / 1.39× / 1.28×. The ETH view moves CASHCAT's P(≥ 2x) by only ±8% relative — less than any original token — while the chain state moves it from 8% (Decay) to 24% (Revival): **the Robinhood Chain factor matters three times more than ETH for this token**, which is the note's thesis made quantitative. Linkage table: P(≥ 2x | ETH ≤ 0%) = 9.3% vs 30.1% if ETH doubles (ratio 3.2×, the lowest of the eight).

If the $175M cap reading of 2 Oct is preferred to the $115M of 8 Oct, every probability-weighted cap scales by 1.52 ($160M → $243M unconditional, table method) and the price multiple to the ATH falls from 2.7× to ~1.8×, which would raise P(new ATH) to roughly the P(≥ 2x)–P(≥ +50%) band (14–21%); the probabilities of the fixed multiples do not change.

### 3.6 Monte Carlo note [CALC]
Per-token refit: δ = −1.35/yr, s = 3.00 (the s grid for this token runs to 4.0, so 3.00 is an interior optimum, not a bound). The idiosyncratic scale is the largest of the eight tokens: to reproduce 21% ≥ +50% *and* 66% ≤ −50% / 41% dead the MC needs a very wide shock, which with a Student-t(3) yields fatter tails than the table's Pareto extrapolation (≥ 10x 6.1% vs 1.8%; dead 48% vs 41%; EV 2.18× vs 1.39×). As in the original model the honest reading is the range: ≥ 10x ≈ 2–6%, new ATH ≈ 10–13%, dead ≈ 41–48%, EV ≈ 1.4–2.2×. The MC's conditional-on-ETH numbers are lower than the table's (P(≥ +50% | ETH ≥ +100%) 27% vs 40%) because with λ = 0.45 the MC chain contribution is only β = 0.68/0.59, whereas the table mixes in 45% of the full generic conditional — the same effect noted for the λ = 0.5 tokens in the original (s.5.3).

---

## 4. Eight-token summary (Base blend) [CALC]

### 4.1 Scenario-table method
| Token | Cap now | ATH needs | ≥ +50% | ≥ 2x | ≥ 3x | ≥ 5x | ≥ 10x | New ATH | ≤ −50% | Dead | EV | Prob.-wtd cap | ≥ 2x given chain ≥ +50% | ≥ 2x given ≥ +100% | ≥ 5x given ≥ +100% | ATH given ≥ +100% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHILLGUY | $13.0M | 53.2× | 11.9% | 7.3% | 4.4% | 2.3% | 0.8% | 0.1% | 64.3% | 39.5% | 0.93× | $12.1M | 21.4% | 26.2% | 9.0% | 0.3% |
| CHILLHOUSE | $1.5M | 19.5× | 10.5% | 6.5% | 3.9% | 2.0% | 0.8% | 0.3% | 72.5% | 48.7% | 0.81× | $1.2M | 14.3% | 16.9% | 5.8% | 0.9% |
| TROLL | $50.0M | 5.6× | 25.9% | 17.5% | 11.5% | 6.3% | 2.5% | 5.4% | 54.5% | 29.6% | 1.79× | $89.6M | 44.8% | 51.8% | 23.3% | 20.1% |
| TRIPLE T | $8.0M | 3.2× | 21.0% | 13.7% | 8.7% | 4.7% | 1.8% | 8.1% | 56.6% | 31.7% | 1.46× | $11.7M | 28.3% | 32.5% | 12.8% | 21.1% |
| CUPSEY | $6.5M | 3.2× | 14.8% | 9.4% | 5.8% | 3.0% | 1.1% | 5.3% | 63.2% | 38.0% | 1.09× | $7.1M | 20.2% | 23.5% | 8.5% | 14.3% |
| WOJAK (ETH) | $18.4M | 2.9× | 19.3% | 12.5% | 7.8% | 4.2% | 1.6% | 8.0% | 59.6% | 34.3% | 1.34× | $24.6M | 28.9% | 33.8% | 13.2% | 23.7% |
| **CASHCAT (RH)** | $115M | 2.7× | 20.8% | 13.7% | 8.8% | 4.7% | 1.8% | 9.8% | 65.8% | 41.3% | 1.39× | $160M | 26.4% | 30.1% | 12.2% | 23.0% |
| **PEPE (ETH)** | $1,750M | 6.9× | 21.8% | 13.5% | 7.6% | 3.0% | 0.7% | 1.6% | 42.5% | 12.0% | 1.22× | $2,128M | 53.7% | 67.8% | 18.6% | 9.7% |

The six original rows are identical to `risultati_probabilita.md` section 8 (verified, section 0).

### 4.2 Monte Carlo
| Token | ≥ +50% | ≥ 2x | ≥ 3x | ≥ 5x | ≥ 10x | New ATH | ≤ −50% | Dead | EV | Median | ≥ 2x given chain ≥ +50% | ≥ 2x given ≥ +100% | ≥ 5x given ≥ +100% | ATH given ≥ +100% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHILLGUY | 11.2% | 7.8% | 4.7% | 2.6% | 1.3% | 0.4% | 64.3% | 33.3% | 0.93× | 0.33× | 22.4% | 28.1% | 8.3% | 0.8% |
| CHILLHOUSE | 9.8% | 7.4% | 5.2% | 3.4% | 2.0% | 1.3% | 72.2% | 45.7% | 1.02× | 0.23× | 13.1% | 14.7% | 6.0% | 2.2% |
| TROLL | 23.7% | 19.3% | 14.3% | 9.7% | 5.9% | 8.9% | 53.9% | 33.0% | 2.30× | 0.42× | 38.4% | 43.8% | 22.4% | 20.5% |
| TRIPLE T | 19.3% | 15.2% | 10.9% | 7.1% | 4.3% | 10.4% | 56.1% | 31.8% | 1.83× | 0.40× | 25.2% | 27.8% | 12.9% | 19.0% |
| CUPSEY | 13.7% | 10.4% | 7.1% | 4.5% | 2.6% | 6.6% | 62.9% | 35.1% | 1.30× | 0.33× | 18.5% | 20.6% | 8.2% | 12.9% |
| WOJAK (ETH) | 17.7% | 13.9% | 9.8% | 6.5% | 3.9% | 10.0% | 59.0% | 34.2% | 1.69× | 0.36× | 25.4% | 28.2% | 13.0% | 20.5% |
| **CASHCAT (RH)** | 18.6% | 15.6% | 12.2% | 9.0% | 6.1% | 13.0% | 65.6% | 48.1% | 2.18× | 0.22× | 21.9% | 23.0% | 13.4% | 19.4% |
| **PEPE (ETH)** | 20.4% | 15.2% | 9.4% | 4.4% | 1.4% | 2.6% | 43.2% | 10.4% | 1.32× | 0.58× | 60.7% | 78.2% | 26.7% | 14.8% |

### 4.3 Probability-weighted market caps (current cap × EV, table method; MC in parentheses)
CHILLGUY $12.1M (12.1) · CHILLHOUSE $1.2M (1.5) · TROLL $89.6M (115.2) · TRIPLE T $11.7M (14.7) · CUPSEY $7.1M (8.4) · WOJAK $24.6M (31.0) · **CASHCAT $160M (251)** on the $115M base ($243M–$381M on the $175M base) · **PEPE $2.13B (2.32B)**. Given the chain doubles: CASHCAT $335M (352), PEPE $6.6B (8.0B). As in the original, EV is driven by the 30× cap and the tail assumption; quote as orders of magnitude.

---

## 5. Plain-language explanation: why the two new tokens' numbers come out the way they do

**PEPE** ends up with roughly the *same headline upside* as the small tokens (about 1 chance in 5 of being up ≥ 50% in a year, 1 in 7 of doubling) but a *much better downside* (4 in 10 to lose half, 1 in 8 to lose 80%, versus 6 in 10 and 1 in 3 for the typical small meme), a *much worse far tail* (3% for a 5×, under 1% for a 10×, under 2% for a new ATH that is 6.9× away) and a *median that is a loss but not a wipe-out* (MC median 0.58× vs 0.22–0.42× for the others). The reasons: (1) it is ~100× bigger than the other tokens, so a 5× is a return to its all-time record cap and a 10× would be the largest memecoin ever after DOGE — the lottery ticket is gone, as the fall of its ETH beta from ~18× in 2024 to ~1.5× in 2026 shows; (2) it has survived a −79% year with 593K holders still growing, Binance/Coinbase/Kraken/Robinhood listings and a $323M perp book, so a −80% from here — a $350M cap, below anything since January 2024 — needs a genuine ETH crash plus a liquidation cascade; (3) it tracks ETH more than any other token (λ = 1.1): if ETH doubles PEPE has roughly a 2-in-3 chance (table) to 4-in-5 (MC) of doubling and an 85–88% chance of being up ≥ 50%, but if ETH ends the year flat or down its chance of doubling is 1%. PEPE is therefore not a "memecoin bet" in the sense of the other seven; it is a leveraged ETH bet with an ETF option attached. The ETF is the one binary: approval is the only identified catalyst that could move PEPE independently of ETH, and it is modelled only as a mild tilt (+15% upside odds, +5% downside odds) because the note finds no basis to put a probability on SEC effectiveness.

**CASHCAT** comes out as the *highest-variance* token in the set: about 1 in 5 to be up ≥ 50%, 1 in 7 to double, 1 in 10 to make a new high (only 2.7× away, the closest ATH after WOJAK's 2.9×), but 2 in 3 to lose half and roughly 4–5 in 10 to be effectively dead; its MC median (0.22×) is the worst of the eight, and its EV (1.4–2.2×) the second highest after TROLL. The reasons: (1) it is a current-cycle token three months old, −63% from a high set six weeks ago, with the Robinhood app listing as a real distribution edge no other chain meme has — the youth and the ladder push the upside odds up (×1.23); (2) 89% of supply in 1,000 wallets, a 13.7% wallet nobody can identify, $2.6–5.4M of liquidity for a $115M cap, a perp market that already produced a −60% minute, a hack-driven dump and a chain that is 14 weeks old with one sequencer and 7-day exits push the downside odds up more (×1.38); (3) only 45% of its fate is tied to ETH; the rest is the generic memecoin decay path plus the Robinhood Chain factor. That factor is what the probabilities hinge on: in the Revival state (1 in 5) CASHCAT has a 1-in-4 chance of doubling and 17–20% of a new ATH; in the Decay state (1 in 3) it has 8–10% and 5–9%, and a 51–60% chance of being dead. Readers who believe Robinhood will keep pushing its chain (HOOD earnings 27 Oct, the $15B stock-token business, Tenev's "works great for memes too") should mentally move toward the Revival row; readers who read fees −97%, Noxa's disappearance and the subsidy's end as the end of the mania should move toward Decay. The ETH view barely matters for this token (±8% relative on P(≥ 2x) across the three blends).

**How they compare with the six originals.** On P(≥ 2x) the eight tokens now rank TROLL 17.5% > TRIPLE T 13.7% ≈ CASHCAT 13.7% ≈ PEPE 13.5% > WOJAK 12.5% > CUPSEY 9.4% > CHILLGUY 7.3% > CHILLHOUSE 6.5% (table method). On P(dead) PEPE 12% is in a class of its own; CASHCAT 41% sits between CHILLGUY (40%) and CHILLHOUSE (49%). On "what a rally buys": PEPE is the extreme rally play (×70 between no-rally and rally), CASHCAT the extreme attention play (×3.2). For every token except PEPE the single most likely outcome remains losing at least half.

---

## 6. Caveats specific to the two new tokens (carry into the report, together with the original caveats 1–10)

1. **CASHCAT data conflicts.** Holder count 41K (DEXTools, Aug) vs > 61K (Arkham, Jul) vs 112.6K (GeckoTerminal, undated) — a 2.7× spread; the model uses the range only qualitatively (the holders/liquidity factor is 1.05/1.10). ATH market cap $226M / $235.8M / $254M / ~$311M depending on provider and supply method; the model uses the price ATH ($0.3115 → 2.7×); on the $254M cap figure the multiple would be 2.2×. Current cap $115M (8 Oct, from a low-reliability press release) vs $168–175M (1–2 Oct, CoinGecko/CoinCodex): the base is $115M and the range is stated; probability-weighted caps scale linearly. Contract verification status, deployer, top-10 breakdown and contract ownership are unknown [CASHCAT-KQ1, KQ2, KQ3, KQ5]. No price after 8 Oct was found.
2. **The chain is three months old.** Robinhood Chain went live on 1 July 2026; every base rate in the model (Coin Metrics decay statistics, the generic table) comes from Solana/Ethereum memecoins, not from a chain that has existed for one quarter. The Robinhood Chain factor (20/45/35, ×2.0/0.6, ×0.5/1.6, ±0.70 log-shift) is the modeller's assumption, anchored on the activity statistics in [CASHCAT-KQ6] and on the size of the token's own event-driven moves [CASHCAT-KQ3]; a different modeller could reasonably use 30/40/30 or 10/40/50. The gas-subsidy end (29 Sep) is contradicted by one report of an extension to 31 Dec [CASHCAT-KQ6]. Chain-level discrete risks (sequencer outage, upgrade-key misuse, bridge/7-day-exit problems, Robinhood deprioritising memes under regulatory pressure) are only approximated by the 0.90/1.15 chain-risk multiplier.
3. **PEPE ETF binary.** The Canary spot PEPE ETF (S-1/A 2 Oct 2026) may become effective, be delayed indefinitely or be withdrawn; no prediction-market odds exist [PEPE-Q3, Q7]. The model encodes it as a mild symmetric tilt, not as a scenario. If approval were, say, 50% likely and worth a one-off +30–50% (the DOGE ETF's experience — AUM $13.7M, NAV −29% YTD — argues against a large permanent effect [BASE-KQ5]), the P(≥ +50%) figures would move by a few points, not tens of points.
4. **PEPE price readings disagree** on 2–3 Oct (Crypto Times $0.0000054 vs CoinGabbar $0.000004253; Etherscan's on-chain cap implies ~$0.0000045); the model uses the 10–13 Oct consensus ($0.0000041), and the drawdown/multiples would shift by ±10% with the other readings [PEPE-Q1]. DEX liquidity for PEPE was not found; concentration is 41% or 77% depending on whether exchange wallets are counted [PEPE-Q1, Q4].
5. **The PEPE conditional table is a second judgmental table**, built on one note's back-of-envelope betas (no formal regression exists: "all ratios are back-of-envelope from price points" [PEPE-Q6]). λ > 1 extrapolates the table beyond its rows by 10%; the floor of the clipping binds in the A row (upside cells), for B/≥ 10x and for E/dead (all set to 0.05%), and the amplification itself is an assumption.
6. **Both notes are built from search-engine snippets**, with every direct page fetch blocked [cashcat.md and pepe.md method notes]; prices and caps are 1–8 Oct (CASHCAT) and 10–13 Oct (PEPE) snapshots, not 8 Oct 2026 quotes, and several sources are promotional (press releases, prediction sites) and are flagged as such in the notes.
7. **Monte Carlo tails.** CASHCAT needs the widest idiosyncratic shock of the set (s = 3.0), so its MC ≥ 10x (6.1%), new-ATH (13%) and dead (48%) figures are more tail-assumption-dependent than any other token's; PEPE's MC, with the smallest shock (s = 0.85), is close to a pure beta play and its conditional figures exceed the table's. Quote the table/MC pairs as ranges.
8. **Nothing here is financial advice.** CASHCAT is a zero-utility, anonymous, three-month-old token on a three-month-old chain; PEPE is a zero-utility token whose entire upside in this model is ETH's. A total loss is a plausible outcome for CASHCAT in every scenario; for PEPE a −80% is a one-in-eight outcome in the Base case.

---

## 7. Verification statement

Running `python3 -I model_probabilita_8.py` from this folder on 13 Oct 2026 produced `output_modello_8.txt`, `risultati_probabilita_8.md` and `risultati_probabilita_8.csv`. Section 12 of the output compares the script's rows for the SOL scenario distribution, the generic conditional table and the six original tokens with `../Probabilità rialzo memecoin Solana 2027/risultati_probabilita.csv`: 1,154 numeric cells, 0 rows missing, maximum absolute difference 0.000000. The six original tokens' Base results (and their Ottimistico/Pessimistico sensitivity rows, conditional columns, scenario-by-scenario rows and EVs) are therefore unchanged versus `risultati_probabilita.md`; the generic MC calibration (β_up 1.5, β_dn 1.3, δ −0.80, s 1.60, SSE 0.0037) and the per-token MC parameters of the six are also identical to the original output.
