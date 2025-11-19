_Note: Source document was split into 3 OCR chunks (pages 1-23, pages 24-46, pages 47-65) to stay within token limits._

# TIA_LPM_DSM_SecC_F2024-v1

## Page 1
# Section C 

C.1. Reinsurance ..... 2
Tiller Ch. 4: Basic Methods of Reinsurance ..... 3
Tiller Ch. 5: Advanced Methods of Reinsurance ..... 16
Tiller Ch. 6: Assumption ..... 31
Tiller Ch. 7: Reinsurance of In-Force Risks ..... 41
Tiller Ch. 9: Risk Transfer Considerations ..... 52
Tiller Ch. 17: Non-Proportional Reinsurance ..... 57
LPM-160: Strategic Reinsurance and Insurance ..... 62

## Page 2
# Section C. 1 

## Reinsurance Topics

## Page 3
# Tiller Ch. 4: Basic Methods of Reinsurance 

Source Author: Tiller and Tiller, 4th ed. (2015)

## Overview of This Reading

This chapter covers 3 basic methods used to reinsure ongoing new business (called "traditional reinsurance")

The first half of the chapter describes the methods, and the second half shows comparative examples for each method

The detailed study manual focuses on the verbal description of each method, while the video lesson contains side-by-side numerical examples to better illustrate key differences and also similarities in the 3 methods

## Key topics for the exam include:

1. YRT reinsurance

- Risks transfered to reinsurer
- Calculation of ceded net amount at risk
- YRT retention determination methods
- Determination of ceded reserve credit
- Product-specific simplifications
- Aspects of YRT premium scales
- How to calculate YRT reinsurance premium
- Uses for YRT and comparison with coinsurance

2. Coinsurance

- Risks transfered to reinsurer
- Calculation of coinsurance premiums and allowances
- Uses of coinsurance
- Other considerations: policyholder dividends, policy loans, and premium taxes
- Treatment of deficiency reserves compared to YRT reinsurance

3. Modified coinsurance

- Compare with coinsurance
- Calculation of mod-co adjustment
- Defining the mod-co interest rate
- Uses, advantages, and disadvantages of mod-co

## Page 4
# Introduction to Traditional Reinsurance 

Traditional reinsurance can be issued on an automatic or facultative basis and can be proportional or non-proportional

Automatic vs. facultative is not defined in Ch. 4. Automatic means the reinsurer automatically accepts each policy, while facultative means the reinsurer can individually underwrite and select specific policies.

Proportional is not directly defined in this chapter, but it essentially means the reinsurer assumes a \% of each risk included in the reinsurance agreement. All of the methods and examples in Ch. 4 assume proportional. Non-proportional will be covered in Ch. 17.

## Yearly Renewable Term (YRT) Reinsurance Overview of YRT

Under YRT reinsurance, the ceding company reinsures mortality or morbidity risk only
The ceding company retains responsibility for:

1. All Liabilities - Unearned YRT Premiums - Unpaid Reinsurance Claims
2. Payment of everything not covered by the reinsurance (surrender values, dividends, commissions, and other expenses)

The YRT reinsurance premiums are NOT directly related to the premium rates of the original plan of insurance

The reinsured amount is based on the net amount at risk (NAR), not the gross face of the policy

- $\mathrm{NAR}=$ Face - Terminal Reserve $\left({ }_{t} V_{x}\right)$
- But in practice, it can be based on anything the companies agree on
- NAR is usually calculated exactly by policy unless treaty says otherwise
- Ignore deficiency reserves, additional reserves, and rider reserves in the calculation
- NAR affects both YRT premiums and the amount of DB reinsured on death
- DB paid on death $=$ Reserve released + ceding company's share of NAR + reinsurer's share of NAR


## Important Points Regarding NAR

1. Companies must agree on the method
2. Ensure that the benefit amount used in premium calculation $=$ benefit amount paid on death
3. Document the agreed process clearly in the reinsurance treaty
4. NAR used should be reasonably close to the actual NAR

## Page 5
# YRT Retention Determination Methods 

## 1. Pro Rata

- Original proportional method
- Preferred for most YRT arrangements
- Ceding company retains a constant $\%$ of the NAR and reinsurer holds a constant $\%$ of the risk
- Reinsured $\%=\frac{\text { Original Face Amount Ceded }}{\text { Total Original Face Amount of Policy }}$
- Results in very small reinsurance amounts in later durations (when NAR is very small)
- Quota share reinsurance - every policy is reinsured by the same \%
- With a general pro rata method, the \%s may vary by policy with face amount and initial retention


## 2. Level or Constant Retention

- Company retains a fixed amount of the NAR
- Any decrease in NAR is allocated to the reinsured portion
- Causes the reinsured NAR to decrease more rapidly than pro rata method
- Once NAR < constant retained amount, there is no more reinsurance
- Technically this is also a proportional method since the NAR can be determined in advance

3. Constant Risk Reinsured (rare)

- Reinsured amount $=$ constant amount
- Ceding company absorbs the reduction in NAR
- Once NAR < constant amount reinsured, the NAR is reinsured 100\% (nothing retained)


## 4. Formula Retention

- NAR and retention are determined by initially agreed upon formula

## Page 6
# Rentention Examples 

Suppose the following for a single policy:

- Face amount $=1$ million
- 10th year terminal reserve $=55,000$
- Initial reinsured amount $=900,000$

At the end of year 10, NAR $=1,000,000-55,000=945,000$

- Pro Rata Reinsured Amount $=\frac{900,000}{1,000,000} \times 945,000=850,500$
- Level Retention Reinsured Amount $=945,000-100,000=845,000$
- Company will always retain exactly $1,000,000-900,000=100,000$ while NAR $<$ 100,000
- Once NAR $<100,000$, the company will retain $100 \%$ of the NAR
- Constant Risk Reinsured Amount = exactly 900,000 while NAR $>900,000$
- After NAR $<900,000$, reinsured amount $=$ NAR

YRT reinsurance is generally simpler and cheaper than other forms of reinsurance

- YRT involves less overall risk and requires less capital than other forms (helps make YRT cheaper)
- Historically, the administrative ease of YRT gave it a big advantage over other forms, but technology has made this less of an advantage

Ceded Reserve Credit $=$ Unearned Net Valuation Premium for benefit amount reinsured

## Product-Specific Simplifications

These were more common on older treaties before advances in system technology

## 1. Level Premium Term

- If underlying terminal reserves are close to zero, set NAR $=$ Face
- Includes ART and other renewable term products


## 2. Decreasing Term

- NAR may decrease following the pro rata method, leaving the ceding company with little risk and profit
- Ceding company may keep a level retention to pass all NAR decrease to reinsurer


## 3. Whole Life Insurance

- WL typically uses pro rata method based on \% of original amount reinsured - same $\%$ of terminal reserve

Reinsured Amount $=$ Original Reinsured $\% \times($ Face - Terminal Reserve $)$

## Page 7
# 4. Universal Life 

- Pro rata and level retention methods are common
- Option 1 UL works much like WL for reinsurance purposes (declining NAR)
- Option 2 often uses the pro rata method (constant $\%$ of face since NAR = Face on an option 2 policy)
- If a policy's NAR increases to comply with IRC Section 7702, the treaty should spell out how this will be handled; otherwise, the ceding company must absorb it

5. Variable Life - treated the same as UL

## YRT Premium Scale

## YRT premium rates $=\%$ of a mortality table or a $\%$ of a company's COI rates

- Usually vary by age, duration, sex, underwriting class, and sometimes policy size
- YRT rates are usually unique to each ceding company
- Select period of 15 years is common to reflect lower mortality on underwritten lives (could also be 20 or 25 years)

Annual cession fee - may also be charged by the reinsurer to cover maintenance expenses
Becoming rarer since admin is more automated
Zero first-year YRT premium (ZFT) - common for YRT premium to be zero first-year
Effectively a first-year allowance $=$ first-year YRT premium

## Cost-benefit tradeoff considerations

- Use of bonuses, ZFT, and experience refunds will increase YRT premiums since reinsurer has to fund those
- Bonuses (persistency and production) and experience refunds are rare today
- Cession fees will lower YRT premiums since the reinsurer is collecting more in fees


## Policy year vs. calendar year YRT scales:

- Policy year is the most popular
- Calendar year avoids the reinsurer having to set up any reserve at year-end
- YRT terminal reserves $=0$


## YRT Rate Guarantees and Increases

YRT treaties often state that YRT rates will not exceed the valuation net premium

1. Avoids reinsurer having to establish premium deficiency reserves

## Page 8
2. Provides reinsurer flexibility in future premiums

# YRT Reinsurance Premium Calculation 

General formula:

$$
\begin{aligned}
\text { ReinsPrem } & =\text { YRT Rate } \times \frac{\text { Ceded NAR }}{1000} \\
\text { YRT Rate } & =\text { rate charged by reinsurer on a per } 1000 \text { basis }
\end{aligned}
$$

Other adjustments to the premium:

- Cession fee (if any) is added to reinsurance premium
- Substandard ratings
- Substandard table extra premium
- Increase basic YRT rate by a multiple
- Multiple increases $25 \%$ for each rating ( $125 \%, 150 \%, 200 \%, \ldots$ )
- Rating may be removed in later years if based on new underwriting evidence
- Substandard flat extra premium for 5 years or more
- 75-85\% coinsurance allowance on the extra premium in the first year
- $10-15 \%$ in renewal years
- Substandard flat extra premium for less than 5 years
- 10-15\% coinsurance allowance on the extra premium in all years
- Riders
- Waiver of premium and other ancillary benefits
- 75-85\% coinsurance allowance on the extra premium in the first year
- $10-15 \%$ in renewal years
- Accidental death benefit
- Flat YRT rate all ages and durations
- ADB is usually reinsured on a bulk basis using a separate treaty
- Term life riders
- Usually use the base policy YRT rates (but not always)
- Critical illness riders (usually priced separately)
- Monthly renewable term (MRT) for UL
- Operates in the same manner as YRT
- MRT rate is the same for 12 months, then changes on anniversary

## Page 9
- NAR changes monthly
- Major difference with YRT: unearned reinsurance premium is based on monthly premium and reserve credit is reduced proportionally
- If MRT premium is charged in arrears (EOM), ceded reserve credit $=0$


# Uses of YRT 

Generally used for WL, UL, and term life

- Traditionally was not used for term, but has become popular because of alternative capital solutions

YRT is the best choice when the primary objective is the transfer of mortality risk
Can also be used for disability income, LTCI, and critical illness
Not good for annuities

## Other Considerations for YRT

Reinsurers may have a lower profit objective for YRT
Does not provide much opportunity for profits from investment risk, persistency risk, or cash surrender risk

Generally, the ceding company gets little surplus relief from YRT

- YRT transfers only the C-2 (mortality and morbidity) component of the ceding company's risk based capital
- Ceding company could negotiate ZFT scale or even a first year allowance, but this will increase the cost of YRT premiums


## Coinsurance

## Overview of Coinsurance

With coinsurance, the key word is proportionate

- Reinsurer receives proportionate share of gross premium
- Reinsurer sets up a proportionate share of the reserve
- Reinsure reimburses ceding company its proportionate share of death and surrender benefits

Expense allowance - amount paid by reinsurer for commissions and other expenses incurred on the ceded portion

- May not cover all actual expenses $\Rightarrow$ ceding company should set up liability for any shortfall

## Page 10
- Expressed as a \% of ceded premium

Ceding company is still responsible for setting up reserve and paying death benefits, surrender benefits, dividends, commissions, expenses, etc.

In other words, the ceding company is still the one facing the policyholder, but the ceding company is reimbursed by the reinsurer for reinsurer's share

Compared to YRT, coinsurance is more complex to administer

- More complicated expense allowances
- Reinsurer must track ceding company's reserves
- Must track and reimburse cash surrender benefits


# Coinsurance Premiums and Allowances 

In the simplest case, the coinsurance premium is simply the $\%$ of the GP corresponding to the $\%$ of face amount ceded

$$
\text { ReinsPrem }=(\text { Amount Ceded Per 1000 }) \times(\text { GP Per 1000 })
$$

