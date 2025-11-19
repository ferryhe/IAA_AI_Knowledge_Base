_Note: Source document was split into 2 OCR chunks (pages 1-21, pages 22-28) to stay within token limits._

# LTAM_II_Chapter9_Variable Annuities_20240818

## Page 1
# Chapter 9 Variable Annuities 

## Learning Outcomes

The student will be able to:
Construct deterministic and stochastic discrete cash flow models for basic variable annuity products and riders incorporating dynamic assumptions and policyholder behavior.

Chapter 9 illustrates cash flow models for VAs with GMDB, GMIB or GMABs. A VA's model projection node consists of the account value, guarantee base value, and other values. Values, cashflows, and payoffs are path dependent on economic and market outcomes as well as policyholder behavior for policy optionality including benefit utilization, partial withdrawals, surrenders, and transferring funds between subaccounts. For example, higher ITM-ness is tied to lower surrender activity.

Chapter 9.1 considers the connection between VA GMxB guarantee riders and Chapter 4's framework on financial options (or LTAM Part I Chapter 10). Chapter 9.2 illustrates a basic model for a VA with GMDB. Chapter 9.2's context is deterministic, with market returns that are constant over the entire time horizon. We present the policyholder perspective of undecremented conditional cash flows and the insurer's decremented perspective. Chapter 9.3 illustrates the construction of stochastic models and application to GMxBs. The models incorporate dynamic policyholder. We present the distribution of simulated outcomes as part of the risk profile. Chapter 9.4 briefly states a number of considerations related to VA models and products.

Like previous Chapters, Chapter 9's LTAM VA models strive to balance educational purposes, transparency, and simplicity. We focus on projecting the VA's charges and benefits, but do not complete the income statement or balance sheet. The additional financial statement variables (columns) and formulas would be the same as or similar to Chapter 8 and other previous chapters.

We assume 100\% of the account is allocated to a single equity subaccount, a large cap index fund such as the S\&P500, and none is allocated to the fixed account. We do not model a fixed account or transfers from equity subaccount to/from fixed accounts. Unlike Chapter 8, we do not illustrate incorporating hedging into Chapter 9's model and treat as beyond scope. In Chapter 9.4 we describe dynamic hedging and how to incorporate into cash flow models using model building blocks we already know and have covered.

We do not model liability values. Accounting standards and regulatory reserve and capital requirements such as U.S. GAAP, U.S. statutory (VM-21), and IFRS 17 entail fair value methods beyond scope. We do not model more than one rider on a policy, e.g., a GMDB+GMIB combination, nor do we model GLWBs. Chapter 9's VA cash flow model uses an annual time step. It is not uncommon for models of VAs with GMxBs to use weekly or daily time steps. An

## Page 2
annual time step removes the need to model interim activity and values. Additional simplifications are described later.

Making these simplifications does alter our educational purpose to illustrate how we use underlying building blocks to construct a VA model or to illustrate risk profiles. On the other hand, we could incorporate a more robust approach to each simplification resulting in an exponentially larger and more complex model but much less suitable for as an introductory model for students.

Chapter 9 builds upon previous chapter's model basic building blocks.

Chapter 9's model design focus is

1) modeling basic variable annuities and GMDB, GMIB, and GMAB riders
2) modeling dynamic assumptions and policyholder behavior
3) applying simulations and calculating CTE and VaR

# PONDER 

How does a VA's risk profile compare to a FIA's risk profile?

### 9.1 Embedded Options and Options Framework

The GMxBs are financial options embedded in insurance contracts. For VAs, the GMxB payoff is the excess of the benefit paid with the guarantee in excess of amount paid without the guarantee, i.e., the account value. GMxB excess benefits are amounts paid in excess of the amounts that would be paid in absence of the guarantee(s).

Recall, at any time the option is said in-the-money (ITM) if the option payoff would be positive and out-of-the-money if the payoff would be negative. For VAs, ITM-ness is based on the fair value of future benefits. As a proxy shortcut, common practice is to measure ITM-ness as a ratio. For example, GMDB ITM-ness is measured as Benefit Base divided by the Account Value.

A GMDB is similar to a European put option, however, the guarantee is exercised at death rather than a certain time of maturity - time is a random variable. The payoff upon death is the larger of the current account value and the GMDB benefit base.

At time $t$, let $S_{t}$ denote the value of the policyholder's account and $K_{t}$ denote the benefit base. For a ROP GMDB, $K_{t}=K_{0}=S_{0}$. Let $T$ denote the policyholder's future lifetime as in LTAM Part / Chapter 2.

At death, the beneficiary receives the amount

## Page 3
$$
\max \left(S_{T}, K_{T}\right)=S_{T}+\max \left(K_{T}-S_{T}, 0\right)
$$

The amount is the account value plus a put option payoff with strike price $K_{T}$ and expiration contingent on the death of the policyholder, i.e., a GMDB is a life-contingent put option.

An earnings-enhanced death benefit (EEB) can be similarly expressed as an option payoff. Suppose a VA has a ROP GMDB and an EEB paying the beneficiary an additional benefit equal to $35 \%$ of any increase in account value. Let $K$ denote the initial premium deposited. Upon the annuitant's death the beneficiary receives the amount.

$$
S_{T}+\max \left(K-S_{T}, 0\right)+0.35 \times \max \left(S_{T}-K, 0\right)
$$

The last term $\max \left(S_{T}-K, 0\right)$ is a call option's payoff with strike price $K$.
A GMAB is also similar to a European put option. The payoff is contingent on the policyholder persisting to the end of the GMAB period, that is, not dying or surrendering. Suppose a VA is sold to age $(x)$ with a GMAB guaranteeing that at the end of 10 years the account value will be at least $110 \%$ of the initial premium $K$. After 10 years, the account is worth

$$
\max \left(S_{10}, 1.1 K\right)=S_{10}+\max \left(1.1 K-S_{10}, 0\right)
$$

The embedded GMAB value at issue is ${ }_{10} p_{x} \times \operatorname{put}(1.1 K, 10)$ where $p$ reflects all decrements. When there are multiple sequential or renewal guarantee periods, the GMAB payoff and value formulas are more complicated.

For GMDBs and GMABs the underlying is generally the VA's account value and the benefit base is analogous to an option's strike price. For GMDBs and GMABs, the excess is the benefits paid in excess of the account value.

Excess Benefit $=\max (0$, Benefit Base - Account Value)
GMIBs and GMWBs may also appear to be similar GMDB and GMAB guarantee values with option payoffs. However, for GMIBs and GMWBs, the guaranteed benefit base is not the value or amount paid upon the annuitization or upon initiating withdrawals. The base is not analogous to an option strike price.

For a GMIB, the base is used to purchase a payout annuity using guaranteed annuity purchase rates or factors based on conservative interest and mortality guarantee assumptions. Suppose the form of guaranteed annuity is a life annuity. In absence of the guarantee, the current account value could be used to buy a life annuity.

The GMIB payoff is
$\max ($ Guaranteed Annuity Value, Account Value)
$=\max ($ Guaranteed Annuity Value, Current Annuity Value)
The payment using current assumptions is determined by,
Current Annuity Factor $=\operatorname{PV}(\$ 1 /$ month using current interest and mortality)

## Page 4
Current Annuity Factor $\times$ Current Payment $=$ Account Value
With the guarantee, the guaranteed base payment is determined by,
Guaranteed Annuity Factor $=\mathrm{PV}(\$ 1 /$ month using guaranteed interest and mortality)
Guaranteed Annuity Factor $\times$ Base Payment $=$ Benefit Base
The guaranteed annuity's value is
Base Payment $\times$ PV(\$1/month using current assumptions)
We can express the GMIB payoff in terms of payments,
$\max (0$, Base Payment - Current Payment $) \times \operatorname{PV}(\$ 1 /$ month using current assumptions $)$
or as,
Excess Benefit $=\max (0$, Base Payment - Current Payment $) \times$ Current Annuity Factor
Likewise for GMWBs, it is the withdrawal amounts stated as a percent of the base paid during the payout phase that are guaranteed rather than the value of the account. Similar to a GMIB, the base determines withdrawal amounts. For the value of excess benefits, we compare the present value of withdrawals using current assumptions with the account value.

VAs contain other embedded options. Policyholders have the option to withdraw some or all of the funds prior to maturity when it is no advantageous to do so, for example, when the guarantee is deeply out-of-the-money. By surrendering the policy, the policyholder forgoes paying GMxB charges or "option premium". If the account value is much greater than the guarantee value, surrendering and repurchasing a new contract with identical features is equivalent to resetting the base and beginning a new guarantee term.

Insurers offer reset provisions to prevent high surrender rates on deep out-of-the-money guarantees. Reset provisions provide policyholder-elected benefit base resets to the current account value thereby changing the strike price after issue. A reset also typically adjusts the guarantee period, for example, resetting a 10-year GMAB not only resets the guaranteed amount but also resets the start of the 10-year period to the reset date.

VAs consists of investments in one or more available mutual funds. Each fund varies as to its investment goals and risk level ranging from low to high risk. A policyholder's VA is a blend of underlying investments of varying risks as measured by beta or volatility. Policyholders are allowed to transfer funds which provides an option to alter the risk characteristics of the GMxBs' underlying after the policy is issued. Most products have transfer restrictions.

