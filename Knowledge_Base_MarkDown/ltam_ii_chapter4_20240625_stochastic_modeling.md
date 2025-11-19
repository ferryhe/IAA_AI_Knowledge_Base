_Note: Source document was split into 3 OCR chunks (pages 1-16, pages 17-34, pages 35-37) to stay within token limits._

# LTAM_II_Chapter4_20240625 Stochastic Modeling

## Page 1
# Chapter 4 Stochastic Models 

## Learning Outcomes

The student will be able to:
Describe basic options, option payoffs at maturity, and moneyness.
Describe the need for stochastic models and how stochastic models apply simulation including measuring risk using metrics such as variance, value at risk, and conditional tail expectation.

Describe the need for Economic Scenario Generators (ESG) and the structure of ESG models and components.

Describe static and dynamic assumptions.

Recall from LTAM Part I Chapter 1, a stochastic model is a model possessing some random component, for example, where one or more inputs are stochastic, i.e., random variables. "Stochastic" is derived from the Greek stokhastikos for aim, guess, or conjecture with the connotation of random from the German stochastic originating in 1917. A stochastic model produces a probability distribution of outcomes generated from simulations or stochastic projections. Each simulated set of inputs generates a different outcome. Each simulation or collection of simulated inputs results in a different distribution of outcomes.

In each simulation, the randomly generated values are used as the deterministic inputs to a deterministic model. Once stochastic variables have been simulated, a simulation's scenario is generally indistinguishable from a deterministic model specified by inputs equal to the simulated inputs.

In Part I and so far in Part II, we have only used deterministic models. We have not modeled liabilities (or assets) in which the cash flows and values depend on interest rates and financial market returns. This asset-liability dependency affects policyholder behavior and company actions. We wish to explore and model more complex contexts, in particular, insurance products where the performance and risk profiles for both the consumer and insurer depend on interest rates and market returns.

Stochastic models provide advantages and insights over deterministic models in the finance, insurance, and risk management sectors due to their ability to simulate a range of possible futures rather than a single or handful of predefined scenarios. Over the years, stochastic models have evolved to accommodate the increasing volatility and unpredictability of economic and financial variables, which often change in random and unforeseen ways. This shift from deterministic to stochastic modeling reflects the necessity to capture the complex and dynamic nature of economic environments.

## Page 2
Chapter 4 sets the stage for later chapters. Chapters 4.1-4.3 review (or introduce) financial options, Greeks, delta hedging, Monte Carlo simulation, and risk metrics. Chapter 4.4 covers economic scenario generators, that is, simulating future interest rates and market returns. Chapter 4.5 covers dynamic assumptions.

Risk is the effect of uncertainty on objectives, including both threats and opportunities. Uncertainty means both better and worse than expected are possible. Management makes decisions and implements actions to reach objectives in an uncertain world. Risk management is the process of deciding courses of actions under uncertainty by identifying, assessing, and understanding risks and making decisions. Similar to key performance indicators (KPIs), key risk indicators (KRIs) are metrics related to risk that are deemed important by decision makers or by those evaluating decision makers. Variance and standard deviation are common risk measures.

A basic risk management tool in insurance and investments is diversification, or the pooling of unsystematic risks. A principle underlying pooling and diversification is based on the law of large numbers. The average of results for a large number of trials converges to the expected value. Our long-term actuarial models reflect the we are modeling insurance policies with similar risks. The law of large numbers suggests as the number of predicted events, $N$, grows larger, the variance of the sample mean decreases and the mean or average improves its predictive power.

You may have forgotten we have been using discrete deterministic cash flow models to calculate expected values - for population, decrements, cash flows, and present values since first introduced in LTAM Part I Chapter 1. Our only random variables have been decrements mortality and lapses. Recall, $K_{x}$, the curtate future lifetime of a life age $x$, is a discrete random variable for the number of future complete years lived by life age $x$.

In LTAM Part I Chapter 1 we asserted that in appropriate contexts, that is, with risks that are independent and reasonably identical, we simplify our cash flow model to calculate expected present values (output) by using the expected value as the singular value or input for $X$ ( $X$ could be any distribution). In other words, we can treat $K_{x}$ (and by extension, $q_{x}$ ) as non-random or deterministic and treat the average $E(X)$ or mean $\mu$ with certainty!

For pooled diversifiable risks, the law of large numbers allows us to replace random variables and unexpected cash flows in a model with expected values and expected cash flows. A deterministic model reasonably predicts the expected outcome!

We then provided a warning.

Before proceeding, we issue the first of many warnings regarding a model simplification of treating a random variable as deterministic. Using averages or singular values when not appropriate can lead to disastrous results.

## Page 3
In this book, we cover contexts when a deterministic model is not appropriate. We model many insurance products containing embedded options such as variable annuities, fixed indexed annuities, and ULSG. These products' cash flows depend on random variables such as interest rates and market returns. How then, do we calculate expected values? In addition, we have not been calculating variance or other risk metrics. How can we calculate variance of output variables such as PV(Benefit) and PV(Premium) in our long-term actuarial models?

In practice, discrete stochastic cash flow models are used in many business contexts to calculate expected values, variance, and other statistical risk metrics using simulations.

Simulation reasonably creates the distribution of outcomes and calculation of risk metrics!

# 4.1 Options 

As background material we briefly review options from LTAM Part I Chapter 10. For examples and more details, see LTAM Part I.

### 4.1.1 Options

A derivative is a financial instrument that offers a return based on the performance or value of some other variable called the underlying. The name "derivative" is due to the fact that it "derives" its value from the other variable. The underlying variable is often the price of a traded asset such as a stock, stock index, commodity, interest rate, or foreign currency, but can be values such as the amount of rainfall. To reduce verbiage, we restrict our attention to traded assets and prices, but descriptions can be recast for non-assets and their associated values. The spot price is the price for the immediate purchase of the underlying.

An option is a financial instrument providing one party the right but not an obligation to buy or sell an underlying from the other party at a specified price, called the strike price or exercise price, over a specified time period denoted by the expiry or expiration date.

We define the following variables and notation.
$t=0$ is the time when the forward contract is signed.
$T$ be the time to maturity or expiration.
$S_{t}$ denote the underlying asset's price at time $t$.
$K$ denote the strike price.
The exercise of an option is the act of paying/receiving the strike price to buy/sell the asset. If the option buyer exercises the option to buy or sell, the option seller (also called the option writer) is obligated to sell to or buy from the option buyer. An option must either be exercised by or on the expiration date or it becomes worthless.

A call is an option providing the right to buy. A put - an option providing the right to sell. Options can be exchange traded or can be over-the-counter. Options allow individuals and

## Page 4
companies to hedge and limit or constrain an outcome. Options provide a form of insurance protection from financial loss.

The exercise style of the option specifies the time at which exercise can occur. A European option can be exercised on a single specified date - the expiration date. An American option can be exercised at any time before or on the option's expiry date. A Bermudan option can only be exercised during specified periods but not for the entire time period of the option.

A covered option is when the investor writing (selling) the call or put option owns or is shorting the underlying asset. A covered call is a long position in the underlying asset and writing a call option on the same asset. A covered put is a short position in the underlying asset and writing a put option on the same asset. A naked position is when the investor does not hold the corresponding underlying long or short position, e.g., a naked call or a naked put. An investor writing a covered option receives the option's premium but limits upside profit potential as compared to a naked position.

Exchange options tend to be short-lived and have expiration dates such as 1 month, 3 months, 6 months, or 1 year from the issue date. Plain-vanilla options are options that have basic (simple) terms and are usually called options without using a qualifier. Exotic options are options with complex terms. Exotics go by names such as Asian, barrier, basket, binary, compound, lookback, rainbow, and swaption.

For example, an Asian option provides a payoff based on an average price over a specified period of time. The spot price could be based on an average or the strike price could be based on an average. The average could be an arithmetic or geometric average. This contrasts with American and European options where the payoff is based on the underlying asset's price at a specific point in time, i.e., the exercise date. Buying and selling Asian options allows investors or companies to manage cost or revenue risks associated with the underlying at the average price over time instead of a spot price at one point in time.

An interest rate option has a strike rate rather than a strike price. The payoff is the difference between the strike rate and the underlying reference market rate times the notional face amount times the fractional day count for which the rate applies. An interest rate cap is a derivative which makes a payoff at the end of each interest rate period that the interest rate exceeds the strike rate. A caplet is a one period interest rate call, that is, the individual payoff corresponding to a single interest rate period. An interest rate cap can be viewed as a combination or series of caplets over successive periods. An interest rate floor is a derivative which makes a payoff at the end of each interest rate period that the interest rate is below the strike rate. A floorlet is a one period interest rate put. An interest rate floor can be viewed as a combination or series of floorlets over successive periods. Each caplet and floorlet is settled in cash at the end of the period. An interest rate collar is the combination of an interest rate cap and floor with the same underlying rate, maturity and notional principal amounts.

Options can be used to hedge risks associated with guarantees in variable annuity products, indexed products, and other products.

## Page 5
For a call option in general, if the underlying's market price at expiration $S_{T}$ is greater than the strike price $K$, the payoff is the difference $S_{T}-K$; otherwise, the payoff is zero. The buyer (long call) receives the payoff, and the seller (short call) pays the payoff. We write this mathematically as payoff $=\max \left(0, S_{T}-K\right)$.

Figure 4.1a illustrates the call payoffs in general.
Figure 4.1a

Long and short calls are mirror images, i.e., symmetric about the $x$-axis.. The long call's slope is +1 and the short call's slope is -1 . For each $\$ 1$ change in $S_{T}$ above the strike price, the payoff increases or decreases by $\$ 1$.

