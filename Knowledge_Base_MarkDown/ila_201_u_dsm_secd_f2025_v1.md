_Note: Source document was split into 4 OCR chunks (pages 1-22, pages 23-45, pages 46-68, pages 69-87) to stay within token limits._

# ILA-201-U_DSM_SecD_F2025_v1

## Page 1
# TheInfiniteActuary 

## ILA-201-U Section D

## Product Management

J. Eddie Smith, IV, FSA

Nov 2025 / Mar 2026 / Jul 2026

## Page 2
# Section D: Product Management 

D.1. Product Management Topics ..... 2
Embedded Value Practice and Theory ..... 3
ILA201-801: Diversification of Longevity and Mortality Risk ..... 20
ILA201-100: Diversification ..... 26
ILA201-101: Life In-Force Management: Improving Consumer Value and Long-Term Profitability ..... 36
ILA201-102: The Economics of Insurance ..... 47
FAQ on Certain Insurance Reserves Held After the TCJA ..... 57
Evolving Strategies to Improve Inforce Post-Level Term Profitability ..... 67
Mechanics of Dividends ..... 72

## Page 3
# Section D. 1 

## Product Management Topics

## Page 4
# Embedded Value Practice and Theory 

Source Author: Robert Frasca and Ken LaSorella (March 2009)

## Overview of This Reading

Embedded value (EV) is a measure of shareholders' value in an insurer: the current value of freely distributable surplus plus the PV of the existing business's future distributable earnings

The formulas in this reading present many, many opportunities for numerical exam questions, and they are best learned through the examples in the video lesson

## Key topics for the exam include:

- Definition of EV
- Comparisons between EV and AAV
- EV components and formulas
- Adjusted net worth (ANW)
- In-force business value (IBV)
- Cost of capital (CoC)
- Risk discount rate (RDR)
- PV of distributable earnings (PVDE)
- Methods for reflecting debt capital
- EV assumptions: economic vs. non-economic
- Market-consistent EV
- Time value of financial options and guarantees (TVOG)
- Risk-neutral assumptions
- Comparisons between EV and MCEV
- Analysis of Movement-how to perform and define key components
- Contribution from new business
- Target IBV
- Experience gains and losses
- Changes in valuation bases or assumptions
- EV disclosure guidance and issues


## Introduction

Embedded value (EV) = measurement of value that shareholders own in an insurance enterprise

- Shareholder value is made up of capital, surplus, and the PV of future earnings to from the existing business
- Has evolved to embody a codified collection of rules and practices

## Page 5
- Uses of EV:
- Justification for stock prices and acquisition purchase prices
- Performance measurement for executive compensation
- Profitability analysis for lines of business
- Assessment of returns for capital allocation purposes
- EV is similar to actuarial appraisal value (AAV), but there are differences:
- AAV includes contribution of future new business, while EV does not
- AAV uses higher discount rates than EV
- Expense assumptions in EV are more company-specific than those used in AAV, where assumptions reflect prevailing sentiment of the market


# History of EV 

- In the 1980s, companies in the UK started to disclose EV
- Dec 2001: Association of British Insurers develop guidelines for calculation of EV (Achieved Profits Method)
- European Embedded Value (EEV) defined in May 2004 by the CFO Forum
- Market-Consistent Embedded Value (MCEV) developed by the CFO Forum in 2008


## EV Mechanics and Formulas

## EV = Adjusted Net Worth (ANW) + In-Force Business Value (IBV)

- Adjusted Net Worth (ANW)
- ANW = Required Capital + Free Surplus
- ANW excludes intangible assets (e.g. goodwill)
- The entire ANW is not distributable since it includes required capital
- ANW starts with statutory capital and surplus but adds back items like AVR and non-admitted assets because these items have realizable value
- 2 approaches for valuing ANW

1. Most literal approach: only FS is marked to market and tax effected (adjusted for taxes)

* Assume assets supporting RC earn book rates of return

2. More practical approach: entire ANW is marked to market and tax effected

* Assume entire ANW earns a market rate of return
- In-Force Business Value (IBV)

## Page 6
- IBV $=$ PVBP $-\mathrm{PV}(\mathrm{CoC})$
- Book Profits (BP) $=$ Surplus $_{t}-$ Surplus $_{t-1} \times\left(1+i_{t}\right)$
* $i=$ after-tax rate of return on assets supporting surplus
* $\mathrm{BP}=$ growth in surplus other than interest earned on surplus $=$ statutory net income after taxes after removing investment income on surplus (required capital)
- Required Capital $(\mathrm{RC})=$ percent of regulatory risk-based capital
* US: usually the NAIC authorized control level RBC
* Canada: usually a \% of MCCSR
* Could also use the level of capital needed to maintain a specific rating from a rating agency capital or use economic capital
$-\mathrm{CoC}_{t}=\mathrm{RC}_{t-1} \times\left(\mathrm{RDR}-i_{t}\right)$
* Reflects the annual risk premium that must be paid to the owners of capital backing the business (the shareholders)


# - Risk discount rate (RDR) 

* RDR = discount rate for all PVs in an EV calculation
* RDR can technically vary with time, but most companies use a constant RDR
* RDRs often vary from company to company and from LOB to LOB
* RDR can be based on a weighted average cost of capital (WACC) or just on the cost of equity (e) (see "Debt and Debt-Like Capital" below)
- CAPM cost of equity: $e=R F+\beta \times(R M-R F)$
* $R F=$ risk-free rate
* $R M=$ expected equity rate of return (e.g. S\&P 500)
* $R M-R F=$ market risk premium
* $\beta=$ measure of relative risk (sensitivity) of a company's stock to that of the market