Embedded options and guarantees in retail insurance and wealth management products are more complex and challenging to model than plain vanilla options traded in financial markets. GMxB values are based on long-term guarantees, are path-dependent, and depend on policyholder behavior.

## Page 5
# 9.2 VA Deterministic Model and GMxB Cash Flows 

Chapter 9.2's context is deterministic. In addition, Example 9.1 illustrates constant market returns over the entire time horizon.

We assume 100\% of the account is allocated to a large cap index fund such as the S\&P500. We do not model a fixed account or transfers from separate accounts to/from fixed accounts. We do not model dollar cost averaging or partial withdrawals. Chapter 9's representative product fee assessment frequency is annual as is the timing of roll-ups and ratchets. Chapter 9's VA cash flow model use an annual time step. It is not uncommon for models of VAs with complex guarantees to use weekly or daily time steps. An annual time step removes the need to model interim activity such as deducting pro-rata charges.

Decrement assumptions are in tab = Assumption1. The initial examples do not model policyholder behavior. Although simplifications are made, the LTAM VA model illustrates the development and interdependencies between the account value and guarantee bases.

In Chapter 9's model, surrenders, M\&Es and rider charges, and deaths all occur EOP in that order as in Figure 9.1. With a small time step the decrement timing as EOP is not lossy as it is with Chapter 9's annual time step. M\&E and GMxB rider charges are only non-zero in the last time step of a policy year (e.g., policy month 12 or week 52 or day 365). Similar to Chapter 8's fixed annuities and FIAs, the timing of surrender charges is continuous vs. curtate. Since surrender charges decrease on policy anniversaries, policyholders will wait nanoseconds after the EOP to avoid a higher charge.

Figure 9.1 GMDB Timing

Our focus is on the GMxB pay offs, GMxB charges, and their present values. We do not calculate policy earnings or construct the projected income statement or balance sheet. We do not model insurer expenses or revenue sharing. Reserves and capital are beyond scope.

We need an assumption for market returns. In Example 9.1, we first use an $8 \%$ return and then change the assumption to a $5 \%$ return. We will see that an $8 \%$ is always out-of-the-money and a $5 \%$ return is always in-the-money.

A deterministic level return does not reveal the payoff guarantees under different possible market outcomes. Subsequent examples in Chapter 9.3 use 1,000 simulated economic scenarios for equity returns and interest rates.
![Page 5 Image 1](ltam_ii_chapter9_variable_annuities_20240818_assets/ltam_ii_chapter9_variable_annuities_20240818_p05_img1.jpg)

## Page 6
In Examples 9.1-9.6, a VA is sold January 1, 2026. We assume 100\% of the account value is in a large cap index fund with market returns net of investment fund fees. The VA has a free partial provision but partial withdrawals are assumed to be 0 . Mortality is $70 \%$ of the 1994 MGDB ALB table.

Example 9.1 presents the formulas for each column. Subsequent examples only present what has been modified from preceding examples.

# Example 9.1 

A VA with GMDB was purchased $1 / 1 / 26$ with a $\$ 110,000$ deposit. The GMDB has an annual 6\% roll-up. The policy's associated inputs are in cells A5:B15. Market returns net of investment fund fees in Column H. Discount rates equal to new money investment rates are in Column G. Policyholder's projected conditional undecremented account and benefit base values are calculated in Columns M-S. The insurer's projected decremented cash flows and values are calculated in Columns T-AE.

Inputs in cells B3:B12 specify the policyholder, VA, and GMDB information.

Figure 9.2a

| A | B |
| :--: | :--: |
| 1 | VA with GMDB Roll-Up |
| 2 | Input |
| 3 | Issue Date $1 / 1 / 26$ |
| 4 | Issue Age 50 |
| 5 | Fund Value 110,000 |
| 6 | M\&E Charge $1.15 \%$ |
| 7 | Mortality A/E $70 \%$ |
| 8 | Free Partial Withdrawal $10 \%$ |
| 9 | Valuation Date $12 / 31 / 25$ |
| 10 | Guarantee Basis 110,000 |
| 11 | Roll-Up Rate $6 \%$ |
| 12 | GMDB Charge $0.35 \%$ |

Figure 9.2b presents the typical indices and dates, rates and decrements.
Figure 9.2b

|  | C | D | E | F | G | H | I | J | K | L |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  |  |  |  | Input |  | Decrements |  |  |  |
|  | Proj |  | Policy | Age | Discount | Return | Mortality | Surrender |  | EOP 8 |
| 2 | Year | EOP Date | Year | BOP | Rate | Rate | Rate | Rate | p | Policies |
| 3 | 0 | 12/31/25 | 0 |  |  |  |  |  |  | 1 |
| 4 | 1 | 12/31/26 | 1 | 50 | 4.0\% | 8.0\% | 0.23\% | 2\% | 0.978 | 0.978 |
| 5 | 2 | 12/31/27 | 2 | 51 | 4.0\% | 8.0\% | 0.25\% | 2\% | 0.974 | 0.952 |
| 6 | 3 | 12/31/28 | 3 | 52 | 4.0\% | 8.0\% | 0.28\% | 3\% | 0.969 | 0.923 |

Columns G-H are the discount and return rates which are constant in this example. Columns I-L are the standard formulas for calculating decrements and EOP number of participants. We omit

## Page 7
the BOP number of policies. The decrements are death and surrenders. Mortality uses 70\% (B7) of the 1994 MGDB ALB table which starts at age 1,

I4 = INDEX(MGDB_94_M, F4, 1) *B\$7, etc.
Surrenders use the assumed base lapse rates and do not reflect policyholder behavior,

$$
J 4=\text { VLOOKUP(E4, Surrender_Rate, 2) }
$$

Columns K and L calculate p and the EOP number of policies

$$
\begin{aligned}
& \mathrm{K} 4=(1-\mathrm{I} 4)^{*}(1-\mathrm{J} 4) \text {, etc. } \\
& \mathrm{L} 3=1 \text { and } \mathrm{L} 4=\mathrm{L} 3^{*} \mathrm{~K} 4 \text {, etc. }
\end{aligned}
$$

# Policyholder Perspective 

Columns M-S calculate policyholder's projected conditional undecremented account and benefit base values. Observe that the policy is always out-of-the-money (Column S ITM < 100\%) since the account value grows at $8 \%$ while the guarantee base grows at $6 \%$.

Figure 9.2c

| 1 | E | M | N | 0 | $P$ | Q | R | S |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | PH Account and Benefit Basis |  |  |  |  |  |  |
|  | Policy <br> Year | EOP Account | Growth | M\&Es | GMDB <br> Charges | Surrender Charge | EOP Guarantee Base | ITM <br> Base / AV |
| 3 | 0 | 110,000 |  |  |  | 0 | 110,000 | $100 \%$ |
| 4 | 1 | 117,018 | 8,800 | 1,366 | 416 | 5,266 | 116,600 | $100 \%$ |
| 5 | 2 | 124,484 | 9,361 | 1,453 | 442 | 4,481 | 123,596 | $99 \%$ |
| 6 | 3 | 132,426 | 9,959 | 1,546 | 471 | 3,575 | 131,012 | $99 \%$ |
| 17 | 14 | 261,476 | 19,664 | 3,053 | 929 | 0 | 248,699 | $95 \%$ |
| 18 | 15 | 278,159 | 20,918 | 3,248 | 988 | 0 | 263,621 | $95 \%$ |

Column M calculates the EOP Account value which equals the prior EOP AV plus the growth in the account from investment returns less the M\&E and GMDB charges,

$$
\mathrm{M} 4=\mathrm{M} 3+\mathrm{N} 4-\mathrm{O} 4-\mathrm{P} 4
$$

Column N calculates the growth from investment returns,

$$
\mathrm{N} 4=\mathrm{H} 4^{*} \mathrm{M} 3
$$

Columns O-P calculates the M\&E and GMDB charges which are assessed at the end of the policy year and thus includes growth,

$$
\begin{aligned}
& \mathrm{O} 4=\mathrm{B} \$ 6 *(\mathrm{M} 3+\mathrm{N} 4) \\
& \mathrm{P} 4=\mathrm{B} \$ 12 *(\mathrm{M} 3+\mathrm{N} 4)
\end{aligned}
$$

Column Q calculates the surrender charge reflecting the free partial withdrawal (B9) using a continuous method, that is, uses the next period's surrender charge rate assuming the policyholder waits nanoseconds for the next period's ( $\mathrm{Col} \mathrm{E}+1$ ) lowered surrender charge rate.

## Page 8
With a free partial provision only ( $100 \%$ - free partial percentage) of the surrender charge is assessed.

$$
\mathrm{Q} 4=\text { VLOOKUP }(\mathrm{E} 4+1, \text { SurrenderCharge_Rate, 2 })^{*} \mathrm{M} 4^{*}(1-\mathrm{B} \$ 8)
$$

Column R calculates the EOP roll-up benefit base at the $6 \%$ roll-up rate (cell B11),

$$
\mathrm{R} 4=\mathrm{R} 3^{*}(1+\mathrm{B} \$ 11)
$$

Column S calculates the in-the-moneyness (ITM) as the guarantee base divided by the account value, i.e., the payoff upon death of the base versus the payoff the account value.

$$
\mathrm{S} 4=\mathrm{R} 4 / \mathrm{M} 4
$$

# Insurer Perspective 