Now let's consider puts. For a put option in general, if the underlying's market price at expiration $S_{T}$ is less than the strike price $K$, the payoff is the difference $K-S_{T}$; otherwise, the payoff is zero. The buyer (long put) receives the payoff, and the seller (short put) pays the payoff. We write this mathematically as payoff $=\max \left(0, K-S_{T}\right)$.

Figure 4.1b illustrates the put payoffs in general.
Figure 4.1b

Long and short put are mirror images, i.e., symmetric about the $x$-axis.. The long put's slope is 1 and the short call's slope is +1 . For each $\$ 1$ change in $S_{T}$ below the strike price, the payoff decreases or increases by $\$ 1$.

Furthermore, the long call and long put payoffs are symmetric about the vertical line $S_{T}=K$ as are the short call and short put payoffs.
![Page 5 Image 1](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p05_img1.jpg)
![Page 5 Image 2](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p05_img2.jpg)

## Page 6
# 4.1.2 Moneyness 

At any time on or before expiration, if exercised immediately (even if the option cannot be exercised such as a European option), an option is said to be
in-the-money if the payoff would be positive,
out-of-the-money if the payoff would be negative, and
at-the-money if the payoff would be close to zero .
A call option is in-the-money if $S>K$, out-of-the-money if $S<K$, and at-the-money if $S \approx K$. A put option is in-the-money if $S<K$, out-of-the-money if $S>K$, and at-the-money if $S \approx K$. An option's intrinsic value is the value if it were exercised immediately: $\operatorname{Max}(0, S-K)$ for a call and $\operatorname{Max}(0, K-S)$ for a put. An option's time value is its price in excess of the intrinsic value: Option Price $=$ Intrinsic Value + Time Value

At expiration, an option's time value is zero. Prior to expiration, an option's time value reflects the possibility that the underlying price will change to increase the payoff. A call is at least equal to $S-K$ and most equal to $S$. A put is at most equal to $K-S$ and least equal to $S$.

### 4.1.3 Option Values

LTAM Part I Chapter 10.4 develops a binomial option pricing model to calculate an option's value. A brief summary is provided.

The binomial option pricing model assumes that
Over each single time period, the underlying's price can move up or down only by a specified multiplicative factor, i.e., the price follows a binomial distribution.

Other values besides the up and down prices are not allowed (possible) during or at the end of each period. With this assumption, a no-arbitrage price can be determined. The binomial method constructs a replicating portfolio for the option thereby transforming the problem of determining the call price to constructing the replicating portfolio and determining its price.

We started with a European call option on a non-dividend paying stock with stock price $S$. Let $\boldsymbol{u}$ and $d$ denote the multiplicate factors for the stock's up and down price movement, that is, at the time to maturity $T$ the stock price is either $S u$ or $S d$. Let $c_{u}$ and $c_{d}$ denote the call price or payoff at $T$ from an up and down movement respectively.

Figure 4.2

## Page 7
Stock Prices

Call Prices

We construct a replicating portfolio by considering the following two portfolios,
Portfolio I: long call
Portfolio II: buy $\Delta$ shares of stock and lend $B$ at the risk-free rate, i.e., buy zero-coupon bond

We want the two portfolios' payoffs at $T=h$ to be equal for each possible outcome - whether the stock goes up to $S u$ or down to $S d$. If the stock goes up, $c_{u}=S u \Delta+B e^{r h}$ and if the stock goes down, $c_{d}=S d \Delta+B e^{r h}$, where $r$ is the continuous risk-free rate.

Solving the equations algebraically, we derived the following equations:

$$
\begin{aligned}
& \Delta=\frac{c_{u}-c_{d}}{S u-S d} \\
& B=e^{-r h} \frac{u c_{d}-d c_{u}}{u-d} \\
& c=S \Delta+B=e^{-r T}\left(\frac{\left(e^{r h}-d\right)}{u-d} \times c_{u}+\frac{\left(u-e^{r h}\right)}{u-d} \times c_{d}\right)
\end{aligned}
$$

We then considered an $n$-period lattice, that is, a lattice with $n$ steps and $h=T / n$ with $n$ becoming large. See LTAM Part I Examples 10.6-10.11. Visually tracking prices across time results in a lattice, hence the method is described as the binomial lattice method.

Figure 4.3
![Page 7 Image 1](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p07_img1.jpg)
![Page 7 Image 2](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p07_img2.jpg)

## Page 8
The model is practical and a tractable method which is relatively simple yet useful. It requires only algebra to solve two equations with two unknowns and does not require advanced mathematics. The model can price options for which there are no closed-form analytical solutions such as the Black-Scholes formula. The model is flexible and agile. We can price options with early exercise dates, adapt it for exotics, incorporate decisions and consumer behavior, and support assumptions such as non-constant volatility.

Using lattices to determine prices is similar to how calculus uses rectangles to determine area or how TVs and screens use pixels. While a few rectangles, pixels, or lattices appear simplistic or might be lossy, the use of many converges to the area, image, or option value.

Figure 4.4

# 4.1.4 Stochastic Processes and Black-Scholes 

A Wiener process is a continuous-time stochastic process, often called a Brownian motion. A Brownian motion is the random motion of particles suspended in a fluid (a liquid or a gas) resulting from their collision with the fast-moving molecules in the fluid. Think of the particles' motions as tracing a path, and as applied to finance, the path of prices over time.

We can mathematically write functions and equations including differential equations and integrals and then solve these equations. The stochastic process will specify the drift (if there was no randomness, is the particle moving in one direction or along a path?) and the infinitesimal variance $\sigma^{2}$ (the random shock along the path). The drift could be zero. The larger the variance, the more the particle or price could deviate from the path. If we define the processes and parameters, we can calculate values.

A landmark result for the price of a European call option with strike price $K$ with time to expiry $T$ with no dividends paid prior to $T$ was introduced by Fischer Black, Myron Scholes, and Robert Merton in a 1973 research paper. Let $S_{T}$ be the stock price at time $T$. Assume $S_{T}$ is a lognormal distribution, i.e., $\ln \left(S_{T}\right)$ is normally distributed with mean $\mu$ and variance $\sigma^{2}$ (as annual rates of return). As with the binomial model, there are six inputs to the Black-Scholes formula:
$S$, the current price of the stock;
$K$, the strike price of the option;
$\sigma$, the volatility of the stock;
$r$, the continuously compounded risk-free interest rate;
![Page 8 Image 1](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p08_img1.jpg)
![Page 8 Image 2](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p08_img2.jpg)
![Page 8 Image 3](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p08_img3.jpg)

## Page 9
$T$, the time to expiration; and
$\delta$, the dividend yield on the stock
The Black-Scholes formula is

$$
c=S e^{-\delta T} \times N\left(d_{1}\right)-K e^{-r T} \times N\left(d_{2}\right)
$$

where $N(x)$ is the cumulative normal distribution function, and

$$
\begin{aligned}
& d_{1}=\frac{\ln (S / K)+\left(r-\delta+\frac{\sigma^{2}}{2}\right) \times T}{\sigma \sqrt{T}} \\
& d_{2}=d_{1}-\sigma \sqrt{T}
\end{aligned}
$$

Using the same assumptions, the binomial lattice calculation converges to Black-Scholes value.
Black-Scholes is developed from the following stochastic process,

$$
d S_{t}=\mu S_{t} d t+\sigma S_{t} d W_{t}
$$

where $t$ is time, $S_{t}$ is the underlying asset's price at $t, \mu$ is the expected rate of return (expected drift), and $\sigma$ is the underlying asset volatility, and $d W_{t}$ is a Wiener process (or Brownian) motion.

# 4.2 The Greeks and Delta Hedging 

As background material we review the Greeks and delta hedging from LTAM Part I Chapter 10.
A hedge is an investment position taken to offset changes, losses, or gains incurred by an individual or organization's assets and liabilities. Hedging is a risk management technique to manage outcomes. Consider an investor that owns asset $X$. Suppose as $X$ changes value, another asset $Y$ 's value changes by an amount equal and opposite to $X$. We say $Y$ is a perfect hedge of $X$. Owning $Y$ eliminates risk in a portfolio position owning by "locking in" the outcome.

We could form a partial hedge by buying less units of $Y$ so that $Y$ 's value changes less than $X$ 's, e.g., $75 \%$ of $X$. We could over-hedge by buying more so that $Y$ 's value changes by more than $X$ 's, e.g., $120 \%$ of $X$. A hedge ratio is the ratio of the protected or hedged position to the entire position ( $100 \%, 75 \%$, and $120 \%$ in the perfect, partial, and over-hedged examples).
![Page 9 Image 1](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p09_img1.jpg)

## Page 10
Hedges do not lock in profit. Hedges do not magically turn losses into profits - they approximately protect or lock in a position. "Lock" should not be taken too literally. Hedges do not protect against all risks - an investor must choose which risks it is hedging. Furthermore, hedges have execution risk especially for complex asset and liabilities such as variable annuities. Hedges are not a zero-value proposition - they are not free; the cost of the hedge instruments is not the same as the value of the starting portfolio.

# PONDER 

How does an option's value change when the stock price changes?

Define delta $(\Delta)$ as the ratio of the change in the option price divided by the ratio of change in the underlying asset's price or to be more mathematically precise, $\Delta$ is the partial derivative of the option with respect to $S$,

$$
\Delta=\frac{\text { change in option price }}{\text { change in underlying price }}=\frac{\partial c}{\partial S} \text { or } \frac{\partial p}{\partial S}
$$

The binomial option pricing model's replicating portfolio is the key to the Ponder's answer and provides important insights and implications. Consider the context of a call option. The replicating portfolio is $c=S \Delta+B$. If $S$ changes by 1 , then $c$ changes by $\Delta$. The replicating portfolio's $\Delta$ is the same as the $\Delta$ defined above, which is why $\Delta$ is used to denote the number of replicating shares and not some other letter. We can also observe consistency in the usage of delta from the replicating portfolio's solution,

