_Note: Source document was split into 7 OCR chunks (pages 1-2, pages 3-13, pages 14-16, page 17, pages 18-19, pages 20-25, pages 26-35) to stay within token limits._

# CS10 LocalGLMnet a deep learning architecture for actuaries

## Page 1
# LocalGLMnet: a deep learning architecture for actuaries 

Jürg Schelldorfer* ${ }^{*}$ Mario V. Wüthrich ${ }^{\dagger}$<br>Prepared for:<br>Fachgruppe "Data Science"<br>Swiss Association of Actuaries SAV

Version of August 4, 2021


#### Abstract

The purpose of this tutorial is to discuss the LocalGLMnet architecture which is tailored to the needs of actuaries. The LocalGLMnet is a flexible network architecture for tabular data that allows for variable selection, the study of interactions, gives nice interpretations and allows to rank variable importance. We explore a LocalGLMnet on accident insurance claims data for which we also have short claim descriptions. In a second step we try to understand the predictive power of these claim descriptions by adding a recurrent neural network layer to process the claim texts into tabular data.


Keywords. LocalGLMnet, neural network, deep learning, variable selection, interactions, explainable artificial intelligence, XAI, generalized linear model, GLM, tabular data, variable importance, Shapley additive explanation, natural language processing, NLP, text recognition, recurrent neural network, long short-term memory cell, LSTM.

## 0 Introduction and overview

This data analytics tutorial has been written for the working group "Data Science" of the Swiss Association of Actuaries SAV, see
https://www.actuarialdatascience.org
The purpose of this tutorial is twofold. Firstly, we discuss the LocalGLMnet architecture of Richman-Wüthrich [21] which provides a new network architecture for tabular data that is interpretable, allows for variable selection, allows for the study of interactions, and which allows to rank variables according to their importance. We study this LocalGLMnet proposal on synthetic accident insurance data. This accident insurance data is supported by small claim descriptions, and in a second step we apply text recognition tools to see whether these claim descriptions allow for improving the prediction accuracy. For integrating these claim descriptions into the LocalGLMnet architecture we use a recurrent neural network layer which turns the claim texts into tabular data.

[^0]
[^0]:    *Swiss Re, Juerg_Schelldorfer@swissre.com
    ${ }^{\dagger}$ RiskLab, Department of Mathematics, ETH Zurich, mario.wuethrich@math.ethz.ch

## Page 2
# 1 Empirical analysis of claim data 

The available data describes synthetic accident insurance claims. ${ }^{1}$ We drop 10 claims with claim occurrence year 1987. This provides us with 99 '990 claims, all having occurred between 1988/01/01 and 2006/07/20. These claims have been reported in the calendar years from 1998 to 2008. The maximal reporting delay is 1 '042 days, this corresponds to 2.85 years or to almost 149 weeks. Figure 1 shows the accident dates vs. the reporting delays of these claims (in weekly

Figure 1: Accident dates vs. reporting delays in weekly units, the orange vertical lines show the $90 \%, 97.5 \%$ and $99 \%$ quantiles, and the cyan dots give the weekly averages.
units), the cyan dots give the weekly averages; in average we have a reporting delay of 5.56 weeks. The orange vertical lines show the $90 \%, 97.5 \%$ and $99 \%$ quantiles at 11,26 and 39 weeks. From this plot we cannot detect any trends in reporting delays, i.e., it suggests a stationary reporting behavior over time.
The claim amounts of these accident insurance claims range from 20 to 3 '136'046. Figure 2 shows empirical plots of these claim amounts. On the left-hand side we show the empirical density plot being unimodal, and on the right-hand side the log-log plot indicating heavy-tailedness, i.e., resembling asymptotically a straight line with negative slope.

These claims are supported by 9 covariates shown on lines 6-14 of Listing 1. We will not further discuss the meaning of these covariates as their names are rather self-explanatory. Line 15 gives a short claim description, and line 16 the initial case estimate. We further analyze the 9 covariates on lines 6-14 of Listing 1. Moreover, the accident date, accident daytime and the reporting date, see lines 3-5 of Listing 1, allow us to calculate time related variables such as the

[^0]
[^0]:    ${ }^{1}$ https://www.openml.org/d/42876; this data set was kindly created and provided by Colin Priest, while similar, it is not identical to the data set used in www.kaggle.com/c/actuarial-loss-estimation.
![Page 2 Image 1](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p02_img1.jpg)

## Page 3
Figure 2: (lhs) Empirical density of claim amounts truncated at 10'000, (rhs) log-log plot of claim amounts.

Listing 1: Excerpt of the accident claim data.

```
data.frame': 99990 obs. of 16 variables:
$ ClaimNumber : chr "WC1592772" "WC1592805" "WC1592809" "WC1592818" ...
$ AccDate : Date, format: "2005-01-13" "1994-09-28" "1991-11-11" ...
$ AccTime : int 9 15 14 8 9 7 14 14 14 12 ...
$ RepDate : Date, format: "2005-01-24" "1994-10-17" "1992-04-16" ...
$ Age : int 45 40 19 18 34 50 46 19 19 21 ...
$ Gender : Factor w/ 2 levels "F","M": 2 2 1 1 2 1 2 2 2 1 ...
$ MaritalStatus : Factor w/ 3 levels "M","S","U": 2 1 2 3 1 2 1 2 2 2 ...
$ DependentChildren : int 0 0 0 0 0 0 0 0 0 0 ...
$ DependentsOther : int 0 0 0 0 0 0 0 0 0 0 ...
$ WeeklyPay : int 500 283 0 373 200 517 0 200 767 200 ...
$ PartTimeFullTime : Factor w/ 2 levels "F","P": 1 1 1 2 1 1 1 1 1 1 ...
$ HoursWorkedPerWeek : int 38 38 0 2 6 38 0 38 40 37 ...
$ DaysWorkedPerWeek : int 5 5 5 4 5 5 5 5 5 5 ...
$ ClaimDescription : chr "MOVING DISC STRAINED RIGHT SHOULDER" "BOILING ...
$ InitialCaseEstimate: num 9500 3000 250 1000 400 1000 550 110 9700 9500 ...
$ Claim : int 102 1451 48 492 191 320 133 108 7110 8378 ...
```

reporting delay, which has been illustrated in Figure 1, but also the weekday of the accident, the accident month and the accident year. We are going to use this information as covariates for claim prediction because claims maybe influenced by the daytime, the weekday, the season expressed by the calendar months, and the accident year in case of non-stationarity. In Figure 13 in the appendix we show the number of claims and the average claim amounts per AccYear, AccMonth and AccWeekday; all plots of average claim amounts have the same $y$-scale. For the last year 2016 we only have data until July 20. We observe that claim averages are increasing over time. AccMonth is fairly uniform and we have less accidents on weekends, however, this does not significantly influence the claim averages. Figure 14 shows AccTime and RepDelay. Accidents during night times are less frequent but more expensive, and reporting delay does not have a major impact on claim averages. We censor reporting delay at 100 days, because of
![Page 3 Image 1](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p03_img1.jpg)

## Page 4
scarcity of data beyond and because of right-skewness of reporting delays.
Figure 15 shows Age, Gender and MaritalStatus. For regression modeling, we will censor Age at ages 16 and 70 because observations beyond these censoring points are scarce. Figure 16 shows DependentChildren, DependentsOther and WeeklyPay. We will censor DependentChildren and DependentsOther at 1, to differentiate 0 and 1, this provides us with binary variables. WeeklyPay is shown censored at 1'200. Figure 17 shows PartTimeFullTime, HoursWorkedPerDay and DaysWorkedPerWeek. HoursWorkedPerWeek is censored at 60. The levels of these covariates show some sensitivities in claim averages, and our goal is to fit a regression model to the individual claim sizes to understand systematic effects in the claim amounts and the significance of these differences.
Analyzing dependence between covariate components, see Table 8 in the appendix, we find positive correlation between WeeklyPay, Age, DaysWorkedPerWeek and HoursWorkedPerWeek, which, of course, makes perfect sense from a practical point of view. We also find positive correlation between AccYear and HoursWorkedPerWeek. A further analysis of this positive correlation shows that it comes from the fact that in the early years from 1988 to 1994 roughly 1'500 claims per year have HoursWorkedPerWeek equal to 0 , and after 1994 such zeros have almost completely disappeared. Probably such zeros in early years are missing data; to not distort our analysis, we will simply drop these claims which leaves us with 89'332 claims.

# 2 Data pre-processing 

### 2.1 Covariate pre-processing

For successful regression modeling we need to pre-process (raw) covariate information. We have already mentioned in the previous section how we censor certain covariates. Moreover, continuous and binary variables are normalized to having zero mean and unit variance, i.e., having raw covariates, the $j$-th raw covariate component $x_{i, j}^{\text {raw }}$ of claim $i$ is normalized by

$$
x_{i, j}^{\mathrm{raw}} \mapsto x_{i, j}=\frac{x_{i, j}^{\mathrm{raw}}-\operatorname{mean}\left(x_{i, j}^{\mathrm{raw}}\right)}{\operatorname{stddev}\left(x_{i, j}^{\mathrm{raw}}\right)}
$$

where the empirical mean and the empirical standard deviation (stddev) are calculated for fixed component $j$ over all available claims $i$.

Standardization of continuous and binary variables to zero mean and unit variance is going to be important because comparison of variables requires that they live on the same scale.

Categorical (nominal) variables with more than two levels are pre-processed by one-hot encoding. Assume that the $j$-th raw covariate component is a categorical variable with $L$ levels labeled by $c_{1}, \ldots, c_{L}$. One-hot encoding maps these $L$ levels to the $L$ unit vectors of the Euclidean space $\mathbb{R}^{L}$. Thus, having raw categorical variable $x_{j}^{\text {raw }}$, we receive its one-hot encoding by the embedding

$$
x_{j}^{\text {raw }} \mapsto\left(\mathbb{1}_{\left\{x_{j}^{\text {raw }}=c_{1}\right\}}, \ldots, \mathbb{1}_{\left\{x_{j}^{\text {raw }}=c_{L}\right\}}\right)^{\top} \in \mathbb{R}^{L}
$$

Note that one-hot encoding is different from dummy coding. Dummy coding selects a reference level and maps the levels different from the reference level to the $L-1$ unit vectors of the Euclidean space $\mathbb{R}^{L-1}$. Dummy coding leads to full rank design matrices which is important in

## Page 5
GLM. One-hot encoding does not give full rank design matrices because we have one redundancy in this encoding, however, this is exactly needed, here, and it will be explained below.

We require one-hot encoding for categorical variables with more than two levels. This does not lead to full rank design matrices, however, this is not a necessary property in the LocalGLMnet approach.

We denote the resulting pre-processed covariate of claim $i$ by $\boldsymbol{x}_{i, j} \in \mathbb{R}^{16}, 13$ components coming from continuous or binary variables, and we have 1 categorical variable MaritalStatus with 3 levels. We denote the input dimension by $q=16$.

Outlook 2.1 In the first part of this tutorial we work with tabular covariate information. This is the most suitable data to work with within the LocalGLMnet architecture. In the second part of this tutorial we also perform text recognition where we use the claim descriptions on line 15 of Listing 1. These claim descriptions will first be embedded into Euclidean spaces before using this information in the LocalGLMnet architecture. A similar approach can be used for time series, spatial or image data using recurrent neural networks (RNNs), see RichmanWüthrich [20] for RNNs, or convolutional neural networks (CNNs), see Meier-Wüthrich [14] for CNNs. The same also applies to the use of attention layers and embedding layers in the case of categorical covariate components, see Section 2.2 in Schelldorfer-Wüthrich [23] for embedding layers.

# 2.2 Learning and training data 

