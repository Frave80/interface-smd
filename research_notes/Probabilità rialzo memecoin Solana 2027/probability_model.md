# Probability model: 12-month upside of six memecoins conditional on a SOL / ETH rally (8 Oct 2026 -> 8 Oct 2027)

Model date: 9 October 2026. Author: research agent (no web access; all inputs come from the notes listed below).
Files in this folder:
- `model_probabilita.py` — the full model (Python 3, numpy only). Run from this folder with `python3 -I model_probabilita.py` (~40 s).
- `risultati_probabilita.md` — all result tables (markdown), written by the script.
- `risultati_probabilita.csv` — the same results as machine-readable rows (column legend in the first lines).
- `output_modello.txt` — the verbatim console output of the run documented here (also appended at the end of this file, section 8).
- `probability_model.md` — this file: every assumption, formula, weight, result and caveat.

Input notes (cited below as [SOL-Qn], [BASE-KQn], [TOKEN], [OUTLOOK-KQn], [REPORT]):
- [SOL-Qn] `sol_probability_inputs.md` (this folder), questions Q1–Q6.
- [BASE-KQn] `memecoin_base_rates.md` (this folder), key questions KQ1–KQ6.
- [CHILLGUY], [CHILLHOUSE], [TROLL] `../Memecoin Solana Chillguy Chillhouse Troll/{chillguy,chillhouse,troll}.md`.
- [OUTLOOK-KQn] `../Memecoin Solana Chillguy Chillhouse Troll/solana_altcoin_outlook.md`.
- [TRIPLET], [CUPSEY] `../Memecoin Solana Wojak Triple T Cupsey/{triple_t,cupsey}.md`.
- [WOJAK] `../Memecoin Solana con Wojak Ethereum/wojak_ethereum.md`.
- [REPORT] `/home/user/interface-smd/reports/Memecoin Solana con Wojak Ethereum.md` (rally-scenario table and per-coin strengths/weaknesses).

What this model is: a transparent bookkeeping exercise that turns the evidence in the notes into numbers, so that the report can say "roughly X% chance of Y" with a visible derivation. What it is not: a forecast. The data behind it are search-engine snippets, small samples and judgmental estimates (see section 7). Nothing here is financial advice.

Label convention: **[NOTE]** = number taken from a note; **[ASSUMPTION]** = number chosen by the modeller and justified in words; **[CALC]** = computed by the script.

---

## 0. Structure of the model in one paragraph

1. Build a probability distribution for the SOL price on 8 Oct 2027 in five scenarios (Crollo, Ribasso, Laterale, Rialzo forte, Euforia) by blending four sources with explicit weights.
2. For each SOL scenario, state the probability that a *generic established* memecoin (not a new launch) reaches each outcome (≥ +50%, ≥ 2x, ≥ 3x, ≥ 5x, ≥ 10x, ≤ −50%, ≤ −80%) over the same 12 months, anchored on the empirical base rates.
3. Adjust the generic probabilities for each of the six tokens with a small set of bounded, documented odds multipliers (cycle age, drawdown, holders/liquidity, CEX ladder, catalysts, concentration, IP) and a "linkage" parameter that says how much the token actually follows the chain.
4. Combine 1 × 3 to obtain unconditional probabilities, probabilities conditional on SOL ≥ +50% and ≥ +100%, the probability of a new ATH, the expected multiple and the probability-weighted market cap.
5. Cross-check with a 100,000-path Monte Carlo (chain return + idiosyncratic heavy-tailed shock) calibrated to the same tables.
WOJAK is run through the identical pipeline with ETH in place of SOL.

---

## 1. SOL 12-month scenario distribution