$$
\text { Call } \Delta=\frac{c_{u}-c_{d}}{S u-S d}
$$

which is the ratio of the change in the binomial's call prices to the change in the underlying's prices. A put $\Delta$ also equals $\left(c_{u}-c_{d}\right) /(S u-S d)$, however a call's $\Delta$ is positive whereas a put's $\Delta$ is negative.

If an investor sells an option, then a position owning $\Delta$ shares approximately offset any change in the options's value.

In the Black-Scholes framework: Call $\Delta=e^{-\delta T} N\left(d_{1}\right)$ and a Put $\Delta=-e^{-\delta T} N\left(-d_{1}\right)$
Delta hedging is an investing strategy that hedges an option(s) price risk by taking an offsetting position with the same $\Delta$ resulting in a delta-neutral position, that is, the portfolio's $\Delta$ is 0 . However, since delta changes as time passes and the underlying price changes, to maintain a delta hedge a portfolio needs to be rebalanced.

Static hedging establishes a hedge position that is held a long time, e.g., until the end of the time horizon or infrequently adjusted. Dynamic hedging continuously monitors the position's

## Page 11
delta or other risk metrics and adjusts the hedge frequently such as weekly, daily, or hourly by buying and selling the underlying.

How does an option's value change when one and only one input changes? We consider the following inputs $S, K, \sigma, r, T$, the time to expiration; and
$\delta$, the annual dividend paid continuously expressed as a rate per underlying price
Risk metrics known collectively as the Greeks are defined as following.
Delta $(\Delta)$ measures the option price change for a change in $S: \Delta=\partial / \partial S$
Gamma $(\Gamma)$ measures the change in delta for a change in $S: \Gamma=\partial^{2} / \partial S^{2}$
Vega measures change in the option price for a change in volatility $\sigma: V e g a=\partial / \partial \sigma$
Theta $(\theta)$ measures the change in the option price for a decrease in $T: \theta=\partial / \partial T$
Rho $(\rho)$ measures the change in the option price for a change in $r: \rho=\partial / \partial \mathrm{r}$
Psi $(\psi)$ measures the change in the option price for a change in $\delta: \psi=\partial / \partial \delta$.
We can extend the Greeks from options to measuring the change in any asset or liability value from a change in an input.

Typically models are too complex to take derivatives mathematically and in practice, sensitivities are quantified by running the model with shocked values as described above. Using a derivative's definition, $\frac{f(x+h)-f(x)}{h}$, we apply a small shock $h$ to the sensitivity tested variable $x$ where " $f$ " is the model. If there is directional bias, we shock both up and down to minimize directional bias versus a standard calculus definition of change which only shocks in one direction. In this case we make an adaption and use $\frac{f(x+h)-f(x-h)}{h-(-h)}$.

We shock both up and down to minimize directional bias versus a standard calculus definition of change which only shocks in one direction, e.g., $i+$ shock. All assets and liabilities are not locally (i.e., within a small range) monotonically increasing, decreasing, or symmetric. In these cases, shocking in only one direction either up or down could be inaccurate and misleading.

For example, consider Rho $(\rho)$ which is the continuous risk-free equivalent of the interest rate risk metric duration. Let $\boldsymbol{i}$ denote a spot rate curve and let $h=10$ basis points $(0.1 \%)$. Using the same model that calculates Value using spot rate curve $\boldsymbol{i}$, let Up and Down equal the Value with a parallel curve shock up and shock down respectively, that is, Up = Value ${ }_{\text {@ } i+10 b p s}$ and Down $=$ Value ${ }_{\text {@ } i-10 b p s} .10$ basis points is commonly used in practice. Why? 10 basis points is small but not too small and is a nice round number. Then

## Page 12
(4.3a)

$$
\text { Rho }=\text { Duration }=-\frac{\text { Up }- \text { Down }}{\text { Value } \times 0.002}
$$

and

$$
\text { Convexity }=\left(\frac{\text { Up }- \text { Value }}{\text { Value } \times \text { shock }}-\frac{\text { Value }- \text { Down }}{\text { Value } \times \text { shock }}\right) / \text { shock }=\frac{\text { Up }+ \text { Down }-2 \times \text { Value }}{\text { Value } \times 0.001^{2}}
$$

Calculating Value and post-shock Up and Down values are straightforward using the discrete delta definition in a computer program - run the same model three times no matter how complex the model, assets, or liabilities.

# 4.3 Simulations 

As background material we briefly review Monte Carlo simulation from LTAM Part I Chapter 10.
In LTAM Part I Chapter 10 we stated the binomial option pricing model is useful and flexible, for example, adapting from European to American to exotic options. However, for complicated or path dependent options with $n$ time steps, there are $2^{n}$ paths and a full binomial lattice is computationally intensive. In practice, Monte Carlo simulation for economic scenarios is often used in long-term actuarial models. However, Monte Carlo simulation is also slow and alternatives have emerged and continue to emerge and evolve. Brute force methods can be prohibitively run-time expensive.

Monte Carlo simulation applies randomization as a tool to calculate values or solve problems. We first provide examples to illustrate the approach, provide additional background, and then discuss its application to long-term actuarial models.

## Example 4.1

We wish to calculate the value of $\pi$. You likely know $\pi$ is approximately 3.14 and is the area of a circle with radius 1 . But do you know how to calculate $\pi$ 's value to two decimals or to 8 or 12 decimals? There are "pure" mathematical methods to calculate $\pi$ including calculus and Taylor series. There is nothing random about $\pi$. How do we use random numbers to calculate $\pi$ ?

Consider a unit circle and square on an $x-y$ graph as in Figure 4.5, i.e. a circle with radius 1 and a square with length 2 .

Figure 4.5

## Page 13
We randomly generate two numbers $x$ and $y$ from the uniform distribution between -1 and 1: every point in the unit square has an equal chance or probability of being generated. The percentage of randomly generated points in the circle will be the ratio of the circle's area to the square's area or $\pi / 4$. Equivalently, a point is in the circle if $x^{2}+y^{2} \leq 1$. A computer can generate thousands or millions of points and evaluate whether or not $x^{2}+y^{2} \leq 1$. We generate $N$ points and take the ratio of points inside the circle to $N$. As $N$ becomes large, the ratio approaches $\pi / 4$ ! No calculus or complicated mathematics needed: a simple evaluation criterion (is $x^{2}+y^{2} \leq 1$ ? yes or no?) and computer power.

# End Example 4.1 

Although we could $\pi$ calculate directly, we can also estimate the value. Simulation becomes more powerful when we cannot or do not know how to calculate the value directly or when the direct method is unwieldy and time consuming. Simulation entails a tradeoff between calculating a value exactly (assuming we can mathematically solve for the value) and an approximation. How close is close enough?

We can apply similar methods to stock prices, options, and modeling insurance product cash flows and values. Now the question is how might we simulate a stock price? For assets and liabilities in general, different institutions and market participants use a variety of methods. Suppose we analyze daily stock prices. We could use an empirical probability distribution, fit a probability distribution such as a lognormal distribution to empirical data, or use a more sophisticated model that reflects parameters changing over time, e.g., mean, variance, or skewness. We could start with a specified stochastic process such as a Black-Scholes or Cox-Ingersoll-Ross model.

Our intent is not to dig into mathematical minutiae but to illustrate methodology. Again, without sophisticated mathematics - stochastic processes, differential equations, or riskneutral valuation equations - a model or statistical distribution and computer power can provide a reasonable approximation!

Furthermore, our model can be simple or sophisticated according to our needs. Stock price volatility and correlations with other variables can be a constant or non-constant over time.
![Page 13 Image 1](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p13_img1.jpg)

## Page 14
Similarly, we can value asset and liability cash flows entailing uncertainty and in particular, simulate complex insurance products with guarantees such as variable annuity Mxs, index annuities, and SGUL.

This method of randomly producing outcomes to calculate values is called the Monte Carlo method, develop by Stanislaw Ulam in the late 1940s while working at the Los Alamos National Laboratory. He named it after the Monte Carlo casino in Monaco which his uncle would visit.

A Monte Carlo method is a computational algorithm based on repeated random sampling to obtain numerical results. The algorithm uses randomness to solve problems whether or not the problem is deterministic or not. Monte Carlo methods are quite practical in many contexts.

Monte Carlo methods generally involve the following:
1 Construct or select an existing model.
a) Define and select the pertinent input variables.
b) Decide which inputs are modeled as certain vs. random (deterministically vs. stochastically). Let the certain variables be $X_{1} \ldots X_{m}$, the random variables be $Y_{1} \ldots Y_{n}$.
c) Specify the relationships and dependencies between variables.
d) Construct or select the model or software that performs the requisite calculations

2 Generate a scenario.
a) Specify values for the deterministic variables $X_{1} \ldots X_{m}$.
b) Generate values for the random variables $Y_{1} \ldots Y_{n}$ over the set of possible values

3 Compute all calculations treating all inputs as deterministic, i.e., certain.
4 Repeat steps 2 and 3 for the desired number of scenarios $N$.
5 Calculate the desired metrics from the outcome distribution.
In many stochastic long-term actuarial models, the only stochastically generated variables are the economic scenarios, that is, spot rate curves, market returns, etc.

Once we have specified distributions or models, we generate a set of random values $y_{1}, \ldots, y_{n}$ for each scenario. We use capital letters to denote the variables and lower-case letters to denote the values for a specific scenario. A common method is to generate random numbers between 0 and 1 from the uniform distribution and use the inverse cumulative distribution function. That is, if for $Y_{k}$ the cumulative distribution function is $P\left(Y_{k}\right)$ and the random number is $r$, then the randomly generated $y_{k}$ is such that $P\left(y_{k}\right)=r$, or $y_{k}=P^{-1}(r)$. Figure 4.6 illustrates this process visually.