To perform a proper out-of-sample generalization analysis we partition our data into a learning data set $\mathcal{L}$ and a test data set $\mathcal{T}$. We hold on to the same partitioning throughout this tutorial to have comparability across all methods studied. The learning data set $\mathcal{L}$ will be used for model fitting (this includes early stopping rules in gradient descent fitting), and the test data set $\mathcal{T}$ will only be used for out-of-sample predictive performance analyses. For information about generalization analysis (GA) we refer to Chapter 4 in Wüthrich-Merz [31], in particular, Section 4.1.3 provides a decision-theoretic approach to forecast evaluation using strictly consistent scoring functions and Section 4.2 describes cross-validation (CV).
The empirical analysis of our data has shown that the claim averages are non-stationary over time and that claim sizes follow a highly skewed distribution. To have learning and test data sets sharing similar properties w.r.t. claim sizes we partition the entire data in a stratified way into learning data set $\mathcal{L}$ and test data set $\mathcal{T}$ in a ratio $4: 1$. That is, we order the claims w.r.t. their claim sizes. Then, we select at random 1 claim from the 5 biggest ones for $\mathcal{T}, 1$ claim from the 5 second biggest ones for $\mathcal{T}$, and so on, and the non-selected claims are allocated to $\mathcal{L}$. This random allocation provides us with a learning data set $\mathcal{L}=\left(Y_{i}, \boldsymbol{x}_{i}\right)_{1 \leq i \leq n}$ of size $n=71^{\prime} 466$ and a test data set $\mathcal{T}=\left(Y_{t}^{\dagger}, \boldsymbol{x}_{t}^{\dagger}\right)_{1 \leq t \leq \tau}$ of size $\tau=17^{\prime} 866$, with $Y_{i}$ and $Y_{t}^{\dagger}$ denoting the claim sizes and with $\boldsymbol{x}_{i} \in \mathbb{R}^{q}$ and $\boldsymbol{x}_{t}^{\dagger} \in \mathbb{R}^{q}$ denoting the covariate information; we distinguish learning and test data by using a super-script ${ }^{\dagger}$ and by using different lower indexes.

The general assumption is that all data $\left(Y_{i}, \boldsymbol{x}_{i}\right)$ and $\left(Y_{t}^{\dagger}, \boldsymbol{x}_{t}^{\dagger}\right)$ are independent and identical

## Page 6
distributed (i.i.d.), ${ }^{2}$ and we are going to determine the conditional distribution (in-sample) of $Y_{i}$, given $\boldsymbol{x}_{i}$, which can then be used to forecast (out-of-sample) $Y_{t}^{\dagger}$, given $\boldsymbol{x}_{t}^{\dagger}$.

# 3 Tweedie's family for claim size modeling 

### 3.1 Tweedie's distributions

The most popular family of distribution functions for regression modeling is the exponential dispersion family (EDF). An attractive sub-family within the EDF is Tweedie's family [28] which is extensively studied in Jørgensen [9, 10]; we also refer to Chapter 2 in Wüthrich-Merz [31]. Tweedie's family contains, among others, the Gaussian, the Poisson, the gamma and the inverse Gaussian models. The density within Tweedie's family takes the following general form

$$
Y \sim f(y ; \theta, v / \varphi)=\exp \left\{\frac{y \theta-\kappa_{p}(\theta)}{\varphi / v}+a(y ; v / \varphi)\right\}
$$

with exposure $v>0$, dispersion parameter $\varphi>0$, canonical parameter $\theta \in \boldsymbol{\Theta}_{p}$ in the effective domain $\boldsymbol{\Theta}_{p} \subseteq \mathbb{R}$, normalization $a(\cdot ; \cdot)$ not depending on the canonical parameter $\theta$, and cumulant function $\kappa_{p}: \boldsymbol{\Theta}_{p} \rightarrow \mathbb{R}$ given by

$$
\kappa_{p}(\theta)= \begin{cases}\frac{1}{2-p}((1-p) \theta)^{\frac{2-p}{1-p}} & \text { for } p \in \mathbb{R} \backslash((0,1] \cup\{2\}) \\ \exp \{\theta\} & \text { for } p=1 \\ -\log (-\theta) & \text { for } p=2\end{cases}
$$

For $p \in(0,1)$ there do not exist any Tweedie's distribution functions, see Theorem 2 in Jørgensen [9]. Tweedie's family is summarized in Table 1.

| $p$ | distribution | support of $Y$ | $\boldsymbol{\Theta}_{p}$ |
| :--: | :-- | :--: | :--: |
| $p<0$ | generated by extreme stable distributions | $\mathbb{R}$ | $[0, \infty)$ |
| $p=0$ | Gaussian distribution | $\mathbb{R}$ | $\mathbb{R}$ |
| $p=1$ | Poisson distribution | $\mathbb{N}_{0}$ | $\mathbb{R}$ |
| $1<p<2$ | Tweedie's compound Poisson distribution | $[0, \infty)$ | $(-\infty, 0)$ |
| $p=2$ | gamma distribution | $(0, \infty)$ | $(-\infty, 0)$ |
| $p>2$ | generated by positive stable distributions | $(0, \infty)$ | $(-\infty, 0]$ |
| $p=3$ | inverse Gaussian distribution | $(0, \infty)$ | $(-\infty, 0]$ |

Table 1: Tweedie's family; this table is taken from Table 4.1 in Jørgensen [10].
The characterizing property of Tweedie's family is that a Tweedie distributed random variable $Y$ has the first two moments for canonical parameter $\theta \in \boldsymbol{\Theta}_{p}$ given by

$$
\mu=\mu(\theta)=\mathbb{E}[Y]=\kappa_{p}^{\prime}(\theta) \quad \text { and } \quad \operatorname{Var}(Y)=\frac{\varphi}{v} \kappa_{p}^{\prime \prime}(\theta)=\frac{\varphi}{v} \mu^{p}=\frac{\varphi}{v} V(\mu)>0
$$

the latter describes the meaning of parameter $p$ and it motivates the definition of the variance function $\mu \mapsto V_{p}(\mu)=\mu^{p}$ within Tweedie's family. For this reason, Tweedie's family is said to have power variance functions with power variance parameter $p \in \mathbb{R} \backslash(0,1)$.

[^0]
[^0]:    ${ }^{2}$ The i.i.d. assumption applies to $\left(Y_{i}, \boldsymbol{x}_{i}\right)_{i}$. The responses $Y_{i}$, given covariates $\boldsymbol{x}_{i}$, are only independent, but not identically distributed because the distribution typically differs in different covariates $\boldsymbol{x}_{i}$.

## Page 7
For claim size modeling power variance parameters $p \geq 2$ are most suitable; this includes the (absolutely continuous) gamma and the inverse Gaussian models. For claim size modeling we set exposure $v=1$. This provides us with coefficient of variation (CoV)

$$
\operatorname{CoV}(Y)=\frac{\sqrt{\operatorname{Var}(Y)}}{\mathbb{E}[Y]}=\varphi \mu^{p / 2-1}
$$

Thus, for $\mu>1$ the coefficient of variation is increasing in power variance parameter $p \geq 2$. Nevertheless, all members of Tweedie's family are light-tailed as we have exponentially decaying survival function, that is, the survival function $1-F(y ; \theta, v / \varphi)$ of $Y$ decays exponentially for $y \rightarrow \infty$, see Remarks 2.11 and Section 2.2.5 in Wüthrich-Merz [31].

# 3.2 Maximum likelihood estimation: null model 

Maximum likelihood estimation (MLE) within Tweedie's family is straightforward because we have a very attractive form of densities in (3.1) that allows for a direct estimation of canonical parameter $\theta$. For i.i.d. data $\boldsymbol{Y}=\left(Y_{1}, \ldots, Y_{n}\right)^{\top}$ the log-likelihood is given by

$$
\theta \mapsto \ell_{\boldsymbol{Y}}(\theta)=\sum_{i=1}^{n} \frac{Y_{i} \theta-\kappa_{p}(\theta)}{\varphi / v}+a\left(Y_{i} ; v / \varphi\right)
$$

Calculating the derivative w.r.t. $\theta$, and setting this derivative equal to zero gives us MLE (subject to existence ${ }^{3}$ )

$$
\widehat{\theta}=h_{p}\left(\frac{1}{n} \sum_{i=1}^{n} Y_{i}\right)
$$

with canonical link $h_{p}$ for $p \geq 2$

$$
\mu>0 \mapsto h_{p}(\mu)=\left(\kappa_{p}^{\prime}\right)^{-1}(\mu)=\frac{1}{1-p} \mu^{1-p}<0
$$

Note that this MLE does not consider any covariates $\boldsymbol{x} \in \mathbb{R}^{q}$, therefore, we call this model the null model, the homogeneous model or the intercept model.

The MLE $\widehat{\theta}$ is estimated on the learning data $\mathcal{L}$, and model performance is studied out-ofsample on the (independent) test data $\mathcal{T}$.

### 3.3 Forecast evaluation and generalization loss

Forecast evaluation should be performed based on so-called strictly consistent scoring functions (also called strictly consistent loss functions). Strictly consistent scoring functions have been studied in Gneiting-Raftery [7] and Gneiting [6], we also refer to the tutorial of Fissler et al. [5] for a thorough explanation of strictly consistent scoring.
Using the canonical link (3.4), there is a one-to-one correspondence between the canonical parameter $\theta=h_{p}(\mu)$ and the mean parameter $\mu=\kappa_{p}^{\prime}(\theta) .{ }^{4}$ The MLE $\widehat{\mu}=\kappa_{p}^{\prime}(\widehat{\theta})$ of $\mu$ is also given

[^0]
[^0]:    ${ }^{3}$ Remark that the MLE $\widehat{\theta}$ needs to lie in the effective domain $\Theta_{p}$, and we might receive solution at the boundary of $\Theta_{p}$ which requires some care. For claim sizes with power variance parameters $p \geq 2$ we always receive an inner solution in (the interval) $\Theta_{p}$. Uniqueness is given by the convexity of the cumulant function $\kappa_{p}$.
    ${ }^{4}$ Note that $\kappa_{p}$ is convex which implies that $\kappa_{p}^{\prime \prime}>0$, see (3.3), and, henceforth, $\kappa_{p}^{\prime}$ and $h_{p}$ are strictly increasing.

## Page 8
by

$$
\widehat{\mu}=\frac{1}{n} \sum_{i=1}^{n} Y_{i}
$$

We call $\widehat{\mu}$ the MLE in the mean parametrization and $\widehat{\theta}$ is the MLE in the canonical parametrization. For forecast evaluation it is more convenient to work with the mean parametrization, i.e., to estimate the mean parameter $\mu$ with MLE. Savage [22] has proved that the (only) strictly consistent scoring functions for mean estimation $\mu$ are the Bregman divergences, see also Theorem 7 in Gneiting [6]. Therefore, we should restrict ourselves to Bregman divergences for forecast evaluation of (3.5).

Working within Tweedie's family, a specific Bregman divergence offers itself. Namely, the unit deviance is a distribution-adapted Bregman divergence within the chosen member of Tweedie's family, and minimizing (in-sample) unit deviances exactly provides MLEs $\widehat{\mu}$.

The unit deviance within Tweedie's family is given by, we also refer to Section 4.1.2 and Example 4.11 in Wüthrich-Merz [31], and we set $\theta=\theta(\mu)=h_{p}(\mu)$,

$$
\begin{aligned}
\mathfrak{d}_{p}(y, \mu) & =2 \frac{\varphi}{v}\left(\log f\left(y ; h_{p}(y), v / \varphi\right)-\log f(y ; \theta, v / \varphi)\right) \\
& =2\left(y h_{p}(y)-\kappa_{p}\left(h_{p}(y)\right)-y h_{p}(\mu)+\kappa_{p}\left(h_{p}(\mu)\right)\right) \geq 0
\end{aligned}
$$

We observe that maximizing the log-likelihood in $\theta=\theta(\mu)$ is equivalent to minimizing the unit deviance in $\mu$ (on the 2nd line) because we apply a sign-switch to the log-likelihood. For claim size modeling we focus on $p \geq 2$. The unit deviances are for $p>2$ given by

$$
\mathfrak{d}_{p}(y, \mu)=2\left(y \frac{y^{1-p}-\mu^{1-p}}{1-p}-\frac{y^{2-p}-\mu^{2-p}}{2-p}\right)
$$

and in the gamma case $p=2$ we have

$$
\mathfrak{d}_{2}(y, \mu)=2(y / \mu)-1+\log (\mu / y))
$$

The MLE (3.5) in Tweedie's family for $p \geq 2$ is then also obtained by solving for data $\boldsymbol{Y}$

$$
\widehat{\mu}=\underset{\mu>0}{\operatorname{argmin}} \frac{1}{n} \sum_{i=1}^{n} \mathfrak{d}_{p}\left(Y_{i}, \mu\right)
$$

In-sample and out-of-sample deviance losses of $\widehat{\mu}$, being estimated on learing data $\mathcal{L}=\boldsymbol{Y}$, are given by