Columns T-AA calculate the insurer's decremented cash flows and account and benefit base values. Columns AB-AE calculate GMDB payoffs and present values. Observe that the policy's guarantee never pays off - the excess of the death benefit over the account value is always 0 .

Figure 9.2d

|  | F | T | U | V | W | X | Y | Z | AA | AB | AC | AD | AE |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | Age <br> BOP | Insurer Cash Flows and Values |  |  |  |  |  |  |  |  |  |  |  |
|  |  | EOP AV | Growth | AV Released on Surrender | M\&Es | GMDB <br> Charges | AV Released on Death | EOP <br> Guar Base | Surrender Charges | Excess DB | PV(Excess DB Claims) | PV(GMDB Charges) | PV(Excess Charges) |
| 2 | 50 | 110,000 |  |  |  |  |  | 110,000 |  |  | 0 | 5,280 | $(5,280)$ |
| 4 | 51 | 114,389 | 8,800 | 2,376 | 1,339 | 407 | 289 | 113,980 | 126 | 0 | 0 | 5,084 | $(5,084)$ |
| 5 | 52 | 118,432 | 9,151 | 2,965 | 1,387 | 422 | 334 | 117,588 | 131 | 0 | 0 | 4,865 | $(4,865)$ |
| 6 | 53 | 122,077 | 9,475 | 3,581 | 1,430 | 435 | 383 | 120,774 | 127 | 0 | 0 | 4,625 | $(4,625)$ |
| 17 | 64 | 76,727 | 6,485 | 8,755 | 906 | 276 | 882 | 72,977 | 0 | 0 | 0 | 2,077 | $(2,077)$ |
| 18 | 65 | 72,524 | 6,138 | 8,286 | 858 | 261 | 935 | 68,734 | 0 | 0 | 0 | 1,899 | $(1,899)$ |

Columns T-AA are the undecremented policyholder values multiplied by the BOP or EOP number of policies and decrements as applicable.

$$
\begin{array}{ll}
\mathrm{T} 4=\mathrm{L} 4^{*} \mathrm{M} 4 & \mathrm{U} 4=\mathrm{L} 3^{*} \mathrm{~N} 4 & \mathrm{~V} 4=\mathrm{L} 3^{*} \mathrm{~J} 4^{*}(\mathrm{M} 3+\mathrm{N} 4) \\
\mathrm{X} 4=\mathrm{L} 3^{*}(1-\mathrm{J} 4)^{*} \mathrm{O} 4 & \mathrm{Y} 4=\mathrm{L} 3^{*} \mathrm{I} 4^{*}(1-\mathrm{J} 4)^{*} \mathrm{M} 4 & \mathrm{Z} 4=\mathrm{L} 4^{*} \mathrm{R} 4 \\
\mathrm{AA} 4=\mathrm{L} 3^{*} \mathrm{~J} 4^{*} \mathrm{Q} 4 &
\end{array}
$$

We do not calculate ITM-ness from the insurer perspective since it duplicates ITM from the policyholder perspective: ITM $=Z 4 / T 4$ but also equals $(L 4 * R 4) /\left(L 4^{*} M 4\right)=R 4 / M 4$ which is what is calculated in S4.

Column AB calculates the excess death benefit payoff from the guarantee. The number of deaths is BOP \# of polices $\times$ number not lapsing $\times$ number dying.

$$
\mathrm{AB} 4=\mathrm{L} 3^{*} \mathrm{I} 4^{*}(1-\mathrm{J} 4)^{*} \mathrm{MAX}(\mathrm{R} 4-\mathrm{M} 4,0)
$$

Columns AC-AE calculates the present value of the excess death benefit and GMDB charges using the discount rates in Column G. Column AE calculates the GMDB loss as guaranteed benefits paid less charges. The death benefits and charges occur EOP.

## Page 9
$$
\begin{aligned}
\mathrm{AC} 3 & =(\mathrm{AC} 4+\mathrm{AB} 4) /(1+\mathrm{G} 4) \\
\mathrm{AE} 3 & =\mathrm{AC} 3-\mathrm{AD} 3
\end{aligned} \quad \mathrm{AD} 3=(\mathrm{AD} 4+\mathrm{X} 4) /(1+\mathrm{G} 4)
$$

Column AF calculates the insurer's account value rollforward which serves as a validation check on the Column U-Y movements in the account, that is, EOP AV = BOP AV + Growth - AV Released on Surrender - M\&Es - Charges - AV Released on Death,

$$
\mathrm{AF} 4=\mathrm{AF} 3+\mathrm{U} 4-\mathrm{V} 4-\mathrm{W} 4-\mathrm{X} 4-\mathrm{Y} 4
$$

Columns T and AF are equal.

Figure 9.2e

|  | E | T | U | V | W | X | Y | AF |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | Insurer Cash Flows and Values |  |  |  |  |  | Validation |
| 2 | Policy <br> Year | EOP AV | Growth | AV Released on Surrender | M\&Es | GMDB <br> Charges | AV Released on Death | AV <br> Rollforward |
| 3 | 0 | 110,000 |  |  |  |  |  | 110,000 |
| 4 | 1 | 114,419 | 8,800 | 2,376 | 1,339 | 407 | 259 | 114,419 |
| 5 | 2 | 118,498 | 9,154 | 2,966 | 1,387 | 422 | 299 | 118,498 |
| 6 | 3 | 122,184 | 9,480 | 3,583 | 1,431 | 435 | 345 | 122,184 |
| 17 | 14 | 77,434 | 6,536 | 8,824 | 913 | 278 | 790 | 77,434 |
| 18 | 15 | 73,294 | 6,195 | 8,363 | 866 | 263 | 843 | 73,294 |

The observations that the policy is always out-of-the-money and the excess death is 0 is because we have assumed the market return is $8 \%$. After charges, the net rate credited to the account is $6.5 \%=8-1.15-0.35$ which is greater than the $6 \%$ roll-up rate, so the base is always less than the account value.

If we change the market return to 5\% as in Figure 9.2f then the policy is always in-the-money (Column 5 ITM > 100\%) and the net rate credited to the account is $3.5 \%=5-1.15-0.35$ which is less than the $6 \%$ roll-up rate, so the base is always greater than the account value.

Figure 9.2f 5\% Market Return

|  | E | H | M | R | S | AB | AC | AD | AE |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  |  | PH Account and Benefit Basis |  |  |  |  |  |  |
| 2 | Policy <br> Year | Return <br> Rate | EOP Account | EOP Guarantee Base | ITM <br> Base / AV | Excess <br> DB | PV[Excess <br> DB Claims] | PV[GMDB <br> Charges] | PV[Excess Charges] |
| 3 | 0 |  | 110,000 | 110,000 | 100\% |  | 3,676 | 4,133 | (458) |
| 4 | 1 | 5.0\% | 113,768 | 116,600 | 102\% | 6 | 3,817 | 3,903 | (86) |
| 5 | 2 | 5.0\% | 117,664 | 123,596 | 105\% | 14 | 3,955 | 3,660 | 295 |
| 6 | 3 | 5.0\% | 121,694 | 131,012 | 108\% | 24 | 4,089 | 3,406 | 683 |
| 17 | 14 | 5.0\% | 176,259 | 248,699 | 141\% | 219 | 4,819 | 1,201 | 3,619 |
| 18 | 15 | 5.0\% | 182,295 | 263,621 | 145\% | 246 | 4,766 | 1,076 | 3,690 |

# End Example 9.1 

### 9.3 VA Stochastic Model

## Page 10
Example 9.2 repeats Example 9.1 but we enhance the model to use a simulated scenario for input market returns and interest rates. We use a VBA macro to run 1,000 simulations.

Recall as described in Chapter 4.4, in this book for an economic scenario generator we use the American Academy of Actuaries Interest Rate Generator (AIRG Version 7.1.202305) jointly produced by the American Academy of Actuaries (the Academy) and Society of Actuaries (SOA). The AIRG models U.S. Treasury rates and equity and bond returns. We used the diversified large cap U.S. equity output which is the accumulated value of $\$ 1$ over the projection period. Tab Scen1000 has the 1,000 simulated equity returns and spot rate curve scenarios for a 30-year projection period. For space purposes we only store the $1,5,10$, and 20-year rates. Cells =Scen1000!B3:AF1002 are range named Scenario_1000_Equity.

We converted the accumulated wealth factors into annual rates of return. Equity return rates are in tab = Scen1000. Cells B2:BI1002 are range named Scenario_1000_Equity.

Figure 9.3

|   | A | B | C | D | E | F | G | M | N | 0 | $P$  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  1 | US Equity Returns |  |  | Year |  |  |  |  |  |  |   |
|  2 | Scenario | 0 | 1 | 2 | 3 | 4 | 5 | 11 | 12 | 13 | 14  |
|  3 | 1 | 1.000 | 0.972 | 1.007 | 1.232 | 1.334 | 1.501 | 3.129 | 2.549 | 2.760 | 3.630  |
|  4 | 2 | 1.000 | 1.274 | 1.772 | 2.097 | 2.072 | 1.885 | 0.860 | 0.960 | 0.957 | 1.342  |
|  5 | 3 | 1.000 | 1.092 | 1.063 | 1.087 | 1.273 | 1.582 | 3.597 | 4.075 | 3.670 | 3.983  |
|  1001 | 999 | 1.000 | 1.032 | 1.157 | 1.464 | 1.782 | 1.941 | 3.518 | 3.405 | 3.859 | 4.771  |
|  1002 | 1000 | 1.000 | 1.215 | 1.350 | 1.574 | 1.689 | 1.606 | 5.903 | 8.346 | 9.926 | 10.591  |