Figure 4.6

## Page 15
For example, in a 6-year projection suppose we use a normal distribution with mean 100 and standard deviation 10 . We randomly generate the numbers $0.41,0.23,0.84,0.77,0.36$, and 0.68 in the interval $(0,1)$. Therefore, $y_{1}, \ldots, y_{6}=97.72,92.61,109.94,107.39,96.42$, and 104.68.

# 4.3.1 Random Numbers 

Random number generation is a process creates a sequence of numbers that cannot be reasonably predicted better than by random chance. A generated sequence will contain some patterns detectable in hindsight. A physical or hardware random number generator, called a true random number generator, generates each number based on the current value of a continuously changing physical characteristic, for example, electrical noise or nuclear decay.

A pseudo-random generator, often used by computer programs and applications, generates each number based on an algorithm, and hence are pre-determined. As they are not truly random, they are called pseudo-random numbers. A simple algorithm is a linear congruential generator such as $A_{i}=48271 A_{i-1} \bmod \left(2^{31}-1\right)$. The generated sequence of numbers is deterministic, reproducible (using the same seed $A_{0}$ ), and periodic (repeats). The idea is to have the modulus be a large prime number, and for this reason, Mersenne primes such as $2^{31}-1$ and $2^{61}-1$ were used in early computer programs.

The choice of multiplier ( 48,271 in the above example) is a critical choice in the quality of the random generator. Most multipliers generate sequences which fail tests for non-randomness. The challenges, non-randomness tests, and underlying theory are beyond scope. However, given a quality generator, pseudo-random numbers are easy to implement in a program and fast for a computer to produce. For this reason, this book treats random numbers necessary for simulations as inputs into our models and not as a preliminary model generating output.

A variation on a single linear congruential generator is to use two in combination. Bratley et al. present a method to generate uniform numbers on the interval $(0,1)$ using the following method:

$$
\begin{aligned}
& A_{i}=40014 A_{i-1} \bmod \left(2^{31}-85\right) \\
& B_{i}=40692 B_{i-1} \bmod \left(2^{31}-249\right)
\end{aligned}
$$
![Page 15 Image 1](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p15_img1.jpg)

## Page 16
$$
C_{i}=\left(A_{i}+B_{i}\right) \bmod \left(2^{31}-85\right)
$$

Bratley indicates that $A_{0}$ may be any seed provided $B_{0}$ is any of 1, 140822472, 905932980, 1185805228 , or 1749585844 . $C_{i} /\left(2^{31}-85\right)$ is the desired uniform number.

Excel provides functions RAND and RANDBETWWEN that output a random number between 0 and 1 and between two user-specified integers respectively. However, these functions have been demonstrated to be flawed and should not be used beyond illustrative examples.

Modern financial and actuarial software applications use high quality random number generators and are available as part of their libraries.

Once we have the inputs including the randomly generated $y_{1}, \ldots, y_{n}$, we use the model to perform the requisite calculations. Sometimes we are interested in a single value, for example, $N P V$ or a call option's price at $t=0$. Other times we are interested in many values: present values, surplus, income, sales, costs, and net cash flow for each month or year over the entire time horizon.

Although we often generate scenario inputs all at once including across the entire time horizon, the model must treat modeled events like actual events unfolding one period at a time. That is, the model does not have crystal ball foresight by looking into the future. If we model possible supplier disruptions and in the scenario a severe disruption occurs in year 4 of a 10-year projection, we cannot instruct the model to stockpile inventory in year 3 . We use the model's decision rules and the "data" known in year 3. In the context of ALM, if the scenario is: rates will increase rapidly and significantly in year 4 , then we cannot in year 3 instruct the model to act as if the future (year 4) is known. If we are running monthly projections, consumer behavior and company and competitor actions and reactions are based on what is known at that point in time in the projection.

We then use the power of computers, generating $N$ scenarios and producing $N$ outcomes, i.e., a distribution of outcomes, or what we have called a risk outcome curve. $N$ can be as small as 50 or 100 , or as large as 10,000 or million. $N$ depends on how long it takes to run one scenario. Does it take less than a second, seconds, minutes, or hours? The time to run a single scenario is an important consideration in constructing the model. A modeler balances tradeoffs between the model's intended purpose, model fidelity, complexity, and other operational considerations. Complexity is not always better and over-complex models can produce poor or flawed output for the business user's intended purpose.

# 4.3.2 Simulations and Risk Metrics 

Model simulation is used to obtain a distribution of many possible outcomes. An outcome distribution portrays a given scenario's outcome as a point with the range of outcomes along the horizontal $x$-axis and the likelihoods or probabilities associated with those outcomes along the vertical $y$-axis.

## Page 17
Suppose a simulation model is run for 1,000 scenarios. Figure 4.7 presents a histogram of net present values (NPV) of earnings grouped into ranges of $\$ 15$ million. The probability of each range is the percent of scenarios that fall in that range, e.g., NPV is between $\$ 45$ and $\$ 60$ million for 171 or $17.1 \%$ of the scenarios. Model outputs in addition to earnings often include supporting details, financial statements, and metrics, such as number of customers.

Figure 4.7 Monte Carlo Results: Net Present Value (in millions)

We can generate a continuous risk outcome curve by smoothing out the top of histograms' rectangles. A distribution of outcomes provides insights into the level and degree of uncertainty in results, or in other words, the project's financial risk. We can calculate metrics and statistics on the results, such as the mean, variance, and percentiles. We can also make statements such as "the probability of a loss is $5.7 \%$ " calculated by adding the probabilities with net income less than zero: $0.7 \%+1.0 \%+1.5 \%+2.5 \%$. We use these metrics to measure risk, i.e., the degree of uncertainty in the outcomes.

A distribution or outcome curve's tails are the area underneath the curve to the far left (left tail) and to the far right (right tail), i.e., really bad outcomes or really good outcomes. The words "heavy", "fat", "light", and "thin" are commonly used to describe the amount of area in the tails, that is, how many or what percent of the outcomes are in the tails. The words "long" and "short" are commonly used to describe how far from the middle the tails are, that is, how big the good or bad outcome can be relative to average or expected outcome.
especially for normal distributions. Events or outcomes are often described by how many standard deviations they are away from the mean, for example a 2 -standard deviation event or
![Page 17 Image 1](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p17_img1.jpg)
![Page 17 Image 2](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p17_img2.jpg)

## Page 18
a 4-standard deviation event. We then quantify impacts from financial losses to flood water levels to manufacturing defects. For a normal distribution (bell curve), two to six standard deviations correspond to:

| Standard Deviation | Chances of happening |
| :--: | :--: |
| 2 | 1 in 22 |
| 3 | 1 in 370 |
| 4 | 1 in 16 thousand |
| 5 | 1 in 1.7 million |
| 6 | 1 in 507 million |

The chances of happening rapidly decrease as the number of standard deviations from the mean increases. A normal distribution's tails are "short" and "light." Most of the curve's area is in the middle: $68 \%$ is within one standard deviation and $95 \%$ is within two standard deviations.

However, the outcome distributions of various insurance products such as VAs with GMxBs have distributions with fat-tails. T Simulations provide insights into how the outputs behave in the tails. Two common risk measures used by financial institutions are Value at Risk (VaR) and Conditional Tail Expectation (CTE). CTEs are used for long-term insurance modeled reserves and capital.

Risk is the effect of uncertainty. How do we quantify this effect? Let's recast the definition as: risk is a level of uncertainty from expectation within the context of objectives. Expected is a probabilistic expectation, and expected is not used in the sense of a planned expectation, although a plan can assume most likely outcomes. "Level of uncertainty" is then relative to the expectation.

Risk, as uncertainty, needs to be measured across the result profile, that is, measure horizontal distances in a histogram or outcome curve. Let's recast the definition as: risk is a level of uncertainty from expectation within the context of objectives. "Expected" is a probabilistic expectation. Level of uncertainty is then relative to the expectation.

Both Value at Risk and Conditional Tail Expectation measure risk relative to the expected value AND at a level of certainty, i.e., use the mean and the $N^{\text {th }}$ percentile or ( $100-N^{\text {th }}$ ) percentile depending on the whether the perspective is losses or profits.

# Value at Risk (VaR) 

Suppose the objective is profits. We illustrate Value at Risk at the 95\% level, i.e., we use the 5\%tile. This means $95 \%$ of the results are better, i.e., $95 \%$ of the area of the curve is to the right and $5 \%$ to the left. Figures 4.8a-b illustrate VaR(95).

Figure 4.8a Value at Risk: VaR(95) on Profits

## Page 19
The risk, or uncertainty, is measured as the difference of the expected result minus the 5\%-tile. This measure is called Value at Risk, or VaR for short, and to denote the level of uncertainty, we denote as VaR(95). VaR is the distance between the mean and the 5\%-tile. The expected result is the statistical mean; i.e., $50 \%$ of the curve's area is to the right of the expected result and $50 \%$ to the left. Note that the expected profit is already reflected in the return calculation.

A common alternative definition is VaR equals the 5\%-tile, but we wish to measure the loss relative to the expected result and not the absolute loss measured relative to 0 .

For example, suppose the expected result is $\$ 400,000$ and the $5 \%$-tile profit is a loss of $\$ 1.6$ million. Then VaR(95) is $\$ 400,000$ less negative $\$ 1.6$ million, or $\$ 2$ million. Similarly, we can measure risk at the 99 percent level, which is VaR(99). Suppose the $99 \%$-tile is a loss of $\$ 2.1$ million. Then VaR(99) is $\$ 2.5$ million. These statements can be translated as: there is a $95 \%$ chance that the outcome will not be more than $\$ 2$ million worse than the expected mean of $\$ 400,000$, and there is a $99 \%$ chance the outcome is not worse by $\$ 2.5$ million. We can use any percentile, which we denote by $N: N \%$-tile.