Sometimes, however, coinsurance uses banded premiums, and there are several approaches:

- Simplest banding approach: Base reinsurance on GP actually paid but use common set of allowances for all bands
- More complicated but more equitable approach: Base reinsurance premium on GP actually paid and vary the coinsurance allowances by band
- Base reinsurance premium on a specified band of premium rates regardless of the size of the policy
- Usually use the highest band
- One set of allowances for all sizes
- If use highest band, creates additional margin for ceding company of policies in lower bands


## Policy fee treatment can vary

- Sometimes reinsurer allows ceding company to retain entire policy fee paid by policyholder
- With many treaties the policy fee is coinsured and the reinsure pays a $100 \%$ allowance on it (netting the cash impact back to zero)
- Allows reinsurer's portion of policy fee to be included in reinsurer's deficiency reserve calculation


## Coinsurance allowances may vary

- Reinsurer's assumptions and profit objectives will rarely be the same as ceding company's

## Page 11
- Reinsurer may specify a different set of allowances by sex, underwriting class (risk classification), and/or age


# Changes in reinsurance premiums 

- Indeterminate and non-guaranteed premiums - reinsurer may retain the right to recalculate coinsurance premiums if direct premium changes
- For other situations where the reinsurer changes premiums, the ceding company may have a provision to also change the allowances to keep the same net cash flow or even recapture the business

Other provisions that can exist but are less common today:

- Experience refunds - if present, the coinsurance premiums will be higher
- Chargeback provisions - requires return of excess allowances for policies that lapse early
- Persistency and production bonuses paid to ceding company - difficult to monitor in practice


## Coinsurance Premium and Allowance Calculations

With coinsurance, the reinsurer develops unique allowances for each product
Reinsurance premiums are paid annually regardless of policyholder premium mode
Substandard and rider methods are essentially the same as those for YRT reinsurance (see p. C8)

- Typically allowances on substandard are the same as standard


## Uses of Coinsurance

Can be used for any type of insurance-life, disability, medical, or annuity
Traditionally, has been the most common for term life, which has little or no cash value, and therefore minimal investment risk

Also useful for cash value products where the ceding company wants to pass investment risk to reinsurer

The reinsurer shares risks due to:

- Mortality or morbidity risk
- Lapse and cash surrenders
- Investment risks
- Surplus strain of new business

## Page 12
# Policyholder Dividends 

Historically reinsurers usually did not share in policyholder dividends
If a large portion of a par block is ceded and reinsurer does not share in policyholder dividends, it may be difficult for the ceding company to earn enough on the retained assets to fund policyholder dividends

Methods for reflecting policyholder dividends:

- No direct sharing in policyholder dividends, but reinsurer pays a higher allowance than it would otherwise
- Reinsurer may participate in a current dividend scale but not in any future revisions
- Reinsurer may participate in revisions to scale subject to negotiations
- New York only: NY Reg 102 requires reinsurer to participate proportionately in policyholder dividends, including any changes to dividend scales if reinsurance reserve credit taken by ceding company


## Other Coinsurance Considerations

Policy loans - reinsurers do not participate in policy loans

- Automatic premium loans have no impact on reinsurance premium either

Premium taxes - Reinsurer does NOT pay a premium tax on reinsurance premium directly to states

Historically, reinsurers reimburse company for premium tax on reinsurance premium in 1 of 3 ways:

1. Most common: reinsurer includes a provision in the basic allowance (instead of paying it separately)
2. Pay exact amount - tedious and creates uncertainty for reinsurer
3. Pay a fixed percentage (e.g. $2.0 \%$ ) as a proxy

Reserve credit - if reinsurer is admitted or accredited in ceding companys state of domicile, the ceding company can reduce its required reserves through a reinsurance reserve credit

- Very important benefit for ceding company
- Ceding company's net liability on balance sheet $=$ Liability before reinsurance - reserve credit


## Nonforfeiture statuses

- RPU: adjust ceded amount proportionally to reflect reduced face
- ETI: reinsurance continues for the term of the policy without any more reinsurance premium

## Page 13
- If nonforfeiture benefit is small, the reinsurer may pay the equivalent cash surrender value to ceding company and have no further liability

Deficiency reserves - unlike YRT, coinsurance passes the proportionate share of deficiency reserves to the reinsurer as well

# Modified Coinsurance (Mod-Co) 

## Overview of Mod-Co

Mod-co is identical to coinsurance in virtually all ways except that

1. Ceding company retains the assets and reserves for the ceded portion
2. Reinsurer pays a mod-co adjustment, which is the increase in the ceded reserve less a credit for investment income (since the reinsurer does not hold the assets)

The entire reserve (and associated assets) appear on the ceding company's balance sheet

- No reserve credit shown

All of the reinsurer's participation in asset performance is recognized through the mod-co adjustment

Mod-co allows the ceding company to control how the assets backing the ceded reserves are invested/managed

## Origins of Mod-Co

Mod-co was originally created for situations where the ceding company was not allowed to take reserve credits from foreign and non-admitted reinsurers

Other reasons mod-co remained popular:

- Ceding companies believed they could get better returns on assets if they controlled them
- Ceding companies benefited from capital gains on assets
- Good for policyholder dividends where the reinsurer didn't participate since the ceding company could manage a common pool of assets
- Ceding company would have more assets available for policy loans (remember that reinsurers do not participate in loans)


## Mod-Co Premiums and Allowances

Very similar to coinsurance-all of the info covered earlier on allowances, premiums (banding, etc.) applies to mod-co as well

Any differences with coinsurance would result from

1. Different tax treatment

## Page 14
2. Differences in the investment income assumption of the reinsurer on coinsurance and the interest rate used in the mod-co reserve adjustment

# Mod-Co Reserve Adjustment 

The mod-co adjustment is paid by the reinsurer to the ceding company

- If it's positive, the reinsurer owes it to the ceding company
- If negative, the ceding company owes it to the reinsurer

Mod-co adjustment $=$
Ending ceded reserves

- Beginning ceded stat reserves
- "Interest" on beginning ceded reserves

To the extent that the mod-co interest rate is different from rate earned on the ceding company's assets, mod-co will result in different financial results

- If the mod-co interest rate $=$ ceding company's earned rate, the net income effect would be identical to coinsurance
- If the mod-co interest rate is higher than the ceding company's earned rate, the ceding company's income would be lower under mod-co than coinsurance

The mod-co interest rate is defined in the reinsurance treaty (very important)

- Intended to allow the reinsurer to participate in the total performance of the assets backing the ceded reserves
- Includes effects of asset defaults, capital gains/losses, timing risks, and investment income
- Not a simple interest rate-in reality it is "a sum of money representing a total investment return"
- The NAIC's Credit for Reinsurance Model Regulation and the NAIC's Life and Health Reinsurance Agreements Model Regulation now govern requirements for reserve credits and serve as the basis for the mod-co interest rate
- Traditionally, the mod-co interest rate was defined in terms of the ceding company's portfolio rate, its new money rate, an outside index, or just a fixed rate

For illustration purposes later in the chapter, the simple fixed rate approach is used, and it's the most likely to be used in an exam problem because it's actually feasible to work out with an SOA-approved calculator. This is demonstrated in the video lesson as well.

Statutory reserves are used as the reserve basis

## Page 15
# Uses of Mod-Co 

1. Used primarily to reinsure products that develop cash values or have significant asset risks
2. Allows ceding company to retain control of investments while getting surplus relief of coinsurance (especially good if reinsurer is unauthorized)

- Especially good for interest-sensitive products with a crediting rate tied to asset performance

3. In the past, mod-co had tax advantages over coinsurance, but have these have been eliminated from tax code
4. Used today when the reinsurer is an offshore, unauthorized company or to provide reinsurance involving deficiency and additional reserves mandated by Regulation XXX

## Other Advantages and Disadvantages of Mod-Co

## Mod-co eliminates some problems with coinsurance

- No question about reserve credits
- Eliminates problem of reinsurer not participating in policy loans since ceding company holds all assets
- Allows ceding company more control over investments
- Allows the ceding company to maintain a higher level of assets $\Rightarrow$ attain a higher comparative asset ranking than with coinsurance

Mod-co's main drawback: more complicated to administer than coinsurance because of the reserve adjustment calculation

## Comparative Models

Starting on p. 83 of the Tiller book, they begin showing examples of the 3 types of basic reinsurance covered in Ch. 4. These are very good examples to review, but there are some pitfalls to be aware of:

- Don't spend too much time trying to reproduce the "before reinsurance" financial statements from the first principles values given. It is much more important to focus on the reinsurance aspects.
- From a practical perspective, it is very difficult to compare all of the tables without literally tearing the pages of the book out and lining them up side by side. Don't over-spend study time going in circles.
- All of the examples omit a very important aspect of basic reinsurance, which is how each method treats ceded death claims and ceded surrender benefits. The examples assume no deaths or surrenders.

The video lesson addresses all of the points above with a TIA-unique example that helps "surface" key patterns that are difficult to see in the text.

## Page 16
# Tiller Ch. 5: Advanced Methods of Reinsurance 

Source Author: Tiller and Tiller, 4th ed. (2015)

## Advanced Methods

## Overview of This Reading

Most of Ch. 5 contains additional variants of coinsurance that are used in more of a "financial" context, where the primary objective is surplus relief or using reinsurance to raise capital

As with Ch. 4, the differences and similarities with the Ch. 5 methods are best learned through examples, and that is the focus of the video lesson

The last section of Ch. 5 beginning on Tiller p. 150 covers alternative reinsurance structures and focuses on special purpose vehicles (SPVs)

## Key topics for the exam include:

- Advantages of advanced forms of reinsurance
- Coinsurance and mod-co
- Be able to compare and contrast with each other
- Calculation of the "reinsurance report"
- Calculation of the outstanding surplus account
- Funds withheld coinsurance
- Compare and contrast with coinsurance and mod-co
- Calculation of the funds withheld balance
- Funds withheld mod-co
- Compare and contrast with coinsurance, mod-co, and funds withheld coinsurance
- Calculation of the funds withheld balance
- Partially modified coinsurance
- Contrast mechanics with other forms of coinsurance
- Advantages and disadvantages
- Alternative reinsurance structures: SPVs
- Purpose of SPVs
- Typical SPV model
- Objectives of sponsors and investors
- Use of LOCs vs. bonds
- General considerations for alternative reinsurance structures

## Page 17
# Overview of Advanced Reinsurance 

Advanced uses of reinsurance are intended to provide surplus relief and reduce the amount of assets the ceding company must transfer to the reinsurer

1. Allows ceded reserve credit for reinsurers not admitted in ceding company's domicile jurisdiction
2. Improves ceded reserve credit security by retaining assets with the ceding company
3. Coordinates asset management when the risks reinsured are highly asset sensitive
4. Minimizes capital gains/losses on assets at initiation of the reinsurance
5. Allows easy recapture of reinsurance by minimizing capital gains and losses

Most advanced methods take on the form of coinsurance, mod-co, or partially modified coinsurance (part-co)

YRT is generally not used for surplus management because it provides little earnings and surplus relief

- Exceptions:
- YRT may provide more earnings help for products that are also YRT
- YRT can significantly reduce the ceding company's C-2 required capital for "mortality-centered" products

In Ch. 5, the authors essentially ignore uses of YRT beyond what was covered in Ch. 4 and instead focus on coinsurance, mod-co, and part-co-all of which are covered in examples.

Special purpose vehicle (SPV) - entity that provides outside funding to an insurer for "highly remote risks" like assuming redundant capital XXX reserves, etc.

- These are covered in several sections at the end of the Ch. 5 material (p. C-26 of the detailed study manual).


## Terminology

In-force block - an existing block of business made up of policies issued in the past (with mixed issue dates)

- The authors focus more on in-force blocks in Ch. 5, whereas Ch. 4 methods mainly apply to individual new issues (but either set of methods can be used for in-force or new business)

Initial premium (or initial consideration) - usually equals ceded stat reserves
Renewal reinsurance premium - ceded portion of renewal premium paid after inception
Initial allowance - ceding company's pre-tax stat gain at inception