$$
\beta=\frac{\text { Covariance(Company's Stock Return, Market Total Return) }}{\text { Variance(Market Total Return) }}
$$

* If $\beta<1$, the company has less risk (and therefore less expected return) than the overall market
* If $\beta<0$, the company's stock return is negatively correlated with the market's return

## Page 7
# Debt and Debt-Like Capital 

In the UK and Canada, debt is not considered as part of the EV calculation $\Rightarrow \mathrm{RDR}$ is based on cost of equity capital only

Some jurisdictions (e.g. US) do not allow conventional debt to be used to fund capital requirements (e.g. can't borrow money to back RBC)

- However, debt-like instruments (surplus notes, capital notes, or preferred shares) can be combined with equity capital to fund total capital requirement
- RDR that reflects both cost of equity capital and cost of debt

Therefore, debt can either explicitly or implicitly recognized in the EV calculation

1. Explicit Recognition of Debt in Cost of Capital

- $\mathrm{RDR}=$ cost of equity only
- $\mathrm{CoC}=\mathrm{WACC}$
- Reflect debt $(D)$ explicitly in the CoC formula $\Rightarrow$ assume the after-tax cost of debt $=d$

$$
\begin{aligned}
\mathrm{CoC}_{t} & =\left(R C_{t-1}-D_{t-1}\right) \times\left(R D R-i_{t}\right)+D_{t-1} \times\left(d_{t}-i_{t}\right) \\
& =\left(R C_{t-1}-D_{t-1}\right) \times\left(e_{t}-i_{t}\right)+D_{t} \times\left(d_{t}-i_{t}\right) \\
& =\text { explicit cost of equity }+ \text { explicit cost of debt }
\end{aligned}
$$

2. Implicit Recognition of Debt in the RDR

- Rather than reflect debt explicitly, use $\mathrm{RDR}=\mathrm{WACC}$

$$
\mathrm{RDR}_{\mathrm{WACC}}=e \times\left(\frac{E}{E+D}\right)+d \times\left(\frac{D}{E+D}\right)
$$

- $\mathrm{CoC}_{t}=\mathrm{RC}_{t-1} \times\left(\mathrm{RDR}_{\mathrm{WACC}}-i_{t}\right)$
- WACC can be expanded to include other sources of capital like preferred stock

$$
\mathrm{RDR}_{\mathrm{WACC}}=e \times\left(\frac{E}{E+D+P}\right)+d \times\left(\frac{D}{E+D+P}\right)+p \times\left(\frac{P}{E+D+P}\right)
$$

EV results will be the same under the 2 methods if the following conditions are true:

1. Values for equity and debt used in WACC are fair values
2. Debt is maintained at a constant percentage of the PV of distributable Earnings (PVDE) throughout the projection period

PV of Distributable Earnings (PVDE) and IBV

## Page 8
Distributable earnings (DE) = stat after-tax stat net income profits - increase in RC

$$
\begin{aligned}
\mathrm{DE} & =B P_{t}+i \times R C_{t-1}+\left(R C_{t-1}-R C_{t}\right) \\
\mathrm{PVDE} & =\mathrm{PVBP}-\mathrm{PV}(\mathrm{CoC})+\mathrm{RC} \\
& =\mathrm{IBV}+\mathrm{RC} \\
\mathrm{EV} & =\mathrm{PVDE}+\mathrm{FS}
\end{aligned}
$$

If there is zero debt or $\mathrm{RDR}=$ WACC (implicit recognition of debt):

$$
\text { PVDE }=\mathrm{IBV}+\mathrm{RC}
$$

If explicit recognition of debt in RDR:

$$
\text { PVDE }=\mathrm{IBV}+(\mathrm{RC}-D)
$$

because RDR $=$ cost of equity only, and only the equity capital portion of RC is distributed (or injected) from shareholders

# IBV and Value of Business Acquired (VOBA) 

When acquiring another company, the buyer establishes a VOBA asset under US GAAP representing the value of future GAAP earnings

VOBA may take the form of an IBV calculation, but there are usually differences in accounting bases, assumptions, and the definition of RDR

- If GAAP reserves $>$ stat reserves, future GAAP profits will be higher
- VOBA tends to use a market view of assumptions, which will likely differ from the company-specific best estimate assumptions used for EV
- VOBA almost always uses a WACC RDR reflecting the acquirer's capital structure


## Value of New Business (VNB)

$\mathrm{VNB}=$ value of new business sold in since the prior reporting date

- Does not reflect the value of future new business to be sold in future reporting periods

Common point of confusion: You may have seen VNB in more of a pricing context where it refers to the PV of future profits expected from future new business. That is not what VNB refers to in an EV context. In this reading and any strict EV context, VNB captures the portion of current EV attributable to business that was sold since the last reporting date (since the last reporting date would not have assumed future new business). This is covered more in the Analysis of Movement section beginning on p. D-11.

## Use of EV to Support an Appraisal

$\mathrm{EV} \neq$ actuarial appraisal and generally can't be used directly to produce appraisal value

- EV does not value future new business, but an actuarial appraisal does

## Page 9
- An actuarial appraisal is likely to use different assumptions (e.g. the buyer's) than EV EV, along with normal financial and non-financial information, might provide additional benefit to an analyst


# Assumptions 

## Types of EV Assumptions

1. Non-economic projection assumptions - relate to existing and future operating environment of the company

- Narrowly focused on the company or LOB
- Policyholder behavior assumptions, mortality rates, interest-crediting strategies, etc.

2. Economic assumptions - relate to the existing and future economic environment

- Interest rates, asset default rates, credit spreads on reinvested assets, and rates of inflation
- Updated at each valuation date

Certain assumptions like claim inflation could fall into either category

## Non-economic assumptions

- Best estimate, entity-specific assumptions without PADs
- Can include extrapolation of observed trends (assuming mortality improvement is common)
- Combination of company data and industry data, depending on credibility
- Persistency rates tend to be more company-specific
- Consider the relationship between policyholder behavior (lapse rates), product design, and investment performance
- Expenses also rely more on company data
- All expenses should be reflected in EV calculations: acquisition, maintenance, and overhead
- Include expectation for expense inflation
- Expense improvement can be projected for start-up businesses
- Include an assumption for unanticipated one-time costs
- Project federal and local taxes on a best estimate basis
- Include highly probable future changes in tax law

## Page 10
# Economic Assumptions (RDR) 

Economic assumptions are based on management's best estimate, taking into account past experience and the economic environment on valuation date

- Assumed investment returns are based on actual asset portfolio performance less investment expenses and less expected defaults
- Do not capitalize excess investment return without reflecting the additional risk
- Example: if assuming higher credit spreads in investment returns, you should increase the RDR to reflect a higher risk margin
$\mathrm{RDR}=$ risk-free rate + risk margin
Two RDR approaches commonly used when reflecting the cost of debt:
- Top-down approach: group WACC
- Calculated using the equity cost of capital with allowance for the impact of debt financing on market-value basis
- Reflect the market's view of the effect of all types of risk of a company's business
- Bottom-up approach: product-specific WACC
- Reflects the differences in risk inherent in each product group
- Use product-specific betas
- Add additional risk margin for non-market risks at the product or group level
- Multinational companies often create country-specific RDRs


## Financial Options and Guarantees

Total value of financial options and guarantees $=$ Intrinsic Value + TVOG

- Intrinsic value $=\mathrm{O} / \mathrm{G}$ value assuming current in-the-moneyness of the $\mathrm{O} / \mathrm{G}$ does not change in the future
- Assumes current in-force is projected with best estimate assumptions (deterministic scenario)
- Example 1: VA GMDB $=1000$ and $A V=800$. The deterministic projection would start with a NAR of 200, which would steadily shrink as the AV grows. No allowance for the possibility that the $A V$ could drop in future scenarios.
- Example 2: VA GMDB $=1000$ and $A V=1100$. The intrinsic value would be zero. Essentially this means a deterministic projection would put a zero value on the GMDB, never accounting for the possibility that the GMDB could come back into the money.
- Time value of financial options and guarantees (TVOG) = additional value (to the policyholder) reflecting potential changes in financial markets that will increase/decrease the value of the options and guarantees before their expiry

## Page 11
- TVOG $=$ Deterministic PVDE - Mean Stochastic PVDE
- The mean stochastic PVDE reflects both the intrinsic value and time value
- The stochastic projection will result in a lower mean PVDE because there will be some scenarios where the options and guarantees become very valuable (e.g. VA guarantees that become very valuable when equity markets fall)


# EV reflecting TVOG $=$ Deterministic EV - TVOG 

- This effectively "swaps in" the stochastic PVDE to replace the deterministic PVDE


## Products That Have a TVOG Component

- VA and VUL with guarantees like GMDB, GMIB, GMAB, GMWB
- UL and fixed deferred annuities with guaranteed minimum crediting rates
- For these, the TVOG would capture the value to the policyholder (hence cost to the insurer) arising from the possibility that interest rates could fall below guarantees
- Options and crediting floors in EIA contracts and other fixed annuities and investment contracts
- UL with no-lapse guarantees (a.k.a. UL with secondary guarantees, or ULSG)

The company's asset portfolio can also contain investments with a TVOG component (e.g. CMOs)

- This is also a cost to the company because embedded options in assets like CMOs usually work against the investor (e.g. falling interest rates cause CMO prepayments to speed up)
- The stochastic projection should also capture this assuming the asset assumptions are set up accordingly


## Assumptions Needed for TVOG

TVOG assumptions, methodologies, and models should be consistent with other EV calculations Stochastic considerations:

1. Stochastic simulations can be based on a regime-switching lognormal model, Cox-Ingersoll-Ross, or other
2. Need policyholder behavior algorithm to reflect utilization of options and guarantees
3. Consider management actions when developing the stochastic model

- Example: how management might react to low interest rates

For simple, short duration options, TVOG can be calculated using closed-form solutions like Black-Scholes

- Never appropriate for longer duration guarantees in more complex products

## Page 12
# Real-World vs. Risk-Neutral Probabilities 

Real-world probabilities - used for scenarios that lead to best-estimate (expected value) of future cash flows

- Examples or real world probabilities: estimates of volatility and interest rates

Risk-neutral probabilities - used for scenarios lead to a market-consistent current value of an asset or liability

- Actively traded options are usually valued on a market-consistent basis

The CFO Forum's original EEV principles do not require valuing TVOG on market-consistent basis, but the practice appears to be evolving toward market-consistent

- Called market-consistent EV (MCEV)

When valuing TVOG on a market-consistent basis, the actuary should properly reflect the cost of guarantees in the cost of capital and RDR

See MCEV appendix material at the very end for more details

## Analysis of Movement

Analysis of movement - reconciliation between the opening and closing EV that allocates the total change into various categories such as:

1. Contribution from new business
2. Contribution from in-force business
3. Contribution from free surplus
4. Capital movements
5. Other (e.g. foreign currency exchanges)

Commonly, the IBV movement is analyzed first, then the effect of changes in ANW (capital movements) is layered on later

## Page 13
# IBV Movement Analysis: 

|  |  | IBV | NI |
| :--: | :--: | :--: | :--: |
| (1) | Opening IBV | \#\#\# |  |
| (2) | $\pm$ Model refinements and error corrections | \#\#\# |  |
| (3) | = Revised opening IBV | \#\#\# |  |
| (4) | $\pm$ Expected new business contribution | \#\#\# | \#\#\# |
| (5) | $\pm$ Expected in-force contribution | \#\#\# | \#\#\# |
| (6) | = Target IBV and NI | \#\#\# | \#\#\# |
| (7) | $\pm$ Experience gains/losses to IBV and NI | \#\#\# | \#\#\# |
| (8) | $\pm$ Changes in valuation basis and/or assumptions | \#\#\# |  |
| (9) | $\pm$ Other IBV changes and NI | \#\#\# | \#\#\# |
| (10) | = Closing IBV and NI | \#\#\# | \#\#\# |

The above table mirrors the presentation format in the reading. The "\#\#\#" indicate that numbers go in those cells. Basically, there are two items being rolled forward: IBV and stat net income (NI). More explanation in the material below.

Each number in the outline below ties to the number in the table above for reference. I've included this numbering more as a practical thing so you can refer back and forth, but it's important to understand that there doesn't have to be exactly 10 lines. There could be more or less depending on how much detail a company wants to present.

The video lesson demonstrates how to populate this table numerically with both a basic and more advanced example.

## Explanations of Each Movement Item

All formulas below assume zero debt (consistent with the authors' presentation), but they could be adjusted to assume debt as shown earlier on p. D-6 of the detailed study manual

## 1. Opening IBV

- Represents the IBV at the close of the prior reporting period


## 2. Model refinements and error corrections

- Represents changes made after the IBV was "reported"


## 3. Revised opening IBV

- Represents the IBV at the close of the prior period reflecting refinements and corrections (essentially the revised starting point for the current movement analysis)


## 4. Expected new business contribution (VNB)

- VNB can be based on beginning of period assumptions, assumptions at the point of sale, or end of period assumptions (any could be used)

1) Beginning of period (BOP) - consistent with business plans that set VNB targets
2) Point of sale - the most theoretically accurate but are difficult to reflect in the movement because they usually don't match opening or closing assumptions

## Page 14
3) End of period (EOP) - most consistent with external reporting since the assumptions match those in the final total IBV

- In the authors' formulas, they assume BOP assumptions in the VNB calculation, assume that all NB is written mid-year, and ignore any cost of capital associated with NB

$$
\begin{aligned}
{ }_{\mathrm{NB}} \mathrm{EIBV}_{t} & =\mathrm{IBV} \text { of } \mathrm{NB} \text { expected at } \mathrm{EOP} \\
& =\mathrm{VNB}_{t} \times(1+\mathrm{RDR})^{0.5}-{ }_{\mathrm{NB}} \mathrm{BP}_{t} \\
{ }_{\mathrm{NB}} \mathrm{ENI}_{t} & =\text { expected NB book profit (i.e. net income from NB) } \\
& ={ }_{\mathrm{NB}} \mathrm{BP}_{t} \\
{ }_{\mathrm{NB}} \mathrm{EC}_{t} & =\text { total contribution expected from NB } \\
& ={ }_{\mathrm{NB}} \mathrm{EIBV}_{t}+{ }_{\mathrm{NB}} \mathrm{ENI}_{t} \\
& =\mathrm{VNB}_{t} \times(1+\mathrm{RDR})^{0.5}
\end{aligned}
$$

In other words (assuming annual reporting):

- EIBV is the VNB expected by EOY right after the EOY BP occurs (and hence reflects the expected IBV for future BPs generated by the NB beyond year $t$ )
- EIBV is the expected portion of total IBV (in-force and all) at the current reporting date that exists because NB was sold since the prior reporting date
- EC is the impact on total EV from selling NB because it still includes the first BP, which will affect the company's ANW
- If EC $>0$ it means that by selling NB the company increased it's total EV
- Keep in mind that EC could very well be negative because it "contains" the first year BP, which is likely to be a loss for NB. If the first year BP is very negative, it could more than offset any positive IBV for future BPs. In other words, selling NB could increase IBV but lower ANW more.


# 5. Expected in-force contribution

## Page 15
Reflects the unwinding of IBV between the previous close and current date

$$
\begin{aligned}
{ }_{\mathrm{IF}} \mathrm{EIBV}_{t} & =\text { In-force IBV expected at EOP } \\
& =\mathrm{IBV}_{t-1} \times(1+\mathrm{RDR})-\mathrm{IF} \mathrm{BP}_{t}+\underbrace{(\mathrm{RDR}-i) \times R C_{t-1}}_{\mathrm{CoC}_{t}} \\
& =\text { previous IBV with "interest" right after the BP and CoC "drop off" at EOY } \\
{ }_{\mathrm{IF}} \mathrm{ExIncrIBV}_{t} & =\text { expected change in IBV from } t-1 \text { to } t \\
& ={ }_{\mathrm{IF}} \mathrm{EIBV}_{t}-\mathrm{IBV}_{t-1} \\
& =\mathrm{IBV}_{t-1} \times \mathrm{RDR}-{ }_{\mathrm{IF}} \mathrm{BP}_{t}+\mathrm{CoC}_{t} \\
{ }_{\mathrm{IF}} \mathrm{ENI}_{t} & =\text { expected net income from in-force at end of period } \\
& ={ }_{\mathrm{IF}} \mathrm{BP}_{t}+i \times \mathrm{RC}_{t-1} \\
{ }_{\mathrm{IF}} \mathrm{EC}_{t} & =\text { total time } t \mathrm{EV} \text { contribution expected from the in-force that existed at } t-1 \\
& ={ }_{\mathrm{IF}} \mathrm{ENI}_{t}+{ }_{\mathrm{IF}} \mathrm{ExIncrIBV}_{t} \\
& =\mathrm{RDR} \times\left(\mathrm{IBV}_{t-1}+\mathrm{RC}_{t-1}\right) \\
& =\mathrm{RDR} \times \mathrm{PVDE}_{t-1}
\end{aligned}
$$

In other words, we expect the total increase in EV from PVDE $_{t-1}$ to equal the RDR "interest" ignoring actual experience and any other adjustments in assumptions, etc. These other items are reflected separately. We are just trying to develop a target against which we can compare actual EV.

# 6. Target IBV 

- Represents the total expected IBV for the current reporting date

$$
\operatorname{TargIBV}_{t}={ }_{\mathrm{IF}} \mathrm{EIBV}_{t}+{ }_{\mathrm{NB}} \mathrm{EIBV}_{t}
$$

- The valuation model should be able to reproduce TargIBV using BOP assumptions for both NB and in-force (at least if you are using BOP assumptions like the authors)
- Target net income (target BP):

$$
\operatorname{TargNI}_{t}={ }_{\mathrm{NB}} \mathrm{BP}_{t}+{ }_{\mathrm{IF}} \mathrm{BP}_{t}+i \times \mathrm{RC}_{t-1}
$$

7. Experience gains/losses

- Experience gains and losses can be separated into economic vs. non-economic
- Non-economic experience (e.g. expenses) is considered "controllable" by management, so it's useful to look at it separately from the effects of economic factors like interest rate changes, which are beyond management's control
- Difficulties: not easy to accurately attribute all changes, and each "line" requires an additional model run
- Main goal: produce report lines that provide management with actionable information

## Page 16
- Approaches for dealing with assumption interaction

Certain assumptions interact in the model-you'll get different IBVs when updating assumptions separately vs. together
1.) Independent assumption approach with model resets

- Replace a particular modeled assumption in the target valuation model with corresponding actual experience
- Difference between target IBV and IBV based on the replaced assumption is attributed to that particular assumption
- Reset the previous assumption back to the original expected, then set a different assumption to actual and capture the IBV impact
- Problem: original target IBV + all of the incremental changes most likely will not equal a recomputed IBV based on all actual experience because of assumption interactions
- Must include residual change in IBV as a balancing item

2.) Stepwise approach: update assumptions without model resets

- Like approach 1 but don't reset assumptions back to expected after quantifying each IBV change
- For example, if you quantify mortality first, then lapse, you would leave the actual mortality assumption in the model when moving on to lapse
- Allows for effects of assumption interaction (even though some of the lapse change is technically attributable to lapse-mortality interaction, for example)
- Since there are too many model assumptions to quantify individually, usually just focus on critical assumptions, then a final run with all updated
- The final run's IBV change should not be too large-or else there are probably individual assumptions that should have been analyzed

8. Changes in valuation basis and/or assumptions

- Changes in valuation basis and cost of capital basis
- Usually not a factor in the U.S. since statutory valuation bases aren't changed often
- More significant in Canada or other jurisdictions where reserve assumptions are routinely unlocked
- If applicable, often shown as a separate line
- Changes in Prospective Assumptions
- Reflects the change in IBV resulting from changes to future EV assumptions
- Typically focus on the same assumptions broken out separately in the experience gains/losses section

## Page 17
- Can use the same independent or stepwise approach to quantify assumption changes
- Changes to the RDR are usually shown separately and shown last (do all runs at previous RDR, then switch to new RDR and quantify IBV change)

9. Other

- Any other item that impacted the change in IBV
- Example: impact of changing foreign exchange rates

10. Closing IBV

- The final IBV at the current reporting date reflecting all current assumptions
- This would be the opening IBV for the movement analysis next period


# Contribution from Free Surplus (FS) 

$\mathrm{FS}=$ residual component of ANW that is not required to support in-force business
Expected return on FS = the after-tax market rate of return on supporting assets

$$
{ }_{\mathrm{FS}} \mathrm{EC}_{t}=\mathrm{FS}_{t-1} \times i_{t}
$$

FS is also adjusted to reflect capital movements (cash paid in/out of FS to shareholders)

## Aggregate Contribution

Can perform a less detailed higher-level analysis at the aggregate company level
After adjusting ANW to remove impact of any investor cash flows in/out of ANW during the period, the aggregate contribution to EV is:

$$
\mathrm{AC}_{t}=\left(\mathrm{AdjANW}_{t}-\mathrm{ANW}_{t-1}\right)+\left(\mathrm{IBV}_{t}-\mathrm{IBV}_{t-1}\right)
$$

For example, if shareholders pay 1 million into surplus during the year, AdjANW $=$ Actual EOY ANW - interest-adjusted value of the 1 million. Main idea: don't let external cash flows distort the EV change since you're trying to assess how the business performed.

Can also break ANW into RC and the residual FS (AdjFS):

$$
\begin{aligned}
\mathrm{AC}_{t} & =\left(\mathrm{AdjFS}_{t}-\mathrm{FS}_{t-1}\right)+\left[\left(\mathrm{IBV}_{t}+\mathrm{RC}_{t}\right)-\left(\mathrm{IBV}_{t-1}+\mathrm{RC}_{t-1}\right)\right] \\
& =\left(\mathrm{AdjFS}_{t}-\mathrm{FS}_{t-1}\right)+\left(\mathrm{PVDE}_{t}-\mathrm{PVDE}_{t-1}\right)
\end{aligned}
$$

If no capital cash flows occurred in the period, the expected total change in EV from both IBV and ANW is:

$$
\mathrm{EC}_{t}=\underbrace{\mathrm{VNB}_{t} \times(1+\mathrm{RDR})^{0.5}}_{\mathrm{NB}}+\underbrace{\mathrm{PVDE}_{t-1} \times \mathrm{RDR}}_{\mathrm{IF}}+\underbrace{\mathrm{FS} \times i_{t}}_{\mathrm{FS}}
$$

## Page 18
# Effective EV Rate 

The following is sometimes used to measure value added:

$$
\frac{\text { Increase in EV Adjusted for Investor Cash Flows }}{\text { Opening EV }}
$$

Problem: VNB can be a major component of value added, distorting this measure
Effective EV rate $=$ alternative metric that removes what might be a disproportionate contribution from new business

$$
\text { EffEVRate }_{t}=\frac{\left(\text { AdjANW }_{t}-\text { ANW }_{t-1}\right)+\left(\text { IBV }_{t}-\text { IBV }_{t-1}\right)-\text { VNB }_{t}}{\text { IBV }_{t-1}+\text { ANW }_{t-1}+0.5 \times \text { VNB }_{t}}
$$

The effective EV rate can be compared to the RDR

- If EffEVRate $<$ RDR, it means actual EV was below expected (below target) $\Rightarrow$ the combined effect of experience variations and assumption changes lowered EV
- If EffEVRate $>$ RDR, it means the opposite $\Rightarrow$ experience gains and/or assumption changes raised EV above expected

The effective EV rate should be based on end of period assumptions

- This may mean updating VNB, etc. to reflect any assumption changes in the final IBV


## Disclosure

## Criticisms of EV

- Susceptible to manipulation-based on assumptions or methods that outside observers do not fully understand
- Not useful for comparing performance across different companies since assumptions and methods differ
- Comparing EV over time within a company is also problematic if the observer doesn't understand all changes

Because of the above criticisms, adequate disclosure is an important part of EV reporting
EV information related to an individual company found can be found in the company's annual report-if company calculates EV and chooses to disclose the results

Types of EV information available (quality and detail varies company to company):

- Basics elements of EV: IBV, VNB, ANW, etc.
- Analysis of movement: allows reader to understand the EV profits arising from various sources and the causes for the changes in EV over time
- Sensitivity test results for critical assumptions

## Page 19
- Items that have the most impact on EV are the most important to disclose
- Items involving substantial subjectivity are also important to disclose

The CFO Forum's 2006 European Embedded Value Principles paper provides disclosure guidance regarding:

1. Key assumptions
2. How key assumptions were determined
3. Methodologies
4. Reconciliation of opening to closing EV by source
5. Analysis of change in free surplus
6. Sensitivities to key assumptions

Additional guidance in the 2006 paper:

- List of prescribed sensitivities
- 100 basis point increase in the risk discount rate
- 100 basis point reduction in the interest rate environment
- $10 \%$ decrease in equity or property values
- 100 basis point increase in yield on equities or property
- $10 \%$ decrease in maintenance expenses
- $10 \%$ decrease in lapse rates
- $5 \%$ decrease in mortality and morbidity rates
- Basis for determining required capital for cost of capital calculations
- Derivation of risk margins
- Pattern of reinvestment yields

Other EV guidance:

- UK: follow CFO Forum requirements
- Canada:
- OSFI does not provide any guidance
- The CIA published a draft paper in 2000 similar to the CFO Forum, but at a less detailed level
- US: no formal guidance

Even with guidance, disclosure practices of companies continue to be criticized for lack of clarity and completeness

## Page 20
- Variability in the level of disclosure provided around various key assumptions and methodologies
- Some feel that companies provide enough to claim compliance with CFO Forum guidelines, but without details that are necessary for a full understanding of their methods and assumptions


# Appendix: Market-Consistent Embedded Value 

CFO Forum published a Market Consistent Embedded Value Principles paper in 2008

## MCEV improvements over EV:

1. Measurement basis is more consistent with the fair value basis on which assets and many financial liabilities are prices and valued
2. Improves consistency of measurement across companies by removing most of the subjectivity previously reflected in a company's financial assumptions

## "Simplifications" of MCEV compared to traditional EV:

- Eliminates cost of capital associated with hedgeable risk because RDR and pre-tax investment returns are risk-free rates
- Cost of capital for non-hedgeable risks is based on an economic capital approach
- The TVOG calculation removes subjectivity since it uses market-consistent assumptions


## MCEV Challenges:

- Analysis of movement of MCEV can be significantly more complicated
- Requires tracking movements of the fair values of assets and liabilities

Group MCEV - brings non-covered business within MCEV umbrella

- Non-covered business based on an "unadjusted asset value" under IFRS

## Page 21
# II A201-801: Diversification of Longevity and Mortality Risk 

Source Author: Stuart Silverman and Dan Theodore (March 2016)

## Overview of This Reading

This paper highlights the value of using a stochastic mortality model to assess the degree to which mortality risk on a term life product offsets with the longevity risk of a life annuity product

There are a number of tables that appear in the study note, and I recommend reviewing those as you work through the detailed study manual. The video lesson offers some additional perspectives using charts and graphs that pull together key points from various tables in the reading. I think those additional perspectives will be critical in helping you retain the testable points for this paper-which are fairly straightforward if you just line up the numbers in a more simplified fashion! :)

## Key topics for the exam include:

- Understand the basic theory that changes in mortality should have opposite effects on term life insurance and life annuities
- Sources of mortality volatility
- How to quantify the cost of mortality volatility
- How to assess the appropriateness of deterministic margins using stochastic analysis
- How changes in business mix impact the results


## Correlation of Mortality Improvement

Most actuaries believe there is a natural hedge between life insurance mortality risk and payout annuity longevity risk

- For example, higher-than-expected mortality will hurt term life products but help payout annuities


## The question is: to what does the risk offset?

The authors found that appears to be some correlation in the mortality improvement between a typical term life insured and a typical payout annuitant

- The authors looked at historical mortality improvement at age 35 vs. age 75 for both males and females
- Age $35=$ typical term insured age and age $75=$ typical payout annuitant age
- Using annual data:
- Correlation of male term and payout mortality improvement $\approx 2 \%$
- Correlation of female term and payout mortality improvement $\approx 25 \%$
- Using 5-year average to reduce noise:
- Correlation of male term and payout mortality improvement $\approx 26 \%$

## Page 22
- Correlation of female term and payout mortality improvement $\approx 60 \%$
- Key takeaway: there appears to be some correlation (hence opportunity for a hedge), but it's not $100 \%$


# Case Study 