Value at Risk at the N-percentile level or VaR(N), equals the mean less the (100-N)\%-tile's value. If the objectives are negative outcomes such as claim losses, the left-right orientation of the graph is reversed as in Figure 4.8b, and $\operatorname{Var}(N)$ is the $N \%$-tile less the mean.

Figure 4.8b Value at Risk: VaR(95) on Claim Losses
![Page 19 Image 1](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p19_img1.jpg)

## Page 20
# Conditional Tail Expectation (CTE) 

Conditional tail expectation is similar to VaR except instead of using the percentile's value which is the start of the tail, we use the average in the tail or the average of results worse than the specified percentile. In other words, given the condition that an event in the tail has occurred, the conditional tail expectation is the value that is expected, i.e., the average. Figure 4.9 illustrates CTE(95).

Figure 4.9 Conditional Tail Expectation: CTE(95) on Profits
$50 \%$ to the left. Note that the expected profit is already reflected in the return calculation.

As with VaR, a common alternative definition is CTE equals the average in the $5 \%$-tile, but we wish to measure the loss relative to the expected result and not the absolute loss measured relative to 0 .
![Page 20 Image 1](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p20_img1.jpg)
![Page 20 Image 2](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p20_img2.jpg)

## Page 21
Conditional Tail Expectation at the N\%-level or CTE(N), equals the mean less the average in the tail, i.e., average of outcomes worse than the N\%-tile. CTE is also known as Tail Value at Risk or TVaR(N). It follows from the definitions that $\operatorname{CTE}(N) \geq \operatorname{VaR}(N)$. CTE can be significantly larger for long fat-tailed outcome distributions. For example, in measuring CTE at the 95 percent level, consider the average outcome of the worst $5 \%$ outcomes. Suppose the tail average is $\$ 4$ million. Then the risk measure, or CTE(95) or TVaR(95), is $\$ 400,000$ minus negative $\$ 4$ million, or $\$ 4.4$ million.

Visually, the $N \%$-tile indicates $N \%$ of the curve's area, i.e., percent of outcomes, lies to the right and (100-N)\% lies to the left. The expected result is the statistical mean. $50 \%$ of the curve's area is to the right of the expected result, and $50 \%$ to the left.

Simply shifting the entire curve to the right so that $99 \%$ of outcomes are positive or to the left so that only $1 \%$ of outcomes are positive does not change the amount at risk. The difference between the expected results and the percentiles changes by the same amount, so the difference does not change. Changing the shape of the curve can change the mean, the values where the N\%-tile occurs, and the averages in the tail.

# Example 4.2 

Consider the output from 1,000 simulations calculating the present value of claims less charges for a variable annuity with a guaranteed minimum death benefit presented in Figure 4.10 Column C. Column A ranks the values in in ascending order which is most profitable to least profitable. Column B is the scenario number.

Figure 4.10

|  | A | B | C | D | E | F |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | VA with GMDB Stochastic Results |  |  |  | Risk Measures |  |
| 2 | Rank | Scenario | PV(Claims - Charges) |  |  | PV(Claims - Charges) |
| 3 | 1 | 465 | $(17,097)$ |  | Average | $(3,431)$ |
| 4 | 2 | 161 | $(14,549)$ |  | Std Dev | 3,552 |
| 5 | 3 | 246 | $(13,598)$ |  | VaR(70) = 70\%-tile | $(1,846)$ |
| 6 | 4 | 200 | $(13,285)$ |  | CTE-70 | 843 |
| 7 | 5 | 727 | $(12,837)$ |  | CTE-98 | 5,099 |
| 8 | 6 | 204 | $(12,479)$ |  |  |  |
| 702 | 700 | 822 | $(1,848)$ |  |  |  |
| 703 | 701 | 184 | $(1,844)$ |  |  |  |
| 1001 | 999 | 104 | 6,051 |  |  |  |
| 1002 | 1,000 | 467 | 8,014 |  |  |  |

Statistical risk metrics are calculated in Cells F3..F7 using Excel functions for average, standard deviation and percentile,

$$
\begin{aligned}
& \text { F3 }=\text { AVERAGE }(\mathrm{C}: \mathrm{C}) \\
& \mathrm{F} 4=\operatorname{STDEV}(\mathrm{C}: \mathrm{C}) \\
& \text { F5 }=\text { PERCENTILE.INC }(\mathrm{C}: \mathrm{C}, 0.7)
\end{aligned}
$$

## Page 22
Excel does not have functions for conditional tail expectations (CTE) equal to the averages in the tail or the worst ( $100-\mathrm{N}) \%$ of scenarios. We calculate CTE-70 and CTE-98 as the average of scenarios 701-1000 and 981-1000 respectively,

$$
\begin{aligned}
& \text { F6 = AVERAGE(C703:C1002) } \\
& \text { F7 = AVERAGE(C983:C1002) }
\end{aligned}
$$

We could have alternatively calculated CTEs as

$$
\begin{aligned}
& \text { F6 = SUMIFS(C:C, A:A,">700") / } 300 \\
& \text { F7 = SUMIFS(C:C, A:A,">980") / } 20
\end{aligned}
$$

# End Example 4.2 

### 4.3.3 Insurance Products

Recall, policyholder behavior is any action taken by a policyholder who has the right to exercise policy rights and options including, but not limited to, surrender, lapse, withdrawals, fund transfers, deposits, premium payments, policy loans (taking and repaying), annuitization, or benefit elections. Mortality and morbidity events are not policyholder behaviors. Policyholder behavior can be extremely challenging in setting assumptions and how to incorporate behavior and feedback mechanisms in the model.

Many insurance products such as variable annuities contain embedded options. Policyholders have the option to withdraw some or all of the funds prior to maturity when it is no longer advantageous to do so, for example, when the guarantee is deeply out-of-the-money. By surrendering the policy, the policyholder forgoes paying GMxB charges or "option premium". If the account value is much greater than the guarantee value, surrendering and repurchasing a new contract with identical features is equivalent to resetting the base and beginning a new guarantee term.

Embedded options and guarantees in retail insurance and wealth management products are more complex and challenging to model than plain vanilla options traded in financial markets. GMxB values are based on long-term guarantees, are path-dependent, and depend on policyholder behavior.

In our discrete cash flow model, each model time step (a spreadsheet row) corresponds to a lattice node. Each simulated economic scenario mirrors one path in a lattice. A binomial lattice consisted of a spot price $S_{k}$ and the call or put's option value $c_{k}$ or $p_{k}$. A variable annuity (VA)'s model projection node consists of the account value, guarantee base value and a number of options that the policyholder can elect from benefit utilization, partial withdrawals, surrenders, transferring funds between subaccounts. Values, cashflows, and payoffs are path dependent on policyholder behavior. For example, higher ITM-ness is tied to lower surrender activity.

## Page 23
In Part II, we enhance the LTAM model to use a simulated economic scenario for input market returns and interest rates. Chapter 8-9's Example use a VBA macro to run 1,000 simulations. Consider Chapter 9's variable annuity examples. Outcomes are sorted by the present value of net claims in ascending order which is most to least profitable. Net claims are the insurer's payouts in excess of the account less the contract charges assessed the policyholders. Figures 4.10c-d present one of Chapter 9 example's simulation results.

Figure 4.10c PV(Net Claims) as a Percent of Account Value

Figure 4.10d PV(Net Claims) Frequency

# 4.3.4 Speed and Efficiency 

Monte Carlo can be slow. For complex insurance blocks of business - asset projections run in tens of minutes, liability projections can take tens of hours to run. For complicated or path dependent guarantees including embedded options described in Chapters 5 and 7-9 or LTAM Part I Chapter 4 and 10, there can be millions of possible paths.
![Page 23 Image 1](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p23_img1.jpg)
![Page 23 Image 2](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p23_img2.jpg)

## Page 24
How many scenarios N produce an acceptable outcome distribution's shape? We can determine the number of scenarios necessary to reach the point at which additional iterations provide no additional information about the shape of distribution. In testing, one usually compares a small number of scenarios such as 250 or 1000 with the results from a larger number such as 1,000 or 10,000. Monte Carlo can be computationally intensive to converge and produce risk profiles. We describe several methods to improve efficiency.

The control variate method estimates the error on each trial by using the price of a related option that does have a pricing formula which is used to improve the accuracy of the Monte Carlo price on each trial.

The antithetic variate method uses the idea that for every simulated realization, there is an opposite and equally likely realization. Draw a random normal number $z$, then also use $-z$. The two are negatively correlated reducing the variance of the estimate.

Stratified sampling methods stratify (partition) the region in which random numbers are generated. Generate random numbers from each percentile of the uniform distribution $U(0,1)$ and use the inverse cdf function. For the $k^{t h}$ draw $u_{k}$, use $u_{k} / 100+(k-1) \times 0.01$ which is uniformly distributed over the $k^{t h}$-percentile. This generates a random number for each percentile of normal distribution. This can be generalized to multiple dimensions when option payoffs depend on multivariable or in the case of insurance products.

# 4.4 Economic Scenario Generators (ESGs) 

In many stochastic long-term actuarial models, the only stochastic variables are economic scenarios where a scenario represents future interest rate curves, market returns, inflation, foreign exchange rates, etc. An economic scenario generator (ESG) is a model that simulates relevant future values of economic and financial market variables. ESGs are self-named and generate economic scenarios often used in conjunction with other models. For example, ESG outputs are inputs into long-term actuarial cash flow models., e.g., Chapter 4 and 8-9's models.