$$
\begin{aligned}
L_{p}(\boldsymbol{Y}, \widehat{\mu}) & =\frac{1}{n} \sum_{i=1}^{n} \frac{v_{i}}{\varphi} \mathfrak{d}_{p}\left(Y_{i}, \widehat{\mu}\right) \\
L_{p}\left(\boldsymbol{Y}^{\dagger}, \widehat{\mu}\right) & =\frac{1}{\tau} \sum_{t=1}^{\tau} \frac{v_{t}^{\dagger}}{\varphi} \mathfrak{d}_{p}\left(Y_{t}^{\dagger}, \widehat{\mu}\right)
\end{aligned}
$$

If we have two different predictors $\widehat{\mu}_{1}$ and $\widehat{\mu}_{2}$ being estimated on the learning data $\mathcal{L}=\boldsymbol{Y}$, then the first one should be preferred if we have out-of-sample deviance losses

$$
L_{p}\left(\boldsymbol{Y}^{\dagger}, \widehat{\mu}_{1}\right)<L_{p}\left(\boldsymbol{Y}^{\dagger}, \widehat{\mu}_{2}\right)
$$

## Page 9
# 3.4 Forecast dominance 

Evaluation of (3.11) implicitly assumes that we know the true data generating distribution, i.e., in our case the true power variance parameter $p \geq 2$. However, typically, this is not the case. Following the proposal of Krüger-Ziegel [11] and Denuit et al. [2], we should prefer predictor $\widehat{\mu}_{1}$ over $\widehat{\mu}_{2}$ if

$$
L_{p}\left(\boldsymbol{Y}^{\dagger}, \widehat{\mu}_{1}\right)<L_{p}\left(\boldsymbol{Y}^{\dagger}, \widehat{\mu}_{2}\right) \quad \text { for all } p \geq 2
$$

This is a robustified version of (3.11) accounting for model uncertainty in $p \geq 2$.
$\square$ Unfortunately, often, we do not have a strict ordering (3.12) that simultaneously applies to all $p \geq 2$, therefore, one should restrict power variance parameters $p$ to the most reasonable values for modeling the data $\boldsymbol{Y}$ and $\boldsymbol{Y}^{\dagger}$ and evaluate the corresponding fitted models.

Outlook 3.1 Merz-Wüthrich [15] study network model fitting under model uncertainty by fitting the same network architecture simultaneously to different power variance parameters $p \geq 2$. This approach may lead to more robustness in model fitting, because simultaneous study of deviance losses $L_{p}(\boldsymbol{Y}, \widehat{\mu})$ for different $p$ 's needs to be equally good for these different power variance parameters. In this tutorial we do not further follow this route.

### 3.5 Lab: the null model

We fit the null model for power variance parameters $p=2$ (gamma model), $p=2.5$ and $p=3$ (inverse Gaussian model) to the accident insurance claim data presented in Section 1. In the null model the MLE $\widehat{\mu}=12^{\prime} 718$ is easily obtained from (3.5), and it does not depend on the specific choice of $p \geq 2$.

|  | in-sample loss on $\mathcal{L}$ |  |  | out-of-sample loss on $\mathcal{T}$ |  |  |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $L_{p=2}$ | $L_{p=2.5}$ | $L_{p=3}$ | $L_{p=2}$ | $L_{p=2.5}$ | $L_{p=3}$ |
| null model | 5.1304 | $1.0196 \cdot 10^{-1}$ | $3.5895 \cdot 10^{-3}$ | 5.1393 | $1.0200 \cdot 10^{-1}$ | $3.5885 \cdot 10^{-3}$ |

Table 2: In-sample and out-of-sample deviance losses (3.9)-(3.10) for power variance parameters $p=2,2.5,3$; the losses use $v_{i} / \varphi \equiv v_{t}^{\dagger} / \varphi \equiv 1$.

Table 2 shows the resulting in-sample and out-of-sample deviance losses $L_{p}(\boldsymbol{Y}, \widehat{\mu})$ and $L_{p}\left(\boldsymbol{Y}^{\dagger}, \widehat{\mu}\right)$ for power variance parameters $p=2,2.5,3$, see (3.9)-(3.10). We use these results as benchmarks for the subsequent models. We remark that the losses in Table 2 live on different scales for different power variance parameters $p$ because the unit deviances $\mathfrak{d}_{p}$ take different functional forms for different $p$ 's.

## 4 Plain-vanilla deep neural network

### 4.1 Definition of neural networks

Fully-connected feed-forward neural (FFN) networks have been studied in our previous tutorials Noll et al. [18], Ferrario et al. [4] and Schelldorfer-Wüthrich [23], therefore, we only give a very brief summary, here.

## Page 10
Denote the depth of the chosen FFN network architecture by $d \in \mathbb{N}$, and choose for $1 \leq m \leq d$ non-linear activation functions $\phi_{m}: \mathbb{R} \rightarrow \mathbb{R}$ and integers (dimensions) $q_{m-1}, q_{m} \in \mathbb{N}$. Initialize $q_{0}=q$ by the dimension of the covariates $\boldsymbol{x} \in \mathbb{R}^{q}$. The $m$-th $F F N$ layer is defined by the mapping

$$
\begin{aligned}
\boldsymbol{z}^{(m)}: \mathbb{R}^{q_{m-1}} & \rightarrow \mathbb{R}^{q_{m}} \\
\boldsymbol{x} & \mapsto \boldsymbol{z}^{(m)}(\boldsymbol{x})=\left(z_{1}^{(m)}(\boldsymbol{x}), \ldots, z_{q_{m}}^{(m)}(\boldsymbol{x})\right)^{\top}
\end{aligned}
$$

having neurons $z_{j}^{(m)}(\boldsymbol{x}), 1 \leq j \leq q_{m}$, for $\boldsymbol{x}=\left(x_{1}, \ldots, x_{q_{m-1}}\right)^{\top} \in \mathbb{R}^{q_{m-1}}$,

$$
z_{j}^{(m)}(\boldsymbol{x})=\phi_{m}\left(w_{0, j}^{(m)}+\left\langle\boldsymbol{w}_{j}^{(m)}, \boldsymbol{x}\right\rangle\right)=\phi_{m}\left(w_{0, j}^{(m)}+\sum_{l=1}^{q_{m-1}} w_{l, j}^{(m)} x_{l}\right)
$$

for given network weights $\boldsymbol{w}_{j}^{(m)}=\left(w_{l, j}^{(m)}\right)_{1 \leq l \leq q_{m-1}}^{\top} \in \mathbb{R}^{q_{m-1}}$ and bias (intercept) $w_{0, j}^{(m)} \in \mathbb{R}$. A FFN network of depth $d \in \mathbb{N}$ is obtained by composing $d$ FFN layers (4.1) to provide learned representation

$$
\begin{aligned}
\boldsymbol{z}^{(d: 1)}: \mathbb{R}^{q} & \rightarrow \mathbb{R}^{q_{d}} \\
\boldsymbol{x} & \mapsto \boldsymbol{z}^{(d: 1)}(\boldsymbol{x})=\left(\boldsymbol{z}^{(d)} \circ \cdots \circ \boldsymbol{z}^{(1)}\right)(\boldsymbol{x})
\end{aligned}
$$

This $q_{d}$-dimensional learned representation $\boldsymbol{z}^{(d: 1)}(\boldsymbol{x}) \in \mathbb{R}^{q_{d}}$ is then outputted using a strictly monotone link function $g: \mathbb{R} \rightarrow \mathbb{R}$

$$
\boldsymbol{x} \mapsto \mu(\boldsymbol{x})=g^{-1}\left(\beta_{0}+\left\langle\beta, \boldsymbol{z}^{(d: 1)}(\boldsymbol{x})\right\rangle\right)
$$

with output parameter $\boldsymbol{\beta}=\left(\beta_{1}, \ldots, \beta_{q_{d}}\right)^{\top} \in \mathbb{R}^{q_{d}}$, bias $\beta_{0} \in \mathbb{R}$, and where $\langle\cdot, \cdot\rangle$ denotes the scalar product in the Euclidean space $\mathbb{R}^{q_{d}}$. This deep FN network has network parameter

$$
\boldsymbol{\vartheta}=\left(w_{0,1}^{(1)}, \boldsymbol{w}_{1}^{(1)}, \ldots, w_{0, q_{d}}^{(d)}, \boldsymbol{w}_{q_{d}}^{(d)}, \beta_{0}, \boldsymbol{\beta}\right) \in \mathbb{R}^{r}
$$

of dimension $r=\sum_{m=1}^{d} q_{m}\left(q_{m-1}+1\right)+\left(q_{d}+1\right)$.

# Remarks 4.1 

- The link function $g$ and the canonical link $h$ may differ.
- For interpretation we refer to the tutorials [18, 4, 23] and Chapter 7 in [31], in particular, we refer to the similarities between GLMs and FFN networks.
- State-of-the-art fitting of FFN networks uses variants of the stochastic gradient descent (SGD) algorithm exploring early stopping to not (in-sample) over-fit to the learning data $\mathcal{L}$. We use the nadam version of SGD. For tracking over-fitting we split the learning data $\mathcal{L}$ into training data $\mathcal{U}$ and validation data $\mathcal{V}$, and we retrieve the network weights $\widetilde{\boldsymbol{\vartheta}}$ that provide the lowest validation loss $\mathcal{V}$ using a callback. For more details we refer to Section 7.2.3 in [31], in particular, to Figures 7.7-7.8.

## Page 11
# 4.2 Lab: FFN networks 

We fit a FFN network architecture to the different deviance losses $L_{p}$ with power variance parameters $p=2$ (gamma model), $p=2.5$ and $p=3$ (inverse Gaussian (IG) model) to the accident insurance claim data presented in Section 1. As depth of the FNN network we choose $d=3$ having $\left(q_{1}, q_{2}, q_{3}\right)=(20,15,10)$ neurons in the FFN layers. We choose hyperbolic tangent activation function for $\phi_{m}, 1 \leq m \leq d$, and log-link for $g$. The latter is not the canonical link for power variance parameters $p \geq 2$, but it ensures that range and domain of the link function $g$ match the effective domain $\boldsymbol{\Theta}_{p}$ and the means $\mu(\theta)$ for power variance parameters $p \geq 2$.
We choose a training to validation split of $4: 1$, and we choose a mini-batch size of 5'000, Listing 4 in the appendix gives the exact fitting specification in case of the gamma deviance loss, and the deviance losses are encoded in Listing 3 in the appendix (as these are not directly available in the R library keras). Fitting these networks takes roughly 30 epochs, thus, fitting is very fast here. The results are presented in Table 3.

|  | in-sample loss on $\mathcal{L}$ |  |  | out-of-sample loss on $\mathcal{T}$ |  |  |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $L_{p=2}$ | $L_{p=2.5}$ | $L_{p=3}$ | $L_{p=2}$ | $L_{p=2.5}$ | $L_{p=3}$ |
| null model | 5.1304 | 1.0196 | 3.5895 | 5.1393 | 1.0200 | 3.5885 |
| gamma FFN net | 4.4714 | 0.9510 | 3.5127 | 4.5542 | 0.9605 | 3.5237 |
| $p=2.5$ FFN net | 4.4717 | 0.9498 | 3.5095 | 4.5670 | 0.9617 | 3.5251 |
| IG FFN net | 4.5286 | 0.9555 | 3.5166 | 4.6039 | 0.9642 | 3.5268 |

Table 3: In-sample and out-of-sample deviance losses (3.9)-(3.10) for power variance parameters $p=2,2.5,3$; the losses use $v_{i} / \varphi \equiv v_{t}^{\dagger} / \varphi \equiv 1$; for better readability we display losses in indifferent units for different $p$ 's: $10^{0}=1$ for $p=2,10^{-1}$ for $p=2.5$ and $10^{-3}$ for $p=3$.

In view of forecast dominance (3.12) we give preference to the gamma model $p=2$, see blue in color Table 3. However, these solutions would need further analysis to perform a thorough model selection, e.g., one can study Tukey-Anscombe plots, dispersion parameters, etc. We refrain from doing so because this is not the main purpose of this tutorial.
We remark that the inverse Gaussian model (IG FFN net) does not have the lowest in-sample loss on $L_{p=3}$, i.e., we have $3.5166>3.5095$. This seems counter-intuitive, but it is caused by the fact that we exercise early stopping. In fact, the inverse Gaussian model is more sensitive in fitting and, typically, this results in an earlier stopping time. Here, it uses less than 30 epochs, whereas the other two cases use more than 30 epochs. In general, the inverse Gaussian model is more difficult to fit and, therefore, the robustified approach of Merz-Wüthrich [15] should be preferred.