- Effectively the price paid by the reinsurer to assume its share

## Page 18
- This is essentially a large upfront expense allowance from the reinsurer that creates additional surplus for the ceding company
- It also forms the reinsurer's initial investment in the ceding company-much more later

Renewal allowance - expense allowance paid by reinsurer after inception (intended to defray renewal commissions, maintenance expenses, etc.)

Experience refund - mechanism to share some of reinsurer's stat profits back to the ceding company

- Usually not paid until outstanding surplus account has been fully repaid to reinsurer

Risk charge - profit charge by paid ceding company to reinsurer each period

- Assessed as a \% of the outstanding surplus account

Outstanding surplus account - tracks the repayment of the reinsurer's remaining investment each period

# Advanced Methods of Reinsurance 

Beginning on p. 113 of the Tiller book, the authors begin addressing each of the following 5 variations of coinsurance using a comparative example based on a SPDA reinsured at $100 \%$.

1. Coinsurance
2. Modified Coinsurance
3. Funds Withheld Coinsurance
4. Funds Withheld Modified Coinsurance
5. Partially Modified Coinsurance

All of the caveats I mentioned about the examples in Ch. 4 also apply here-arguably more since the methods become increasingly abstract. It is much easier to understand the key differences by comparing the results of each method side-by-side, and that is the focus of the video lesson.

The detailed study manual below focuses on the description of each method and generic formulas. Your head is going to hurt by the time you get to the end of Ch. 5. I would prioritize understanding coinsurance, mod-co, and funds withheld coinsurance first. The other two methods are built from those and really just involve more tedium.

## Coinsurance and Mod-Co

The coinsurance mod-co mechanics in Ch. 5 are identical to those demonstrated in Ch. 4
The primary difference in more of "surplus relief" application is that there is more emphasis on tracking the reinsurer's investment in the ceding company using the outstanding surplus account (OSA), which is like a fancy loan from the reinsurer the ceding company that is repaid through experience and risk charges

$$
\mathrm{OSA}_{t}=\mathrm{OSA}_{t-1}+\operatorname{StatGain}_{t}-i \times \mathrm{OSA}_{t-1}-\text { RiskCharge }_{t}
$$

## Page 19
where:

- StatGain $=$ reinsurer's gain from operations (i.e. reinsurer's profit)
- $i \times \mathrm{OSA}_{t-1}=$ investment income on the beginning OSA
- Think of this as investment income "lost" by the reinsurer since they extended that capital to the ceding company-therefore the ceding company owes this to the reinsurer
- RiskCharge $=$ a percentage (e.g. $3 \%$ ) $\times$ beginning OSA (i.e. $\mathrm{OSA}_{t-1}$ )

The OSA is from the reinsurer's perspective, so it's tracked as a negative amount

- Initial OSA = reinsurer's first year stat gain, which will negative due to the first year allowance paid to the ceding company

In subsequent periods, the OSA is reduced by positive stat gains and increased by the investment income rate and risk charge rate

Again, think of the OSA as a fancy loan from the reinsurer to ceding company. The investment income and risk charge components are like interest rate charges owed to the reinsurer. The stat gains are how the "loan" gets repaid.

The Tiller book also shows a "reinsurance report" for each example-this is simply a cash flow report that shows how much cash the ceding company owes the reinsurer

# Net Cash Due to Reinsurer $=$ 

Ceded premium

- Allowances
- Ceded benefits
- Mod-co adjustment (if using mod-co)
- Experience refund (if any)

FAQ: Where's the risk charge? Answer: In the coinsurance and mod-co examples, the Tiller book assumes the risk charge is paid implicitly in the OSA. Like the investment income owed on the OSA each period, the risk charge serves to prolong the OSA payback. They make a different assumption for funds withheld agreements, as we will see later.

## Mod-Co vs. Coinsurance

As discussed in Ch. 4, the chief advantage of mod-co is that it allows the ceding company to maintain the assets backing ceded reserves

- Especially ideal if ceding company would like to recapture the business at some point (no need to move assets twice since they never moved to reinsurer initially)

Mod-co is a popular way of reinsuring inforce blocks

## Things coinsurance and mod-co have in common:

1. Initial reinsurance premium $=$ ceded reserves

## Page 20
2. Renewal reinsurance premiums $=$ ceded $\%$ of gross premiums (same as Ch. 4)
3. Initial allowance $=$ pre-tax price incurred by reinsurer excluding required capital

- This is the first-year gain for the ceding company and the first year stat loss for the reinsurer
- This is also the starting point for the OSA

4. Renewal allowances cover ceding company expenses and may even provide a small profit margin to the ceding company
5. Experience refunds and OSA may be used to share profits or to define recapture pricing

Even though the above points are listed in the mod-co section of the chapter, they are true of all other forms of advanced reinsurance covered in this chapter. Other methods we will cover differ only in how the logistics of cash payments are handled and how things are shown on income statements and balance sheets.

## Page 21
# Simple Example: Coinsurance vs. Mod-Co 

Suppose Company CCC cedes $80 \%$ of an inforce block with gross reserves of 100 million to Company RRR, and suppose RRR agrees to pay a $10 \%$ first year allowance.

## If coinsurance:

- Initial premium $=80 \mathrm{M}$
- Initial allowance $=8 \mathrm{M}$
- CCC's gain at inception $=8 \mathrm{M}$ $=80 \mathrm{M}$ reserve credit +8 M allowance -80 M initial premium paid
- RRR's loss at inception $=-8 \mathrm{M}$ $=80 \mathrm{M}$ initial premium received -8 M allowance paid -80 M reserve increase


## If mod-co:

- Initial premium $=80 \mathrm{M}$
- Initial allowance $=8 \mathrm{M}$
- CCC's gain at inception $=8 \mathrm{M}$ $=80 \mathrm{M}$ mod-co adj received +8 M allowance -80 M initial premium paid
- RRR's loss at inception $=-8 \mathrm{M}$ $=80 \mathrm{M}$ initial premium received -8 M allowance paid $-80 \mathrm{M}$ mod-co adj paid

As you can imagine, it would be a bit silly in the mod-co example for CCC and RRR to manually exchange the 80 M . The 80 M nets out, and only 8 M has to move from RRR to CCC. This is just another way of saying the ceding company retains the assets under modco.

The key result with both examples is that CCC has "created" 8M of additional surplus using reinsurance that it would not have otherwise. CCC has to eventually repay this to RRR using foregone earnings through the OSA (i.e. gains on the ceded business that RRR will keep), but CCC can now put this additional 8 M of capital to work for any number of other things that might also create value. Much like any business would go to a bank for a loan, this is how an insurer can use reinsurance in a financial context. It's like a fancy "payday loan"-you get a lump sum upfront but you pledge a part of your future paycheck to the lender.

## Funds Withheld Coinsurance

Funds withheld coinsurance (FW-Co) ${ }^{1}$ looks like regular coinsurance in many ways:
${ }^{1}$ Instructor's note: The abbreviations "FW-Co" and "FW-Mod-Co" are not used in the book, but I use them for shorthand, and I think it would be fine to use on the exam since it's pretty obvious what it would mean in a reinsurance exam problem context.

## Page 22
- Identical calculations of premiums, allowances, experience refunds, and risk charges
- Identical initial stat gain


# Key differences with FW-Co: 

- Ceding company retains the initial premium and reinsurer retains the initial allowance
- If allowance < initial premium (most common situation):
* Ceding company has an accounts payable liability asset
* Reinsurer has an accounts receivable asset
- If allowance > initial premium, it's the other way around (reinsurer has the payable liability)
* Alternatively, the reinsurer may actually pay the excess, the authors say, in which case the initial FW balance $=0$
- Each period, the FW balance will go up or down depending on which company owes more to the other
- Key point: No cash actually changes hands
- The FW assets and liabilities are "paper" assets and liabilities, but as they change, they impact income
- Example: if the reinsurer's receivable asset changes from 100 to 105, it creates income of 5 on the income statement (same income effect as if cash had actually been paid)
* The accounting effects are identical to concepts like changes in reserves, DAC, and other non-cash accounting items
- Reserves appear on the reinsurer's, but the assets stay with the ceding company
- Remember the ceding company retains the initial premium, which is essentially these assets
- An interest adjustment is made in the FW balance reflecting interest on assets held by ceding company


## Comparing FW-Co with coinsurance and mod-co:

|  | Coinsurance | Mod-Co | FW-Co |
| :-- | :--: | :--: | :--: |
| Reinsurer holds reserve | Yes | No | Yes |
| Ceding company takes reserve credit | Yes | No | Yes |
| Reinsurer holds assets backing ceded reserves | Yes | No | No |
| Actual assets are identified | Yes | No | Yes |
| Reinsurer owns performance of assets | Yes | No* | Yes |
| Calculate mod-co adjustment | No | Yes | No |
| Establish a FW asset or liability | No | No | Yes |

*With mod-co, the reinsurer doesn't own the assets, but they still participate in asset performance through the mod-co interest rate

