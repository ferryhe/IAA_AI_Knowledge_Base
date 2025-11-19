_Note: Source document was split into 2 OCR chunks (pages 1-18, pages 19-29) to stay within token limits._

# LTAM_II_Chapter8_Fixed and Fixed Indexed Annuities_20240813

## Page 1
# Chapter 8 Fixed and Fixed Indexed Annuities 

## Learning Outcomes

The student will be able to:
Construct deterministic and stochastic discrete cash flow models for basic fixed annuities and fixed indexed annuities incorporating dynamic assumptions, policyholder behavior, and hedging.

Chapter 8 builds upon previous chapter's model basic building blocks. Fixed annuity cash flow model mechanics are similar to Chapter 5's UL account value but without the life insurance parts such as COls or death benefits. The insurer receives the initial premium, invests assets, earns investment income, credits interest, and pays surrender values and account values upon death. Having studied Chapter 5 is helpful but is not a prerequisite.

Chapter 8's model design focus is

1) modeling basic fixed annuities and fixed indexed annuities
2) incorporating hedges
3) modeling dynamic assumptions and policyholder behavior
4) applying simulations and calculating CTE and VaR

Chapter 8.1 restricts the focus to undecremented conditional account value cash flows and also restricts the context to constant (and hence deterministic) interest rates and index returns over the entire time horizon. We do this to provide transparency enabling insights by allowing us to make comparisons. We deliberately construct Chapter 8.1 examples to illustrate and directly compare product provisions related to account value mechanics - interest credited and index credits - and their funding with fixed income securities, and for FIAs, with call options.

Chapter 8.2 introduces the construction and application of stochastic models for fixed annuities and FIAs. The models incorporate dynamic policyholder behavior and illustrates FIA product management with hedging and product design. Chapter 8.3 briefly states a number of considerations related to FIA models and products.

Like previous Chapters, Chapter 8's FA and FIA models strive to balance educational purposes, transparency, and simplicity. For FIAs, we assume 100\% of the account is allocated to a large cap index fund such as the S\&P500 and none is allocated to the fixed account. We do not model a fixed account or transfers from the Index account to/from fixed accounts.

We set the reserve liability equal to the account value. Accounting standards and regulatory reserve requirements entail fair value methods beyond scope.

We only cover 1-year point-to-point index credit methods. Exotic methods add complexity but do not substantially change the basic building blocks. The FIA cash flow model uses an annual

## Page 2
time step. It is not uncommon for models of FIAs with complex guarantees such as GLWBs to use weekly or daily time steps. An annual time step removes the need to model interim activity and values.

We use Black-Scholes to calculate call option prices. We could alternatively use other option pricing models. We then have a nested model and could apply methods such as outer-inner loops illustrated in Chapter 3. We make additional simplifications described later.

# 8.1 Funding Fixed and Fixed Indexed Annuities 

Chapter 8.1's context is undecremented conditional cash flows in which not only are rates deterministic, interest rates and index returns are constant over the entire time horizon. Second, we initially only consider a 1-year point-to-point FIA with a 0\% floor and without a cap or index spread. We do this for simplicity and transparency. We do not repeat this is the context, instead we state when we modify the context. Examples 8.3 and 8.4 will illustrate a cap and non-zero floors and index spreads.

As described in Chapter 7.2, a common approach for fixed annuities is to manage to a target spread which is the difference between the net investment rate earned on invested assets the and credited rate: Spread = Net Investment Earned Rate - Credited Rate.

Fixed annuity portfolios typically consist of fixed income securities such as government bonds, high-quality corporate bonds and mortgages, asset-back securities, and other risky assets. A benchmark investment strategy is a systematic approach to managing an investment portfolio that aims to achieve returns comparable to a specified benchmark. Benchmarks are developed based on information such as product cash flows, capital constraints, performance objectives, risk profiles, and asset liability management (ALM) strategies including duration matching targets and limits. For example, MYGAs and FIAs with short vs. long surrender charge periods, or sold via banks vs. agents, and FIAs with and without GWLBs (Guaranteed Withdrawal Living Benefits) exhibit different cash flow risks and policyholder behavior including lapsation, resulting in different investment strategies and hence also different net investment yields and interest rate risk metrics.

In Chapter 8 we use a simplistic benchmark that allocates percentages to a portfolio consisting of 5-year, 10-year, and 20-year corporate bond and mortgages. We do not specify granularity by credit rating or differentiate credit spreads by maturity and assume an overall Portfolio Spread for the benchmark as specified in tab Assumption1. Chapter 8 examples set the allocation mix at $25 \% / 50 \% / 25 \%$ for the 5/10/20-year fixed income securities and the Portfolio Spread over treasuries to $2 \%$.

Benchmarks are often relatively simplistic but may have more granularity for allocations by asset class, credit rating, and other characteristics in addition to maturity. For example, asset class could specify percentages by U.S. Treasuries, investment-grade corporate bonds, mortgage-backed securities (MBS), asset-backed securities (ABS), municipal bonds and other government-related bonds.

## Page 3
Recall, from Chapter 7, an FIA contains an embedded derivative - the insurer writes (i.e., sells) a call option to the policyholder.

Figure 8.1

We split a FIA into two parts: 1) the part for account value that is guaranteed, and 2) the part for index credits. FIA portfolios consist of fixed income securities for the guaranteed part like fixed annuities and the appropriate call options and other derivatives for the index credits to cover the written call.

First the insurer buys fixed income securities to fund the guaranteed account value at the end of the index term plus the target spread amount. Second, the insurer uses the remaining amount, the option budget, to purchase the appropriate call options for an effective hedge, that is, offset the written call option. Based on what the option budget supports, the insurer determines the indexing method's parameters: participation rate, cap, and index spread (this is not the target spread). Rather than crediting the option budget as interest as for a fixed annuity, the amount is used to buy call options (and also sell call options in the case of caps).

At any time, an option is said to be in-the-money (ITM) if the option payoff would be positive, out-of-the-money (OTM) if the payoff would be negative, and at-the-money (ATM) if the payoff would be zero or close to zero.

The interest credit at $t=k$ for a FIA with participation rate ParRate ${ }_{k}$ and account value $A V_{k}$ is,

$$
\begin{aligned}
& \text { Index Credit }_{k}=\max \left(\text { ParRate }_{k} * \text { Index Return }_{k}, 0\right) \times A V_{k} \\
& =\text { ParRate }_{k} \times A V_{k} / \text { Index }_{k} \times \max \left(\text { Index }_{k+1}-\text { Index }_{k}, 0\right) \\
& =\# \text { Call Options }_{k} \times \text { ATM Call Option payoff }
\end{aligned}
$$

where the call's strike price is $K_{k}=$ Index $_{k}$, i.e., an ATM call, and the number of call options purchased is \# Call Options ${ }_{k}=$ Participation Rate $_{k} \times A V_{k} /$ Index $_{k}$.

Given an available Option Budgetk and an ATM call with price Call Price ${ }_{k}$, the number of Call Options $_{k}$ that can be purchased is Option Budgetk / Call Price ${ }_{k}$. It follows that,
(8.1) \# Call Options $_{k}=$ ParRate $_{k} \times A V_{k+1} /$ Index $_{k}=$ Option Budget $_{k} /$ Option Price $_{k}$

Chapter 8.1.2 generalizes Equation 8.1 in a more robust FIA context for non-zero floors and index spreads.
![Page 3 Image 1](ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_assets/ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_p03_img1.jpg)

## Page 4
# 8.1.1 MYGA and FIA Compared 

Example 8.1 illustrates the first year of a 7-year MYGA without decrements.

## Example 8.1

A 7-year MYGA (multi-year guaranteed annuity) was purchased with a \$100,000 deposit. The benchmark portfolio rate of fixed income securities is $6.75 \%$. The target spread is $1.75 \%$ and the credited rate is $5 \%=6.75 \%-1.75 \%$ which is guaranteed for 7 years. The minimum guaranteed rate is $1.5 \%$. Investment income is $6.75 \% \times \$ 100,000=\$ 6,750$. Credited interest is $5.00 \% \times$ $\$ 100,000=\$ 5,000$ and the account value at the end of the year is $\$ 100,000+\$ 5,000$. The spread is $\$ 6,750-\$ 5,000=\$ 1,750=1.75 \% \times \$ 100,000$.

We now consider the $\$ 100,000$ in invested assets at $t=0$ split into the assets that fund the (Guaranteed) Credited Interest and the assets that fund the insurer's Spread: Total Asset = Assets for Spread + Assets for Credited Interest. Spread = Assets for Spread $\times$ Earned Rate, so Assets for Spread $=\$ 1,750 / 6.75 \%=\$ 25,926$. Credited Interest $=$ Assets for Credited Interest $\times$ Earned Rate, so Assets for Credited Interest $=\$ 5,000 / 6.75 \%=\$ 74,074$. This split of assets is typically not done for fixed annuities but we do as a precursor to Example 8.2.

## End Example 8.1

Example 8.2 illustrates the first year of a 7-year FIA without decrements - the inputs and product parameters are deliberately chosen to mirror Example 8.1's MYGA.

## Example 8.2

A 7-year FIA using a 1-year point-to-point crediting method was purchased with a \$100,000 deposit. The floor is $0 \%$, the participation rate is $67.22 \%$ which is guaranteed for 1 year, and there is no cap or index spread. The index is at 1,000, the insurer's benchmark portfolio of bonds earns $6.75 \%$ and the target spread is $1.75 \%$. An at-the-money call option's price on the index is $\$ 69.68$ per unit of index. The option budget is $5 \%=6.75 \%-1.75 \%$.

Suppose in the first year the Index return is $7.44 \%$. The index credits equal $67.22 \% \times 7.44 \%=5 \%$ and the account value at the end of the year is $\$ 100,000+\$ 5,000$.

We now consider the $\$ 100,000$ in invested assets at $t=0$ split into the assets that fund the Guaranteed Account Value (GAV) plus Spread and the assets for the index credit, i.e., the option budget: Total Asset = Assets for GAV+Spread + Option Budget. At $t=1$, the GAV is $\$ 100,000$ since the floor is $0 \%$ and the Spread $=\$ 1,750$ as in Example 8.1. The insurer invests the present value at $t=0$ in bonds, or $\$ 101,750 / 1.0675=\$ 95,316$. The option budget is the remaining amount or $\$ 100,000-\$ 95,316=\$ 4,684$. The number of call options the insurer can purchase equals Option Budget / Call Price $=\$ 4,684 / \$ 69.68=67.22$. This is how the $67.22 \%$ participation rate was determined.

## Page 5
The option budget dollar amount is the present value at $t=0$ of the option budget rate applied to the account: $\$ 4,684=5 \% \times \$ 100,000 / 1.0675$. Rather than crediting the accumulated value at $t=1$ with $\$ 5,000$ in interest as in Example 8.1's MYGA, the amount is used to buy call options.

# End Example 8.2 