Outlook 4.2 In the considerations above we have chosen unit dispersion $\varphi \equiv 1$, and a constant dispersion choice implies that it cancels in optimization. Therefore, the specific choice is irrelevant for optimization. Analyzing the models and data in more depth often suggests that $\varphi=\varphi(\boldsymbol{x})$ should also be modeled covariate dependent, too. This can be done in a double FFN network model where estimations of mean parameter $\mu(\boldsymbol{x})$ and dispersion parameter $\varphi(\boldsymbol{x})$ are alternated as in the double GLM of Smyth-Verbyla [25]. Typically, this uses a saddlepoint approximation, we refer to Section 3.5 in Jørgensen and Section 5.5.2 in Wüthrich-Merz [31], and then the modeling of the dispersion parameter boils down to a gamma model with unit

## Page 12
deviances $\mathfrak{d}_{p}(Y, \widehat{\mu})$ as responses for given mean estimates $\widehat{\mu}$. This approach is sometimes also called residual MLE, see Section 5.5.3 in Wüthrich-Merz [31].

# 5 LocalGLMnet 

The FFN network architectures of Table 3 often provide good predictive power, however, they are neither easily interpretable nor do they allow for variable selection. I.e., we cannot answer the question whether we should keep, say, variable HoursWorkedPerWeek in the model or not. For this reason we present the LocalGLMnet of Richman-Wüthrich [21] which allows us to make such decisions.

### 5.1 Definition of generalized linear models

A classical GLM can be obtained as a special case of a FFN network, namely, if we set depth $d=0$, we receive GLM regression function

$$
\boldsymbol{x} \mapsto \mu(\boldsymbol{x})=g^{-1}\left(\beta_{0}+\langle\boldsymbol{\beta}, \boldsymbol{x}\rangle\right)
$$

with regression parameter $\boldsymbol{\beta}=\left(\beta_{1}, \ldots, \beta_{q}\right)^{\top} \in \mathbb{R}^{q}$ and bias $\beta_{0} \in \mathbb{R}$. The key idea of LocalGLMnets is to replace the (constant) regression parameters $\boldsymbol{\beta}=\left(\beta_{1}, \ldots, \beta_{q}\right)^{\top}$ by covariate dependent regression attentions $\boldsymbol{\beta}(\boldsymbol{x})=\left(\beta_{1}(\boldsymbol{x}), \ldots, \beta_{q}(\boldsymbol{x})\right)^{\top}$, which are modeled by FFN networks.

### 5.2 Definition of the LocalGLMnet architecture

We now make regression parameter $\boldsymbol{\beta}$ in (5.1) covariate $\boldsymbol{x}$-dependent.
Assumptions 5.1 (LocalGLMnet) Choose a FFN network architecture of depth $d \in \mathbb{N}$ with input and output dimensions being equal to $q_{0}=q_{d}=q$ to model the regression attentions

$$
\begin{aligned}
\boldsymbol{\beta}: \mathbb{R}^{q} & \rightarrow \mathbb{R}^{q} \\
\boldsymbol{x} & \mapsto \boldsymbol{\beta}(\boldsymbol{x})=\boldsymbol{z}^{(d: 1)}(\boldsymbol{x})=\left(\boldsymbol{z}^{(d)} \circ \cdots \circ \boldsymbol{z}^{(1)}\right)(\boldsymbol{x})
\end{aligned}
$$

The LocalGLMnet is defined by the additive decomposition

$$
\boldsymbol{x} \mapsto \mu(\boldsymbol{x})=g^{-1}\left(\beta_{0}+\langle\boldsymbol{\beta}(\boldsymbol{x}), \boldsymbol{x}\rangle\right)
$$

## Remarks 5.2

- This regression function is called LocalGLMnet, because locally around a given $\boldsymbol{x}$, regression function (5.3) can be understood as a GLM (supposed that $\boldsymbol{\beta}(\boldsymbol{x})$ is more or less constant in this environment).
- $\boldsymbol{\beta}(\boldsymbol{x})$ are called regression attentions because they provide more or less attention to specific values of the components of $\boldsymbol{x}$ in (5.3). This analogy is drawn from the attention layers introduced by Bahdanau et al. [1] and Vaswani et al. [29]. Additive decomposition (5.3) is also similar to the structure of Shapely values [24] (after applying the link function $g$ ) which allows, yet, for another interpretation, we refer to Lundberg-Lee [13], Sundararajan-Najmi [26], Sundararajan-Najmi [26] and Lorentzen-Mayer [12] for SHapley Additive exPlanation (SHAP).

## Page 13
Remarks 5.3 (interpretation of the LocalGLMnet regression function (5.3)) The additive decomposition (5.3) allows for an intuitive interpretation. Select one component $1 \leq j \leq q$ and study the terms

$$
\beta_{j}(\boldsymbol{x}) x_{j}
$$

(1) If $\beta_{j}(\boldsymbol{x}) \equiv \beta_{j}(\neq 0)$ is not covariate dependent (and different from zero), we receive a GLM term in $x_{j}$.
(2) Condition $\beta_{j}(\boldsymbol{x}) \equiv 0$ says that the term $x_{j}$ should not be included.
(3) Property $\beta_{j}(\boldsymbol{x})=\beta_{j}\left(x_{j}\right)$ says that we have a term $\beta_{j}\left(x_{j}\right) x_{j}$ that does not interact with other terms. Sensitivities of $\beta_{j}(\boldsymbol{x})$ in the components of $\boldsymbol{x}$ can be obtained by the gradient

$$
\nabla \beta_{j}(\boldsymbol{x})=\left(\partial_{x_{1}} \beta_{j}(\boldsymbol{x}), \ldots, \partial_{x_{q}} \beta_{j}(\boldsymbol{x})\right)^{\top} \in \mathbb{R}^{q}
$$

The $j$-th component $\partial_{x_{j}} \beta_{j}(\boldsymbol{x})$ of this gradient $\nabla \beta_{j}(\boldsymbol{x})$ explores whether we have a linear term in $x_{j}$, and the components different from $j$ quantify the interactions.
(4) We do not have identifiability as we may still receive

$$
\beta_{j}(\boldsymbol{x}) x_{j}=x_{j^{\prime}}
$$

by learning a regression attention $\beta_{j}(\boldsymbol{x})=x_{j^{\prime}} / x_{j}$. In our examples, we did not experience these difficulties.

We emphasize in item (2) that $\beta_{j}(\boldsymbol{x}) \equiv 0$ indicates that the 'term' $x_{j}$ in the additive decomposition (5.3) should be dropped. The 'covariate' $x_{j}$ may still need to be kept, as it may play an important role in attention weights $\beta_{j^{\prime}}(\boldsymbol{x})$ for some $j^{\prime} \neq j$.

# 5.3 Lab: the LocalGLMnet 

### 5.3.1 Results of the LocalGLMnet

We proceed completely analogously to Section 4.2 and fit a LocalGLMnet to the accident insurance data of Section 1. As depth of the LocalGLMnet we choose $d=4$ having $\left(q_{1}, q_{2}, q_{3}, q_{4}\right)=$ $(20,15,10,16)$ neurons in the FFN layers. Note that $q_{4}=q_{0}=q=16$ corresponds to the input dimension. We choose hyperbolic tangent activation function for $\phi_{m}, 1 \leq m \leq d-1$, the linear function $\phi_{d}(x)=x$, and log-link for $g$. The rest is done completely analogously to Section 4.2, namely, we fit this LocalGLMnet architecture using deviance loss functions $L_{p}$ with $p=2,2.5,3$. The explicit LocalGLMnet architecture is shown in Listing 5 in the appendix, and the results are presented in Table 4.

From a forecast dominance viewpoint we again prefer the gamma model over the other power variance parameter models. Moreover, for this particular data set the LocalGLMnet outperforms the deep FFN network. However, this is not the crucial point of introducing the LocalGLMnet, but the LocalGLMnet leads to interpretable predictions and it allows for variable selection as we are going to demonstrate in the next sections.

## Page 14
|  | in-sample loss on $\mathcal{L}$ |  |  | out-of-sample loss on $\mathcal{T}$ |  |  |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $L_{p=2}$ | $L_{p=2.5}$ | $L_{p=3}$ | $L_{p=2}$ | $L_{p=2.5}$ | $L_{p=3}$ |
| null model | 5.1304 | 1.0196 | 3.5895 | 5.1393 | 1.0200 | 3.5885 |
| gamma FFN net | 4.4714 | 0.9510 | 3.5127 | 4.5542 | 0.9605 | 3.5237 |
| $p=2.5$ FFN net | 4.4717 | 0.9498 | 3.5095 | 4.5670 | 0.9617 | 3.5251 |
| IG FFN net | 4.5286 | 0.9555 | 3.5166 | 4.6039 | 0.9642 | 3.5268 |
| gamma LocalGLMnet | 4.4434 | 0.9460 | 3.5022 | 4.5388 | 0.9588 | 3.5207 |
| $p=2.5$ LocalGLMnet | 4.4654 | 0.9480 | 3.5045 | 4.5506 | 0.9599 | 3.5220 |
| IG LocalGLMnet | 4.5287 | 0.9551 | 3.5144 | 4.5860 | 0.9637 | 3.5272 |

Table 4: In-sample and out-of-sample deviance losses (3.9)-(3.10) for power variance parameters $p=2,2.5,3$; the losses use $v_{i} / \varphi \equiv v_{t}^{\dagger} / \varphi \equiv 1$; for better readability we display losses in indifferent units for different $p$ 's: $10^{0}=1$ for $p=2,10^{-1}$ for $p=2.5$ and $10^{-3}$ for $p=3$.

# 5.3.2 Variable selection and variable importance 

The purpose of this section is to understand whether we need to include all additive terms into the regression function (5.3). We would like to explore this question by classical statistical testing. That is, we consider the null hypothesis $H_{0}: \beta_{j}(\boldsymbol{x})=0$ for a given $1 \leq j \leq q$. If the estimates $\widehat{\beta}_{j}(\boldsymbol{x})$ differ too much from zero we reject this null hypothesis $H_{0}$. In classical statistics, one performs a Wald test or a likelihood ratio test (LRT) to answer such questions. Both tests are based on an asymptotic theory for MLE. Unfortunately, there is no similar asymptotic theory available for FNN networks. Therefore, we need to explore an empirical test.
In view of Remarks 5.3 (2) we need to understand whether for some components $j$ we have $\beta_{j}(\boldsymbol{x}) \approx 0$ to analyze the null hypothesis $H_{0}$ for that $j$. In order to make this decision we extend the original covariates $\boldsymbol{x}_{i}$ by additional information that does not belong to our data. We therefore expand the original covariates $\boldsymbol{x}$ to $\boldsymbol{x}^{+}=\left(\boldsymbol{x}^{\top}, x_{q+1}, x_{q+2}\right)^{\top} \in \mathbb{R}^{q+2}$ and consider the extended LocalGLMnet regression function

$$
\boldsymbol{x}^{+} \mapsto \mu\left(\boldsymbol{x}^{+}\right)=g^{-1}\left(\beta_{0}+\left\langle\boldsymbol{\beta}\left(\boldsymbol{x}^{+}\right), \boldsymbol{x}^{+}\right\rangle\right)
$$

These two additional components $x_{q+1}, x_{q+2}$ will be taken purely at random and, thus, they cannot contain any systematic effects explaining response $Y$. For this reason we would like to see that the network finds estimated regression attentions $\widehat{\beta}_{q+1}\left(\boldsymbol{x}^{+}\right) \approx 0$ and $\widehat{\beta}_{q+2}\left(\boldsymbol{x}^{+}\right) \approx 0$ for these two additional terms. Network estimation will not provide them being exactly equal to zero as there is some noise in the data that also lets these regression attentions fluctuate around zero. The magnitude of these fluctuations will identify regression attention estimates $\widehat{\beta}_{j}\left(\boldsymbol{x}^{+}\right)$, $1 \leq j \leq q$, that are not sufficiently different from zero to justify inclusion in (5.6) and (5.3), respectively.
These two additional components $x_{q+1}$ and $x_{q+2}$ should be centered and have unit variance to live on the same scale as the other components in $\boldsymbol{x}$. For claims $1 \leq i \leq n$ we choose i.i.d. random variables $x_{i, q+1} \sim \operatorname{Uniform}[-\sqrt{3}, \sqrt{3}]$, and independent i.i.d. random variables $x_{i, q+2} \sim \mathcal{N}(0,1)$. These variables are standardized, and we choose two different components to see whether the distributional choice influences our decision. We fit this model to the data using the gamma deviance loss $L_{2}$, the results are given in Table 5.