## Page 23
The authors note that RBC and FIT treatment for regular coinsurance and FW-Co are the same, but mod-co is different (they don't explain how)

The "reinsurance report" concept introduced in the previous sections is the basis for the FW balance each period (since cash isn't actually changing hands under FW)

# EOY FW Balance $=$ 

BOY FW Balance

+ Ceded premium
- Allowances
- Ceded benefits
- Experience refund (if any)
- Risk charge

FAQ: Wait a second! You said the risk charge doesn't belong in the net cash calculation for coinsurance! Answer: That's correct. The Tiller book assumes that the risk charge will actually be paid in cash for FW agreements. Therefore, they back it out of the FW balance reflecting it's been paid outside of the net funds withheld due to the reinsurer. Don't get stuck on this right now. I cover it pretty well in the video lesson using an example.

## Special note on the FW ceded premium:

- The actual renewal ceded premiums for FW are no different than other forms of coinsurance already discussed (= ceded \% of gross premium)
- For accounting purposes, the Tiller book also includes investment income on the FW balance in the renewal ceded premium owed to the reinsurer

FW Renewal Ceded Prem $=$ Coinsurance Renewal Ceded Prem + Inv Income on FW Balance

- There are no specific accounting rules for how to handle the investment income owed to the reinsurer, but this ensures it's accounted for

The OSA calculation for FW is identical to coinsurance and mod-co

$$
\mathrm{OSA}_{t}=\mathrm{OSA}_{t-1}+\operatorname{StatGain}_{t}-i \times \mathrm{OSA}_{t-1}-\text { RiskCharge }_{t}
$$

However, the authors note the following alternative (and equivalent) calculation is used more in practice for FW:

$$
\begin{aligned}
\mathrm{OSA}_{t}= & \mathrm{OSA}_{t-1}+\text { CededPrem }_{t} \\
& -\text { CededBen }_{t}-\text { CededResIncr }_{t}-\text { ExperienceRefund }_{t}-\text { RiskCharge }_{t}
\end{aligned}
$$

## Funds Withheld Modified Coinsurance

FW-Mod-Co is identical to mod-co in the initial transaction

- Same initial premium, initial allowance, and initial mod-co adjustment

## Page 24
Key difference with mod-co: With FW-Mod-Co, the reinsurer retains the initial allowance

- Reinsurer sets up a FW accounts payable for initial allowance
- Ceding company sets up an equal/opposite receivable asset

Like regular FW-Co, the ceding company retains assets supporting ceded reserves
Like regular mod-co, the ceding company does not show a reserve credit on the balance sheetand the reinsurer does not show an assumed reserve

Tip: In your mind, just rename this method "allowance withheld mod-co" because that's really the effect it has on financial statements. It looks just like regular mod-co, except there's a FW balance tied only to the initial allowance that's withheld.

The FW balance now reflects the mod-co adjustment (otherwise identical to regular FW balance):

# EOY FW-Mod-Co Balance $=$ 

BOY FW Balance

+ Ceded premium
- Allowances
- Ceded benefits
- Mod-co adjustment
- Experience refund (if any)
- Risk charge

Since the initial mod-co adjustment will cancel the initial premium, the net starting FW balance under FW-Mod-Co is simply the retained initial allowance

- This means that while for a typical regular FW deal, the initial balance sheet will show a receivable for the reinsurer and a payable for the ceding company, under FW-Mod-Co, the balance sheet will usually show the opposite

The mod-co adjustment under FW-Mod-Co will generally be higher in subsequent periods compared to the mod-co adjustment under regular mod-co

- With FW-Mod-Co, the ceding company is not retaining as much assets as it would under regular mod-co
- Therefore the interest component of the mod-co adjustment is less (the mod-co interest rate isn't applied to the outstanding retained allowance because the reinsurer possesses these assets)

The OSA is calculated the same as all other forms of coinsurance

- In "textbook" cases like the one in Tiller where the mod-co interest rate $=$ earned rate assumed, the OSA will equal the FW-Mod-Co balance exactly because both start with the initial allowance and are affected by the same net activity

FW-Mod-Co may violate NAIC and state laws

## Page 25
- State laws usually require at least quarterly settlement of amounts due under reinsurance agreements
- The authors note it may be possible to get approval in specific circumstances


# Partially Modified Coinsurance (Part-Co) 

A.k.a. "co/mod-co," "split co/mod-co," and "COMB"

## Part-Co is a combination of coinsurance and mod-co

- Initial coinsurance reserve $=$ initial allowance
- Remaining reserves are reinsured on a mod-co basis
- No cash transfer at inception of treaty
- The initial allowance and mod-co adjustment owed by the reinsurer will always exactly cancel the initial premium owed by the ceding company
- In renewal years, the proportions of the coinsurance and mod-co are adjusted to minimize cash flows
- Adjustment may be scheduled in the treaty or could be allowed to float with the increase in coinsurance reserves
- Generally, as renewal profits emerge, they are used to increase the mod-co proportion and reduce the coinsurance proportion
* Essentially, the coinsurance portion is tracking the reinsurer's investment
- Some states disapprove of increases in the coinsurance $\%$ due to negative profits $\Rightarrow$ could be seen as the reinsurer not paying its share of losses


## Advantages of Part-Co

1. No initial cash transaction
2. Eliminates need for accounts receivable and accounts payable (regulators may favor it over FW for this reason)

## Disadvantages of Part-Co

1. Very complicated to administer and understand
2. "Looks and smells" like older surplus relief treaties that did not transfer risk (regulators may have concerns)
3. Requires 2 stat gain calculations

- Calculate preliminary stat gain to determine change in co/mod-co proportions
- Calculate final stat gain reflecting the new split in co/mod-co

4th disadvantage: Part-co is yet another abstract reinsurance framework to know for the exam. OK, I added this one myself. Good news (maybe): part-co has only rarely been tested numerically in all the years the Tiller material has been on the ILA syllabi.

## Page 26
I think the most intuitive way to think about part-co is to pretend you have 2 reinsurance treaties: one for the coinsurance piece and one for the mod-co piece. Ultimately that's what's really going on. The ceded reserved is reinsured by 2 different methods. If you can see things from that perspective, it's really just a matter of applying the coinsurance and mod-co mechanics covered earlier to each piece. It's just a lot of extra work since the proportions shift, as noted above.

# An Alternative Reinsurance Structure: The SPV 

This final section corresponds to pp. 150-156 of Tiller Ch. 5. SPVs are difficult to visualize if you have never encountered them before. The video lesson contains several visuals that should make it easier to commit these concepts to memory for the exam.

## Overview of SPVs

Special purpose vehicles (SPVs) are an alternative to the typical reinsurance arrangement
SPVs are typically used to fund capital requirements for extremely unlikely events or to provide capital for redundant reserves

Redundant Reserves $=$ Total Regulation $X X X$ Reserves - Economic Reserves

- Total Regulation $X X X$ reserves $=$ basic statutory reserve + additional reserves required by XXX
- Economic Reserves $=$ reserves needed to fully mature the risks reinsured without regard to statutory requirements
- Commonly equals the "net GAAP benefit reserve": BenRes - DAC
- GAAP reserves often contain PADs, so there is still some margin in the economic reserve
- Economic reserves should emerge from the cash flows and not required additional funding


## Economic Reserves + Required Capital

- Should be sufficient to fund claims and expenses with a high degree of confidence under significant adverse developments

Required capital in a SPV application $=$ minimum amount the investor believes is sufficient to fund any deviations from economic reserves

- May not tie to regulatory or rating agency capital
- In practice it is greater of the minimum required by regulators and minimum required by investors
- If it is too large, the SPV may not be viable

Capital backing redundant reserves can be hard assets (e.g. bonds) or soft assets (e.g. a LOC)

## Page 27
SPVs were traditionally located outside the US to avoid US regulatory obstacles, but SPVs have been increasingly formed within the US since 2000

# Objectives of SPV Sponsors and Investors 

- SPV investor $=$ entity providing additional funding
- SPV owner $=$ SPV sponsor
- Usually a reinsurer
- If SPV owner = a ceding company, it means there is no reinsurer involved in the deal (i.e. a direct insurer is working directly with investors)
- The sponsor could also be the parent of the (re)insurer (This is how the SPV model discussed later works. The authors mention this design causes fewer tax problems, but they do not elaborate on why that is.)
- In any case, the SPV sponsor's objective is to fund redundant reserves with low-cost capital
- Allows sponsor to use its other capital for higher risk (higher return) purposes
- Investor wants a very remote exposure to a loss (i.e. low probability than economic reserve + require capital is not sufficient)
- If the investor's risk is low, the investor is willing to accept a small return, which satisfies the sponsor's objective of getting low cost capital


## A Securitization SPV

Securitization - transaction where future gains (e.g. future releases of redundant reserves) are sold by an insurer or reinsurer to investors for cash

There are 4 key entities:

1. The (re)insurer
2. Sponsor $=$ parent of the (re)insurer

- Contributes capital and receives distributable earnings
- As noted earlier, the (re)insurer may be the sponsor, in which case there are only 3 total entities

3. SPV = a captive reinsurer (usually just called the "captive")

- Captive $=$ another entity owned by the same parent company or sponsor
- The (re)insurer cedes $100 \%$ of business to the captive (usually through coinsurance)

4. Investors $=$ entities who purchase bonds issued by the captive

- If LOCs are used instead of bonds, the investor role is basically filled by a bank

## Page 28
# Typical Steps for Structuring an SPV 

1. Sponsor forms the captive and contributes enough capital to meet the requirements agreed with the investors and regulators

- This is the required capital discussed earlier

2. Captive issues bonds to the investors, and the following is documented:

- Restrictions on use of the funds
- Delineation between reserve and capital requirements
- Funds provided by the bonds will be used to pay benefits and claims only after all assets backing reserves and required capital are depleted
- Statements of how and when dividends, cash, or other assets may be paid to the sponsor
- How and when any experience refunds will be paid to the ceding company
- Payment of interest on the bonds
- Repayment of the initial principal

3. The funds are then placed in 3 trusts, depending on the purpose of the funds:
1) Capital account trust contains the required capital contributed by sponsor (parent)
2) Economic reserve trust is funded by the cash flows from the underlying business (premiums less claims, etc.)
3) Redundant reserve trust holds funds from investors (the cash investors paid for bonds)

This structure will remain in place until the SPV is wound down
In practice, the terms may be modified by mutual agreement to release some assets if there is less need funds

## SPV Investor Considerations:

1. SPVs are expensive to establish

- Analysis is time-consuming and costly
- SPVs require a sufficient volume of business to justify the expenses

2. Bonds for SPVs are no longer issued in capital markets

- Before the financial crisis, rating agencies rated SPV-issued bonds very high, which allowed monoline insurers to protect investors from loss
- This no longer happens post- financial crisis

3. Structures usually include new business for a limited period of issues (e.g. 1 year)

## Page 29
- It is easier to predict the capital needs for a limited period or specific volume
- The terms can be expanded to include more new business if mutually desired

4. Most SPVs provide coverage for a limited group of products (e.g. all level premium term products)
5. Maximum funding for required capital must be in place at SPV inception

- Investors usually do not want to rely on promises to fund at a future date

6. Maximum funding of the redundant reserves should be in place at the establishment of the SPV

- There are agreements in place that provide more funding at a later date, as needed
- Sponsor generally will pay a fee for this commitment by the investor to provide funds later as well as a fee for funds actually provided

7. Risks ceded to the SPV are some form of coinsurance

- YRT generally doesn't transfer redundant reserves, but a guaranteed premium YRT could

8. Asset structure must be formatted so that ceding company can take U.S. statutory reserve ceded credit

- Use of trusts facilitates this

9. Investor must be prepared to have its assets held in the SPV for a long period (30+ years)
10. Investor generally retains the investment income from the assets

# Use of LOCs to Fund SPVs 

Since it became difficult/impossible to fund SPVs through bonds after the financial crisis, LOCs are often used now instead of bonds

- Post-crisis, banks became willing to issue long-term LOCs to captives for terms up to 30+ years
- The LOC is placed in the redundant reserve trust (same place the bonds were placed)

The rest of the structure is the same as described above for bonds

## Advantages of LOCs

- Only the amount of annual redundancy needs to be funded by the LOC
- Bank commits to increasing the LOC amount each year for a guaranteed fixed charge
- Avoids the need to refinance the LOC
- Better than using bonds, which would have to be reissued (refinanced)
- The cost of long-term LOCs has fallen as banks gain comfort

## Page 30
- In 2009 a 5-year LOC might charge a 500 bps spread
- In 2014, a 20-year LOC might charge less than 100 bps


# General Considerations for Alternative Reinsurance Structures 

1. Clearly identify the goal
2. Consider all objectives, regulations, and accounting matters
3. Develop and carefully analyze models of the transaction
4. Document the agreed transaction clearly with regard to the obligations of and restrictions on each of the parties
5. Monitor the emerging results
6. Do not rely on an assumed common practice since structures like SPVs tend to be unique

## Page 31
# Tiller Ch. 6: Assumption 

Source Author: Tiller and Tiller, 4th ed. (2015)

## Overview of This Reading

In previous chapters, the focus was mainly indemnity reinsurance, where the ceding company is was still under legal obligation for all policyholder claims (i.e. the reinsurer simply reimbursed the ceding company)

Assumption reinsurance is a process where the original insurer is totally replaced by an assuming insurer, who becomes responsible for $100 \%$ of all policy obligations

Assumption reinsurance is effectively the sale of a block of business from the transferring insurer to the assuming insurer

## Key topics for the exam include:

- Definition of assumption reinsurance
- Motivations for assumption agreements-transferring company vs. assuming company vs. regulators
- Assumption Reinsurance Model Act
- Transfers not included
- Commissioner approvals required and commissioner considerations
- Requirements for policyholder notification
- Process for policyholder consent
- Assumption process
- Assumption reinsurance agreement
- Regulatory approval
- Effect on policyholder
- Failure of the assuming insurer to perform
- Practical considerations
- Financial effects of assumption reinsurance
- Assumption reinsurance in Canada
- Insurance Company Act (ICA)


## Overview of Assumption Reinsurance

- Sometimes just called "assumption"
- Effectively a sale of $100 \%$ of the business
- Transferring insurer - the original direct insurer being replaced
- Assuming insurer - the new insurer 100\% responsible for all policy obligations

## Page 32
- Assuming reinsurer issues a notice of transfer and certificate of assumption to the policyholder
- All future contact is between the assuming insurer and the policyholder-the transferring insurer has no further obligation
- Assumption agreements rarely have recapture provisions (unlike indemnity agreements, which often do)


# Transferring Insurer Perspective 

## Reasons to Use Assumption Reinsurance

- Exit a product line or sell a block of business to reduce risk or administrative expense
- May move agency relationships as well
- Sell problematic blocks
- Could make the remaining business more attractive for a future whole-company sale
- Raise capital more easily than other means
- Assumption does not require investment bankers or SEC approval
- Less likely to require shareholder approval
- Gains and losses resulting from assumption are recognized immediately under US stat, tax, and GAAP accounting
- Indemnity gains are amortized over future years under US stat and GAAP
- Indemnity losses are recognized immediately under US stat and GAAP
- Transferring insurer may receive higher value under assumption if indemnity would be subject to recapture
- Transferring insurer may be insolvent and required by a rehabilitator (e.g. state regulator) to use assumption to place business with another insurer