First, observe that when the index return is $7.44 \%$, Example 8.1 and 8.2 are identical for the policyholders account value and the insurer's dollar spread. When returns are less than or more than $7.44 \%$, the account value is less or more respectively, however, the dollar spread remains the same (in the first year).

Second, our model assumes hedging is $100 \%$ effective: the purchased call is exactly the same as the written call in amount, timing, and parameters such as strike price. We consider these and additional considerations in Chapter 8.3. For our examples, we assume hedges are perfect and we can buy call options precisely as desired.

## PONDER

Example 8.2 illustrated that the number of call options the budget can purchase only supports a $67.2 \%$ participation rate. How can we modify the product design to support a $90 \%$ participation rate?

We now continue Example 8.1's 7-year MYGA for a 10-year time horizon.

## Example 8.1 Continued

We assume the net investment earned rate stays constant over time. We assume both liabilities and assets are equal to the account value. Figure 8.2 illustrates rates and cash flows.

Figure 8.2

## Page 6
| A | B | C | D | E | F | G | H | I | J | K | L |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | Fixed Annuity (MYGA) |  | Rates |  | PH Account |  |  |  | Invested Assets |  |  |
|  |  | Policy | Portfolio | Credited | EOP | Interest | Investment |  | For Spread | For GAV | Total |
| 2 | Input | Year | Rate | Rate | Account | Credit | Income | Spread |  |  |  |
| 3 | Deposit | 100,000 | 0 |  |  | 100,000 |  |  |  | 25,926 | 74,074 | 100,000 |
| 4 | Target Spread | $1.75 \%$ | 1 | $6.75 \%$ | $5.00 \%$ | 105,000 | 5,000 | 6,750 | 1,750 | 27,222 | 77,778 | 105,000 |
| 5 | Benchmark Rate | $6.75 \%$ | 2 | $6.75 \%$ | $5.00 \%$ | 110,250 | 5,250 | 7,088 | 1,838 | 28,583 | 81,667 | 110,250 |
| 6 | Initial Guar Rate | $5.00 \%$ | 3 | $6.75 \%$ | $5.00 \%$ | 115,763 | 5,513 | 7,442 | 1,929 | 30,013 | 85,750 | 115,763 |
| 7 | Initial Guar Period | 7 | 4 | $6.75 \%$ | $5.00 \%$ | 121,551 | 5,788 | 7,814 | 2,026 | 31,513 | 90,038 | 121,551 |
| 8 | Guar Minimum Rate | $1.50 \%$ | 5 | $6.75 \%$ | $5.00 \%$ | 127,628 | 6,078 | 8,205 | 2,127 | 33,089 | 94,539 | 127,628 |
| 9 |  |  | 6 | $6.75 \%$ | $5.00 \%$ | 134,010 | 6,381 | 8,615 | 2,233 | 34,743 | 99,266 | 134,010 |
| 10 |  |  | 7 | $6.75 \%$ | $5.00 \%$ | 140,710 | 6,700 | 9,046 | 2,345 | 36,480 | 104,230 | 140,710 |
| 11 |  |  | 8 | $6.75 \%$ | $5.00 \%$ | 147,746 | 7,036 | 9,498 | 2,462 | 38,304 | 109,441 | 147,746 |
| 12 |  |  | 9 | $6.75 \%$ | $5.00 \%$ | 155,133 | 7,387 | 9,973 | 2,586 | 40,220 | 114,913 | 155,133 |
| 13 |  |  | 10 | $6.75 \%$ | $5.00 \%$ | 162,889 | 7,757 | 10,471 | 2,715 |  |  |  |

Cells B3:B7 are inputs. Cells B3:B5 are the initial premium, insurer's target spread, and benchmark portfolio earned rate respectively. Cells B6:B7 are the initial guarantee rate and guarantee period. Cell B8 is the guaranteed minimum interest rate.

Columns D-E calculate the portfolio earned rate and the credited rate. Since all cash flows are reinvested at the same rate, the earned rate remains a constant $6.75 \%$ during and beyond the guarantee period. In years 8-10 the portfolio rate and credited rate remain at $6.75 \%$ and $5.00 \%$ respectively. The minimum guaranteed credited rate (B8) is not reached.

$$
\begin{aligned}
& \mathrm{D} 4=\mathrm{B} \$ 5, \mathrm{D} 5=\mathrm{D} 4, \text { etc. } \\
& \mathrm{E} 4=\mathrm{MAX}(\mathrm{~B} \$ 8, \mathrm{D} 4-\mathrm{B} \$ 4), \text { etc. }
\end{aligned}
$$

Columns F-G calculate the EOP account value and the interest credited to the account during the period

$$
\begin{aligned}
& \mathrm{F} 3=\mathrm{B} 3, \mathrm{~F} 4=\mathrm{F} 3+\mathrm{G} 4, \text { etc. } \\
& \mathrm{G} 4=\mathrm{F} 3^{*} \mathrm{E} 4, \text { etc. }
\end{aligned}
$$

Columns H-I calculate the insurer's investment income and spread,

$$
\begin{aligned}
& \mathrm{H} 4=\mathrm{F} 3^{*} \mathrm{D} 4, \text { etc. } \\
& \mathrm{I} 4=\mathrm{F} 3^{*} \mathrm{~B} \$ 4, \text { etc. }
\end{aligned}
$$

Columns J-L allocate the total assets into the amount needed for the spread and for the guaranteed account value.

$$
\begin{aligned}
& \mathrm{J} 3=\mathrm{I} 4 / \mathrm{D} 4, \text { etc. } \\
& \mathrm{K} 3=\mathrm{G} 4 / \mathrm{D} 4, \text { etc. } \\
& \mathrm{L} 3=\mathrm{J} 3+\mathrm{K} 3, \text { etc. }
\end{aligned}
$$

# End Example 8.1 Continued

## Page 7
In Example 8.1 MYGA's product design, the credited rate is the solve-for variable, albeit a straightforward determination once the investment strategy and target spread are specified. Although Example 8.1 did not model decrements, the insurer's assets equal the account value and are sufficient to pay out surrender cash values. In Chapter 8.2 we expand the example to model decrements and use stochastic scenarios.

We now continue Example 8.2's 7-year FIA using a 1-year point-to-point crediting method for a 10-year time horizon. At time $t=k$, we invest ( $\mathrm{AV}_{\mathrm{k}}+$ Target $\$$ Spread) / ( $1+$ Earned Rate $_{\mathrm{s}}$ ) in bonds. The option budget in dollars is the leftover amount. Based on the available option budget, we apply Equation 8.1 to determine the number of ATM calls to purchase and the participation rate. That is, in the FIA's product design, the participation rate is the solve-for variable.

In the continuation, we illustrate call option price calculations using Black-Scholes. We could alternatively use other option pricing models. We then have a nested model and could apply methods such as outer-inner loops illustrated in Chapter 3.

# Example 8.2 Continued 

We assume the net investment earned rate and index return stays constant over time as do market inputs for Black-Scholes. We again assume both liabilities and assets are equal to the account value. Figure 8.3a illustrates rates and cash flows.

Figure 8.3a

|  | A | B | C | D | E | F | G | H | I | J |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | Fixed Indexed Annuity (FIA) |  |  | Rates |  |  |  |  | PH Account |  |
|  | Input |  | Policy <br> Year | Portfolio <br> Rate | Option <br> Budget | Participation <br> Rate | Index | Index <br> Change | EOP <br> Account | Index <br> Credit |
| 3 | Deposit | 100,000 | 0 |  |  |  | 1,000 |  | 100,000 |  |
| 4 | Target Spread | 1.75\% | 1 | 6.75\% | 5.00\% | 67.2\% | 1,074 | 7.44\% | 105,000 | 5,000 |
| 5 | Benchmark Rate | 6.75\% | 2 | 6.75\% | 5.00\% | 67.2\% | 1,154 | 7.44\% | 110,250 | 5,250 |
| 6 | Index Dividend Rate | 1.75\% | 3 | 6.75\% | 5.00\% | 67.2\% | 1,240 | 7.44\% | 115,763 | 5,513 |
| 7 |  |  | 4 | 6.75\% | 5.00\% | 67.2\% | 1,332 | 7.44\% | 121,551 | 5,788 |
| 8 |  |  | 5 | 6.75\% | 5.00\% | 67.2\% | 1,431 | 7.44\% | 127,628 | 6,078 |
| 9 |  |  | 6 | 6.75\% | 5.00\% | 67.2\% | 1,538 | 7.44\% | 134,010 | 6,381 |
| 10 |  |  | 7 | 6.75\% | 5.00\% | 67.2\% | 1,652 | 7.44\% | 140,710 | 6,700 |
| 11 |  |  | 8 | 6.75\% | 5.00\% | 67.2\% | 1,775 | 7.44\% | 147,746 | 7,036 |
| 12 |  |  | 9 | 6.75\% | 5.00\% | 67.2\% | 1,907 | 7.44\% | 155,133 | 7,387 |
| 13 |  |  | 10 | 6.75\% | 5.00\% | 67.2\% | 2,049 | 7.44\% | 162,889 | 7,757 |

Cells B3:B6 inputs. Cells B3:B5 are the initial premium, insurer's target spread, and benchmark portfolio earned rate respectively. Cell B6 is the Index's dividend rate which is a Black-Scholes input. The floor rate is not an input, we instead hardcode it as $0 \%$ in various formulas.

Columns D-E calculate the portfolio earned rate and the option budget as a rate. Since all cash flows are reinvested at the same rate, the portfolio rate remains a constant $6.75 \%$ during and beyond the guarantee period.

## Page 8
D4 = B\$5, D5 = D4, etc.
E4 = D4 - B\$4, etc.
Column F uses Equation 8.1 to calculate ParRate ${ }_{k}=#$ Call Options $k /\left(A V_{k+1} / \operatorname{Index}_{k}\right)$,
$\mathrm{F} 3=\mathrm{T} 3 /(\mathrm{I} 3 / \mathrm{G} 3)$, etc.
Column G is the index value. In order to have Column I-J have the same outcome (numerical values) as Example 8.1, we set Column G so the Index growth rate is 0.05/Participation Rate,

G4 = G3*(1+0.05/F4), etc.
Observe this results in an Index return of $0.05 / 67.2 \%=7.44 \%$ for Example 8.2.
Column H calculates the Index return,

$$
\mathrm{H} 3=\mathrm{G} 4 / \mathrm{G} 3-1 \text {, etc. }
$$

Columns I-J calculate the EOP account value and index credit during the period: Index Credit ${ }_{k}=\operatorname{Max}\left(0 \%\right.$, ParRate $\left._{k} \times \operatorname{Index} \operatorname{Return}_{k} \times \operatorname{Index}_{k}\right)$ reflecting the $0 \%$ floor.

$$
\begin{aligned}
& \mathrm{I} 3=\mathrm{B} 3, \mathrm{I} 4=\mathrm{I} 3+\mathrm{J} 4 \text {, etc. } \\
& \mathrm{J} 4=\operatorname{MAX}\left(0, \mathrm{I} 3^{*} \mathrm{H} 4^{*} \mathrm{~F} 4\right) \text {, etc. }
\end{aligned}
$$