The inclusion of the two additional (unrelated) components $x_{i, q+1}$ and $x_{i, q+2}$ slightly worsens

## Page 15
|  | in-sample loss on $\mathcal{L}$ |  |  | out-of-sample loss on $\mathcal{T}$ |  |  |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $L_{p=2}$ | $L_{p=2.5}$ | $L_{p=3}$ | $L_{p=2}$ | $L_{p=2.5}$ | $L_{p=3}$ |
| null model | 5.1304 | 1.0196 | 3.5895 | 5.1393 | 1.0200 | 3.5885 |
| gamma FFN net based on $\boldsymbol{x}$ | 4.4714 | 0.9510 | 3.5127 | 4.5542 | 0.9605 | 3.5237 |
| gamma LocalGLMnet based on $\boldsymbol{x}$ | 4.4434 | 0.9460 | 3.5022 | 4.5388 | 0.9588 | 3.5207 |
| gamma LocalGLMnet based on $\boldsymbol{x}^{+}$ | 4.4357 | 0.9455 | 3.5023 | 4.5458 | 0.9607 | 3.5254 |

Table 5: In-sample and out-of-sample deviance losses (3.9)-(3.10) for power variance parameters $p=2,2.5,3$; the losses use $v_{i} / \varphi \equiv v_{t}^{\dagger} / \varphi \equiv 1$; for better readability we display losses in indifferent units for different $p$ 's: $10^{0}=1$ for $p=2,10^{-1}$ for $p=2.5$ and $10^{-3}$ for $p=3$.
the predictive performance. The reason is that these additional components give a higher overfitting potential, and, typically, we stop the SGD algorithm more early.

We extract the estimated regression attentions $\widehat{\beta}_{q+1}\left(\boldsymbol{x}_{i}\right)$ and $\widehat{\beta}_{q+2}\left(\boldsymbol{x}_{i}\right)$, the corresponding code is given in Listing 6 , and we calculate their empirical means $\hat{\beta}_{q+1}$ and $\bar{\beta}_{q+2}$ and their empirical standard deviations $\bar{s}_{q+1}$ and $\bar{s}_{q+2}$ over all claims $1 \leq i \leq n$ (of the learning data $\mathcal{L}$ ). These are given by

$$
\bar{\beta}_{q+1}=-0.0007, \quad \bar{\beta}_{q+2}=0.0452 \quad \text { and } \quad \bar{s}_{q+1}=0.0522, \quad \bar{s}_{q+2}=0.0387
$$

Thus, the regression attentions $\widehat{\beta}_{q+1}\left(\boldsymbol{x}_{i}\right)$ are quite centered and the regression attentions $\widehat{\beta}_{q+2}\left(\boldsymbol{x}_{i}\right)$ are a bit biased, this is verified by Figure 4 (bottom-middle and bottom-right). The fluctuations of these regression attentions $\widehat{\beta}_{q+1}\left(\boldsymbol{x}_{i}\right)$ and $\widehat{\beta}_{q+2}\left(\boldsymbol{x}_{i}\right)$ are of magnitudes between $\bar{s}_{q+1}=0.0522$ and $\bar{s}_{q+1}=0.0387$. If we multiply these magnitudes with the $99.5 \%$ normal quantile (3.29) to receive a two-sided $1 \%$ rejection region around zero, we receive a critical value of roughly $\pm 0.15$. This allows us to determine the rejection region for the above null hypothesis $H_{0}$

$$
\mathcal{R}_{99.9 \%}=\mathcal{I}_{99.9 \%}^{c}=[-0.15,0.15]^{c}
$$

Figures 3 and 4 show the estimated regression attentions $\widehat{\beta}_{j}\left(\boldsymbol{x}_{i}\right)$ for all continuous and binary components $j$ for 5 '000 randomly selected claims $\boldsymbol{x}_{i}$ (we do not display all claims to not overload the plots). The shaded cyan area shows the interval $\mathcal{I}_{99.9 \%}$, and the text in red color (bottomright of plots) shows the coverage ratio (CR) of this interval $\mathcal{I}_{99.9 \%}$ over all claims $1 \leq i \leq n$. These coverage ratios are around $99.9 \%$ for the covariates HoursWorkedPerWeek, DaysWorkedPerWeek and AccWeekday (besides the two purely random components $x_{i, q+1}$ and $x_{i, q+2}$ ). This suggests that these three terms may not be necessary in our regression model, and the remaining terms seem significant, i.e., the null hypothesis $H_{0}$ of setting these regression attentions to zero is rejected. We mention that HoursWorkedPerWeek and DaysWorkedPerWeek are almost fully concentrated in one single value, see Figure 17 in the appendix. These terms seem to not allow to sufficiently differentiate the claims.

We have presented an empirical test for the null hypothesis $H_{0}: \beta_{j}(\boldsymbol{x})=0$ for a given $1 \leq j \leq q$. This null hypothesis can be tested using the coverage ratio of the (empirical) interval $\mathcal{I}_{99.9 \%}$. This test requires some care, as it based on the fitted LocalGLMnet, and if the purely random additional components $x_{i, q+1}$ and $x_{i, q+2}$ show to much structure in the fitted model, then, for sure, the model over-fits to these components, e.g., in estimates $\widehat{\beta}_{q+2}\left(\boldsymbol{x}_{i}\right)$ we observe a

## Page 16
Figure 3: Regression attentions $\widehat{\beta}_{j}\left(\boldsymbol{x}_{i}^{+}\right)$of $5^{\prime} 000$ randomly selected covariates $\boldsymbol{x}_{i}^{+}$, the cyan area shows the interval $\mathcal{I}_{99.9 \%}$ and the red number gives the coverage ratio (CR) of this interval; the $y$-scale is identical in all plots (the orange lines are at $\pm 0.25$ for orientation purposes), and on the $x$-scale we have covariate components $x_{j}$.
bias, see Figure 4 (bottom-right). If this bias is too large, a different seed should be chosen for SGD fitting. We also mention that this test is only useful for continuous and binary variables because the one-hot encoded categorical variables do not live on the same scale (centered and unit variance).

An evident empirical measure for variable importance (VI) of continuous and binary covariates is defined by

$$
\mathrm{VI}_{j}=\frac{1}{n} \sum_{i=1}^{n}\left|\widehat{\beta}_{j}\left(\boldsymbol{x}_{i}\right)\right|
$$
![Page 16 Image 1](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p16_img1.jpg)

## Page 17
Figure 4: Regression attentions $\widehat{\beta}_{j}\left(\boldsymbol{x}_{i}^{+}\right)$of $5^{\prime} 000$ randomly selected covariates $\boldsymbol{x}_{i}^{+}$, the cyan area shows the interval $\mathcal{I}_{99.9 \%}$ and the red number gives the coverage ratio (CR) of this interval; the $y$-scale is identical in all plots (the orange lines are at $\pm 0.25$ for orientation purposes), and on the $x$-scale we have covariate components $x_{j}$.

Figure 5: Variable importance $\mathrm{VI}_{j}$ of the continuous and binary covariates, the blue vertical line gives the average importance $\left(\mathrm{VI}_{q+1}+\mathrm{VI}_{q+2}\right) / 2$ of the two additional components $x_{q+1}$ and $x_{q+2}$.
![Page 17 Image 1](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p17_img1.jpg)
![Page 17 Image 2](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p17_img2.jpg)

## Page 18
for $1 \leq j \leq q$ and where we aggregate over all claims $1 \leq i \leq n$. In Figure 5 we show this variable important measure, the most important variables being WeeklyPay, AccYear and Age. At the other end we have the least important variables DaysWorkedPerWeek, AccTime, HoursWorkedPerWeek and AccWeekday. Thus, compared to the coverage ratio we additionally question the significance of AccTime from the variable importance plot.

|  | in-sample loss on $\mathcal{L}$ |  |  | out-of-sample loss on $\mathcal{T}$ |  |  |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $L_{p=2}$ | $L_{p=2.5}$ | $L_{p=3}$ | $L_{p=2}$ | $L_{p=2.5}$ | $L_{p=3}$ |
| null model | 5.1304 | 1.0196 | 3.5895 | 5.1393 | 1.0200 | 3.5885 |
| gamma FFN net based on $\boldsymbol{x}$ | 4.4714 | 0.9510 | 3.5127 | 4.5542 | 0.9605 | 3.5237 |
| gamma LocalGLMnet based on $\boldsymbol{x}$ | 4.4434 | 0.9460 | 3.5022 | 4.5388 | 0.9588 | 3.5207 |
| - drop AccWeekday | 4.4645 | 0.9486 | 3.5057 | 4.5320 | 0.9587 | 3.5225 |
| - drop HoursWorkedPerWeek | 4.4669 | 0.9500 | 3.5099 | 4.5214 | 0.9567 | 3.5188 |
| - drop DaysWorkedPerWeek | 4.4382 | 0.9460 | 3.5032 | 4.5269 | 0.9577 | 3.5204 |
| - drop AccTime | 4.4715 | 0.9497 | 3.5080 | 4.5367 | 0.9590 | 3.5228 |
| gamma LocalGLMnet based on $\boldsymbol{x}^{-}$ | 4.4709 | 0.9497 | 3.5081 | 4.5250 | 0.9580 | 3.5212 |

Table 6: In-sample and out-of-sample deviance losses (3.9)-(3.10) for power variance parameters $p=2,2.5,3$; the losses use $v_{i} / \varphi \equiv v_{t}^{\dagger} / \varphi \equiv 1$; for better readability we display losses in indifferent units for different $p$ 's: $10^{0}=1$ for $p=2,10^{-1}$ for $p=2.5$ and $10^{-3}$ for $p=3$.

Table 6 shows a backward elimination analysis where we individually drop the variables AccWeekday, HoursWorkedPerWeek, DaysWorkedPerWeek and AccTime. Based on this analysis we decide to drop AccWeekday, HoursWorkedPerWeek and DaysWorkedPerWeek, and to keep AccTime; we call this reduced covariate $\boldsymbol{x}^{-} \in \mathbb{R}^{13}$. This decision considers the following:
(1) SGD fitting involves many elements of randomness in fitting, therefore, the numbers in Table 6 should not be read in absolute terms, but allow for interpretation.
(2) Some of these variables may interact in the regression attentions $\widehat{\boldsymbol{\beta}}(\boldsymbol{x})$ with others, therefore, dropping a term $\widehat{\beta}_{j}(\boldsymbol{x}) x_{j}$ does not necessarily mean that $x_{j}$ should completely be dropped.
(3) In view of Table 6 and the coverage ratio analysis we drop the three variables AccWeekday, HoursWorkedPerWeek and DaysWorkedPerWeek, the latter two being correlated with WeeklyPay (being the most important variable). We keep AccTime, the variable importance plot in Figure 5 may be a bit misleading for AccTime because this covariate is imbalanced between day and night times, see Figure 14.
(4) The resulting model should be as parsimonious as possible.

# 5.3.3 Covariate contributions 

Next we plot covariate contributions $\widehat{\beta}_{j}(\boldsymbol{x}) x_{j}$, which is the attribution of the predictor to the different additive components in (5.3).
Figure 6 shows the covariate contributions $\widehat{\beta}_{j}\left(\boldsymbol{x}_{i}\right) x_{i, j}$ of the continuous variables Age, WeeklyPay, AccYear, AccMonth, AccTime, RepDelay; the $y$-scale is identical in all plots. We see that claim amounts are increasing in most of these variables, and AccTime shows that claims are more

## Page 19
Figure 6: Feature contributions $\widehat{\beta}_{j}\left(\boldsymbol{x}_{i}\right) x_{i, j}$ of the continuous variables $j$ for $5^{\prime} 000$ randomly selected covariates $\boldsymbol{x}_{i}$, the magenta line shows a spline fit; the $y$-scale is identical in all plots and on the $x$-scale we have $x_{j}$.
expensive during nights. The magenta curve shows a spline fit, and the more volatility is observed around this spline the more strong the interactions are in $\widehat{\beta}_{j}\left(\boldsymbol{x}_{i}\right)$, see Remarks 5.3 (3).