## Hypothetical Products Analyzed

1. Level premium term life insurance

- \$1 billion face with $\$ 3.3 \mathrm{M}$ first year premium
- 10-, 20-, and 30-year level terms considered
- Split male (75\%) / female (25\%)

2. Single premium immediate annuity (SPIA)

- Life only
- Males ages 65, 75, and 85
- $\$ 5.4$ single premium
- $\$ 0.5 \mathrm{M}$ annualized payments

The products were each designed to produce an IRR of $9 \%$ based on distributable earnings
Factors affecting profits other than mortality were ignored (differences lapse risk, differing durations, etc.)

The SPIA in-force was smaller than the term in-force (common for typical insurers)

- Most life insurers have more mortality risk than longevity risk


## Are Deterministic Margins Appropriate in Aggregate?

Many insurers apply assumption margins as a scalar to a best estimate
For example:

- Term: increase mortality by $5 \%$ and decrease improvement by $0.50 \%$
- SPIA: decrease mortality by $5 \%$ and increase improvement by $0.50 \%$

Problem: if these assumptions are used simultaneously, it will overstate aggregate risk (doesn't reflect diversification)

- In other words, it's not likely that term mortality would be $5 \%$ higher at the same time SPIA mortality is $5 \%$ lower

The authors found that the term IRR falls from $9.00 \%$ to $6.89 \%$, and the SPIA IRR falls from $9.00 \%$ to $5.36 \%$ when using fixed margins

## Page 23
- The combined IRR was $6.89 \%$ with fixed margins


# Impact of Mortality Volatility 

To reflect mortality volatility, the authors developed a stochastic mortality model based on 3 aspects of mortality risk:

1. Trend risk - uncertainty in future mortality improvement

- Mortality improvement does not follow smooth/predictable trends
- Affected by both long-term waves and random annual fluctuations
- 3 factors affecting trend risk:

1.) Long-term trends (10-years)

- Driven by changes in medical practice/research, society, economy, politics, and the environment

2.) Annual volatility

- Drivers: Extreme weather, disease, and variations in reporting

3.) Correlation between long-term and annual trend volatility
4. Basis risk - uncertainty in the assumed mortality level

- Reflects the risk that a given insurers' mortality experience isn't 100\% of industry experience ${ }^{1}$
- Was modeled independently for the term and SPIA products since sales/underwriting approaches are likely different for those products
- Basis risk is lower for insurers with higher certainty in their best estimate assumption

3. Long-term underwriting risk - uncertainty in how long it takes for underwriting effects to wear off (i.e. transition from select to ultimate mortality)

- Modeled by looking at 3 independent variables:
(a) Uncertainty around initial select period length
(b) Length of grading off period for preferred or substandard mortality
(c) Ultimate mortality level after underwriting has completely worn off

The authors note 2 other sources of mortality volatility that they did not consider:

[^0]
[^0]:    ${ }^{1}$ Unfortunately the term "basis risk" gets used very loosely from reading to reading, and you may see it refer to other risks on the syllabus that have nothing to do with mortality risk. What the authors call "basis risk" in this paper is essentially the risk that the best estimate mortality assumption is wrong. In practice, each insurer will likely apply a different ratio of industry experience, but each insurer will have different levels of certainty based on their own experience. Since the authors are doing their study from an industry perspective, they are using a multiple of $100 \%$, but allowing for deviations around that. On other ILA syllabi or in other literature, you may have seen this risk referred to as "volatility around the best estimate" or "level risk."

## Page 24
1. Extreme long-term events (e.g. medical breakthroughs or drug-resistant bacteria that have long-term effects on mortality)
2. Catastrophic short-term events (pandemics, terrorism, etc.)

# Cost of Volatility 

The IRR falls from $9.00 \%$ to $8.72 \%$ for SPIA and $8.86 \%$ for term if mortality is modeled stochastically

- Reason: "asymmetric dispersion" in the tails (i.e. the bad tail is worse than the good tail)
- For payout annuitants, there is a limit on premature death, but annuitants could survive a very long time
- For term insureds, the cost of premature death is greater than premium and investment income gains from surviving

Insurers who do not model mortality stochastically will underprice the products (i.e. not be compensated for the cost of volatility)

## Stochastic Projections of Mortality and Longevity

The authors performed a stochastic simulation involving 1000 scenarios and calculated the PV of distributable earnings and IRRs at various percentiles for both the term and SPIA products

The distribution of results is helpful for understanding how conservative the deterministic fixed margins are in each product

- The $6.95 \%$ term deterministic IRR with fixed margins falls between the 95th and 99th percentile result
- The 5.36\% SPIA deterministic IRR with fixed margins falls between the 90th and 95th percentile result


## Savings From Diversification

Diversification Savings $=$ Combined PVDE - (Standalone Term PVDE + Standalone SPIA PVDE)

The authors found that the savings from diversification increases as you approach the tail

- At the 50th percentile, the savings $\approx 0$
- At the 75 th percentile at nigher, the savings are positive at all discount rates
- At the 99th (worst) percentile, the savings are substantial
- Using an $8 \%$ discount rate, the combined PVDE is 102 K higher (about $11 \%$ higher than the sum of the standalone PVDEs)

The combined IRR is also higher than either of the standalone IRRs at higher percentiles

## Page 25
- The combined IRR tracks pretty closely to the term life IRR at most percentiles ${ }^{2}$
- However, at the 99th percentile, the combined IRR is $6.33 \%$ compared to $-1.59 \%$ and $6.26 \%$ for SPIA and term, respectively


# Fixed Margin vs. Stochastic Modeling 

The $6.89 \%$ IRR based on the combined deterministic results with fixed margins falls between the 95th and 99th percentile of the combined stochastic results

- This suggests that the combined deterministic results with fixed margins are overly conservative if the insurer's risk appetite is at a lower percentile ${ }^{3}$

Stochastic analysis would allow an insurer to revise its deterministic margins so that the resulting IRR better aligns with the insurer's risk appetite based on the stochastic results

- In other words, lower the margins to increase the combined IRR to the level desired (and also increase the combined PVDE)
- The authors solved for new fixed margins that increased the deterministic IRR to $7.55 \%$, which corresponds to the 90th percentile of the stochastic results

If the insurer is able to lower margins to reflect mortality/longevity diversification, the insurer can offer more competitive products

## Managing Business Mix Reflecting Desired Risk Tolerance

In this section, the authors look at different mixes of term and SPIA business
An insurer might be interested to know how much of each product it should target for the mortality/longevity hedge

- Requires stochastic analysis because the deterministic results can't show how the diversification benefit changes as the business mix changes
- Deterministic analysis will show more aggregate cost as the proportion of SPIAs increases (because SPIAs are less profitable than term on a standalone basis)

Overall return $=$ weighted average of term and SPIA returns
The authors found that there is very little difference in IRRs at all percentiles if the SPIA volume is increased $5 x$

However, if SPIAs are increased 10x, IRRs fall at all percentiles

[^0]
[^0]:    ${ }^{2}$ This is probably because there is much more term being modeled than SPIA
    ${ }^{3}$ This is may seem confusing without looking at the tables closely, but the authors are just reinforcing the point that the combined deterministic results don't properly reflect diversification because the combined IRR should fall relative to the position of the standalone IRRs.

## Page 26
Key takeaway: an insurer can increase its SPIA in-force up to a threshold (5x) before IRRs deteriorate and margins have to be recalibrated ${ }^{4}$

# Impact of Business Mix on Diversification Savings 

I was surprised that the authors do not talk at all about how the diversification savings changes as the business mix changes. Given that they originally set out to determine the extent of the mortality/longevity hedge, this seems worth exploring, so I wanted to add a little more detail here. We can draw some interesting conclusions by comparing numbers across several tables.

For example, at the 99th percentile (where the savings are the most pronounced), we can see that the PVDE savings increase as the SPIA proportion increases:

|  | Combined | SPIA | Term | Savings | Savings \% |
| :-- | --: | --: | --: | --: | :--: |
| Baseline | $-826,082$ | $-111,106$ | $-817,206$ | 102,230 | $11 \%$ |
| 5x SPIA | $-945,061$ | $-555,530$ | $-817,206$ | 427,675 | $31 \%$ |
| 10x SPIA | $-1,204,147$ | $-1,111,060$ | $-817,206$ | 724,119 | $38 \%$ |

All of the results above are based on the $8 \%$ discount rate. The baseline result is the same result mentioned in the "Savings From Diversification" section and can also be found in Figure 22. The combined results come from Figures 23 and 24.

The authors do not show the $5 x$ and $10 x$ standalone SPIA results at the 99th percentile, but we can easily calculate those by simply scaling the baseline results by a factor of 5 and 10, respectively. ${ }^{5}$ The term volume was held constant, so it is the same in each case.

Key takeaway: As more SPIAs are sold relative to term business, the diversification savings increases. At the 10x level, combined results are $38 \%$ higher than the sum of the standalone results. I'm sure there is some threshold where the savings begins decline, but we don't have enough information to solve for that point. At any rate, being able to reduce tail risk by $38 \%$ seems like a very substantial benefit.

See the video lesson for more numerical perspectives on the authors' results that tie this result in with the IRR results discussed previously.

[^0]
[^0]:    ${ }^{4}$ There seems to be a typo on p. 11 where the authors state that " $\ldots$. the fixed margin that was solved for to approximate the effect of the 90th percentile scenario under the original mix of life insurance and annuity business produces a result that is now between the 90th and 95th percentiles. . " They're referring to the $7.55 \%$ IRR mentioned in the previous section. This IRR actually falls between the 75 th and 90 th percentiles under the $10 \times$ SPIA results. This suggests the insurer would need to increase deterministic margins to stay at the 90th percentile if the SPIA proportion is increased.
    5 You can verify this in Figure 20, which shows the best estimate deterministic results at the $5 x$ and $10 x$ levels. The $5 x$ and $10 x$ SPIA results are just multiples of the $1 x$ run.

## Page 27
# II A201-100: Diversification 

Source Author: CFO Forum (October 2013)

## Pages 1-18 Only

## Overview of This Reading

The full title of this paper is "Diversification: Considerations On Modelling Aspects and Related Fungibility and Transferability"

However, the topics of "fungibility and transferability," while getting a brief mention in the Executive Summary, are covered in pages beyond page 18, so they are generally not covered on the syllabus

The testable page range of this paper primarily focuses methods and considerations for modeling risk dependencies and diversification

## Key topics for the exam include:

- Model capabilities
- Structure (top-down vs. bottom-up, one-level vs. multi-level)
- Dependence (tail behavior)
- Aggregation methodologies (linear, copula, and others)
- Correlations, calibration, and parameterization
- Key conclusions and observations


## Executive Summary

Context: Policy responses to the financial crisis (e.g. higher loss absorbency, recovery and resolution) have raised questions about insurers' ability to measure and recognize diversification and its effects

Purpose: This paper supplements the CRO Forum's 2005 paper "A Framework for incorporating diversification in the solvency assessment of insurers"

- Provides additional analysis on practical considerations
- Considers the context of wider developments like ORSA, stress testing, and risk appetites


## Intentions:

- Provide a basis for companies to evaluate and justify their treatment of diversification within their modelling
- Assist communication with supervisors regarding approaches for modelling diversification benefits
- Enable greater understanding of the effects of diversification

## Page 28
- Improved cooperation to promote recognition of diversification in regulatory solvency assessments


# Key Contents of the Paper: 

- Modelling Approach: factors affecting diversification modelling
- Five Principles for Setting Model Correlations, Calibrations, and Parameterization:

1. Expert Judgement should be utilized and documented
2. Parameterization should use as much relevant data as practicable
3. Estimation of dependency relationships should account for tail behavior
4. Material dependencies should be identified and their capital impact explained
5. Model Users should understand how diversification assumptions impact outcomes

- Fungibility and Transferability: Clear distinction between the two, how fungibility can be demonstrated for economic capital models, and that transferability is relevant for liquidity assessment ${ }^{6}$
- Challenges to Fungibility: legal structure, asset recognition, intra-group arrangements, partial holdings, and policy/shareholder restrictions
- Regulatory Context: Assessment of how different regulatory developments inform the recognition of diversification benefits and promote a flexible approach


## Overall Message:

- Diversification is central to insurance business and risk management
- Recognizing diversification benefits in regulatory solvency assessment is key to policyholder protection and financial stability


## Introduction to Diversification

## Diversification is central to insurance business

- In finance, diversification means reducing risk by investing in a variety of assets
- For European insurers, it involves "diluting" (mitigating) ALM exposure with insurance, financial, and operational risks


## Insurers manage risk by pursuing diversifying strategies:

- Pooling similar and sufficiently independent risks (e.g. over time)

[^0]
[^0]:    ${ }^{6}$ As noted earlier, these topics only get a brief mention in the Executive Summary and are covered in more detail on pages outside the syllabus page range. Fungibility refers to the ability of capital to be used to absorb losses or meet capital requirements in any part of the insurance group where it's needed. In other words, it's not earmarked or restricted to a specific purpose/entity. Transferability refers to the company's ability to physically move or make available capital from one entity to another within the group.

## Page 29
- Pooling dissimilar risks (diversity of products, market segments, geographies)
- Combining opposite risks for internal hedges (e.g. policies reacting differently to interest rate changes)
- Limiting risk concentrations
- Limiting underwriting to specific risks
- Using risk mitigation like reinsurance, hedging, securitization

Aim of diversifying strategies: Reduce aggregate exposure to a single source by exposing the portfolio to areas that react differently to the same event

Not all risk can be diversified away: Insurers use risk mitigation strategies (e.g. reducing concentration, hedging, reinsurance) to improve resilience

# Model Capabilities 

Clarity around model structure helps provide understanding and confidence in model output

## Model Structure: Factors Impacting Diversification Quantification

- Level of granularity at which risks are defined
- Finer granularity (e.g. larger variance-covararince matrix) leads to:
* Lower diversification within a risk category
* Greater diversification between categories
- Increasing risk factors usually leads to increasing overall diversification
- Granularity should reflect the nature of the insurer's risk profile
* Use less granular approach for less material risks
- Impacts how models capture interaction between asset/liability payoffs due to combined risk drivers
* E.g. interactions between interest rate risk and mortality/lapse
- Approach to risk aggregation (top-down vs. bottom-up)
- Risk drivers are grouped into sub-risk groups
* E.g. mortality risk is a sub-risk of life insurance risk
- Top-Down Aggregation Approach
* First, measure broad categories of risk (market risk, operational risk, life risk, etc.)
* Combine high-level risk categories distribute using a specific risk aggregation model
* Example: The Solvency II standard formula

## Page 30
# - Bottom-Up Aggregation Approach 

* Begin with the most detailed, granular individual risk drivers within each category
* Simulate the individual risk drivers jointly and aggregate to calculate capital at higher levels (e.g., company or group)
* Key Feature: Always begins at a very detailed, granular level
- Often a combination of both approaches is used in practice
- Both require a common time horizon for risk measurement
- Key difference: Top-down specifies broad correlations between sub-risks; bottom-up requires specification of all underlying risk drivers


## - Top-down advantages:

* More intuitive
* Limits number of dependencies to estimate
* Facilitates step-wise calculation
* Easier to make correlation matrix consistent (PSD)


## - Top-down disadvantages:

* Correct top-level correlations depend on exposure to risk factors
* More approximate
* Can lead to inconsistencies
* Less conducive to granular decision-making
* Limited for direct interactions between sub-risks
- Insurers' internal models often use a bottom-up approach with a combined correlation matrix for all risk types
- The quantum of diversification resulting from the model should not be used to assess the model's quality ${ }^{7}$


## - Levels of aggregation (multi-level vs one-level approach)

- Filipovic's paper ${ }^{8}$ compares Solvency II Standard Formula's 2-level aggregation to a global correlation matrix approach ${ }^{9}$
- Filipovic's conclusions:

[^0]
[^0]:    7 In other words, the true quality of an internal model is not assessed by the numerical output of diversification, but by the rigor, transparency, appropriateness, etc. of the model itself.
    8 This is a paper the source reading cites.
    9 2-level means intra- then inter-risk modules.

## Page 31
* 2-level aggregation using a common market correlation generally can't reproduce true bottom-up aggregation because "inter-module" correlation matrices are entity-specific
* A minimal, implied company-specific correlation matrix can be derived
- Allows going from multi-level to one-level aggregation and serves as a benchmark ${ }^{10}$
- Demodularization approach helps identify key dependent risk pairs


# - Dimensions of diversification 

- Intra-risk aggregation: Across exposures within an individual risk type (e.g. market risk)
- Inter-risk aggregation: Across individual risk types (e.g. life risk and market risk)
- Aggregation across portfolios: Simultaneous application of methodology to all portfolios within an entity
- Aggregation across entities: Consolidated measure across entities within groups


## Modelling Dependence

Two main components in risk modelling: marginal risk distribution and dependency structure
Distinction between dependency and correlation: Linear correlation is a special case of dependency, quantifying only a linear relationship

- Linear correlation is popular due to its tractability with elliptic distributions in variancecovariance matrices