Spot rate curve output is listed by scenario and project year in rows and maturities in columns. The output has rates for $0.25,0.5,1,2,3,5,7,10$, and 30 year maturities. For space purposes we only store the 1-year and 10-year rates. We discount cash flows using the 10-year rate. which we use as the discount rate. Cells AH3:AJ31002 are range named Scenario_1000_Rate. We do not need to model portfolio rates since we have assumed $100 \%$ of the account value is allocated to the equity account and none is allocated to the fixed account. To extend our model to have non-zero allocation to the fixed account we could model the fixed income asset portfolio or use a proxy model (Asset Proxy Model II) for portfolio rates as in Chapter 8.

Reall, a dynamic assumption reflects an expectation that policyholder behavior is affected or changes due to current economic conditions (stochastic modeling) and contractual values and guarantees. Our surrender (lapse) and utilization assumptions reflect ITM-ness or market conditions at the projection nodes. Policyholder behavior is hard to predict but critical to VA product performance and risk profiles. Lower lapse rates are assumed if the guarantee is deep in-the-money and vice versa, higher lapse rates if the guarantee is deep out-of-the money. We use a simple dynamic lapse assumption for VAs with GMxBs - a step function: Dynamic Lapse Rate $=$ Base Rate $\times$ Factor where

|  ITM\% | Factor  |
| --- | --- |
|  $<75 \%$ | $150 \%$  |
|  $75 \% \leq$ ITM $<100 \%$ | $100 \%$  |

## Page 11
$100 \% \leq$ ITM $<110 \% \quad 90 \%$
$110 \% \leq$ ITM $<150 \% \quad 75 \%$
$>150 \% \quad 60 \%$
These factors are stored in tab Assump1 and range-named Surrender_Rate_Dynamic_Factor.
As in Chapter 8, labeling and tabs for Examples 9.2 and later are prefaced with an "E" due to VBA treating numbered tabs as the order in which tabs appear (e.g., tab $=3$ is the third worksheet in left-to-right order).

# Example E9.2 

We repeat Example 9.1 for a stochastic scenario. We illustrate scenario 257 which we chose since the guarantee goes deep in-the-money. We then present the simulation results.

Example 9.2's template and formulas are identical to Example 9.1 except for the following modifications. As in Chapter 8 we use an input in cell B17 to specify the scenario number from the set of 1,000 scenarios.

Figure 9.4a

|  | A | B |
| :-- | :--: | :--: |
| 16 | Used By Macro |  |
| 17 | Scenario | 257 |
| 18 | GMxB Rider | GMDB |

The macro uses a FOR loop to populate cell B17 from 1 to 1,000 and copy the desired output to tab E9.2_Out. Cell B18 specifies the rider type from a drop down menu. Cell B18 is used by the macro to determine the appropriate output cells and is not used within the calculations.

Figure 9.4b presents selected columns.
Figure 9.4b

| 1 |  | G | H | J | M | R | S | T | AB | AC | AD | AE |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Policy <br> Year | Discount Rate | Return Rate | Surrender <br> Rate | PH Account and Benefit Basis |  |  | Insurer Cash Flows and Values |  |  |  |  |
|  |  |  |  |  | EOP Account | EOP Guarantee Base | ITM Base / AV | EOP <br> Account | Excess DB | PV(Excess DB Claims) | PV(GMDB Charges) | $\begin{aligned} & \text { PV(Excess } \\ & \text { Charges) } \end{aligned}$ |
| 3 | 0 |  |  |  | 110,000 | 110,000 | $100 \%$ | 110,000 |  | 11,441 | 4,275 | 7,166 |
| 4 | 1 | 4.40\% | $-21.0 \%$ | $2 \%$ | 85,643 | 116,600 | $136 \%$ | 84,168 | 69 | 11,876 | 4,164 | 7,712 |
| 5 | 2 | 4.28\% | $-6.2 \%$ | $1 \%$ | 79,139 | 123,596 | $156 \%$ | 76,463 | 108 | 12,275 | 4,069 | 8,206 |
| 6 | 3 | 3.67\% | $-9.2 \%$ | $2 \%$ | 70,814 | 131,012 | $185 \%$ | 67,080 | 161 | 12,565 | 3,979 | 8,585 |
| 7 | 4 | 3.04\% | 29.8\% | $2 \%$ | 90,531 | 138,872 | $153 \%$ | 83,849 | 141 | 12,806 | 3,802 | 9,004 |
| 19 | 16 | 3.80\% | 28.7\% | 8\% | 202,015 | 279,439 | $138 \%$ | 80,829 | 400 | 13,777 | 1,884 | 11,894 |

Column G lookups the interest rates corresponding to cell B17's scenario,

$$
\text { G4 }=\text { INDEX }(\text { Scenario_1000_Rate, } 31^{*}(\mathrm{~B} \$ 17-1)+\mathrm{C} 4,3)
$$

Column H lookups the market index values and calculates the market return,

## Page 12
H4 = INDEX(Scenario_1000_Equity, B\$17, C4 + 1) / INDEX(Scenario_1000_Equity , $\mathrm{B} \$ 17, \mathrm{C} 4)-1$

Surrenders use the assumed base lapse rates multiplied by dynamic factors. ITM is a decimal displayed as percentage. The input factor table uses the percentage, i.e., an integer. We convert ITM to an integer by multiplying by a 100 and truncating.

J4 = VLOOKUP(E4, Surrender_Rate, 2) * VLOOKUP(TRUNC(100*S4), Surrender_Rate_Dynamic_Factor, 2)

The remaining formulas are identical to Example 9.1.

# Simulation: Macro and tab = E8.5 Output 

The macro "Run Scenario Simulation" on tab = Control is used to run the simulations for Examples 9.2-7.

Figure 9.4c

Cells B7:B9 are inputs. B7 indicates which scenario set to use. Currently only Scenario_1000 is enabled but would allow the reader to add additional sets. Inputs could also be added to specify to run a subset of the 1,000 scenarios. Cells B8:B9 indicate the calculation tab and the tab for the simulated output.

The macro uses a FOR loop to populate tab E9.2 cell B17 from 1 to 1,000 and then copies the calculation output cell out which are the PVs of the excess DB claims, charges, and difference then pastes as values to the output tab in succeeding rows. The macro uses E9.2 cell B18 indicating the guarantee type to determine which cells to copy from the calculation tab since the cells are different for GMDB, GMIB and GMAB. The macro then sorts the results by PV(Excess - Charges) in ascending order which is most to least profitable.

Figure 9.4d
![Page 12 Image 1](ltam_ii_chapter9_variable_annuities_20240818_assets/ltam_ii_chapter9_variable_annuities_20240818_p12_img1.jpg)

## Page 13
|  | A | $B$ | C | D | E | F | G | H | I | J |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | VA with GMDB Roll-Up: Stochastic Results |  |  |  |  |  | Risk Measures |  |  |  |
|  |  |  | PV(Excess | PV(GMDB | PV(Claims - |  | PV(Excess | PV(GMDB | PV(Claims - |  |
| 2 | Rank | Scenario | DB) | Charges) | Charges) |  | DB) | Charges) | Charges) |  |
| 3 | 1 | 340 | 0 | 9,550 | $(9,550)$ | Average | 2,384 | 5,247 | $(2,864)$ |  |
| 4 | 2 | 254 | 0 | 9,238 | $(9,238)$ | Std Dev | 3,467 | 947 | 4,161 |  |
| 5 | 3 | 639 | 0 | 8,732 | $(8,732)$ | 70\%-tile | 2,533 | 5,630 | $(2,482)$ |  |
| 6 | 4 | 492 | 0 | 8,610 | $(8,610)$ | CTE-70 | 6,712 | 4,362 | 2,350 |  |
| 7 | 5 | 687 | 0 | 8,510 | $(8,510)$ | CTE-98 | 13,973 | 3,398 | 10,575 |  |
| 1001 | 999 | 892 | 14,404 | 2,519 | 11,885 |  |  |  |  |  |
| 1002 | 1,000 | 262 | 15,585 | 3,524 | 12,062 |  |  |  |  |  |

Statistical risk metrics described in Chapter 4.3 are calculated in Cells H3:J7. Recall, rows 3-5 use Excel functions for average, standard deviation and percentile,

$$
\begin{array}{ll}
\mathrm{H} 3=\text { AVERAGE(C3:C1002) } & \mathrm{H} 4=\text { STDEV(C3:C1002) } \\
\mathrm{H} 5=\text { PERCENTILE.INC(C3:C1002, 0.7) } & \mathrm{H} 6=\text { AVERAGE(C703:C1002) } \\
\mathrm{H} 7=\text { AVERAGE(C983:C1002) } &
\end{array}
$$

Excel does not have functions for conditional tail expectations (CTE) which recall are the averages in the tail or the worst $(100-\mathrm{N}) \%$ of scenarios. We calculate CTE-70 and CTE-98 as the average of scenarios 701-1000 and 981-1000 respectively. We could have alternatively calculated CTEs as