In long-term actuarial models, discount rates and fixed-income and equity returns are critical to calculating liability and asset cash flows and values. Scenarios include future interest rate paths including spot rate curves (or equivalently forward rate curves or par yield curves) for various term structures such as sovereign yields and corporate spreads or equivalently yield curves of different credit qualities. Scenarios can also include financial market returns like bonds, stocks, and real estate and economic variables such as inflation, GDP, and unemployment rates. ESGs can extend across multiple sovereigns incorporating foreign exchange rates to global institutions.

Applications of ESGs are widespread in financial institutions, supporting both market-consistent valuations and real-world risk management to understand tail risks. Market-consistent valuations adhering to risk-neutral and arbitrage-free conditions focus on reproducing observable prices of traded assets to determine comparable prices for non-traded instruments.

## Page 25
Real-world models, on the other hand, generate forward-looking economic dynamics, helping managers gauge the likelihood of future events and their business impacts.

ESGs model the uncertainty and variability of economic and financial factors thereby helping institutions and individuals understand the potential impact on their financial position and risk profile and providing insights into how different economic scenarios affect business strategies and objectives. ESGs are integral inputs to valuation and risk management models of complex assets and insurance liabilities including the determination of reserve and capital requirements by enabling future cash flow projections over a range of economic scenarios. ESGs are also essential to the evaluation of asset-liability management, investment, and hedging strategies, and capital allocation.

ESGs can be described using Chapter 1's model input-throughput-output structure.

| Model | Inputs | Throughputs | Outputs |
| :-- | :-- | :-- | :-- |

ESGs contain several inter-related components and models such as an interest rate model, an equity return model, parameterization, and calibration. Choices related to ESG design and construction vary depending on business purpose. Steps in constructing an ESG entail

1) establishing purpose, e.g., valuation, pricing, economic capital
2) model design which includes which risk factors are modeled and selecting discrete or continuous models for interest rates, equities, and other economic variables,
3) parameterization which includes determining data,
4) calibration which is an iterative process to modify parameters so output aligns with purpose,
5) determining output: real-world or risk-neutral scenarios, number of scenarios, time step
6) scenario generation, and
7) validating and reviewing the scenario set for consistency and appropriate interrelationships.

The throughput's calculation engine structure may utilize cascade structures, correlations, or direct relationships. ESG output scenarios can be real-world scenarios and/or risk-neutral scenarios. Each output scenario consists of specified financial variables at time steps over the projection period. For example, a scenario could consist of spot rate curves and equity returns at each month-end over a 50-year period.

ESGs can generate a broad range of scenarios, reflecting various potential future economic conditions. By running thousands of simulations, ESGs offer a comprehensive view of possible outcomes, providing a richer and more nuanced understanding of potential risks and opportunities. This extensive range of scenarios is much more informative than a limited set of deterministic scenarios, which cannot capture the full spectrum of possible future states.

ESGs inherently account for the complex interrelationships between different economic variables. By simulating these variables together, ESGs produce scenarios that reflect realistic

## Page 26
and intricate interactions, which would be challenging to replicate using deterministic models. This complexity is essential for understanding compound outcomes resulting from multiple interacting factors, providing a more robust basis for decision-making. Despite their advantages, ESGs also have limitations that need to be understood and managed.

It is challenging for ESGs to produce realistic plausible scenarios to reflect market participant behavior and how interest rates and equity returns should evolve over time. ESG output scenario requirements are encapsulated by specifying acceptance criteria and an accepted set of stylized facts. In social sciences, especially economics, a stylized fact is a simplified presentation of an empirical finding. In the context of an ESG, a stylized fact is a qualitative or quantitative property the scenario(s) should have.

Some models reflect economic cycles or include mean reversion. For example, when interest rates are very high or low or the rate curve is very steep or inverted, a model incorporates a bias to revert at a parameterized speed towards a mean target level. Mean reversion reflects that central banks and governments implement monetary and fiscal policies when interest rates fall outside a target or desirable range.

Validation and review analyze output sets of scenarios for consistency with acceptance criteria and stylized facts and for calibrated models, that calibrations are consistent with calibration criteria. Analysis includes comparing averages and various percentiles, using fan charts and histograms, and back-testing.

ESG model details are beyond scope, are complicated, technical, and require much judgment in their construction and their application. As with several beyond-scope topics in this book, we refer the reader to Figure 4.11's outstanding whitepapers providing comprehensive overviews, technical and non-technical details, discussions on the component models such as interest rate models and equity models, considerations, and examples. Chapter 4.4.1 provides a summarized overview.

# 4.11 ESG Whitepapers 

Conning, "Economic Scenario Generators - A Practical Guide." SOA Research Institute 2016
"Evolution of economic scenario generators: a report by the Extreme Events Working Party members." Cambridge University Press 2019

Conning, "A User's Guide to Economic Scenario Generation in Property/Casualty Insurance." CAS Research Papers, 2020

Ahlgrim, Kevin C., D'Arcy, Stephen P., and Gorvett, Richard W., "Comparison of Actuarial Financial Scenario Generators." Casualty Actuarial Society 2021

Strommen, Stephen J., "Understanding the Connection between Real-World and RiskNeutral Scenario Generators." SOA Research Institute 2022

Ambagaspitiya, Rohana and Ford, Charles, "Calibrating Interest Rate Models" SOA Research Institute 2023

## Page 27
# Book's ESG and Scenarios 

In this book we use the American Academy of Actuaries Interest Rate Generator (AIRG Version 7.1.202305) jointly produced by the American Academy of Actuaries (the Academy) and Society of Actuaries (SOA). The AIRG models U.S. Treasury rates and equity and bond returns.

The AIRG was first developed in the early 2000s. It has undergone a number of versions and is updated annually. The AIRG is used in current U.S. regulatory reserving and capital regimes including VM-20, VM-21, VM-22 (which are life, variable annuity, and non-variable annuity reserve requirements respectively) and in C3-Phase II capital requirements. The AIRG "software" is a user-friendly Excel spreadsheet with worksheet tabs: Scenario Generator, Single Scenario, Scenario Subsets, Parameters, MRP (mean reversion parameters), and Historical Curves. Various tabs contain documentation on methods, parameterization, and parameter values.