Limitation: Many financial risks are not adequately described by elliptic distributions ${ }^{11}$

- Financial risks may have skewness or heavy tails
- Relying solely on constant linear correlations can be misleading
- Doesn't capture how the dependency structure can change drastically under stress (e.g. higher implied correlations in stressed markets)
- This drawback can be addressed by calibrating correlation to incorporate tail behavior

Methods to analyze tail behavior:

- Adverse quadrant correlation: Linear correlation calculated only for observations in the "adverse quadrant" (bad tail)
- Adverse period correlation: Linear correlation calculated only for observations within a historical period of adverse market conditions

[^0]
[^0]:    ${ }^{10}$ Being able to transform from a multi-level aggregation approach to a one-level aggregation approach is important because it provides a theoretical bridge between different model structures such as the Solvency II Standard Formula and internal models. This facilitates comparisons.
    ${ }^{11}$ The normal (Gaussian) distribution is a common example of an elliptic distribution.

## Page 32
- Rolling correlation: Linear correlation calculated over a fixed-length historical window to highlight periods of higher dependency
- Tail dependency analysis: Mapping process to estimate correlation parameters by comparing simulated Gaussian distributions with empirically observed joint distributions, focusing on tail dependency

Frequency of observations (daily, weekly, monthly) impacts dependency results

- Monthly or quarterly returns can show increased tail dependency for market risk variables

Alternative measures may be more appropriate: copulas, rank correlations, and coefficients of tail dependence

Tail dependence is important for joint extreme values, which are a major concern in risk aggregation

There is no one-size-fits-all solution for incorporating tail dependency; each company must demonstrate how it is addressed

# Risk Aggregation Methodologies 

## Main Approaches:

- Linear aggregation model: Aggregates risk (e.g. VaR, ES) using correlations and individual risk measures
- Copula model: Aggregates risk using a copula for co-dependence and individual risk P\&L simulations; offers greater flexibility


## Comparison of Different Aggregation Methodologies Approaches:

These generally flow from simple to complex

- Simple summation: sum the individual risk amounts
- Advantages:
- Conservative (ignores diversification, produces upper bound)
- No data required
- Easy to communicate
- Disadvantages:
- Ignores diversification benefits
- Assumes all inter-risk correlations are one
- No meaningful risk interactions
- Fixed diversification percentage: do a simple sum, then reduce by a fixed amount (e.g. $20 \%$ reduction)
- Advantages:

## Page 33
- Easy to implement and communicate
- Recognizes some diversification
- Disadvantages:
- Results highly dependent on chosen percentage
- Does not capture non-linearity
- No meaningful interactions or changes in exposures
- Variance-covariance matrix: combine risk amounts using constant correlations
- Advantages:
- Allows for interactions across risk types
- Relatively simple to understand and implement
- Disadvantages:
- Interactions assumed linear and fixed over time
- Must satisfy positive semi-definiteness (PSD)
- Implies elliptically distributed underlying risks (no skewness)
- Correlation factors sensitive to underlying risk distributions
- Overall diversification depends on pairwise correlations
- Copula: a function that combines marginal probability distributions into a joint probability distribution
- Advantages:
- Much more flexible than covariance matrix (allows for skewness, non-linearity, heavy-tailedness)
- Combines marginal probability distributions into joint
- Allows rich interactions
- Disadvantages:
- Requires estimation of distributions for all underlying risk categories
- Demanding computation (Monte Carlo)
- Results subject to parameter estimation uncertainty
- Challenging communication
- Integrated model: underlying risk drivers are modeled together, capturing their interactions and dependencies
- Advantages:
- Identifies and models interactions of common underlying risk drivers

## Page 34
* Calculates outcome distribution/economic capital in a single step
* Appealing and intuitive
* Represents 'real world'
* Captures non-linearity
- Disadvantages:
* Demanding in terms of input and computing power
* Parameterization challenges related to structural risk interactions
* Transparency/communication challenges

Many methods require that their correlation matrices to be positive semi-definite (PSD)

- Various technical methods are used in practice to ensure this


# Correlations, Calibration, and Parameterization 

Challenge: Reliability of diversification quantification, despite its broad acceptance
Model variables are often partially correlated, requiring careful establishment of structures and parameters

Five principles to guide development of credible dependency assumptions:

1. Expert Judgement should be utilized and incorporated in a structured and documented way

- Subject matter experts (SMEs) are an important supplement to any model
- Critical in assessing tail correlation where data is sparse
- Leverages economic relationships to imply risk factor behavior in extreme scenarios
- Relevant for assessing data relevance (e.g. structural historical changes, frequency of returns)
- Can impact granularity and precision of parameters
- Bayesian inference can combine prior information, observations, and expert opinion to reduce parameter uncertainty

2. Parameterization should utilize as much relevant data as practicable

- Dependency levels are difficult to measure accurately; many observations needed
- Historical results alone are unlikely to provide reliable indication of dependency in adverse scenarios or tail correlation
- Product, portfolio, or business circumstances change, rendering older data obsolete
- Useful to benchmark results against similar variables with internal or external data

## Page 35
- Expert judgement is relevant for how structural economic changes impact historical market data relevance

3. Estimation of dependency relationships should take into account tail behavior

- Dependencies can strengthen in volatile/extreme market circumstances (e.g. stock markets globally more correlated in extreme negative scenarios)
- Important to consider behavior in tail events, despite limited observations for such events

4. Material dependencies should be identified and their impact on capital should be appropriately explained

- Sensitivity testing helps identify dependencies with most material impact on capital calculations
- Materiality guides modelling and validation efforts
- Explanation should consider main drivers of dependencies
- Benefits of understanding explicit drivers of dependencies:
- Increases understanding of the causes of dependency
- Enhances credibility of tail correlation
- Back-testing against historical results (e.g. simulated loss ratios) can help verify risk and dependency parameters, though tail information is limited

5. Model users should understand how diversification assumptions impact model outcomes

- Diversification concepts/calculations can be opaque but significantly impact model outcomes and business decisions
- Nature of assumptions and main limitations should be communicated to model users and management
- Sensitivities to key diversification assumptions or measures of uncertainty can aid communication
- Model risk related to key assumptions like diversification benefits should be considered when setting risk tolerance and appetite


# Observations, Key Messages, and Conclusions 

Computed diversification benefits are influenced by many aggregation process factors, complicating understanding

## - Model structure and non-separability

- Risk interactions in different risk categories may not be captured depending on granularity, leading to misestimation of risks or diversification benefits

## Page 36
- Inappropriate classification may hinder risk management and mask important risks
- Level of granularity impacts how diversification is implicitly or explicitly captured
- Influences calculation and management of benefits
- Careful comparison needed between models with different granularity levels (e.g. Solvency II standard formula vs. internal models)
- More granular aggregation typically shows more explicit diversification
- Care needed to recognize tail dependencies to avoid overestimating diversification
- Model structure and level of granularity need to fit the business profile
- More material risks are typically captured more granularly
- Geographical diversification becomes important for international companies
- Dependence modelling
- Inappropriate modelling can result in incorrect diversification benefits, even with reasonable individual capital components
- Important to consider how risks behave in tail events
- Model parameterization
- Difficulties in estimating parameters (e.g. correlation factors) and their evolution over time
- Expert opinion is usually necessary due to lack of data data and material impact on computed benefits
- Modelling and validation efforts need to be driven by materiality
- Focus on most material dependencies for parameterization and validation
- Model comparison and benchmarking to the Standard Formula
- Care needed due to structural differences and limited granularity of SF
- Correlation parameters and diversification benefits may not be directly comparable with internal models


# Conclusions: 

- Diversification ratios are unreliable for inter-company comparison due to different structural approaches
- Diversification should not be a basis for assessing model validity
- Consistent use of confidence levels is needed for assessing risk relationships
- Expert judgement plays an important role regardless of modelling approach or structure

## Page 37
# II A201-101: Life In-Force Management 

Source Author: Swiss Re (June 2017)

## Overview of This Reading

This paper describes various ways insurers can increase the profitability of in-force (existing) business

This paper is written for a European audience, but there are a lot of general takeaways for US and Canadian insurers

This paper basically reduces to an outline of 6 "levers" that insurers can use to increase the profitability of their in-force blocks. I would be able to list all 6 levers as well as detail under each. There is honestly not a lot of depth to this paper, which mentions a lot of topics at a very high level. A number of these topics are covered in greater detail elsewhere on the syllabus, however.

## Key topics for the exam:

- Factors that have strained life insurers' profits
- Know the 6 levers and detail/examples of each:

1. Steering liability portfolios to support strategic ambitions and financial targets

- How to apply a holistic in-force steering framework
- Re-designing products and developing services
- Cross- and up-selling
- Methods for dealing with unprofitable books

2. Improving persistency ( 7 items)
3. Improving claims management (6 items)
4. Adjusting asset management subject to regulatory constraints and risk appetite

- Key challenges that affect life insurers' investment income
- Asset strategies
- Strategies to increase asset yield
- Adapting to new regulatory frameworks

5. Optimizing capital

- Methods for stabilizing cash flows and earnings
- Methods for freeing up trapped capital

6. Increasing operational efficiency (reducing costs)

- Way to modernize the IT landscape
- Possible ways of optimizing operations

## Page 38
# Executive Summary 

Life insurers are increasingly focusing on optimization of in-force business, not just creating new business

Factors that have strained life insurers' profits:

## 1. Low interest rate environment

- Hurts savings-type products, which generate the majority of premium income (85\%) in the global life insurance industry
- Lower fixed income asset returns make it harder to fund guarantees
- A spike in interest rates would also hurt: would trigger high lapses

2. Increased competition - price comparison websites, etc.
3. Increased regulatory pressure to show the true economic cost of insurance (Solvency II, IFRS 17$)^{12}$

In addition to changing product features and re-pricing products, insurers are beginning to use in-force management as a tool for improving profits

This article recommends 6 key areas ("levers") for improving in-force management

## Overview of 6 Levers for Effective In-Force Management

1-3.) Managing liabilities and improving consumer value

1. Steering liability portfolios to support strategic ambitions and financial targets

- Allocate capital to the most attractive products and LOBs

2. Improving persistency by providing a higher value to policyholders

- Product enhancements increase persistency

3. Improving claims management

- Be supportive of policyholders
- Claims demonstrate the value of insurance to insurers' clients
- Improve claims by encouraging healthier lifestyles

4. Adjusting asset management subject to regulatory constraints and the insurer's risk appetite

- Investment income contributes to profit and helps fund claims


## 5. Optimizing capital

- Excessive capital increases economic costs

[^0]
[^0]:    ${ }^{12}$ This paper is written primarily for a European audience, so you'll see various references to Solvency II, which is more of a "market-consistent" economic capital framework for regulatory capital. Solvency II tends to penalize products that have more of an investment-orientation.

## Page 39
- Tools: reinsurance and capital market solutions

6. Increasing operational efficiency (reducing costs) on in-force operations

The remaining sections provide more detail on each lever

# Steering Liability Portfolios 

Involves allocating capital to the most attractive product types and business lines
Liability steering is similar to investment-decision making but more complex, requiring collaboration from multiple areas of the company

## Applying a Holistic In-Force Steering Framework

1. Set financial targets

- Accounting-based indicators: easy to understand but fail to capture long-term nature of business
- Positive cash flows may take years to materialize for traditional life insurance
- Short-term business (e.g. medical reimbursement) and unit-linked ${ }^{13}$ products provide a faster payback
- Economic value (EV) metrics: explicitly recognize relative riskiness and quantify future cash flows and cost of capital

2. Determine constraints

- Capacity limits, capital adequacy, required cash flows, risk appetite

3. Project future market conditions

- Requires assumptions for demand, competition, risk landscape, and regulation
- New technology: Big Data and machine learning
- Research on consumer preferences
- Measurement of consumer behavior
- Surveys on consumer preferences
- Discrete choice experiments can measure unconscious behavioral biases and aid new product development
- New sources of competition: financial services firms, Big Tech, and small niche players

4. Identify opportunities and rank by attractiveness

- Product design, customer retention, cross- and up-selling (organic growth), sale of business, M\&A, portfolio run-off

[^0]
[^0]:    13 "Unit-linked" products are similar to what Americans call "variable" products and what Canadians call "segregated" products.

## Page 40
5. Specify target liability portfolio
6. Manage asset portfolio
7. Optimize capital structure
8. Verify that constraints are met

# Re-Designing Products and Developing Services 

1. Align product strategy to cope with changing market conditions

- Lower or abolish guaranteed benefits
- Align crediting rates with expected investment returns
- Shift interest rate and market risks to policyholders with unit-linked products
- Offer participating whole life (has not been popular)
- Reprice biometric risks (e.g. mortality) because low interest rates prevent sufficient reserves
- Reduce product complexity to appeal to online buyers

2. Prepare for rising interest rates

- When interest rates rises quickly, policyholders may shock lapse to purchase cheaper or more attractive products

3. Develop new services

- Adding more services improves consumer value (e.g. wearables for health monitoring and disease management)
- Will require collaboration with health care and technology providers


## Growing High-Performance Business Through Cross- and Up-Selling

- Cross-selling - selling a new product to an existing customer
- Up-selling - upgrading an existing customer's product
- Benefits:

1. Cross/up-sell when policyholder reports a claim
2. Reduce costs/prices by selecting good risks for cross/up-selling
3. Diversify underwriting risks

- Challenges:
- Fragmented IT systems and silo-ed organizations
- Demographic segmentation may be insufficient to identify consumer preferences

## Page 41
# Dealing With Unprofitable Books 

- Reducing the in-force risk profile
- Reasons costs have gone up: higher capital requirements and low interest rates
- 3 types of solutions (from least to most challenging):

1. Change non-guaranteed elements

* Lower dividends and crediting rates
* Increase fees and premiums

2. Exchange/conversion programs

* Convince policyholders to switch to policies with lower guarantees but higher return potential

3. Buyout programs - buy back unprofitable policies from customers

- Risks of exchange and buyout programs:

1. Adverse selection (anti-selection) - may cause profitable policyholders to lapse and unprofitable ones to persist
2. Reputational risk - policyholders feel pressured to terminate contracts

- Reasons policyholders may no longer want their policy:

1. No longer need income protection
2. Life expectancy has changed
3. Needs have changed

- Options to deal with unprofitable or non-core run-off business

1. Retain and run off to expiry

- Advantages
* Full control and profit retention
* No dependence on external providers
* No external fees
* Keep access to high-value customers
* Keep experience of current team
- Disadvantages
* Different skill set required
* Maintains exposure to future losses/volatility
* Operational inefficiencies due to a shrinking book

## Page 42
- Longest timeframe to liquidate liabilities

2. Outsource to a third-party administrator (TPA)

- Advantages
- TPA may be able to manage the business more efficiently
- Frees up resources
- Good option when business value is high
- Disadvantages
- Exposure to reputational risk (TPA may provide bad service)
- TPA fees may erode profits
- Maintains exposure to future losses/volatility

3. Reinsure with maintained or outsourced administration

- Advantages
- Limits exposure to future losses
- Provides capital relief
- Frees management to focus on the other LOBs
- Disadvantages
- Ceding company usually maintains contractual liability with policyholders
- 2 parties being in control limits full operational/capital synergies
- Introduces counterparty risk
- Policyholder approval required to allow reinsurer to assume all all contractual liabilities ${ }^{14}$
- Few reinsurers can assume all administrative functions

4. Sell block

- Advantages
- Quick and effective way to achieve early exit from business
- Capital can be redeployed to other lines
- Creates operational, capital, and tax efficiencies
- Disadvantages
- Highest up-front losses for the seller
- Might need approval from policyholder or regulator
- Buyer availability may be limited outside the US and UK

[^0]
[^0]:    ${ }^{14}$ They are alluding to assumption reinsurance here

## Page 43
# Increasing Persistency 

- How high lapses hurt insurers:
- Acquiring new customers is 6-7x more costly than retaining an existing one
- Acquisition costs are not recouped
- Anti-selection (healthy lives lapse) can hurt mortality products
- Lower-than-expected ultimate lapses hurt lapse supported products
- Drivers of lapses
- Consumer-specific drivers:
* Needs change (new stage of life)
* Premiums lower on other products
* Lack of interaction between insurer and customer
* Advisors encouraging policy switching
- Market-specific drivers:
* High unemployment, falling income
* Spike in interest rates
- Response levers insurers can use to mitigate lapses
- Premium holidays to help with temporary affordability
- Offer discounts to match better offers
- Offer exchanges or alternative products if needs have changed
- Mitigating lapses on post-level term business
- US insurers have found that more gradual transitions to the ART period can reduce shock lapses
- Helping policyholders avoid negative behavioral biases
- Behavioral economics may shed light on why policyholders lapse
- Some insurers are managing persistency by studying consumers' evolving needs
- Improving lapse predictions with predictive analytics
- Life insurers have been slow to implement advanced data mining and predictive modeling techniques
- Propensity-to-lapse models have been largely unsuccessful to date
- This is a promising area for the future
- Increasing customer engagement