Figure 7: Feature contributions $\widehat{\beta}_{j}\left(\boldsymbol{x}_{i}\right) x_{i, j}$ of the binary variables $j$ for $5^{\prime} 000$ randomly selected covariates $\boldsymbol{x}_{i}$; the $y$-scale is identical to Figure 6.

Figure 7 shows the covariate contributions $\widehat{\beta}_{j}\left(\boldsymbol{x}_{i}\right) x_{i, j}$ of the binary variables Gender, DependentChildren, DependentsOther, PartTimeFullTime; the $y$-scale is the same as in Figure 6. The difference in the binary variables are clearly smaller than for the continuous ones, which is also reflected by the variable importance plot in Figure 5. DependentChildren and DependentsOther only has a small volume in level 1, and these levels seem mainly driven by interactions (because
![Page 19 Image 1](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p19_img1.jpg)
![Page 19 Image 2](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p19_img2.jpg)

## Page 20
of the large boxes in the boxplot).

Figure 8: Feature contribution $\widehat{\beta}_{j}\left(\boldsymbol{x}_{i}\right)$ of the categorical variable MaritalStatus for $5^{\prime} 000$ randomly selected covariates $\boldsymbol{x}_{i}$; the $y$-scale is identical to Figure 6.

Finally, Figure 8 gives the covariate contributions $\widehat{\beta}_{j}\left(\boldsymbol{x}_{i}\right)$ of the categorical variable MaritalStatus. Note that we do not multiply with $x_{i, j}$ in this case, because these covariate components just correspond to the 0-1's from one-hot encoding. This plot now also illustrates why we do not consider dummy coding, namely, if we would use dummy coding, e.g., choosing level single (S) as reference level, then the corresponding $x_{j}=0$, and we could not model interactions for this level because it would imply that $\widehat{\beta}_{j}\left(\boldsymbol{x}_{i}\right) x_{j}=0$, and all single persons would share the same value (being the bias estimate $\widehat{\beta}_{0}$ ).

# 5.3.4 Interactions 

Next we analyze the interaction terms by studying the sensitivities $\partial_{x_{k}} \widehat{\beta}_{j}(\boldsymbol{x})$ given in (5.5), see Listing 7 for the code. A zero term $\partial_{x_{j}} \widehat{\beta}_{j}(\boldsymbol{x}) \approx 0$ for $k=j$ supports linearity, and $\partial_{x_{k}} \widehat{\beta}_{j}(\boldsymbol{x}) \neq 0$ for $k \neq j$ means that $x_{k}$ and $x_{j}$ interact. Figure 9 shows a spline fit to these partial derivatives to all claims $1 \leq i \leq n$ for the continuous covariate components. We do not observe any zero terms $\partial_{x_{j}} \widehat{\beta}_{j}(\boldsymbol{x}) \approx 0$, saying, that non of these components can be modeled by a linear term. Moreover, we observe that most continuous variables interact, e.g., Age, WeeklyPay and AccYear interact, but also RepDelay, AccTime and AccYear interact, as well as Age with AccTime. Only, AccMonth does not seem to have major interactions with other variables.
Figure 10 shows the interactions of the continuous variables with the binary variables. Also here we observe major interactions, e.g., between Age, PartTimeFullTime and Gender, or WeeklyPay and PartTimeFullTime, AccMonth and Gender or AccTime and DependentChildren. This finishes the LocalGLMnet example.

## 6 Claim descriptions

### 6.1 Pre-processing and descriptive analysis

All previous analysis has not been considering the claim descriptions that are available for each claim, see line 15 of Listing 1. Analyzing these claim descriptions requires a NLP pipeline as
![Page 20 Image 1](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p20_img1.jpg)

## Page 21
Figure 9: Spline fits to the sensitivities $\partial_{x_{k}} \widehat{\beta}_{j}\left(\boldsymbol{x}_{i}\right)$ of the continuous variables.
nicely described in Ferrario-Nägelin [3]. We briefly go through the different steps to make this data useful for claim prediction.

Listing 2: Extract of claim descriptions.

```
[1] "TWISTED OVER LIGAMENT SPECTACLES"
[2] "CARRYING PUMP RASH SOFT TISSUE INJURY HERNIA"
[3] "PULLING HEAVY STEEL AND RIGHT SHOULDER STRAIN"
[4] "WENT OF LACERATED LEFT CORNEA"
[5] "LIFTING A MESH SLIP CUT"
[6] "MOVING WASHING WOOL BLOCK LOWER BACK"
[7] "BENDING KNEE STRESS"
[8] "LIFTING BOX PULLED LOWER BACK"
[9] "CRUSHED BETWEEN DRILL CRUSHED MOUTH RING FINGER"
[10] "PUSHING RESIDENT ONTO SEVERE STRAINED LEFT SIDE ARM STRAIN"
```

Listing 2 gives examples of such claim descriptions (we mention that also these claim descriptions have been generated synthetically). We first apply data cleaning to these claim descriptions, this involves: (1) we transform the entire texts to lower case, and (2) we remove stopwords. The remaining words then need to be embedded into a Euclidean space. The most popular word embedding tools are word2vec of Mikolov et al. [16, 17] and Global Vectors (GloVe) of the Stanford NLP group, ${ }^{5}$ see Pennington et al. [19]. GloVe provides pre-trained embeddings of different embedding dimensions $50,10,200$ and 300 . Since in this tutorial we will rely on the

[^0]
[^0]:    ${ }^{5}$ https://nlp.stanford.edu/projects/glove/
![Page 21 Image 1](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p21_img1.jpg)

## Page 22
Figure 10: Spline fits to the sensitivities $\partial_{x_{k}} \widehat{\beta}_{j}\left(\boldsymbol{x}_{i}\right)$ of the continuous variables w.r.t. the binary variables.
pre-trained embedding of dimension $b=50$, we need to align our claim descriptions with the available vocabulary in GloVe. There are only 6 words in our claim descriptions that we could not find in the GloVe vocabulary, so we simply remove these 6 words from our claim descriptions. After these data cleaning the 89 '332 claim descriptions use in total $W=1^{\prime} 013$ different words, and the longest text has length $T=11$. Figure 11 shows the 20 most commonly used words in the claim descriptions, body appearing 4'417 times and left and right appearing 23'818 and 24'686 times, respectively.

# 6.2 Word embedding 

The 89 '332 claim descriptions then need to be transformed so that we can use them as covariates. In a first step we tokenize our vocabulary, which means that we assign to each word a fixed integer $1 \leq w \leq W$. This allows us to map the claim descriptions to integer sequences

$$
\text { ClaimDescription } \mapsto\left(w_{1}, \ldots, w_{T}\right)^{\top} \in\{0,1, \ldots, W\}^{T}
$$

We add 0 because we are padding all claim descriptions to equal lengths $T=11$ by adding zeros at the beginning of the texts. Thus, each claim description is now represented by an integer sequence of length $T=11$, where each component $w_{t} \in\{0,1, \ldots, W\}$ corresponds to a given word of our vocabulary, for instance, the word 'right' has label $w=1$ and 'thumb' has label $w=19$. These labels can be treated as categorical variables, and in NLP one embeds these
![Page 22 Image 1](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p22_img1.jpg)

## Page 23
Figure 11: 20 most frequently used words in the claim descriptions.
(categorical) variables into low-dimensional spaces. In our application we choose embedding dimension $b=50$ and consider the embedding map for our vocabulary

$$
\boldsymbol{e}:\{0,1, \ldots, W\} \rightarrow \mathbb{R}^{b} \quad w \mapsto \boldsymbol{e}(w)
$$

This embedding map should be such that we receive contextual proximity, thus, words with a similar meaning should stand in a neighborhood to each other in this embedding map $\boldsymbol{e}$. This embedding map then allows us to map the claim descriptions to matrices

$$
\text { ClaimDescription } \mapsto \mathrm{M}=\left(\boldsymbol{e}\left(w_{1}\right), \ldots, \boldsymbol{e}\left(w_{T}\right)\right)^{\top} \in \mathbb{R}^{T \times b}
$$

Each row $1 \leq t \leq T$ in this matrix M corresponds to a word embedding $\boldsymbol{e}\left(w_{t}\right) \in \mathbb{R}^{b}$. Such contextual embedding maps can be learned, e.g., using word2vec of Mikolov et al. [16, 17]. We use the pre-trained GloVe embedding $b=50$ that can be downloaded. ${ }^{6}$.

# 6.3 Long short-term memory layers 

### 6.3.1 Long short-term memory architecture for text processing

Coming back to our accident claim data example of Section 1. Each claim $i$ consists of the triple $\left(Y_{i}, \boldsymbol{x}_{i}, \mathrm{M}_{i}\right)$, where $Y_{i}>0$ describes the claim size, $\boldsymbol{x}_{i} \in \mathbb{R}^{q}$ the tabular claim information and $\mathrm{M}_{i} \in \mathbb{R}^{T \times b}$ the claim description. Our goal is to design a suitable regression function

$$
(\boldsymbol{x}, \mathrm{M}) \mapsto \mu(\boldsymbol{x}, \mathrm{M})=\mathbb{E}[Y \mid \boldsymbol{x}, \mathrm{M}]
$$

that describes the conditionally expected claim amount of $Y$, given $\boldsymbol{x}$ and M .
M is a matrix that can be interpreted as a time series as the words stand in a fixed order to each other in the sentence. Such data can be processes by RNNs or CNNs. For illustrative purposes we use a specific RNN architecture that is based on long short-term memory (LSTM)

[^0]
[^0]:    ${ }^{6}$ https://nlp.stanford.edu/projects/glove/
![Page 23 Image 1](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p23_img1.jpg)

## Page 24
layers. These have been introduced by Hochreiter-Schmidhuber [8]; for an extended discussion we refer to our tutorial Richman-Wüthrich [20] and to Chapter 8 in Wüthrich-Merz [31]. An LSTM layer considers a matrix $M \in \mathbb{R}^{T \times b}$ as a time series by processing one word (row of $M$ ) after the other. Moreover, it has a mechanism (memory cell) that encodes the order of the words (in a time-causal sense), that is, it carries forward a memory cell that encodes what has already been read from the given sentence. We will not describe LSTM layers in detail, here. The general functioning of RNNs is illustrated in Figure 8.4 of Wüthrich-Merz [31], ${ }^{7}$ and the LSTM layer/cell is explained in detail in Section 8.3.1 of Wüthrich-Merz [31].
We choose input dimension $b_{0}=b=50$ (embedding dimension) and number of neurons $b_{1} \in \mathbb{N}$. An LSTM layer $\boldsymbol{z}^{\text {LSTM }}$ provides us with the following processing of the text matrix $M$

$$
\boldsymbol{z}^{\mathrm{LSTM}}: \mathbb{R}^{T \times b_{0}} \rightarrow \mathbb{R}^{b_{1}} \quad \mathrm{M} \mapsto \boldsymbol{z}^{\mathrm{LSTM}}(\mathrm{M})
$$

We further process this output by a FFN layer $\boldsymbol{z}^{[1]}: \mathbb{R}^{b_{1}} \rightarrow \mathbb{R}^{b_{2}}$, for some dimension $b_{2} \in \mathbb{N}$, before concatenating the processed text description $M$ with the tabular feature $\boldsymbol{x} \in \mathbb{R}^{q}$

$$
(\boldsymbol{x}, \mathrm{M}) \mapsto \widetilde{\boldsymbol{x}}=\widetilde{\boldsymbol{x}}(\boldsymbol{x}, \mathrm{M})=\left(\boldsymbol{x}^{\top},\left(\boldsymbol{z}^{[1]} \circ \boldsymbol{z}^{\mathrm{LSTM}}\right)(\mathrm{M})\right)^{\top} \in \mathbb{R}^{q_{0}}
$$

with dimension $q_{0}=q+b_{2}$. Now, we are at the stage where we can explore the LocalGLMnet architecture. Regression attentions are constructed as

$$
\begin{aligned}
\boldsymbol{\beta}: \mathbb{R}^{q_{0}} & \rightarrow \mathbb{R}^{q_{0}} \\
\widetilde{\boldsymbol{x}} & \mapsto \boldsymbol{\beta}(\widetilde{\boldsymbol{x}})=\boldsymbol{z}^{(d: 1)}(\widetilde{\boldsymbol{x}})=\left(\boldsymbol{z}^{(d)} \circ \cdots \circ \boldsymbol{z}^{(1)}\right)(\widetilde{\boldsymbol{x}})
\end{aligned}
$$