Next, Figure 8.3b presents the option price calculation and the insurer's invested assets.
Figure 8.3b

| 1 | C | K | L | M | N | 0 | P | Q | R | S | T |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | F(A) | Market Inputs |  | Call Calculations |  | Requirements |  | Invested Assets |  |  |  |
| 2 | Policy <br> Year | Volatility | Risk-Free Rate | d1 | Option Cost | Spread | Guaranteed EOP Account | Bond | Option <br> Budget | Total | \# calls |
| 3 | 0 | $15 \%$ | 4.00\% | 0.225 | 69.68 |  |  | 95,316 | 4,684 | 100,000 | 67.2 |
| 4 | 1 | $15 \%$ | 4.00\% | 0.225 | 74.86 | 1,750 | 100,000 | 100,082 | 4,918 | 105,000 | 65.7 |
| 5 | 2 | $15 \%$ | 4.00\% | 0.225 | 80.43 | 1,838 | 105,000 | 105,086 | 5,164 | 110,250 | 64.2 |
| 6 | 3 | $15 \%$ | 4.00\% | 0.225 | 86.41 | 1,929 | 110,250 | 110,340 | 5,422 | 115,763 | 62.7 |
| 7 | 4 | $15 \%$ | 4.00\% | 0.225 | 92.84 | 2,026 | 115,763 | 115,857 | 5,693 | 121,551 | 61.3 |
| 8 | 5 | $15 \%$ | 4.00\% | 0.225 | 99.74 | 2,127 | 121,551 | 121,650 | 5,978 | 127,628 | 59.9 |
| 9 | 6 | $15 \%$ | 4.00\% | 0.225 | 107.16 | 2,233 | 127,628 | 127,733 | 6,277 | 134,010 | 58.6 |
| 10 | 7 | $15 \%$ | 4.00\% | 0.225 | 115.13 | 2,345 | 134,010 | 134,119 | 6,591 | 140,710 | 57.2 |
| 11 | 8 | $15 \%$ | 4.00\% | 0.225 | 123.70 | 2,462 | 140,710 | 140,825 | 6,920 | 147,746 | 55.9 |
| 12 | 9 | $15 \%$ | 4.00\% | 0.225 | 132.90 | 2,586 | 147,746 | 147,867 | 7,266 | 155,133 | 54.7 |
| 13 | 10 | $15 \%$ | 4.00\% | 0.225 | 142.78 | 2,715 | 155,133 | 155,260 | 7,629 | 162,889 | 53.4 |

Columns K-N calculate the call option price using Black-Scholes. Columns K-L are market inputs for volatility and the risk-free interest rate. Columns M-N applies the Black-Scholes formula for call prices in two steps. Recall, the Black-Scholes formula is

$$
c=S e^{-\delta T} \times N\left(d_{1}\right)-K e^{-r T} \times N\left(d_{2}\right)
$$

where $N(x)$ is the cumulative normal distribution function, and

## Page 9
$$
d_{1}=\frac{\ln (S / K)+\left(r-\delta+\frac{\sigma^{2}}{2}\right) \times T}{\sigma \sqrt{T}}
$$

Note $S=$ Index $_{k}$ (Col G) and the strike price $K=$ Index $_{k} \times(1+$ Floor). We simplify Column M-N formulas since $T=1$ and floor $=0 \%$.