$$
\begin{aligned}
& \text { F6 = SUMIFS(C\$3:C\$1002, \$A\$3:\$A\$1002,">700") / } 300 \\
& \text { F7 = SUMIFS(C\$3:C\$1002, \$A\$3:\$A\$1002,">980") / } 20
\end{aligned}
$$

Figure 9.4e presents two common VA risk metric graphs. The first graph presents the metric PV of Net Claims by scenario in descending order. The second presents the metric's frequency distribution of outcomes, i.e., a histogram with the $x$-axis measured in standard deviations.

Figure 9.4e

End Example 9.2
![Page 13 Image 1](ltam_ii_chapter9_variable_annuities_20240818_assets/ltam_ii_chapter9_variable_annuities_20240818_p13_img1.jpg)

## Page 14
We can implement any number of different dynamic assumption equations as well as for other assumptions. Typically dynamic assumptions are used for policyholder behavior such as surrenders, partial withdrawals, premium persistency, benefit utilization such as annuitization or the commencement of GMWB withdrawals, and fund transfers between risky and safe assets.

Assumptions can apply a dynamic multiplier to a base rate or can use predictive analytic and regression formulas or can use some combination. We provided some examples in Chapter 4.3. The following are examples of other dynamic policyholder behavior assumptions .

A general form for surrender and utilization rates is,

$$
\text { Rate }=a_{0}+a_{1} X_{1}+a_{2} X_{2}+a_{3} X_{3}
$$

where $a_{k}$ are determined through regression on relevant experience data and the $X_{k}$ are covariates.

A related form by letting $X_{k}=I T M^{k}$ is,

$$
\text { Rate }=a_{0}+a_{1} I T M+a_{2} I T M^{2}+a_{3} I T M^{3}
$$

Another approach is to apply multiplicative and/or additive factors to base rates. Factor formulas can be one-sided allowing only an increase or decrease or two-sided formula allowing both increases and decreases to base rates. Example 9.2 used this approach: Lapse Rate = Base Rate $\times$ Factor. Two other examples of factors are,

Factor $=1-0.8 \times($ ITM -1.2$)$ perhaps subject to a minimum and/or maximum
Factor $=$ ITM $^{-0.25 \times \text { Policy Year }}$ perhaps subject to a minimum and/or maximum.
The above examples use ITM as the driver. However, human behavior is influenced by many other factors.

We now consider an annual ratchet GMDB.

# Example 9.3 

Example 9.3 is identical to Example 9.2 except that the GMDB is an annual ratchet instead of a roll-up. Example 9.3 also illustrates scenario 257 and then presents simulation results. We make two modifications to Example 9.2. First, we change the input by greying out the roll-up rate.

Figure 9.5a

## Page 15
|  | A | B |
| :-- | :-- | :-- |
| 1 | VA with GMDB Ratchet |  |
|  |  |  |
| 2 | Input |  |
| 11 | Roll-Up Rate |  |
| 12 | GMDB Charge | $0.20 \%$ |
| 16 | Used By Macro |  |
| 17 | Scenario | 257 |
| 18 | GMxB Rider | GMDB |

Second, we change Column R's guarantee base formula,
$\mathrm{R} 4=\mathrm{MAX}(\mathrm{R} 3, \mathrm{M} 4)$, recall the roll-up formula is $\mathrm{R} 3^{*}(1+\mathrm{B} \$ 11)$
The different base growth method results in a different development of the guarantee base.
Figure 9.5b

Figure 9.5 c presents the simulation results and risk metrics.
Figure 9.5 c

|  | A | B | C | D | E | F | G | H | I | J |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | VA with GMDB Ratchet: Stochastic Results |  |  |  |  | Risk Measures |  |  |  |  |
|  |  |  | PV(Excess DB) | PV(GMDB Charges) | PV(Claims - <br> Charges) |  | PV(Excess DB) | PV(GMDB Charges) | PV(Claims - <br> Charges) |  |
| 2 | Rank | Scenario |  |  |  |  |  |  |  |  |
| 3 | 1 | 254 | 693 | 10,463 | $(9,770)$ | Average | 1,411 | 3,689 | $(2,277)$ |  |
| 4 | 2 | 687 | 143 | 8,020 | $(7,877)$ | Std Dev | 1,236 | 1,361 | 1,599 |  |
| 5 | 3 | 179 | 264 | 7,818 | $(7,554)$ | 70\%-tile | 1,526 | 4,101 | $(1,563)$ |  |
| 6 | 4 | 535 | 115 | 7,635 | $(7,520)$ | CTE-70 | 2,281 | 2,838 | (557) |  |
| 7 | 5 | 386 | 182 | 7,584 | $(7,402)$ | CTE-98 | 6,189 | 3,798 | 2,390 |  |
| 1001 | 999 | 74 | 11,380 | 5,533 | 5,847 |  |  |  |  |  |
| 1002 | 1,000 | 364 | 11,814 | 5,287 | 6,527 |  |  |  |  |  |

Figure 9.5d presents two VA risk metric graphs.
Figure 9.5d
![Page 15 Image 1](ltam_ii_chapter9_variable_annuities_20240818_assets/ltam_ii_chapter9_variable_annuities_20240818_p15_img1.jpg)

## Page 16
# End Example 9.3 

Example 9.4 presents a GMIB rider with a roll-up provision. For illustrative convenience, Chapter 9 uses a 20-year certain only annuity with monthly BOP payments as the guaranteed annuity form purchased by the GMIB benefit base rather than a life annuity. In Chapter 9's model, surrenders, annuitization elections, M\&Es and GMIB charges, and deaths all occur EOP in that order as in Figure 9.6. We continue to assume policyholders will wait nanoseconds after the EOP to avoid a higher charge.

Figure 9.6 GMIB Timing

We use a step function for the GMIB dynamic utilization assumption:

| ITM\% | Utilization Rate |
| :-- | :--: |
| $<125 \%$ | $2 \%$ |
| $125 \% \leq$ ITM $<150 \%$ | $4 \%$ |
| $150 \% \leq$ ITM $<175 \%$ | $8 \%$ |
| $175 \% \leq$ ITM $<200 \%$ | $12 \%$ |
| $>200 \%$ | $16 \%$ |

ITM-ness is measured by the relative value of the guaranteed annuity payment amount to the current annuity payment amount, i.e., the amount that could be purchased using the projection node's 10-year rate. We use the 10-year rate for convenience. Alternatively, we could use a benchmark rate reflecting the underlying investment strategy for payout annuities. The dynamic utilization rates are stored in tab Assump1 and range-named Surrender_Rate_Dynamic_Factor.
![Page 16 Image 1](ltam_ii_chapter9_variable_annuities_20240818_assets/ltam_ii_chapter9_variable_annuities_20240818_p16_img1.jpg)
![Page 16 Image 2](ltam_ii_chapter9_variable_annuities_20240818_assets/ltam_ii_chapter9_variable_annuities_20240818_p16_img2.jpg)

## Page 17
Most of Example 9.4's formulas are the same as for Example 9.1-3's GMDB, for example, the account value and guarantee base only depend on returns, charges, and roll-up rates and not whether the guarantee is a GMDB or a GMIB. We use the same dynamic lapse formula for both. We present the variables and formulas that are new or different than the GMDB examples.

# Example E9.4 

A VA with a roll-up GMIB is sold January 1, 2026. The GMIB waiting period is 4 years and is reflected in the benefit utilization rate (its equal to $0 \%$ for the first four years). The policy's associated inputs are in cells A3:B14. The guaranteed form of annuity payment is a 20-year certain-only annuity. Market scenario inputs are in Columns G-H corresponding to scenario 513.

Figure 9.7a

|  | A | B |
| :-- | :-- | :-- |
| 2 | Input |  |
| 12 | GMIB Charge | $0.40 \%$ |
| 13 | Guaranteed Annuity Rate | $3 \%$ |
| 14 | Guaranteed Annuity Factor | 181.42 |
| 16 | Used By Macro |  |
| 17 | Scenario | 513 |
| 18 | GMxB Rider | GMIB |

Cell B13 is an additional input for the guaranteed annuity interest rate. Cell B14 calculates the PV of $20 \$ 1$ BOP payments which is $\left(1-v^{20}\right) /(i v)$ where $i$ and $v$ use a monthly effective rate.

$$
B 14=\left(1-(1+B 13)^{\wedge}-20\right) /\left(\left((1+B 13)^{\wedge}(1 / 12)-1\right) /\left((1+B 13)^{\wedge}(1 / 12)\right)\right)
$$

Figure 9.7 b presents decrements and the policyholder's undecremented account values and benefit basis.

Figure 9.7b

| 1 |  | Decrements |  |  |  |  |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Policy <br> Year | Mortality <br> Rate | Surrender <br> Rate | Annuitization <br> Rate | p | EOP \# <br> Policies | EOP <br> Account | Growth | M\&Es | GMIB <br> Charges | Surrender <br> Charge | EOP Guarantee <br> Base |
| 3 | 0 |  |  |  |  | 1 | 110,000 |  |  |  | 0 | 110,000 |
| 4 | 1 | $0.23 \%$ | $1 \%$ | $0 \%$ | 0.986 | 0.986 | 128,892 | 20,921 | 1,506 | 524 | 5,800 | 116,600 |
| 5 | 2 | $0.25 \%$ | $1 \%$ | $0 \%$ | 0.983 | 0.969 | 129,742 | 2,893 | 1,516 | 527 | 4,671 | 123,596 |
| 10 | 7 | $0.44 \%$ | $12 \%$ | $2 \%$ | 0.859 | 0.726 | 177,665 | 45,269 | 2,075 | 722 | 0 | 165,399 |
| 11 | 8 | $0.49 \%$ | $6 \%$ | $2 \%$ | 0.917 | 0.666 | 178,162 | 3,302 | 2,081 | 724 | 0 | 175,323 |