for a deep FFN network architecture $\boldsymbol{z}^{(d: 1)}$. The LocalGLMnet is obtained by

$$
(\boldsymbol{x}, \mathrm{M}) \mapsto \mu(\boldsymbol{x}, \mathrm{M})=g^{-1}\left(\beta_{0}+\langle\boldsymbol{\beta}(\widetilde{\boldsymbol{x}}(\boldsymbol{x}, \mathrm{M})), \widetilde{\boldsymbol{x}}(\boldsymbol{x}, \mathrm{M})\rangle\right)
$$

We are now ready to see whether we can gain predictive power from the claim descriptions.

# 6.3.2 Lab: LSTM results 

The explicit architecture chosen is shown in Listing 8. We download the pre-trained GloVe embeddings of dimension $b=50$, and these are used in the embedding layer on lines $6-7$ of Listing 8 to embed the $W=1^{\prime} 013$ different words to $\mathbb{R}^{50}$, and the padding label 0 is mapped to the origin in $\mathbb{R}^{b}$. These GloVe embeddings are declared to be non-trainable, i.e., we do not adjust them to our prediction task. In general, one could declare these embeddings to be trainable too, but this requires more data and it will use more computational time. On line 13 the output of the LSTM part $\boldsymbol{z}^{[1]} \circ \boldsymbol{z}^{\mathrm{LSTM}}$ is concatenated with the tabular feature $\boldsymbol{x}^{-} \in \mathbb{R}^{13}$ which gives us a $q_{0}=13+3=16$ dimensional feature vector $\widetilde{\boldsymbol{x}}$. This feature vector is then inputted to the LocalGLMnet, see lines 15-22 of Listing 8. Listing 9 shows on lines 6-17 how we pre-process the claim descriptions, and lines 20-25 give the code to extract the GloVe embedding weights $\boldsymbol{e}(w)$ for the words $0 \leq w \leq W$ used in our claim descriptions.
We are now ready to fit this LSTM-LocalGLMnet architecture to simultaneously process the tabular feature information and the claim descriptions. The results are presented in Table 7.

[^0]
[^0]:    ${ }^{7}$ We do not use a time-distributed FFN layer here, though we could; an architecture with a RNN architecture with a time-distributed FFN layer is shown in Figure 8.5 of Wüthrich-Merz [31]. In our experiments here, a time-distributed FFN layer has not been fully competitive.

## Page 25
|  | in-sample loss on $\mathcal{L}$ |  |  | out-of-sample loss on $\mathcal{T}$ |  |  |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $L_{p=2}$ | $L_{p=2.5}$ | $L_{p=3}$ | $L_{p=2}$ | $L_{p=2.5}$ | $L_{p=3}$ |
| null model | 5.1304 | 1.0196 | 3.5895 | 5.1393 | 1.0200 | 3.5885 |
| gamma FFN net based on $\boldsymbol{x}$ | 4.4714 | 0.9510 | 3.5127 | 4.5542 | 0.9605 | 3.5237 |
| gamma LocalGLMnet based on $\boldsymbol{x}$ | 4.4434 | 0.9460 | 3.5022 | 4.5388 | 0.9588 | 3.5207 |
| gamma LocalGLMnet based on $\boldsymbol{x}^{-}$ | 4.4709 | 0.9497 | 3.5081 | 4.5250 | 0.9580 | 3.5212 |
| LSTM-LocalGLMnet based on $\left(\boldsymbol{x}^{-}, \mathrm{M}\right)$ | 3.8935 | 0.8640 | 3.3569 | 4.0392 | 0.8835 | 3.3867 |

Table 7: In-sample and out-of-sample deviance losses (3.9)-(3.10) for power variance parameters $p=2,2.5,3$; the losses use $v_{i} / \varphi \equiv v_{t}^{\dagger} / \varphi \equiv 1$; for better readability we display losses in indifferent units for different $p$ 's: $10^{0}=1$ for $p=2,10^{-1}$ for $p=2.5$ and $10^{-3}$ for $p=3$.

We observe a major gain in predictive performance through including the claim descriptions.
Fo The difficulty with this solution is that it is biased: the average (in-sample) prediction $\widehat{\mu}\left(\boldsymbol{x}_{i}, \mathrm{M}_{i}\right)$ is $13^{\prime} 514$ whereas the average observed claim amount $Y_{i}$ is $12^{\prime} 718$. One reason for this (big) difference is that we do not use the canonical link $h_{p=2}$ of the gamma model, but the log-link for $g$. Thus, our solution does not fulfill the so-called balance property, see Wüthrich [30], and we need to apply a bias regularization step, we refer to Section 7.4.2 in Wüthrich-Merz [31] for an extended discussion.

Figure 12: (lhs) Auto-calibration property, see also footnote ${ }^{8}$, (rhs) Tukey-Anscombe plot of 5'000 randomly selected claims.

This over-estimation is verified by Figure 12 (lhs) that presents a spline fit to $Y_{i} \sim \widehat{\mu}\left(\boldsymbol{x}_{i}, \mathrm{M}_{i}\right)$, $1 \leq i \leq n .^{8}$ The black dots show this spline fit, which indicates that especially large estimates $\widehat{\mu}\left(\boldsymbol{x}_{i}, \mathrm{M}_{i}\right)$ over-estimate the observations $Y_{i}$ (are below the red diagonal line). This applies to

[^0]
[^0]:    ${ }^{8}$ The spline fit in Figure 12 (lhs) is motivated by the so-called auto-calibration property, meaning that we would like to have $\mathbb{E}[Y \mid \mu(\boldsymbol{x}, \mathrm{M})]=\mu(\boldsymbol{x}, \mathrm{M}), \mathbb{P}$-a.s., see Definition 3.1 in Krüger-Ziegel [11].
![Page 25 Image 1](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p25_img1.jpg)

## Page 26
estimates above $\exp \{11\}=59^{\prime} 874$ (vertical dotted line), which accounts for roughly $1 \%$ of all claims (the blue line shows the empirical density of $\widehat{\mu}\left(\boldsymbol{x}_{i}, \mathrm{M}_{i}\right), 1 \leq i \leq n$ ). The reason for this over-estimation is that the data $Y_{i}$ is too heavy-tailed for a gamma distributional assumption, and, therefore, the gamma model moves the estimates $\widehat{\mu}\left(\boldsymbol{x}_{i}, \mathrm{M}_{i}\right)$ too much towards large observations $Y_{i}$, which is a sort of over-fitting to large observations.

Outlook 6.1 There is no simple solution to solve the over-fitting problem in the upper tail of Figure 12 because, typically, there is no simple off-the-shelf distribution that is suitable for simultaneously modeling the body and the tail of the observations. For this reason, often mixture or composite models are proposed. Alternatively, one could use right-censored data. However, all these proposals lead to difficulties in fitting because they involve the expectation-maximization (EM) algorithm, which is rather slow and difficult in fitting.

The cheap solution is to simply scale $\widehat{\mu}\left(\boldsymbol{x}_{i}, \mathrm{M}_{i}\right)$ with a multiplicative factor such that the estimated claim averages are equal to the average observed claims. With this solution we sacrifice a little bit of predictive power, but we mitigate the bias. This scaling does not significantly improve the upper tail in Figure 12 (lhs), but it rectifies the balance property.

Figure 12 (rhs) gives the Tukey-Anscombe plot plotting the gamma deviance residuals

$$
\varepsilon_{i}=\operatorname{sgn}\left(Y_{i}-\widehat{\mu}\left(\boldsymbol{x}_{i}, \mathrm{M}_{i}\right)\right) \sqrt{\mathfrak{o}_{p=2}\left(Y_{i}, \widehat{\mu}\left(\boldsymbol{x}_{i}, \mathrm{M}_{i}\right)\right)}
$$

against the logged fitted means $\widehat{\mu}\left(\boldsymbol{x}_{i}, \mathrm{M}_{i}\right)$. We make three observations: (1) There are many outliers which also indicates that the model is not sufficiently heavy-tailed for this data. (2) The cyan line shows twice the estimated standard deviation of the residuals $\varepsilon_{i}$. This standard deviation is rather constant across all fitted means $\widehat{\mu}\left(\boldsymbol{x}_{i}, \mathrm{M}_{i}\right)$ which indicates that we can work with a constant dispersion parameter (deviance) estimate $\widehat{\varphi}=1.44$ for this data. ${ }^{9}$ (3) A dispersion parameter estimate bigger than 1 in a gamma model also indicates that the model may not fit, because a dispersion parameter bigger than 1 implies a shape parameter in the gamma model being less than 1. Consequently, the gamma density is strictly decreasing, usually, to compensate for large claims. Such a model does not allow for reasonable claims simulation because it will result in too many samples close to zero.

We conclude that including claim descriptions substantially improves the results in this example. The auto-calibration plot in Figure 12 indicates that we receive a reasonably good model for most of the claims, however, because the observations are more heavy-tailed than the gamma model assumption allows for, we have some over-fitting to large claims. Within Tweedie's family it is not possible to mitigate this problem, the only way out is to consider a more complicated model, i.e., either a model with more parameters, a mixture or a composite model. One could also work with transformed data, e.g., with log-observations. In applications this is not recommended because the balance property may severely fail after back-transformation, and its correction may involve covariates itself which makes the transformed fitting almost useless.

[^0]
[^0]:    ${ }^{9}$ This constant dispersion is rather atypical for real data, i.e., here we can observe that this is (must be) simulated data.

## Page 27
# 7 Conclusions 

This tutorial presents the LocalGLMnet which gives us an interpretable network architecture. We have seen that this architecture allows for variable selection, it allows to quantify variable importance, and it allows for the study of interactions. We have exemplified this on a synthetic accident insurance data set, and we have identified variables that can be dropped from the model. In a second step, we have implemented a NLP pipeline to improve our predictive model by integrating claim descriptions of the individual claims. This has been done by using a LSTM layer that has processed the claim descriptions to tabular data. This tabular representation has then been concatenated with the classical tabular covariate information. Using this joint information as a new input to the LocalGLMnet has equipped us with a network regression model that has provided a substantially better model than the one without the claim descriptions. As a side product we have seen that working with claim sizes can be challenging because the commonly used distributional models for regression modeling are less heavy-tailed than typical insurance claim size data. If this is the case, the regression models often slightly over-fit to the largest claims. This can be partially mitigated by a more robust estimation approach following the lines of Merz-Wüthrich [15]. Moreover, we have discussed forecast dominance by simultaneously considering different deviance loss functions, and we have used an autocalibration plot to back-test the fitted model.

## References

[1] Bahdanau, D., Cho, K., Bengio, Y. (2014). Neural machine translation by jointly learning to align and translate. arXiv:1409.0473
[2] Denuit, M., Charpentier, A., Trufin, J. (2021). Autocalibration and Tweedie-dominance for insurance pricing in machine learning. arXiv:2103.03635
[3] Ferrario, A., Nägelin, M. (2020). The art of natural language processing: classical, modern and contemporary approaches to text document classification. SSRN Manuscript ID 3547887. Version March 1, 2020.
[4] Ferrario, A., Noll, A., Wüthrich, M.V. (2018). Insights from inside neural networks. SSRN Manuscript ID 3226852.
[5] Fissler, T., Lorentzen, C., Mayer, M. (2021). Model comparison and validation: user guide for consistent scoring functions in machine learning and actuarial practice. Preprint.
[6] Gneiting, T. (2011). Making and evaluating point forecasts. Journal of the American Statistical Association 106/494, 746-762.
[7] Gneiting, T., Raftery, A.E. (2007). Strictly proper scoring rules, prediction, and estimation. Journal of the American Statistical Association 102/477, 359-378.
[8] Hochreiter, S., Schmidhuber, J. (1997). Long short-term memory. Neural Computation 9/8, 17351780 .
[9] Jørgensen, B. (1987). Exponential dispersion models. Journal of the Royal Statistical Society, Series B 49/2, 127-145.
[10] Jørgensen, B. (1997). The Theory of Dispersion Models. Chapman \& Hall.
[11] Krüger, F., Ziegel, J.F. (2020). Generic conditions for forecast dominance. Journal of Business $\mathcal{E}$ Economics Statistics, to appear.