$$
\begin{aligned}
& \mathrm{M} 3=\left(\mathrm{LN}(\mathrm{G} 3 /(\mathrm{G} 3)+(\mathrm{L} 3-\mathrm{B} \$ 6+\left(\mathrm{K} 3^{\wedge} 2\right) / 2\right)) / \mathrm{K} 3, \text { etc. } \\
& \mathrm{N} 3=\mathrm{G} 3^{*} \mathrm{EXP}(-\mathrm{B} \$ 6)^{*} \mathrm{NORMDIST}(\mathrm{M} 3,0,1, \text { TRUE })-\mathrm{G} 3^{*} \mathrm{EXP}(-\mathrm{L} 3)^{*} \mathrm{NORMDIST}(\mathrm{M} 3-\mathrm{K} 3, \\
& 0,1, \text { TRUE), etc. }
\end{aligned}
$$

Columns O-P calculate the required EOP amounts for the Guaranteed Account value reflecting the floor (Cell B6) and the insurer's spread.

$$
\begin{aligned}
& \mathrm{O} 3=\mathrm{I} 3^{*} \mathrm{~B} \$ 4, \text { etc. } \\
& \mathrm{P} 3=\mathrm{I} 3, \text { etc. }
\end{aligned}
$$

Columns Q-R calculate the assets needed to fund the Guaranteed Account Value (GAV) plus Spread and the option k .

$$
\begin{aligned}
& \mathrm{Q} 3=(\mathrm{O} 4+\mathrm{P} 4) /(1+\mathrm{B} \$ 5) \text {, etc. } \\
& \mathrm{R} 3=\mathrm{I} 3-\mathrm{Q} 3 \text {, etc. }
\end{aligned}
$$

Column S calculates Total Asset = Assets for (GAV+Spread) + Option Budget.

$$
\mathrm{S} 3=\mathrm{Q} 3+\mathrm{R} 3 \text {, etc. }
$$

Column T uses Equation 8.1 to calculate \# Call Options $_{k}=$ Option Budget $_{k} /$ Call Price $_{k}$.

$$
\mathrm{T} 3=\mathrm{R} 3 / \mathrm{N} 3 \text {, etc. }
$$

The option budget dollar amount is the present value at $t=0$ of the option budget as a rate: Column $R=$ Column $E \times$ Column $I /(1+$ Column D) or Option Dollar Budget $=$ Credited Rate $\times$ Account Value / (1 + Earned Rate). Rather than crediting the accumulated value at $t=1$ of the option budget with interest as in Example 8.1's MYGA, the amount is used to buy call options.

# End Example 8.2 Continued 

In Example 8.2 observe that the option budgets as a rate and d1 are constant; and the calculated participation rates are constant while the call price increases as the index increases and the number of call options purchased increases. When the index return is $7.44 \%$ in all years, Examples 8.1 and 8.2 are identical for both the policyholders account value and the insurer's dollar spread.

Although Example 8.1 did not model decrements, the insurer's assets equal the account value and are sufficient to pay out surrender cash values. Chapter 8.2 expands the example to model decrements and use stochastic scenarios.

## Page 10
# 8.1.2 FIAs With Caps or Non-Zero Floors and Index Spreads 

Next, we redo Example 8.2 for two more FIA product designs. Example 8.2 solved for the participation rate based on option budget. Example 8.3 modifies Example 8.2 by setting the participation rate to $90 \%$, say for consumer preferences and competitive product features. With a higher participation rate, we must limit the upside by using one of the other product design levers - a cap and/or an index spread.

A FIA with a cap is a written bull spread. Recall from Chapter 4.1, a bull spread is the combination of long a call with strike price $K_{1}$ and short a call with strike price $K_{2}$. The payoff increases as the market goes up above $K_{1}$ but the payoff is limited on the upside by $K_{2}$. The position buys market appreciation between $K_{1}$ and $K_{2}$ by partially financing it by selling the second call. Since $K_{1}<K_{2}$, the first call has a higher price than the second call.

Figure 8.4 Bull Spread with Calls

For a FIA with a cap, the underlying is the index, the bull spread's long call has strike price equal to the floor applied to the index and the short call's strike price equals the cap applied to the index. For a $0 \%$ floor, the long call is ATM.

Example 8.3 modifies Example 8.2 by adding a cap. We only describe what we have changed.

## Example 8.3

We continue to assume the net investment earned rate and index return stays constant over time as do market inputs for Black-Scholes. We again assume both liabilities and assets are equal to the account value. Figure 8.5a illustrates rates and cash flows.

Figure 8.5a
![Page 10 Image 1](ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_assets/ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_p10_img1.jpg)

## Page 11
| A | B | C | D | E | F | G | H | I | J | K |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | Fixed Indexed Annuity (FIA) |  |  | Rates |  |  |  |  | PH Account |  |
|  |  |  | Policy | Portfolio | Option | Participation |  |  | Index | EOP |
| 2 | Input |  | Year | Rate | Budget | Rate | Cap | Index | Change | Account | Credit |
| 3 | Deposit | 100,000 | 0 |  |  |  |  | 1,000 |  | 100,000 |  |
| 4 | Target Spread | $1.75 \%$ | 1 | 6.75\% | 5.00\% | 90.0\% | 6.32\% | 1,056 | 5.56\% | 105,000 | 5,000 |
| 5 | Benchmark Rate | 6.75\% | 2 | 6.75\% | 5.00\% | 90.0\% | 6.32\% | 1,114 | 5.56\% | 110,250 | 5,250 |
| 6 | Index Dividend Rate | 1.75\% | 3 | 6.75\% | 5.00\% | 90.0\% | 6.32\% | 1,176 | 5.56\% | 115,763 | 5,513 |
| 7 | Guar Minimum Cap | 2.00\% | 4 | 6.75\% | 5.00\% | 90.0\% | 6.32\% | 1,241 | 5.56\% | 121,551 | 5,788 |
| 8 |  |  | 5 | 6.75\% | 5.00\% | 90.0\% | 6.32\% | 1,310 | 5.56\% | 127,628 | 6,078 |
| 9 |  |  | 6 | 6.75\% | 5.00\% | 90.0\% | 6.32\% | 1,383 | 5.56\% | 134,010 | 6,381 |
| 10 |  |  | 7 | 6.75\% | 5.00\% | 90.0\% | 6.32\% | 1,460 | 5.56\% | 140,710 | 6,700 |
| 11 |  |  | 8 | 6.75\% | 5.00\% | 90.0\% | 6.32\% | 1,541 | 5.56\% | 147,746 | 7,036 |
| 12 |  |  | 9 | 6.75\% | 5.00\% | 90.0\% | 6.32\% | 1,627 | 5.56\% | 155,133 | 7,387 |
| 13 |  |  | 10 | 6.75\% | 5.00\% | 90.0\% | 6.32\% | 1,717 | 5.56\% | 162,889 | 7,757 |

Columns C-E and H-J's formulas are identical to Example 8.2.
We added an additional input in Cell B7 for the guaranteed minimum cap rate of $2 \%$. Instead of solving for the participation rate as in Example 8.2, we input Column F as $90 \%$. We inserted Column G for the cap rate which is set each year. We describe how we calculated the $6.32 \%$ cap rate at the end.

Although we do not modify Column H's formula, observe that in order to have Column J-K's EOP Account and Index Credit have the same outcome (numerical values) as Examples 8.1-2, the Index Return is $0.05 / 90 \%=5.56 \%$ in Example 8.3.

We modified Column K's Index Credit for the cap: Index Credit ${ }_{k}=$ Max(0\%, Min(Capk, Participation Rate $k \times$ Index Return $k) \times$ Index $_{k}$.
$\mathrm{K} 4=\operatorname{MAX}(0, \operatorname{MIN}(\mathrm{G} 4, \mathrm{I} 4 * \mathrm{~F} 4)) * \mathrm{~J} 3$, etc.
Next, Figure 8.5b presents the option price calculations and the insurer's invested assets.
Figure 8.5b

| 1 | C | N | 0 | $P$ | Q | R | S | T | U | V | W | X | Y |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | F(A) | Long ATM Call |  | Short |  | Requirements |  | Invested Assets |  |  |  |  |  |
| 2 | Policy <br> Year | d1 | Option <br> Cost | d1 | Option <br> Cost | Spread | Guaranteed EOP Account | Bond | Option <br> Budget | Shortfall | Total | \#Calls | Goal <br> Seek |
| 3 | 0 | 0.225 | 69.68 | 0.634 | 23.61 |  |  | 95,316 | 4,684 | 1,587 | 100,000 | 67.2 | 0.0 |
| 4 | 1 | 0.225 | 73.55 | 0.634 | 24.92 | 1,750 | 100,000 | 100,082 | 4,918 | 1,666 | 105,000 | 66.9 | 0.0 |
| 5 | 2 | 0.225 | 77.63 | 0.634 | 26.31 | 1,838 | 105,000 | 105,086 | 5,164 | 1,750 | 110,250 | 66.5 | 0.0 |
| 6 | 3 | 0.225 | 81.95 | 0.634 | 27.77 | 1,929 | 110,250 | 110,340 | 5,422 | 1,837 | 115,763 | 66.2 | 0.0 |
| 7 | 4 | 0.225 | 86.50 | 0.634 | 29.31 | 2,026 | 115,763 | 115,857 | 5,693 | 1,929 | 121,551 | 65.8 | 0.0 |
| 8 | 5 | 0.225 | 91.31 | 0.634 | 30.94 | 2,127 | 121,551 | 121,650 | 5,978 | 2,026 | 127,628 | 65.5 | 0.0 |
| 9 | 6 | 0.225 | 96.38 | 0.634 | 32.66 | 2,233 | 127,628 | 127,733 | 6,277 | 2,127 | 134,010 | 65.1 | 0.0 |
| 10 | 7 | 0.225 | 101.73 | 0.634 | 34.47 | 2,345 | 134,010 | 134,119 | 6,591 | 2,233 | 140,710 | 64.8 | 0.0 |
| 11 | 8 | 0.225 | 107.38 | 0.634 | 36.39 | 2,462 | 140,710 | 140,825 | 6,920 | 2,345 | 147,746 | 64.4 | 0.0 |
| 12 | 9 | 0.225 | 113.35 | 0.634 | 38.41 | 2,586 | 147,746 | 147,867 | 7,266 | 2,462 | 155,133 | 64.1 | 0.0 |
| 13 | 10 | 0.225 | 119.65 | 0.634 | 40.54 | 2,715 | 155,133 | 155,260 | 7,629 | 2,585 | 162,889 | 63.8 | 0.0 |

## Page 12
Columns L-O, R-U, and W-X's formulas and values are identical to Example 8.2.
We inserted Columns P-Q to calculate the bull spread short call's price with strike price $=$ Index $_{\mathrm{k}}$ $\times\left(1+\mathrm{Cap}_{\mathrm{k}}\right)=\mathrm{Col} \mathrm{H} \times(1+\mathrm{Col} \mathrm{G})$. The cap rate affects the short call's price. We also inserted Column V to calculate the option budget's shortfall to support the ( $90 \%$ ) participation rate.

The short call should have its own volatility input. Volatility decreases at a decreasing rate as strike prices increase - this property is called the volatility smile (named for how its graph looks). However, for simplicity we use the same volatility (Col L) for both calls.

Columns P-Q calculate the short call's d1 and price using Black-Scholes.

$$
\begin{aligned}
& \mathrm{P} 3=\left(\mathrm{LN}\left(\mathrm{H} 3 / \mathrm{H} 3^{*}(1+\mathrm{G} 4)\right)+(\mathrm{M} 3-\mathrm{B} \$ 6+(\mathrm{L} 3^{\wedge} 2) / 2)\right) / \mathrm{L} 3, \text { etc. } \\
& \mathrm{Q} 3=\mathrm{H} 3^{*} \mathrm{EXP}(-\mathrm{B} \$ 6)^{*} \mathrm{NORMDIST}(\mathrm{P} 3,0,1, \text { TRUE })-\mathrm{H} 3^{*}(1+\mathrm{G} 4)^{*} \mathrm{EXP}(- \\
& \text { M3)*NORMDIST(P3-L3, 0, 1, TRUE), etc. }
\end{aligned}
$$

Column V calculates the shortfall - the option budget needed to support the participation rate less the available option budget (Col U). To support a $90 \%$ participation rate, we need an option budget of Option Budget ${ }_{k}=$ Long Call Price $_{\mathrm{k}} \times$ Participation Rate $_{\mathrm{k}} \times \mathrm{AV}_{\mathrm{k}+1} /$ Index $_{\mathrm{k}}=$ Col O $\times$ Col F $\times$ Col J / Col H.

$$
\mathrm{V} 3=03^{*} \mathrm{~F} 4^{*} \mathrm{~J} 3 / \mathrm{H} 3-\mathrm{U} 3, \text { etc. }
$$

Finally, we solve for the cap rate in Column G such that the following hold: \# Call Options ${ }_{k}=$ Option Budget Shortfall ${ }_{k}$ / Short Call Price ${ }_{k}$, or that Col X = Col V / Col Q. We use Excel's "Goal Seek" utility found in the menu bar under "Data | What-If-Analysis" that solves for an unknown variable. We have used Goal Seek, for example, to solve for IRR. We use Column Y to calculate the quantity Col V - Col Q $\times$ Col X and use Goal Seek to solve for Col G such that Col $Y$ is 0 .

$$
\mathrm{Y} 3=\mathrm{V} 3-\mathrm{Q} 3^{*} \mathrm{X} 3 \text {, etc. }
$$


# End Example 8.3 

Next, Example 8.4 modifies Example 8.2 for a FIA with a non-zero floor and index spread. A nonzero floor substantially reduces the available option budget lowering the participation rate. For example, with a $1 \%$ floor and a $0 \%$ index spread, the participation rate is $60.8 \%$ as compared to Example 8.2's $67.2 \%$. A lower interest rate environment significantly increases the floor's impact. As a result, FIAs have $0 \%$ floors in practice. However, non-zero index spreads are common. We include Example 8.4 to illustrate the mechanics for both.
![Page 12 Image 1](ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_assets/ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_p12_img1.jpg)

## Page 13
First, we generalize Equation 8.1's relationships for a more robust FIA context with non-zero floors and index spreads.

The interest credit at $t=k$ for a FIA with participation rate ParRatek, Floor, (Index) Spread, and account value $A V_{k}$ is,

Index Credit ${ }_{k}=\max \left(\right.$ ParRate $\left._{k} *\left(\right.\right.$ Index Return $\left._{k}-\text { Spread }\right)$, Floor) $\times A V_{k}$
$=$ Floor $\times A V_{k}+$ ParRate $k_{k} \times A V_{k} /$ Index $k_{k} \times \max \left(\left(\right.\right.$ Index $k_{k+1}-$ Index $\left._{k}\right)-$ Spread $\times$ Index $_{k}-$ Floor $\times$ Index $_{k} /$ ParRate $\left._{k}, 0\right)$
$=$ Floor $\times A V_{k}+$ ParRate $k_{k} \times A V_{k} /$ Index $k_{k} \times \max \left(\right.$ Index $k_{k+1}-$ Index $_{k} \times(1-$ Spread - Floor $/$ ParRate $\left._{k}\right), 0)$
= \# Call Options $_{k} \times$ OTM Call Option payoff
where
(8.2a) strike $K_{k}=$ Index $_{k} \times\left(1-\right.$ Spread - Floor $/$ ParRate $\left._{k}\right)$ and
(8.2b) \# Call Options ${ }_{k}=$ Participation Rate $_{k} \times A V_{k} /$ Index $_{k}$ as previously.
When Spread $=0$ and Floor $=0$, Equation 8.2a is equivalent to Equation 8.1.
Example 8.4 modifies Example 8.2. We only describe what we have changed.

# Example 8.4 

Figure 8.6a illustrates rates and cash flows.
Figure 8.6a

|  | A | B | C | D | E | F | G | H | I | J |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | Fixed Indexed Annuity (FIA) |  |  | PH Account \& Insurer CFs |  |  |  |  |  |  |
|  |  |  |  | Portfolio <br> Rate | Option <br> Budget | Participation <br> Rate | Index | Index <br> Change | EOP <br> Account | Index <br> Credit |
| 2 | Input |  | Policy <br> Year |  |  |  |  |  |  |  |
| 3 | Deposit | 100,000 | 0 |  |  |  | 1,000 |  | 100,000 |  |
| 4 | Target Spread | 1.75\% | 1 | 6.75\% | 5.00\% | 62.9\% | 1,084 | 8.45\% | 105,000 | 5,000 |
| 5 | Benchmark Rate | 6.75\% | 2 | 6.75\% | 5.00\% | 62.9\% | 1,176 | 8.45\% | 110,250 | 5,250 |
| 6 | Floor | 1.00\% | 3 | 6.75\% | 5.00\% | 62.9\% | 1,275 | 8.45\% | 115,763 | 5,513 |
| 7 | Index Spread | 0.50\% | 4 | 6.75\% | 5.00\% | 62.9\% | 1,383 | 8.45\% | 121,551 | 5,788 |
| 8 | Index Dividend Rate | 1.75\% | 5 | 6.75\% | 5.00\% | 62.9\% | 1,500 | 8.45\% | 127,628 | 6,078 |
| 9 |  |  | 6 | 6.75\% | 5.00\% | 62.9\% | 1,627 | 8.45\% | 134,010 | 6,381 |
| 10 |  |  | 7 | 6.75\% | 5.00\% | 62.9\% | 1,764 | 8.45\% | 140,710 | 6,700 |
| 11 |  |  | 8 | 6.75\% | 5.00\% | 62.9\% | 1,913 | 8.45\% | 147,746 | 7,036 |
| 12 |  |  | 9 | 6.75\% | 5.00\% | 62.9\% | 2,075 | 8.45\% | 155,133 | 7,387 |
| 13 |  |  | 10 | 6.75\% | 5.00\% | 62.9\% | 2,250 | 8.45\% | 162,889 | 7,757 |

We added additional inputs in Cells B6:B7 for the Floor and Index Spread.

## Page 14
Recall, in Example 8.2 we solved for Participation Rate in Column F as \# Call Options / (AVk+1 / Indexk). However, the call's price depends on the strike price which depends on the participation rate which depends on the number of call options which depends on the call's price. These dependencies result in circular references if the participation rate is calculated in cells without code or manual hardcoding. We solved for the Participation Rate in Column U and then copy and pasted Column U to Column F as values. Furthermore, it takes a few "copy and paste values" iterations to converge as changing Column F changes Column U. Since our context is constant rates we only need to determine F4, e.g., F5 = F4, etc.

In order to have Column I-J have the same numerical outcomes as Examples 8.1-8.3, we modified Column G so the Index Return is 0.05/Participation Rate + Spread,

G4 = G3*(1+0.05/F4 + B\$7), etc.
Observe the Index Return is $0.05 / 62.9 \%+0.5 \%=8.45 \%$ in Example 8.4.
We modified Column J's Index Credit for the non-zero floor and index spread: Index Credit ${ }_{k}=$ Max(Floor, Participation Rate $\times$ (Index Return ${ }_{k}-$ Index Spread) $\times$ Index $_{k}$.

J4 = MAX(B\$6, (H4 - B\$7)*F4)*I3, etc.
Next, Figure 8.6b presents the option price calculations and the insurer's invested assets.
Figure 8.6b

|  | C | K | L | M | N | 0 | P | Q | R | S | T | U |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | FIA) | Market Inputs |  | Call Calculations |  | Requirements |  | Invested Assets |  |  |  |  |
| 2 | Policy <br> Year | Volatility | Risk-Free Rate | d1 | Option Cost | Spread | Guaranteed EOP Account | Bond | Option <br> Budget | Total | \# calls | Participation Rate |
| 3 | 0 | $15 \%$ | 4.00\% | 0.087 | 59.59 |  |  | 96,253 | 3,747 | 100,000 | 62.9 | $62.9 \%$ |
| 4 | 1 | $15 \%$ | 4.00\% | 0.087 | 64.63 | 1,750 | 101,000 | 101,066 | 3,934 | 105,000 | 60.9 | $62.9 \%$ |
| 5 | 2 | $15 \%$ | 4.00\% | 0.087 | 70.09 | 1,838 | 106,050 | 106,119 | 4,131 | 110,250 | 58.9 | $62.9 \%$ |
| 6 | 3 | $15 \%$ | 4.00\% | 0.087 | 76.01 | 1,929 | 111,353 | 111,425 | 4,338 | 115,763 | 57.1 | $62.9 \%$ |
| 7 | 4 | $15 \%$ | 4.00\% | 0.087 | 82.43 | 2,026 | 116,920 | 116,996 | 4,555 | 121,551 | 55.3 | $62.9 \%$ |
| 8 | 5 | $15 \%$ | 4.00\% | 0.087 | 89.39 | 2,127 | 122,766 | 122,846 | 4,782 | 127,628 | 53.5 | $62.9 \%$ |
| 9 | 6 | $15 \%$ | 4.00\% | 0.087 | 96.94 | 2,233 | 128,904 | 128,988 | 5,021 | 134,010 | 51.8 | $62.9 \%$ |
| 10 | 7 | $15 \%$ | 4.00\% | 0.087 | 105.13 | 2,345 | 135,350 | 135,438 | 5,273 | 140,710 | 50.2 | $62.9 \%$ |
| 11 | 8 | $15 \%$ | 4.00\% | 0.087 | 114.01 | 2,462 | 142,117 | 142,209 | 5,536 | 147,746 | 48.6 | $62.9 \%$ |
| 12 | 9 | $15 \%$ | 4.00\% | 0.087 | 123.64 | 2,586 | 149,223 | 149,320 | 5,813 | 155,133 | 47.0 | $62.9 \%$ |
| 13 | 10 | $15 \%$ | 4.00\% | 0.087 | 134.09 | 2,715 | 156,684 | 156,786 | 6,104 | 162,889 | 45.5 | $62.9 \%$ |