### 1.1 Inputs
- Spot S0 = **$110** [NOTE, SOL-Q1: $109.5–110.5 on 8–9 Oct 2026]. ATH = **$294.85** [NOTE, SOL-Q1].
- Volatility σ = **55%** [NOTE, SOL-Q1/Q2: 30-day realized 57.6%, 1-month ATM implied 53.2%; the notes' lognormal table uses 55% and a 70% stress case].
- Horizon T = 1 year (8 Oct 2026 → 8 Oct 2027).

### 1.2 Scenario definitions (price on 8 Oct 2027)
| Code | Scenario | Price | Return from $110 |
|---|---|---|---|
| A | Crollo | < $70 | worse than −36% |
| B | Ribasso | $70–110 | −36% to 0% |
| C | Laterale / moderato | $110–150 | 0% to +36% |
| D | Rialzo forte | $150–250 | +36% to +127% |
| E | Euforia | > $250 | more than +127% (ATH $294.85 is inside E) |

Internally the script uses seven finer buckets (<70, 70–110, 110–150, 150–165, 165–220, 220–250, >250) so that the thresholds "SOL ≥ +50%" (= $165) and "SOL ≥ +100%" (= $220) are exact; the five display scenarios are sums of the fine buckets.

### 1.3 The four component distributions

**(a) Lognormal / implied-vol view** [CALC from NOTE]. P(S_T > K) = N(d2), d2 = [ln(S0/K) + (μ − σ²/2)·T] / (σ√T), with μ = 0 (zero price drift, as in the notes' table) and σ = 55%. This reproduces the notes' figures (P(>$150) = 20%, P(>$200) = 8.7%, P(>$250) = 3.9%, P(>$100) = 46%) [SOL-Q2]. Result: A 29.2%, B 31.6%, C 19.1%, D 16.2%, E 3.9%. The 70% stress case is shown alongside (E = 6.4%).

**(b) Prediction-market view** [CALC from NOTE]. The only market data are the Kalshi year-end-2026 close ladder captured in late Sep 2026 with SOL ≈ $121: P(≥$100) = 71%, P(≥$150) = 34%, P(≥$200) = 27% [SOL-Q3]. No 2027 markets exist [SOL-Q3 Gaps]. Method: (i) fit a lognormal with free drift μ_b and vol σ_b to those three points over T_k = 0.26 y (late Sep → 1 Jan 2027) by grid search; the fit is μ_b = +0.90/yr, σ_b = 110% (SSE 0.0068; it reproduces 68%/40%/22%). The ladder cannot be matched by a 55%-vol lognormal at all (with zero drift the maximum achievable P(≥$150) in 3 months from $121 is ~26%) — this is the long-shot bias and thin liquidity ($183K volume) the notes describe [SOL-Q3 Inferences]. (ii) Because the market only covers the next quarter, the fitted (μ_b, σ_b) are applied for 0.26 y and the implied-vol lognormal (a) for the remaining 0.74 y; the sum of two normal log-returns is normal, so component (b) is a lognormal with effective 12-month vol 73% and mean log-return −0.035 [CALC]. Result: A 28.5%, B 23.4%, C 16.2%, D 19.8%, E 12.2%. Interpretation: the market view fattens both tails relative to (a), mostly the upper one.

**(c) Historical 12-month base rates** [NOTE, SOL-Q4 "MY CALC": approximate monthly series Jan 2021–Sep 2026, 57 rolling windows]: P(>0%) = 49%, P(>+50%) = 33%, P(>+100%) = 31% (32% full sample; the 31% "from Jan 2022" value is used), P(>+200%) = 28%, P(<−50%) = 25%. The survival function F(r) = P(return > r) is linearly interpolated between these points [ASSUMPTION: linear interpolation]; e.g. P(return < −36%) = 25% + (14/50)·(51% − 25%) = 32.3%; P(return > +127%) = 31% − (27/100)·(31% − 28%) = 30.2%. Result: A 32.1%, B 18.9%, C 11.6%, D 7.2%, E 30.2%. This distribution is extremely bimodal because the sample contains the 2021 and 2023 years (+917% in 2023); the notes say "treat with caution" and point out that today's vol (56%) is roughly half the 2021–2025 regime, which argues for a compressed version [SOL-Q4]. Caution is implemented through the blend weight (20% in the Base case, 10% in the pessimistic case), not by modifying the numbers.

**(d) Macro tilt** [ASSUMPTION encoding NOTE facts]. Current facts in [SOL-Q6]: Fed hiked on 16 Sep 2026 with another hike pencilled in and no 2027 cuts in the dots (futures ~4.6% end-2027); CLARITY Act cloture failed 15 Sep 2026; BTC ETF −$487M on 7 Oct and SOL ETF outflows 5–7 Oct; Solana network revenue −87% y/y; DAT companies at 0.3–0.5× mNAV; the put-biased option skew (RR25 ≈ −0.9) [SOL-Q1]. Offsetting but conditional: Grayscale/Coinbase "bottom is in", SOL ETF 12-week streak, Alpenglow, possible 2027 cuts. The notes' own conclusion is that "bearish drivers are current facts; bullish drivers are forecasts/conditional". This is encoded as a **negative price drift of −15%/yr** on the 55%-vol lognormal in the Base case (sensitivity: −25%/yr with 60% vol in the pessimistic case; 0% in the optimistic case). Result (−15%): A 39.2%, B 31.6%, C 15.9%, D 11.3%, E 2.1%.

### 1.4 Weights and blends [ASSUMPTION]
| Blend | w(a) lognormal | w(b) prediction markets | w(c) historical | w(d) macro | macro drift / vol |
|---|---|---|---|---|---|
| Ottimistico | 0.30 | 0.30 | 0.30 | 0.10 | 0% / 55% |
| **Base** | **0.35** | **0.20** | **0.20** | **0.25** | **−15% / 55%** |
| Pessimistico | 0.30 | 0.10 | 0.10 | 0.50 | −25% / 60% |

Rationale for the Base weights: the option-implied lognormal is "the more disciplined source" [SOL-Q3] and gets the largest weight; prediction markets and history are each informative about tail fatness but are small-sample / biased, so 20% each; the macro tilt gets 25% because the notes rank the rate regime as "the single most important bearish input" [SOL-Q6].

### 1.5 Result: SOL scenario probabilities [CALC]
| Scenario | Ottimistico | **Base** | Pessimistico |
|---|---|---|---|
| A Crollo (<$70) | 29.9% | **32.1%** | 39.1% |
| B Ribasso ($70–110) | 25.3% | **27.4%** | 27.6% |
| C Laterale ($110–150) | 16.0% | **16.2%** | 14.9% |
| D Rialzo forte ($150–250) | 14.6% | **13.9%** | 12.1% |
| E Euforia (>$250) | 14.2% | **10.3%** | 6.3% |
| P(SOL ≥ +50%, ≥ $165) | 24.4% | **20.0%** | 14.8% |
| P(SOL ≥ +100%, ≥ $220) | 16.6% | **12.5%** | 8.1% |
| P(SOL ≥ ATH $294.85) | 7.1% | **5.2%** | 3.2% |

P(≥ ATH) = P(>250) × (share of the >250 bucket that lies above $294.85 under the 55% lognormal) [CALC]. Cross-checks: Polymarket priced a new SOL ATH by end-2026 at 3–9% in mid-2026 [SOL-Q3]; the 5% figure for a 12-month horizon is in the same range. The Base distribution says: roughly 6 chances in 10 that SOL is lower in a year, 1 in 5 that it is up ≥ 50%, 1 in 8 that it doubles.

### 1.6 Probability that SOL *touches* a level at any time in the window [CALC]
| Level | Notes' method (2 × terminal prob., 55% vol, driftless) [SOL-Q2] | MC daily paths, driftless 55% | MC daily paths with the single lognormal best-fitting the Base blend (drift +10%, vol 69%) — upper sensitivity |
|---|---|---|---|
| $150 | 40% | 46% | 56% |
| $200 | 17% | 19% | 30% |
| $250 | 8% | 8% | 17% |
| $300 | 4% | 4% | 10% |

The first two columns are the figures to quote (they correspond to the notes); the daily-path simulation is slightly above the reflection shortcut because the shortcut assumes continuous monitoring with an exact −σ²/2 drift. The third column shows how much fatter the touch odds become if one believes the full Base blend (which includes the prediction-market and historical tails).

### 1.7 ETH distribution for WOJAK [ASSUMPTION + CALC]
Same return buckets applied to ETH spot $2,600 [NOTE, WOJAK §9: $2,694 on 29 Sep, $2,547 on 7 Oct 2026] → <$1,655 / $1,655–2,600 / $2,600–3,545 / $3,545–5,909 / >$5,909 (ETH ATH ≈ $4,950, Aug 2025 [WOJAK §9], lies inside D). ETH vol = **50%** [ASSUMPTION: no ETH vol in the notes; set slightly below SOL's 55% because ETH is the larger asset]. Components (a) and (d) are recomputed for ETH; (b) and (c) are SOL-specific and are reused as an "altcoin proxy" [ASSUMPTION, caveat]. Base result: A 30.2%, B 29.1%, C 17.1%, D 13.8%, E 9.8%; P(ETH ≥ +50%) = 19.3%, P(ETH ≥ +100%) = 11.9%.

---

## 2. Conditional response of a GENERIC established memecoin

Outcome definitions (price multiple m over 12 months): ≥ +50% (m ≥ 1.5), ≥ 2x, ≥ 3x, ≥ 5x, ≥ 10x, ≤ −50% (m ≤ 0.5), "effectively dead" (m ≤ 0.2, i.e. worse than −80%). "Liquidity collapse" is not modelled separately; it is folded into the per-token downside multipliers (section 3).

### 2.1 Evidence used
- E1. Of 150 CEX-priced Solana memecoins launched since Dec 2023, 81% drew down ≥ 90% from ATH, only 3.3% ever reclaimed ATH, two-thirds never had a second rally at all; median 370 days from peak to −95% ("recovery essentially does not happen") [BASE-KQ3, Coin Metrics Oct 2026]. The sample is survivor-biased (CEX-priced), so the broad universe is harsher.
- E2. Equal-weight top-10 meme basket −78.7% from Jan 2025 to Feb 2026 vs BTC −30.7% (downside amplification ≈ 2.5×); 2025 memecoin cap −65% [BASE-KQ1, KQ3].
- E3. Q3 2026: SOL +38–60% while the Solana meme category moved from ~$3.7B to ~$3.3–3.9B (−11% to +6%); upside concentrated in brand-new tokens (ZCAT) [BASE-KQ1 Window D; OUTLOOK-KQ5]. Established memes posted only ~20% weekly spikes [OUTLOOK-KQ5].
- E4. 2025 windows (SOL +24% Q2, +35% Q3): big memes rallied for days/weeks (BONK +70% in July 2025) but ended far below SOL on a multi-month basis (BONK −41% from July peak by 9 Aug, WIF −75% YTD) [BASE-KQ1 Window C].
- E5. 2024 windows: established memes delivered 2–4× SOL's move (Nov 2024: SOL +43%, BONK +175%, WIF +98%; POPCAT and BONK set new ATHs); Dec 2023: BONK +572% in the month vs SOL +25–30% [OUTLOOK-KQ5; BASE-KQ1 Windows A–B]. "In 2024-type windows most (likely >70%) of established memes rose and the median beat SOL" [BASE-KQ1 Inferences].
- E6. Replacement, not recovery: DOGE/SHIB never reclaimed 2021 highs in 2024; the Solana class of 2024 stayed 80–97% below its highs through the 2025–26 bounces; realistic relief rallies for dead prior-cycle memes were 2–3× (CHILLGUY 2.4× Apr→mid-2025, MOODENG 3.5×, TROLL 2.6×) [OUTLOOK-KQ6].
- E7. Listings: +10% to +80% in 1–2 days, negative on average at 3–6 months (Binance 7-year dataset −22.7% at 3 months, −37.6% at 6 months); a trading catalyst, not a 12-month driver [BASE-KQ5].
- E8. Memecoin beta is high (>1) over days/weeks but with low R²; the idiosyncratic component dominates over months; the SOL↔meme feedback loop is structurally weaker in 2026 (meme share of Solana volume 40%→16%, hold times 300 s→58 s) [BASE-KQ2].

### 2.2 The table [ASSUMPTION, every cell is an estimate]
| SOL scenario | ≥ +50% | ≥ 2x | ≥ 3x | ≥ 5x | ≥ 10x | ≤ −50% | ≤ −80% (dead) |
|---|---|---|---|---|---|---|---|
| A Crollo (< −36%) | 3% | 1.5% | 0.8% | 0.3% | 0.1% | 85% | 55% |
| B Ribasso (−36% to 0) | 8% | 4% | 2.2% | 1% | 0.3% | 65% | 35% |
| C Laterale (0 to +36%) | 18% | 10% | 5.5% | 2.5% | 0.8% | 45% | 20% |
| D Rialzo forte (+36% to +127%) | 40% | 25% | 15% | 8% | 3% | 28% | 12% |
| E Euforia (> +127%) | 65% | 50% | 35% | 20% | 8% | 15% | 6% |
| **Unconditional (Base SOL blend)** [CALC] | **18.3%** | **11.8%** | **7.5%** | **4.0%** | **1.5%** | **57.9%** | **32.8%** |

Row-by-row reasoning:
- **A (Crollo).** With SOL down more than a third, the 2–2.5× downside amplification (E2) puts the modal meme at −70% to −90%: ≤ −50% at 85% and dead at 55%. Upside is residual (3% ≥ +50%): only an idiosyncratic viral event can beat a crashing chain (E8).
- **B (Ribasso).** SOL flat-to-down. The 2025 experience (E2, E4) and the 370-day decay path (E1) make ≤ −50% the base case (65%); a third die. 8% ≥ +50% allows for attention-driven spikes that survive the year.
- **C (Laterale).** SOL up 0–36%. This is the 2025 Q2–Q3 and Q3 2026 regime (E3, E4): memes rally briefly, give it back, category flat. ≥ +50% at 18%, ≥ 2x at 10%; still 45% ≤ −50% because the sector's drift is negative even when SOL rises.
- **D (Rialzo forte).** SOL +36% to +127%. Halfway between the 2024 response (E5: most established memes up, median beat SOL) and the 2025–26 response (E3–E4: beta ≈ 0–1 and replacement by new launches). 40% ≥ +50%, 25% ≥ 2x, 8% ≥ 5x; 28% still lose half (E6: prior-cycle names often do not participate).
- **E (Euforia).** SOL more than doubles (ATH regained). Closest analogues are Dec 2023 and Nov 2024 (E5): >70% of established memes rose and the median beat SOL, so 65% ≥ +50% and 50% ≥ 2x; 20% ≥ 5x and 8% ≥ 10x reflect that the 10×+ outcomes in those windows went to the one or two leaders (BONK 2023) and to new launches. Even in euphoria 15% lose half (E6: DOGE/SHIB-type laggards, 2024 class in 2025).
- Monotonicity across columns and rows is imposed by construction.

**Sanity checks [CALC].** Unconditional ≥ 2x = 11.8% is consistent with "two-thirds never have a second rally" over multi-year horizons (E1) scaled to one year. Implied P(reclaim ATH) for a generic token whose ATH is 5× / 10× / 20× away = 4.0% / 1.5% / 0.6% (section 4.2 method), bracketing Coin Metrics' 3.3% multi-year reclaim rate (E1). Unconditional ≤ −50% = 58% and dead = 33% sit between the 2025 sector (−65% cap) and the 2026 stabilisation.

---

## 3. Per-token adjustments

### 3.1 Linkage to the chain, λ [ASSUMPTION]
Each token's scenario-conditional probabilities are a mixture: p_token(s) = λ·p_table(s) + (1 − λ)·p_table(unconditional). λ = 1 means the token follows the SOL scenario fully; λ = 0 means its outcome is independent of SOL. Evidence: TRIPLE T +920% Apr→Jul 2026 with SOL flat, then −72% while SOL +35–40% [TRIPLET KQ7]; CUPSEY +6,500% Jun→Aug 2026 then −70% while SOL rose to $113–121 [CUPSEY Q7]; WOJAK 7.5× Feb→Jun 2026 with ETH falling, then −65% while ETH +70% [WOJAK §9]; CHILLHOUSE's moves were "stunt-driven rather than beta to SOL" [CHILLHOUSE KQ8]; CHILLGUY is perp-traded on Binance and its 2026 moves were attributed to macro sentiment ("no coin-specific catalyst") [CHILLGUY KQ1]; TROLL's spikes coincided with Solana-meme rotations and listings, "better modelled as a Solana-meme-sector beta play than as leveraged SOL" [TROLL KQ8].
| Token | λ | Reason |
|---|---|---|
| CHILLGUY | 0.8 | Binance perp, macro-driven 2026 moves, 118K holders = sector proxy |
| TROLL | 0.8 | moved with Solana-meme rotations (May 2026) and listings |
| WOJAK | 0.6 | ETH cult-coin basket member but 2026 run was contra-ETH |
| CHILLHOUSE | 0.5 | stunt-driven; no 2026 activity |
| TRIPLE T | 0.5 | own attention cycle, negatively correlated with SOL in Q3 2026 |
| CUPSEY | 0.5 | own narrative cycle (July 2026 campaign), weak SOL link |

### 3.2 Odds multipliers [ASSUMPTION, each justified by a note]
Each factor multiplies the *odds* p/(1−p) of the upside outcomes (≥ +50% … ≥ 10x) by M_up and of the downside outcomes (≤ −50%, dead) by M_dn. The product over factors is clipped to **[0.5, 2.0]**. Multiplying odds (rather than probabilities) keeps every number between 0 and 1 and preserves the ordering ≥ 10x ≤ ≥ 5x ≤ … ≤ ≥ +50%. A final consistency rule keeps P(≥ +50%) + P(≤ −50%) ≤ 98%.

**CHILLGUY** (price $0.0125, ATH $0.665 → ATH needs 53×; cap $13M [CHILLGUY KQ1–2])
| Factor | up | down | Source |
|---|---|---|---|
| cycle age: 2024-cycle, ATH 27 Nov 2024, "one-cycle meme" | 0.70 | 1.15 | [CHILLGUY KQ2]; E6 |
| drawdown −98%: decay phase | 0.85 | 1.10 | [CHILLGUY KQ2]; E1 |
| 118K holders, $1.2M Raydium liquidity, $3–5M CEX volume | 1.10 | 0.90 | [CHILLGUY KQ1] |
| Binance Futures perp (75×) + Bybit/KuCoin/Bitget/Gate/MEXC spot, but perp in Binance's 2026 delisting size band | 1.15 | 1.10 | [CHILLGUY KQ3] |
| catalysts: none found in 2026 | 0.90 | 1.00 | [CHILLGUY KQ2, KQ5] |
| concentration: >20% bundled single entity, top-10 52% | 0.90 | 1.10 | [CHILLGUY KQ4] |
| IP: Banks copyright claim, dormant 22 months | 0.90 | 1.00 | [CHILLGUY KQ5] |
| **product → applied** | **0.55 → 0.55** | **1.38 → 1.38** | |

**CHILLHOUSE** (price $0.0015, ATH $0.02919 → 19.5×; cap $1.5M [CHILLHOUSE KQ2–3])
| Factor | up | down | Source |
|---|---|---|---|
| cycle age: 2025 stunts, ATH 28 Oct 2025 | 0.70 | 1.15 | [CHILLHOUSE KQ3] |
| drawdown −95% | 0.85 | 1.10 | [CHILLHOUSE KQ2] |
| 19K holders, $0.4M liquidity, ~$20K/day DEX volume | 0.80 | 1.30 | [CHILLHOUSE KQ2] |
| Kraken + MEXC (Innovation Zone), CoinEx shutting down | 1.00 | 1.00 | [CHILLHOUSE KQ4] |
| catalysts: no third-party coverage or team activity since 29 Oct 2025 | 0.60 | 1.20 | [CHILLHOUSE KQ6] |
| concentration: bundles flagged, unverified; LP status unknown | 0.95 | 1.10 | [CHILLHOUSE KQ5] |
| IP: uses the Chill Guy image (Banks) | 0.90 | 1.00 | [CHILLHOUSE KQ1, KQ7] |
| **product → applied** | **0.24 → 0.50 (floor)** | **2.17 → 2.00 (cap)** | |

**TROLL** (price $0.050, ATH $0.282 → 5.6×; cap $50M [TROLL KQ2–3])
| Factor | up | down | Source |
|---|---|---|---|
| cycle age: ATH Aug 2025 but a 2026 cycle of its own (May 2026 peak ~$117M) | 1.00 | 1.00 | [TROLL KQ3] |
| drawdown −82% | 0.95 | 1.05 | [TROLL KQ2] |
| 65–70K holders (+35–45% in 2026), liquidity $1.7–3.9M | 1.15 | 0.90 | [TROLL KQ2] |
| CEX ladder: Coinbase (Sep 2025), Binance.US (Jan 2026), KuCoin, MEXC perp, "Binance Alpha" tag | 1.25 | 0.90 | [TROLL KQ4] |
| catalysts: airdrop campaign 1 Sep 2026; Binance global spot/futures not yet listed (optionality); exclusive IP licence helps listings | 1.20 | 1.00 | [TROLL KQ3, KQ4, KQ6] |
| concentration: 10 whales funded the licence, Ramirez's bag, only promotional top-10 figure | 0.95 | 1.05 | [TROLL KQ5] |
| IP: exclusive worldwide Trollface licence (Sep 2025) | 1.10 | 0.95 | [TROLL KQ1] |
| **product → applied** | **1.71 → 1.71** | **0.85 → 0.85** | |

**TRIPLE T** (price $0.0085, ATH $0.027 → 3.2×; cap $8M [TRIPLET KQ2–3])
| Factor | up | down | Source |
|---|---|---|---|
| cycle age: launched Feb 2026, ATH 23 Jul 2026 | 1.10 | 0.95 | [TRIPLET KQ1, KQ3] |
| drawdown −70% (two pump/dump cycles) | 1.00 | 1.00 | [TRIPLET KQ3] |
| 22–25K holders rising through the drawdown, $0.7M liquidity | 1.00 | 1.00 | [TRIPLET KQ2] |
| CEX ladder: BitMart spot + MEXC perp only; no tier-1 or Alpha | 0.90 | 1.05 | [TRIPLET KQ4] |
| catalysts: Ramadan 2027 (~Feb 2027) for a sahur meme; brainrot meta still spawning clones | 1.15 | 1.00 | [TRIPLET KQ6, KQ8] |
| concentration: top-10 16.3%, mint/freeze revoked, LP burned | 1.05 | 0.95 | [TRIPLET KQ5] |
| IP: public-domain AI character | 1.00 | 1.00 | [TRIPLET KQ1] |
| **product → applied** | **1.20 → 1.20** | **0.95 → 0.95** | |

**CUPSEY** (price $0.0065, ATH $0.021 → 3.2×; cap $6.5M [CUPSEY Q2–3])
| Factor | up | down | Source |
|---|---|---|---|
| cycle age: relaunched contract Jan 2026, ATH 21–22 Aug 2026 | 1.10 | 0.95 | [CUPSEY Q1, Q3] |
| drawdown −70%, blow-off top, 30-day momentum negative | 1.00 | 1.00 | [CUPSEY Q3] |
| 15K holders, $0.5M liquidity | 0.95 | 1.05 | [CUPSEY Q2] |
| CEX ladder: Gate pilot, MEXC Meme+, WEEX, Bitrue Alpha, KCEX (second tier) | 0.90 | 1.05 | [CUPSEY Q4] |
| catalysts: pump.fun mascot / IP / airdrop claims, none verified | 1.00 | 1.00 | [CUPSEY Q1, Q6] |
| concentration: project wallet 16.8%, 8% to KOLs, nothing locked, prior migration | 0.85 | 1.15 | [CUPSEY Q5] |
| IP/reputation: unowned brand, trader not involved, phishing "airdrop" scams | 0.95 | 1.05 | [CUPSEY Q5, Q6] |
| **product → applied** | **0.76 → 0.76** | **1.26 → 1.26** | |

**WOJAK (Ethereum)** (price $0.0000000592, ATH $0.000000174 → 2.9×; circulating cap $18.4M [WOJAK §2–3])
| Factor | up | down | Source |
|---|---|---|---|
| cycle age: new contract 2026, ATH 20 Jun 2026 | 1.10 | 0.95 | [WOJAK §3] |
| drawdown −65% | 1.00 | 1.00 | [WOJAK §3] |
| 12.3K holders (halved by migration), $0.4–0.9M Uniswap liquidity, volume $8–11M → $1M/day | 0.90 | 1.10 | [WOJAK §2, §6] |
| CEX ladder: Kraken (30 Sep 2026), HTX, Gate perp, MEXC, LBank; Bitget/CoinEx lost | 1.10 | 0.95 | [WOJAK §5] |
| catalysts: MiCAR whitepaper (EU admission path), 27.27% burned, "no CEX moment yet" (Binance/Coinbase absent) | 1.10 | 1.00 | [WOJAK §4, §5, §10] |
| concentration: 68% dust wallets, low-float, no top-10 table for the new contract | 0.95 | 1.05 | [WOJAK §6] |
| IP: unowned Wojak brand, clones on Solana/Base/Robinhood/BSC; brand war won in 2026 | 0.95 | 1.05 | [WOJAK §8] |
| **product → applied** | **1.08 → 1.08** | **1.09 → 1.09** | |

Bounds matter: CHILLHOUSE's raw upside product (0.24) is floored at 0.5 and its downside product (2.17) capped at 2.0, so the model is *less* pessimistic on CHILLHOUSE than the factors alone would be.

---

## 4. Computation

### 4.1 Scenario-table method [CALC]
- Token conditional vector: p_i(o | s) = odds_mult( λ_i·T(o | s) + (1 − λ_i)·T_unc(o), M_i(o) ), where T is the generic table, T_unc its unconditional average under the Base SOL blend, and M_i(o) = M_up for upside outcomes, M_dn for downside outcomes.
- Unconditional: P_i(o) = Σ_s P(s)·p_i(o | s), with P(s) from the chosen blend.
- Conditional on SOL ≥ +50% (≥ $165): weights restricted to the fine buckets 165–220, 220–250, >250 (the 165–220 and 220–250 buckets inherit scenario D's conditional vector, >250 inherits E's). Conditional on SOL ≥ +100% (≥ $220): buckets 220–250 and >250. The same for ETH.
- New ATH: P(m ≥ k_ATH) is read off the token's threshold probabilities by log-linear interpolation between the points (1.5, 2, 3, 5, 10); beyond 10× a Pareto tail P(m ≥ k) = P(≥10x)·(k/10)^(−α) with α = log2[P(≥5x)/P(≥10x)] (floored at 1.05) [ASSUMPTION]. Example: for the generic unconditional vector α ≈ 1.4, so P(≥ 20×) = 0.6%, P(≥ 53×) ≈ 0.15%.
- Expected multiple (EV): band midpoints [ASSUMPTION] — dead 0.10×, (0.2, 0.5] 0.35×, (0.5, 1.5) 0.95×, [1.5, 2) 1.72×, [2, 3) 2.4×, [3, 5) 3.8×, [5, 10) 6.8×, ≥ 10× the Pareto mean 10·α/(α−1) **capped at 30×**. The cap matters: with α ≈ 1.4 the uncapped tail mean would be ~35×, so EV is a conservative number driven by the cap, not a precise one.
- Probability-weighted market cap = current cap × EV.

### 4.2 Monte Carlo cross-check [CALC]
- Chain: 100,000 terminal SOL (and ETH) prices drawn so that the fine-bucket frequencies equal the Base blend exactly (a 2-million-draw driftless 55% lognormal is split by bucket and each bucket resampled with the blended weight). This reproduces the scenario probabilities (A 32.1%, B 27.7%, C 16.2%, D 13.7%, E 10.4% in the draw) rather than forcing a single lognormal onto a bimodal blend; the single best-fitting lognormal (drift +10%, vol 69%) is used only for the touch sensitivity.
- Memecoin: log-multiple r_m = β_up·max(r_chain, 0) + β_dn·min(r_chain, 0) + δ + s·ε, with ε a unit-variance Student-t (3 degrees of freedom) shock — heavy tails on both sides, as the per-token histories (+920% / −72% in months) require.
- Generic calibration: (β_up, β_dn, δ, s) chosen by grid search to minimise the scenario-probability-weighted squared error between the MC's scenario-conditional outcome probabilities and the generic table of section 2. Result: **β_up = 1.5, β_dn = 1.3, δ = −0.80/yr, s = 1.60** (weighted SSE 0.0037). Reading: an established meme has upside beta 1.5 and downside beta 1.3 to SOL, a decay drift of −80% in log terms (e^−0.8 ≈ 0.45×/yr absent any chain move or luck) and a large idiosyncratic shock. The asymmetry is milder than the notes' "downside beta larger than upside beta" because the decay drift δ already captures most of the 2025–26 underperformance.
- Per token: β = λ_i × generic β; (δ_i, s_i) re-fitted so that the MC matches the token's scenario-table unconditional P(≥ +50%), P(≥ 2x) and P(≤ −50%). The MC's conditional and tail numbers are then *out-of-sample* relative to the fit and are reported next to the table numbers. EV in the MC is the mean of min(m, 30).
- Touch probabilities: 100,000 daily (252-step) SOL paths, driftless 55% and the fitted-blend lognormal.

---

## 5. Results (Base blend) — scenario table vs Monte Carlo

### 5.1 Summary, scenario-table method
| Token | Cap now | ATH needs | ≥ +50% | ≥ 2x | ≥ 3x | ≥ 5x | ≥ 10x | New ATH | ≤ −50% | Dead (≤ −80%) | EV | Prob.-wtd cap | ≥ 2x given chain ≥ +50% | ≥ 2x given chain ≥ +100% | ≥ 5x given ≥ +100% | ATH given ≥ +100% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHILLGUY | $13.0M | 53× | 11.9% | 7.3% | 4.4% | 2.3% | 0.8% | 0.1% | 64.3% | 39.5% | 0.93× | $12.1M | 21.4% | 26.2% | 9.0% | 0.3% |
| CHILLHOUSE | $1.5M | 19.5× | 10.5% | 6.5% | 3.9% | 2.0% | 0.8% | 0.3% | 72.5% | 48.7% | 0.81× | $1.2M | 14.3% | 16.9% | 5.8% | 0.9% |
| TROLL | $50.0M | 5.6× | 25.9% | 17.5% | 11.5% | 6.3% | 2.5% | 5.4% | 54.5% | 29.6% | 1.79× | $89.6M | 44.8% | 51.8% | 23.3% | 20.1% |
| TRIPLE T | $8.0M | 3.2× | 21.0% | 13.7% | 8.7% | 4.7% | 1.8% | 8.1% | 56.6% | 31.7% | 1.46× | $11.7M | 28.3% | 32.5% | 12.8% | 21.1% |
| CUPSEY | $6.5M | 3.2× | 14.8% | 9.4% | 5.8% | 3.0% | 1.1% | 5.3% | 63.2% | 38.0% | 1.09× | $7.1M | 20.2% | 23.5% | 8.5% | 14.3% |
| WOJAK (ETH) | $18.4M | 2.9× | 19.3% | 12.5% | 7.8% | 4.2% | 1.6% | 8.0% | 59.6% | 34.3% | 1.34× | $24.6M | 28.9% | 33.8% | 13.2% | 23.7% |

### 5.2 Summary, Monte Carlo (same tokens, same Base blend)
| Token | ≥ +50% | ≥ 2x | ≥ 3x | ≥ 5x | ≥ 10x | New ATH | ≤ −50% | Dead | EV (cap 30×) | Median multiple | ≥ 2x given chain ≥ +50% | ≥ 2x given ≥ +100% | ≥ 5x given ≥ +100% | ATH given ≥ +100% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHILLGUY | 11.2% | 7.8% | 4.7% | 2.6% | 1.3% | 0.4% | 64.3% | 33.3% | 0.93× | 0.33× | 22.4% | 28.1% | 8.3% | 0.8% |
| CHILLHOUSE | 9.8% | 7.4% | 5.2% | 3.4% | 2.0% | 1.3% | 72.2% | 45.7% | 1.02× | 0.23× | 13.1% | 14.7% | 6.0% | 2.2% |
| TROLL | 23.7% | 19.3% | 14.3% | 9.7% | 5.9% | 8.9% | 53.9% | 33.0% | 2.30× | 0.42× | 38.4% | 43.8% | 22.4% | 20.5% |
| TRIPLE T | 19.3% | 15.2% | 10.9% | 7.1% | 4.3% | 10.4% | 56.1% | 31.8% | 1.83× | 0.40× | 25.2% | 27.8% | 12.9% | 19.0% |
| CUPSEY | 13.7% | 10.4% | 7.1% | 4.5% | 2.6% | 6.6% | 62.9% | 35.1% | 1.30× | 0.33× | 18.5% | 20.6% | 8.2% | 12.9% |
| WOJAK (ETH) | 17.7% | 13.9% | 9.8% | 6.5% | 3.9% | 10.0% | 59.0% | 34.2% | 1.69× | 0.36× | 25.4% | 28.2% | 13.0% | 20.5% |

### 5.3 How to read the two methods together
- The two methods agree within a few points on the headline outcomes (≥ +50%, ≥ 2x, ≤ −50%) because the MC is calibrated on them; the useful information is where they differ.
- The MC's ≥ 10x and new-ATH probabilities are systematically higher (roughly ×1.3–2.5, up to ×4 for the far-away ATHs of CHILLGUY and CHILLHOUSE) than the table's: the Student-t(3) shock has a fatter tail than the Pareto extrapolation from the 5×/10× points. The honest reading is a range, e.g. CHILLHOUSE new ATH 0.3–1.3%, TROLL 5–9%, WOJAK 8–10%.
- The MC's conditional probabilities for the attention-driven tokens (λ = 0.5–0.6) are a little lower than the table's, because in the MC the chain contributes through β = λ·β_generic only, whereas the table mixes in the full generic conditional with weight λ.
- The **median** multiple in the MC (0.23–0.42× unconditional; 0.5–1.6× even given a chain rally) is the number a non-quant reader should remember: the typical outcome is a loss; the EV above 1 comes from a thin right tail.
- EV figures are driven by the 30× cap and should be quoted as "of the order of", not to two decimals.

### 5.4 Sensitivity to the SOL/ETH blend [CALC, section 10 of the output]
Moving from the Pessimistic to the Optimistic blend changes P(chain ≥ +50%) from 15% to 24% and shifts each token's P(≥ 2x) by roughly ±10–15% relative (e.g. TROLL 14.8% → 17.5% → 19.5%; CHILLGUY 6.0% → 7.3% → 8.4%). The ranking of the tokens is identical in all three blends. The model's conclusions are therefore much more sensitive to the memecoin base rates (section 2) and the per-token multipliers (section 3) than to the macro view of SOL.

### 5.5 What a rally actually buys [CALC, section 11 of the output]
| Token | λ | P(≥ 2x) if chain ends ≤ 0% (A+B) | P(≥ 2x) unconditional | P(≥ 2x) if chain ≥ +100% | ratio |
|---|---|---|---|---|---|
| CHILLGUY | 0.8 | 2.5% | 7.3% | 26.2% | 10.4× |
| CHILLHOUSE | 0.5 | 3.8% | 6.5% | 16.9% | 4.5× |
| TROLL | 0.8 | 7.4% | 17.5% | 51.8% | 7.0× |
| TRIPLE T | 0.5 | 8.5% | 13.7% | 32.5% | 3.8× |
| CUPSEY | 0.5 | 5.6% | 9.4% | 23.5% | 4.2× |
| WOJAK | 0.6 | 6.8% | 12.5% | 33.8% | 5.0× |

CHILLGUY and TROLL are the "rally plays": their odds of doubling rise 7–10× if SOL doubles. TRIPLE T, CUPSEY and CHILLHOUSE are "attention plays": a SOL rally only quadruples their odds, and most of their (modest) upside probability exists regardless of SOL.

### 5.6 Comparison with the report's scenario table [REPORT]
The report's "forte" scenario (SOL ≈ $250) assigns TROLL $200–300M (4–6×), WOJAK $55–75M (3–4×), CHILLGUY $40–65M (3–5×), TRIPLE T $24–32M (3–4×), CUPSEY $20–22M (3–3.5×), CHILLHOUSE $6–12M (4–8×). The model's scenario-E (SOL > $250) conditional probabilities of reaching **≥ 3×** are: TROLL ~42%, WOJAK ~25%, TRIPLE T ~24%, CUPSEY ~17%, CHILLGUY ~19%, CHILLHOUSE ~12% (scenario_E rows of `risultati_probabilita.csv`, column v3). In other words, the report's "forte" multiples are plausible *targets conditional on euphoria*, but even in euphoria they are reached by roughly one token in four, and the euphoria scenario itself has a ~10% probability. The product (P(E) × P(≥ 3× | E)) is 1–5% per token, which is what the unconditional columns above show.

---

## 6. Plain-language explanation (for the non-quant reader)

**Why the numbers come out this way.**

1. *SOL itself probably does not rally.* The options market prices a 55% volatility and no drift; that alone gives only a 20% chance that SOL is above $150 in a year and a 4% chance above $250. The Fed is hiking, the CLARITY Act failed, ETF flows just turned negative. Prediction markets and the 2021–2023 history are more optimistic, so the model gives them some weight, landing at "about 1 chance in 5 that SOL is up ≥ 50% in a year, 1 in 8 that it doubles, 1 in 20 that it beats its all-time high" and "roughly 6 chances in 10 that it is lower".

2. *Even if SOL doubles, an old memecoin usually does not double with it.* The Coin Metrics study says only 3.3% of Solana memes ever got back to their peak and two-thirds never had a second rally at all; in the most recent SOL rally (+40–60% in Q3 2026) the established-meme basket was flat and the gains went to tokens launched that month. The model therefore says that, **given** SOL doubles, a generic old meme has about a 1-in-2 chance of doubling in the euphoria case and 1-in-4 in the strong-rally case — and multiplies that by the modest probability of the rally itself. Unconditionally this is ~12% for doubling and ~4% for a 5×.

3. *Each token then moves up or down from that generic number for stated reasons.* TROLL (Coinbase + Binance.US listings, exclusive IP licence, 65–70K growing holders, a 2026 cycle of its own) gets its odds raised by 1.7×; CHILLGUY (−98%, a 2024 meme, bundled supply, IP dispute, no catalyst) gets them cut by almost half; CHILLHOUSE (no sign of a team since Nov 2025, $20K/day volume) hits the floor of the allowed range; TRIPLE T, CUPSEY and WOJAK are near neutral: younger, closer to their highs, but with thin liquidity and insider/clone issues.

4. *How much of the upside actually depends on the rally.* TRIPLE T, CUPSEY and WOJAK made their 2026 highs while their chains were flat or falling and fell while the chains rose. So the model only lets half of their outcome depend on SOL/ETH; the other half is "their own attention cycle". That is why their probabilities move less between the no-rally and rally columns than CHILLGUY's and TROLL's.

5. *The headline figures.* Over the next 12 months, roughly: TROLL has about a 1-in-4 chance of being up ≥ 50% and about 1-in-6 of doubling, rising to ~1-in-2 if SOL doubles; TRIPLE T and WOJAK about 1-in-5 and 1-in-7 (1-in-3 if their chain doubles); CUPSEY about 1-in-7 and 1-in-10; CHILLGUY about 1-in-8 and 1-in-14 (1-in-4 if SOL doubles), with a new ATH (53× away) essentially off the table (<1%); CHILLHOUSE about 1-in-10 and 1-in-15, with roughly a coin-flip chance of being effectively dead. For every token the single most likely outcome is to lose at least half: 55–72% unconditionally, and still 22–55% even if the chain doubles.

6. *Why "expected value" can exceed 1 while the typical outcome is a loss.* The expected multiple (0.8–1.8× in the table, 0.9–2.3× in the Monte Carlo) is the average over thousands of paths, dominated by a few paths with 10–30× outcomes. The median path loses roughly 60–75% (MC medians 0.23–0.42×). A reader who cannot hold a basket of many such bets, or cannot tolerate a near-total loss, should look at the median and the "dead" column, not the EV.

---

## 7. Caveats (please carry into the report)

1. **Illustrative, not predictive.** Scenario probabilities, the conditional table and the multipliers are judgmental estimates anchored on the notes; a different modeller would produce different numbers. The purpose is transparency of reasoning, not accuracy.
2. **Data quality.** Every market figure comes from search-engine snippets (direct fetches were blocked); current prices/caps are late-Sep/early-Oct 2026 snapshots, not 8 Oct 2026 quotes; aggregators disagree by 15–50% on some tokens [all TOKEN notes, method notes].
3. **Small samples.** The SOL historical base rates come from ~57 overlapping monthly windows reconstructed from memory ("verify before publication" [SOL-Q4]); the memecoin base rates come from one Coin Metrics study (150 tokens, survivor-biased) plus anecdotal per-token windows [BASE-KQ1, KQ3].
4. **No formal beta.** No source publishes a regression beta of Solana memes to SOL [BASE-KQ2]; the β_up = 1.5 / β_dn = 1.3 / δ = −0.8 Monte Carlo parameters are calibrated to the judgmental table, not estimated from data.
5. **Prediction-market component.** The Kalshi ladder is a 3-month, $183K-volume, long-shot-biased market; using it for 12 months required the two-stage assumption in section 1.3(b). No 2027 market exists.
6. **ETH assumptions.** ETH volatility (50%) and the reuse of SOL's prediction-market and historical components for ETH are assumptions; the WOJAK conditional table is the Solana-meme table (PEPE-type Ethereum memes may have better survival, e.g. PEPE set a new ATH in Dec 2024 [OUTLOOK-KQ6]).
7. **Tails and EV.** P(≥ 10x), P(new ATH) for far-away ATHs and EV depend on the tail assumption (Pareto vs Student-t) and on the 30× cap; quote them as ranges and orders of magnitude.
8. **Liquidity collapse, delisting, rug, migration risks** are only partially captured by the downside multipliers; a Binance perp delisting (CHILLGUY), a second contract migration (CUPSEY, WOJAK) or an LP withdrawal (CHILLHOUSE, LP status unknown) would be discrete events outside the lognormal/t framework.
9. **Scenario independence.** The model treats the memecoin response as depending only on where SOL ends the year, not on the path (a spike to $200 in March followed by a return to $110 would be "scenario B" with a possibly very different memecoin outcome).
10. **Nothing here is financial advice.** The tokens are illiquid, high-risk assets with no fundamental floor; a total loss is a plausible outcome in every scenario.

---

## 8. Verbatim output of `python3 -I model_probabilita.py` (run of 9 Oct 2026)

(The same text is in `output_modello.txt`; tables are also in `risultati_probabilita.md` and `risultati_probabilita.csv`.)

# Risultati del modello probabilistico (8 ott 2026 -> 8 ott 2027)

Generated by model_probabilita.py (seed 20261009, 100,000 Monte Carlo paths). All figures are model ESTIMATES built from the research notes; see probability_model.md.

## 1. SOL: component distributions on 8 Oct 2027 (S0 = $110)

(b) Kalshi fit: drift mu_b = +0.90/yr, vol sigma_b = 1.10, SSE = 0.0068 (fitted on P(>=100)=71%, P(>=150)=34%, P(>=200)=27% at T=0.26y from $121; fit reproduces: P(>=100)=68.3%, P(>=150)=40.3%, P(>=200)=22.4%). Applied for the first 0.26 y, then the 55% IV lognormal for the remaining 0.74 y: effective 12-month vol 0.73, mean log-return -0.035.

| Bucket | (a) lognormal 55% | (a') stress 70% | (b) Kalshi-fitted | (c) historical | (d) macro -15% | (d) macro -25%/60% | (d) macro 0% |
|---|---|---|---|---|---|---|---|
| <70 | 29.2% | 38.4% | 28.5% | 32.1% | 39.2% | 48.5% | 29.2% |
| 70-110 | 31.6% | 25.3% | 23.4% | 18.9% | 31.6% | 27.8% | 31.6% |
| 110-150 | 19.1% | 14.9% | 16.2% | 11.6% | 15.9% | 12.8% | 19.1% |
| 150-165 | 4.5% | 3.7% | 4.5% | 4.4% | 3.4% | 2.7% | 4.5% |
| 165-220 | 9.3% | 8.6% | 11.4% | 2.0% | 6.4% | 5.1% | 9.3% |
| 220-250 | 2.4% | 2.6% | 3.9% | 0.8% | 1.5% | 1.2% | 2.4% |
| >250 | 3.9% | 6.4% | 12.2% | 30.2% | 2.1% | 1.9% | 3.9% |

## 2. SOL: blended scenario probabilities (sensitivity)

| Scenario | Ottimistico (a.30/b.30/c.30/d.10, d=0%) | Base (a.35/b.20/c.20/d.25, d=-15%) | Pessimistico (a.30/b.10/c.10/d.50, d=-25%, vol 60%) |
|---|---|---|---|
| A: Crollo (<$70, peggio di -36%) | 29.9% | 32.1% | 39.1% |
| B: Ribasso ($70-110, da -36% a 0%) | 25.3% | 27.4% | 27.6% |
| C: Laterale/moderato ($110-150, da 0 a +36%) | 16.0% | 16.2% | 14.9% |
| D: Rialzo forte ($150-250, da +36% a +127%) | 14.6% | 13.9% | 12.1% |
| E: Euforia (>$250, oltre +127%) | 14.2% | 10.3% | 6.3% |
| P(SOL >= +50%, >= $165) | 24.4% | 20.0% | 14.8% |
| P(SOL >= +100%, >= $220) | 16.6% | 12.5% | 8.1% |
| P(SOL >= ATH $294.85) [= P(>250) x share of the >250 bucket above $294.85 under the 55% lognormal] | 7.1% | 5.2% | 3.2% |

Fine buckets, Base blend: <70: 32.1%, 70-110: 27.4%, 110-150: 16.2%, 150-165: 4.2%, 165-220: 7.5%, 220-250: 2.1%, >250: 10.3%

Single lognormal best-fitting the Base blend (used only for the touch sensitivity): drift +0.10/yr, vol 0.69 (SSE 0.00161). Monte Carlo terminal SOL draws (bucket-resampled, so they match the blend): median = $94, mean = $120, share by scenario = A: 32.1%, B: 27.7%, C: 16.2%, D: 13.7%, E: 10.4%.

## 3. SOL: probability of TOUCHING a level at any time in the 12 months

| Level | Notes (2 x terminal, 55% vol, driftless) | MC daily paths, driftless 55% | MC daily paths, Base-blend drift/vol |
|---|---|---|---|
| $150 | 40.2% | 46.1% | 56.3% |
| $200 | 17.3% | 18.9% | 30.2% |
| $250 | 7.7% | 8.1% | 16.9% |
| $300 | 3.6% | 3.7% | 10.0% |

## 4. ETH (for WOJAK): blended scenario probabilities, same return buckets

| Scenario (ETH, S0 = $2,600) | Ottimistico | Base | Pessimistico |
|---|---|---|---|
| A: <$1,655 | 28.4% | 30.2% | 36.9% |
| B: $1,655-2,600 | 26.4% | 29.1% | 29.7% |
| C: $2,600-3,545 | 16.7% | 17.1% | 15.8% |
| D: $3,545-5,909 (ATH $4,950 inside) | 14.6% | 13.8% | 11.8% |
| E: >$5,909 | 13.9% | 9.8% | 5.8% |
| P(ETH >= +50%) | 23.9% | 19.3% | 13.9% |
| P(ETH >= +100%) | 16.1% | 11.9% | 7.4% |

Monte Carlo lognormal fitted to the ETH Base blend: drift +0.08/yr, vol 0.64.

## 5. Conditional response of a GENERIC established Solana memecoin (12 months)

Rows: SOL scenario. Columns: probability that the memecoin reaches the outcome. ESTIMATES (see probability_model.md s.2).

| SOL scenario | >= +50% | >= 2x | >= 3x | >= 5x | >= 10x | <= -50% | <= -80% (dead) |
|---|---|---|---|---|---|---|---|
| A: Crollo (<$70, peggio di -36%) | 3.0% | 1.5% | 0.8% | 0.3% | 0.1% | 85.0% | 55.0% |
| B: Ribasso ($70-110, da -36% a 0%) | 8.0% | 4.0% | 2.2% | 1.0% | 0.3% | 65.0% | 35.0% |
| C: Laterale/moderato ($110-150, da 0 a +36%) | 18.0% | 10.0% | 5.5% | 2.5% | 0.8% | 45.0% | 20.0% |
| D: Rialzo forte ($150-250, da +36% a +127%) | 40.0% | 25.0% | 15.0% | 8.0% | 3.0% | 28.0% | 12.0% |
| E: Euforia (>$250, oltre +127%) | 65.0% | 50.0% | 35.0% | 20.0% | 8.0% | 15.0% | 6.0% |
| Unconditional (Base SOL blend) | 18.3% | 11.8% | 7.5% | 4.0% | 1.5% | 57.9% | 32.8% |

Sanity check vs Coin Metrics: implied generic P(reclaim ATH | ATH is ~5x away) = 4.0%, (10x away) = 1.5%, (20x away) = 0.6%; Coin Metrics multi-year reclaim rate = 3.3%.

## 6. Per-token adjustment factors (odds multipliers: upside / downside)

### CHILLGUY  (chain SOL, price 0.0125, ATH 0.665 -> new ATH needs 53.2x; cap $13.0M; linkage lambda = 0.8)

| Factor | Upside odds x | Downside odds x |
|---|---|---|
| cycle_age (2024-cycle, ATH Nov 2024) | 0.70 | 1.15 |
| drawdown -98% (decay phase) | 0.85 | 1.10 |
| holders 118K / liq $1.2M / vol $3-5M | 1.10 | 0.90 |
| CEX ladder: Binance perp 75x + 5 spot (delist risk) | 1.15 | 1.10 |
| catalysts: none found 2026 | 0.90 | 1.00 |
| concentration: >20% bundled, top-10 52% | 0.90 | 1.10 |
| IP: Banks copyright claim (dormant) | 0.90 | 1.00 |
| **Product (raw)** | 0.55 | 1.38 |
| **Applied (clipped to [0.5, 2.0])** | 0.55 | 1.38 |

### CHILLHOUSE  (chain SOL, price 0.0015, ATH 0.02919 -> new ATH needs 19.5x; cap $1.5M; linkage lambda = 0.5)

| Factor | Upside odds x | Downside odds x |
|---|---|---|
| cycle_age (2025 stunts, ATH Oct 2025) | 0.70 | 1.15 |
| drawdown -95% (decay phase) | 0.85 | 1.10 |
| holders 19K / liq $0.4M / vol ~$20K DEX | 0.80 | 1.30 |
| CEX ladder: Kraken + MEXC (thin) | 1.00 | 1.00 |
| catalysts: no team activity since Nov 2025 | 0.60 | 1.20 |
| concentration: bundles flagged (unverified) | 0.95 | 1.10 |
| IP: Chill Guy image (Banks) | 0.90 | 1.00 |
| **Product (raw)** | 0.24 | 2.17 |
| **Applied (clipped to [0.5, 2.0])** | 0.50 | 2.00 |

### TROLL  (chain SOL, price 0.05, ATH 0.282 -> new ATH needs 5.6x; cap $50.0M; linkage lambda = 0.8)

| Factor | Upside odds x | Downside odds x |
|---|---|---|
| cycle_age (ATH Aug 2025 but own 2026 cycle, May 2026 peak) | 1.00 | 1.00 |
| drawdown -82% | 0.95 | 1.05 |
| holders 65-70K rising / liq $1.7-3.9M | 1.15 | 0.90 |
| CEX ladder: Coinbase, Binance.US, KuCoin, MEXC perp, Alpha tag | 1.25 | 0.90 |
| catalysts: airdrop Sep 2026, Binance global optionality, IP license | 1.20 | 1.00 |
| concentration: 10 whales + Ramirez bag, opaque | 0.95 | 1.05 |
| IP: exclusive Trollface license | 1.10 | 0.95 |
| **Product (raw)** | 1.71 | 0.85 |
| **Applied (clipped to [0.5, 2.0])** | 1.71 | 0.85 |

### TRIPLE T  (chain SOL, price 0.0085, ATH 0.027 -> new ATH needs 3.2x; cap $8.0M; linkage lambda = 0.5)

| Factor | Upside odds x | Downside odds x |
|---|---|---|
| cycle_age (2026 launch, ATH Jul 2026) | 1.10 | 0.95 |
| drawdown -70% | 1.00 | 1.00 |
| holders 22-25K rising / liq $0.7M | 1.00 | 1.00 |
| CEX ladder: BitMart spot + MEXC perp only | 0.90 | 1.05 |
| catalysts: Ramadan 2027 (Feb), brainrot meta | 1.15 | 1.00 |
| concentration: top-10 16%, LP burned | 1.05 | 0.95 |
| IP: public-domain character | 1.00 | 1.00 |
| **Product (raw)** | 1.20 | 0.95 |
| **Applied (clipped to [0.5, 2.0])** | 1.20 | 0.95 |

### CUPSEY  (chain SOL, price 0.0065, ATH 0.021 -> new ATH needs 3.2x; cap $6.5M; linkage lambda = 0.5)

| Factor | Upside odds x | Downside odds x |
|---|---|---|
| cycle_age (relaunch Jan 2026, ATH Aug 2026) | 1.10 | 0.95 |
| drawdown -70% (blow-off, momentum negative) | 1.00 | 1.00 |
| holders 15K / liq $0.5M | 0.95 | 1.05 |
| CEX ladder: Gate, MEXC, WEEX, Bitrue Alpha (2nd tier) | 0.90 | 1.05 |
| catalysts: pump.fun mascot claim (unverified) | 1.00 | 1.00 |
| concentration: 16.8% project wallet + 8% KOL unlocked, migration | 0.85 | 1.15 |
| IP/reputation: unowned, trader not involved, phishing scams | 0.95 | 1.05 |
| **Product (raw)** | 0.76 | 1.26 |
| **Applied (clipped to [0.5, 2.0])** | 0.76 | 1.26 |

### WOJAK (ETH)  (chain ETH, price 5.92e-08, ATH 1.74e-07 -> new ATH needs 2.9x; cap $18.4M; linkage lambda = 0.6)

| Factor | Upside odds x | Downside odds x |
|---|---|---|
| cycle_age (new contract 2026, ATH Jun 2026) | 1.10 | 0.95 |
| drawdown -65% | 1.00 | 1.00 |
| holders 12.3K / liq $0.4-0.9M / vol falling | 0.90 | 1.10 |
| CEX ladder: Kraken, HTX, Gate perp, MEXC, LBank | 1.10 | 0.95 |
| catalysts: MiCAR whitepaper, 27% burn, no CEX moment yet | 1.10 | 1.00 |
| concentration: 68% dust wallets, low float, no top-10 table | 0.95 | 1.05 |
| IP: unowned Wojak brand, clones, brand war won | 0.95 | 1.05 |
| **Product (raw)** | 1.08 | 1.09 |
| **Applied (clipped to [0.5, 2.0])** | 1.08 | 1.09 |

## 7. Per-token results: scenario table vs Monte Carlo

Generic MC calibration: beta_up = 1.5, beta_down = 1.3, decay drift delta = -0.80/yr, idiosyncratic scale s = 1.60 (Student-t, 3 d.o.f.); weighted SSE vs table = 0.0037.

### CHILLGUY

MC token parameters: beta_up = 1.20, beta_down = 1.04, delta = -1.00, s = 1.30; P(SOL >= +50%) = 20.0%, P(SOL >= +100%) = 12.5%.

| Outcome | Uncond. (table) | Uncond. (MC) | given SOL >= +50% (table) | given SOL >= +50% (MC) | given SOL >= +100% (table) | given SOL >= +100% (MC) |
|---|---|---|---|---|---|---|
| >= +50% | 11.9% | 11.2% | 32.3% | 32.1% | 37.8% | 39.9% |
| >= 2x | 7.3% | 7.8% | 21.4% | 22.4% | 26.2% | 28.1% |
| >= 3x | 4.4% | 4.7% | 13.4% | 13.1% | 16.8% | 16.5% |
| >= 5x | 2.3% | 2.6% | 7.1% | 6.7% | 9.0% | 8.3% |
| >= 10x | 0.8% | 1.3% | 2.7% | 3.0% | 3.4% | 3.6% |
| <= -50% | 64.3% | 64.3% | 35.5% | 23.9% | 31.8% | 16.8% |
| <= -80% (dead) | 39.5% | 33.3% | 17.9% | 6.9% | 16.0% | 5.1% |
| New ATH (>= 53.2x) | 0.1% | 0.4% | 0.3% | 0.7% | 0.3% | 0.8% |
| Expected multiple (EV, tail capped at 30x) | 0.93x | 0.93x | 2.11x | 1.98x | 2.48x | 2.32x |
| Prob.-weighted market cap ($M) | 12.1 | 12.1 | 27.4 | 25.7 | 32.2 | 30.2 |
| Median multiple (MC only) | - | 0.33x | - | 0.98x | - | 1.21x |

Scenario-by-scenario (SOL scenario -> outcome), scenario table / MC:

| Scenario | P(scen) | >= +50% | >= 2x | >= 5x | >= 10x | <= -50% | <= -80% (dead) | New ATH | EV |
|---|---|---|---|---|---|---|---|---|---|
| A | 32.1% | 3% / 3% | 2% / 2% | 1% / 1% | 0% / 1% | 84% / 88% | 58% / 60% | 0.0% / 0.2% | 0.42x / 0.44x |
| B | 27.4% | 6% / 6% | 3% / 4% | 1% / 2% | 0% / 1% | 71% / 74% | 42% / 33% | 0.0% / 0.3% | 0.60x / 0.69x |
| C | 16.2% | 11% / 10% | 6% / 7% | 2% / 3% | 1% / 1% | 56% / 56% | 29% / 19% | 0.0% / 0.5% | 0.87x / 1.00x |
| D | 13.9% | 23% / 19% | 14% / 12% | 4% / 4% | 1% / 2% | 41% / 37% | 21% / 10% | 0.1% / 0.4% | 1.50x / 1.38x |
| E | 10.3% | 41% / 43% | 29% / 30% | 10% / 9% | 4% / 4% | 30% / 15% | 15% / 5% | 0.4% / 0.8% | 2.68x / 2.43x |

### CHILLHOUSE

MC token parameters: beta_up = 0.75, beta_down = 0.65, delta = -1.40, s = 1.85; P(SOL >= +50%) = 20.0%, P(SOL >= +100%) = 12.5%.

| Outcome | Uncond. (table) | Uncond. (MC) | given SOL >= +50% (table) | given SOL >= +50% (MC) | given SOL >= +100% (table) | given SOL >= +100% (MC) |
|---|---|---|---|---|---|---|
| >= +50% | 10.5% | 9.8% | 21.8% | 17.4% | 24.7% | 19.5% |
| >= 2x | 6.5% | 7.4% | 14.3% | 13.1% | 16.9% | 14.7% |
| >= 3x | 3.9% | 5.2% | 9.0% | 8.8% | 10.9% | 9.6% |
| >= 5x | 2.0% | 3.4% | 4.8% | 5.5% | 5.8% | 6.0% |
| >= 10x | 0.8% | 2.0% | 1.8% | 3.2% | 2.2% | 3.5% |
| <= -50% | 72.5% | 72.2% | 56.6% | 53.0% | 54.6% | 48.3% |
| <= -80% (dead) | 48.7% | 45.7% | 34.5% | 25.3% | 33.2% | 21.7% |
| New ATH (>= 19.5x) | 0.3% | 1.3% | 0.7% | 2.0% | 0.9% | 2.2% |
| Expected multiple (EV, tail capped at 30x) | 0.81x | 1.02x | 1.48x | 1.57x | 1.68x | 1.71x |
| Prob.-weighted market cap ($M) | 1.2 | 1.5 | 2.2 | 2.4 | 2.5 | 2.6 |
| Median multiple (MC only) | - | 0.23x | - | 0.46x | - | 0.53x |

Scenario-by-scenario (SOL scenario -> outcome), scenario table / MC:

| Scenario | P(scen) | >= +50% | >= 2x | >= 5x | >= 10x | <= -50% | <= -80% (dead) | New ATH | EV |
|---|---|---|---|---|---|---|---|---|---|
| A | 32.1% | 6% / 6% | 3% / 4% | 1% / 2% | 0% / 1% | 83% / 83% | 61% / 61% | 0.2% / 1.0% | 0.52x / 0.71x |
| B | 27.4% | 7% / 8% | 4% / 6% | 1% / 3% | 0% / 2% | 76% / 76% | 51% / 48% | 0.2% / 1.2% | 0.63x / 0.89x |
| C | 16.2% | 10% / 10% | 6% / 8% | 2% / 4% | 1% / 2% | 68% / 69% | 42% / 39% | 0.2% / 1.5% | 0.78x / 1.12x |
| D | 13.9% | 17% / 14% | 10% / 10% | 3% / 5% | 1% / 3% | 60% / 61% | 37% / 32% | 0.4% / 1.6% | 1.14x / 1.31x |
| E | 10.3% | 26% / 20% | 18% / 15% | 6% / 6% | 2% / 4% | 53% / 47% | 33% / 21% | 1.0% / 2.2% | 1.80x / 1.75x |

### TROLL

MC token parameters: beta_up = 1.20, beta_down = 1.04, delta = -0.75, s = 2.35; P(SOL >= +50%) = 20.0%, P(SOL >= +100%) = 12.5%.

| Outcome | Uncond. (table) | Uncond. (MC) | given SOL >= +50% (table) | given SOL >= +50% (MC) | given SOL >= +100% (table) | given SOL >= +100% (MC) |
|---|---|---|---|---|---|---|
| >= +50% | 25.9% | 23.7% | 58.8% | 45.6% | 64.9% | 51.3% |
| >= 2x | 17.5% | 19.3% | 44.8% | 38.4% | 51.8% | 43.8% |
| >= 3x | 11.5% | 14.3% | 31.7% | 28.7% | 38.2% | 33.0% |
| >= 5x | 6.3% | 9.7% | 18.9% | 19.6% | 23.3% | 22.4% |
| >= 10x | 2.5% | 5.9% | 7.8% | 11.5% | 9.8% | 13.2% |
| <= -50% | 54.5% | 53.9% | 25.4% | 27.9% | 22.4% | 23.1% |
| <= -80% (dead) | 29.6% | 33.0% | 11.9% | 13.7% | 10.5% | 11.4% |
| New ATH (>= 5.6x) | 5.4% | 8.9% | 16.2% | 17.8% | 20.1% | 20.5% |
| Expected multiple (EV, tail capped at 30x) | 1.79x | 2.30x | 4.36x | 4.19x | 5.16x | 4.69x |
| Prob.-weighted market cap ($M) | 89.6 | 115.2 | 217.9 | 209.4 | 258.0 | 234.7 |
| Median multiple (MC only) | - | 0.42x | - | 1.27x | - | 1.58x |

Scenario-by-scenario (SOL scenario -> outcome), scenario table / MC:

| Scenario | P(scen) | >= +50% | >= 2x | >= 5x | >= 10x | <= -50% | <= -80% (dead) | New ATH | EV |
|---|---|---|---|---|---|---|---|---|---|
| A | 32.1% | 10% / 12% | 6% / 10% | 2% / 5% | 1% / 3% | 77% / 72% | 46% / 50% | 1.5% / 4.5% | 0.74x / 1.32x |
| B | 27.4% | 16% / 19% | 9% / 15% | 3% / 7% | 1% / 5% | 60% / 58% | 31% / 34% | 2.2% / 6.8% | 1.05x / 1.90x |
| C | 16.2% | 27% / 26% | 17% / 21% | 5% / 10% | 2% / 6% | 44% / 47% | 20% / 25% | 3.9% / 9.4% | 1.58x / 2.49x |
| D | 13.9% | 49% / 36% | 33% / 29% | 12% / 14% | 5% / 8% | 30% / 36% | 14% / 18% | 9.9% / 13.1% | 3.03x / 3.25x |
| E | 10.3% | 68% / 53% | 56% / 46% | 26% / 23% | 11% / 14% | 21% / 22% | 10% / 11% | 22.1% / 21.4% | 5.60x / 4.87x |

### TRIPLE T

MC token parameters: beta_up = 0.75, beta_down = 0.65, delta = -0.85, s = 2.15; P(SOL >= +50%) = 20.0%, P(SOL >= +100%) = 12.5%.

| Outcome | Uncond. (table) | Uncond. (MC) | given SOL >= +50% (table) | given SOL >= +50% (MC) | given SOL >= +100% (table) | given SOL >= +100% (MC) |
|---|---|---|---|---|---|---|
| >= +50% | 21.0% | 19.3% | 39.7% | 31.9% | 43.8% | 35.1% |
| >= 2x | 13.7% | 15.2% | 28.3% | 25.2% | 32.5% | 27.8% |
| >= 3x | 8.7% | 10.9% | 18.9% | 18.1% | 22.4% | 19.9% |
| >= 5x | 4.7% | 7.1% | 10.6% | 11.7% | 12.8% | 12.9% |
| >= 10x | 1.8% | 4.3% | 4.2% | 6.7% | 5.1% | 7.2% |
| <= -50% | 56.6% | 56.1% | 38.3% | 36.9% | 36.3% | 32.9% |
| <= -80% (dead) | 31.7% | 31.8% | 20.0% | 17.4% | 19.1% | 15.3% |
| New ATH (>= 3.2x) | 8.1% | 10.4% | 17.7% | 17.2% | 21.1% | 19.0% |
| Expected multiple (EV, tail capped at 30x) | 1.46x | 1.83x | 2.73x | 2.78x | 3.13x | 2.99x |
| Prob.-weighted market cap ($M) | 11.7 | 14.7 | 21.8 | 22.2 | 25.0 | 23.9 |
| Median multiple (MC only) | - | 0.40x | - | 0.80x | - | 0.91x |

Scenario-by-scenario (SOL scenario -> outcome), scenario table / MC:

| Scenario | P(scen) | >= +50% | >= 2x | >= 5x | >= 10x | <= -50% | <= -80% (dead) | New ATH | EV |
|---|---|---|---|---|---|---|---|---|---|
| A | 32.1% | 12% / 12% | 8% / 10% | 3% / 5% | 1% / 3% | 70% / 69% | 43% / 43% | 4.5% / 6.7% | 0.94x / 1.29x |
| B | 27.4% | 15% / 17% | 9% / 13% | 3% / 6% | 1% / 4% | 60% / 59% | 33% / 33% | 5.3% / 8.9% | 1.10x / 1.64x |
| C | 16.2% | 21% / 21% | 13% / 16% | 4% / 8% | 1% / 5% | 50% / 51% | 25% / 27% | 7.1% / 11.2% | 1.37x / 1.99x |
| D | 13.9% | 33% / 26% | 21% / 21% | 7% / 10% | 3% / 6% | 42% / 44% | 21% / 21% | 12.3% / 14.0% | 2.06x / 2.36x |
| E | 10.3% | 46% / 36% | 35% / 29% | 14% / 13% | 6% / 7% | 35% / 32% | 19% / 15% | 22.9% / 19.6% | 3.35x / 3.06x |

### CUPSEY

MC token parameters: beta_up = 0.75, beta_down = 0.65, delta = -1.05, s = 1.85; P(SOL >= +50%) = 20.0%, P(SOL >= +100%) = 12.5%.

| Outcome | Uncond. (table) | Uncond. (MC) | given SOL >= +50% (table) | given SOL >= +50% (MC) | given SOL >= +100% (table) | given SOL >= +100% (MC) |
|---|---|---|---|---|---|---|
| >= +50% | 14.8% | 13.7% | 29.7% | 24.4% | 33.2% | 27.2% |
| >= 2x | 9.4% | 10.4% | 20.2% | 18.5% | 23.5% | 20.6% |
| >= 3x | 5.8% | 7.1% | 13.0% | 12.4% | 15.6% | 13.9% |
| >= 5x | 3.0% | 4.5% | 7.1% | 7.5% | 8.5% | 8.2% |
| >= 10x | 1.1% | 2.6% | 2.7% | 4.3% | 3.3% | 4.7% |
| <= -50% | 63.2% | 62.9% | 45.3% | 41.2% | 43.2% | 36.4% |
| <= -80% (dead) | 38.0% | 35.1% | 25.0% | 17.7% | 23.9% | 15.2% |
| New ATH (>= 3.2x) | 5.3% | 6.6% | 11.9% | 11.5% | 14.3% | 12.9% |
| Expected multiple (EV, tail capped at 30x) | 1.09x | 1.30x | 2.00x | 2.03x | 2.29x | 2.20x |
| Prob.-weighted market cap ($M) | 7.1 | 8.4 | 13.0 | 13.2 | 14.9 | 14.3 |
| Median multiple (MC only) | - | 0.33x | - | 0.65x | - | 0.75x |

Scenario-by-scenario (SOL scenario -> outcome), scenario table / MC:

| Scenario | P(scen) | >= +50% | >= 2x | >= 5x | >= 10x | <= -50% | <= -80% (dead) | New ATH | EV |
|---|---|---|---|---|---|---|---|---|---|
| A | 32.1% | 8% / 8% | 5% / 6% | 2% / 3% | 1% / 2% | 76% / 76% | 50% / 49% | 2.9% / 4.0% | 0.70x / 0.89x |
| B | 27.4% | 10% / 11% | 6% / 9% | 2% / 4% | 1% / 2% | 67% / 67% | 39% / 37% | 3.4% / 5.5% | 0.84x / 1.14x |
| C | 16.2% | 14% / 15% | 9% / 11% | 2% / 5% | 1% / 3% | 57% / 59% | 31% / 29% | 4.5% / 7.2% | 1.04x / 1.42x |
| D | 13.9% | 24% / 19% | 15% / 15% | 5% / 6% | 2% / 4% | 49% / 49% | 27% / 22% | 8.0% / 9.0% | 1.53x / 1.68x |
| E | 10.3% | 35% / 28% | 25% / 21% | 9% / 8% | 4% / 5% | 42% / 35% | 23% / 15% | 15.6% / 13.4% | 2.45x / 2.25x |

### WOJAK (ETH)

MC token parameters: beta_up = 0.90, beta_down = 0.78, delta = -0.95, s = 2.10; P(ETH >= +50%) = 19.3%, P(ETH >= +100%) = 11.9%.

| Outcome | Uncond. (table) | Uncond. (MC) | given ETH >= +50% (table) | given ETH >= +50% (MC) | given ETH >= +100% (table) | given ETH >= +100% (MC) |
|---|---|---|---|---|---|---|
| >= +50% | 19.3% | 17.7% | 40.8% | 32.1% | 45.7% | 35.5% |
| >= 2x | 12.5% | 13.9% | 28.9% | 25.4% | 33.8% | 28.2% |
| >= 3x | 7.8% | 9.8% | 19.2% | 18.0% | 23.3% | 20.1% |
| >= 5x | 4.2% | 6.5% | 10.7% | 11.7% | 13.2% | 13.0% |
| >= 10x | 1.6% | 3.9% | 4.2% | 6.5% | 5.2% | 7.1% |
| <= -50% | 59.6% | 59.0% | 37.9% | 36.7% | 35.4% | 32.7% |
| <= -80% (dead) | 34.3% | 34.2% | 19.7% | 17.0% | 18.5% | 14.8% |
| New ATH (>= 2.9x) | 8.0% | 10.0% | 19.6% | 18.4% | 23.7% | 20.5% |
| Expected multiple (EV, tail capped at 30x) | 1.34x | 1.69x | 2.75x | 2.74x | 3.21x | 2.96x |
| Prob.-weighted market cap ($M) | 24.6 | 31.0 | 50.6 | 50.4 | 59.1 | 54.5 |
| Median multiple (MC only) | - | 0.36x | - | 0.79x | - | 0.92x |

Scenario-by-scenario (ETH scenario -> outcome), scenario table / MC:

| Scenario | P(scen) | >= +50% | >= 2x | >= 5x | >= 10x | <= -50% | <= -80% (dead) | New ATH | EV |
|---|---|---|---|---|---|---|---|---|---|
| A | 30.2% | 10% / 10% | 6% / 8% | 2% / 4% | 1% / 2% | 76% / 74% | 48% / 49% | 3.8% / 5.9% | 0.76x / 1.11x |
| B | 29.1% | 13% / 14% | 8% / 11% | 2% / 5% | 1% / 3% | 64% / 63% | 36% / 36% | 4.7% / 8.1% | 0.95x / 1.46x |
| C | 17.1% | 19% / 19% | 11% / 15% | 3% / 7% | 1% / 4% | 52% / 54% | 27% / 28% | 6.9% / 10.8% | 1.25x / 1.82x |
| D | 13.8% | 33% / 26% | 21% / 20% | 7% / 9% | 3% / 5% | 42% / 44% | 22% / 21% | 13.1% / 14.7% | 2.02x / 2.32x |
| E | 9.8% | 48% / 37% | 36% / 29% | 14% / 13% | 6% / 7% | 34% / 32% | 18% / 14% | 25.9% / 21.1% | 3.45x / 3.03x |

## 8. Summary table (scenario-table method, Base blend)

| Token | Cap now | ATH needs | P(>=+50%) | P(>=2x) | P(>=3x) | P(>=5x) | P(>=10x) | P(new ATH) | P(<=-50%) | P(dead <=-80%) | EV multiple | Prob.-wtd cap $M | P(2x | chain>=+50%) | P(2x | chain>=+100%) | P(5x | chain>=+100%) | P(ATH | chain>=+100%) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHILLGUY | $13.0M | 53.2x | 11.9% | 7.3% | 4.4% | 2.3% | 0.8% | 0.1% | 64.3% | 39.5% | 0.93x | 12.1 | 21.4% | 26.2% | 9.0% | 0.3% |
| CHILLHOUSE | $1.5M | 19.5x | 10.5% | 6.5% | 3.9% | 2.0% | 0.8% | 0.3% | 72.5% | 48.7% | 0.81x | 1.2 | 14.3% | 16.9% | 5.8% | 0.9% |
| TROLL | $50.0M | 5.6x | 25.9% | 17.5% | 11.5% | 6.3% | 2.5% | 5.4% | 54.5% | 29.6% | 1.79x | 89.6 | 44.8% | 51.8% | 23.3% | 20.1% |
| TRIPLE T | $8.0M | 3.2x | 21.0% | 13.7% | 8.7% | 4.7% | 1.8% | 8.1% | 56.6% | 31.7% | 1.46x | 11.7 | 28.3% | 32.5% | 12.8% | 21.1% |
| CUPSEY | $6.5M | 3.2x | 14.8% | 9.4% | 5.8% | 3.0% | 1.1% | 5.3% | 63.2% | 38.0% | 1.09x | 7.1 | 20.2% | 23.5% | 8.5% | 14.3% |
| WOJAK (ETH) | $18.4M | 2.9x | 19.3% | 12.5% | 7.8% | 4.2% | 1.6% | 8.0% | 59.6% | 34.3% | 1.34x | 24.6 | 28.9% | 33.8% | 13.2% | 23.7% |

## 9. Summary table (Monte Carlo, Base blend)

| Token | P(>=+50%) | P(>=2x) | P(>=3x) | P(>=5x) | P(>=10x) | P(new ATH) | P(<=-50%) | P(dead) | EV | Median | P(2x | chain>=+50%) | P(2x | chain>=+100%) | P(5x | chain>=+100%) | P(ATH | chain>=+100%) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHILLGUY | 11.2% | 7.8% | 4.7% | 2.6% | 1.3% | 0.4% | 64.3% | 33.3% | 0.93x | 0.33x | 22.4% | 28.1% | 8.3% | 0.8% |
| CHILLHOUSE | 9.8% | 7.4% | 5.2% | 3.4% | 2.0% | 1.3% | 72.2% | 45.7% | 1.02x | 0.23x | 13.1% | 14.7% | 6.0% | 2.2% |
| TROLL | 23.7% | 19.3% | 14.3% | 9.7% | 5.9% | 8.9% | 53.9% | 33.0% | 2.30x | 0.42x | 38.4% | 43.8% | 22.4% | 20.5% |
| TRIPLE T | 19.3% | 15.2% | 10.9% | 7.1% | 4.3% | 10.4% | 56.1% | 31.8% | 1.83x | 0.40x | 25.2% | 27.8% | 12.9% | 19.0% |
| CUPSEY | 13.7% | 10.4% | 7.1% | 4.5% | 2.6% | 6.6% | 62.9% | 35.1% | 1.30x | 0.33x | 18.5% | 20.6% | 8.2% | 12.9% |
| WOJAK (ETH) | 17.7% | 13.9% | 9.8% | 6.5% | 3.9% | 10.0% | 59.0% | 34.2% | 1.69x | 0.36x | 25.4% | 28.2% | 13.0% | 20.5% |

## 10. Sensitivity of the unconditional token probabilities to the SOL/ETH blend

| Token | Blend | P(SOL/ETH >= +50%) | P(>=+50%) | P(>=2x) | P(>=5x) | P(new ATH) | P(<=-50%) | P(dead) | EV |
|---|---|---|---|---|---|---|---|---|---|
| CHILLGUY | Ottimistico | 24.4% | 13.4% | 8.4% | 2.7% | 0.1% | 62.2% | 37.9% | 1.02x |
| CHILLGUY | Base | 20.0% | 11.9% | 7.3% | 2.3% | 0.1% | 64.3% | 39.5% | 0.93x |
| CHILLGUY | Pessimistico | 14.8% | 9.9% | 6.0% | 1.8% | 0.1% | 67.6% | 42.2% | 0.81x |
| CHILLHOUSE | Ottimistico | 24.4% | 11.3% | 7.1% | 2.3% | 0.3% | 71.4% | 47.7% | 0.86x |
| CHILLHOUSE | Base | 20.0% | 10.5% | 6.5% | 2.0% | 0.3% | 72.5% | 48.7% | 0.81x |
| CHILLHOUSE | Pessimistico | 14.8% | 9.4% | 5.7% | 1.8% | 0.3% | 74.4% | 50.5% | 0.74x |
| TROLL | Ottimistico | 24.4% | 28.3% | 19.5% | 7.3% | 6.2% | 52.4% | 28.3% | 1.99x |
| TROLL | Base | 20.0% | 25.9% | 17.5% | 6.3% | 5.4% | 54.5% | 29.6% | 1.79x |
| TROLL | Pessimistico | 14.8% | 22.6% | 14.8% | 5.2% | 4.4% | 58.0% | 32.0% | 1.55x |
| TRIPLE T | Ottimistico | 24.4% | 22.3% | 14.8% | 5.1% | 8.9% | 55.3% | 30.8% | 1.56x |
| TRIPLE T | Base | 20.0% | 21.0% | 13.7% | 4.7% | 8.1% | 56.6% | 31.7% | 1.46x |
| TRIPLE T | Pessimistico | 14.8% | 19.1% | 12.3% | 4.1% | 7.2% | 58.8% | 33.2% | 1.34x |
| CUPSEY | Ottimistico | 24.4% | 15.9% | 10.2% | 3.4% | 5.8% | 61.9% | 37.0% | 1.16x |
| CUPSEY | Base | 20.0% | 14.8% | 9.4% | 3.0% | 5.3% | 63.2% | 38.0% | 1.09x |
| CUPSEY | Pessimistico | 14.8% | 13.4% | 8.3% | 2.7% | 4.7% | 65.2% | 39.7% | 1.00x |
| WOJAK (ETH) | Ottimistico | 23.9% | 20.9% | 13.7% | 4.7% | 9.0% | 58.1% | 33.3% | 1.45x |
| WOJAK (ETH) | Base | 19.3% | 19.3% | 12.5% | 4.2% | 8.0% | 59.6% | 34.3% | 1.34x |
| WOJAK (ETH) | Pessimistico | 13.9% | 17.2% | 10.9% | 3.5% | 6.9% | 62.2% | 36.3% | 1.20x |

## 11. Linkage effect: what a rally buys you (Base blend, scenario table)

Difference between P(>=2x | chain >= +100%) and P(>=2x | chain <= 0%) shows how much of each token's upside actually depends on the chain.

| Token | lambda | P(2x | chain <= 0%, scen. A+B) | P(2x | uncond.) | P(2x | chain >= +100%) | Ratio rally/no-rally |
|---|---|---|---|---|---|
| CHILLGUY | 0.8 | 2.5% | 7.3% | 26.2% | 10.4x |
| CHILLHOUSE | 0.5 | 3.8% | 6.5% | 16.9% | 4.5x |
| TROLL | 0.8 | 7.4% | 17.5% | 51.8% | 7.0x |
| TRIPLE T | 0.5 | 8.5% | 13.7% | 32.5% | 3.8x |
| CUPSEY | 0.5 | 5.6% | 9.4% | 23.5% | 4.2x |
| WOJAK (ETH) | 0.6 | 6.8% | 12.5% | 33.8% | 5.0x |


Written: /home/user/interface-smd/research_notes/Probabilità rialzo memecoin Solana 2027/risultati_probabilita.md
Written: /home/user/interface-smd/research_notes/Probabilità rialzo memecoin Solana 2027/risultati_probabilita.csv
Written: /home/user/interface-smd/research_notes/Probabilità rialzo memecoin Solana 2027/output_modello.txt