Column K is an additional decrement for annuitizing, that is, electing or utilizing the GMIB. The decrement rate is also called the election rate, utilization rate, or annuitization rate. We lookup dynamic rates similar to Examples 9.2-3 using Column W's ITM. We use IF statements to set the annuitization rate to 0 during the 5 -year waiting period and $100 \%$ at age 75 and beyond. We also modify Column L's p to reflect the annuitization decrement.

## Page 18
```
\(\mathrm{K} 4=\mathrm{IF}(\mathrm{E} 4<5,0, \mathrm{IF}(\mathrm{F} 4>=75,1, \mathrm{VLOOKUP}\left(\mathrm{TRUNC}\left(100^{*} \mathrm{~W} 4\right)\right.\),
    Utilization_Rate_GMIB_Dynamic, 2)))
\(\mathrm{L} 4=(1-\mathrm{I} 4)^{*}(1-\mathrm{J} 4)^{*}(1-\mathrm{K} 4)\)
```

Column N-S's formulas for undecremented cash flows and values are the same as for GMDB.
Figure 9.7c presents variables related to ITM. ITM-ness is measured by the relative value of the guaranteed annuity payment amount to a current annuity payment amount that could be purchased.

Figure 9.7c

|  | E | G | T | U | V | W | X |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | Policy <br> Year | Input <br> Discount <br> Rate | Current <br> Annuity Factor | PH View of Payments and ITM |  |  |  |
|  |  |  |  | Guar Annuity <br> Payment | Current Annuity <br> Payment | ITM | Benefit <br> Base/AV |
| 3 | 0 |  |  |  |  |  | 100\% |
| 4 | 1 | 4.40\% | 161.17 | 643 | 800 | 80\% | 90\% |
| 5 | 2 | 5.04\% | 153.03 | 681 | 848 | 80\% | 95\% |
| 11 | 8 | 5.12\% | 152.09 | 966 | 1,171 | 82\% | 98\% |
| 12 | 9 | 5.05\% | 153.01 | 1,024 | 1,177 | 87\% | 103\% |

Column T calculates the current annuity factor as of the projection node. . The formula is the same as cell B14's guaranteed annuity factor except the input interest rate is column G rather than B13's guaranteed interest rate,

$$
\mathrm{T} 4=(1-(1+\mathrm{G} 4)^{\wedge}(-20)) /\left(\left((1+\mathrm{G} 4)^{\wedge}(1 / 12)-1\right) /\left((1+\mathrm{G} 4)^{\wedge}(1 / 12)\right)\right)
$$

Column U-V calculate annuity payments, Payment = Annuity Value / Annuity Factor,

$$
\mathrm{U} 4=\mathrm{S} 4 / \mathrm{B} \$ 14 \quad \mathrm{~V} 4=\mathrm{N} 4 / \mathrm{T} 4
$$

Since the annuities do not involve life continencies, ITM-ness is determined by the guaranteed annuity payment relative to the current annuity payment. Column W calculates ITM as the guaranteed payment divided by the current payment,

$$
\mathrm{W} 4=\mathrm{U} 4 / \mathrm{V} 4
$$

For comparison, Column X calculates the benefit base divided by the account value which is the metric used to measure GMDB and GMAB ITM-ness,

$$
\mathrm{X} 4=\mathrm{IF}(\mathrm{Y} 4=0,0, \mathrm{AF} 4 / \mathrm{Y} 4)
$$

Figure 9.7d presents the insurer's decremented cash flows.
Figure 9.7d

## Page 19
|  | E | G | Y | Z | AA | $A B$ | $A C$ | $A D$ | $A E$ | AL |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | Policy <br> Year | Input <br> Discount <br> Rate | EOP <br> Account | Growth | Insurer Cash Flows and Values |  |  |  |  | Validation |
|  |  |  |  |  | AV Released on Surrender | AV Released on Annuitization | M\&Es | GMIB <br> Charges | AV Released on Death | AV Rollforward Check |
| 3 | 0 |  | 110,000 |  |  |  |  |  |  |  |
| 4 | 1 | $4.40 \%$ | 127,058 | 20,921 | 1,571 | 0 | 1,488 | 517 | 287 | 127,058 |
| 5 | 2 | $5.04 \%$ | 125,736 | 2,851 | 1,871 | 0 | 1,472 | 512 | 317 | 125,736 |
| 11 | 8 | $5.12 \%$ | 118,598 | 2,398 | 7,885 | 2,471 | 1,392 | 484 | 586 | 118,598 |
| 12 | 9 | $5.05 \%$ | 109,798 | 3,144 | 7,304 | 2,289 | 1,290 | 449 | 612 | 109,798 |

We add Account Value Released on Annuitization (Column AB) to insurer cash flows and modify Column AL's Account Value Rollforward accordingly.

$$
\begin{aligned}
& A B 4=M 3 * K 4 *(1-J 4) *(N 3+O 4) \\
& A L 4=Y 3+Z 4-A A 4-A B 4-A C 4-A D 4-A E 4
\end{aligned}
$$

The remainder, Columns AF-AK use formulas identical to Examples 9.1-3.

Figure 9.7e

|  | E | AF | AG | AH | AI | AJ | AK |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | Policy <br> Year | EOP <br> Basis | Guarantee <br> Charges | Surrender <br> Charges | Excess <br> Annuitization | PV(Excess) | PV(GMIB <br> Charges) |
| 2 |  |  |  |  |  |  |  |

Figure 9.7f presents the simulation results and risk metrics.
Figure 9.7f

|  | A | B | C | D | E | F | G | H | I | J |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | VA with GMIB Roll-Up: Stochastic Results |  |  |  |  | Risk Measures |  |  |  |  |
|  |  |  | PV(Excess DB) | PV(GMDB Charges) | PV(Claims - <br> Charges) |  | PV(Excess DB) | PV(GMDB <br> Charges) | PV(Claims - <br> Charges) |  |
| 2 | Rank | Scenario |  |  |  |  |  |  |  |  |
| 3 | 1 | 340 | 0 | 20,089 | (20,089) |  | Average | 6,043 | 7,170 | $(1,127)$ |
| 4 | 2 | 254 | 0 | 19,813 | (19,813) |  | Std Dev | 10,077 | 2,973 | 12,193 |
| 5 | 3 | 777 | 0 | 18,433 | (18,433) |  | 70\%-tile | 5,137 | 8,237 | (840) |
| 6 | 4 | 43 | 0 | 18,277 | (18,277) |  | CTE-70 | 18,247 | 4,266 | 13,981 |
| 7 | 5 | 639 | 0 | 17,348 | (17,348) |  | CTE-98 | 43,362 | 2,433 | 40,929 |
| 1001 | 999 | 14 | 50,276 | 2,653 | 47,623 |  |  |  |  |  |
| 1002 | 1,000 | 486 | 54,032 | 2,300 | 51,732 |  |  |  |  |  |

Figure 9.7g presents two risk metric graphs.
Figure 9.7g

## Page 20
# End Example 9.4 

Next we consider a GMIB with an annual ratchet.

## Example E9.5

Example 9.5 illustrates a GMIB with a ratchet. As with GMDBs, the only formulaic difference is the benefit base.
$\mathrm{S} 4=\mathrm{MAX}(\mathrm{S} 3, \mathrm{~N} 4)$ instead of the roll-up's $=\mathrm{S} 3^{*}(1+\mathrm{B} \$ 11)$

Figure 9.8a

|  | E | N | 0 | $P$ | Q | R | S | T | U | V | W |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  | PH Account and Benefit Basis |  |  |  |  |  | PH View of ITM and Payments |  |  |  |
|  | Policy | EOP |  |  | GMIB | Surrender | EOP Guarantee | Current | Guar Annuity | Current Annuity |  |
| 2 | Year | Account | Growth | M\&Es | Charges | Charge | Base | Annuity Factor | Payment | Payment | ITM |
| 3 | 0 | 110,000 |  |  |  | 0 | 110,000 |  |  |  |  |
| 4 | 1 | 129,023 | 20,921 | 1,506 | 393 | 5,806 | 129,023 | 161.17 | 711 | 801 | $89 \%$ |
| 5 | 2 | 130,005 | 2,895 | 1,517 | 396 | 4,680 | 130,005 | 153.03 | 717 | 850 | $84 \%$ |
| 6 | 3 | 109,194 | $(19,204)$ | 1,274 | 332 | 2,948 | 130,005 | 157.85 | 717 | 692 | $104 \%$ |

Figure 9.8b presents the simulation results and risk metrics.
Figure 9.8b
![Page 20 Image 1](ltam_ii_chapter9_variable_annuities_20240818_assets/ltam_ii_chapter9_variable_annuities_20240818_p20_img1.jpg)
![Page 20 Image 2](ltam_ii_chapter9_variable_annuities_20240818_assets/ltam_ii_chapter9_variable_annuities_20240818_p20_img2.jpg)

## Page 21
Figure 9.8 c presents two risk metric graphs.

# End Example E9.5 