## Other Considerations for Transferring Insurer

- Assumption is "intended to be an irrevocable step"
- If a company wishes to stay in a LOB or maintain its field force, indemnity would be better
- Transferring insurer should perform reasonable due diligence on prospective assuming insurers
- If assuming insurer becomes insolvent, original company could have a contingent liability to policyholders
- Trusts can be used to mitigate the risk of insolvency
- Would allow transferring insurer to take over if assuming insurer becomes insolvent

## Page 33
- Some state insurance departments may not fully accept the trust if it does not equally protect all policyholders


# Assuming Insurer Perspective 

- May want to assume several blocks of similar business to optimize administrative capacity
- Lowers assuming insurer's per unit expenses
- Must carefully consider all costs, including cost to convert business to buyer's admin system
- Acquire a field force and build larger LOB
- Earn a higher return on excess surplus than can be achieved otherwise
- Assuming insurer may have a lower cost of capital
- Must carefully review persistency, mortality, expense, and investment assumptions

Any non-cash assets transferred to the assuming insurer are marked to market

- May allow assuming insurer to achieve higher investment returns


## Assumption Agreements Caused by State Regulators

- State insurance departments often use assumption reinsurance to provide security to the policyholders of insolvent insurers
- May result in a very favorable deal for the assuming insurer compared to situations where a regulator is not involved


## Assumption Reinsurance Model Act

The NAIC's Assumption Reinsurance Model Act provides guidance but has been adopted by less than half of all states

- Regulation and requirements for assumption reinsurance vary widely by state
- Makes the assumption process tedious, and complicated

An insurance policy is a legal contract between the policyholder and the insurance company

- Cannot be modified by either party without the other's consent
- Novation - modification of an insurance policy


## Transfers NOT regulated by the Model Act:

- Ceding company remains directly liable to policyholder (indemnity)
- One insurer is substituted for another upon expiration of the insurance coverage, and a new insurance contract is issued

## Page 34
- Mergers or consolidations (M\&A)
- Liquidation or rehabilitation
- A state insurance guaranty association is involved
- Single group policies transferred at request of the group


# State commissioner approvals required: 

- Transferring insurer must obtain commissioner approval in domicile state
- Assuming insurer must be licensed in states where it will be assuming risks unless those state commissioners approve


## Foreign assuming insurers are required to file:

- Copy of the assumption certificate
- Copy of the notice of transfer
- Affidavit stating that the transaction is subject to substantially the same requirements in parties' domicile states


## The commissioner will consider the following factors:

- Financial condition of both insurers before and after the transaction
- Competence and integrity assuming insurer's management
- Assuming insurer's plans to administer the transferred business
- Fairness to the policyholders
- If notice of transfer is clear and adequate


## Requirements for policyholder notification:

- Date of the transfer and novation
- Contact information for both insurance companies
- Notification of the policyholder's right to consent or reject the offer along with consequences
- Statement that the assuming insurer is licensed or authorized in policyholder's state
- Contact information for the person at the transferring insurer
- Contact information for the insurance department in the state where the policyholder resides
- Financial information for both insurers:
- Financial ratings from the last 5 years from 2 nationally recognized rating agencies
- Last 3 annual balance sheets of both companies

## Page 35
- Copy of the Management's Discussion and Analysis from the previous annual statement of both companies
- An explanation of the reasons for the assumption

Certificate of assumption - contains the primary information regarding the novation

- Intended for policyholder to keep with their original policy


# Process for policyholder consent: 

1. Notification must include a pre-addressed, postage paid response card to indicate acceptance or rejection
2. If no response received within 24 months, assuming insurer must mail one final notice giving the policyholder 30 days to respond
3. If no response is received, the Model Act permits assuming insurer to deem consent
4. If policyholder has paid premiums to the assuming company during this time period, the policyholder is deemed to have consented

## The Assumption Process

1. Establish assumption reinsurance agreement - covers the sale or transfer

- The negotiation phase is lengthy and complicated
- The following should be documented in the assumption reinsurance agreement:

1. The policies or block being transferred
2. Desired effective date of the transaction, subject to approvals from regulators and boards
3. Consideration being paid to the assuming insurer (usually stated as a function of the reserves on the block)
4. Initial ceding commission at inception-normally price paid by the assuming insurer
5. Which insurer is responsible for claims incurred before but not paid by effective date
6. Responsibility for policy administration and services after the effective date
7. Transition and approval responsibilities of each party
8. Notification of policyholders
9. Notification of agents/brokers and payment of future commissions
10. Tax treatment
11. Cooperation/responsibility for tax and financial reporting

## Page 36
12. Responsibility for payment/receipt of any tax liabilities or assets
13. Representations and warranties typical of such transactions
14. Treatment of policies prior to assumption or never assumed

# 2. Regulatory approval 

- Each party submits assumption reinsurance agreement to their domicile state regulators
- It is a good idea to discuss a proposed agreement with states beforehand to identify specific concerns
- The assumption agreement itself needs to be approved only by the 2 states of domicile of the transferring and assuming insurer
- Each state with affected policyholders must approve the assumption notice and assumption certificate
- Tedious and time-consuming process because states follow different procedures


## 3. Effect on policyholder

- Policyholder must be notified and consent for the assumption is binding
- Consent can be specific, implied, or given by a regulator in the event of insolvency
- See the NAIC Assumption Model Act earlier for details
- If consent has occurred and been approved by states, the policyholder deals directly with the assuming company going forward without any further contact with the original carrier
- Opposite of indemnity reinsurance, where the policyholder has no right to "look" to the reinsurer at all
- For policyholders that do not consent, their policies stay with the original insurer
- These are often reinsured on an indemnity basis


## 4. Failure of the assuming insurer to perform

- If it was obvious the assuming insurer was financial unsound at time of transfer, the transferring insurer could have a contingent liability
- Hence its good to do due diligence
- Anything is possible through litigation-no guarantees that the transferring insurer is ever free of liability


## Practical Considerations for Assumption Reinsurance in the US

The consent process can take years to complete

- Interim indemnity reinsurance

## Page 37
- Often the business is transferred using 100\% coinsurance or mod-co first
- The assuming insurer either assumes responsibility for policy admin or uses a TPA
- As policyholder consents are received, policies move from the indemnity to the assumption agreement
- For policies that never leave the indemnity agreement, the original insurer is still directly liable for claims


# - Right of assumption agreements 

- Used by a reinsurer that prefers indemnity but wants the option to convert to assumption in the future (e.g. if some event occurs)
- Could be a clause in a standard indemnity agreement
- Tax implications should be carefully considered


## - Legal considerations

- Requires competent, experienced legal counsel and working with the relevant insurance regulators in advance of any formal agreement or announcement
- Regulators may want more authority for assumption than for indemnity
* Placing assets in trust/escrow may not be enough


## - Administrative considerations

- The transferring insurer may continue to perform admin function for a period of time for a fee
- The assuming insurer may use a TPA


## - Filing details

- Can be "extremely voluminous"
- Regulators may require a copy of every policy form-difficult to provide in practice since the original company may not even have


## - Existing indemnity reinsurance

- If prior indemnity agreements exist, they normally continue-the assuming insurer normally steps into the transferring company's shoes
- The existing indemnity reinsurer may want to negotiate termination or recapture


## - Types of notice and consent in use by states (varies by state)

1. Based on the review of the state-policyholders are simply notified
2. If policyholder makes a premium payment to assuming insurer, that is considered consent
3. Like (2) but allow policyholders to object to assumption

## Page 38
4. Require active acceptance by policyholder
5. Like (4) but allow assumption to be effective immediately as long as transferring insurer agrees to have responsibility on assuming reinsurer insolvency
6. Allow $100 \%$ assumption if a large majority of policyholders accept

- Insolvency, liquidation, and rehabilitation
- Each situation is unique
- Generally assumption process is faster in these situations


# Financial Effects of Assumption Reinsurance in the US 

- Transferring insurer (fairly straightforward)
- Statutory reporting:
* Treated like policy surrender
* Policy reserves are released
* Assets and policy loans are transferred to assuming insurer
- GAAP reporting:
* Write off DAC and release benefit reserves
- Tax reporting:
* Taxable gain occurs if the MV assets paid by transferring company (net of purchase price) are less than tax reserves released
* Otherwise it's a loss (reduces taxable income)
- Assuming insurer (more complicated)
- Statutory reporting:
* Same reporting as indemnity
* Establish appropriate reserve for risks assumed
* Initial allowance is treated as an immediate expense
* After the assumption, amounts received and paid are treated as direct amounts
* Any gain or loss is recorded as of the date of the date of the assumption
- GAAP reporting:
* Treated under GAAP purchase accounting so that no gain or loss occurs immediately (gets amortized)
* Initial consideration and allowance are amortized over future revenues
- Tax reporting:

## Page 39
* Block is treated as the purchase of an asset
* Any ceding commission or strain must be amortized over 180 months
* Tax reserves are based on the original policy issue dates, not the assumption date


# Assumption Reinsurance in Canada 

Canadian assumption regulation and processes are simpler than in the US

1. Only 1 national regulator instead of multiple states
2. Transferring insurers in Canada do not have absolute relief of policyholder obligations

## Insurance Company Act (ICA)

Insurance Company Act (ICA) governs the transfer of business and assumption

- Requires transferring insurer to have the approval of the Minister of Finance if substantially all risks will be transferred
- Requires approval Superintendent of Insurance if less 100\% are to be transferred
- Shareholders, members and policyholders are entitled to vote through a special resolution


## The assuming insurer can be any of the following:

1. A federally registered insurance company or society
2. A foreign company that reinsures the risks in Canada
3. A provincial corporation if the Superintendent has satisfactory arrangements
4. An entity authorized to accept risks that were undertaken outside of Canada by the transferring company

## Requirements for the transferring insurer:

- Must publish notice of the transaction in the Canada Gazette at least 30 days before applying for Minister's or Superintendent's approval
- Must make assumption agreement available to shareholders, members, and policyholders at least 30 days after the publication of the notice
- Copies must be sent to any shareholders, members, or policyholder that requests in writing
- Superintendent may ask for a report by an independent actuary before approving
- Must send information to the affected policyholders regarding the assumption

## Page 40
# Implementation in Canada 

- Liabilities are removed from transferring insurer's books and placed on assuming insurer's books under Canadian GAAP
- Relatively simple in Canada compared to US
- Both insurers should discuss with Superintendent of Insurance first

## Page 41
# Tiller Ch. 7: Reinsurance of In-Force Risks 

Source Author: Tiller and Tiller, 4th ed. (2015)

## Overview of This Reading

This chapter primarily addresses the statutory accounting effects of placing indemnity reinsurance on existing in-force risks using various forms of coinsurance

This chapter, along with Ch. 6 creates many opportunities for questions that ask you to compare indemnity and assumption reinsurance

Beginning with the "Terminology" section, the remaining portion of Ch. 7 more or less completes Ch. 5 by giving a little more information on in-force blocks of reinsurance and listing advantages and disadvantages for each of the 6 distinct reinsurance methods covered in Ch. 4 and 5

## Key topics for the exam include:

- Compare indemnity reinsurance with assumption reinsurance
- Ceding company and assuming reinsurer perspectives
- Uses and objectives
- Use of indemnity reinsurance for surplus relief
- Treaty considerations with respect to:
- Relationship between initial and renewal allowances
- Experience refunds
- Factors affecting size of risk charge
- Recapture
- Risk based capital effects
- Advantages and disadvantages of:
- YRT
- Coinsurance
- Mod-co
- Funds withheld coinsurance
- Funds withheld mod-co
- Part-co
- Miscellaneous pricing and treaty considerations


## Use and Objectives of Indemnity Reinsurance for In-Force Risks

These follow the list of reasons a transferring insurer would use assumption in Ch. 6 pretty well, but there are differences to know for comparisons.

## Ceding Company Perspective