Columns K-L, O, and Q-T's formulas are identical to Example 8.2.
We modified Column M-N's formulas using Equation 8.2 such that the strike price $=$ Index $_{\mathrm{k}} \times(1$ + Spread + Floor / ParRate) $=$ Col G $\times(1+\mathrm{B} 7+\mathrm{B} 6 / \mathrm{Col} \mathrm{F})$.

$$
\begin{aligned}
& \mathrm{M} 3=(\mathrm{LN}(\mathrm{G} 3 /\left(\mathrm{G} 3^{*}(1+\mathrm{B} \$ 7+\mathrm{B} \$ 6 / \mathrm{F} 4)\right))+(\mathrm{L} 3-\mathrm{B} \$ 8+\left(\mathrm{K} 3^{\wedge} 2\right) / 2)) / \mathrm{K} 3 \\
& \mathrm{~N} 3=\mathrm{G} 3^{*} \mathrm{EXP}(-\mathrm{B} \$ 8)^{*} \mathrm{NORMDIST}(\mathrm{M} 3,0,1, \mathrm{TRUE})-\mathrm{G} 3^{*}(1+\mathrm{B} \$ 7+\mathrm{B} \$ 6 / \mathrm{F} 4)^{*} \mathrm{EXP}(-\text { L3)*NORMDIST(M3 - K3, 0, 1, TRUE) }
\end{aligned}
$$

## Page 15
We modified Column P's formula to reflect a non-zero floor for the EOP Guaranteed Account Value $=$ Account Value $_{\mathrm{k}} \times(1+$ Floor $)$,

$$
\mathrm{P} 4=\mathrm{I} 3^{*}(1+\mathrm{B} \$ 6) \text {, etc. }
$$

Observe the 1\% floor reduces the available Option Budget in Column R as compared to Example 8.2 by $1 \% \times$ Account Value $_{\mathrm{k}} /(1+$ Portfolio Rate $)$.

We moved Example 8.2's Column F Participation Rate calculation to Column U,

$$
\mathrm{U} 3=(\mathrm{R} 3 / \mathrm{N} 3) /(\mathrm{I} 3 / \mathrm{G} 3) \text {, etc. }
$$

Finally, we copied and pasted Column U's values to Column until Column U's values didn't change with a tolerance of 0.001 .

# End Example 8.4 

### 8.2 FA and FIA Stochastic Model

We extend Chapter 8.1-8.3's examples to non-constant interest rates and index returns. We also model decrements and project income statement and balance sheet items as in Chapters 2 and 5. Thus, the majority of formulas will be the same as Examples 8.1-2 Continued and as Chapter 4. As such, we focus on what is new or different. Although Chapter 8.2 goes from a constant rate and return context to simulations, we continue to keep the model simple.

Examples 8.1-4 did not use decrements. Similar to Chapters 3-6 and LTAM Part I, tab Assumption1 contains various ultimate mortality tables, lapse tables, product surrender charges, and corporate inputs for tax rates and investment spreads over Treasuries. The mortality basis is the 2012 IAM Basic ANB table which starts at age 0. IAM stands for Individual Annuity Mortality.

In Chapter 8's model, surrenders, deaths, and charges all occur EOP in that order as in Figure 8.7. With a small time step the decrement timing as EOP is not lossy as it is with Chapter 8's annual time step. The timing of surrender charges is continuous vs. curtate. Since surrender charges decrease on policy anniversaries, policyholders will wait nanoseconds after the EOP to avoid a higher charge.

Figure 8.7 MYGA and FIA Timing
![Page 15 Image 1](ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_assets/ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_p15_img1.jpg)

## Page 16
We simplify the context by excluding expenses such as commission and maintenance expenses and omit capital.

Recall as described in Chapter 4.4, in this book for an economic scenario generator we use the American Academy of Actuaries Interest Rate Generator (AIRG Version 7.1.202305) jointly produced by the American Academy of Actuaries (the Academy) and Society of Actuaries (SOA). The AIRG models U.S. Treasury rates and equity and bond returns. Tab Scen1000 has the 1,000 simulated index returns and spot rate curve scenarios. The spot rate curve output is listed by scenario and projection year in rows and maturities in columns. The output has rates for 0.25 , $0.5,1,2,3,5,7,10$, and 30 -year maturities. For space purposes we only store the $1,5,10$, and 20-year rates. Cells Scen1000!AH3:AM31002 are range named Scenario_1000_Rate.

For asset portfolios yields we use Asset Proxy Model II described in Chapter 2.3. Recall, the starting portfolio rate is either the yield of the starting assets on existing business or on new business is the initial yield earned from investing the first-year deposit or premium according to the investment strategy, e.g., a benchmark rate based on a mix of fixed income securities. Thereafter, liability cash flows and asset portfolio cash flows are reinvested at the scenario's then current benchmark rate. We assume asset cash flows are a specified (constant) percentage of the portfolio as it "rolls over" each period resulting from coupons, maturities, and pre-payments. The projected period's portfolio rate is the weighted-average of the newly invested assets and the remaining assets earning the prior portfolio rate. If there is negative cash flow, the portfolio rate remains unchanged. The asset proxy models ignore price changes from interest rate risk, capital gains and losses, and credit risk but does capture to some degree the changes and risks to earnings from interest rate changes over time and the resulting investment earnings.

The MYGA dynamic lapse rate assumption is as follows. Let CredRate = Credited Rate, CompRate = Competitor Rate. The dynamic lapse rate is Total Lapse = Base Lapse + Excess lapse where

Excess Lapse Rate $=-10 \times($ CredRate - CompRate $+0.5 \%)^{1.2} \times(1-7 \times$ Surrender Charge Rate) if CredRate $\geq$ CompRate $-0.5 \%$,
Excess Lapse Rate $=10 \times($ CompRate $-0.5 \%$ - CredRate $)^{1.2} \times(1-7 \times$ Surrender Charge Rate) if CredRate $\leq$ CompRate $-0.5 \%$, and
Competitor Rate $=\max ($ Scenario's 5 -year rate $+0.5 \%$, Scenario's 10 -year rate $+1 \%$ ).
A more compact equation is,
Excess Lapse Rate $==10 *$ SIGN(CredRate - CompRate $+0.5 \%) * \mid$ CredRate CompRate $+0.5 \% \mid^{\wedge} 1.2^{*}(1-7$ SurrenderCharge_Rate $))$.

The FIA dynamic lapse rate assumption is the same except we substitute Option Budget for Credited Rate. We deliberately chose the above parameters (10, 1.2 and 7) to exaggerate the excess lapses.

## Page 17
For simulations, we run a macro "Run Simulation Scenario" on tab Control. Labeling and tabs for Examples 8.5-7 are prefaced with an "E" due to VBA treating numbered tabs as the order in which tabs appear (e.g., tab $=3$ is the third worksheet in left-to-right order).

Example 8.5 extends Example 8.1.

# Example E8.5 

A 7-year MYGA was purchased with a \$100,000 deposit by a 50-year old male. The product has a $10 \%$ free withdrawal provision. We illustrate Scenario 6 and then present simulation results. The policy's associated inputs are in Figure 8.8a's Cells A5:B13.

Figure 8.8a

|  | A | B |
| :--: | :--: | :--: |
| 1 | Fixed Annuity (MYGA) |  |
| 2 | Input |  |
| 3 | Deposit | 100,000 |
| 4 | Target Spread | $1.75 \%$ |
| 5 | Free Partial Withdrawal | $10 \%$ |
| 6 | Initial Guar Rate | $4.75 \%$ |
| 7 | Initial Guar Period | 7 |
| 8 | Guar Minimum Rate | $1.50 \%$ |
| 9 | Mortality A/E | $100 \%$ |
| 10 | Benchmark: 5-year | $25 \%$ |
| 11 | Benchmark: 10-year | $50 \%$ |
| 12 | Benchmark: 20-year | $25 \%$ |
| 13 | Asset Portfolio Flow | $30 \%$ |
| 14 |  |  |
| 16 | Used By Macro |  |
| 17 | Scenario | 6 |