Our final example is a GMAB.

## Example 9.6

Example 9.6 illustrates a GMAB with the provision that after 10 years the account value will be at least $110 \%$ of the original deposit. Similar to a GMDB, the payoff is the excess of the benefit base over the account value. However, the payoff is a credit to the account value rather than a payment to a beneficiary. The payoff events are that the policy is in force at multiples of 10 years rather than death, i.e., potential payoffs at $t=10,20,30, \ldots$ The GMAB provision automatically renews with a guarantee that after another 10-year period the account value will be at least $110 \%$ of the current account value (which reflects any GMAB credit to the account).

We only present variables and formulas that are new or different than GMDB formulas. We illustrate scenario 48. We add inputs for the GMAB period and the GMAB factor in cells B13B14.

Figure 9.9a
A
B
1 VA with GMAB
2 Input
12 GMAB Charge $0.25 \%$
13 GMAB Period 10
14 GMAB Factor $110 \%$
16
Used By Macro
17 Scenario 48
18 GMxB Rider GMAB
Figure 9.9b presents decrements and the policyholder account values and benefit basis.
![Page 21 Image 1](ltam_ii_chapter9_variable_annuities_20240818_assets/ltam_ii_chapter9_variable_annuities_20240818_p21_img1.jpg)

## Page 22
Figure 9.9b

|  | E | H | M | N | 0 | $P$ | Q | R | S | T | U | V |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | Policy <br> Year | Return <br> Rate | EOP <br> Account | Growth | M\&Es | GMAB <br> Charges | Surrender Charge | GMAB <br> Segment | EOP Guarantee Base | AV*: Prior to GMAB Benefit | GMAB <br> Benefit | Benefit <br> Base/AV* |
| 2 |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | 0 |  | 110,000 |  |  |  | 0 | 0 | 110,000 | 110,000 |  | 100\% |
| 4 | 1 | 17.0\% | 126,910 | 18,712 | 1,480 | 322 | 6,853 | 1 | 121,000 | 126,910 | 0 | $95 \%$ |
| 5 | 2 | 8.9\% | 136,249 | 11,273 | 1,589 | 345 | 6,131 | 1 | 121,000 | 136,249 | 0 | $89 \%$ |
| 12 | 9 | -13.3\% | 89,817 | $(13,987)$ | 1,048 | 228 | 0 | 1 | 121,000 | 89,817 | 0 | $135 \%$ |
| 13 | 10 | 0.7\% | 121,000 | 631 | 1,040 | 226 | 0 | 1 | 121,000 | 89,182 | 31,818 | $136 \%$ |
| 14 | 11 | 9.7\% | 130,844 | 11,702 | 1,526 | 332 | 0 | 2 | 133,100 | 130,844 | 0 | $102 \%$ |
| 22 | 19 | -12.7\% | 235,424 | $(34,877)$ | 2,746 | 597 | 0 | 2 | 133,100 | 235,424 | 0 | $57 \%$ |
| 23 | 20 | 11.2\% | 258,159 | 26,401 | 3,011 | 655 | 0 | 2 | 133,100 | 258,159 | 0 | $52 \%$ |
| 24 | 21 | -1.4\% | 250,931 | $(3,665)$ | 2,927 | 636 | 0 | 3 | 283,975 | 250,931 | 0 | $113 \%$ |
| 32 | 29 | 8.6\% | 204,387 | 16,373 | 2,384 | 518 | 0 | 3 | 283,975 | 204,387 | 0 | $139 \%$ |
| 33 | 30 | 12.5\% | 283,975 | 25,447 | 2,643 | 575 | 0 | 3 | 283,975 | 226,616 | 57,359 | $125 \%$ |

Since the GMAB benefit increases the account value, we add Columns T-U related to the GMAB payoff. For calculation convenience we add column $R$ to track in which 10-year period (Cell B13) the policy year is, which we call GMAB Segment.

$$
\mathrm{R} 4=\operatorname{TRUNC}((\mathrm{E} 4+9) / \mathrm{B} \$ 13)
$$

Columns S calculates the GMAB guarantee base. For $\mathrm{k}=0,1,2, \ldots$, in years $10 \mathrm{k}, \ldots 10 \mathrm{k}+9$, the base equals the GMAB Factor of $110 \%$ (cell B14) multiplied by $A V_{10 k}$.

$$
\mathrm{S} 4=\mathrm{IF}(\mathrm{R} 4=\mathrm{R} 3, \mathrm{~S} 3, \mathrm{~B} \$ 14 * \mathrm{M} 3)
$$

Columns T calculates the EOP account value prior to any credit to the account from the GMAB Benefit, which equals BOP AV + Growth - M\&Es - GMAB Charges.

$$
\mathrm{T} 4=\mathrm{M} 3+\mathrm{N} 4-04-\mathrm{P} 4
$$

Column U calculates the GMAB Benefit. The payoff only occurs in the last year of each GMAB segment or at multiples of the GMAB period (cell B13). The payoff is the greater of 0 and the excess of the base over the account value.

$$
\mathrm{U} 4=\mathrm{IF}(\mathrm{R} 4=\mathrm{R} 5,0, \mathrm{MAX}(0, \mathrm{~S} 4-\mathrm{T} 4))
$$

In Columns S and U we could alternatively use modular arithmetic, for example,

$$
\mathrm{U} 4=\mathrm{IF}(\mathrm{MOD}(\mathrm{E} 4, \mathrm{~B} \$ 13)=0, \mathrm{MAX}(0, \mathrm{~S} 4-\mathrm{T} 4), 0)
$$

Column V calculates the benefit base divided by the account value prior to the GMAB benefit,

$$
\mathrm{V} 4=\mathrm{S} 4 / \mathrm{T} 4
$$

We modify Column M's EOP Account to include Column U's GMAB benefit,

$$
\mathrm{M} 4=\mathrm{T} 4+\mathrm{U} 4 \text { which also equals } \mathrm{M} 3+\mathrm{N} 4-04-\mathrm{P} 4+\mathrm{U} 4
$$

## Page 23
In this example, the GMAB is in-the-money at years 10 and 30 but out-of-the money at year 20.
The remainder of the formulas in Columns W-AI are the same as GMDB's formulas.
Figure 9.9 c presents the simulation results and risk metrics.
Figure 9.9c

|  | A | $B$ | C | D | E | F | G | H | I | J |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | VA with GMAB: Stochastic Results |  |  |  |  | Risk Measures |  |  |  |  |
|  |  |  | PV(Excess DB) | PV(GMDB <br> Charges) | PV(Claims - <br> Charges) |  |  | PV(Excess DB) | PV(GMDB <br> Charges) | PV(Claims - <br> Charges) |
| 2 | Rank | Scenario |  |  | $(19,903)$ |  |  |  |  |  |
| 3 | 1 | 254 | 0 | 19,903 | $(17,179)$ |  | Average | 2,596 | 5,922 | $(3,326)$ |
| 4 | 2 | 340 | 0 | 17,179 | $(16,882)$ |  | Std Dev | 5,237 | 2,451 | 6,233 |
| 5 | 3 | 43 | 0 | 16,882 | $(15,803)$ |  | 70\%-tile | 1,063 | 6,572 | $(3,207)$ |
| 6 | 4 | 777 | 0 | 15,803 | $(15,673)$ |  | CTE-70 | 8,392 | 4,479 | 3,912 |
| 7 | 5 | 317 | 0 | 15,673 | $(15,673)$ |  | CTE-98 | 23,454 | 3,999 | 19,455 |
| 1001 | 999 | 671 | 26,179 | 2,758 | 23,421 |  |  |  |  |  |
| 1002 | 1,000 | 104 | 32,831 | 4,699 | 28,132 |  |  |  |  |  |

Figure 9.9d presents two risk metric graphs.
Figure 9.9d

# End Example 9.6 

As compared to Example 9.5, the average has increased from $(1,775)$ to 257 , the standard deviation increased from 5,323 to 8,813 and the CTEs have increased significantly, just over doubling in magnitude. Although one should not read too much into the details, we can generally conclude that policyholders behave to capitalize on ITM scenarios and lapse in out-of-the-money scenarios, both of which decrease insurer performance and increase risk.

### 9.4 Model and Hedging Considerations
![Page 23 Image 1](ltam_ii_chapter9_variable_annuities_20240818_assets/ltam_ii_chapter9_variable_annuities_20240818_p23_img1.jpg)

## Page 24
Although in practice, VA models make many simplifications, they are not as sweeping as Chapter 9's simplifications. In general, simplifications must be used with judgment and their appropriateness depends on context and materiality. There are many potential complexities and considerations. We state a few.

Our illustrated products were simple and we made explicit and implicit model simplifications. However, our model simulations did illustrate that VAs with GMxBs are risky. Although in each example, PV (Net Claims) were negative in 700 to 800 of the scenarios (and hence the was profitable), the tail of losses was long and large. Although beyond scope, CTE-70s are used in conjunction with in reserve standards and CTE-98 in capital standards.

During the global financial crisis of 2008-09, some VA writers incurred high losses for a variety of reasons. A major reason was guaranteed benefits were too rich, for example, roll-up rates were too high (7\%) and ratchet frequencies were too high (daily). Due to the cost of hedging, many insurers had limited their hedging to delta and partial rho hedges. There were other reasons such as basis risk.