## Page 42
- Exit a product line or sell a block to reduce risk and admin expense
- Agency relationships usually move as well but not always
- Ceding company usually retains admin responsibilities as source of income
- Discontinue admin of block
- Block may be too small or may require expensive admin system upgrades
- Cede problem blocks through indemnity to make remaining business more attractive
- Cost of reinsurance may produce more favorable financial results
- Raise capital without involvement of investment bankers or approval from SEC or shareholders
- Indemnity may allow for recapture, but ceding company will receive less value
- Rehabilitator may require assumption for an insolvent insurer
- Use of indemnity avoids having to market assets to market-allows ceding company to avoid losses at time of transaction if asset $\mathrm{MV}<\mathrm{BV}$


# Indemnity Reinsurer Perspective 

As with the preceding ceding company list, this list tracks the "assuming insurer" perspective pretty closely in Tiller Ch. 6 creating more compare/contrast question opportunities.

1. Increase business in force without selling new business

- Indemnity and assumption can both be used

2. Indemnity is useful when assuming company is not authorized in a state or has lower rating than ceding company

- Avoids higher lapses from policyholders who don't like lower rated company

3. Indemnity reinsurer can optimize excess admin capacity

- Must carefully consider costs

4. Acquire new distribution system or build larger LOB quickly
5. Earn higher return on excess surplus

- Reinsurer may have lower cost of capital than ceding company

6. YRT reinsurance for in-force blocks can increase reinsurer's growth and profitability Important theme to note: even though indemnity reinsurance is not technically a sale of the business, it can accomplish a lot of the the same objectives. You can think of any reinsurance arrangement as the full or partial "sale" of some or all risks from one company to another. Anything that causes the ceded risks to be "worth more" to the assuming company than the ceding company would cause the assuming company to enter such a transaction and also make it attractive to the ceding company as well.

## Page 43
# Indemnity Reinsurance vs. Assumption 

Choice depends heavily on circumstances and facts for a specific transaction

1. Indemnity is better when ceding company:

- Wants to continue in LOB
- Keep agency force
- Fears reputational risk of transfer obligations to assumption reinsurer

2. Indemnity is not generally disclosed to policyholders and agents
3. Indemnity is a much quicker process than assumption

- No approval needed from policyholder and possibly no approval needed from regulators/shareholders

4. Indemnity is better for short-duration insurance products may terminate before assumption process is completed
5. Indemnity is more useful than assumption if reinsurer is not licensed in all states with existing in-force
6. Indemnity agreements go into effect immediately allow immediate ceding of risks

- No waiting on policyholder approvals like assumption

7. Indemnity gains at inception are amortized under stat, GAAP, and tax accounting

- Good if company wants to lock in future profits instead of recognize immediately

8. Indemnity agreements are more likely to have recapture provisions, which may be desirable to ceding company
9. Indemnity allows for less than $100 \%$ of risks to be ceded
10. Indemnity reinsurance has a counterparty risk capital requirement, but assumption does not
11. Assumption is more popular with insurance departments rehabilitating troubled insurers, but sometimes guaranty associations prefer indemnity for companies with negative or uncertain results

As with assumption agreements, the ceding company should perform due diligence on prospective indemnity reinsurers

## Indemnity Reinsurance for Surplus Relief

Became popular in 1980s, but there were problems in the early days:

- "No risk" or very low risk transactions became popular, but some companies became insolvent

## Page 44
- Treaties with experience refunds became associated with not transferring risk
- However, today an experience refund does not in itself indicate lack of risk transfer
- Regulators began denying reserve credit and/or surplus relief to transactions that did not transfer meaningful risks
"Surplus treaties" - generally result in increase of ceding company's surplus
"RBC treaties" - structured to primarily provide RBC relief to ceding company but have little or no surplus relief

Both types increase the surplus ratio of the ceding company

# Surplus Relief Treaty Considerations 

1. Should be designed to be permanent
2. Only the ceding company should have the option to terminate
3. Clearly define terms of termination and recapture in the treaty
4. Recapture must generally be for all in-force
5. Recapture of indemnity reinsurance intended to be permanent is allowed only if reinsurer has solvency concerns
6. Recapture provision should lower the initial consideration and/or renewal allowances from the reinsurer
7. Experience refund provisions are common
8. All significant risks must transfer for ceding company to receive reserve credit and/or surplus relief

## Terminology

Ch. 7 has a terminology section that mostly overlaps with the terminology introduced in Ch. 5. Only the additional information added by Ch. 7 is included below. Bigger picture, you can think of these as considerations that go into a reinsurance treaty.

## Allowances

## Renewal Allowances

If renewal allowances are set higher than ceding company's expenses, it creates an additional source of profit for ceding company

If set lower than ceding company's expenses, US regulators will likely NOT allow a reserve credit and/or surplus gain for the ceding company

- In Canada, it is allowed (lowers gain at inception)

Initial Allowances

## Page 45
Higher initial allowances lead to lower renewal allowances and vice versa
Lower initial and renewal allowances could be better when the ceding company only needs temporary surplus relief and desires to recapture the business sooner

# Experience Refunds 

Usually not earned until outstanding surplus account is paid off
Reasons the reinsurer may pay an experience refund:

1. High uncertainty about expected results at time of pricing
2. Encourage the ceding company to manage claims and policyholder services well

Potential regulatory problem: regulators may view an experience refund as a warning flag that the treaty does not transfer sufficient risk

- The authors feel this is an unfair view since a treaty can transfer risk and offer experience refunds


## Risk Charge

Often applied in the outstanding surplus account ${ }^{2}$
A.k.a. "profit charge," "risk and profit charge," or "expense and risk charge"

The size of the risk charge is highly negotiable and varies by situation:

- Nature of risks assumed
- Size of the transaction
- Reinsurer's profit objectives
- Market conditions
- Ceding company's stability
- Tax considerations
- Company relationships
- Reinsurer's expenses

Historically, risk charges have ranged from $1 \%$ of outstanding surplus on low risk treaties to $15 \%$ or more of invested capital for higher risk treaties

## Recapture Provisions

Recapture provision - ceding company's right to end the reinsurance agreement and fully assume block of business again

[^0]
[^0]:    ${ }^{2}$ All of the examples in the Tiller book assume the risk charge is applied to the OSA, but actual treaties can define it different terms.

## Page 46
Treaty may be defined so that recapture can't occur until outstanding surplus account $>0$

- Treaty may allow recapture if ceding company makes a payment equal to outstanding surplus account

Recapture provisions do not indicate that risk transfer is absent

- Gives ceding company a way to benefit from business that is more profitable than expected
- May indicate the reinsurer expects less "negative volatility" in earnings


# Risk Based Capital Effects 

Generally, RBC requirements pass proportionately from the ceding company to reinsurer

- Examples: required capital for mortality (C-2), morbidity, asset (C-1), or interest rate risks (C-3)

Ceding companies also have to hold RBC for counterparty credit risk

- Requirement is much smaller than RBC ceded
- Reflects reinsurer's insolvency risk based on its financial strength
- In general, capital requirements for the ceding company are reduced more under assumption than under indemnity reinsurance, as there is no counterparty component for assumption


## RBC Effects by Type of Reinsurance

- YRT - transfers significant C-2 component to reinsurer for any type of life product
- Allows ceding company to reduce face amount used in C-2 calculation by ceded portion
- Usually eliminates C-2 required capital for ceding company
- Coinsurance - transfers C-1 and C-3 risk in addition to C-2
- Counterparty credit risk requirement is larger than YRT
- Mod-co and combined methods - RBC transfer varies by risk
- Transfers of asset risks are based on exposure and ownership
- Generally asset performance risk transfers to reinsurer
- Remember that even though the reinsurer does not possess the assets under a mod-co deal, they have to assume risks of asset performance through the mod-co interest mechanism
- Indemnity vs. assumption reinsurance
- Generally, capital requirements for the ceding company are reduced more under assumption than under indemnity reinsurance
- There is no counterparty credit risk requirement for assumption reinsurance

## Page 47
# Advantages and Disadvantages of Each Method 

This section discusses advantages and disadvantages of each of the methods covered in chapters 4 and 5.

## YRT

## Trends That Make YRT Attractive to Ceding Companies

1. Increased focus on capital adequacy
2. Demands for higher return on capital
3. Relatively low capital levels in the industry in the light of growth opportunities
4. Inexpensive way to reinsure mortality costs, sometimes even less than ceding company's mortality assumptions

## Reasons Ceding Companies Now Reinsure Large Portions Using YRT

The overall trend in the US and Canada has been to increase the proportion of in-force reinsured

1. Reinsurers' mortality assumptions are aggressive (attractive YRT rates)
2. Increases confidence in ability to pay policyholder dividends long-term
3. Reduces net capital requirements, especially in early durations
4. Allows ceding company to use more competitive pricing (charge lower premiums, increase sales)
5. Can address over-retention issues resulting from M\&As

## Advantages of YRT

1. Limits reinsurer's investment and lapse risk since there is no reserve or cash value buildup
2. Does not require reinsurer to manage level of assets involved under coinsurance
3. Lower ongoing cost than any form of coinsurance

## Disadvantages of YRT

1. Limits potential for surplus relief
2. YRT rates are not guaranteed in the US (may increase)

## Coinsurance

## Advantages of Coinsurance

## Page 48
1. Simplest to administer if a quota share method used ${ }^{3}$
2. Cleanest form of reinsurance from regulatory view point-fewest questions concerning transfer of risk

# Disadvantages of Coinsurance 

1. Chief disadvantage: Need to transfer assets

- Ceding company must transfer control of assets equal to the reserves (significant amount for inforce)

2. May have to give reinsurer control of or veto power over the dividend or interest rate determination

- May raise regulatory concerns or increase reputation risk

3. Requires reinsurer to manage the assets, subjecting it to additional investment risk
4. If treaty terminated, reinsurer must transfer assets to ceding company

- Potential capital gains or losses in asset transfer

5. Ceding company cannot take reserve credit if reinsurer is not admitted in ceding company's state of domicile unless reinsurer provides some form of security acceptable to the state-expensive and burdensome
6. Exposes ceding company to counterparty credit risk

## Modified Coinsurance

## Advantages of Mod-Co

1. Major advantage: Avoids liquidating or transferring ownership of assets to the reinsurer
2. Allows ceding company to maintain control of the investment policy for a block of business (especially interest-sensitive products)
3. Applicable to all plans of insurance (same as coinsurance)
4. Eliminates reserve credit problem for non-admitted reinsurers
5. Tax advantages

- Reinsurer can deduct full increase in tax reserves corresponding to mod-co adjustment paid
- Ceding company excludes mod-co adjustment from taxable income
- Tax reserves on ceded portion remain with ceding company

6. Reinsurer may prefer not to manage assets (may not have the expertise)
${ }^{3}$ The term "quota share" was not explicitly defined in Ch. 5, but that's basically what all of the examples were based on. Quota share $=$ constant $\%$ ceded for all policies.

## Page 49
7. Makes recapture easier for ceding company since it already possesses the assets
8. Assets backing ceded can be co-mingled with other assets and used for other purposes

# Disadvantages of Mod-Co 

1. More complicated to administer than coinsurance because of mod-co adjustment
2. Surrenders and deaths require special transactions
3. Transfer of assets back to the reinsurer if treaty terminates can create exposure to capital losses for the ceding company
4. Transfer of initial mod-co adjustment to the ceding company can create problems for the reinsurer
5. Reinsurer would prefer coinsurance if it has doubts about solvency of the ceding company

## Funds Withheld Coinsurance

## Advantages of FW-Co

1. No cash changes hands in the initial transaction and cash flow is minimized throughout life of treaty
2. Lessens ceding company's risk if reinsurer becomes insolvent
3. Ceding company can take reserve credit up to amount of funds it is holding even if reinsurer is non-admitted
4. Assets can be managed consistently with other assets on similar business

## Disadvantages of FW-Co

1. More complicated than coinsurance
2. May be regulatory limits on the length of time funds can remain unpaid

- Usually not a problem if the ceding company is holding a net payable liability to reinsurer