Inputs in cells B3..B8 specify the MYGA product information similar to Example 8.2 with the addition of Cell B5's Free Partial Withdrawal. Cell B9 is the A/E (Actual-to-Expected) factor to adjust mortality rates. Cells B10:B12 specify the asset allocation for the benchmark investment strategy. Cell B13 specifies the percentage of the bond and mortgage portfolio that turns over each year. Cell B17 specifies the scenario number from the set of 1,000 scenarios. The macro uses a FOR loop to populate cell B17 from 1 to 1,000 and the copies the desired output, which in this example is cell AF3' PV of net income, to tab E8.5_Out.

Figure 8.8 b presents rates and decrements.
Figure 8.8b

## Page 18
|  | C | D | E | F | G | H | I | J | K | L | M |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  |  | Rates |  |  |  | Decrements |  |  |  |  |
| 2 | Policy <br> Year | Age <br> BOP | Discount Rate | Benchmark Rate | Credited Rate | Competitor Rate | Mortality <br> Rate | Base <br> Lapse | Excess <br> Lapse | p | EOP \# <br> Policies |
| 3 | 0 |  |  |  |  |  |  |  |  |  | 1 |
| 4 | 1 | 50 | 6.40\% | 6.48\% | 4.75\% | 5.40\% | 0.229\% | 4\% | 0.2\% | 0.956 | 0.956 |
| 5 | 2 | 51 | 5.61\% | 6.86\% | 4.75\% | 5.88\% | 0.256\% | 4\% | 1.2\% | 0.946 | 0.904 |
| 6 | 3 | 52 | 5.41\% | 7.51\% | 4.75\% | 6.50\% | 0.283\% | 4\% | 3.0\% | 0.927 | 0.838 |
| 10 | 7 | 56 | 5.63\% | 6.84\% | 4.75\% | 5.85\% | 0.392\% | 40\% | 1.9\% | 0.579 | 0.364 |
| 11 | 8 | 57 | 5.72\% | 7.01\% | 5.01\% | 6.02\% | 0.427\% | 10\% | 1.8\% | 0.878 | 0.320 |

Column E retrieves the forward rate curve in tab Assumption1 as in previous chapters.

$$
\mathrm{E} 4=\text { INDEX }(\text { ForwardRateCurve1, C4, 1) }
$$

Column F retrieves (lookups) the 5-year, 10-year, and 20-year interest rates and calculates the new benchmark rate corresponding to cell B17's scenario,

$$
\begin{aligned}
\mathrm{F} 4= & \mathrm{B} \$ 10^{*} \text { INDEX }(\text { Scenario_1000_Rate, } 31^{*}(\mathrm{~B} \$ 17-1)+\mathrm{C} 4,4) \\
& +\mathrm{B} \$ 11^{*} \text { INDEX }(\text { Scenario_1000_Rate, } 31^{*}(\mathrm{~B} \$ 17-1)+\mathrm{C} 4,5) \\
& +\mathrm{B} \$ 12^{*} \text { INDEX }(\text { Scenario_1000_Rate, } 31^{*}(\mathrm{~B} \$ 17-1)+\mathrm{C} 4,6)+\text { Portfolio_Spread }
\end{aligned}
$$

Column G calculates the credited rate which is the initial guaranteed rate (B6) during the initial guarantee period (B7) and the portfolio rate (Col Z) less the target spread (B4), subject to guaranteed minimum rate (B8).

$$
\mathrm{G} 4=\mathrm{IF}(\mathrm{C} 3<\mathrm{B} \$ 7, \mathrm{~B} \$ 6, \mathrm{MAX}(\mathrm{~B} \$ 8, \mathrm{Z} 4-\mathrm{B} \$ 4)) \text {, etc. }
$$

Column H calculates the dynamic competitor rate using the specified formula and retrieves the 5 -year and 10-year interest rates.

$$
\begin{aligned}
& \mathrm{H} 4=\operatorname{MAX}\left(\operatorname{INDEX}\left(\text { Scenario_1000_Rate,31* }(\mathrm{B} \$ 17-1)+\mathrm{C} 4,4\right)+0.005\right. \\
& \text { INDEX }(\text { Scenario_1000_Rate, } 31^{*}(\mathrm{~B} \$ 17-1)+\mathrm{C} 4,5)+0.01 \text { ), etc. }
\end{aligned}
$$

Columns I, J, and M are the standard formulas for calculating decrements and EOP number of participants. We omit the BOP number of policies. The decrements are death and surrenders.

Mortality uses the 2012 IAM Basic Male ANB table which starts at age 0, multiplied by the A/E factor,

$$
\mathrm{I} 4=\text { INDEX }(\mathrm{IAM} \_12 \_\mathrm{M}, \mathrm{D} 4+1,1)^{*} \mathrm{~B} \$ 9
$$

Columns J-K retrieve the base lapse rates and calculate the dynamic excess lapse rate reflecting the credited rate, competitor rate, and surrender charge rate.

J4 = VLOOKUP(E4, Surrender_Rate, 2).
$\mathrm{K} 4=\mathrm{IF}(\mathrm{G} 4>\mathrm{H} 4-0.005,-10^{*}(\mathrm{G} 4-\mathrm{H} 4+0.005)^{\wedge} 1.2, \mathrm{IF}(\mathrm{G} 4=\mathrm{H} 4-0.005,0,10^{*}(\mathrm{H} 4-$ $\left.\mathrm{G} 4-0.005)^{\wedge} 1.2)\right)^{*}\left(1-7^{*}\right.$ VLOOKUP(C4,SurrenderCharge_Rate,2)) .

Alternatively,

## Page 19
$\mathrm{K} 4=10 * \operatorname{SIGN}(\mathrm{H} 4-\mathrm{G} 4-0.005) * \operatorname{ABS}(\mathrm{H} 4-\mathrm{G} 4-0.005)^{\wedge} 1.2 *(1-7 * \operatorname{VLOOKUP}(\mathrm{C} 4$, SurrenderCharge_Rate, 2)), etc.

Columns L and M calculate p (which is modified to add the excess lapse to the base lapse rate) and the EOP number of policies

$$
\begin{aligned}
& \mathrm{L} 4=(1-\mathrm{I} 4)^{*}(1-\mathrm{J} 4-\mathrm{K} 4) \text {, etc. } \\
& \mathrm{M} 3=1 \text { and } \mathrm{M} 4=\mathrm{M} 3 * \mathrm{~L} 4
\end{aligned}
$$

Figure 8.8c presents the policyholder's perspective of account value and the insurer's perspective of cash flows and values as in in previous chapters and LTAM Part I. Policyholder's projected conditional undecremented account values are calculated in Columns N-P. The insurer's projected decremented cash flows and values are calculated in Columns Q-V.

Figure 8.8c

| 1 | C | D | N | 0 | $P$ | Q | R | S | T | U | V |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  | PH Account |  |  | Insurer Cash Flows and Values |  |  |  |  | Validation |
| 2 | Policy <br> Year | Age <br> BOP | EOP <br> Account | Interest <br> Credit | Surrender <br> Charge | EOP AV | Interest <br> Credit | AV Released on Surrender | AV Released on Death | Surrender <br> Charges | AV Rollforward |
| 3 | 0 |  | 100,000 |  | 0 | 100,000 |  |  |  |  | 100,000 |
| 4 | 1 | 50 | 104,750 | 4,750 | 6,599 | 100,111 | 4,750 | 4,410 | 229 | 278 | 100,111 |
| 5 | 2 | 51 | 109,726 | 4,976 | 5,925 | 99,194 | 4,755 | 5,418 | 254 | 293 | 99,194 |
| 6 | 3 | 52 | 114,938 | 5,212 | 5,172 | 96,334 | 4,712 | 7,298 | 273 | 328 | 96,334 |
| 10 | 7 | 56 | 138,382 | 6,275 | 0 | 50,348 | 3,943 | 36,396 | 198 | 0 | 50,348 |
| 11 | 8 | 57 | 145,312 | 6,930 | 0 | 46,434 | 2,521 | 6,236 | 199 | 0 | 46,434 |

# Policyholder Perspective 

Columns N-P calculate policyholder's projected conditional undecremented account values and interest credited. Columns N-O calculate the EOP Account value and Interest Credit as in Example 8.2.

Column P calculates the surrender charge reflecting the free partial withdrawal (B5) using a continuous method, that is, uses the next period's surrender charge rate assuming the policyholder waits nanoseconds for the next period's $(\mathrm{Col} \mathrm{C}+1)$ lowered surrender charge rate,

$$
\mathrm{P} 4=\text { VLOOKUP }(\mathrm{C} 4+1 \text {, SurrenderCharge_Rate, 2)*N4*(1-B\$5), etc. }
$$

## Insurer Perspective

Columns Q-V calculate the insurer's decremented cash flows and values and are similar to Chapter 2, 3, and 5's formulas, e.g., see Example 5.2. Columns Q-U are the undecremented policyholder values multiplied by the BOP (prior EOP) or EOP number of policies and decrements as applicable.

$$
\mathrm{Q} 4=\mathrm{M} 4^{*} \mathrm{~N} 4 \quad \mathrm{R} 4=\mathrm{M} 3^{*} \mathrm{O} 4 \text {, etc. }
$$

## Page 20
The account value released upon death and surrender equal the BOP view of the EOP account value multiplied by the year's deaths and surrenders respectively
$\mathrm{S} 4=\mathrm{M} 3^{*}(\mathrm{~J} 4+\mathrm{K} 4)^{*}(\mathrm{~N} 3+04) \quad \mathrm{T} 4=\mathrm{M} 3^{*} \mathrm{I} 4^{*}(1-\mathrm{J} 4-\mathrm{K} 4)^{*} \mathrm{~N} 4$, etc.
The surrender charges collected are BOP number of policies multiplied by the lapse rate and the EOP surrender charge,
$\mathrm{U} 4=\mathrm{M} 3^{*}(\mathrm{~J} 4+\mathrm{K} 4)^{*} \mathrm{P} 4$, etc.
The reader should validate that the decremented account value rolls forward, that is,
Column Q = Prior_Q + R - S - T
We do this validation in Column V.

$$
\mathrm{V} 4=\mathrm{V} 3+\mathrm{R} 4-\mathrm{S} 4-\mathrm{T} 4(=\mathrm{Q} 3+\mathrm{R} 4-\mathrm{S} 4-\mathrm{T} 4)
$$

# Projection: Financial Statement Items 

Financial statement items are calculated in W-AF. The bulk of the financial projection is similar to Chapters 2 and 5 . We highlight what is new or different.

Figure 8.8d