We did not model GLWBs (Guaranteed Living Withdrawal Benefits). When the first withdrawal is made is a key variable for performance and risk profiles. GLWBs are modeled by forming subcohorts for each projection month consisting of the subpopulation that became that took their first withdrawal that month, i.e., first-time utilizers. Chapter 10 introduces multistate models in the context of disability income and long-term care. In Chapter 10, we form monthly subcohorts corresponding to the onset of disability or long-term care.

In Chapter 8 we stated many insurers for FIAs take a simple approach to model future hedges using Black-Scholes rather than calculate fair values in a risk-neutral valuation framework. This is reasonable method since other than slippage from hedge ineffectiveness, the index credit paid to policyholders equals the hedge option payoffs since the insurer sets and resets product parameters for participation rates, caps, and index spreads (ignoring product minimum guarantees). However, with VAs, the insurer bears the risk including (negative) market returns and volatility. VA hedging is considerably more challenging in practice to execute and to model.

Recall from Chapter 4, the financial Greeks - delta, gamma, Vega, rho, theta, psi - measure the embedded options or GMxBs value sensitivity to changes in the underlying, volatility, interest rates, and other variables. Delta hedging is an investing strategy that hedges an option(s) price risk by taking an offsetting position with the same $\Delta$ resulting in a delta-neutral position, that is, the portfolio's $\Delta$ is 0 . However, since delta changes as time passes and the underlying price changes, to maintain a delta hedge a portfolio needs to be rebalanced. Dynamic hedging continuously monitors the position's delta and other Greeks or risk metrics and adjusts the hedge frequently such as weekly, daily, or hourly by buying and selling hedge instruments. Hedge instruments include equity futures and options such as puts, interest rate swaps and futures, swaptions, variance swaps, and variance futures.

In practice, insurers use a combination of static and dynamic hedging of the Greeks as well as reinsurance. Fully hedging delta and rho is common whereas partial hedges of gamma, Vega, or

## Page 25
cross Greeks such as delta-rho vary considerably reflecting insurer's risk management and product design strategies as well as market conditions. In addition to the two risk graphs we presented showing the distribution of outcomes by scenario and a histogram of PV(Net Claims), VA risk profile also portray the distribution and histograms of the various Greeks.

To quantify the Greeks and determine the trading hedge positions, we run the model multiple times shocking the desired variable up and down. For example, to quantify delta we shock the equity index value, run the model, and quantify the change in the guarantee's value (fair value, liability, or other value to be hedged). We shock both up and down to minimize directional bias versus a standard calculus definition of change which only shocks in one direction, e.g., variable + shock. All assets and liabilities are not locally (i.e., within a small range) monotonically increasing, decreasing, or symmetric. In these cases, shocking in only one direction either up or down could be inaccurate and misleading.

Although running the model multiple times sounds and is easy to program, doing so creates numerous challenges that must be overcome, namely, run time. Run time is a very real constraint for a VA model to simply rely on brute force methods to measure Greeks with outerinner loops in tandem with fair value valuations.

VA risk management starts with product design, of which evaluating hedging strategies is a key component. Design choices include the following. What is the structure, type, level, and frequencies of guarantee and charges, for example, roll-ups versus annual or daily ratchets? What are the fund options and investment and transfer frequency restrictions? Which product features can be used to manage policyholder behavior? For example, GWLBs provide incentives for policyholders to defer the first withdrawal. Transfer algorithm products have built in delta hedging, for example, Target Volatility and Constant Proportional Portfolio Insurance products.

Although reserve methods are beyond scope, we would be remiss not to introduce students to the greatest present value of accumulated deficit (GPVAD) method. A purpose of a reserve is so that the insurer has the funds on hand to fulfill its obligations. In previous chapters, reserves were calculated as the PV(Benefits and Expenses) - PV(Premiums) where premiums were either gross premiums or net premiums according to the valuation method. However, the context was deterministic.

As we have seen in Chapter 8 and 9, deterministic methods are not always appropriate as they do not capture the range of outcomes and risks. Only considering the PV at the valuation date ignores the funds that may be needed at future points in time. In a scenario, a guarantee could be significantly in-the-money creating a large shortfall at some point in the future only to later to be less in-the-money or be out-of-the-money. GPVAD methods are used in stochastic or principle-based reserving contexts to reflect the full spectrum and timing of risks.

Under the greatest present value of accumulated deficit (GPVAD) method, future asset and liability cash flows are projected for a block or group of policies over multiple scenarios. Under each scenario, at each projection node, the accumulated deficiency is calculated as the difference between the liability value (or regulatory reserve) and the available assets at that

## Page 26
point in time. That is, the deficit is the excess of the outstanding liability over accumulated assets at each time step in the projection. Each projection year-end's accumulated deficiency is discounted to the valuation date $(t=0)$ using appropriate (or prescribed) discount rates. The GPVAD is the most negative of those discounted values.

Across all scenarios, the GPVAD method identifies the scenario(s) that produces the greatest present value of accumulated deficiencies. This value represents the highest risk of underfunding the liabilities and is used to determine the required reserve.

# 9.5 Exercises 

## Problems are in Excel. They are also provided for your reference below.

1. A VA is sold April 22, 2026 with a $\$ 120,000$ deposit. If applicable, the roll-up rate is $5 \%$. Annual returns are input in Column B.
a) Calculate the EOP account value in Column C.
b) Calculate the roll-up benefit base in Column D.
c) Calculate an annual ratchet benefit base in Column E.
d) Calculate a combo benefit base which is the maximum of the roll-up and ratchet in Column F.
e) Calculate a combo benefit base which applies the roll-up rate to the ratchet in Column G.
2. A VA with an annual ratchet GMDB is sold January 1, 2023. The policy's associated inputs are in cells A5:B14 and in market scenario inputs are in Columns F-G. Partially completed cash flow model calculation are in Columns H-K.
a) Calculate the policyholder's projected conditional undecremented account and benefit basis values in Columns L-P.
b) Calculate the insurer's projected decremented cash flows and values in Columns Q-AC.
3. A VA with a roll-up GMIB is sold January 1, 2023. The policy's associated inputs are in cells A5:B15. The guaranteed form of annuity payment is a 20-year certain-only annuity. Market scenario inputs are in Columns F-G. Partially completed cash flow model calculation are in Columns H-K.
a) Calculate the policyholder's projected conditional undecremented account and benefit basis values in Columns M-Q.
b) Calculate the policyholder's guaranteed annuity factor in cell B16 and annuitization benefits and ITM-ness in Columns R-U.
c) Calculate the insurer's projected decremented cash flows and values in Columns V-AI.
4. A VA with a GMDB and GMIB is modeled using simulation. Given the stochastic results in cells A4:E1003, calculate the metrics in cells H5:J9.

## Page 27
5. A VA is sold March 28, 2023 with a $\$ 140,000$ deposit. The roll-up rate is $7 \%$. Simulated projected annual returns for the next 20 years are input in Column B.
a) Calculate the EOP account value in Column C.
b) Calculate the roll-up benefit base in Column D.
c) Calculate an annual ratchet benefit base in Column E.
d) Calculate a combo benefit base which is the maximum of the roll-up and ratchet in Column F.
e) Calculate a combo benefit base which applies the roll-up rate to the ratchet in Column G.
6. A VA with an annual ratchet GMDB is sold January 1, 2023. The policy's associated inputs are in cells A5:B14 and stochastic simulation market scenario inputs are in Columns G-H. Partially completed cash flow model calculation are in Columns I-L.
a) Calculate the policyholder's projected conditional undecremented account and benefit basis values in Columns M-S.
b) Calculate the insurer's projected decremented cash flows and values in Columns T-AE and rollforward validation in Column AF.
7. A VA with a roll-up GMIB is modeled using simulation and dynamic assumptions to model policyholder behavior. The stochastic results sorted in ascending order are in cells A4:E1003. Calculate the risk metrics in cells H5:J9.
8. A VA is sold May 9, 2023 with a $\$ 180,000$ deposit. The roll-up rate is $6 \%$. Simulated projected annual returns for the next 25 years are input in Column B.
a) Calculate the EOP account value in Column C.
b) Calculate the roll-up benefit base in Column D.
c) Calculate an annual ratchet benefit base in Column E.
d) Calculate a combo benefit base which is the maximum of the roll-up and ratchet in Column F.
e) Calculate a combo benefit base which applies the roll-up rate to the ratchet in Column G.
9. A VA with an annual ratchet GMDB is sold January 1, 2023. The policy's associated inputs are in cells A5:B14 and stochastic simulation market scenario inputs are in Columns G-H. Partially completed cash flow model calculation are in Columns I-L.
a) Calculate the policyholder's projected conditional undecremented account and benefit basis values in Columns M-S.
b) Calculate the insurer's projected decremented cash flows and values in Columns T-AE and rollforward validation in Column AF.

## Page 28
10. A VA with a roll-up GMAB is modeled using simulation and dynamic assumptions to model policyholder behavior. The stochastic results sorted in ascending order are in cells A4:E1003. Calculate the risk metrics in cells H5:J9.

# Exploratory Experiments 

Using one or more of the Examples' model spreadsheets, explore impacts in values and risk profiles from changing various inputs, dynamic formulas, and/or product features. For example, change roll-up rates, consider a roll-up in combination with a ratchet, consider a VA with a GMDB and a GMIB. Run the AIRG for monthly output and explore ratchet frequency.