3. May increase the reinsurer's counterparty risk compared to mod-co transaction
4. Fluctuations in receivable assets may create undesirable accounting results
5. Reserve credit problem for ceding company if reinsurer not admitted and funds withheld are with the reinsurer

- Not as bad as regular coinsurance since ceding company holds assets backing ceded reserves

6. Regulators may require marking assets to market

## Page 50
# Funds Withheld Modified Coinsurance 

## Advantages of FW-Mod-Co

1. Reinsurer retains initial allowance

- Does not need to liquidate assets to pay it and minimize future capital loss exposure

2. Reinsurer has less risk if ceding company becomes insolvent since it is holding assets underlying the initial allowance

## Disadvantages of FW-Mod-Co

1. Adds more complexity
2. Mod-co adjustment becomes complicated because the ceding company did not get allowance in cash

- Must make a special adjustment to the interest part to make up for the ceding company not earning interest on the allowance

3. Deferral of allowance payment likely violates NAIC Model Life and Health Reinsurance Agreement Regulation

## Partially Modified Coinsurance

Ch. 7 mostly repeats the advantages and disadvantages listed in Ch. 5 for part-co and adds a few more. We are showing all here for completeness.

## Advantages of Part-Co

1. No cash transaction initially and no capital gains and losses
2. Eliminates need for FW receivables and payables
3. Facilitates recapture by reducing the volume of assets subjected to market value adjustments

- Significant advantage for treaties intended to provide temporary surplus relief

4. Potentially fewer regulatory questions compared to FW transactions

## Disadvantages of Part-Co

1. Very complicated to administer and understand
2. "Looks and smells" like older surplus relief treaties that did not transfer risk (regulators may have concerns)
3. Requires 2 stat gain calculations

- Calculate preliminary stat gain to determine change in co/mod-co proportions
- Calculate final stat gain reflecting the new split in co/mod-co

## Page 51
# Pricing and Treaty Considerations 

Parts of this section of Ch. 7 repeat things that were said earlier word for word, so only the additional points are included below

1. Same regulation covers indemnity reinsurance for in-force and new issues
2. Recapture provisions are generally not included when indemnity reinsurance is intended to be permanent
3. Indemnity reinsurance of in-force risks frequently includes the transfer of administrative responsibilities to reinsurer
4. Treaties covering in-force risks should contain the same types of provisions as treaties for new issues

- Exception: Wording may be changed to reflect the timing of underwriting and issue

5. Legal authorization to issue policies and agent licensing are necessary for in-force reinsurance as well as issues
6. Reinsurers should require the ceding company to adhere to defined underwriting standards
7. Ceding company should state that any financial reports provided to reinsurer are accurate and complete

## Page 52
# Tiller Ch. 9: Risk Transfer Considerations 

Source Author: Tiller and Tiller, 4th ed. (2015)

## Pages pp. 269-280 Only

## Overview of This Reading

This chapter explains the history and importance of risk transfer for reinsurance accounting under US accounting systems

## Key topics for the exam include:

- How and why reinsurance treaties failed to transfer risk historically
- Risk transfer under US statutory accounting
- Life and Health Reinsurance Agreement Model Regulation


## Some History

In the past, reinsurance treaties sometimes transferred little or no risk to the reinsurer

1. Redundant statutory reserve financing where the reinsurer's earnings are not truly at risk
2. Creative tax planning - e.g. an insurer in a tax loss position cedes business to an insurer with taxable gains, so that neither pays taxes

- The IRS can prohibit this now

3. Treaties that allowed reinsurers to delay/defer payments
4. Increase surplus and earnings in order to "dividend" cash to upstream owners

These treaties often masked the true financial situation of the ceding company

## Treaty Terms Commonly Used to Reduce Risk Transfer

1. Setting the initial ceding commission or purchase price of an in-force block significantly lower than expected future earnings

- Conservative pricing or experience refunds do not necessarily indicate lack of risk transfer
- Key question: if experience is bad, who bears the losses?

2. Fixed interest rate mod-co adjustments that do not reference actual asset performance

- Effectively guarantees investment performance for the reinsurer

3. Reinsurer can terminate the agreement from inception if the ceding company is insolvent, changes ownership, or changes management
4. Use of side agreements to guarantee performance of the ceded business so that the reinsurer has no ultimate risk

## Page 53
5. Mandatory recapture of the ceded business at the reinsurer's option
6. Allowing the reinsurer to defer payments to the ceding company for long periods or forever

# Acceptable Risk Transfer 

The primary function of reinsurance is to transfer insurance-related risks; everything else is secondary

Acceptable risk transfer is highly dependent the accounting system
The remaining 4 sections discuss risk transfer under US statutory, US GAAP, US Federal Income Tax, and non-US systems

## Risk Transfer in US Statutory Reporting and Regulation

## Life and Health Reinsurance Agreement Model Regulation

Must be adopted by all US states and applies to all forms of reinsurance except YRT and some non-proportional reinsurance

The Model Reg starts with the assumption that a treaty qualifies for reserve credits and other benefits of normal reinsurance accounting

The Model Reg specifies 11 specific conditions, and if any of those are present, state regulators can prohibit the ceding company from establishing any asset or reducing any liability in its statutory financial statements ${ }^{4}$

Ceding company may NOT take any kind of credit if ANY of the 11 conditions exist:

1. Renewal EA < anticipated allocable renewal expenses (commissions, premium taxes, admin costs, etc.)

- Results in a net cash loss to the ceding company
- Reserve credit will be granted if ceding company sets up a liability for the shortfall

2. The reinsurer can deprive the ceding company of surplus or assets at the reinsurer's option or automatically on insolvency

- Would allow the reinsurer to cancel the agreement when the ceding company needs it the most
- Termination is allowed if the ceding company does not pay amounts that it owes

3. Ceding company must repay reinsurer for losses under the agreement

- Does not include:
${ }^{4}$ For example, regulators could deny a reserve credit for coinsurance or deny the mod-co adjustment for a mod-co agreement. Any ceding company who enters any kind of coinsurance agreement discussed in Tiller Ch. 5 will want to be able to show reserve/surplus relief under statutory accounting, so there is a strong incentive to satisfy the Model Reg's criteria.

## Page 54
- Offsetting experience refunds against past losses
- Payment of the reinsurer's losses on voluntary termination by the ceding company
- Reinsurer's ability to raise reinsurance premiums "excessively" or risk charges so high that it forces the ceding company to terminate the agreement

4. Ceding company must recapture or terminate all or part of the reinsurance under contract by a specific date
5. Ceding company is required to pay amounts not realized from the reinsured policies

- Example: payment of premiums in excess of the direct premiums

6. Agreement fails to transfer all significant risk inherent in the reinsured business
7. Credit, reinvestment, or disintermediation risk is significant and the assets are either not transferred to reinsurer or legally segregated in a trust/escrow

- Assets held by the ceding company for the reinsurer do not need to be segregated for LTCI, most types of WL, or fixed premium UL without dump-in premiums

8. Settlements are less frequent than quarterly or reinsurer doesn't pay amounts due in cash within 90 days
9. Ceding company has to make warranties or representations which are not reasonably related to reinsured business
10. Ceding company is required to guarantee the future performance of the reinsured business
11. Agreement is principally for temporary surplus relief without transferring all significant risks

# Additional requirements in the Model Reg for the ceding company: 

1. In-force agreements must be filed with the commissioner within 30 days of execution, along with financial impact data
2. Ceding company's AA must consider the Model Reg in the Actuarial Opinion
3. Increases in surplus are shown on special line of the capital and surplus account
4. Final agreement or letter of intent must be signed before taking reserve credit on financial statements
5. Reinsurance agreement must be in writing and include a provision stating the agreement constitutes the entire contract

## The Risk Transfer Product Table

The Model Reg lists 6 risk categories and whether each is significant for 17 different product types

## Page 55
- 6 risk categories: morbidity, mortality, lapse, credit quality, reinvestment, and disintermediation

If a risk type is significant, it must be transferred to the reinsurer for the reserve credit to be allowed

Table 9.1 on p. 276 of the book contains the full $6 x 17$ grid. Here is a summary of which of the primary products covered on the ILA track (life insurance, annuities, LTCI) fall into each of the 6 significant risk categories:

1. Morbidity: LTCI only
2. Mortality: all types of life insurance and immediate annuities
3. Lapse: all life and annuity products except immediate annuities
4. Credit Quality: all products except non-par term
5. Reinvestment: all products except non-par term
6. Disintermediation: all products except non-par term, LTCI, and immediate annuities

# Other Considerations Regarding US Statutory Risk Transfer 

- Restatement of annual statement - required if reserve credit is denied or additional liabilities were required
- Cash flow testing - should reflect reinsurance cash flows and should show a reduction in net liabilities (else treaty fails risk transfer test)
- Reinsurance should be modeled separately from direct risks
- Reserve credits vs. additional liabilities - establishing a liability (e.g. for an EA shortfall) is usually more appropriate than reducing reserve credits
- However, the additional liability is not deductible for FIT purposes
- Effect on the reinsurer - ceding company will likely contact the reinsurer at some point to modify/terminate the treaty if there are risk transfer problems
- If ceding company is denied reserve credit, the IRS may deny reinsurance accounting to the reinsurer for tax purposes
- Required capital - will not be reduced if reserve credit is denied
- Financing treatment - treaties that are denied reinsurance accounting are treated like loans, which is "rarely useful to either party"
- Differences by state - some states have even stricter requirements than the Model Reg
- Non-proportional reinsurance - mostly excluded from Model Reg, but be careful not to delay payments for an overly long period
- YRT reinsurance - excluded because of lack of asset risk and to avoid complicating the YRT rate increase process

## Page 56
- Effects on other accounting systems - US GAAP and tax reporting start with US stat in some manner
- If US stat denies reserve credits, it's likely GAAP and tax will too
- Denial of ceded reserve credit when risk is transferred
- Even if reserve credit is denied, the treaty is still a legal contract, and each party must honor its obligations
- Reasons reserve credit would be denied (or delayed) even if risk is transfered:
* Treaty wasn't signed in a timely fashion
* proper security wasn't established for a reinsurer not licensed in ceding company's jurisdiction
* Experience refund and pricing that is more conservative than normal
* Provision for a recapture and termination at a given time for a given price
* Other terms that interfere with normal reinsurance cash flows

## Page 57
# Tiller Ch. 17: Non-Proportional Reinsurance 

Source Author: Tiller and Tiller, 4th ed. (2015)

## Overview of This Reading

The forms of non-proportional reinsurance covered in this chapter are used to manage total claims for a block of life business, not reinsure individual risks like the forms of proportional reinsurance covered in earlier chapters

It's called "non-proportional" because the reinsurance coverage is not defined in terms of a proportion of individual contract's risks. In previous chapters, methods like YRT and various forms of coinsurance always involved defining a percentage of net amount at risk or death benefit covered-even though those percentages could vary at different risk levels (e.g. constant retention). With non-proportional agreements, the coverage is usually defined at a more aggregate level for an entire block-for example, amount of total claims incurred by the ceding company before reinsurance claims begin.

Generally, non-proportional reinsurance is used much, much less than proportional reinsurance in the life insurance industry

There are 3 forms of non-proportional reinsurance covered in this chapter:

1. Stop loss
2. Catastrophe coverage (most common for life insurance)
3. Spread loss (rarely if ever used for life insurance)

## Key topics for the exam include:

- Be able to describe and compare each of the 3 non-proportional methods
- Understand the reserve considerations for non-proportional methods


## Stop Loss Coverage

Stop loss puts a limit on total claims from the ceding company's perspective
For life insurance, stop loss applies to an entire block of business, not just one life
Can be used alone, but is usually used along with proportional reinsurance

- Example: A company may want to increase retention on new business but limit overall claims
- Reinsurer may resist use of stop loss after recapture or retention if another reinsurer is used for stop loss


## Elements of Stop Loss Coverage

These 4 points should be defined in a stop loss reinsurance contract

1. Maximum Retention of the Ceding Company

- Defines max amount per life that will be part of the stop loss coverage

## Page 58
- If a policy has a higher DB than max retention, the excess should be excluded from the stop loss premium, but isn't always in practice