## Page 44
- Traditionally, insurers and customers interact mainly at the point of sale
- "Engaged and healthy customers keep their policies for longer"
- Smartphones, social media, etc. are making it easier to interact with customers
* Can explain why premiums have increased
* Can be used to promote healthier lifestyles


# Improving Claims Management 

An efficient claims management process provides a good experience for customers but also ensures only legit claims are paid

There are 6 levers for improving claims management

1. Increasing process efficiency

- M\&A can lead to fragmented infrastructures
- Avoid silos and poor communication between units
- Automation can increase efficiency

2. Enhancing claims experience

- Best case: easy, effective, timely claims settlement
- Start with a clear explanation of coverage when policy is sold
- Provide clear guidance on how to file claims
- Immediately inform policyholder if claim is not covered
- Offer appeals process for denied claims

3. Improving fraud prevention and detection

- Lowers claim costs and premiums
- Make customers aware of the consequences of fraud
- Putting a fraud notification at the top of a claims form is more effective than at the bottom
- Improve fraud detection with training and predictive modeling

4. Deep-dive on claims analytics

- Actuaries and data scientists could use claims data to enhance predictive modeling capabilities
- Claims analytics is improving in 2 ways:

1.) Easier and cheaper data collection
2.) Advances in predictive modeling and hardware

## Page 45
5. Supporting health recovery and job reintegration

- Employ clinical teams that help rehabilitate LTC/disability claimants
- Case management programs can have disease management and care support elements
- Requires collaboration with employers (e.g. giving employers incentives for successful reintegration)

6. Nudging health-related behaviors

- Examples:
- Text message reminders for appointments, medication, etc.
- Rewards for going to the gym
- Uses of behavioral economics:
- Communicate health advice from healthcare professionals instead of insurers
- Benchmark progress against peers
- Use default options that require consumers to opt out of health programs


# Managing Assets 

## Key Challenges That Affect Life Insurers' Investment Income

- Low interest rates
- Deviations in mortality and lapse experience
- Regulatory changes
- Reinvestment risk


## Asset Strategies Relevant for In-Force Books

1. Improve asset-liability duration match
2. Hedge investment risks with derivatives

## Strategies Insurers Have Used to Find Higher-Yielding Assets

1. Alternative investments (private equity, hedge funds)
2. Less liquid asset classes (real estate, infrastructure, and commercial mortgages)
3. Lower-rated bonds (e.g. BBB corporates)
4. Foreign securities (mainly done by Asia Pacific insurers)

## Adapting to New Regulatory Frameworks

Changes in capital required by regulators requires insurers to reallocate assets

## Page 46
# Optimizing Capital 

## Stabilizing Cash Flows and Earnings

- Transferring mortality and morbidity risks
- Proportional reinsurance (quota share) - can reduce mortality and morbidity risk
- Non-proportional reinsurance - excess-of-loss, stop-loss, etc. can transfer cat risk
- Capital market solutions (e.g. cat bonds) transfer cat risk to investors
* Uses a special purpose vehicle (SPV) to create a reinsurance agreement and issue bonds
* Investors suffer losses if a cat event occurs
- Transferring longevity risk on life annuities
- Indemnity-based reinsurance: ceding company pays fixed premiums to a (re)insurer and receives payments based on actual longevity experience
- Index-based reinsurance: linked to a population index instead of the actual experience of the reinsured block
- Some insurers are willing to accept longevity risk from other insurers to diversify mortality risk
- Transferring lapse risk
- Value-in-force (VIF) solutions - allow insurer to sell/reinsure embedded value (EV) to raise capital and improve solvency ratios
- Non-proportional lapse risk reinsurance - pays the ceding company if lapses are above a threshold


## Freeing Up Trapped Capital

- Efficient reserve financing
- XXX/AXXX excess reserve financing in the US had evolved from coinsurance to "soft" assets like letters of credit and credit-linked notes, then AG 48 put limitations on soft assets
- Principles-based reserves should reduce but not eliminate the need to finance excess reserves
- Increasing available capital and liquidity
- VIF monetizations can increase liquidity and provide capital for other uses
- VIF financing is called "Zinszusatzreserve" in Germany
- Selling a block is also an option

## Page 47
# Increasing Operational Efficiency 

## Modernizing the IT Landscape

- Overhauling the IT core system
- Reduces IT operation costs
- Smart applications can combine multiple data sources to train statistical-learning algorithms to support/replace human processes
- Increasing process automation
- Frees resources for other activities
- Digital reporting platforms allow policyholders to self-report claims
- Artificial intelligence (AI)
- Can improve everything from product design to post-sales service
- Can process natural language and perform sentiment analysis to assess customer concerns
- AI may be able to recommend products and services (virtual assistants, etc.)
- Chat bots and robo advisors
* Reduces costs (replaces people)
* AI-powered robo advisors can process natural language and assess customer needs
* Could raise regulatory concerns if robo advisors provide incomplete information


## Optimizing the Operating Model

- Complexity and inefficiency increases operational costs
- Possible solutions:
- Outsourcing can help insurers who lack economies of scale
- Transferring operations to lower cost offshore captives or reinsurers

## Page 48
# II A201-102: The Economics of Insurance 

Source Author: Swiss Re (2001)

## Pages 4-31 Only

## Overview of This Reading

This is a very large study note in terms of testability; it is rich with quantitative, conceptual, and listy topics that could be tested ${ }^{15}$

Perhaps the most fundamental thing to understand from this reading is that economic methods are designed to link profits to insurance risk, not investment risk

## Key topics for the exam include:

- Shortcomings of traditional measurement systems
- How and why insurers can "borrow" cheaply to create value
- Base cost of capital
- Frictional costs - both from the shareholders' and insurer's perspective
- Franchise value
- How to create a replicating portfolio and how it changes through time
- How to calculate the economic value of liabilities
- How to calculate economic profit
- Why economic profit is immune to interest rate changes
- How emerging insurance experience affects economic profit
- The purpose of the treasury function
- Considerations for incentive compensation
- Problems with alternative methods like embedded value

Note: The video lesson series in the online course includes extensive numerical examples to illustrate key concepts in this chapter. Going through those examples is critical to fully understanding the framework in this study note, which often intimidates people at first. The good news is that once you master a few fundamentals, it's actually not that bad!

[^0]
[^0]:    ${ }^{15}$ This study note existed on the LPM syllabus and its predecessors for many, many years before moving to ILA-201 in Fall 2025.

## Page 49
# Introduction: Why Economic Capital? 

## Prerequisites for Maximizing Shareholder Value

1. Understand the value creation process
2. Ability to measure value creation
3. Incentive systems that align management interests with value creation

## How the Insurance Industry is Changing

Until the 1990s, competition was low and profit margins were high
Changes in the 1990s:

- Deregulation and globalization
- Increased competition from inside and outside the industry (banking)
- Higher competition $\rightarrow$ lower profit margins $\rightarrow$ higher volumes now required
- Increased value awareness across the industry


## Shortcomings of Artificial Value Measurement Systems

"Artificial" - traditional, non-economic approaches

1. Mask true value in a company
2. Mislead managers about key risks
3. Vary greatly across product lines and countries $\rightarrow$ comparisons are difficult
4. Overly conservative

- Leads to "hidden reserves"
- Allows companies to smooth/control profit emergence (U.S. GAAP)
- Smoothing masks volatility and true economic condition
- May hide the need for corrective actions


## The Economic Perspective

Assets should be valued at market values
Liability cash flows should be valued using best estimates and time value of money

## How Insurers Are Financial Intermediaries

1. Liability-Driven Financial Intermediaries

Borrow money from policyholders (premiums)
Invest premiums in financial markets

## Page 50
Pay benefits to policyholders if claim event occurs
2. Reduce Policyholder's Credit Exposure

