# PEPE (Pepe the Frog memecoin, Ethereum, contract 0x6982508145454Ce325dDbE47a25d4ec3d2311933) — research notes as of 13 October 2026

Method note: all direct page fetches (WebFetch and curl via the proxy) failed with DNS/connection errors, so every figure below comes from search-engine snippets. Dates are those shown by the snippets; where a snippet was undated this is flagged. Price-prediction sites and paid press releases (openPR, CoinGabbar "Pepeto" promos, Bitget/MEXC news mirrors) are low-quality; they are cited only where nothing better exists and are labelled.

## Q1. Current situation (10–13 Oct 2026): price, market cap, FDV, volume, holders, liquidity, perp OI/funding

### Takeaway
As of 10–13 Oct 2026 PEPE trades at roughly $0.00000405–0.00000423 (4.05e-6 to 4.23e-6), market cap ≈ $1.67–1.78 bn (FDV identical because the full 420.69 T supply is circulating), 24h volume ≈ $156–207 M, ~592.5 k holders (2 Oct), futures open interest ≈ $323 M with slightly positive funding (2 Oct). PEPE is ~85–86 % below its December 2024 ATH and ranks ~#61 by market cap and #3–4 among memecoins.

### Cited Findings
- Price 13 Oct 2026: Coinbase $0.00000405 (1-week change −6.04 %); Kraken ≈ $0.0000042 with market cap $1,759,572,709; Bybit $0.00000423, 24h volume ≈ $207.27 M (timestamp 12 Oct); TokenPost: rally to $0.00000406 at 04:54 UTC 13 Oct after a daily loss; CoinGabbar citing CoinMarketCap $0.000004231, market value ≈ $1.75 bn — [Coinbase](https://www.coinbase.com/price/pepe); [Kraken](https://www.kraken.com/prices/pepe); [Bybit](https://www.bybit.com/en/price/pepe/); [TokenPost](https://tokenpost.com/news/investing/30823); [CoinGabbar (promo site, citing CMC)](https://www.coingabbar.com/en/pepe-coin-price-prediction-pepe-bounces-56-off-000000405)
- 12 Oct 2026 (Bybit page): total market cap $1.78 B, +5.29 % in 24h, ranked 61st overall on CoinMarketCap — [Bybit](https://www.bybit.com/en/price/pepe/)
- 11 Oct 2026 (MetaMask page): price $0.00000419, 24h range $0.00000398–0.00000424, market cap ≈ $1.76 bn, 24h volume ≈ $156 M; ATH listed as $0.00002803; price one month earlier (11 Sep 2026) $0.00000331 — [MetaMask](https://metamask.io/price/pepe)
- ~10 Oct 2026 (Coinbase, "three days old" per snippet): price ≈ $0.00000405, market cap ≈ $1.67 bn, ATH $0.00002829 (Dec 2024) — [Coinbase](https://www.coinbase.com/price/pepe)
- Blockworks: price ≈ $0.000004, market cap ≈ $1.65 bn (undated snapshot) — [Blockworks](https://blockworks.com/price/pepe)
- 7 Oct 2026: PEPE fell 5.52 % to ≈ $0.00000405, retesting a weekly trendline; support cited at $0.00000400–0.00000438 (CoinMarketCap AI news page) — [CoinMarketCap](https://coinmarketcap.com/cmc-ai/pepe/latest-updates/)
- 2 Oct 2026: futures open interest "edged marginally higher over the last 24 hours to $322.92 million" (CoinGlass data) with a positive funding rate of 0.0109 % — [FXStreet, 2 Oct 2026](https://www.fxstreet.com/cryptocurrencies/news/pepe-price-forecast-pepe-sustains-mild-recovery-on-firm-retail-support-202610020311); [Tradingpedia, 2 Oct 2026](https://www.tradingpedia.com/2026/10/02/pepe-coin-holds-firm-as-retail-traders-drive-demand/)
- CoinGlass cached PEPE futures pages (undated) show OI of ≈ $154.3 M and ≈ $229.9 M on different captures; the 1000PEPE contract page shows ≈ $133.7 M; Coinalyze (coin/stable-margined only) shows $38.5 M — [CoinGlass PEPE futures](https://www.coinglass.com/currencies/PEPE/futures); [CoinGlass 1000PEPE](https://www.coinglass.com/currencies/1000PEPE); [Coinalyze](https://coinalyze.net/pepe/open-interest/)
- Holders: Etherscan token page snapshot 2 Oct 2026 07:40 UTC shows 592,524 holders and "Onchain Market Cap: $1,901,518,346.40" — [Etherscan](https://etherscan.io/token/0x6982508145454ce325ddbe47a25d4ec3d2311933)
- Holders: 587,300 addresses as of 13 Sep 2026 (article citing Etherscan); same article says top-10 wallets hold 77.04 % of supply — [CoinGabbar (promo site)](https://www.coingabbar.com/en/pepe-price-prediction-2026-pepe-eyes-major-breakout)
- 3 Oct 2026: Crypto Times reported the token price "drops nearly 7 %" after the ETF amendment, citing ≈ $0.0000054; CoinGabbar on the same news cited $0.000004253 — conflicting; the $0.0000054 figure is inconsistent with every other early-October reading — [Crypto Times, 3 Oct 2026](https://www.cryptotimes.io/2026/10/03/canary-amends-pepe-etf-filing-as-token-price-drops-nearly-7/); [CoinGabbar](https://www.coingabbar.com/en/canary-pepe-etf-amended-what-the-filing-says-about-launch)
- CoinGecko's "pepe-token" page returned in search ($0.0003061, cap ≈ $225 k, volume $52) is a different token ("Pepe Community"), not PEPE — [CoinGecko (wrong token)](https://www.coingecko.com/en/coins/pepe-token)

### Inferences
- Consensus mid-October 2026 snapshot: price ≈ $0.0000041 ± 0.0000001, market cap ≈ $1.72 bn, FDV = market cap (fixed, fully circulating supply), daily spot volume $150–210 M (≈ 9–12 % of market cap, high turnover typical of memecoins).
- OI/market-cap ratio ≈ 0.19 ($323 M / $1.7 bn), i.e. leverage is large relative to the float — consistent with the liquidation-driven moves of Sept–Oct 2026.
- Holder count drifted up ≈ +0.9 % between 13 Sep and 2 Oct 2026 (587.3 k → 592.5 k), a slow but positive trend.
- Etherscan's $1.90 bn on-chain cap on 2 Oct implies a price near $0.0000045 that day, i.e. PEPE lost ~8–10 % between 2 Oct and 10–13 Oct.

### Gaps
- No DEX-liquidity (Uniswap PEPE/WETH TVL, DexScreener) figure found: the only results were block-explorer pool pages with implausible or templated numbers ($44, $19) and look-alike contracts; treat DEX liquidity as not found.
- No exchange-by-exchange OI breakdown, long/short ratio or liquidation totals for 10–13 Oct 2026.
- No reading for 13 Oct from CoinGecko/CoinMarketCap directly (pages not fetchable).

## Q2. Origin, history and full price history (ATH, ATL, yearly highs/lows, drawdown)

### Takeaway
PEPE launched 14 April 2023 as a no-utility ERC-20 by an anonymous team, listed on Binance on 5 May 2023, suffered a "team dump" of 16 T tokens in August 2023, set its ATH of $0.00002825 on 9 Dec 2024 (market cap > $11 bn), then fell ~79 % in 2025 (high $0.0000219 / low $0.0000030) and has traded in a $0.0000022–0.0000053 band in 2026; current drawdown from ATH ≈ 85–86 %. It made no new highs in 2025 or 2026.

### Cited Findings
**Origin / 2023**
- ATL $0.000000055142 recorded 18 Apr 2023 (four days after launch); CoinGlass lists 18 Apr 2023 as the largest single-day gain (+182.80 %) and largest intraday range (+260.37 %) in the token's history — [MEXC news](https://www.mexc.com/news/937713); [CoinGlass historical data](https://www.coinglass.com/currencies/PEPE/historical-data)
- Binance listed PEPE and FLOKI in its Innovation Zone on 5 May 2023 (spot pairs USDT and TUSD, trading from 16:00 UTC); PEPE rose 41 % within an hour and market cap passed $1 bn; Binance's listing note warned PEPE "had no utility or value-support mechanism" and that insiders appeared to have bought ~7 % of supply shortly after creation — [ForkLog](https://forklog.com/en/binance-lists-pepe-and-floki-in-the-innovation-zone/); [Decrypt, May 2023](https://decrypt.co/139010/liam-binance-lists-pepe-meme-coin-market-cap-hits-1-billion); [Benzinga](https://benzinga.com/markets/cryptocurrency/23/05/32243753/pepe-and-floki-join-binance-will-these-meme-coins-dethrone-dogecoin-shiba-inu)
- Launch allocation: 93.1 % of the 420.69 T supply to the Uniswap pool (LP tokens burned), 6.9 % to a multisig for CEX listings/bridges/liquidity — [Datawallet](https://www.datawallet.com/crypto/what-is-pepe-coin); [Binance Square](https://www.binance.com/en/square/post/16379252698121)
- "Team dump", 24–25 Aug 2023: ≈ 16 T PEPE (~$15 M, ~4 % of supply, ~60 % of the multisig's holdings) was sent from the multisig to OKX, Binance, KuCoin and Bybit and sold; the multisig threshold had been changed from 5/8 to 2/8; the team blamed three ex-members; ~10 T remained; price fell 18–20 % on 25 Aug 2023 — [The Block, 26 Aug 2023](https://www.theblock.co/news/ecosystems/2023-08-26-pepe-team-members-stole-15-million-from-multisig-247576); [Techflow](https://www.techflowpost.com/en-US/article/12823); [AMBCrypto](https://ambcrypto.com/whats-behind-pepes-recent-dump/amp/)
- Kaiko on the August 2023 dump: PEPE fell ~20 % but CEX liquidity "remained steady", with $300 k more bids than asks within 0.5 % of mid — [Kaiko](https://www.kaiko.com/resources/pepe-plunges-as-founders-sell)
- 24 Oct 2023: 6.9 T PEPE (≈ $5.5 M, 1.6 % of supply) burned from the multisig, price +31 % — [CoinDesk, 24 Oct 2023](https://www.coindesk.com/business/2023/10/24/pepe-memecoin-burns-55m-tokens-prompting-31-rise)
- Creator identity: in Aug 2023 Pauly (NotLarvaLabs) named Zachary Testa (@degenharambe) as creator and alleged an $865 k Lamborghini purchase and zero payment to Matt Furie; claims were unverified and disputed — [Techflow](https://www.techflowpost.com/en-US/article/12823); [Bittime](https://www.bittime.com/en/blog/siapa-pencipta-pepe-pepe-dan-apa-alasannya)

**2024**
- Market cap ≈ $591 M at the start of 2024 — [Cointelegraph, Dec 2024](https://cointelegraph.com/news/pepe-memecoin-flips-uniswap-market-cap)
- 14 Mar 2024 ATH $0.00001064 (ETH-memecoin rally) — [MEXC news](https://www.mexc.com/news/715997)
- 27 May 2024 ATH $0.00001725 after US spot-ETH-ETF approval (+88 % since 20 May) — [Cointelegraph, 27 May 2024](https://cointelegraph.com/news/pepe-memecoin-hits-record-high-risks-40-crash-june)
- ~1 Nov 2024: PEPE at $0.000009554, 43 % below its then-peak of $0.00001718 — [Watcher.guru, Nov 2024](https://watcher.guru/news/pepe-coin-how-high-can-pepe-surge-in-november-2024)
- 7 Dec 2024: market cap topped $11 bn (≈ 18× the January level); Decrypt: $11.37 bn, flipping UNI and LTC — [Cointelegraph](https://cointelegraph.com/news/pepe-memecoin-flips-uniswap-market-cap); [Decrypt](https://rhino.decrypt.co/295502/pepe-flips-uni-and-ltc-surges-past-11-billion-market-cap-to-new-record?amp=1)
- ATH $0.00002825 on 9 Dec 2024 (CoinMarketCap, CoinGlass); variants: $0.00002824 (Mudrex), $0.00002803 (MetaMask), $0.00002829 (Coinbase), $0.0000275 (CCN/FXStreet intraday reports) — [CoinMarketCap](https://coinmarketcap.com/currencies/Pepe/); [CoinGlass](https://www.coinglass.com/currencies/PEPE/historical-data); [FXStreet, 9 Dec 2024](https://www.fxstreet.com/cryptocurrencies/news/pepe-meme-coin-hits-new-all-time-high-with-market-cap-surpassing-11-billion-202412090742); [Mudrex](https://mudrex.com/learn/pepe-price-prediction-2024-2025-2030-and-beyond/)

**2025**
- CoinLore yearly table: 2025 high $0.0000219, low $0.0000030, average ≈ $0.0000096; open ≈ $0.0000194 → close ≈ $0.0000040, i.e. ≈ −79 %; worst months Feb −42.7 %, Nov −30.9 %, Jan −30.7 %, Oct −29.7 %; best months May +31.1 %, Apr +23.5 % — [CoinLore](https://www.coinlore.com/coin/pepe); [CoinLore historical](https://www.coinlore.com/coin/pepe/historical-data)
- 30 Apr 2025: ≈ $0.00000879 after weeks of sideways trading — [Capital.com citing cryptoticker](https://capital.com/en-eu/analysis/pepe-price-prediction)
- Mid-Aug 2025: −44.5 % year-to-date — [Capital.com](https://capital.com/en-int/analysis/pepe-price-prediction)
- 14 Aug 2025: "PEPE drops 4 % as memecoin sector underperforms broader crypto market" — [CoinDesk, 14 Aug 2025](https://www.coindesk.com/markets/2025/08/14/pepe-drops-4-as-memecoin-sector-underperforms-broader-crypto-market)
- 10 Oct 2025 (tariff-driven crash, ~$19 bn market-wide liquidations): PEPE crashed to $0.0000065, lowest since Feb 2024, with > $20 M PEPE liquidations; still −17.6 % from 1 Oct as of 13 Oct 2025 — [MEXC news](https://www.mexc.com/news/129400); [OneSafe](https://www.onesafe.io/blog/pepe-coin-analysis-market-crash)
- 29 Oct 2025: market cap had fallen from ≈ $10 bn to $2.9 bn ("$7.1 bn wipeout") — [Bankless Times, 29 Oct 2025](https://www.banklesstimes.com/articles/2025/10/29/pepe-coin-price-crash-and-the-7-1-billion-wipeout-explained/)
- Year-end 2025: PEPE ended 2025 below $0.000004 — [Cryptopolitan](https://www.cryptopolitan.com/pepe-price-prediction/)

**2026**
- 2 Jan 2026: +≈ 26 % in a day to ≈ $0.000005106; futures OI +82 % to ≈ $446.5 M; 24h volume > $800 M (another source $932.6 M, +419 %) — [Yellow.com (FR)](https://yellow.com/fr/news/le-meme-coin-pepe-bondit-de-26-tandis-que-le-volume-d’échanges-grimpe-de-plus-de-400-); [CoinGape](https://coingape.com/markets/pepe-coin-price-enters-2026-with-a-25-surge-as-open-interest-jumps-82-whats-next/); [MEXC news](https://www.mexc.com/news/392082)
- 11 Feb 2026: ≈ $0.0000036 (−6 % on the day); Santiment: top-100 wallets accumulated 23.02 T PEPE over four months since the October sell-off; token −73 % from its peak ~9 months earlier; daily chart in lower highs/lower lows, RSI mid-30s — [MEXC news](https://www.mexc.com/news/686402); [Yahoo Finance](https://finance.yahoo.com/news/whales-accumulate-23-trillion-pepe-104225124.html); [crypto.news](https://crypto.news/pepe-coin-price-tests-support-whales-accumulate-2026/)
- 14–15 Feb 2026: +24 % to ≈ $0.00000472 then +29 % to ≈ $0.00000487; "83.2 % below ATH of $0.00002803" — [MEXC news](https://www.mexc.com/news/940333)
- 1 Mar 2026: $0.0000037, −85.5 % from the Dec 2024 peak; 4 Mar 2026 (MEXC page): $0.000003598, 24h range $0.000003345–0.0000036; 16 Mar 2026: +21 % to a two-week high ≈ $0.0000040 — [MEXC news](https://www.mexc.com/news/825589); [MEXC price page](https://www.mexc.com/en-US/price/PEPE); [MEXC news](https://www.mexc.com/news/716940)
- 8 Apr 2026: Canary S-1 filed; FXStreet "Why is PEPE price rallying today? open interest surge backs bullish breakout" — [FXStreet, 8 Apr 2026](https://www.fxstreet.com/cryptocurrencies/news/pepe-price-forecast-open-interest-surge-backs-bullish-breakout-setup-202604080529)
- April 2026: PEPE ≈ $0.0000038 (−4.91 %) when a whale withdrew 800 B from Coinbase Prime — [MEXC news](https://www.mexc.com/news/1054442)
- May 2026: ≈ $0.00000405, CoinGecko market cap ≈ $1.7 bn — [The Portugal News, 18 May 2026](https://www.theportugalnews.com/news/2026-05-18/pepe-price-prediction-pepe-vs-new-meme-coin-presales/1022598)
- 13 Jun 2026: ≈ $0.0000028 (+2.3 % on the day), support $0.00000272 — [CoinReporter, Jun 2026](https://www.coinreporter.io/2026/06/pepe-price-prediction-2026-2032-will-pepe-coin-dominate-dogecoin-and-shiba-inu-in-2026/)
- 1 Jul 2026: "recent monthly low reached $0.00000225 on July 1" (prediction site, low quality) — [StealthEx](https://stealthex.io/blog/pepe-coin-price-prediction/)
- 21 Aug 2026: FXStreet "whale activity, retail speculation fuel fresh PEPE rally" — [FXStreet, 21 Aug 2026](https://www.fxstreet.com/cryptocurrencies/news/pepe-price-forecast-whale-activity-retail-speculation-fuel-fresh-pepe-rally-202608210525)
- 11 Sep 2026: $0.00000331 — [MetaMask](https://metamask.io/price/pepe)
- 21–22 Sep 2026: PEPE +22.2 % in 24h to $0.0000049 (TheStreet), ≈ +25 % single-day on 21 Sep amid a $919 M wave of short liquidations as BTC broke $85,000; weekly gain > 40 % (≈ 42–45 %), briefly $0.00000515 and market cap > $2 bn; Invezz: $4.09 M PEPE liquidations in 24h ($2.33 M shorts), OI +30 %; no project-specific catalyst — [TheStreet](https://www.thestreet.com/crypto/markets/pepe-surges-22-leading-bitcoin-dogecoin-xrp-?.tsrc=rss); [BigGo Finance](https://finance.biggo.com/news/d311428d-c7b7-44ad-8be3-420e926934d8); [Invezz, 22 Sep 2026](https://invezz.com/news/2026/09/22/pepe-price-jumps-nearly-15-as-short-squeeze-fuels-rally/); [CoinGape](https://coingape.com/markets/what-is-driving-the-pepe-coin-price-rally-of-30-today/)
- MetaMask: local highs near $0.0000053 in September before consolidating at $0.0000043–0.0000045; attributed to > $900 M short liquidations and BTC's move — [MetaMask](https://metamask.io/price/pepe)
- 24 Sep 2026: −13 % in 24h after the ~45 % weekly rally; memecoins underperformed majors in a risk-off session — [CoinMarketCap, 24 Sep 2026](https://coinmarketcap.com/top-stories/6ab4b3fa9b764f5d2ecae6ea/)
- 2 Oct 2026: "mild recovery", OI $322.92 M — [FXStreet](https://www.fxstreet.com/cryptocurrencies/news/pepe-price-forecast-pepe-sustains-mild-recovery-on-firm-retail-support-202610020311)
- 7 Oct 2026: −5.52 % to ≈ $0.00000405; 12–13 Oct: $0.00000405–0.00000423 (see Q1)

### Inferences
- Drawdown from ATH now: $0.00000405–0.00000423 vs $0.00002825 → −85.0 % to −85.7 % (≈ −86 %).
- 2026 range so far: low ≈ $0.00000225 (1 Jul, weakly sourced) / ≈ $0.0000028 (mid-June, better sourced); highs ≈ $0.0000051 (2 Jan) and ≈ $0.0000051–0.0000053 (21–22 Sep). PEPE has made no new ATH since 9 Dec 2024; the 2025 high ($0.0000219) was set in early January 2025 and 2026 highs are ~80 % below the ATH.
- 2024 was ≈ +18× in market cap (Jan → early Dec); 2025 ≈ −79 %; 2026 year-to-date (≈ $0.0000040 at end-2025 → ≈ $0.0000041 on 13 Oct) is roughly flat, masking a −45 % drawdown into June/July and a +130 % rebound into late September.
- The early-June 2026 "$0.000013" reading on iTokenly conflicts by ~4× with all other June data and is almost certainly an error.

### Gaps
- Exact June 2026 daily low not found (best evidence: ≈ $0.0000028 on 13 Jun with $0.00000272 support; $0.00000225 on 1 Jul from a low-quality site).
- Exact 2025 Q2 and Q3 peaks (e.g., May and July 2025 highs) not found; only CoinLore monthly percentages.
- Exact date of the 2025 low ($0.0000030, likely Nov–Dec 2025) not confirmed.

## Q3. Exchange and product coverage: spot/perp listings, ETF/ETP status, Robinhood

### Takeaway
PEPE has spot and perpetual coverage on all major venues (Binance spot since 5 May 2023 and 1000PEPE perps; Coinbase International perps since Apr 2024 and Coinbase/Robinhood US spot since Nov 2024; Kraken Pro perps outside the US; Bybit). A US spot PEPE ETF (Canary Capital) is filed (S-1 8 Apr 2026, S-1/A 2 Oct 2026, Cboe BZX, BitGo custody) but not effective or launched; no REX-Osprey, Grayscale or 21Shares PEPE product was found; the only listed PEPE product is Valour's SEK-denominated ETP in Sweden.

### Cited Findings
- Binance spot listing 5 May 2023, Innovation Zone, USDT/TUSD pairs (see Q2) — [ForkLog](https://forklog.com/en/binance-lists-pepe-and-floki-in-the-innovation-zone/)
- Binance Futures runs a USDT-margined 1000PEPEUSDT perpetual (leverage/margin tier updates 8 May 2024 and 2 Aug 2024) and launched a 1000PEPEUSDC perpetual with up to 50× leverage on 7 Mar 2024 — [ChainCatcher](https://www.chaincatcher.com/en/article/2123340); [Blockchain.news](https://blockchain.news/zh/news/binance-futures-adjusts-leverage-margin-tiers); [MEXC news](https://www.mexc.com/news/697957)
- Coinbase International Exchange launched PEPE perpetual futures on 18 Apr 2024 — [CoinDesk, 11 Apr 2024](https://www.coindesk.com/markets/2024/04/11/pepe-coin-spikes-on-coinbase-international-plan-to-list-perpetual-futures); [crypto.news](https://crypto.news/coinbase-perpetual-futures-pepe/)
- Robinhood listed PEPE for US customers in Nov 2024; Coinbase added PEPE to its spot listing roadmap the same day and subsequently listed it — [CoinGape](https://coingape.com/pepe-coin-set-to-be-listed-on-coinbase-following-robinhood-listing/); [Cryptorank](https://cryptorank.io/news/feed/11bb7-coinbase-officially-lists-pepe)
- Coinbase offers "perpetual-style" US futures (5-year expiry, up to 10×) and the CFTC's move to allow true US perpetuals was still pending as of 22 Apr 2026; Robinhood said it is exploring US perpetuals — [BNN Bloomberg, 22 Apr 2026](https://www.bnnbloomberg.ca/markets/crypto/2026/04/22/crypto-exchanges-gear-up-to-launch-us-perpetual-futures-ahead-of-rule-change/); [Finimize](https://finimize.com/content/us-crypto-exchanges-gear-up-to-offer-perpetual-futures)
- Kraken: PEPE/USD perpetual futures on Kraken Pro for most non-US regions; Kraken's page also mentions CME-listed futures access for US clients via Kraken Derivatives US, but Kraken Derivatives US (launched July 2025) initially offered BTC/ETH/SOL CME futures and no CME PEPE contract was found — [Kraken futures page](https://www.kraken.com/features/futures/pepe); [BusinessWire, 15 Jul 2025](https://www.businesswire.com/news/home/20250715200422/en/Kraken-Launches-US-Regulated-Derivatives-Offering-Creating-Unified-Access-to-Futures-and-Crypto-Spot-Markets)
- Bybit lists PEPE (spot price page); CoinGlass tracks both PEPE and 1000PEPE futures contracts across exchanges — [Bybit](https://www.bybit.com/en/price/pepe/); [CoinGlass](https://www.coinglass.com/currencies/PEPE)
- Canary Capital filed an S-1 for a spot PEPE ETF on 8 Apr 2026 (fund holds PEPE directly plus a small ETH allocation for gas) — [crypto.news](https://crypto.news/canary-capital-files-s-1-to-launch-spot-pepe-etf/); [The Defiant](https://thedefiant.io/news/regulation/canary-capital-pepe-etf-sec-filing-jwlmse); [DL News](https://www.dlnews.com/articles/markets/why-investors-want-a-pepe-memecoin-etf/)
- Canary PEPE ETF Pre-Effective Amendment No. 1 (S-1/A) filed 2 Oct 2026: Delaware statutory trust, listing on Cboe BZX, BitGo Bank & Trust as PEPE custodian, U.S. Bank as cash custodian, 10,000-share creation baskets, NAV from the CoinDesk PEPE Benchmark Rate (60m NY Rate), no ticker, not a '40 Act fund; shares cannot be sold until the SEC declares the registration effective; no launch date — [SEC EDGAR S-1/A, 2 Oct 2026](https://www.sec.gov/Archives/edgar/data/0002109686/000199937126022017/canarypepe-s1a_100226.htm); [GNCrypto](https://www.gncrypto.news/news/canary-pepe-etf-filing-cboe-listing-plan/); [CoinGabbar](https://www.coingabbar.com/en/canary-pepe-etf-amended-what-the-filing-says-about-launch)
- The filing itself flags holder concentration as a risk: the ten largest wallets held ≈ 41 % of circulating supply as of early 2026 — [Datawallet](https://www.datawallet.com/crypto/what-is-pepe-coin)
- Eric Balchunas (Bloomberg ETF analyst) commented the filing signals a shift in crypto sentiment; coverage stresses it "shows ambition, not approval" — [CoinGabbar](https://www.coingabbar.com/en/canary-pepe-etf-amended-what-the-filing-says-about-launch)
- REX-Osprey appears in coverage only as issuer of other memecoin funds (DOGE, BONK, TRUMP); no REX-Osprey PEPE product found — [DL News](https://www.dlnews.com/articles/markets/why-investors-want-a-pepe-memecoin-etf/); [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/canary-files-pepe-etf-crypto-152800045.html)
- Europe: Valour (DeFi Technologies) listed a PEPE ETP (SEK-denominated, 1.9 % fee, fully backed, Copper custody) on Sweden's Spotlight Stock Market alongside FLOKI; 21Shares has DOGE but no PEPE ETP found; MarketVector Meme Coin Index (MEMECOIN, 2024) includes PEPE — [Yahoo Finance](https://finance.yahoo.com/news/floki-pepe-crypto-etps-debut-144132171.html); [Valour product page](https://valour.com/en/products/valour-pepe-sek); [ETF Stream](https://www.etfstream.com/de/etf-screener/VALOUR_PEPE)

### Inferences
- PEPE's product stack (CEX spot + perps everywhere, US retail via Robinhood/Coinbase, a pending US spot ETF, a Swedish ETP) is the deepest of any Ethereum memecoin and rivals only DOGE/SHIB; this is the main structural reason it functions as the sector bellwether.
- Approval odds are uncertain: the S-1/A moved the filing forward (exchange/custodian named) but nothing suggests imminent effectiveness; the Oct 2025–Oct 2026 memecoin drawdown and the SEC's broader caution are headwinds.

### Gaps
- Could not confirm OKX spot/perp listing details, Robinhood's current PEPE availability in 2026 (only the Nov 2024 listing is sourced), or Grayscale (no PEPE product found; results were Grayscale XRP filings).
- Valour PEPE ETP AUM not found.

## Q4. Tokenomics, holder concentration, exchange holdings, whale flows (2026)

### Takeaway
Fixed 420.69 T supply, no mint/tax/staking, one meaningful burn (6.9 T in Oct 2023); trackers treat the full supply as circulating. Concentration is high but definitions differ (top-10 = 41 % of circulating per the ETF filing, early 2026; 77 % per an Etherscan-based count in Sept 2026 that likely includes exchange hot wallets). 2026 whale data (Santiment/Lookonchain/Arkham) show net accumulation and CEX outflows: 23 T bought by top-100 wallets Oct 2025–Feb 2026, a record 4.54 T single-day CEX outflow in Aug 2026, top-100 non-exchange wallets ≈ 86 T.

### Cited Findings
- Total supply 420.69 T; 93.1 % to Uniswap LP (LP burned), 6.9 % multisig; 6.9 T (1.6 %) burned Oct 2023; no transaction tax, no ongoing burn mechanism (some Binance Square posts claim periodic burns or a "$1 billion burn" — unverified) — [Datawallet](https://www.datawallet.com/crypto/what-is-pepe-coin); [cryptint](https://cryptint.io/declassified/coins/pepe); [CoinDesk, 24 Oct 2023](https://www.coindesk.com/business/2023/10/24/pepe-memecoin-burns-55m-tokens-prompting-31-rise); [Binance Square (unverified)](https://www.binance.com/en/square/post/17479024070498)
- ≈ 420.56 T ERC-20 PEPE unlocked on Ethereum = 99.97 % of supply (Dec 2024) — [MEXC tokenomics page](https://www.mexc.com/ru-RU/price/PEPE/tokenomics)
- PEPE has no staking, fee-payment, collateral or voting mechanism — [altFINS](https://altfins.com/crypto-screener/pepe-pepe)
- Top-10 wallets ≈ 41 % of circulating supply (early 2026, cited from the ETF filing's risk factors) — [Datawallet](https://www.datawallet.com/crypto/what-is-pepe-coin)
- Top-10 wallets 77.04 % of supply, 587,300 holders (13 Sep 2026, Etherscan-based, promo site) — [CoinGabbar](https://www.coingabbar.com/en/pepe-price-prediction-2026-pepe-eyes-major-breakout)
- Exchange supply (historical): 40.74 % of total supply on exchanges in Jan 2024 (Santiment, highest since Oct 2023); 160.02 T on exchanges in Jun 2023 (ATH); 169.93 T as of 15 Jun 2024 — [FXStreet, Jan 2024](https://www.fxstreet.com/cryptocurrencies/news/pepe-selling-pressure-mounts-as-whale-deposits-two-trillion-pepe-to-binance-202401121244); [FXStreet, Jun 2024](https://www.fxstreet.com/amp/cryptocurrencies/news/pepe-holders-distribute-their-tokens-after-massive-profit-taking-for-30-days-202406151200); [FXStreet, Jun 2023](https://www.fxstreet.com/cryptocurrencies/news/pepe-supply-on-exchanges-hits-all-time-high-as-secs-regulatory-crackdown-widens-202306061509)
- Aug 2026 (Santiment via CMC/MetaMask): net 4.54 T PEPE left centralized exchanges in one day, the largest single-day outflow since Nov 2024; top-100 wallets grew holdings > 6 % in 30 days to ≈ 86 T; CMC rated the signal "neutral", noting price ~90 % below ATH and months of sideways trading — [CoinMarketCap AI updates](https://coinmarketcap.com/cmc-ai/pepe/latest-updates/); [MetaMask](https://metamask.io/price/pepe)
- 11 Feb 2026 (Santiment): top-100 wallets accumulated 23.02 T PEPE over four months since the Oct 2025 sell-off — [Yahoo Finance](https://finance.yahoo.com/news/whales-accumulate-23-trillion-pepe-104225124.html); [CryptoPotato](https://cryptopotato.com/is-pepe-ready-to-explode-whales-load-up-23-trillion-tokens/)
- Santiment: PEPE among tokens with a 620 % surge in $100k+ transactions in early Jan 2026 — [CoinGabbar](https://www.coingabbar.com/en/price-prediction/pepe-price-prediction-2026-bull-bear-target-analysis)
- Arkham-tracked sale (article ≈ Jan–Feb 2026): a holder of 1.7 T PEPE since October sold 858 B (≈ $3.88 M), retaining ≈ 842 B — [Bitget news](https://www.bitget.com/news/detail/12560605177534)
- Arkham-tracked accumulation (article ≈ Nov 2025): a wallet added ≈ $9 M of PEPE since 6 Nov — [Coinpaper](https://coinpaper.com/12363/is-pepe-gearing-up-for-a-comeback-after-9-m-whale-accumulation)
- Apr 2026 (Lookonchain): whale withdrew 800 B PEPE (≈ $3.08 M) from Coinbase Prime, first withdrawal in eight months — [MEXC news](https://www.mexc.com/news/1054442)
- May 2026 (Lookonchain): a trader opened a 10× leveraged long on PEPE worth ≈ $4.62 M (snippet says "1.31 billion PEPE", which at $4.62 M implies 1.31 T; figure inconsistent); a "100 % win-rate" whale moved remaining PEPE to Bitget with an estimated cumulative loss of $17.12 M — [Lookonchain PEPE feed](https://www.lookonchain.com/token/pepe)
- Jul 2026 (Lookonchain): 11 associated addresses cumulatively bought 1.299 T PEPE (≈ $3.58 M) — [Lookonchain PEPE feed](https://www.lookonchain.com/token/pepe)
- Lookonchain feed item: "A whale address bought 6,008.8 billion PEPE 8 hours ago" (2025, undated) — [Lookonchain](https://www.lookonchain.com/feeds/32519)
- Binance's 2023 listing note: insiders appeared to have bought ≈ 7 % of supply shortly after creation — [Decrypt](https://decrypt.co/139010/liam-binance-lists-pepe-meme-coin-market-cap-hits-1-billion)

### Inferences
- The 77 % vs 41 % top-10 discrepancy is explained by whether exchange hot wallets (Binance, Coinbase, OKX, Bybit, Robinhood) are counted: the raw Etherscan top-10 is dominated by CEX addresses, so ~77 % overstates "whale" concentration while ~41 % (ETF filing) is the better investor-facing figure. Either way concentration is far above DOGE's.
- Top-100 non-exchange wallets at ≈ 86 T ≈ 20 % of supply (Aug 2026), up from ≈ 63 T four months before the Feb 2026 reading, consistent with whales buying the 2025–26 drawdown.
- Supply-tracker circulating figure (420.69 T) appears not to deduct the Oct 2023 6.9 T burn; true outstanding supply ≈ 413.8 T. This matters marginally (<2 %) for FDV.

### Gaps
- No 2026 figure for share of supply held on exchanges (last Santiment % is Jan 2024) or for Binance's specific balance; Arkham entity balances not fetchable.
- No Nansen smart-money data found for PEPE in 2026.
- Could not verify the 1.31 B/1.31 T leveraged-long figure.

## Q5. Social / on-chain metrics (holders trend, X/Telegram, social dominance, Google Trends)

### Takeaway
Holders ≈ 592.5 k (2 Oct 2026) and slowly rising; the PEPE X account is cited at ≈ 670 k followers (undated); social-dominance readings are dated (LunarCrush 2.9 % vs SHIB 1.7 %; Santiment 3.55 % peak in May 2024); overall crypto social chatter was at a two-year low in Feb 2026. No 2026 Santiment social-dominance or Google Trends reading specific to PEPE was found.

### Cited Findings
- Holders 592,524 (2 Oct 2026) — [Etherscan](https://etherscan.io/token/0x6982508145454ce325ddbe47a25d4ec3d2311933); 587,300 (13 Sep 2026) — [CoinGabbar](https://www.coingabbar.com/en/pepe-price-prediction-2026-pepe-eyes-major-breakout)
- X followers ≈ 669,940 for the PEPE token account (undated tracker) — [AlphaGrowth](https://alphagrowth.io/pepe)
- Social dominance 2.9 % vs SHIB 1.7 % (LunarCrush, undated/months old) — [Coinspeaker](https://www.coinspeaker.com/guides/pepe-price-prediction/)
- Santiment social dominance rose from 0.81 % to 3.55 % in one week during the May 2024 rally (historical) — [FXStreet, May 2024](https://www.fxstreet.com/cryptocurrencies/news/pepe-hits-new-all-time-high-meme-coin-could-extend-gains-202405271404)
- Crypto-wide: altcoin social conversation at a two-year low in late Feb 2026; Google Trends "altcoin" scored 4/100 vs 100 in mid-Aug 2025 (press release) — [openPR, Mar 2026](https://www.openpr.com/news/4303702/pepe-coin-s-meme-dominance-fades-as-2026-forecasts-spotlight)
- "Pepe Miner" Telegram bot: 4.7 M users, 820 k community (a game bot, not the token community) — [KuCoin Learn](https://kucoin.com/learn/crypto/what-is-pepe-miner-telegram-bot-and-how-to-mine-pepe-in-it)
- Oct 2026 sentiment: CMC "PEPE surges 3.02 % on whale accumulation and social buzz" (undated 2026 page) — [CoinMarketCap](https://coinmarketcap.com/top-stories/6a76b8eca24887465daea7d0/)

### Inferences
- Holder growth of ~5 k/month in a −85 % drawdown indicates a sticky retail base; by holder count PEPE (≈ 593 k) is below BRETT (≈ 891 k, Base) but the comparison across chains is weak.

### Gaps
- No official Telegram/Discord size for PEPE; no PEPE-specific Google Trends index for 2026; no Santiment 2026 social dominance value.

## Q6. Performance relative to ETH/BTC in rallies (beta/correlation estimates); new highs?

### Takeaway
PEPE behaves as a high-beta ETH/BTC proxy on the upside and downside: ≈ 18× in 2024 vs ETH's roughly 1.5×; ≈ −79 % in 2025; in 2026 it fell to ≈ $0.0000022–0.0000028 while ETH bottomed near $1,450–1,570 in June, then rose ≈ +90–135 % to ≈ $0.0000053 while ETH recovered ≈ +74 % to ≈ $2,716 in late September — an upside beta of roughly 1.3–1.8× on that leg. No new PEPE high in 2025 or 2026.

### Cited Findings
- Oct–Dec 2024: PEPE ≈ $0.0000096 on ~1 Nov 2024 → ATH $0.00002825 on 9 Dec 2024 (≈ +196 %); market cap $591 M (Jan 2024) → $11 bn (7 Dec 2024), ≈ 18× — [Watcher.guru](https://watcher.guru/news/pepe-coin-how-high-can-pepe-surge-in-november-2024); [CoinMarketCap](https://coinmarketcap.com/currencies/Pepe/); [Cointelegraph](https://cointelegraph.com/news/pepe-memecoin-flips-uniswap-market-cap)
- 2024 ETH-catalyst sensitivity: +88 % in a week after the 20 May 2024 ETH-ETF approvals; +27 % in a day on ETH-ETF speculation — [Cointelegraph, 27 May 2024](https://cointelegraph.com/news/pepe-memecoin-hits-record-high-risks-40-crash-june); [Cointelegraph](https://cointelegraph.com/news/pepe-all-time-high-ethereum-etf-speculation)
- "PEPE price rallies 300 % as Ethereum crossed $4k" (FXEmpire, 2024 Ethereum-memecoin rally) — [FXEmpire](https://fxempire.com/forecasts/article/pepe-price-rallies-300-as-ethereum-crossed-4k-more-gains-ahead-1415373)
- 2025: PEPE −79 % open-to-close; monthly +23.5 % (Apr) and +31.1 % (May) during the Q2 2025 risk rebound; Aug 2025 memecoin sector underperformed broader crypto — [CoinLore](https://www.coinlore.com/coin/pepe); [CoinDesk, 14 Aug 2025](https://www.coindesk.com/markets/2025/08/14/pepe-drops-4-as-memecoin-sector-underperforms-broader-crypto-market)
- 10 Oct 2025 crash: PEPE to $0.0000065 (lowest since Feb 2024), > $20 M PEPE liquidations within a $19 bn market-wide liquidation — [MEXC news](https://www.mexc.com/news/129400)
- June 2026 ETH drop: ETH ≈ $1,557 after a −3.87 % day (low $1,531), with "June's absolute lows near $1,450" (Cryptopolitan, undated June page); ≈ $1,568 on 27 Jun 2026 (MEXC); ≈ $1,500–1,505 in early June (Octagon) — [Cryptopolitan](https://www.cryptopolitan.com/ethereum-price-prediction/); [MEXC, 27 Jun 2026](https://www.mexc.com/learn/article/will-ethereum-price-recover-after-a-60-drop-eth-price-prediction-for-june-2026/1); [Octagon](https://www.octagonai.co/markets/crypto/eth/how-low-will-ethereum-get-in-2026.md)
- PEPE in the same window: ≈ $0.0000028 on 13 Jun 2026; $0.00000225 on 1 Jul 2026 (weak source) — [CoinReporter](https://www.coinreporter.io/2026/06/pepe-price-prediction-2026-2032-will-pepe-coin-dominate-dogecoin-and-shiba-inu-in-2026/); [StealthEx](https://stealthex.io/blog/pepe-coin-price-prediction/)
- Sept 2026 rebound: BTC broke $85,000 on 21 Sep 2026 (peak ≈ $87,300–87,400, highest since January), ≈ $648 M shorts liquidated; ETH snapshot $2,716 (+5.7 %) in the same rally — [CoinEdition](https://coinedition.com/bitcoin-broke-85k-was-it-real-demand-or-a-short-squeeze/); [KuCoin news](https://www.kucoin.com/news/flash/bitcoin-and-ethereum-surge-1-44b-short-squeeze-shakes-crypto-market)
- PEPE in that rally: +22.2 % in 24h to $0.0000049, +40–45 % on the week, high ≈ $0.00000515–0.0000053, "leading Bitcoin, Dogecoin, XRP" — [TheStreet](https://www.thestreet.com/crypto/markets/pepe-surges-22-leading-bitcoin-dogecoin-xrp-?.tsrc=rss); [BigGo](https://finance.biggo.com/news/d311428d-c7b7-44ad-8be3-420e926934d8); [MetaMask](https://metamask.io/price/pepe)
- Downside beta: 24 Sep 2026 PEPE −13 % in a day while "memecoins underperformed majors" — [CoinMarketCap, 24 Sep 2026](https://coinmarketcap.com/top-stories/6ab4b3fa9b764f5d2ecae6ea/)
- 10–12 Oct 2026: BTC fell toward $80,000 then briefly > $84,000; ETH recovered above $2,500; PEPE −6 % on the week (Coinbase) — [CryptoSlate](https://cryptoslate.com/bitcoin-approaches-an-85000-wall-as-ethereums-26-5-billion-derivatives-market-flashes-warning-signs); [Coinbase](https://www.coinbase.com/price/pepe)
- Feb 2026: Benjamin Cowen warned memecoins face the most downside risk in a tightening-liquidity environment — [MEXC news](https://www.mexc.com/news/692254)

### Inferences
- June→September 2026 leg: ETH $1,559 → $2,716 = +74 %; PEPE $0.00000225 → $0.0000053 = +136 % (or $0.0000028 → $0.0000053 = +89 % using the better-sourced June level). Upside beta ≈ 1.2–1.8× ETH on this move; the 11 Sep → 22 Sep burst (+60 % in ~10 days) was a leverage/short-squeeze event rather than an ETH-driven one.
- Downside in H1 2026: PEPE from ≈ $0.0000051 (2 Jan) to ≈ $0.0000022–0.0000028 (June/July) = −45 % to −56 %, vs ETH's fall to ≈ $1,450–1,570 (ETH's January 2026 level not sourced here, so the ETH-side drawdown cannot be computed; the user's premise implies a comparable or larger PEPE drawdown).
- 2024 full-cycle beta was far higher (PEPE ≈ 18× in market cap vs ETH ≈ +50 % for 2024, ETH figure not sourced in this research), consistent with memecoins amplifying ETH moves 5–10× in a true bull leg but only ~1.5× in a 2026-style relief rally — a sign of fading reflexivity.
- Correlation is positive and high during risk-off (Oct 2025, Sep 24 2026) but the relationship is asymmetric: PEPE's largest moves are liquidation cascades in its own perp market ($323–446 M OI).

### Gaps
- No formal beta/correlation statistics (e.g., 30/90-day rolling correlation vs ETH/BTC) were found from Kaiko, Messari, Galaxy or 21Shares; all ratios above are back-of-envelope from price points.
- ETH's start-of-2026 and start-of-Oct-2024 levels, and PEPE's exact Oct 2024 trough, were not retrieved, so the Oct–Dec 2024 beta cannot be stated precisely beyond "≈ +196 % for PEPE from 1 Nov to 9 Dec 2024".

## Q7. Analyst targets / scenarios 2026–2027 and prediction-market odds

### Takeaway
No sell-side or research-house targets exist; published forecasts are from prediction sites and cluster at $0.000003–0.000007 for 2026 (bearish statistical models see −14 %), with 2027 ranges from $0.0000027 (WalletInvestor) to $0.000044 (Cryptopolitan). No Polymarket or Kalshi market on PEPE was found.

### Cited Findings
- InvestingHaven: 2026 $0.00000318–0.000007; 2027 $0.000005–0.0000095 — [InvestingHaven](https://investinghaven.com/pepe-pepe-price-prediction/)
- CoinGabbar: "most analyst models" 2026 $0.0000038–0.0000539 depending on BTC — [CoinGabbar](https://www.coingabbar.com/en/price-prediction/pepe-price-prediction-2026-bull-bear-target-analysis)
- Coinfomania AI model: 2026 peak $0.0000211, low $0.00000915 (now implausible vs spot) — [Coinfomania](https://coinfomania.com/pepe/predictions/)
- Cryptopolitan: 2027 min $0.000027 / avg $0.000035 / max $0.000044 — [Cryptopolitan](https://www.cryptopolitan.com/pepe-price-prediction/)
- WalletInvestor (bearish): 2027 min $0.0000026617, avg $0.0000028419 — [Coinfomania/WalletInvestor citation](https://coinfomania.com/pepe/predictions/)
- DappRadar statistical model (updated 22 Jun 2026): ≈ −14 % over one year, bearish rating — [DappRadar](https://dappradar.com/token/pepe/price-prediction)
- KuCoin flash note: base case $0.0000025–0.0000045 through year-end (from a $0.0000026 / $1.06 bn snapshot, date unclear — possibly Nov 2025) — [KuCoin news](https://kucoin.com/news/flash/pepe-coin-pepe-price-predictions-for-2026-to-2050-released)
- MEXC-hosted Jan 2026 piece: 2030 $0.000021–0.000048; Benzinga table 2030 ≈ $0.0000563 — [MEXC news](https://www.mexc.com/news/405641); [Benzinga](https://www.benzinga.com/money/pepe-price-prediction/)
- crypto.news technical piece: "chart screams danger: Pepe could plunge 85 %" (undated) — [crypto.news](https://crypto.news/this-chart-screams-danger-pepe-coin-price-could-plunge-85/)
- Coin Bureau (2 Feb 2026): $0.01 would imply a $4.2 tn market cap — "larger than all cryptocurrencies combined" — [Coin Bureau](https://coinbureau.com/analysis/can-pepe-coin-reach-1-dollar)
- Bitget/press: "the $11 billion frog that fell 86 % — and the ETF nobody expected" — [Bitget news](https://www.bitget.com/news/detail/12560605381988)
- Prediction markets: searches for Polymarket/Kalshi PEPE markets returned only generic prediction-market-ETF coverage (Polymarket+Kalshi $150 bn lifetime volume) — [CoinMarketCap Academy](https://coinmarketcap.com/academy/article/polymarket-kalshi-volumes-hit-dollar150b-as-regulators-scrutinize-event-etfs)

### Inferences
- Treat all targets as retail-site output; the only quasi-institutional opinions are Balchunas (ETF sentiment), Cowen (memecoin downside), and Santiment/CMC "neutral" readings.

### Gaps
- No Messari, Galaxy, 21Shares, Kaiko or CoinGecko-research PEPE scenario for 2026–27 found; no prediction-market odds on PEPE price or ETF approval.

## Q8. Competitors, sector share, Ethereum-memecoin cohort

### Takeaway
Memecoin sector ≈ $35.1 bn (CoinGecko, 6 Oct 2026). DOGE ≈ $14.7 bn (42 %), MemeCore ≈ $5.5 bn (undated), SHIB ≈ $3.2–3.4 bn (9–10 %), PEPE ≈ $1.75 bn (≈ 5 %, #3–4). Among Ethereum-native memecoins PEPE is second only to SHIB and dwarfs FLOKI, SPX6900, TURBO, MOG and PEPECOIN; PEPE ≈ 70 % of the non-SHIB Ethereum memecoin cohort.

### Cited Findings
- Sector: CoinGecko meme category ≈ $35.1 bn on 6 Oct 2026; another table ≈ $34 bn; CoinGape's $60.9 bn is an outlier — [crypto.news, Oct 2026](https://crypto.news/best-memecoins-to-buy-in-october-2026-five-names-and-their-limits/); [cryptonews.com](https://cryptonews.com/cryptocurrency/best-meme-coins/)
- DOGE ≈ $14.7 bn (6 Oct 2026, CoinGecko via crypto.news); $13.29 bn (cryptonews table) — same sources
- SHIB ≈ $3.2–3.4 bn (Oct 2026); $3.16 bn (cryptonews table) — same sources
- MemeCore (M): ≈ $5.5 bn market cap, FDV ≈ $22.9 bn at $4.27 (CoinGecko category page, undated); ranked #2 memecoin on DappRadar — [CoinGecko meme category](https://www.coingecko.com/en/categories/meme-token); [DappRadar](https://dappradar.com/rankings/tokens/meme-coins)
- DappRadar top-10 memecoins (undated 2026 snapshot): DOGE, MemeCore, SHIB, PEPE, 币安人生, PUMP, TRUMP, PENGU, BONK, SPX6900; PENGU ≈ $430 M, BONK ≈ $409 M — [DappRadar](https://dappradar.com/rankings/tokens/meme-coins)
- PEPE ≈ $1.75–1.78 bn (12–13 Oct 2026), CMC rank #61 — [Bybit](https://www.bybit.com/en/price/pepe/)
- PENGU $429.45 M, FLOKI $229.12 M, BONK $227.43 M (CoinDCX top-10, Sept 2026); CoinGecko undated: BONK ≈ $566 M, PENGU ≈ $543 M (conflict — different dates) — [CoinDCX](https://coindcx.com/blog/crypto-highlights/top-memes-coins); [CoinGecko](https://www.coingecko.com/en/categories/113)
- FLOKI $278.9 M (22 Sep 2026, MetaMask); ≈ $262 M (CoinGecko, undated) — [MetaMask FLOKI](https://metamask.io/price/floki); [CoinGecko FLOKI](https://www.coingecko.com/en/coins/floki)
- SPX6900 $410.39 M, rank #126 (1 Oct 2026, Bybit); ≈ $340.5 M at $0.37 (Coinbase, undated) — [Bybit SPX](https://www.bybit.com/en/price/spx6900/); [Coinbase SPX](https://www.coinbase.com/price/spx6900)
- WIF $169.34 M at ≈ $0.168 (16 Jun 2026, Trust Wallet); undated trackers $383–397 M — [Trust Wallet](https://trustwallet.com/price/dogwifhat); [Blockworks](https://blockworks.co/price/wif)
- BRETT $56.7 M at $0.00567, ≈ 891 k holders (5 Oct 2026, CMC via CaptainAltcoin) — [CaptainAltcoin](https://captainaltcoin.com/three-meme-coins-set-to-explode-in-2026-pepeto-brett-brett-and-snek-snek/)
- TURBO ≈ $102.02 M (Changelly, ~10 Oct 2026); $69.31 M (Feb 2026 press release) — [Changelly](https://changelly.com/blog/best-shitcoin-to-buy/); [BTCPressWire](https://btcpresswire.com/2am-best-crypto-coins-for-2026-this-next-100x-crypto-presale-just-burned-4b-tokens-as-turbo-slips-and-mog-crashes-to-0-06/)
- MOG $44.1 M, rank #403 (7 Sep 2026); $28–30 M mid-Jul 2026 — [Cryptoast](https://cryptoast.fr/cours-mog-coin-27659.html); [Coinranking](https://coinranking.com/coin/ogeeFxUH0+mogcoin-mog/historical-data)
- PEPECOIN (PEP, Dogecoin-fork PoW chain, not ERC-20): ≈ $10.03 M (CMC, ≈ May 2026) — [CoinMarketCap](https://coinmarketcap.com/currencies/pepecoin-org/)
- Market cap of Pepe (CMC Oct 2026 snapshot) ≈ $1.9 bn "Onchain Market Cap" (2 Oct) — [Etherscan](https://etherscan.io/token/0x6982508145454ce325ddbe47a25d4ec3d2311933)

### Inferences
- Ranking table (latest dated figure, USD): DOGE 14.7 bn (6 Oct) · MemeCore ≈ 5.5 bn (undated) · SHIB 3.2–3.4 bn (Oct) · PEPE 1.75–1.78 bn (12–13 Oct) · PENGU 0.43–0.54 bn (Sep/undated) · SPX6900 0.34–0.41 bn (1 Oct) · BONK 0.23–0.57 bn (Sep/undated) · FLOKI 0.23–0.28 bn (Sep) · WIF 0.17 bn (Jun) · TURBO ≈ 0.10 bn (Oct) · BRETT 0.057 bn (5 Oct) · MOG 0.044 bn (7 Sep) · PEPECOIN 0.010 bn (May).
- PEPE share of sector ≈ 5.0 % ($1.75 bn / $35.1 bn); DOGE ≈ 42 %, top-4 ≈ 71 %.
- Ethereum-memecoin cohort (SHIB + PEPE + FLOKI + SPX6900 + TURBO + MOG ≈ $5.7–6.1 bn): PEPE ≈ 29–31 %; excluding SHIB (≈ $2.4–2.6 bn): PEPE ≈ 68–73 %.
- PEPE is ~8× the fifth-largest memecoin and ~40× the mid-tier (BRETT/MOG), so its flows set the tone for the small ERC-20 memecoins in the report (WOJAK, TROLL, CHILLGUY are far smaller and were not covered here).

### Gaps
- No single dated 10–13 Oct 2026 ranking table; BONK and PENGU figures conflict by ~2× between September and undated snapshots; WOJAK, TROLL, CHILLGUY, TRUMP and PUMP caps not retrieved (out of scope for this note).

## Q9. Institutional/corporate holdings, controversies, strengths/weaknesses, main risks

### Takeaway
No public-company treasury or institutional fund holding PEPE was found (only the pending Canary ETF and the Valour ETP). PEPE's investor case rests on liquidity, listings and bellwether status; its weaknesses are zero utility, fixed-supply/no-burn tokenomics, 41–77 % top-10 concentration, anonymous team with a 2023 insider-dump record, pervasive paid-promo noise ("Pepeto"/"Pepe cofounder" campaigns), and extreme beta in a sector that lost ~70 % from Dec 2024 to Oct 2025.

### Cited Findings
- No public-company PEPE treasury found; the only treasury-company result was an XRP firm — [MEXC news](https://www.mexc.com/news/815750)
- Canary ETF filing is the "main 2026 institutional item"; Valour ETP is the only listed product — [CoinMarketCap](https://coinmarketcap.com/cmc-ai/pepe/latest-updates/); [Valour](https://valour.com/en/products/valour-pepe-sek)
- Controversy 1 — Aug 2023 multisig dump (16 T, $15 M, 5/8→2/8 threshold, ex-team blamed) — [The Block](https://www.theblock.co/news/ecosystems/2023-08-26-pepe-team-members-stole-15-million-from-multisig-247576)
- Controversy 2 — creator doxxing allegations (Zachary Testa, Lamborghini, no payment to Matt Furie), unverified — [Techflow](https://www.techflowpost.com/en-US/article/12823)
- Controversy 3 — Binance's own listing note: no utility, insiders ≈ 7 % of supply — [Decrypt](https://decrypt.co/139010/liam-binance-lists-pepe-meme-coin-market-cap-hits-1-billion)
- Controversy 4 — continuous paid press claiming a "Pepe cofounder" is launching "Pepeto" with a Binance listing; promotional and unverified — [openPR](https://openpr.com/news/4660363/pepe-coin-price-prediction-pepe-jumps-5-6-while-the-pepe); [MEXC news](https://www.mexc.com/news/1054442)
- Retail-loss anecdote: an early PEPE investor who turned $251 into $8 M lost $2.5 M in a crash — [Cryptorank](https://cryptorank.io/news/feed/9d01d-pepe-coin-8-million-251-investment-loses-2-5-crypto-crash)
- Liquidity strength: Kaiko found CEX order-book depth held during the Aug 2023 dump — [Kaiko](https://www.kaiko.com/resources/pepe-plunges-as-founders-sell)
- ETF filing risk language: shares "speculative", no '40 Act protections, top-10 holders ≈ 41 % — [GNCrypto](https://www.gncrypto.news/news/canary-pepe-etf-filing-cboe-listing-plan/); [Datawallet](https://www.datawallet.com/crypto/what-is-pepe-coin)
- Sector risk: memecoins "underperform majors" in risk-off sessions (Aug 2025, Sep 2026); Cowen: memecoins most exposed to tightening liquidity — [CoinDesk](https://www.coindesk.com/markets/2025/08/14/pepe-drops-4-as-memecoin-sector-underperforms-broader-crypto-market); [CoinMarketCap](https://coinmarketcap.com/top-stories/6ab4b3fa9b764f5d2ecae6ea/); [MEXC news](https://www.mexc.com/news/692254)
- Leverage risk: OI $323–446 M vs ≈ $1.7 bn cap; $900 M+ market-wide short liquidations drove the Sept 2026 spike — [FXStreet](https://www.fxstreet.com/cryptocurrencies/news/pepe-price-forecast-pepe-sustains-mild-recovery-on-firm-retail-support-202610020311); [BigGo](https://finance.biggo.com/news/d311428d-c7b7-44ad-8be3-420e926934d8)

### Inferences
- Strengths: deepest listing/product coverage of any ERC-20 memecoin (Binance/Coinbase/Kraken/Bybit perps, Robinhood retail, pending US ETF, Swedish ETP); ~593 k holders and rising; whales net-accumulating and CEX outflows in 2026; fixed supply with LP burned (no team unlock overhang); high volume/turnover and resilient CEX liquidity; sector-bellwether status means it is the first memecoin institutions would access.
- Weaknesses: no utility/cash flow; −85 % from ATH with no new high in 22 months; 2026 upside beta to ETH has shrunk to ~1.2–1.8× (vs multi-× in 2024), i.e. diminishing reflexivity; concentration (41 % top-10 ex-exchanges; 77 % raw); anonymous team with a prior insider-dump; name confusion with PEPECOIN, Pepe Community, Pepeto, Wall Street Pepe etc.; perp-driven liquidation cascades; regulatory risk (ETF may never go effective; US perps still pending CFTC action).
- Main risks ranked: (1) sector-wide memecoin decline/rotation to MemeCore-style new launches; (2) leverage-driven crashes (Oct 2025 template); (3) ETF rejection/withdrawal or SEC delay removing the main 2026 narrative; (4) whale distribution given 20 %+ in top-100 non-exchange wallets.

### Gaps
- No evidence either way on hedge-fund or market-maker PEPE positions (Nansen/Arkham entity data not accessible); no Grayscale/21Shares product; no 2026 Matt Furie/IP development found.