2. Expected Claims of the Covered Business

- Must be define expected claims
- Forms the basis for the attachment point (explained below)
- Expected claims should be defined in relation to ceding company's experience (e.g. $105 \%$ of a company mortality table)
- Must document exactly which policies are included

3. Attachment Point of the Stop Loss Coverage

- Attachment point $=$ level of claims incurred where reimbursement begins (e.g $110 \%$ of expected claims)
- The higher the attachment point above expected claims, the lower the stop loss premium

4. Benefit Limits of the Stop Loss Coverage

- Defines max amount of claims reinsurer will pay
- Reinsurer usually pays less than $100 \%$ of claims above attachment (e.g. $90 \%$ ) to help encourage the ceding company to manage claims well
- Example of benefit limit: $90 \%$ of claims above attachment up to $\$ 1$ million in total and no more than $\$ 100,000$ on any single life

The video lesson contains a quiz to illustrate how stop loss works

# Stop Loss Premium Considerations 

- Stop loss premium $=\%$ of expected claims + a fixed fee
- In reality, pricing stop loss is difficult because of the low frequency and high severity nature of the risks (epidemics, catastrophes, other independent events)
- Expected and actual claims are determined on the NAR, not gross DB
- Net premiums are loaded to cover expenses and risk of deviation (loading could be several times the net premium)


## Benefits of Stop Loss

- Relatively inexpensive
- Useful for protecting surplus
- Could lower long-term reinsurance cost by establishing higher individual risk retentions
- Coverage is closely aligned with management needs: protecting surplus and earnings from claim fluctuations

## Page 59
# Why Few Insurers Purchase Stop Loss 

Main reason: It is difficult to write enough stop loss coverage in any year to provide an adequate spread of risk and balance premiums vs. claims

- Few North American reinsurers offer stop loss
- Reinsurers that write stop loss usually do it to accommodate existing clients
- Max coverage available is usually relatively small compared to insurers' exposures
- Must be renegotiated every year (price and / or coverage could change), so it's not a reliable long-term tool
- After a stop loss claim, insurer is less likely to purchase more coverage because premium will go up
- Ruture expected claims rises as a result of experience and also because of correlation risk-more than one insurer will be affected by pandemics, etc.
- Provides little protection against claims fluctuations for most insurers (only supplements risk management)
- Cannot spread losses or reserves over a number of years because today's accounting models require all premiums and claims to be recognized during coverage period
- Administration is difficult (requires a lot of data)


## Catastrophe Coverage ("Cat Cover")

## More commonly used for life insurance than stop loss

Cat cover protects a ceding company from risk concentrations and unforeseeable events

- Protects against multiple individual claims from a single event (e.g. earthquake, terrorism, etc.)
- 9/11 increased industry focus on concentration risk: multiple lives perished in a common location, triggering cat and accidental death coverages

Covered events and exclusions must be carefully defined

- Exclusion of known concentrations became more common after 9/11
- Examples of possible excluded events: epidemics, wars, riots, terrorism, nuclear hazards
- Examples of possible excluded insureds: sports teams; airline personnel; credit card and travel accident coverage; long-term disability income; and assumed reinsurance


## Characteristics of Cat Cover

- Each reinsurance agreement is individually negotiated and unique
- Premium is expressed as a rate per million of mean inforce business or $\%$ of max benefit (called the "rate on line" in the P\&C business)

## Page 60
- Only NAR is used for determining reinsurance premiums and claims
- Must specify the following:
- Minimum required number of individual claims to trigger (e.g. 5 or more deaths must occur from a single event)
- Max claims covered
- Per life limits
- Large deductibles are common
- Coverages can be done in layers, each with a deductible and include layers below it

Cat events have low probability, so cat covers are unlikely to replace traditional proportional reinsurance or justify increases in retention limits

May be more valuable to larger companies since they have higher exposure to a loss from a single event

# Spread Loss 

Similar to stop loss: reinsurer pays claims above an attachment point
Key difference with stop loss: ceding company repays the reinsurer with interest over a period of years

- Usually accomplished by increasing the premium paid to the reinsurer


## Spread loss is rarely, if ever, used in the US or Canada

- Stat and GAAP accounting views it as a loan, not reinsurance
- Spread loss does not allow the ceding company to take a stat reserve credit
- US GAAP does not treat it as reinsurance
- Reinsurer's primary risks are similar to those of a loan: cash flow timing, credit, insolvency of ceding company
- If ceding company becomes insolvent, reinsurer does not get repaid (like a defaulted loan)


## Non-Proportional Reinsurance Reserve Considerations

There are no objective standards, so it's important to follow ASOP 11 and other accounting pronouncements for guidance

- Ceding company reserve considerations
- Non-proportional agreements rarely qualify for a ceded reserve credit since they cover risks beyond what normal reserves cover
- Regulators are primarily concerned with risk transfer and timing of cash settlement

## Page 61
- If a reinsurer owes a ceding company claim payments, the ceding company is allowed to establish a credit until received
- Under US GAAP, the ceding company would have to demonstrate they expect future recoveries to establish a benefit reserve credit
- Canadian GAAP requires recognition of all future net cash payments
* A reinsurer might have to recognize a margin for spread loss (undesirable)
- Exception to above: a stop loss agreement could have an attachment point set at $80 \%$ of valuation mortality-ceding company could take reserve credit for other $20 \%$ (but even this is unclear)
- Very important to discuss with regulators


# - Reinsurer reserve considerations 

- US stat accounting:
* Some reinsurers include gross reinsurance premiums in earnings in the year covered
- Others reserve all or part of the net premium
* Reinsurer should maintain adequate surplus in relation to its risk for nonproportional reinsurance
- US GAAP:
* All premiums are usually earned during period of coverage
* All claims usually recognized when they occur
* A reinsurer could include only the premium loading as earnings and hold a benefit reserve for the net premium
- Must be able to demonstrate that a future claim is reasonably likely
- Must release the reserve over some period of time if claims do not occur
- Under US stat, US GAAP, and US tax accounting, reinsurer should establish reserve for amount it expects to pay following a claim event

## Page 62
# LPM-160: Strategic Reinsurance and Insurance 

Source Author: Swiss Re (May 2016)

## Pages 1-4, 14-15, \& 18-31 Only

## Overview of This Reading

This paper describes how the reinsurance market is evolving to offer more customized ("strategic") solutions/structures for insurers

The primary audience of this paper is European, but the key concepts would apply to any insurer in the world

## Key topics for the exam include:

- Main motivations for customized (strategic) reinsurance structures
- Be able to briefly describe the 6 life/health strategic reinsurance solutions:

1. Solutions supporting capital efficiency and relief
2. Life in-force monetization
3. Solutions mitigating regulatory changes
4. Solutions supporting growth plans
5. Solutions for mutual insurers
6. Solutions facilitating mergers and acquisitions (M\&A)

## Introduction

Insurers are increasingly using sophisticated, larger, customized reinsurance solutions

- A.k.a. "strategic" reinsurance solutions

Main motivations for customized (strategic) reinsurance structures:

1. Structured protection and risk transfer

- Increases efficiency of insurance programs
- Makes it easier to insure difficult-to-insure risks
- Increases capacity for catastrophic risks (most difficult for smaller carriers)

2. Corporate-finance driven (financial focus)

- Releases trapped or redundant capital and/or increases ROE
- Optimizes capital structure to achieve a broader set of financial objectives
- Can be substituted for traditional capital and reduce the cost of paid-in capital by reducing volatility

3. Enabling strategy and growth (emphasizes dynamic benefits of reinsurance)

## Page 63
- Creates partnership between insurer and reinsurer
- Multi-year solutions align reinsurance with the client's long-term strategic plans

The above categories are not mutually exclusive-ceding companies can create solutions that combine these objectives

# Summary of strategic reinsurance solutions 

There are 10 "strategic reinsurance solutions" listed in the introduction: 4 P\&C solutions and 6 life/health solutions. The remaining on-syllabus page ranges beyond the introduction focus only on the 6 life/health solutions, so we will just focus on those.

1. Solutions supporting capital efficiency and relief (capital management programs
2. Life in-force monetization
3. Solutions mitigating regulatory changes (costs)
4. Solutions supporting growth plans
5. Solutions for mutual insurers
6. Solutions facilitating mergers and acquisitions (M\&A)

## Solutions Supporting Capital Efficiency and Relief

Why strategic reinsurance can be a better alternative to traditional capital:

## 1. Lowers the insurer's cost of capital

- Reinsurers' capital is less expensive because of higher diversification across risks and geographic regions
- Reinsurance dampens the insurer's earnings volatility $\Rightarrow$ makes the insurer itself less risky, so raising traditional capital is cheaper as well


## 2. More targeted, flexible, and private

- More short-term than traditional capital
- Cheaper than raising traditional capital (less complicated and expensive)
- Reinsurance deals can be made in private
- Can target specific risk combinations: e.g. combine non-life retrospective covers ${ }^{5}$ with life quota share agreements


## 3. Can optimize free cash flow and boost ROE

- "Upstream" cash flow and excess capital to the holding company

[^0]
[^0]:    5 Restrospective reinsurance gets little, if any, coverage on the current syllabus. All of the methods covered in the Tiller book are forms of prospective reinsurance, which is reinsurance for future events that haven't occurred. Retrospective reinsurance covers losses from insurable events that have occurred in the past (e.g. ongoing claim payouts for health or LTC insurance).

## Page 64
- Pay dividends to shareholders and/or buy back shares


# Life In-Force Monetization 

Reinsurance can be used to monetize the embedded profits (VIF)

- Upfront ceding commission $=$ VIF
- Releases capital that can be used more efficiently in other businesses and improve overall returns (e.g. issuer higher ROE business)
- Reduces required capital for the monetized block
- Frees up capital and embedded profits in legacy/discontinued LOBs

Policy admin can also be outsourced to the reinsurer, further optimizing the ceding company's operations

## Solutions Mitigating Regulatory Changes

Economic, risk-based solvency regulation and changes to rating agency capital models are driving the following changes:

1. Higher overall capital requirements due to new risk-based capital charges
2. Greater need to optimize capital, product, and business mixes
3. Greater challenges for smaller mono-line insurers, who have less diversification and lack economies of scale

- Should increase M\&A activity

4. Increased demand for reinsurance as a way to achieve capital savings

Strategic reinsurance should provide more opportunities for composite or non-life companies than life-only companies

- Can reduce risk on non-life lines, making companies more balanced from a risk and competitive perspective
- Can reduce/release capital requirement for non-life lines, freeing it up for use in life lines


## Solutions Supporting Growth Plans

- Provide upfront funding/capital for new business
- Reinsurers can provide underwriting expertise when launching a new product or entering a new market

## Page 65
# Solutions for Mutual Insurers 

Mutual insurers are owned by participating policyholders and have a different capital structure than stockholder-owned firms

- Pay out surplus to policyholders through policyholder dividends
- Can't issue stock to raise capital (rely more on retained earnings to build surplus)
- Makes it harder to fund new business, acquire other companies, and compete


## Reinsurance solutions for mutuals:

- Free up capital by reducing capital requirements
- Provide contingent access to capital if threat scenarios emerge
- Provide capital relief for closed participating blocks after demutualization
- When a mutual company demutualizes, it has to maintain a separate closed block for the original par policyholders
- Reinsurance can be cheaper than using bonds or letters of credit for the same purpose


## Solutions Facilitating M\&A

Reinsurance can facilitate M\&A in 3 key areas:

1. Enabling transaction financing and capital efficiency

- Provide efficient/flexible capital/reserve relief with no increase in leverage
- Can be put in place before or after an acquisition and even scaled up later

2. Managing risk and investors' expectations

- Restructure the risks in product portfolio, making it more attractive to buyers
- Reinsure risks the acquiring company does not want to retain
- Protect future earnings and dividends from adverse developments
- Provide risk management expertise before and after the transaction

3. Strengthen stakeholder (shareholders, rating agencies, regulators) confidence by signaling

- Confidence that best practices were used in the transaction
- Commitment of reinsurer's backing
- Increased confidence in the combined entity's ability to manage future risks