## Page 28
[12] Lorentzen, C., Mayer, M. (2020). Peeking into the black box: an actuarial case study for interpretable machine learning. SSRN Manuscript ID 3595944. Version May 7, 2020.
[13] Lundberg, S.M., Lee, S.-I. (2017). A unified approach to interpreting model predictions. In: Advances in Neural Information Processing Systems 30, Guyon, I., Luxburg, U.V., Bengio, S., Wallach, H., Fergus, R., Vishwanathan, S., Garnett, R. (eds.), 4765-74. Montreal: Curran Associates.
[14] Meier, D., Wüthrich, M.V. (2020). Convolutional neural network case studies: (1) anomalies in mortality rates (2) image recognition. SSRN Manuscript ID 3656210.
[15] Merz, M., Wüthrich, M.V. (2021). Deep learning under model uncertainty. SSRN Manuscript ID 3875151 .
[16] Mikolov, T., Chen, K., Corrado, G.S., Dean, J. (2013). Efficient estimation of word representations in vector space. arXiv:1301.3781.
[17] Mikolov, T., Sutskever, I., Chen, K., Corrado, G.S., Dean, J. (2013). Distributed representations of words and phrases and their compositionality. Advances in Neural Information Processing Systems 26, 3111-3119.
[18] Noll, A., Salzmann, R., Wüthrich, M.V. (2018). Case study: French motor third-party liability claims. SSRN Manuscript ID 3164764.
[19] Pennington, J., Socher, R., Manning, C.D. (2014). GloVe: global vectors for word representation. Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), 1532-1543.
[20] Richman, R., Wüthrich, M.V. (2019). Lee and Carter go machine learning: recurrent neural networks. SSRN Manuscript ID 3441030.
[21] Richman, R., Wüthrich, M.V (2021). LocalGLMnet: interpretable deep learning for tablular data. SSRN Manuscript ID 3892015.
[22] Savage, L.J. (1971). Elicitable of personal probabilities and expectations. Journal of the American Statistical Association 66/336, 783-810.
[23] Schelldorfer, J., Wüthrich, M.V. (2019). Nesting classical actuarial models into neural networks. SSRN Manuscript ID 3320525.
[24] Shapley, L.S. (1953). A Value for n-Person Games. In: Contributions to the Theory of Games (AM-28), Vol. II. Kuhn, H.W., Tucker, A.W. (eds.), Princeton University Press, 307-318.
[25] Smyth, G.K., Verbyla, A.P. (1999). Double generalized linear models: approximate REML and diagnostics. In: Proceedings of the 14th International Workshop on Statistical Modelling. Friedl, H., Berghold, A., Kauermann, G. (Eds.). Technical University, Graz, Austria, 66-80.
[26] Sundararajan, M., Najmi, A. (2020). The many Shapley values for model explanation. arXiV:1908.08474v2
[27] Sundararajan, M., Taly, A., Yan, Q. (2017). Axiomatic attribution for deep networks. In: Proceedings of the 34th International Conference on Machine Learning, Proceedings of Machine Learning Research, PMLR. International Convention Centre, Sydney, Australia, 70, 3319-3328.
[28] Tweedie, M.C.K. (1984). An index which distinguishes between some important exponential families. In: Statistics: Applications and New Directions. Ghosh, J.K., Roy, J. (Eds.). Proceeding of the Indian Statistical Golden Jubilee International Conference, Indian Statistical Institute, Calcutta, 579-604.
[29] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł., Polosukhin, I. (2017). Attention is all you need. arXiv:1706.03762v5

## Page 29
[30] Wüthrich, M.V. (2020). Bias regularization in neural network models for general insurance pricing. *European Actuarial Journal* **10/1**, 179-202.

[31] Wüthrich, M.V., Merz, M. (2021). Statistical foundations of actuarial learning and its applications. *SSRN Manuscript ID* 3822407.

29

## Page 30
# A Exploratory data analysis: plots 


Figure 13: Number of claims and average claims per AccYear, AccMonth and AccWeekday.

Figure 14: Number of claims and average claims per AccTime and RepDelay.
![Page 30 Image 1](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p30_img1.jpg)
![Page 30 Image 2](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p30_img2.jpg)

## Page 31
Figure 15: Number of claims and average claims per Age, Gender and MaritalStatus.

Figure 16: Number of claims and average claims per DependentChildren, DependentsOther and WeeklyPay.
![Page 31 Image 1](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p31_img1.jpg)
![Page 31 Image 2](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p31_img2.jpg)

## Page 32
Figure 17: Number of claims and average claims per PartTimeFullTime, HoursWorkedPerWeek and DaysWorkedPerWeek.

|   | Age | WPay | Hours/W | Days/W | AccYear | AccMonth | Weekday | AccTime | RepDelay  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Age |  | 0.17 | 0.04 | 0.03 | 0.09 | -0.01 | 0.01 | -0.03 | 0.00  |
|  WeeklyPay | 0.17 |  | 0.47 | 0.13 | 0.43 | 0.00 | 0.00 | -0.05 | -0.05  |
|  Hours/Week | 0.04 | 0.47 |  | 0.20 | 0.30 | 0.00 | -0.01 | -0.02 | -0.04  |
|  Days/Week | 0.03 | 0.13 | 0.20 |  | -0.03 | 0.00 | 0.00 | -0.01 | -0.02  |
|  AccYear | 0.09 | 0.43 | 0.30 | -0.03 |  | -0.04 | 0.00 | -0.04 | -0.02  |
|  AccMonth | -0.01 | 0.00 | 0.00 | 0.00 | -0.04 |  | 0.01 | -0.01 | 0.00  |
|  AccWeekday | 0.01 | 0.00 | -0.01 | 0.00 | 0.00 | 0.01 |  | 0.00 | 0.00  |
|  AccTime | -0.03 | -0.05 | -0.02 | -0.01 | -0.04 | -0.01 | 0.00 |  | 0.03  |
|  RepDelay | 0.00 | -0.05 | -0.04 | -0.02 | -0.02 | 0.00 | 0.00 | 0.03 |   |

Table 8: Correlations between continuous covariates.
![Page 32 Image 1](cs10_localglmnet_a_deep_learning_architecture_for_actuaries_assets/cs10_localglmnet_a_deep_learning_architecture_for_actuaries_p32_img1.jpg)

## Page 33
# B R code 

Listing 3: Definition of scoring functions.

```
gamma_loss <- function(y_true, y_pred){2*k_mean(y_true/y_pred - 1 - log(y_true/y_pred))}
IG_loss <- function(y_true, y_pred){k_mean((y_true-y_pred)^2/(y_pred^2*y_true))}
p_loss <- function(y_true, y_pred){2*k_mean(y_true^(2-p)/((1-p)*(2-p))
    -y_true*y_pred^(1-p)/(1-p)+y_pred^(2-p)/(2-p))}
```


## Listing 4: Chosen FFN network architecture.

```
design = layer_input(shape = c(16), dtype = 'float32', name = 'design')
#
output = design %>%
    layer_dense(units=20, activation='tanh', name='layer1') %>%
    layer_dense(units=15, activation='tanh', name='layer2') %>%
    layer_dense(units=10, activation='tanh', name='layer3') %>%
    layer_dense(units=1, activation='exponential', name='output)
#
model = keras_model(inputs = list(design), outputs = c(output))
#
CB <- callback_model_checkpoint("path", monitor = "val_loss", verbose = 0,
                                    save_best_only = TRUE, save_weights_only = TRUE)
#
model %>%
compile(loss = gamma_loss, optimizer = 'nadam')
#
fit <- model %>%
fit(list(XX), list(YY), validation_split=0.2,
                                    batch_size=5000, epochs=100, verbose=0, callbacks=CBs)
#
load_model_weights_hdf5(model, "path")
```

Listing 5: Chosen LocalGLMnet network architecture.

```
design = layer_input(shape = c(16), dtype = 'float32', name = 'design')
#
attention = design %>%
    layer_dense(units=20, activation='tanh', name='layer1') %>%
    layer_dense(units=15, activation='tanh', name='layer2') %>%
    layer_dense(units=10, activation='tanh', name='layer3') %>%
    layer_dense(units=16, activation='linear', name='attention')
#
output = list(design, attention) %>%
    layer_dot(name='LocalGLM', axes=1) %>%
    layer_dense(units=1, activation='exponential', name='output')
#
model = keras_model(inputs = list(design), outputs = c(output))
#
CB <- callback_model_checkpoint("path", monitor = "val_loss", verbose = 0,
                                    save_best_only = TRUE, save_weights_only = TRUE)
#
model %>%
compile(loss = gamma_loss, optimizer = 'nadam')
#
fit <- model %>%
fit(list(XX), list(YY), validation_split=0.2,
                                    batch_size=5000, epochs=100, verbose=0, callbacks=CBs)
#
22
load_model_weights_hdf5(model, "path")
```

## Page 34
Listing 6: Extraction of estimated regression attentions.
1
```
    ww <- get_weights(model)
2 zz <- keras_model(inputs=model$input, outputs=get_layer(model, 'attention')$output)
3 #
4 beta.x <- data.frame(zz %>% predict(list(XX)))
5
beta.x <- beta.x * as.numeric(ww[[9]])
```


# Listing 7: Extraction of interactions. 

```
1 j <- 1 # select covariate component
2 #
3 beta.x = attention %>% layer_lambda(function(x) x[,j])
4}\mathrm{ model.2 = keras_model(inputs = c(design), outputs = c(beta.x))
5 #
6 grad = beta.x %>% layer_lambda(function(x) k_gradients(model.2$outputs, model.2$inputs))
7}\mathrm{ model.grad = keras_model(inputs = c(design), outputs = c(grad))
8 #
9 grad.beta.x = data.frame(model.grad %>% predict(XX))
```


## Listing 8: Chosen LSTM-LocalGLMnet network architecture for text processing.

```
design = layer_input(shape = c(13), dtype = 'float32', name = 'design')
#
NLP = layer_input(shape = c(11), name = "NLP")
#
NLPemb = NLP %>%
    layer_embedding(input_dim = 1013+1, output_dim = 50, input_length = 11,
                            weights=list(GloVe), trainable=FALSE, name='NLPemb')
#
LSTMtext = NLPemb %>%
    layer_1stm(units=15, activation='tanh', name='LSTM1', return_sequences=FALSE) %>%
    layer_dense(units=3, activation='tanh', name='FNLayer2')
#
13 tabular = list(design, LSTMtext) %>% layer_concatenate()
#
15 attention = tabular %>%
    layer_dense(units=20, activation='tanh', name='layer1') %>%
    layer_dense(units=15, activation='tanh', name='layer2') %>%
    layer_dense(units=10, activation='tanh', name='layer3') %>%
    layer_dense(units=13+3, activation='linear', name='attention')
#
21 output = list(tabular, attention) %>% layer_dot(name='LocalGLM', axes=1) %>%
22
    layer_dense(units=1, activation='exponential', name='output')
23 #
24 model = keras_model(inputs = list(design, NLP), outputs = c(output))
25 #
26 model %>%
    compile(loss = gamma_loss, optimizer = 'nadam')
```

## Page 35
Listing 9: Tokenizer and extracting the GloVe embeddings for the words used.
⬇
1 # load GloVe
2 vectors = data.table::fread('glove.6B.50d.txt', data.table = F, encoding = 'UTF-8')
3 colnames(vectors) = c('word',paste('dim',1:50,sep = '_'))
4 #
5 # pre-process ClaimDescription
6 dat <- dat1 %>% mutate(clean = ClaimDescription %>% str_to_lower() %>%
7 removeWords(stopwords("en")) %>% str_squish())
8 #
9 removewords <- c("abdomin", "epicondylitis", "gyprock", "handpiece", "repetative", "secateurs")
10 dat1$clean <- str_squish(removeWords(dat1$clean, words=removewords))
11 #
12 tokenizer <- text_tokenizer() %>% fit_text_tokenizer(dat1$clean)
13 text.matrix <- texts_to_matrix(tokenizer, dat1$clean, mode="count")
14 max.words <- length(colSums(text.matrix)[-1])
15 maxlen <- max(rowSums(text.matrix))
16 #
17 x.learn <- texts_to_sequences(tokenizer, dat1$clean) %>% pad_sequences(maxlen = maxlen)
18 #
19 # extract GloVe embeddings
20 word_indices = unlist(tokenizer$word_index)
21 voci < = data.frame(word = names(word_indices), key = word_indices, stringsAsFactors = FALSE)
22 emb <- merge(x=voci, y=vectors, by="word", all.x=TRUE)
23 emb <- emb[order(emb$key),]
24 #
25 GloVe <- rbind(t(rep(0,50)), as.matrix(emb[,3:(50+2)]))