The user specifies inputs in tab Scenario Generator which has a macro button "Generate Scenario". User inputs are: starting date, yield curve on starting date (key rates), number of scenarios (menu choices are 10,000, 1,000, 500, 200, 100, 50, or VM-20's SERT Scenarios), years to project, digits to retain after decimal, time step (menu for monthly, quarterly, semi-annual, and annual), output folder, file format, and output rate (menu for spot rates or bond equivalent yields). Historical interest rates are input in tab Historical Curves allowing the user to update the AIRG beyond the publish date.

For inputs, we updated the historical yield curves, set the starting date and yield curve as of 12/31/23. We used the prescribed scenario picker tool built into AIRG Version 7.1 to generate equity returns and spot rate curves for a 60-year projection period. We output scenarios with monthly time steps and with annual time steps to support different examples.

Outputs are the following asset classes/fund names, in zipped csv files.
U.S. Treasury interest rates: $0.25,0.5,1,2,3,5,7,10,20$, and 30 -years

Equity index fund returns: Money market bond, U.S. intermediate-term government bonds, U.S. long-term corporate bonds, Diversified equity, Diversified balanced allocation, Diversified large cap U.S. equity, Diversified international equity, Intermediate risk equity, Aggressive or specialized equity,

In the AIRG,

- interest rates and equity returns are independent,
- a mean-reversion parameter for interest rates is included.
- interest rates are independent of all other model factors including equity and bond returns,
- the correlation matrix is constant,
- variance reduction techniques are not used,
- bond index returns are modeled as a function of interest rates,
- Equity returns use a monthly stochastic log volatility mode.

## Page 28
This book uses a subset of 1,000 real-world scenarios randomly selected from 10,000 integrated interest rate and equity return generated scenarios. In the Example and Exercise spreadsheets, we have tabs named Scen200 and Scen1000 with the applicable timestep and data.

We used the diversified large cap U.S. equity output which is the accumulated value of $\$ 1$ over the projection period. We converted the accumulated wealth factors into annual rates of return: the returns in Cells B3..BI1002 are range named Scenario_1000_Equity.

Figure 4.12a Example Annual U.S. Equity Returns

|  | A | B | C | D | E | BG | BH | BI |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | US Equity Returns |  |  | Year |  |  |  |  |
| 2 | Scenario | 1 | 2 | 3 | 4 | 58 | 59 | 60 |
| 3 | 1 | $36.4 \%$ | $-4.1 \%$ | $-5.9 \%$ | $41.5 \%$ | $17.0 \%$ | $5.7 \%$ | $-8.3 \%$ |
| 4 | 2 | $15.8 \%$ | $1.3 \%$ | $17.4 \%$ | $21.9 \%$ | $34.4 \%$ | $-5.4 \%$ | $5.5 \%$ |
| 5 | 3 | $-0.2 \%$ | $54.8 \%$ | $6.6 \%$ | $-4.6 \%$ | $34.6 \%$ | $1.5 \%$ | $6.3 \%$ |
| 1000 | 998 | $17.7 \%$ | $17.0 \%$ | $22.9 \%$ | $-1.6 \%$ | $8.3 \%$ | $9.6 \%$ | $1.8 \%$ |
| 1001 | 999 | $19.6 \%$ | $3.8 \%$ | $-2.4 \%$ | $18.6 \%$ | $-4.9 \%$ | $-13.9 \%$ | $-4.5 \%$ |
| 1002 | 1000 | $16.2 \%$ | $7.0 \%$ | $5.3 \%$ | $2.6 \%$ | $-10.7 \%$ | $11.0 \%$ | $-1.2 \%$ |

Spot rate curve output is listed by scenario and project year in rows and maturities in columns. The output has rates for $0.25,0.5,1,2,3,5,7,10$, and 30 -year maturities. For space purposes we only store the spot rates used in the example. Cells BM3..BN61002 are range named Scenario_1000_Rate.

Figure 4.12b Example Annual U.S. Treasury Spot Rates

|  | BK | BL | BM | BN |
| :--: | :--: | :--: | :--: | :--: |
| 1 | US Treasury Spot Rate Curve |  |  |  |
| 2 | Scenario | Year | 7 | 10 |
| 3 | 1 | 0 | $3.979 \%$ | $3.891 \%$ |
| 4 | 1 | 1 | $4.966 \%$ | $4.963 \%$ |
| 5 | 1 | 2 | $5.032 \%$ | $4.951 \%$ |
| 1000 | 17 | 21 | $2.366 \%$ | $2.496 \%$ |
| 1001 | 17 | 22 | $2.301 \%$ | $2.484 \%$ |
| 1002 | 17 | 23 | $2.220 \%$ | $2.423 \%$ |
| 1003 | 17 | 24 | $2.329 \%$ | $2.482 \%$ |
| 61000 | 1000 | 58 | $2.604 \%$ | $2.650 \%$ |
| 61001 | 1000 | 59 | $2.315 \%$ | $2.402 \%$ |
| 61002 | 1000 | 60 | $2.635 \%$ | $2.721 \%$ |

Details on the Academy's equity scenario generator is on the Academy's webpage: C3-Phase II Risk-Based Capital for Variable Annuities: Pre-Packaged Scenarios

## Page 29
The AIRG does not model risk-neutral scenarios or have risk-neutral market calibration capabilities. AIRG's real-world scenarios are not appropriate for use in market-consistent valuation.

# ESG Implementation Project 

ESGs have evolved over the last several decades and are continuing to evolve. The NAIC began an ESG Implementation Project in 2020 to update the AIRG/ESG. The RFP (request for proposal) was award to Conning. For project information, see Life Actuarial (A) Task Force (LATF) Section of the NAIC's Website. ESG Exposure documents can be found in the tab "Exposure Drafts". Some ESG implementation reference material is contained in tab "Documents".

The Principle-Based Reserving (PBR) Section on the NAIC's Website has two sections under Economic Scenarios. The first section, "Economic Scenarios, Tools, Training Materials, and Documentation" contains a link to ESG landing page on Conning's website. The second section, "Stylized Facts and Acceptance Criteria" contains numerous links to presentations and files related to the ESG's requirements including features of a good ESG, and stylized facts and acceptance criteria for treasury (interest rate) models, equity models, and corporate models.

In addition, LATF and related workgroups gave a number of presentations during 2022-23.
Interest Rates- Update on proposed Acceptance Criteria
Corporate Credit \& Bond Fund Returns - Stylized Facts, Acceptance Criteria, and a Simplified Model

## Economic Scenario Generator (ESG) Stylized Facts for Equities

The CAS/Conning whitepaper states,
"Here are some of the high-level features of a good ESG:

- It produces simulation results that reflect the economic view of the risk manager.
- Scenarios are consistent with realistic market dynamics.
- A large simulation should produce some extreme but plausible results (i.e., the simulation covers and moderately exceeds the benchmark stylized facts).
- Component models and architecture must have sufficient flexibility to serve in multiple roles.

If one discusses the essential features of a good ESG with a diverse group of ESG experts, those experts' lists of features and the relative importance of those features will vary. However, they will set forth a common core of ideas that can serve as a checklist of best practices. The following is a list and general discussion of those ideas.

A good ESG,

## Page 30
has a solid methodological foundation for the way the models are built and the way the variables are interrelated, and models are parsimonious, practical, and comprehensive.
...
provides a comprehensive suite of macroeconomic and financial variables and a multieconomy capability. ...
can accommodate many types of calibration views across a wide range of benchmarks.
produces simulation results that reflect a relevant view. ...
produces some extreme but plausible outcomes. ...
embeds realistic market dynamics. ...
is computationally efficient and numerically stable. ...
has fast and robust recalibration capabilities. ...
meets the requirements of regulators and auditing firms. ...
produces sufficient simulation detail for extensive validation. ..."

For examples of stylized facts, the 2023 LATF Interest Rate presentation describes the stylized facts guiding the ESG treasury model.

# "1. Level of Interest Rates 

The level of interest rates (the cost of borrowing money) changes due to a variety of complex and interrelated factors (e.g., supply of and demand for financing, business cycle, GDP, inflation, central bank actions to stimulate the economy or control inflation).
a. Short-term rates (which the Fed has more control of) have generally fallen within a range of $0 \%$ to $20 \%$ and have most often been within the lower part of that range. Longterm rates have generally been within 300 bps of short-term rates.
b. Negative interest rates are possible (have been observed outside the U.S.) but unlikely due to structural and market differences between the U.S. and other economies.
c. Interest rates can exhibit multi-year trends (e.g., up, down, low-for-long). Interest rates can stay at very low levels for several years. Short-term rates can stay very near their lower bound for several years while higher long-term rates continue to fluctuate.

## 2. Volatility of Interest Rates

The volatility of interest rates varies over time, with periods of both high and low volatility.
a. Monthly changes in interest rates are generally limited in size (less than 80 bps ) but changes tend to be greater when the level of interest rates is higher.
b. Monthly changes in short-term rates tend to be larger than monthly changes in longterm rates when short-term rates are not near their lower bound, but the opposite relationship tends to hold when short-term rates are near their lower bound.
c. Volatility tends to increase in stressed markets.

## 3. Term Structure of Interest Rates (shape of yield curve)

The yield curve embodies the term structure of interest rates and takes a variety of shapes.

## Page 31
a. The normal yield curve shape is upward sloping (long-term rates greater than shortterm rates) and concave downward. Normal yield curve shapes can persist for extended periods of time.
b. Non-normal yield curve shapes include inversions (downward sloping), humps, and valleys. Inversions (and other non-normal yield curve shapes) are often associated with key points in the business cycle (e.g., recession indicator) but generally don't persist for extended periods of time.
c. The slope of the yield curve tends to be lower (even negative/inverted) when shortterm rates are at relatively high levels."

For more details on the ESG component models' acceptance criteria and stylized facts see the various whitepapers and presentations. Visit the NAIC's LATF website for the latest ESG updates and discussions.

# 4.4.1 ESG Overview 

There are numerous crucial choices in designing and constructing an ESG including determining data sources and which data, specifying stylized facts, appropriate steady-state levels, determining initial conditions, identifying key parameterization targets, and controlling the expected mean reversion path (e.g., level and speed of reversion to the mean). Expert judgment may be applied to superimpose short-term views of the future to account for current economic conditions and consensus expectations, for example, influenced by central bank policies.

ESG inputs consist of historical and current economic and financial variable data relevant to the scenarios' output. For example, this book's ESG inputs into the AIRG did not include corporate spreads, non-U.S. sovereign rates, foreign exchange rates, GDP, or other economic data.

ESG throughputs consist of several interrelated models or components for key scenario variables including each model's parameterization. Models must be selected for each key variable. Interest models include the Heath-Jarrow-Morton model, Vasicek model, Hull and White model, Cox-Ingersoll-Ross model, and Nelson-Siegel model. Equity models include the Black-Scholes, Heston, and stochastic volatility with jumps model.

Many interest rate and equity models are stochastic processes, that is, they are specified as stochastic differential equations which the ESG model parameterizes and simulates using a random number generator. Models based on stochastic process have various parameters such as drift, volatility (or use stochastic volatility), long-run means, and speed of reversion. For example,

$$
d r_{t}=\mu(r, t) d t+\sigma(r, t) d X_{t}
$$

where $X_{t}$ is a Wiener process and $\mu(r, t)$ and $\sigma(r, t)$ are the drift and volatility components respectively.
We could have a simple stochastic process with constant drift and volatility,

## Page 32
$$
d r_{t}=\mu d t+\sigma d X_{t}
$$

or the stochastic process could incorporate mean reversion,

$$
d r_{t}=a\left(m r p-r_{t}\right) d t+\sigma d X_{t}
$$

where $a$ is the speed of reversion and $m r p$ is the mean reversion parameter, i.e., the long-term level of $r$. In a simulation, the further $r$ drifts from $m r p$, the larger the propensity for $r$ to drift towards mrp.

ESG component models need to be parameterized using statistical and analytical methods and correlation methods used to ensure simulated variables are consistent. An ESG is initialized with historical data and observed market prices as of scenario start date.

Initially generated scenarios may not satisfy the ESGs intended purpose. Calibration modifies the parameters in cascade order. For risk-neutral scenarios, parameters are calibrated to replicate current market prices and be arbitrage-free. Calibrated scenarios are said to be market consistent. Calibrated scenarios are only applicable to determine values of securities similar those used in the calibration. For real-world scenarios, parameters are calibrated to satisfy specified stylized facts. Scenarios could also be left as is, i.e., uncalibrated.

# Throughput Structure 

In ESGs, accurately modeling the relationships between economic and financial variables is essential. These relationships can be structured in several ways, each with unique characteristics and applications.

Some variables are simultaneously generated, e.g., in an n-factor model, n variables are determined simultaneously. As the number of joint variables increases the number of correlations required increases significantly (pair-wise combinations are $n(n-1) / 2$ ). In addition, calibration becomes increasingly difficult.

Many ESGs structurally use a waterfall or cascade method previously described in Chapter 3.4. Typically, "waterfall" is used in the context of assumptions and sensitivities and "cascade" is used in the context of ESGs and dynamic assumptions. Suppose all the variables have a specified order and are indexed from 1 to N. A cascade method determines each subsequent variable(or set of variables), say variable $m$, in the cascade based on upstream variables (i.e., already calculated variables $1, \ldots, m-1$ ) and values of variable $m$ at previous time steps. Both the simulation process to create the initial scenarios and the calibration process follow the same cascade order/structure.

A cascade structure starts with a variable(s) serving as a primary driver for other variables. For example, many ESGs start with interest rates. A 1-factor interest rate model would simulate the risk-free rate or a short-term rate such as 3-month sovereign bond. An $n$-factor interest rate model would simulate $n$ key interest rates at different maturities. These simulated values at projection time step $k$ along with all variable values prior to time step $k$ alongside more random numbers are then used as inputs to simulate the next cascade step's variables.

## Page 33
Figure 4.13 A Cascade Structure

The throughput's component models such as interest rate and equity models can be discrete or continuous. Recall, discrete-time models simulate economic variables at specific intervals, providing a straightforward approach to capturing changes over time. Continuous-time models model changes continuously. Many ESGs use continuous-time models as the underlying foundation but simulate variables on a discrete time basis, e.g., daily, monthly, or quarterly.

In addition, factor models and copula models may be used for some variables. Factor models use underlying factors to drive the simulation of multiple variables, ensuring consistency and reducing dimensionality. Copula models simulate the joint distribution of variables, allowing for complex dependencies and correlations.

Each approach has its advantages and is suited to different scenarios depending on the analysis objectives, such as short-term versus long-term projections or specific regulatory requirements. The choice of approach depends on the goals of the analysis and the specific characteristics of the economic environment being modeled.

# Risk-Neutral and Real-World Economic Scenarios 

Understanding real-world and risk-neutral frameworks is crucial for advanced financial modeling. Real-world frameworks consider the actual behavior and risk preferences of market participants. Output scenarios represent plausible future real-world outcomes. In contrast, riskneutral scenarios do not represent plausible future real-world outcomes. A risk-neutral framework, which assume that all investors are risk-neutral, are used for market-consistent valuations. In risk-neutral valuations, financial instrument prices are equal to the expected value of the discounted possible future cash flows and values. Nuanced considerations are beyond scope and we refer the reader to Figure 4.11's whitepapers.

## Conclusion

ESGs offer a sophisticated and powerful tool for simulating a wide range of economic scenarios, providing valuable insights for risk management and strategic planning. However, their implementation and use come with challenges that require careful management.
Understanding these benefits and limitations allows for better utilization of ESGs, ensuring they provide accurate and meaningful insights while mitigating potential risks and maintaining operational efficiency.
![Page 33 Image 1](ltam_ii_chapter4_20240625_stochastic_modeling_assets/ltam_ii_chapter4_20240625_stochastic_modeling_p33_img1.jpg)

## Page 34
# 4.5 Dynamic Assumptions 

A static assumption is such that the assumption's values do not change during the model's projection period. This does not mean the assumption's values are constant or does not have granularity to reflect characteristics such as age, policy year, sex, risk class, face band, or product. It does mean that the assumption does not change as external economic and financial factors change such as interest rates or equity returns. A static assumption's values are independent of external factors or how the product performs, and are the same for different economic scenarios.

A dynamic assumption is such that the assumption's values change during the model's projection period for one or more scenarios. A dynamic assumption reflects an expectation that policyholder behavior is affected or changes due to projection nodes' economic and/or demographic conditions (within scenarios) and their effect on policy's contractual values and guarantees.

Dynamic assumptions and other scenario-dependent relationships are used to model policyholder behavior, company actions, and third-party actions that depend on how values and other variables change over the economic scenarios. Stochastic models, simulation, and dynamic assumptions provide insights into policyholder behavior risks, mortality, morbidity, asset-liability management, and inform company actions such as investment and hedging strategies and the use of reinsurance.

There are contexts where anticipated policyholder behavior can be appropriately represented by static assumptions. For example, all of LTAM Part I's whole life and level term lapse rates including the post-level periods were static assumptions as behavior on these products are interest-rate insensitive, i.e., the need for mortality protection is largely unaffected by changes in interest rates and market returns.

Dynamic assumptions and actions include:

- policyholder behavior such as lapses, benefit utilization, premium persistency and payment patterns and exercising embedded optionality such as annuitization and commencement of GMWB withdrawals, investment allocations or transfers,
- assets/debt assumptions such as defaults and mortgage and loan prepayments,
- company actions such as sales, products, and non-guaranteed elements such as UL and annuity credited rates, dividend rates, premium rate increases, investment and reinvestment strategies, hedging strategies, capital management, uses of reinsurance, debt issuance, and refinancing,
- third-party actions such as reinsurers, distributors, and competitor rates and premiums.

Dynamic assumptions are often intertwined, not only affecting the model's current projection period but other assumptions in subsequent time periods within the projection. For example, as interest rates change, the insurer's portfolio rates change, policyholder credited rates changes,

## Page 35
and competitors' rates change. Surrender rates vary with the relationship between the rate a policyholder is currently earning and the rates offered by competitors reflecting the surrender charge paid upon surrender. On the asset side, interest rate changes affect debtholders behaviors such as refinancing and defaults.

Model variables affected by dynamic assumptions are typically calculated using a cascade structure. Dynamic assumption values should span a plausible range of policyholder behaviors consistent with the scenarios' emerging variables. Dynamic assumptions should be two-sided to increase or decrease assumption rates as appropriate to reflect different types of external conditions. A one-sided assumption, e.g., rates only increase or only decrease should be judiciously used after analysis such as sensitivity testing.

Consistency between interdependent assumptions is challenging. Policyholder behavior is hard to predict but critical to product performance and risk profiles, especially products with extensive embedded optionality. The model should reflect reactions to actions taken within the projection to emerging conditions, for example, a company's action to change credited rates, premium rates, or fees.

For interest-sensitive products, changes in interest rates influence how renewal credited rates are adjusted. The speed and magnitude of credited rate changes can impact lapse assumptions, which in turn may affect other assumptions like mortality and premium payments. Higher credited rates may lead to lower lapse rates depending on competitor rates.

Reducing interest credited rates or dividend scales may prompt additional lapses or premium payments. Increasing non-guaranteed premiums leads to higher policyholder lapses, surrenders, or conversions, particularly among healthier individuals. We observed in LTAM Part I that level term premium jumps at the end of the level period resulted in anti-selection and higher mortality for persisting policyholders. Premium increases have a similar effect.

Policy guarantees become more valuable and attractive to policyholders in scenarios where interest rates are decreasing or remain low or favorable market returns are followed by large decreases This could lead to lower lapse rates, increased premium payments, or the exercise of guaranteed benefit options. For example, deferred annuities and UL with secondary guarantees, lapse rates decrease when the guarantee becomes valuable.

These qualitative relationships highlight the interconnected nature of economic conditions, product features and performance, policyholder behavior, company actions and third-party actions.

Figure 4.14 provides several simplistic examples of dynamic assumptions. The reader does not need to understand what all the variables and relationships mean, but should appreciate the dynamic nature of the relationships compared to the static assumptions used in Chapters 2-3 and in LTAM Part I.

Figure 4.14 Illustrative Dynamic Assumptions

## Page 36
# Example 1: Fixed Annuity 

Competitor Rate $=\max ($ 5 -year treasury, 36 -month average of the 5 -year treasury).
Reinvestment strategy is a 20/30/50\% allocation between 5-, 10-, and 20-year A-rated corporate bonds.

Bond/Mortgage Prepayment Rate is a generalized linear model using loan/mortgage rate, call premiums, and current market rates and credit spreads.

Renewal Credited Rate = Portfolio Rate - Target Spread.
Surrender Rate $=\max (25 \%$, Base Rate + Dynamic Excess)
where Dynamic Excess $=\left[6 \times\left(\right.\right.$ Competitor Rate $\%$ - Credited Rate $\left.\%-0.5 \%\right)^{1.7}\right] / 100 \times(1-8$ $\times$ Surrender Charge Rate).

## Example 2: Fixed Indexed Annuity with GLWB

Dynamic Lapse = Base Lapse * [Surrender Value / PV(Future GLWB Withdrawals)] ${ }^{0.8}$

## Example 3: Variable Annuity

In-the-moneyness (ITM) = ratio of guaranteed benefit value to account value.
GMIB Utilization Rate is,

| ITM\% | Utilization Rate |
| :--: | :--: |
| $<120 \%$ | $3 \%$ |
| $120 \% \leq$ ITM $<150 \%$ | $5 \%$ |
| $150 \% \leq$ ITM $<180 \%$ | $10 \%$ |
| $>180 \%$ | $20 \%$ |

## Example 4: Variable Annuity

GMIB Utilization Rate $=a_{0}+a_{1} I T M+a_{2} I T M^{2}+a_{3} I T M^{3}$

## Example 5: Variable Annuity

Surrender Rate = Predictive Model (e.g., a generalized linear model) on key predictors from variables such as surrender charge level, in-the-moneyness, benefit utilization status, attained age, policy year, distribution channel, presence of a product feature or rider such as GMxB, return of premium, or secondary guarantee, account value band, investment restriction, M\&E fees, roll-up rate, etc.

### 4.6 Exercises

## [under development]

## True or False

1 A European call option can be exercised any time prior to the option's expiry date.
2 A put option's strike price is $\$ 100$. On the expiry date, the underlying's market price is $\$ 105$. The option's payoff is $\$ 5$.

## Page 37
# Describe or explain briefly 

Compare a long forward position and short forward position
Compare a long call position and a short put position.
Compare a short call position and a long put position.
Describe a stock option's delta. How is it used?
An investor implements a static hedge for a position in a stock and European call. Explain why the position is not riskless for the life of the option.

## Calculations