Insurers hold extra capital to reduce risk of default (from policyholder's perspective)

# How Insurers Differ From Leveraged Investment Funds 

1. Competitive Disadvantage with Investing

Less favorable tax and regulatory environment
Double taxation (more on this later)
2. Insurers Can Borrow More Cheaply

It's cheaper to borrow from policyholders than in capital markets
Insurers can sell policies for more than their economic cost
Policyholders are willing to pay for protection

## How Insurers Create Value

1. Selling contracts for more than the production and frictional costs
2. Achieving investment returns greater than base CoC benchmark

Franchise value = intangible part of a company's market value that represents expected value from future business
$=$ Total Company Market Value - Economic Net Worth
In other words, a company is worth more to investors than simply taking the difference between current assets and current liabilities

## Cost of Capital (CoC) for Insurers

Investors (shareholders) can invest in an insurance company or in some other investment opportunity

Total Opportunity Cost of Capital = Base CoC + Frictional Costs + Liquidity Value + Option to Default Value

Base CoC = Benchmark Return on Investment Portfolio - Replicating Portfolio Return
I.e. the premium required if shareholders invested directly in the assets held by the insurer Do not use CAPM because it doesn't capture frictional costs

## Liquidity Value and Option to Default

1. Insurer's Option to Default

Insolvent insurers may default on liabilities

## Page 51
Cost is based on credit spread resulting from insurer's rating
Add the extra spread to the risk-free rate rate used in the EVL calculation

# 2. Liquidity Value 

Insurers may choose to hold less liquid assets if they can hold them to maturity
Higher yield on illiquid assets lowers the production value
Add the extra liquidity spread to the risk-free rate rate used in the EVL calculation

## Frictional Capital Costs

Frictional capital costs $=$ costs specific to investing in an insurer

## 1. Agency Costs

Shareholders require compensation for lack of transparency and control
Insurance companies are less transparent than other investments a shareholder could make Insurance company may not act in the shareholders' best interest
Cost ranges from 5-200 bps of capital held

## 2. Cost of Financial Distress

Shareholders require extra return for the company-specific risk of ruin (insolvency)
Cost ranges from 10-20\% of market value (shouldn't exceed franchise value)

## 3. Regulatory Restriction Costs

Cost of holding extra regulatory capital that can't be used for other purposes (like a liquidity risk)
Cost ranges from 0-200 bps of restricted capital

## 4. Double Taxation on Investment Income

Insurer's investment income is taxed when it flows through earnings, then it gets taxed again when distributed to shareholders
Cost $=$ Tax Rate $\times$ Taxable Income
Taxable income includes effects of statutory/tax reserve changes and the total investment income on capital

Try to make yourself look at all of this from the shareholder's perspective. As an investor, you want to know that the return for your investment is consistent with the risks taken. By choosing to invest in an insurance company, you need to be compensated for these insurance-company-specific frictional costs that aren't found in alternative investments.

## The Replicating Portfolio

The portfolio that matches the best estimate of future liability cash flows
Provides cash flows to pay claims, expenses, and capital costs

## Page 52
"Produces the liability"
Value of liabilities $=$ market value of replicating portfolio
Best estimate liability cash flows are easily replicated with risk-free assets
The risk in "pure insurance" (e.g. term life) best estimate cash flows is non-systemic and can be diversified away by shareholders

Products with interest rate risk have systemic risk (cannot be diversified away)
Requires more sophisticated hedging
Replication Risk - Inability to find a portfolio that replicates liability cash flows (e.g. liabilities too long)

Treated as a frictional cost

# Calculating the Economic Value of Liabilities (EVL) 

1. Project liability cash flows (premiums, claims, expenses, etc.)
2. Project frictional costs
3. Calculate net liability cash flow at each future point in time

Net $\mathrm{CF}=$ Premiums - Claims - Expenses - Frictional Costs
4. $\mathrm{EVL}=\mathrm{PV}($ Net CF$)$ at risk-free rate

The EVL is based on risk-free rates because the cash flows can be replicated with risk-free assets
Buy zero-coupon bonds to match years with negative net CF
Borrow (short) zero-coupon bonds to match years with positive net CF
EVL = Market Value of Long Bonds - Market Value of Short Bonds

## EVL Example

| Year | Premiums | Claims | Expenses | Frictional Costs | Net CF |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 0 | 100 |  | 87 | 0 | 13 |
| 1 | 100 | 50 | 5 | 2 | 43 |
| 2 |  | 50 | 5 | 2 | -57 |

The company will receive 43 in year 1 and will have to pay out 57 in year 2
Build a replicating portfolio:
Buy zero-coupon bonds maturing for 57 in 2 years
Short zero-coupon bonds maturing for 43 in year 1
The long 2-year bonds will fund the net liability payment in year 2, and the borrowed 1-year bonds will be repaid with the positive cash flow in year 1

## Page 53
Assume the risk-free rate is $3 \%$ all years:

$$
\begin{aligned}
\mathrm{EVL}_{0} & =-\frac{43}{1.03}+\frac{57}{1.03^{2}} \\
& =-41.75+53.73 \\
& =11.98
\end{aligned}
$$

This is the net market value of the risk-free replicating portfolio at time 0

# Economic Profit and IRR 

## Economic Profit at Issue

Economic Profit $=$ Net CF - Change in EVL
From the previous example:

$$
\text { Economic Profit at Issue }=13-11.98=1.02
$$

In other words, the company collected 13 upfront but only had to spend 11.98 to set up the replicating portfolio

The IRR of the cash flows is:

$$
\begin{aligned}
13 & =-\frac{43}{1+\mathrm{IRR}}+\frac{57}{(1+\mathrm{IRR})^{2}} \\
\mathrm{IRR} & =1.44 \%
\end{aligned}
$$

The IRR is the company's cost of borrowing from the policyholder along with the cost of other expenses and frictional costs

Since the company borrowed at a rate of $1.44 \%$, then invested in assets yielding $3 \%$, the company earned a spread of $1.56 \%$

This illustrates the 2nd way that insurers differ from leveraged investment funds: the borrowing advantage

IRR is a fickle animal, especially if the cash flow signs switch a lot. As such, the authors recommend focusing on the absolute economic profit. However, in simple cases like the one above, you might be asked to calculate it on the exam.

## Economic Profit After Issue

At issue, expected economic profit in future periods is zero because the change in EVL is exactly offset by the cash flows and investment return

$$
\begin{aligned}
\text { Economic Profit }_{t}= & \text { Net CF After Frictional Costs }_{t} \\
& +\operatorname{InvReturn}_{t}-\left(\mathrm{EVL}_{t}-\mathrm{EVL}_{t-1}\right) \\
\operatorname{InvReturn}_{t}= & r \times \mathrm{EVL}_{t-1}
\end{aligned}
$$

## Page 54
This is really the same formula used above at issue; it's just that there's no InvReturn at issue.
Continuing the example, now one year after issue:

$$
\begin{aligned}
\mathrm{EVL}_{1} & =\frac{57}{1.03}=55.34 \\
\operatorname{InvReturn}_{1} & =0.03 \times 11.98=0.36 \\
\Delta \mathrm{EVL}_{1} & =55.34-11.98=43.36 \\
\text { Economic Profit }_{1} & =\underbrace{43}_{\text {Net CF }}+\underbrace{0.36}_{\text {InvReturn }}-\underbrace{43.36}_{\Delta \mathrm{EVL}}=0
\end{aligned}
$$

Since the replicating portfolio produces a cash flow pattern that is the mirror image of the liability cash flow pattern, everything perfectly offsets.

# Immunity to Interest Rate Changes 

If the risk-free rate changes, it has no effect on economic profit

- The change in InvReturn is exactly offset by the change in EVL
- InvReturn $=3 \%$ interest on previous EVL $+\Delta$ EVL due to interest rate shift

Suppose the risk-free drops to $2 \%$ at time 1 :

$$
\begin{aligned}
\mathrm{EVL}_{1} & =\frac{57}{1.02}=55.88 \\
\operatorname{InvReturn}_{1} & =0.03 \times 11.98+(55.88-55.34) \\
& =0.36+0.54=0.90 \\
\Delta \mathrm{EVL}_{1} & =55.88-11.98=43.90 \\
\text { Economic Profit }_{1} & =\underbrace{43}_{\text {No Change }}+\underbrace{0.90}_{0.54 \text { higher }}-\underbrace{43.90}_{0.54 \text { higher }}=0
\end{aligned}
$$

The replicating portfolio has a higher InvReturn because rates dropped (i.e. the bonds appreciated), but now the final liability cash flow of 57 is discounted by lower rate as well

## Impact of Different Insurance Experience

If cash flows end up different than expected, economic profit $\neq 0$

## Page 55
Suppose the claims in year 1 are 55 instead of 50 (but the risk-free rate hasn't changed):

$$
\begin{aligned}
\operatorname{NetCF}_{1} & =100-55-5-2=38<43 \\
\operatorname{InvReturn}_{1} & =0.03 \times 11.98=0.36(\text { no effect }) \\
\operatorname{EVL}_{1} & =\frac{57}{1.03}=55.34(\text { no effect }) \\
\Delta \operatorname{EVL}_{1} & =55.34-11.98=43.36(\text { no effect }) \\
\text { Economic Profit }_{1} & =\underbrace{38}_{5 \text { lower }}+\underbrace{0.36}_{\text {Same as before }}-\underbrace{43.36}_{\text {Same as before }}=-5
\end{aligned}
$$

Economic profit is designed to capture the impact of insurance experience

# Treasury Function and Transfer Pricing 

A company could set up a treasury function to attribute performance to underwriting (insurance) decisions vs. investments decisions

Total Profit $=$ Insurance Profit + Investments Profit
The treasury function determines the benchmark total return for the investment unit of the company

The treasury function:

1. Borrows assets equal to the replicating portfolio from the underwriting function
2. Loans assets equal to total capital to the investments function at a rate equal to the benchmark return

By specifying the benchmark return, the treasury function effectively determines the base CoC
When actual investment returns are earned on capital, the investments function pays the treasury interest on the loan

If the benchmark return for $\$ 100$ million of capital is $7 \%$, and the actual return is $8 \%$, then the investment function contributed $\$ 1$ million to economic profit

In the end, the goal is to simply isolate economic profit caused by investment experience to the investments function, not the insurance function. The insurance function's investment return on the replicating portfolio should not impact economic profit since the roll-forward of the replicating portfolio should be offset by cash flows-and if it's not, it is because of insurance experience, not investments experience (see previous examples above).

## Performance Attribution Analysis

Economic profit can be further analyzed within insurance and investments functions
Insurance attribution analysis should separate out:

- Impact of new business

## Page 56
- Deviations from expected experience

Investments attribution analysis should separate out:

- Asset allocation effects
- Currency selection
- Stock selection
- Sector selection


# Setting Economic Value Targets 

- If actual economic profit > expected economic profit, share prices increases
- Should be based on long-term interest rates
- Consider impact of new business
- Benchmark against other companies


## Incentive Compensation

- Should be linked directly to economic value creation
- Should reward good decisions on an ex ante basis (before risks are realized)

Challenge: Most performance can only be measured ex post

- Should not give managers a free put option

Should react to downside risk as well as upside
Deferral systems can be used for low frequency / high severity risks

- Don't based incentives solely on economic profit for high risk business with extreme swings

Suggested approach:

1. Set a baseline target bonus
2. Increase or decrease bonus based on manager or business unit's performance

## Problems with Non-Economic Other Methods

1. Embedded Value $=$ inforce value ( $P V$ of stat profits discounted at insurer's cost of capital) + market value of stat shareholder capital

- Biased toward higher-yielding assets
- Ignores frictional costs other than regulatory restrictions
- Regulatory capital charges are highest for lowest yielding assets

## Page 57
- Does not easily accommodate options and guarantees

2. Risk-Adjusted Return on Capital (RAROC)

RAROC $=$ PV(Economic Profit) $/$ (Risk Capital)

- Assumes all capital costs are proportionate to economic capital
- Hurdle rate is based on CAPM, which ignores frictional costs
- Only considers capital in first year
- Discounts expected returns at the expected earned rate
- Creates incentives to take investment risk

## Page 58
# FAQ on Certain Insurance Reserves Held After the TCJA 

Source Author: American Academy of Actuaries (December 2021)

## Overview of This Reading

All insurers are required to use tax reserves as the reserve basis when calculating taxable income
Tax reserves are defined by federal law: specifically, several subsections of Internal Revenue Code Section $807^{16}$

The Tax Cuts and Jobs Act (TCJA) of 2017 went into effect for calendar year 2018 and introduced significant changes (mostly simplifications) to how tax reserves are calculated

This Academy publication is essentially a long list of (24) FAQs that focus on the TCJA changes but also cover the general tax reserve framework ${ }^{17}$

We've preserved the FAQ numbers so you can easily cross-reference with the source reading if you want

## Key topics for the exam include:

- Understand the purpose of tax reserves
- Definitions of tax reserves and reserve methods
- How to calculate tax reserves for variable and non-variable products life/annuities
- Tax reserves for products other than life and annuity products
- Tax reserves for supplemental benefits and other miscellaneous items
- Accounting for changes in reserve basis


## General Background on Tax Reserves Under IRC §807(c)

Insurers are required to calculate tax reserves for the following $\S 807$ (c) categories ${ }^{18}$ :

1. Life insurance reserves: Includes life, annuity, and certain health insurance ${ }^{19}$
2. Unearned premiums and unpaid losses
3. Amounts (discounted at interest) for obligations under contracts without life, accident, or health contingencies
4. Dividend accumulations and other amounts held at interest
5. Premiums received in advance and premium deposit funds
[^0]
[^0]:    ${ }^{16}$ This is abbreviated IRC $\S 807$ throughout the source reading.
    ${ }^{17}$ It could be worse. There was once an Academy document with 150+ FAQs on a past syllabus!
    ${ }^{18}$ These are the " $\S 807$ (c) categories" that later FAQs sometimes refer to.
    ${ }^{19}$ That's right: the phrase "life insurance reserves" in a tax law context refers to both life and annuity reserves (and even certain health insurance reserves)! If you don't like the use of misnomers in the tax code, write your Congressperson, not TIA!

## Page 59
6. Reasonable special contingency reserves for group term life or group A\&H insurance used for premium stabilization, etc.

Key items that were preserved by the TCJA

- Tax reserve $\geq$ net surrender value (aka CSV)
- Tax reserve $\leq$ statutory reserve ("stat cap")


# 2 major changes introduced by the TCJA 

- Tax reserves now based on NAIC-prescribed method as of valuation date (not issue date)
- No longer prescribed interest/mortality tables for most tax reserves (still some exceptions) ${ }^{20}$


## Frequently Asked Questions on Certain Insurance Reserves

1. What is an insurance reserve?

- A liability for future benefits and expenses minus the value of future premium payments and considerations
- Needs to be supported by sufficient assets to assure company solvency
- A reserve is a balance sheet item; a change in a reserve is an income statement item

2. What is a tax insurance reserve?

- A reserve for the primary purpose of determining taxable income
- Source of guidance: IRC, Treasury rules/guidance, and court interpretations

3. What is a reserve method?

- The calculation of an appropriate amount for an insurer's net liability using stated actuarial formulas or models
- May utilize:
- Prescribed industry-wide factors/assumptions
- Prescribed ranges
- Company-specific factors/assumptions
- Prescribed model parameters
- Determined by the prescribing entity's specific regulatory or economic purpose (NAIC for statutory, federal law/IRC for tax, FASB for GAAP)
- Reserve amounts can vary significantly between methods

[^0]
[^0]:    ${ }^{20}$ Before the TCJA, the IRC prescribed specific interest and mortality tables for tax reserves that were usually different from the US Stat prescribed assumptions. Now, tax reserves rely much more heavily on the stat method.

## Page 60
# 4. What are the currently prescribed tax reserve methods? 

- IRC requires the tax reserve method to be:
- CRVM for life insurance contracts covered by CRVM
- CARVM for annuity contracts covered by CARVM
- Others: use the NAIC-prescribed method or a method consistent with other NAIC-prescribed methods if none exists
- The results of these methods may be further adjusted for computing taxable income

5. What if the method used for calculating statutory reserves is not the prescribed tax reserve method?

- First step: recalculate stat reserves using the prescribed method
- Statutory "permitted practices" are generally not considered NAIC methods for tax reserve calculations
The source reading doesn't explain why this would occur, but suppose an insurer is holding a larger stat reserve than the NAIC-prescribed method. In that case, the insurer must first recalculate the stat reserve using the NAIC-prescribed method before using it to determine the tax reserve.

6. Are all statutory reserves included in the computation of tax reserves?

- No
- Starting point: Stat reserve calculated using an NAIC-prescribed method on the valuation date
- IRC and Treasury regulations:
- Exclude certain types of stat reserves:
* Life deficiency reserves
* Deferred/uncollected/unpaid premium liabilities
* Excess interest reserves
* Asset adequacy reserves
* Voluntary reserves
- Require further adjustments, such as multiplying by a factor or using a different interest rate
- Tax reserves are capped by stat reserves (including deficiency reserves) on a contract level basis
- Exception: cancellable disability income reserves are capped based on the year of incurral in aggregate for the LOB

People often get very confused over how to treat deficiency reserves for tax purposes, so here is some additional clarification. There are basically two things to know:

## Page 61
1. Deficiency reserves should not be included in the stat reserve used to calculate the tax reserve. The tax reserve is usually just $92.81 \%$ of the stat reserve (explained in FAQ 8).
2. Deficiency reserves should be included in the stat reserve used to determine the stat cap. In other words, the final tax reserve cannot exceed the stat reserve including the deficiency reserve.

# 7. Should tax reserves be determined on an individual contract basis? 

- Yes
- If stat reserves are calculated on aggregate basis and allocated to contracts, the allocation method must be required, permitted, or consistent with the NAICprescribed method ${ }^{21}$

8. How are tax reserves for non-variable life insurance reserves calculated?

- Includes: non-variable life insurance, life-contingent annuities, and noncancellable/guaranteed renewable A\&H
- Tax reserve $=92.81 \% \times$ NAIC-prescribed stat reserve
- Remove any of the following from the stat reserve (if present) before multiplying by $92.81 \%$ :
- Deficiency reserves
- Reserves for excess interest guaranteed beyond year-end ${ }^{22}$
- Adjust for deferred/uncollected/unpaid premium liabilities/assets
- Example: subtract DPA from mean stat reserve
- Subject to stat cap and CSV floor

See the video lesson for an illustrative example.
9. How are tax reserves for variable life insurance reserves calculated?

- Follow general reserve rules with modifications for variable nature

$$
\begin{aligned}
\text { TaxRes }= & \max [\text { CSV, } \$ 817 \text { StatRes }] \\
& +92.81 \% \times(\text { Total StatRes }-\max [\text { CSV, } \$ 817 \text { StatRes }])
\end{aligned}
$$

- $\S 817$ StatRes $=$ contract reserve separately accounted for under IRC $\S 817$
- Aka "separate account reserve"
- Covers benefits not guaranteed by the general account (i.e. value of SA assets backing the VA)

[^0]
[^0]:    ${ }^{21}$ This relates to most reserves calculated using VM-20 or VM-21, each of which have methods of allocating aggregate PBRs to individual contracts.
    ${ }^{22}$ Excess interest reserves are reserves that result from the guarantee of interest in excess of the prevailing state assumed rate that is to be paid or credited after the end of the current tax year.

## Page 62
- Cannot exceed the statutory reported amount
- Total StatRes $=$ total stat reserve at the contract level using the NAIC-prescribed method
- Total contract stat reserve includes GA and SA reserves, adjusted for exclusions (remove any deficiency reserves, etc.)
- Subject to stat cap and CSV floor
- IRC $\S 817$ requires an adjustment to end-of-year reserve to remove appreciation/depreciation of supporting assets ${ }^{23}$

See the video lesson for an illustrative example.
10. How are tax reserves for unearned premiums and unpaid losses calculated?

- Unearned premiums and unpaid losses for life insurance and noncancellable/guaranteed renewable A\&H:
- Tax Reserve $=$ stat reported amount (not discounted)
- Cancellable disability income unpaid losses:
- Tax Reseve $=92.81 \%$ of stat reserve (NAIC-prescribed)
- Stat cap based on year of incurral in aggregate for the LOB
- Credit disability unpaid losses: follow P\&C reserve methods and Treasury discounting rules
- Unearned premiums on cancellable health insurance
- Tax Reserve $=$ unearned premiums reduced by $20 \%$
- Other cancellable health insurance claims: based on assumption losses paid mid-year following accident year, discounted per Treasury rules

11. How are tax reserves for amounts discounted at interest only calculated?

- Includes obligations without life, accident, or health contingencies
- Discount rate $=$ highest rate(s) permitted by NAIC as of valuation date
- The $92.81 \%$ factor does not apply ${ }^{24}$
- Stat cap applies on a contract basis

12. How are tax reserves for dividend accumulations and other amounts held at interest calculated?

- Ordinarily equal to the statutory reserves held

[^0]
[^0]:    ${ }^{23}$ This prevents increases/decreases in the value of the SA assets from affecting the tax reserve. Otherwise, tax reserves could fall or rise substantially due to market forces, which would greatly increase volatility in taxable income (and tax revenue).
    ${ }^{24}$ In other words, use $100 \%$ of the result of the PV calculation.

## Page 63
- The $92.81 \%$ factor does not apply

13. How are tax reserves for premiums paid in advance and premium deposit funds calculated?

- Ordinarily equal to the statutory reserves held
- The $92.81 \%$ factor does not apply

14. How are tax reserves for reasonable special contingency reserves under for group term life, group A\&H, and health insurance calculated?

- Ordinarily equal to the statutory reserves held
- The $92.81 \%$ factor does not apply

15. What defines a reserve basis for statutory reporting?

- The NAIC-prescribed method and prescribed actuarial assumptions
- Any other actuarial methods/assumptions used in the calculation

16. What defines a reserve basis for tax reporting?

- NAIC-prescribed method applicable to the contract on the valuation date
- If no NAIC-prescribed method, use another appropriate actuarial method
- Adjustments such as the $92.81 \%$ factor
- Elimination of certain items (e.g. deficiency reserves, due/unpaid premiums)

17. Can a statutory or tax reserve basis for a contract be modified or changed after issue?

- Yes
- The reserve basis is determined at the valuation date but may be modified later
- A reserve basis change is one where regulatory guidance (e.g. VM, IRS notices) consider it as such

18. Are there differences between statutory reserve basis changes and tax reserve basis changes?

- Yes, in definitions, measurements, and reporting processes
- Statutory changes are described in the NAIC Valuation Manual
- Tax changes are described in the IRC, Treasury/IRS guidance, and court interpretations
- Generally, most stat valuation basis changes are considered tax basis changes (but exceptions apply)
- Tax reserve basis changes may include items that are not considered stat changes (more in FAQ 21)
- Measurement differences:

## Page 64
- Stat changes are measured at the $\underline{B O Y}$ of change and flow through surplus
- Tax changes are determined as of the EOY based on EOY inforce (excluding new contracts) and taken into taxable income as required by IRC guidance

See the video lesson for an illustrative example.
19. How are tax reserve basis changes reflected in taxable income?

- Treatment of Tax Reserve Basis Changes Occurring in 2018 and later (Post-TCJA):
- Spread following automatic accounting method change rules
- Decrease in income (reserve increase) recognized in the year of change
- Increase in income (reserve decrease) spread over 4 tax years (year of change + next 3)
- Changes are netted by $\S 807$ (c) category, resulting in a single amount per category
- Must file Form 3115 to obtain automatic consent for accounting method change
- Treatment of pre-1/1/2018 Tax Reserve Basis Changes (Pre-TCJA):
- Continue the 10-year spread under prior law
- Transition rules to account for the difference between tax reserves as of 12/31/2017 and 1/1/2018 (TCJA Impact):
- Transition rules apply to most reserves
- The difference between pre- and post-TCJA law amounts is included/deducted in equal amounts over the next 8 tax years (starting 2018)

20. What reporting is required for tax basis changes?

- Must file Form 3115 listing tax basis changes by $\S 807$ (c) category, even if the amount is zero
- Approval is technically required, but most are expected to be "deemed approved"

21. What are examples of reserve basis changes?

- Rev Ruling 2020-19 examples:
- Yes for tax change: ${ }^{25}$
* Correction of tax reserve formula application
* NAIC VM change for previously issued contracts
* NAIC VM change for contracts issued in year of change
- Not a stat basis change
* Change in Actuarial Guideline

[^0]
[^0]:    ${ }^{25}$ These are all situations that would be considered a change in the tax reserve basis. These are also considered a change in stat basis unless otherwise noted.

## Page 65
* Change in NAIC-prescribed CSO mortality tables
- No for tax change: ${ }^{26}$
* A change in the prevailing VM-20 reserve component (e.g. DR previously exceeded NPR, but now NPR prevails)
* Experience-based update in mortality rates per VM-20
* A change because the CSV floor begins to apply
* Inclusion of previously omitted policy cells (mathematical/posting error)
* Increase in reserves solely for new benefits on existing contracts
- Other examples that are considered stat basis changes, but are not applicable to tax reserves:
- Change in stat reporting from a domiciliary state-approved method to NAICprescribed method
- Any change in non-NAIC-prescribed method
- Unclear: Whether a change in tax reserves due to a change in the stat cap results in a tax basis change
- Guidance: apply consistent treatment

22. How are tax reserves for supplemental benefits calculated?

- Supplemental benefits defined by tax law:
- Guaranteed insurability
- Accidental death or disability
- Convertibility
- Disability waiver
- Other prescribed by regulations (none currently)
- A Qualified Supplemental Benefit (QSB) is one listed above that also meets the following criteria:
- Has a separately identified premium or charge
- Charges cannot be funded from the net surrender value of any other contract benefit
- Must be supplemental to a contract with a reserve in an IRC $\S 807$ (c) category
- Qualified supplemental benefit (QSB) vs. nonqualified supplemental benefit
- QSB Tax Reserve $=92.81 \% \times$ SB Stat Reserve

[^0]
[^0]:    ${ }^{26}$ These are all situations that would not be considered a change in the tax reserve basis. These are also not stat basis changes.

## Page 66
* Treated as a separate contract subject to its own CSV floor (usually none) and stat cap
* Total Contract Tax Reserve = Underlying Contract Tax Reserve + QSB Tax Reserve
- Nonqualified SB treatment:
* Add the SB stat reserve to the underlying contract's stat reserve first
* Total Contract Tax Reserve $=92.81 \% \times$ Total Contract Stat Reserve
* CSV floor and stat cap apply at the total contract level

See the video lesson for an illustrative example.
23. How are tax reserves calculated for supplemental benefits that are not listed in the tax law?

- Key issue: Whether tax reserve for the SB should be treated as separate or combined with underlying contract for statutory cap, $92.81 \%$ factor, and CSV floor
- General IRC approach: Treat life insurance contract as a single integrated contract (QSBs are an exception as noted in FAQ 22)
- LTCI that pays benefits in excess of underlying life/annuity benefits
- Many tax experts agree the excess portion should be treated as a separate contract
- Other non-listed benefits: LTCI that does not provide benefits in excess of underlying life/annuity benefits, accelerated DBs, disability income benefits
- Treatment of these for determining tax reserves is "unclear"

24. Do any of the reserve assumptions used in an NAIC-prescribed reserve method directly affect life insurance contract tax compliance and thus policyholder taxation?

- Yes: mortality and interest requirements as noted below
- Mortality:
- IRC $\S 7702$ and $\S 7702$ A require "reasonable mortality charges" or charges not exceeding prevailing CSO tables
- Prevailing CSO tables are the most recent NAIC-prescribed tables permitted in at least 26 states for reserves when the contract was issued
- New VM tables become prevailing as of their first permissible use date
- 3-year transition period for new prevailing tables: Companies may use prior tables for issues during the year of change and next 2 years
- $\S 7702$ authorizes regulations for using mortality charges different from prevailing tables

## Page 67
- Interest:
- For policies issued on or after 1/1/2021, minimum interest rate for NSP, GLP, and 7 -pay premium $=$ greater of:
* Contract guaranteed rate
* $\min [$ Insurance Interest Rate, $4 \%]$
- Minimum interest rate for GSP = greater of:
* Contract guaranteed rate
* $\min [$ Insurance Interest Rate $+2 \%, 6 \%]$
- Changes in maximum valuation rate for life insurance contracts with $>20$ years duration (per SVL) may trigger changes in the Insurance Interest Rate

Policyholder taxation a major topic in itself that is not covered in any detail on the current ILA-201U syllabus, so unless you've taken another ILA recently that covered IRC $\S 7702$ and 7702A, the above information isn't going to make much sense, and that's OK. The exam committee can't expect you to know any more than what's listed above, so I would simply try to memorize the basic things above for exam prep.

## Page 68
# Evolving Strategies - Post-Level Term Profitability 

Source Author: George Hrischenko, Product Matters (February 2015)

## Overview of This Reading

This article describes advantages and disadvantages of four approaches for pricing premiums in the post-level term (PLT) period

One of the single biggest unknowns with these methods from the perspective of a pricing actuary is: how well policyholders react to the different premium structures?

## Key topics for the exam include:

- Impact of Regulation XXX on term life insurance
- Describe early experience observed in PLT period and its implication for insurer profitability
- Be able to describe, compare, and contrast the 4 approaches

1. The Original Approach
2. Simplified Re-Underwriting
3. The Graded Approach
4. The Class-Continuation Approach

## Introduction and Background

This material comes from the conclusion of the article, but I think it's helpful to read for context upfront.
Level term offers an affordable alternative to expensive permanent life (WL) and has become very popular

Pricing structures have evolved into a limited level premium period followed by a steeply increasing YRT rate scale in the post-level term (PLT) period

- YRT (or ART) = yearly (annually) renewable term (premiums increase annually with age and are much higher than the original level premium)

Now that many term products are reaching the PLT period, insurers are concerned about ongoing profitability

Various pricing approaches for transitioning from the level premium period to the PLT are discussed in this article, but the biggest question is...

How will the policyholder react to any incentives built into the rate structures?

## Brief History of Regulation XXX

In the actual reading, the material in this section comes from a section of the article that is oddly titled "the pricing approach," but this is not one of the four PLT pricing approaches discussed in the later

## Page 69
sections. This material is more of a brief history of how Regulation XXX increased the reserve and capital requirements for term life insurance.

Before 2000, the unitary reserve method allowed companies to hold very low reserves for level term products with YRT premiums in the post-level period

In 2000, Regulation XXX began requiring companies to calculate separate reserves for the level and post-level periods (known as segmented reserves)

- Resulted in much higher reserves than the unitary method because the level period reserve couldn't "count" the much higher future YRT premiums

Companies adapted to XXX by using reinsurance and other sources of financing to raise capital to back the higher reserve requirements

Now that more of these PLT products are entering or nearing the post-level period, companies face questions:

1. How do initial PLT lapse assumptions compare to expected, calculated more than a decade ago?
2. What mortality experience can we expect on the residual in-force?
3. Can we encourage more lives to renew at the PLT?

# What Limited Experience Tells Us 

PLT mortality experience is currently very limited
Early results show lower lapses in early PLT durations than originally assumed, which means mortality could be better than assumed

## Possible explanations for lower PLT lapses:

- Policyholder complacency resulting from automatic bank draft
- Keep policy in force while shopping for lower rate
- Some may feel the high cost is worth it
- Reluctance to go through underwriting again
- Personal situations that cause delayed lapses (divorce, etc.)

Key implication: Retaining even a small portion of lives that were originally expected to lapse could significantly reduce PLT mortality deterioration

The remainder of the article describes 4 pricing approaches for managing PLT experience with the above goal in mind:

1. The Original Approach
2. Simplified Re-Underwriting
3. The Graded Approach

## Page 70
4. The Class-Continuation Approach

# The Traditional Approach (The Original Approach) 

The author refers to this approach as both the "original approach" and the "traditional approach" in the reading, but he seems to favor "traditional approach" the most.

## The Approach

- Assume a shock lapse rate (a.k.a. jump rate) in YRT premiums

This approach has been the most appealing in today's environment
Intended to accomplish 2 goals:

1. Increase the YRT premium enough so that healthier lives would have good reasons to lapse and seek other coverage

- Some companies offered conversion options as well

2. Set a high ceiling rate to allow the company to alter rates with emerging mortality experience

## Advantage Over Other Approaches

- Simplest to administer


## Problems with this approach

- Led to getting shock lapses (surprise!) $\Rightarrow$ only the worst risks remained in force
- Claims volatility due to limited credibility
- Potentially dangerous from an image perspective (negative publicity on high premium increases for people who really need coverage)


## Simplified Re-Underwriting

## The Approach

- Offer the insured the option to answer a simplified issue underwriting questionnaire as the PLT approaches
- If the insured agrees to do the questionnaire...
- Questionnaire determines the PLT risk class (e.g. smoker/non-smoker)
- Resulting YRT rates will be less than the traditional approach's ceiling
- If insured declines survey, they default to traditional YRT rates


## Advantages Over Other Approaches

1. Less arbitrary
2. Greater sense of fairness: appeals to policyholders and regulators

## Page 71
3. Helps address the selective lapsation issue in many of the other approaches
4. Policyholder receives potentially lower rate and insurer has more confidence that the rate is warranted

# Outstanding Questions/Issues 

1. Does offering underwriting send a signal to the policyholder to lapse earlier than they would otherwise?
2. Does the notification of a rate jump cause impaired risks to increase the rate of term conversions?
3. Implementation questions

- How will it be communicated to policyholders?
- How will questions be asked?
- What to do with incomplete questionnaires?
- How to maximize response rate?

Considerations for distributing the questionnaires

- Direct mail using yes/no questions
- Agents and producers-not likely participate in the process without incentives
- Call centers may be useful

Underwriting considerations:

- Web-based solutions used to develop logic-based underwriting decisions
- Example: SCOR's Velogica could be useful for middle markets
- Lab-scoring tools can be used to assess blood and fluid panels (medical underwriting results)


## The Graded Approach

## The Approach

- PLT premiums increase at a much smaller increment in early years of PLT (e.g. first 5 years), then go to YRT schedule


## Advantages Over Other Approaches

1. Initial PLT rates are much more attractive to policyholders
2. Insurer has the right to increase rates to the ceiling if experience justifies it
3. Could be more attractive to policyholders than having to go through re-underwriting
4. Does not increase administrative burden substantially

## Page 72
5. Early results suggest this approach has the intended effect of lowering lapses, which improves PLT mortality

- Has more supportable experience than other approaches


# Outstanding Issues 

1. Best risks can still obtain better rates
2. Companies do not yet have reliable YRT experience using this approach (i.e. after the graded period ends)
3. Most experience has been in Canada-will it play out differently when used in the U.S.?

## The Class-Continuation Approach

## The Approach

- Let's the original risk classes continue into the PLT period
- Magnitude of rate jump depends on insured's original risk classification
- Best risks have lowest premium jump
- Rates converge to ultimate YRT scale in later durations (i.e. the original YRT scale)
- No single rate ceiling like traditional approach


## Advantages Over Other Approaches

- May be considered the "fairest approach" since it relies on original underwriting
- May encourage healthy lives to persist by rewarding the best risks with the lowest premium jumps
- Discourages worst risks by pricing their rates close to the YRT ceiling
- Can use permanent insurance experience to help model risk class rates


## Outstanding Issues

- Lack of experience with approach
- Preferred class rates will have to be fairly low to be competitive, which means they will increase the fastest to their YRT scale later
- Permanent pricing can't be used as a direct proxy
- High selective lapsation risk for any preferred policyholders who have become impaired since issue

## Page 73
# Mechanics of Dividends 

Source Author: Dale Hagstrom, SOA Research Institute (March 2022)

## Overview of This Reading

This paper gives an overview of participating life insurance (policies that pay dividends to policyholders)

Some of the dividend methods covered by this paper can be very complex in the real world. This paper provides only a basic description of them, and it's important to focus only on the level of detail provided for exam purposes. You will probably not fully grasp some of the concepts presented in this paper, but that's not needed for exam purposes.

Policies that pay policyholder dividends are usually called "participating" policies because the policyholders participate in the experience of the block.

## Key topics for the exam include:

- Process to set dividends
- Dividend payment options
- Types of dividend methods and formulas
- Dividend framework
- Recognition of policy activity
- Handling one-time changes and constraints
- Thought process when changing the dividend scale based on experience
- Par business issued by stock life insurance companies
- Different perspectives of "fair and equitable"
- Other considerations and forms of nonguaranteed elements


## Introduction

This paper describes how participating (par) policies work under the traditional approach to setting policyholder dividends

- Participating means that the policyholder participates in the experience of the insurer
- Par policyholders pay a higher premium than non-par policyholders but can receive nonguaranteed dividends in the future

Most par products are whole life, which is what this paper focuses on

- It's possible to have dividends on other types of insurance, but rare

Most par products are issued by mutual companies, while policies with other nonguaranteed elements are issued by stock companies ${ }^{27}$

[^0]
[^0]:    ${ }^{27}$ A mutual life insurance company is one owned by policyholders. A stock company is owned by stockholders.

## Page 74
- Only par policies paying dividends are in scope of this paper


# How Dividends Work 

Definitions of dividend:

- Return of premium that was not needed
- Distribution of surplus that the insurer does not need to retain any longer

In the US and Canada, policyholder dividends are usually based on the contribution principle

- Each policy's dividend = allocation of aggregate divisible in proportion to what the policy contributed to surplus based on experience factor classes


## Process To Set Dividends

- Declaration by Board, after recommendation by management and/or dividend actuary
- Board determines the amount of divisible surplus
* Must balance the need to pay higher dividends (competitiveness) with the need to retain surplus for future needs (new business, solvency)
* Consider surplus impact on ratings
- Board authorizes a dividend scale recommended by management and/or a dividend actuary
* Interactive, back and forth process
* Usually starts with prior year and looks at changes in experience since then
- Distribution to individual policies according to dividend scale adopted
- Dividends are usually paid annually based on the dividend scale in effect on a policy's anniversary
- Ideally the dividend scale will be known at least a month before each policy anniversary so the dividend amount can be communicated on the policyholder's premium notice
- Off-anniversary dividends are payable on death and sometimes other terminations (beyond scope of paper)


## Dividend Payment Options

Common dividend options that policyholders can select (for how they receive the dividend):

- Cash
- Apply toward premium and apply any excess to another option
- Purchase paid-up additions (PUAs) that match the basic policy's coverage period

## Page 75
- Purchase PUAs parallel to basic policy's coverage, including final endowment ${ }^{28}$
- Purchase one-year term insurance addition
- Leave on deposit in a dividend accumulation fund (interest rate could be guaranteed plus a nonguaranteed excess amount)


# Additional dividend options for specialized markets or other special situations: 

- Combination of PUAs and term additions that shift over time to achieve a target layer of coverage
- Called "economic" and "enhancement" in the US and Canada, respectively
- Purchase PUAs in early years, then surrender them in later years to offset premiums
- Important to communicate that dividends are not guaranteed, so premiums may not be fully offset
- Combinations of dividend use and policy loans to "achieve desired cash flows"


## Types of Dividend Methods and Formulas

## 3 principal sources of earnings for dividend payments:

1. Mortality - biggest source initially and rises gradually, then falls as net amount at risk declines
2. Investment - small initially but eventually becomes the dominant source later as the policy accumulates more assets
3. Expense - fairly small and constant over the life of the policy

Gains from these 3 sources add up to the total dividend paid to the policyholder

## Common Dividend Methods

## 1. Contribution Method

- Based on a 3-factor formula for mortality, investment, and expense

$$
\operatorname{Div}_{x, t}=\left(q-q^{\prime \prime}\right)\left(\text { Face }-\operatorname{Res}_{x, t}\right)+\left(i^{\prime \prime}-i\right)\left(\operatorname{Res}_{x, t-1}+\mathrm{NP}_{x}\right)+\left(\operatorname{Exp}_{x, t}-\operatorname{Exp}_{x, t}^{\prime \prime}\right)
$$

where:
$\left(q-q^{\prime \prime}\right)=$ valuation mortality rate minus mortality rate used to distribute surplus
$\left(\right.$ Face $\left.-\operatorname{Res}_{x, t}\right)=$ net amount at risk
$\left(i^{\prime \prime}-i\right)=$ interest rate used to distributed surplus minus valuation interest rate

[^0]
[^0]:    ${ }^{28}$ The author does not explain how this option is different from the previous one, and it's not $100 \%$ clear from the language in the paper. In both cases, the idea is to use each dividend to purchase fully paid-up additions to the total death benefit. This increases the policyholder's DB over time but does not increase the premium since the additions are fully paid up.

## Page 76
$\left(\operatorname{Res}_{x, t-1}+\mathrm{NP}_{x}\right)=$ initial reserve at BOY $t$ after valuation NP is added
$\left(\operatorname{Exp}_{x, t}-\operatorname{Exp}_{x, t}^{\prime \prime}\right)=$ expense allowance (loading in gross premium) minus expense allocated to the policy

- Any of the 3 components can be positive or negative
- $q^{\prime \prime}, i^{\prime \prime}$, and $\operatorname{Exp}^{\prime \prime}$ are not exact insurer experience since it wouldn't be known until $\mathrm{EOY}^{29}$
- Instead, these values are set by the insurer to retain some profit or reconcile aggregate dividends to divisible surplus
- May also include additional factors for specific situations
- Relatively simple as experience factors less explicit margins are used in the formula
- The difference between select and ultimate mortality can also be used to help offset/amortize acquisition costs


# 2. Experience Premium Method 

- One possible formula:

$$
\operatorname{Div}_{x, t}=\left(i^{\prime \prime}-i^{\prime \prime \prime}\right)\left(\operatorname{EPRes}_{x, t-1}^{\prime \prime \prime}+\mathrm{EP}_{x}^{\prime \prime \prime}\right)+\left(\mathrm{GP}_{x}-\mathrm{EP}_{x}^{\prime \prime \prime}\right)
$$

- Using the above formula, dividends $=$ sum of:
(a) Excess of the interest rate used to distribute surplus $\left(i^{\prime \prime}\right)$ over a conservative, low interest rate $\left(i^{\prime \prime \prime}\right)$
$\left(\operatorname{EPRes}_{x, t-1}^{\prime \prime \prime}+\mathrm{EP}_{x}^{\prime \prime \prime}\right)=$ initial reserve at BOY $t$ based on the same assumptions as the experience premium $\mathrm{EP}^{\prime \prime \prime}$
(b) Proxy gross premium (GP) minus an experience premium ( $\mathrm{EP}^{\prime \prime \prime}$ ) based on mortality and expense experience
- Advantages:
- Investment factor is likely positive and will increase over time even if returns are low
- Levels out mortality and expense gains over the life of the policy (no need to update mortality and expense factors)
- Relatively simple since only the investment component needs updating


## 3. Asset Share Method ${ }^{30}$

[^0]
[^0]:    ${ }^{29}$ The author says that you could denote actual experience with a single prime (e.g. $q^{\prime}$ ), but it's not clear how that would be used in the formula since he says that actual experience won't be known soon enough to compute dividends.
    ${ }^{30}$ The asset share method is described with very little detail in the paper, and unless you've seen it in practice, it will probably be difficult to understand what's going on just from this paper. In a life insurance pricing context, a policy's "asset share" is the share of the insurer's assets attributable to that

## Page 77
- Attempts to be more equitable by developing a dividend scale that results in an acceptable pattern of asset shares for representative cells
- Asset shares can be evaluated at an anchor duration (e.g. 20th year)
- Cells are defined by issue age, gender, underwriting class, size, etc.
- Uses the same 3-factor formula as the Contribution Method with the following differences:
- Asset Share method uses best estimate assumptions
- "The factors will not represent the earnings from that source, but rather will represent just what is needed to reproduce a dividend formula designed to result in a certain pattern of asset shares"
- After analyzing representative cells, interpolate/extrapolate to all other possible cells so that dividend scales can be developed for all policies
- Can be complicated to update for inforce policies
- Requires a re-projection of asset shares, replacing expected experience with actual experience
- Adjust dividend scale to return to the original target pattern of assets shares
- May be useful in demonstrating compliance with self-supporting rules in the NAIC illustration regulation


# 4. Fund Method 

- Projects a target fund = reserve + an "amount A" from issue to an anchor duration (e.g. 20th year)
- "Amount A" grows to a target surplus at the anchor duration
- Can be adjusted to achieve a desired pattern of dividends ${ }^{31}$
- Does not contain steps to develop dividend scales or asset shares for individual model cells ${ }^{32}$
policy. It's essentially an accumulation of the cash flows produced by the policy (premiums in, expenses out, etc. accumulated with interest). Pricing actuaries use asset shares to evaluate premiums and other pricing assumptions. Since dividends would be another benefit paid to the policyholder, they can be incorporated into an asset share model so that the dividend actuary can evaluate how dividends affect asset shares. For this exam, you only need a very vague understanding of asset shares since there's so little information about it in this paper.
${ }^{31}$ In the author's words, "One supposes some attention during product development is paid to the resulting pattern of dividends expected, and the pattern of amount A development over time may be crafted to some degree to allow a steadier pattern of dividends, if necessary." The author does not mention "amount A" again or include it in any formulas. See the video lesson for more explanation.
${ }^{32}$ There isn't enough detail in the paper to fully process this statement from the author, but I don't think he's saying you can't develop dividend scales because he goes on to provide a formula framework that can be used to develop dividends. He's probably comparing the methods based on specifics that are not in the paper.

## Page 78
- Uses best estimate assumptions (similar to those used for the asset share method)
- Dividend formula:

$$
\begin{aligned}
\operatorname{Div}_{x, t}= & \left(\text { Fund }_{x, t-1}-\text { Fund }_{x, t}\right)+\mathrm{GP}_{x}+i^{\prime \prime}\left(\text { Fund }_{x, t-1}+\mathrm{GP}_{x}\right) \\
& -q^{\prime \prime}(\text { Face })-\operatorname{Exp}_{x, t}^{\prime \prime}-\text { OtherExp }_{t}
\end{aligned}
$$

where:
$\left(\right.$ Fund $_{x, t-1}-$ Fund $\left._{x, t}\right)=$ negative of growth in target fund (i.e. a charge for required growth)
$i^{\prime \prime}=$ interest rate used to distributed surplus
Fund $_{x, t-1}+\mathrm{GP}_{x}=$ required fund at BOY after GP is added
$q^{\prime \prime}($ Face $)=$ death benefit based on mortality rate used to distribute surplus
$\operatorname{Exp}_{x, t}^{\prime \prime}=$ expense allocated to policy
OtherExp = other benefits and expenses (e.g. commissions and taxes)

- May be easier and less arbitrary than the asset share method
- Can develop consistent rules across plans with the fund method
- Solving for dividend scales using asset shares can be arbitrary and "misleadingly similar to the Contribution Method"
- Like the asset share method, updating dividend scales can be tedious
- Adjust dividends to return to the targeted pattern of funds, replacing expected experience with actual
- Like the asset share method, can be useful for self-support tests


# Concepts That Appear in the Formulas 

- Policy factors - values set by the product for premiums, cash values, face amount, policy loan interest rate
- Experience factors - mortality/morbidity rates, premium persistency, expense, commissions, taxes, investment income, policy termination, reinsurance
- Also experience premiums for the EP method
- Experience factor class - group of policies whose dividends are based on the same experience factors
- A given policy will belong to several experience factor classes


## Possible Variations

Variations of the previous methods also exist

## Page 79
- Developments affecting new business may require updates to dividends for existing business
- The insurer may monitor ratios of accumulated profit to risk charges and adjust dividends as necessary to maintain targets

As experience emerges, it is expressed in terms of "experience factors input to a model" because:

- It is not practical to track a gain and loss exhibit separately for each model cell
- It would prevent the pooling mechanism of insurance

Dividends can be calculated on a per 1000 (per unit) basis and loaded into admin systems in tables

- E.g. if the dividend per unit for a female age 60 with a 100,000 face policy is 5 , the dividend would be $100 \times 5=500$
- Other admin systems may be designed to calculate dividends from first principles using the formulas described earlier


# Dividend Framework 

It's important for a dividend framework to allocate divisible surplus in an equitable manner and that is consistent over time

The actuary must be able to explain why dividends vary within any given year by plan, issue age, duration, underwriting class, size, etc.

- Duration is particularly important for policy illustrations

The actuary should also be able to explain variations over time and why actual dividend scales differed from illustrated scales

The following should be consistent over time so that the contribution principle is followed:

- Assignment of policies to experience factor classes
- Allocation methods for experience factors
- Structure of formulas for using experience factors


## Recognition Of Policy Activity

May insurers also reflect policyholder choices that cause profitability to vary for otherwise identical policies:

- Purchase of PUAs: results in higher coverage, which increases mortality and investment profit sources
- Leaving dividends on deposit: increases investment profit source
- Use of riders for additional coverage (temporary term, accidental death, disability)

## Page 80
- Some insurers incorporate these into the base policy's experience factors, while others have an explicit term for them in the dividend formula
- Policyholder may accept an offer to amend their policy based on new underwriting, regulations, or tax issues
- Policy loan utilization or any other optional feature that affects policy values


# Handling One-Time Changes 

## Examples of temporary changes that could affect aggregate distributable surplus

- Large capital gains/losses that impact income immediately (excludes IMR-related items for US stat)
- Catastrophic mortality event
- Spike in lapse rates (or extreme lack of lapses)
- Release of a liability held for litigation or tax audit
- Major loss in litigation
- Retroactive liability established because of a change in law or court ruling


## Examples of permanent changes that could affect aggregate distributable surplus

- Changes in experience factors to new levels
- Reinsurance cost on existing business
- Change in tax law
- Additional obligations for increasing expenses, benefits, reserves, etc.
- Changes in dividend scale to increase equitability
- Board-approved changes in surplus growth to meet changing ERM, new business, or competitive objectives

Questions to consider when making a one-time change to dividends:

- Which policyholders should be affected (maybe not all)
- Whether the impact can be spread over a few years to moderate it
- Also consider that temporary changes will eventually reverse
- Use of smoothing methods to avoid declines and discontinuities in dividend payments
- Pegging - continue paying prior dividend until dividends on the new scale exceed it
- Substitution - continue paying original scale from issue even if the scale changes shortly after issue

## Page 81
- Experience Premium Method - can also be used to smooth dividends after changes ${ }^{33}$
- How to communicate the change to policyholders and emphasize the nonguaranteed nature of dividends
- How to reflect in future illustrations for new and inforce business
- How to reflect in asset adequacy testing, self-support testing, EV, etc.


# Constraints and Context 

- Allocation based on past contributions, but with "an eye to the future"
- The Contribution Principle is about distributing historical gains
- However, some actuaries may choose to apply it over an extended period of time to help plan for future surplus needs
* ASOP 15 gives the actuary this option
- Relationships between existing business in force and new business
- In Canada, experience factor classes are established at issue and not expected to change
- In the US, experience factor classes may be updated over time as conditions change
- Examples of distinctions that should be made even if experience is pooled:
* Mortality: create an experience mortality table graduated over age/duration, or modify an existing mortality table
- Reflect relationships among issue ages, durations, underwriting classes/eras
- Allows the actuary to increase credibility by pooling cells with too few lives
- Reflect known changes in underwriting, markets, regulation, etc.
* Expense: changing expenses can affect allocations between new and existing business
- Consistency is best
- In Canada, the Insurance Companies Act requires Board approval of the allocation method and an annual opinion on whether the method is fair/equitable
* Investment: different insurers have different philosophies for distinguishing investment experience factor classes
- May be influenced by market interest rate movements

[^0]
[^0]:    ${ }^{33}$ The author does not explain how to go about this, but presumably you would recalculate the EP with updated assumptions. This would help levelize the effect of changing experience over the life of the policy.

## Page 82
- Effect on regulatory/statutory liabilities
- Dividends not taken in cash (e.g. PUAs) will remain on the insurer's book balance sheet as liabilities
- In the US, insurers hold a liability for the amount of dividends declared for the next year
- Reflection of future dividends (beyond the next year)
* Ignored in US statutory reserves but are reflected in Canadian statutory liabilities
* Should be reflected in asset adequacy testing


# Case Studies In Increasing Or Decreasing the Dividend Scale 

## Mixed Experience

Example of a scenario involved mixed recent experience during/after a pandemic:

- Steadily rising portfolio earned rate due to rising yields
- Temporary mortality spike at older ages, then return to normal
- Uncertainty about "long covid" effects on future mortality
- No change on persistency
- Future expenses likely to rise
- Steady surplus ratios
- Some competitors have increased dividend scales

Decision by the insurer's actuary and management:

- Don't change mortality or expense components of the dividend scale
- Use part of the investment experience gains to cover possible rising mortality and expense costs

Actuary should confirm that the revised scale does not cause any problems with:

- Self-support tests
- Asset adequacy analysis
- Internal procedural diligence requirements

Final actions:

- Actuary writes a report
- Board approves the change

## Page 83
- Admin and new business systems are updated/tested
- Announcements are made to the field force and public


# Deteriorating Experience 

Another possible pandemic scenario:

- Insurer's earnings have been flat to decreasing
- Portfolio earned rate has been falling
- Pandemic mortality temporarily spiked at older ages and also ages 25-34 at durations $11-15$
- Uncertainty about "long covid" effects on future mortality
- No change on persistency
- Future expenses likely to rise
- Surplus ratios have fallen slightly but are still adequate
- No changes in competitors' dividend scales
- Field force opposes a reduction in dividend scale

Decision by the insurer's actuary and management:

- Don't change mortality or expense components of the dividend scale
- Increasing the mortality charge for the "problem point" at ages 25-34, durations 1115 is not a good idea because it would unfairly penalize future policies that pass into those age/duration ranges
- Lower the investment component by 15 bps
- Management decides it's too late to use pegging but recommends substitution for policies issued in the last 2 years

Final actions are the same as the previous scenario

## Par Business Issued by Stock Life Insurance Companies

While most par business is issued by mutual companies, 4 "historical situations" have resulted in stock companies with par business:

1. Par business issued back in the days before other forms of nonguaranteed life insurance was available
2. Demutualizations - when mutual companies convert to stock companies, existing par business continues to receive dividends using a "closed block" mechanism

## Page 84
- Closed block mechanism - a formal dividend protection mechanism created as part of a conversion of a mutual insurer to be a stock insurer (must be formally approved by the regulator $)^{34}$

3. Some demutualized insurers continue selling new par policies
4. Conversions of mutual companies to a mutual insurance holding company structure

- Functionally the same as converting to a stock company
- Closed block mechanisms were used to protect existing par policyholders' dividends

Other organizations that issue par business: fraternal benefit organizations, not-for-profits, and charities

# Different Perspectives Of "Fair and Equitable" 

People have different views of what "fair and equitable" means, so the Board and the actuary should have a clear concept of what they believe is appropriate

## Unconstrained perspective is fundamentally retrospective

From simplest (most unconstrained) to more complicated/constrained:

1. Purely retrospective approach - return some portion of earnings based on how various business classes contributed to earnings
2. Variation of No. 1 - return historical earnings reduced by risk charges based on the risks taken by each product line
3. Contribution Principle - dividends are based not only on past earnings but also future risk (allocate smaller dividends to classes with higher future uncertainty)

Perspective may be broadened to improve the ability of the insurer to serve the public
If a dividend scale does not remain attractive, the healthiest lives will leave
Insurers may face pressure to change (or not change) a scale due to:

- Competition
- Consistency with new business
- Sustainability of the dividend scale given future expectations for experience
- Policyholder expectations
- This is a required consideration for "fair and equitable" in Canada
- Avoidance of losses that would result from policyholder or agent reactions
- Regulation expectations
- Complexity vs. practicality

[^0]
[^0]:    ${ }^{34}$ This definition appears later in the article, but it's helpful to include it here.

## Page 85
# Perspective may be broadened to consider external challenges 

- External challenges that may affect the decision to change a dividend scale
- Sales illustrations vs illustrations of current dividend scale
- Competition (especially if NB is tied to the dividend scale)
- Financial reporting and ratings
- Litigation
- Perceptions by policyholders that prior illustrations were prospective estimates/promises
- External environment
- Some constraints on how/when a dividend scale is revised:
- Regulator interrogatories related to illustrations and policyholder treatment
- Problems that aren't addressed soon may only get worse in future years
- Investors who stand to gain or lose if a dividend scale is changed
- The strongest defenses against complaints about the insurer's dividend actions:
- Consistent and documented dividend framework based on the contribution principle to allocate dividends equitably
- Well-documented actions of the Board, taking into account the considerations above


## Perspective may need to consider the special circumstances of a Closed Block

- A demutualized insurer will likely have discretion to manage the dividend scale to reflect emerging experience or avoid a tontine ${ }^{35}$
- After demutualization, emphasis shifts away from reflecting the insurer's long-term emerging experience toward a more specific formula designed to "pay out the last dollar to the last policy" (avoid tontines, etc.)
- The closed block dividend scale should be simplified
- Make revisions to the aggregate dividend scale rather than refinements within the scale
- Could use a uniform factor applied across all cells that maintains the original relativity of dividends
- Disconnect the closed block scale from the NB scale so that the closed block scale can remain simple and unaffected by competitive pressure

[^0]
[^0]:    ${ }^{35}$ A tontine occurs when the final surviving policyholders receive a larger dividend payout because surplus was not distributed as well as it should have been along the way.

## Page 86
- Updating sophisticated closed block scales does not benefit management or shareholders $^{36}$


# Other Considerations 

This section of the paper lists "other considerations beyond the scope of this paper." By that, the author means that he is not going into any more detail about these topics than what he includes in the paper. However, since the information below is in the paper, it is fair game to be tested at the level of detail shown.

## - Authority of Board

- Court decisions - The Board's authority to distribute aggregate surplus has been determined by NY court decisions that give that authority to the Board rather than policyholders
- Revised targets - The actuary may revise earnings targets based on evolving required capital or target retained surplus
* Should be documented if targets change from one generation to the next


## - Actuary's Responsibility

- Dividend Actuary - guidance is provided by ASOP 15 (Allocation of Dividends) and ASOP 24 (Illustration of Dividends)
- Written Report - prepared by the dividend actuary pursuant to US ASOPs 15 and 41 or Canadian SoP subsection 2720


## - Experience Reflected

## - Investment Income

* Allocation methods: portfolio method, investment year method, investment generation method, investment segment method
* Treatment of policy loans - direct recognition at individual policy level vs. pooled with non-loaned assets, fixed interest rate vs. variable loan rates
- Reinsurance - how to reflect the impact of reinsurance
- Taxes - how to reflect taxes that aren't directly tied to a policy or that do not relate to current gains or current premiums
- Miscellaneous Gains - gains from outside the basic policy (e.g. riders, other LOBs, subsidiaries, etc.) or gains that are "borrowed" from another LOB


## - Special Situations

- Revised Blocks - subdivided blocks of business that have amended premiums, CSVs, or new underwriting classes

[^0]
[^0]:    ${ }^{36}$ You will "not [receive] thanks from those individuals who benefit from increased dividends, but [you will receive] some complaints from those individuals who are disappointed by reduced dividends."

## Page 87
- Acquired Blocks - pooling experience factor classes vs. recognizing different credibility levels
- Demutualizations - dividend protection mechanisms and allocation of any compensation paid upon the conversion


# - Complement to Annual Dividends 

- Terminal Dividends - a pattern of fixed dividends varying by policy year to be paid on surrender or death
* Established at policy issue to be distinct from a simple pro-rata share of the annual dividend
* Reflect the release of retained surplus at termination


## Other Forms Of Nonguaranteed Elements

The following are alternatives to par contracts:

- Indeterminate premium life insurance or guaranteed renewable disability insurance
- Discretionary credited rates that can exceed guaranteed rates on account values
- Discretionary COI charges that are lower than the guaranteed max rates
- Variable investment performance on variable or unit-linked products
- Limiting the insured period, followed by a renewable period where the insurer can adjust contract terms