|  | C | D | W | X | Y | Z | AA | $A B$ | $A C$ | $A D$ | $A E$ | AF |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  |  | B/S | I/S | B/S | I/S | I/S | I/S | I/S | I/S | I/S | I/S |
| 2 | Policy <br> Year | Age <br> BOP | Liability | Liability <br> Increase | Asset | Portfolio <br> Rate | Investment Income | Revenue | Cost | EBIT | Net Income | PV(Net <br> Income) |
| 3 | 0 |  | 100,000 | 100,000 | 100,000 |  |  |  |  |  |  | 8,352 |
| 4 | 1 | 50 | 100,111 | 111 | 100,111 | 6.48\% | 6,469 | 6,469 | 4,472 | 1,997 | 1,298 | 7,589 |
| 5 | 2 | 51 | 99,194 | (917) | 99,194 | 6.52\% | 6,514 | 6,514 | 4,463 | 2,052 | 1,334 | 6,681 |
| 6 | 3 | 52 | 96,334 | $(2,860)$ | 96,334 | 6.61\% | 6,545 | 6,545 | 4,383 | 2,161 | 1,405 | 5,637 |
| 10 | 7 | 56 | 50,348 | $(32,652)$ | 50,348 | 6.76\% | 5,602 | 5,602 | 3,943 | 1,660 | 1,079 | 1,422 |
| 11 | 8 | 57 | 46,434 | $(3,914)$ | 46,434 | 6.76\% | 3,396 | 3,396 | 2,521 | 874 | 568 | 935 |

Columns W and Y set the liability and asset equal the account value.

$$
\mathrm{W} 3=\mathrm{Q} 3, \quad \mathrm{X} 4=\mathrm{W} 4-\mathrm{W} 3, \quad \mathrm{Z} 3=\mathrm{W} 3, \text { etc. }
$$

Column Z calculates the BOP portfolio rate using our asset proxy model. The initial deposit earns the initial benchmark rate. Thereafter, the liability increase and the asset portfolio cash flow (B12) are reinvested at the current benchmark rate (Col F). The current portfolio rate (Col Z) is the weighted-average of the newly invested assets and the remaining assets earning the prior portfolio rate. If there is negative cash flow, we ignore any capital gains or losses and the portfolio rate remains unchanged.

$$
\begin{aligned}
& \mathrm{Z} 4=\mathrm{W} 3^{*} \mathrm{~F} 4 / \mathrm{Y} 3 \text { and } \\
& \mathrm{Z} 5=\mathrm{IF}\left(\mathrm{X} 4+\mathrm{B} \$ 13^{*} \mathrm{Y} 3<0, \mathrm{Z} 4,\left((1-\mathrm{B} \$ 13)^{*} \mathrm{Y} 3^{*} \mathrm{Z} 4+(\mathrm{X} 4+\mathrm{B} \$ 13^{*} \mathrm{Y} 3)^{*} \mathrm{~F} 5\right) / \mathrm{Y} 4\right)
\end{aligned}
$$

Columns AA-AF calculate the remaining income statement and balance sheet items using the same formulas as previous chapters such as Chapter 2 and 5 and LTAM Part I.

## Page 21
$$
\begin{array}{ll}
A A 4=Z 4^{*} Y 3-T 4^{*}\left((1+Z 4)^{\wedge} 0.5-1\right), & A B 4=A A 4, \text { etc. } \\
A C 4=X 4+S 4-U 4+T 4, & A D 4=A B 4-A C 4, \text { etc. } \\
A E 4=A D 4^{*}(1-\text { Income_Tax_Rate }), & A F 3=(A F 4+A E 4) /(1+E 4), \text { etc. }
\end{array}
$$

# Simulation: Macro and tab = E8.5 Output 

The macro "Run Scenario Simulation" on tab = Control is used to run the simulations for Examples 8.5-7.

Figure 8.8e

Cells B7..B10 are inputs. B7 indicates which scenario set to use. Currently only Scenario_1000 is enabled but would allow the reader to add additional sets. Cells B8..B9 indicate the calculation tab and the tab for the simulated output. Cell B10 indicates the Product Type, MYGA or FIA

The macro uses a FOR loop to populate cell B17 from 1 to 1,000 and the copies the calculation output cell out which is the PV of net income and pastes as values to tab E8.5Out Column C in succeeding rows. The macro uses tab Control Cell B10 indicating the Product Type to determine output cells and for FIA Cap the macro also solves for each year's cap rate. The macro then sorts the results by in descending order which is most to least profitable.

Figure 8.8f

Statistical risk metrics described in Chapter 4.3 are calculated in Cells G3..J7 except the percentiles and CTEs are viewed as the lowest (worst) outcomes.

Recall, rows 3-5 use Excel functions for average, standard deviation and percentile,
![Page 21 Image 1](ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_assets/ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_p21_img1.jpg)
![Page 21 Image 2](ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_assets/ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_p21_img2.jpg)

## Page 22
$$
\begin{array}{ll}
\mathrm{F} 3=\text { AVERAGE(C3:C1002) } & \mathrm{F} 4=\text { STDEV(C3:C1002) } \\
\mathrm{F} 5=\text { PERCENTILE.INC(C3:C1002, 0.3) } & \\
\mathrm{F} 6=\text { AVERAGE(C703:C1002) } & \mathrm{F} 7=\text { AVERAGE(C983:C1002) }
\end{array}
$$

We could have alternatively calculated CTEs as

$$
\begin{aligned}
& \text { F6 = SUMIFS(C\$3:C\$1002, \$A\$3:\$A\$1002 ,">700") / } 300 \\
& \text { F7 = SUMIFS(C\$3:C\$1002, \$A\$3:\$A\$1002 ,">980") / } 20
\end{aligned}
$$

Figure 8.8 g presents two common risk metric graphs. The first graph presents the metric (PV of Net Income) by Scenario in descending order. The second presents the metric's frequency distribution of outcomes, i.e., a histogram with the $x$-axis measured in standard deviations.

Figure 8.8g

# End Example 8.5 

Example 8.6 extends Example 8.2's FIA.

## Example E8.6

A 7-year FIA was purchased with a $\$ 100,000$ deposit by a 50-year old male. The product has a 10\% free withdrawal provision. The policy's associated inputs are in Figure 8.9a's Cells A3:B10.

We only present variables and formulas that are new or different. We illustrate scenario 24.
Figure 8.9a
![Page 22 Image 1](ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_assets/ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_p22_img1.jpg)
![Page 22 Image 2](ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_assets/ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_p22_img2.jpg)

## Page 23
|  | A | B |
| :-- | :-- | :-- |
| 1 | Fixed Indexed Annuity (FIA) |  |
|  |  |  |
| 2 | Input |  |
| 3 | Deposit | 100,000 |
| 4 | Target Spread | $1.75 \%$ |
| 5 | Mortality A/E | $100 \%$ |
| 6 | Free Partial Withdrawal | $10 \%$ |
| 7 | Benchmark: 5-year | $20 \%$ |
| 8 | Benchmark: 10-year | $50 \%$ |
| 9 | Benchmark: 20-year | $30 \%$ |
| 10 | Index Dividend Rate | $1.75 \%$ |

Figure 8.9 b presents rates and decrements.
Figure 8.9b

|  | C | D | E | F | G | H | I | J | K | L | M | N |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | Policy <br> Year | Age <br> BOP | Rates |  |  |  |  | Decrements |  |  |  |  |
|  |  |  | Discount Rate | Benchmark Rate | Competitor Rate | Index | Index Change | Mortality <br> Rate | Base <br> Lapse | Excess <br> Lapse | p | EOP # <br> Policies |
| 3 | 0 |  |  |  |  | 1,000 |  |  |  |  |  | 1 |
| 4 | 1 | 50 | 6.40\% | 6.50\% | 5.85\% | 879 | $-12.1 \%$ | 0.2285\% | 4\% | $1.1 \%$ | 0.947 | 0.947 |
| 5 | 2 | 51 | 5.61\% | 5.67\% | 4.00\% | 879 | 0.0\% | 0.2557\% | 4\% | $-2.5 \%$ | 0.983 | 0.930 |
| 6 | 3 | 52 | 5.41\% | 7.17\% | 5.65\% | 978 | 11.2\% | 0.2828\% | 4\% | 0.7\% | 0.950 | 0.884 |
| 10 | 7 | 56 | 5.63\% | 6.29\% | 4.76\% | 1,218 | 9.6\% | 0.3922\% | 40\% | $-1.8 \%$ | 0.615 | 0.472 |
| 11 | 8 | 57 | 5.72\% | 4.64\% | 2.89\% | 1,543 | 26.7\% | 0.4272\% | 10\% | $-11.7 \%$ | 1.013 | 0.478 |

Figure 8.9c presents the policyholder's perspective of account value and the insurer's perspective of cash flows and values as in in previous chapters and LTAM Part I.

Figure 8.9c

|  | C | D | 0 | P | Q | R | S | T | U | V | W | X | Y |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | Policy <br> Year | Age <br> BOP | PH Account |  |  |  |  | Insurer Cash Flows and Values |  |  |  |  | Validation |
|  |  |  | Option <br> Budget | Participation Rate | EOP <br> Account | Index <br> Credit | Surrender <br> Charge | EOP AV | Index Credit | AV Released on Surrender | AV Released on Death | Surrender <br> Charges | AV <br> Rollforward |
| 3 | 0 |  |  |  | 100,000 |  |  | 100,000 |  |  |  |  | 100,000 |
| 4 | 1 | 50 | 4.75\% | 64.0\% | 100,000 | 0 | 6,878 | 94,668 | 0 | 5,115 | 217 | 275 | 94,668 |
| 5 | 2 | 51 | 4.71\% | 63.4\% | 100,018 | 18 | 5,896 | 93,062 | 17 | 1,384 | 239 | 223 | 93,062 |
| 6 | 3 | 52 | 4.77\% | 64.2\% | 107,199 | 7,181 | 5,266 | 94,746 | 6,682 | 4,729 | 269 | 196 | 94,746 |
| 10 | 7 | 56 | 4.85\% | 65.3\% | 124,112 | 7,287 | 0 | 58,561 | 5,586 | 36,353 | 231 | 0 | 58,561 |
| 11 | 8 | 57 | 4.85\% | 65.3\% | 145,697 | 21,585 | 0 | 69,606 | 10,185 | $(1,159)$ | 299 | 0 | 69,606 |

# Projection: Financial Statement Items 

The bulk of the financial projection is similar to Chapters 2 and 5 . We highlight what is new or different.

Figure 8.9d

## Page 24
|  | C | D | Z | AA | AB | AC | AD | AE | AF | AG | AH | AI | AJ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | Policy <br> Year | Age <br> BOP | B/S | I/S | B/S | I/S | I/S | I/S | I/S | I/S | I/S | I/S | I/S |
| 2 |  |  | Liability | Lability <br> Increase | Asset | Portfolio <br> Rate | Bond <br> Income | Hedge <br> Income | Revenue | Cost | EBIT | Net <br> Income | PV(Net <br> Income) |
| 3 | 0 |  | 100,000 | 100,000 | 100,000 |  |  |  |  |  |  |  | 8,017 |
| 4 | 1 | 50 | 94,668 | $(5,332)$ | 94,668 | $6.50 \%$ | 6,200 | 0 | 6,200 | 4,181 | 2,018 | 1,312 | 7,219 |
| 5 | 2 | 51 | 93,062 | $(1,606)$ | 93,062 | $6.46 \%$ | 5,834 | 17 | 5,851 | 3,978 | 1,872 | 1,217 | 6,407 |
| 6 | 3 | 52 | 94,746 | 1,684 | 94,746 | $6.52 \%$ | 5,784 | 6,682 | 12,466 | 10,650 | 1,816 | 1,180 | 5,573 |
| 10 | 7 | 56 | 58,561 | $(30,997)$ | 58,561 | $6.60 \%$ | 5,632 | 5,586 | 11,218 | 9,659 | 1,560 | 1,014 | 2,081 |
| 11 | 8 | 57 | 69,606 | 11,045 | 69,606 | $6.60 \%$ | 3,678 | 10,185 | 13,863 | 12,848 | 1,015 | 660 | 1,541 |

Figure 8.9e

# Simulation: Macro and tab = E8.6_Output 

We ran the macro "Run Scenario Simulation" on tab = Control with inputs as in Figure 8.9.f. In addition to looping through all the scenarios, for product FIA Cap the macro also solves for each year's cap rate in Column Q.

Figure 8.9g

|  | A | B | C |
| :--: | :--: | :--: | :--: |
| 6 | Inputs |  |  |
| 7 | Scenario Set | Scenario_1000 | Enter which scenarios to run |
| 8 | Calculation Tab | E8.6 | Select tab for Example calculations |
| 9 | Output Tab | E8.6_Out | Select tab for Example simulation output |
| 10 | Product Type | FIA | Select Product Type |

Figures 8.8g-h present the risk metrics and graphs.
Figure 8.9g

|  | E | F |
| :-- | :-- | :-- |
| 1 | Risk Measures |  |
| 2 |  | PV(Net Income) |
| 3 | Average | 9,245 |
| 4 | Std Dev | 1,194 |
| 5 | 70\%-tile | 8,546 |
| 6 | CTE-70 | 7,957 |
| 7 | CTE-98 | 6,727 |
![Page 24 Image 1](ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_assets/ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_p24_img1.jpg)

## Page 25
Figure 8.9h

There could be other output variables of interest such as the undecremented account value at the end of the surrender charge period $(t=7)$ or the average participation rate over the 7 -year period.

# End Example 8.6 

Example 8.7 extends Example 8.3's FIA with a cap.

## Example E8.7

A 7-year FIA was purchased with a \$100,000 deposit by a 50-year old male. The product has a 10\% free withdrawal provision. The policy's associated inputs are the same as Figure 8.9a's Cells A3:B10. The variables and formulas are the same as Example 8.3 for the undecremented perspective and the same as Example 8.6 for the decremented perspective. We illustrate scenario 24 .

Figure 8.10a presents rates and decrements.
Figure 8.10a

Figure 8.10b presents the policyholder's perspective of account value and the insurer's perspective of cash flows and values as in in previous chapters and LTAM Part I.

Figure 8.10b
![Page 25 Image 1](ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_assets/ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_p25_img1.jpg)
![Page 25 Image 2](ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_assets/ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_p25_img2.jpg)

## Page 26
|  | C | 0 | $P$ | Q | R | S | T | U | V | W | X | Y | Z |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | PH Account |  |  |  |  |  | Insurer Cash Flows and Values |  |  |  |  | Validation |
|  | Policy <br> Year | Option <br> Budget | Participation Rate | Cap | EOP <br> Account | Index <br> Credit | Surrender <br> Charge | EOP AV | Index Credit | AV Released on Surrender | AV Released on Death | Surrender <br> Charges | AV <br> Rollforward |
| 3 | 0 |  |  |  | 100,000 |  |  | 100,000 |  |  |  |  | 100,000 |
| 4 | 1 | 4.75\% | 90\% | 5.8\% | 104,746 | 4,746 | 7,204 | 99,161 | 4,746 | 5,358 | 227 | 288 | 99,161 |
| 5 | 2 | 4.67\% | 90\% | 5.6\% | 109,638 | 4,892 | 6,463 | 101,920 | 4,631 | 1,610 | 261 | 245 | 101,920 |
| 6 | 3 | 4.76\% | 90\% | 5.8\% | 114,860 | 5,223 | 5,643 | 101,419 | 4,855 | 5,069 | 288 | 210 | 101,419 |
| 10 | 7 | 4.84\% | 90\% | 6.0\% | 138,851 | 6,407 | 0 | 65,349 | 4,902 | 40,626 | 257 | 0 | 65,349 |
| 11 | 8 | 4.84\% | 90\% | 6.0\% | 145,568 | 6,717 | 0 | 69,331 | 3,161 | $(1,118)$ | 297 | 0 | 69,331 |

# Projection: Financial Statement Items 

The financial projection formulas are similar to Examples 8.3 and 8.6.

Figure 8.10c

|  | C | AA | $A B$ | $A C$ | $A D$ | $A E$ | $A F$ | $A G$ | $A H$ | $A I$ | $A J$ | $A K$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | B/S | I/S | B/S | I/S | I/S | I/S | I/S | I/S | I/S | I/S | I/S |
|  | Policy <br> Year | Liability | Liability <br> Increase | Asset | Portfolio <br> Rate | Bond <br> Income | Hedge <br> Income | Revenue | Cost | EBIT | Net Income | PV(Net <br> Income) |
| 3 | 0 | 100,000 | 100,000 | 100,000 |  |  |  |  |  |  |  | 8,892 |
| 4 | 1 | 99,161 | (839) | 99,161 | 6.50\% | 6,199 | 4,746 | 10,945 | 8,915 | 2,031 | 1,320 | 8,142 |
| 5 | 2 | 101,920 | 2,759 | 101,920 | 6.42\% | 6,078 | 4,631 | 10,709 | 8,737 | 1,972 | 1,282 | 7,316 |
| 6 | 3 | 101,419 | (501) | 101,419 | 6.51\% | 6,332 | 4,855 | 11,187 | 9,203 | 1,984 | 1,290 | 6,422 |
| 10 | 7 | 65,349 | $(35,981)$ | 65,349 | 6.59\% | 6,364 | 4,902 | 11,266 | 9,501 | 1,765 | 1,147 | 2,612 |
| 11 | 8 | 69,331 | 3,982 | 69,331 | 6.59\% | 4,100 | 3,161 | 7,261 | 6,127 | 1,134 | 737 | 2,024 |

Figure 8.10d

|  | C | AP <br> Short OTM Call |  | AR <br> Requirements |  | AT <br> Conditional Invest |  | AX <br> Assets |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Page 27
Figures 8.9f-g present the risk metrics and graphs.
Figure 8.10f

|  | E | F |
| :-- | :-- | --: |
| 1 | Risk Measures |  |
| 2 |  | PV(Net Income) |
| 3 | Average | 8,604 |
| 4 | Std Dev | 542 |
| 5 | 70\%-tile | 8,427 |
| 6 | CTE-70 | 7,970 |
| 7 | CTE-98 | 6,764 |

Figure 8.10g

# End Example 8.7 

### 8.3 Model and Hedging Considerations

Chapters 8.1 and 8.2 present results with an aura of precision, both mathematically and operationally. Our illustrated products were simple and we made explicit and implicit model simplifications. Each of these simplifications must be used with judgment and their appropriateness depends on context and materiality. There are many potential complexities and considerations. We state a few.

We were able to buy and sell call options on the same underlying as the FIA with the desired strike price (to many decimal places) exactly when we wanted. Participation rates and caps were also to many decimal places. We treated our hedges as if they were 100\% effective. In reality, all hedges have a performance "error".

Static hedging strategies for our Examples' FIA 1-year point-to-point have several operational limitations. There may basis risk if the FIA index is not directly linked to a market index. The desired options and hedge instruments may not be available in the market. Insurers can and do use OTC products, for example, offered by banks. This was the case in the early 2000s. In addition to higher costs, this introduces counterparty risk. To meet insurer demands to hedge
![Page 27 Image 1](ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_assets/ltam_ii_chapter8_fixed_and_fixed_indexed_annuities_20240813_p27_img1.jpg)

## Page 28
FIAs and VAs, the Chicago Board Options Exchange (CBOE) introduced a number of products in the early 2010s.

Market prices change continuously. When does the insurer set the participation rates, cap rates, and index spreads for new sales or at anniversaries on in force business? Some insurers change FIA rates daily. Many insurers change FIA rates weekly or bi-weekly unless warranted by large market movements. Hedging will be ineffective since options cannot be purchased with the exact strike price and maturity or in the quantities desired. Low interest rates and high equity volatility pose challenges by reducing the option budget.

In regards to the number of options to buy, we ignored decrements. That is, our timing assumption simplified the impact decrements have on the number of options to purchase. That is, deaths and lapses do occur during the year (or month) and these policies do not receive the index credit, i.e., option payoff, and hence do not need to be hedged. As a result the Examples' insurer is over hedged. In practice, many insurers do ignore decrements and are over hedged.

We ignored capital and set liability reserves equal to the account value. IFRS, GAAP, and Statutory reserves are beyond scope but reserves can be significantly higher than the account value. We omitted capital. Regulatory capital and economic capital are important considerations.

Many insurers use static hedging strategies especially for simpler FIA designs. Static hedges are a buy-and-hold strategy - hedges are purchased at the onset and are held to maturity. This is simpler to operate and reduces transaction costs as compared to dynamic hedging. Static hedging does not allow for adjustments in response to market changes. If the market behaves differently than expected (e.g., higher volatility), static hedges might be ineffective, leading to losses between the hedge and the FIA's performance.

Static hedges are challenging to use for FIAs with longer time periods (e.g., 5-year point-topoint) or those with complex provisions - proprietary indices, exotic index crediting methods such as averaging, binary, or and high/low-water marks, monthly or daily point-to-points, riders such as GWLBs.

Many reinsurers use dynamic hedging strategies especially for FIA with exotic index crediting methods. Recall, dynamic hedging continuously monitors the position's delta or other risk metrics and adjusts the hedge frequently such as weekly, daily, or hourly by buying and selling the underlying. dynamic hedging offers the opportunity to save

Dynamic hedging allows for continuous adjustments to hedge positions in response to market movements providing better protection in theory against adverse market changes, thus managing risk more effectively. By frequently rebalancing the hedge, insurers can maintain a closer alignment with the FIA's performance, reducing the likelihood of significant losses due to market volatility. Frequent trading leads to higher transaction costs. The need for continuous monitoring and adjustments requires sophisticated systems, models, and expertise, increasing operational complexity.

## Page 29
Better hedge strategy designs and operational effectiveness are a source of competitive advantage. Superior hedge programs reduce risks and costs which can be used to increase competitiveness, earnings, capital efficiency, and enhance product designs.

# 8.4 Exercises