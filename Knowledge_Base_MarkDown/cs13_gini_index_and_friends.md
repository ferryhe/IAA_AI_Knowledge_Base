_Note: Source document was split into 3 OCR chunks (pages 1-12, pages 13-24, pages 25-35) to stay within token limits._

# CS13 Gini Index and Friends

## Page 1
# Gini Index and Friends 

Christian Lorentzen* Michael Mayer ${ }^{\dagger}$ Mario V. Wüthrich ${ }^{\ddagger}$<br>Prepared for:<br>Fachgruppe "Data Science"<br>Swiss Association of Actuaries SAV

Version of October 14, 2022


#### Abstract

In the machine learning community, the Gini index is a very popular score for model selection, and it is also used in actuarial science for evaluating insurance pricing models. The purpose of this tutorial is to discuss the Gini index, both its version in economics and its version in machine learning, which differ. We discuss its relationship to the area under the curve (AUC) of the receiver operating characteristics (ROC) curve, which is often used for model selection in binary classification problems. A main deficiency of the Gini index is that it does not give us a consistent scoring function. Therefore, simply maximizing the Gini index may lead to wrong decisions. The issue is that the Gini index is a rank-based score that is not calibration-sensitive. However, if we use the Gini index for scoring within the class of auto-calibrated regression models, it gives us a strictly consistent scoring function and, henceforth, a sensible model selection tool. This will be discussed in this tutorial.


Keywords. Gini index, Gini score, Gini coefficient, accuracy ratio, consistency, consistent scoring, auto-calibration, Lorenz curve, concentration curve, cumulative accuracy profile, CAP, receiver operating characteristics curve, ROC curve, area under the curve, AUC, model selection, binary classification, regression model.

## 0 Introduction and overview

This data analytics tutorial has been written for the working group "Data Science" of the Swiss Association of Actuaries SAV, see
https://www.actuarialdatascience.org
The Gini index is a very popular score for model selection in the machine learning community. It is also used in actuarial modeling for evaluating non-life insurance pricing models and in finance for evaluating credit risk models; see Frees et al. [18, 19], Denuit et al. [9, 10, 11], So et al. [41], Engelmann et al. [14] and Tasche [43, 44]. The purpose of this tutorial is to discuss the Gini index, both its version in economics and its version in machine learning, which

[^0]
[^0]:    *la Mobilière, Bern, christian.lorentzen@mobiliar.ch
    ${ }^{\dagger}$ la Mobilière, Bern, michael.mayer@mobiliar.ch
    ${ }^{\ddagger}$ RiskLab, Department of Mathematics, ETH Zurich, mario.wuethrich@math.ethz.ch

## Page 2
differ. We discuss its relationship to the area under the curve (AUC) of the receiver operating characteristics (ROC) curve, which is a popular tool for model selection in binary classification problems. The main deficiency of the Gini index is that, in general, it does not give a consistent scoring function. Therefore, simply maximizing the Gini index may lead to wrong decisions because the true model may not be the one that maximizes the Gini index. The issue is that the Gini index is a rank-based score that is not calibration-sensitive, this is illustrated in Section 2.5 , below. However, if we restrict Gini index scoring to the class of auto-calibrated regression models, it gives us a strictly consistent scoring function for the mean functional and, henceforth, a sensible model selection tool. We discuss auto-calibration in Section 2.6, below, as this is of crucial importance in actuarial pricing. For a general reference on the Gini methodology and its use in different fields, we refer to Yitzhaki-Schechtman [48].

Organization. In Section 1 we introduce the Gini index as it is used in economics, with a small excursion into impurity functions of decision trees for classification. In Section 2 we introduce the machine learning version of the Gini index. We do this on a binary classification problem because in that case the Gini index is equivalent to the area under the curve (AUC) of the receiver operating characteristics (ROC) curve. However, the Gini index in machine learning is more general and it can also be used for regression models. In Section 2.5 we discuss the drawbacks of using the Gini index for model selection, in general, the Gini index does not give a (strictly) consistent scoring function. Under the additional assumption of auto-calibration, the Gini index allows for strictly consistent scoring, this is discussed in Section 2.6. In Section 3 we conclude.

# 1 The Gini index in economics 

The Gini index (also called Gini coefficient, Gini ratio or Gini score) is used in different scientific fields, and it has slightly varying definitions in these different fields. Originally, it was introduced by the statistician Corrado Gini $[20,21]$ in 1912, and it is based on the work of the economist Max O. Lorenz [32] who introduced the so-called Lorenz curve in 1905. The original Gini index was used in economics to describe the wealth dispersion or the income inequality within a given population.
In Section 1.1, we start by describing the case of a continuous distribution function $F$, because this is simpler. In Sections 1.2 and 1.3, we briefly sketch the discrete case which is of central interest in empirical data situations and in decision tree modeling. We are going to consider a response variable $Y \sim F$. In actuarial modeling, this response variable may reflect an individual random claim size, and in economics it can either describe the income or the wealth of a randomly selected individual person from a given population.

### 1.1 Continuous distribution case

Assume the real-valued non-negative claim size $Y$ has distribution function $F$ with finite first moment $\mu=\mathbb{E}[Y]<\infty$. We consider a continuous distribution function $F$ in this section. The left-continuous generalized inverse of the distribution function $F$, also called quantile, is given by

$$
\alpha \in(0,1) \quad \mapsto \quad F^{-1}(\alpha)=\inf \{y \in \mathbb{R} ; F(y) \geq \alpha\}
$$

## Page 3
Continuity of $F$ implies $F\left(F^{-1}(\alpha)\right)=\alpha$. In actuarial science one considers the loss size index function for non-negative claim sizes $Y$ with finite first moment

$$
y \geq 0 \quad \mapsto \quad I_{F}(y)=\frac{1}{\mu} \int_{0}^{y} z d F(z)=\frac{1}{\mathbb{E}[Y]} \mathbb{E}\left[Y \mathbb{1}_{\{Y \leq y\}}\right] \in[0,1]
$$

The loss size index $I_{F}(y)$ expresses the proportion of the expected claim amount $\mu=\mathbb{E}[Y]$ that is explained by the claims $Y$ being less or equal to $y$. The loss size index function is an example of a size-biased distribution which is a popular tool in probability and statistics, see Arratia-Goldstein [3].
The loss index size function is closely related to the Lorenz curve [32] that is used in economics to measure inequality (disparity) in wealth distribution. The Lorenz curve measures which proportion of the population contributes which share to the total wealth. The Lorenz curve is received by either plotting the two-dimensional graph

$$
\left(F(y), I_{F}(y)\right) \in[0,1]^{2} \quad \text { for } y \geq 0
$$

or by plotting the following Lorenz curve function $L_{F}$ which is obtained from the above by re-scaling with the quantile functional

$$
\begin{aligned}
\alpha \in(0,1) \quad \mapsto \quad L_{F}(\alpha):=I_{F}\left(F^{-1}(\alpha)\right) & =\frac{1}{\mu} \int_{0}^{F^{-1}(\alpha)} z d F(z) \\
& =\frac{1}{\mathbb{E}[Y]} \mathbb{E}\left[Y \mathbb{1}_{\{Y \leq F^{-1}(\alpha)\}}\right] \in[0,1]
\end{aligned}
$$

Considering the variable transformation $p \mapsto z=F^{-1}(p)$, the Lorenz curve can be rewritten as

$$
\alpha \in(0,1) \quad \mapsto \quad L_{F}(\alpha)=\frac{1}{\mu} \int_{0}^{\alpha} F^{-1}(p) d p \in[0,1]
$$

This latter expression is closely related to the expected shortfall considered in risk managementwe only need to replace the mean $\mu$ in the denominator by the quantile level $\alpha$. In applied nonlife insurance claim size modeling, one often finds the so-called 20-80 Pareto principle meaning that the $20 \%$ largest claims explain $80 \%$ of the total claim amount, or, vice versa, $L_{F}(80 \%)=$ $I_{F}\left(F^{-1}(80 \%)\right)=20 \% .{ }^{1}$ This is a typical sign of heavy-tailed claim sizes; see Section 8.2.3 in Embrechts et al. [13].

Example 1.1 (gamma distribution) The gamma distribution is absolutely continuous with density on the positive real line $\mathbb{R}_{+}$given by

$$
f(y)=\frac{c^{\gamma}}{\Gamma(\gamma)} y^{\gamma-1} \exp \{-c y\} \quad \text { for } y>0
$$

with shape parameter $\gamma>0$ and scale parameter $c>0$, and we write $Y \sim \Gamma(\gamma, c)$. The gamma distribution has mean $\mu=\mathbb{E}[Y]=\gamma / c$, and the loss size index function is for $y \geq 0$

$$
I_{\Gamma(\gamma, c)}(y)=\int_{0}^{y} \frac{c^{\gamma+1}}{\Gamma(\gamma+1)} z^{\gamma} \exp \{-c z\} d z=\frac{1}{\Gamma(\gamma+1)} \int_{0}^{c y} z^{\gamma} \exp \{-z\} d z
$$

[^0]
[^0]:    ${ }^{1}$ In fact, the Pareto distribution has the property that we can recursively iterate the procedure of taking the $20 \%$ largest claims of the corresponding lower-truncated claims. These $20 \%$ largest claims then explain $80 \%$ of the corresponding total lower-truncated claim amount (this comes from the memoryless property of the exponential distribution). The 20-80 Pareto principle is equivalent to considering a Pareto distribution with a tail parameter of $\log _{4}(5)=1.161$.

## Page 4
The latter is the probability that a gamma distributed random variable with shape parameter $\gamma+1>1$ and scale parameter $c>0$ is less or equal to $y$; note that the integral reflects an incomplete $\Gamma$-function. Thus, the loss size index function in the gamma case results in the computation of the gamma quantile of a size-biased transformed gamma random variable with shape parameter transformation $\gamma \mapsto \gamma+1$.

Figure 1: Lorenz curve $\alpha \mapsto L_{\Gamma(\gamma, c)}(\alpha)$ for the gamma distributed random variable $Y \sim \Gamma(\gamma=$ $1, c=1$ ) (red line); the blue dotted line (diagonal) shows complete equality, and the orange dotted line maximal inequality.

The red line in Figure 1 shows the Lorenz curve $\alpha \mapsto L_{\Gamma(\gamma, c)}(\alpha)$ in the case of a gamma distributed random variable $Y \sim \Gamma(\gamma, c)$. This red line is compared to the Lorenz curve where we have complete equality (only one possible claim size reflected by a Dirac distribution, diagonal dotted line in blue color), the difference resulting in the blue area A. The other extreme case is where we have maximal inequality in claim sizes, basically the largest claim explaining the entire mean $\mu$. This is illustrated by the (right-angled) orange dotted line, and the difference resulting in the orange area B.
Figure 2 shows Lorenz curves in the gamma case with fixed mean $\mu=\gamma / c$ of the gamma distribution and varying shape parameter $\gamma \in[1 / 10,10]$. The larger the shape parameter is, the less variability we have, and the more the Lorenz curve approaches the straight line of complete equality (blue line). In fact, in the limit for $\gamma \rightarrow \infty$, the Lorenz curve approaches the straight line of complete equality, and for $\gamma \rightarrow 0$ the Lorenz curve approaches the other extreme case of maximal inequality (green dotted line); note that the coefficient of variation in the gamma case is given by

$$
\operatorname{Vco}(Y)=\frac{\operatorname{Var}(Y)^{1 / 2}}{\mathbb{E}[Y]}=1 / \sqrt{\gamma}
$$

The Lorenz curve is invariant under scaling $\rho Y$ with positive constants $\rho>0,{ }^{2}$ and since the gamma distribution has the property $\rho Y \sim \Gamma(\gamma, c / \rho)$ for $Y \sim \Gamma(\gamma, c)$, we conclude that the Lorenz curve is invariant under different choices of the scale parameter $c>0$.

[^0]
[^0]:    ${ }^{2}$ In fact, one can prove that the Lorenz curve is the same for two different continuous distributions if and only if we have a scale transformation, see Lemma 2 in Fellman [15].
![Page 4 Image 1](cs13_gini_index_and_friends_assets/cs13_gini_index_and_friends_p04_img1.jpg)

## Page 5
Figure 2: Lorenz curve $\alpha \mapsto L_{\Gamma(\gamma, c)}(\alpha)$ for the gamma distribution with fixed mean parameter $\mu=1$ and different shape parameters $\gamma \in[1 / 10,10]$ (from light cyan to red).

The Gini index [21] summarizes the Lorenz curve in one single number. It is received by integrating the Lorenz curve $L_{F}(\cdot)$, resulting in a comparison of the areas A and B in Figure 1.
The Gini index in economics of a distribution $F$ is defined by

$$
G_{F}^{\text {eco }}=\frac{\operatorname{area}(\mathrm{A})}{\operatorname{area}(\mathrm{A}+\mathrm{B})}=2 \operatorname{area}(\mathrm{~A})=1-2 \operatorname{area}(\mathrm{~B}) \in[0,1]
$$

E Economics interpretation. The smaller the Gini index $G_{F}^{\text {eco }}$, the closer we are to the case of complete equality, and a Gini index of 1 reflects maximal inequality (disparity).

The following expressions are equivalent versions of the Gini index for a positively supported continuous distribution $F$ with finite mean $\mu=\mathbb{E}[Y]<\infty$, where $Y \sim F$,

$$
\begin{aligned}
G_{F}^{\text {eco }} & =1-2 \int_{0}^{1} L_{F}(\alpha) d \alpha \\
& =\frac{1}{2 \mu} \int_{0}^{\infty} \int_{0}^{\infty}|y-z| d F(z) d F(y)=\frac{1}{2 \mu} \mathbb{E}[[Y-\widetilde{Y}]] \\
& =1-\frac{1}{\mu} \mathbb{E}[\min (Y, \widetilde{Y})] \\
& =1-\frac{1}{\mu} \int_{0}^{\infty}(1-F(y))^{2} d y \\
& =\frac{1}{\mu} \int_{0}^{\infty} F(y)(1-F(y)) d y \\
& =\frac{2}{\mu} \operatorname{Cov}(Y, F(Y))
\end{aligned}
$$

where $\widetilde{Y}$ is an independent copy of $Y$; lines 2-6 of (1.5) correspond to (2.1), (2.5), (2.8), (2.9) and (2.15) in Yitzhaki-Schechtman [48], and the first line of (1.5) is obtained from Section 5.1
![Page 5 Image 1](cs13_gini_index_and_friends_assets/cs13_gini_index_and_friends_p05_img1.jpg)

## Page 6
of Yitzhaki-Schechtman [48]. ${ }^{3}$ Focusing on line (1.5), Yitzhaki-Schechtman [48] rather study the so-called mean absolute difference or Gini mean difference (GMD) given by

$$
\mathrm{GMD}_{F}=\mathbb{E}[|Y-\widetilde{Y}|]
$$

where $Y, \widetilde{Y} \sim F$ are two independent copies. Thus, the Gini index in economics $G_{F}^{\text {eco }}$ is equal to the mean absolute difference $\mathrm{GMD}_{F}$ scaled by twice the mean $\mu$, and $\mathrm{GMD}_{F}$ describes a $U$-statistics.

For a wide variety of distribution functions $F$, the Gini index in economics $G_{F}^{\text {eco }}$ can be calculated explicitly, e.g., for the uniform, the gamma, the Weibull, the log-normal or the Pareto distributions.

Example 1.1, revisited. In the gamma case $Y \sim F=\Gamma(\gamma, c)$, the Gini index in economics is given by, see formula (2.2) in McDonald-Jensen [33],

$$
G_{\Gamma(\gamma, c)}^{\mathrm{eco}}=\frac{\Gamma(\gamma+1 / 2)}{\sqrt{\pi} \Gamma(\gamma+1)}
$$

Note that this Gini index only depends on the shape parameter $\gamma>0$ in the gamma model. This also reflects the scale invariance mentioned in Example 1.1 above, and in Footnote 2.

Figure 3: Gini index $G_{\Gamma(\gamma, c)}^{\text {eco }}$ in the gamma distribution case for different shape parameters $\gamma>0$.
Figure 3 shows the Gini index in economics $G_{\Gamma(\gamma, c)}^{\text {eco }}$ of the gamma model for different shape parameters $\gamma>0$. It is monotonically decreasing in $\gamma$, which means that the coefficient of variation goes to zero as the shape parameter increases, see (1.3). Basically, for $\gamma \rightarrow \infty$, it converges to the case of complete equality where all claims $Y$ are of the same size $\mu$, while for $\gamma \rightarrow 0$, it approaches the case of maximal inequality.

The Gini index in economics $G_{F}^{\text {eco }}$, the loss size index function $I_{F}(\cdot)$ and the Lorenz curve $L_{F}(\cdot)$ are useful tools to describe disparity in claim sizes (in insurance) and in wealth and income

[^0]
[^0]:    ${ }^{3}$ The identities in (1.5) can easily be verified for the $(0,1)$-uniform distribution which gives $G_{(0,1)}^{\text {eco }}=1 / 3$. We emphasize that the $(0,1)$-uniform distribution does not reflect complete equality, but this would be for the Dirac distribution. Essentially, the formal proofs of the identities in (1.5) only use integration by parts.
![Page 6 Image 1](cs13_gini_index_and_friends_assets/cs13_gini_index_and_friends_p06_img1.jpg)

## Page 7
distributions (in economy), when we assume that the claims (in insurance) or the wealth and income distributions (in economy) can be described by a distribution function $F$. Below, we are also going to use the Gini index to describe heterogeneity (disparity) of systematic effects in regression functions. This will give us a different version (and interpretation) of the Gini index.

# 1.2 Empirical distribution case 

The previous considerations of the Gini index in economics $G_{F}^{\text {eco }}$ have assumed that the true distribution function $F$ is known (and continuous). In most applied situations this is not the case, and it needs to be approximated empirically. Assume that we have non-negative i.i.d. data $Y_{1}, \ldots, Y_{n}$ generated from an unknown positively supported distribution function $F$. This allows us to consider the empirical distribution given by

$$
y \mapsto \widehat{F}_{n}(y)=\frac{1}{n} \sum_{i=1}^{n} \mathbb{1}_{\left\{y \leq Y_{i}\right\}}
$$

This empirical distribution converges to the true distribution uniformly, $\mathbb{P}$-a.s., for sample size $n \rightarrow \infty$; this is the Glivenko-Cantelli result $[22,6]$. The left-continuous generalized inverse of the empirical distribution is for $\alpha \in(0,1)$ given by

$$
\widehat{F}_{n}^{-1}(\alpha)=Y_{(\lceil\alpha n\rceil}
$$

with order statistics $Y_{(1)} \leq Y_{(2)} \leq \ldots \leq Y_{(n)}$, indicated by the lower round brackets $(\cdot)$, and where $\lceil\alpha n\rceil$ denotes the smallest integer bigger or equal to $\alpha n$. Let $\widehat{\mu}=\frac{1}{n} \sum_{i=1}^{n} Y_{i}$ denote the empirical mean. In this empirical case, the Lorenz curve is defined by

$$
\alpha \in(0,1) \quad \mapsto \quad \widehat{L}_{n}(\alpha):=L_{\widehat{F}_{n}}(\alpha):=I_{\widehat{F}_{n}}\left(\widehat{F}_{n}^{-1}(\alpha)\right)=\frac{1}{\widehat{\mu}} \frac{1}{n} \sum_{i=1}^{\lceil\alpha n\rceil} Y_{(i)}
$$

We can either use the notation $\widehat{L}_{n}(\alpha)$ to express that (1.7) is an empirical value of the true Lorenz curve (1.2), or we can use the notation $L_{\widehat{F}_{n}}(\alpha)$ to express that we calculate the Lorenz curve of the empirical distribution.
This allows us to define the Gini index in economics on the empirical data

$$
G_{\widehat{F}_{n}}^{\text {eco }}=\frac{1}{2 \widehat{\mu}} \frac{1}{n^{2}} \sum_{i=1}^{n} \sum_{j=1}^{n}\left|Y_{i}-Y_{j}\right|=\frac{1}{\widehat{\mu}} \frac{1}{n^{2}} \sum_{i=1}^{n} Y_{(i)}(2 i-n-1)
$$

This is the empirical counterpart of (1.5), and there are other equivalent formulations to calculate the Gini index in economics in the empirical case; note that these empirical versions need some care if there are ties in the observations $Y_{1}, \ldots, Y_{n}$, which may occur if we work with noncontinuous models. This empirical version $G_{\widehat{F}_{n}}^{\text {eco }}$ is the quantity that is usually used in economics to summarize (by a single index) the wealth or income disparity in a given economy. ${ }^{4}$

[^0]
[^0]:    ${ }^{4}$ See, e.g., https://data.oecd.org/inequality/income-inequality.html.

## Page 8
# 1.3 Discrete distribution case 

For a dichotomous (Bernoulli) random variable $Y \in\{0,1\}$ with probability $p=\mathbb{P}(Y=1)=$ $\mathbb{E}[Y]=\mu$, the Gini index simplifies to

$$
G_{p}^{\text {eco }}=\frac{1}{2 \mu} \mathbb{E}[[Y-\bar{Y}]]=1-p
$$

Interestingly, we recover twice the variance of a Bernoulli distributed random variable if we rescale by $2 \mu$, leading to the mean absolute difference $\mathrm{GMD}_{p}=2 p(1-p)$. This can be generalized to a categorical random variable $Y$ taking $K$ levels and $p_{k}$ being the probability of level $k$. We therefore consider $|Y-\bar{Y}|=1-\delta_{\{Y=\bar{Y}\}}$. This gives us the mean absolute difference

$$
\mathrm{GMD}_{p_{k}}=\sum_{k=1}^{K} p_{k} \sum_{k^{\prime} \neq k} p_{k^{\prime}}=\sum_{k=1}^{K} p_{k}\left(1-p_{k}\right)=1-\sum_{k=1}^{K} p_{k}^{2}
$$

In fact, this mean absolute difference provides us with the Brier score, see Example 1 of GneitingRaftery [24]. It is also this rescaled form of the Gini index in economics, i.e., the absolute mean difference GMD, that is used in decision trees for classification. Decision trees are a very common class of machine learning models, in particular, as base learners for ensemble models such as random forests and gradient boosted trees. Fitting a decision tree includes repeatedly finding a threshold in a feature to split a tree node into two nodes. The thresholds are usually found by maximizing the decrease in impurity over possible thresholds. One such impurity function for classification problems with $K$ classes is exactly the above Gini mean difference $\mathrm{GMD}_{\hat{p}_{k}}$ with empirical class probability $\hat{p}_{k}$ for class $k$ in a node, in that case we speak about Gini impurity. Another such impurity function is the Shannon entropy, see [28].

## 2 The Gini index in machine learning

In machine learning (ML) the Gini index is frequently used for model selection in binary classification problems. These ML applications use a slightly different version of the Gini index which we are going to introduce in this section. We will also explain the critical points of using the Gini index as a general model selection tool, and we are going to propose an improvement using auto-calibration which mitigates the critical issues in using the Gini index as a model selection tool. In this section, we only consider classification. In Section 2.7 we highlight the use of the proposed concepts in the general regression case. The reason for focusing on a binary classification problem in this section is that this can be related to the receiver operating characteristics (ROC) curve which is frequently studied in binary classification problems.

### 2.1 Binary classification problem and deviance losses

We consider simulated data describing a binary classification problem. ${ }^{5}$ For this we choose a (true) regression function $\boldsymbol{x} \mapsto p^{\dagger}(\boldsymbol{x}) \in(0,1)$, and we simulate independent binary data as follows

$$
Y_{j} \sim \operatorname{Bernoulli}\left(p^{\dagger}\left(\boldsymbol{x}_{j}\right)\right)
$$

[^0]
[^0]:    ${ }^{5}$ The R code to replicate this example can be downlowded from https://github.com/JSchelldorfer/ ActuarialDataScience/tree/master/13\%20-\%20Gini\%20Index.

## Page 9
based on given i.i.d. covariates $\boldsymbol{x}_{j}, j \geq 1 .{ }^{6}$ For our example, we choose two-dimensional covariates $\boldsymbol{x}_{j}$, with a first continuous component being $(-1 / 2,1 / 2)$-uniform distributed and a second categorical component having three levels with equal probabilities.
To work in a proper statistical modeling setup, we generate two data sets with independent responses $\mathcal{L}=\left(Y_{j}, \boldsymbol{x}_{j}\right)_{1 \leq j \leq n}$ and $\mathcal{T}=\left(Y_{i}, \boldsymbol{x}_{i}\right)_{1 \leq i \leq n}$. The first data set $\mathcal{L}$ is the learning data set $^{7}$ solely used for model fitting (in-sample), and the second data set $\mathcal{T}$ is the test data set ${ }^{8}$ only used for model testing and model selection (out-of-sample). In our simulated data, both data sets $\mathcal{L}$ and $\mathcal{T}$ have a sample size of 10 '000. We are going to fit four different models to the learning data $\mathcal{L}$ as illustrated in the following table:

| $\boldsymbol{x} \mapsto p^{\dagger}(\boldsymbol{x})$ | true regression model from which $\mathcal{L}$ and $\mathcal{T}$ are simulated |
| :-- | :-- |
| $\boldsymbol{x} \mapsto \widehat{p}_{0}(\boldsymbol{x}) \equiv \widehat{p}_{0}$ | null (homogeneous) model not considering any covariates $\boldsymbol{x}$ |
| $\boldsymbol{x} \mapsto \widehat{p}_{1}(\boldsymbol{x})$ | regression model that underfits (we drop the second component of $\boldsymbol{x}$ ) |
| $\boldsymbol{x} \mapsto \widehat{p}_{2}(\boldsymbol{x})$ | optimally estimated regression model |
| $\boldsymbol{x} \mapsto \widehat{p}_{3}(\boldsymbol{x})$ | regression model that overfits to learning data $\mathcal{L}$ |

The null (homogeneous) model $\widehat{p}_{0}(\boldsymbol{x}) \equiv \widehat{p}_{0}$ does not consider any covariates, i.e., under this model we assume that the observations $Y_{1}, Y_{2}, \ldots$ are i.i.d. with a fixed Bernoulli probability $p_{0} \in(0,1)$ which is estimated by $\widehat{p}_{0}$. For the model $\widehat{p}_{1}$ that underfits, we do not consider all covariate components of $\boldsymbol{x}$ that are used in the true regression function $p^{\dagger}$. This leads to underfitting, because certain systematic effects cannot be explained by that model. The functional form of the regression function $\widehat{p}_{2}$ is identical to the true regression function $p^{\dagger}$, but the regression parameters are estimated with maximum likelihood estimation (MLE) from the learning data $\mathcal{L}$. Finally, regression function $\widehat{p}_{3}$ additionally includes a leakage of information through one additional covariate component which is only there on $\mathcal{L}$ but not on $\mathcal{T}$, and which is correlated with the response. That is, we expand $\boldsymbol{x}_{j}$ by an additional covariate component $x_{j, 3}$ that is positively correlated with the response $Y_{j}$ on the learning data $\mathcal{L}$, but this additional component $x_{i, 3}$ is independent with the response $Y_{i}$ on the test data $\mathcal{T}$. This leads to in-sample overfitting because this additional component only carries information on $\mathcal{L}$.
We fit these four models to the learning data $\mathcal{L}$, and we perform model evaluation out-of-sample on the test data $\mathcal{T}$, thus, the regression functions $\widehat{p}_{k}, 0 \leq k \leq 3$, are estimated only on $\mathcal{L}$.
Model estimation on $\mathcal{L}$ and model evaluation on $\mathcal{T}$ is done by considering the (average) Bernoulli deviance loss (which is equivalent to the MLE in this Bernoulli case)

$$
\mathfrak{D}\left(\boldsymbol{Y}, \widehat{p}_{k}\right)=\frac{1}{n} \sum_{i=1}^{n}-2\left[Y_{i} \log \left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)+\left(1-Y_{i}\right) \log \left(1-\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)\right] \geq 0
$$

for data $\left(Y_{i}, \boldsymbol{x}_{i}\right)_{i=1, \ldots, n}$, and using vector notation $\boldsymbol{Y}=\left(Y_{1}, \ldots, Y_{n}\right)$. Thus, we either calculate (2.1) in-sample on $\mathcal{L}$ for model estimation or out-of-sample on $\mathcal{T}$ for model evaluation; see also Section 4.1 in Wüthrich-Merz [47].

[^0]
[^0]:    ${ }^{6}$ (a) If we consider a fixed insurance portfolio of sample size $n$, we interpret $\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{n}$ as the given covariates of the selected insurance policies. (b) If we randomly select an insurance policy from a population, we interpret the covariate $\boldsymbol{x} \sim \mathbb{P}$ as a random vector. We will not use capital letters in this latter case because it will always be clear from the context which interpretation (a) or (b) we are using. Basically, (a) can be seen as an empirical version of (b), where we perform $n$ i.i.d. selections from $\mathbb{P}$.
    ${ }^{7}$ The learning data set is also known as training data set.
    ${ }^{8}$ In particular for model selection, the test data set is also called validation data set.

## Page 10
| model | Bernoulli deviance loss $\mathfrak{D}$ <br> in-sample $\mathcal{L}$ | out-of-sample $\mathcal{T}$ | deviance decomposition on $\mathcal{T}$ <br> MCB | DSC | UNC |
| :-- | :--: | :--: | :--: | :--: | :--: |
| true model $p^{\dagger}$ | 0.7633 | 0.7653 | 0.0058 | 0.1475 | 0.9070 |
| model $\widehat{p}_{0}$ | 0.9130 | 0.9070 | 0 | 0 | 0.9070 |
| model $\widehat{p}_{1}$ | 0.8369 | 0.8380 | 0.0039 | 0.0729 | 0.9070 |
| model $\widehat{p}_{2}$ | 0.7633 | 0.7654 | 0.0058 | 0.1474 | 0.9070 |
| model $\widehat{p}_{3}$ | 0.7171 | 0.8089 | 0.0209 | 0.1190 | 0.9070 |

Table 1: In-sample (on $\mathcal{L}$ ) and out-of-sample (on $\mathcal{T}$ ) Bernoulli deviance losses $\mathfrak{D}\left(\boldsymbol{Y}, \widehat{p}_{k}\right)$ in the binary classification case, and additive score decomposition on $\mathcal{T}$ using the R package reliabilitydiag $[12]$.

Table 1 gives the resulting Bernoulli deviance losses (2.1). Model $\widehat{p}_{2}$ has the smallest out-ofsample deviance loss (on $\mathcal{T}$ ) of 0.7654 (in blue) which is close to the true out-of-sample deviance loss of 0.7653 , and preference should be given to this model w.r.t. an out-of-sample deviance loss model selection. We also observe that model $\widehat{p}_{3}$ in-sample overfits ( 0.7171 ), and in-sample losses are not a sensible tool for model selection (because they are biased).
In addition, we compute the additive score decomposition on the test set in Table 1. Following Dawid [8] and Pohle [37], the Bernoulli deviance (or any consistent scoring function) can be decomposed into miscalibration (MCB), discrimination (DSC), and uncertainty (UNC) as follows

$$
\mathfrak{D}\left(\boldsymbol{Y}, \widehat{p}_{k}\right)=\mathrm{MCB}-\mathrm{DSC}+\mathrm{UNC}
$$

Here, $\mathrm{MCB} \geq 0$ measures the amount of auto-miscalibration, see Section 2.6, DSC $\geq 0$ shows how good a model can use the information contained in itself, whereas UNC $\geq 0$ is the pure randomness of $Y$, also called entropy. We see that UNC is by far the dominating component, followed by DSC. The amount of MCB, on the other hand, is negligible. This is well established by the fact, that the best model $\widehat{p}_{2}$ has the largest DSC while $\widehat{p}_{1}$ has the best MCB.
We give a brief motivation to consider (out-of-sample) deviance losses. Deviance losses are Bregman divergences, see Section 2.3.2 in Wüthrich-Merz [47], and, as such, deviance losses are strictly consistent loss functions for mean estimation, which makes the mean functional elicitable, see Gneiting [23], Chapter 4 in Wüthrich-Merz [47] and Section 5 in Fissler et al. [17]. Strict consistency is introduced more formally in (2.21) below.
This strict consistency property tells us that

$$
p=\underset{q \in(0,1)}{\arg \min } \mathbb{E}[\mathfrak{D}(Y, q)]
$$

for $Y \sim \operatorname{Bernoulli}(p)$. That is, the true default probability $p \in(0,1)$ minimizes the expected deviance loss, which makes it sensible to give preference to the model with the smallest (empirical) out-of-sample deviance loss, as this can be understood as an empirical version of (2.3).

Note that (2.3) considers the homogeneous case, i.e., not involving any covariates. These considerations carry over to the regression case with covariates $\boldsymbol{x}$, because we can study the conditional distribution of $Y$, given $\boldsymbol{x}$.

A second way of assessing models is to study the Kullback-Leibler (KL) divergence. Assume that we have two densities $f$ and $g$ which have the same support.

## Page 11
The KL divergence from density $g$ to density $f$ is given by

$$
D_{\mathrm{KL}}(f \| g)=\int_{\mathbb{R}} \log \left(\frac{f(y)}{g(y)}\right) f(y) d y \geq 0
$$

The KL divergence measures how far $g$ is away from $f$. Note that the KL divergence is not a proper distance function as it is not symmetric and does not fulfill the triangle inequality. Nevertheless, we can use it as a measure of divergence because it is 0 if and only if $f=g$, a.e., ${ }^{9}$ see Lemma 2.21 in Wüthrich-Merz [47]. This motivates to calculate the KL divergences from the estimated models $\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)$ to the true model $p^{\dagger}\left(\boldsymbol{x}_{i}\right), 0 \leq k \leq 3$, which are in the (discrete) Bernoulli case given by

$$
D_{\mathrm{KL}}\left(p^{\dagger}\left(\boldsymbol{x}_{i}\right) \| \widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)=p^{\dagger}\left(\boldsymbol{x}_{i}\right) \log \left(\frac{p^{\dagger}\left(\boldsymbol{x}_{i}\right)}{\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)}\right)+\left(1-p^{\dagger}\left(\boldsymbol{x}_{i}\right)\right) \log \left(\frac{1-p^{\dagger}\left(\boldsymbol{x}_{i}\right)}{1-\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)}\right)
$$

for $1 \leq i \leq n$. Preference is now given to the model that has minimal average KL divergence

$$
\begin{aligned}
\underset{0 \leq k \leq 3}{\arg \min } & \frac{1}{n} \sum_{i=1}^{n} D_{\mathrm{KL}}\left(p^{\dagger}\left(\boldsymbol{x}_{i}\right) \| \widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right) \\
& =\underset{0 \leq k \leq 3}{\arg \min } \frac{1}{n} \sum_{i=1}^{n} p^{\dagger}\left(\boldsymbol{x}_{i}\right) \log \left(\frac{p^{\dagger}\left(\boldsymbol{x}_{i}\right)}{\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)}\right)+\left(1-p^{\dagger}\left(\boldsymbol{x}_{i}\right)\right) \log \left(\frac{1-p^{\dagger}\left(\boldsymbol{x}_{i}\right)}{1-\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)}\right)
\end{aligned}
$$

This provides us with the model $\widehat{p}_{k}$ that is closest to the true model $p^{\dagger}$ in average KL divergence. The latter minimization is equivalent to considering (drop all terms that do not depend on $\widehat{p}_{k}$ )

$$
\underset{0 \leq k \leq 3}{\arg \min } \frac{1}{n} \sum_{i=1}^{n}-\left[p^{\dagger}\left(\boldsymbol{x}_{i}\right) \log \left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)+\left(1-p^{\dagger}\left(\boldsymbol{x}_{i}\right)\right) \log \left(1-\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)\right]
$$

The remaining difficulty is that these latter expressions cannot be calculated because, typically, the true model $p^{\dagger}$ is not known. The natural idea is (again) to replace it by the empirical out-of-sample distribution described by the test data set $\mathcal{T}$. This provides us with

$$
\underset{0 \leq k \leq 3}{\arg \min } \frac{1}{n} \sum_{i=1}^{n}-\left[Y_{i} \log \left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)+\left(1-Y_{i}\right) \log \left(1-\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)\right]
$$

Thus, according to minimizing the empirical KL divergence, we give preference to the model $\widehat{p}_{k}$ that minimizes (2.6), but this is precisely the model that minimizes the Bernoulli deviance loss (2.1). This gives a second motivation for the model preference in Table 1. The function in (2.6) is also called binary cross-entropy or log-loss.

# Remarks 2.1 

- Both the Bernoulli deviance loss (2.1) and the KL divergence (2.6) describe empirical quantities. Under the assumption of having i.i.d. out-of-sample data $\left(Y_{i}, \boldsymbol{x}_{i}\right), 1 \leq i \leq n$, these quantities will converge to the true expected quantities (averaged over the covariate distribution of $\boldsymbol{x}$ ) as the sample size $n \rightarrow \infty$. This is due to the law of large numbers and the Glivenko-Cantelli result $[22,6]$.

[^0]
[^0]:    ${ }^{9}$ a.e. stands for almost everywhere; a.s. stands for almost surely.

## Page 12
- We emphasize that (2.6) is an out-of-sample evaluation, i.e., $\widehat{p}_{k}$ has been estimated on the learning data $\mathcal{L}$, and this $\mathcal{L}$-estimated regression model is then evaluated on the test data $\mathcal{T}$ in (2.6). If we would use the learning data in (2.6) for $\left(Y_{i}\right)_{i}$, we would obtain a biased result, and Akaike's [2] information criterion (AIC) tells us how to (asymptotically) correct for this bias in the case of MLE fitted models.

The above methods solve the problem of model selection from a distributional and MLE point of view. Before performing model selection, we should always check whether the models are properly calibrated. Calibration can be checked with an identification function, and because we estimate means $\mathbb{E}\left[Y_{i}\right]=p^{\dagger}\left(\boldsymbol{x}_{i}\right)$, we should choose the identification function for the mean, we refer to Table 2 in Fissler et al. [17]. Basically, this results in checking in the Bernoulli case for an approximate identity

$$
\frac{1}{n} \sum_{i=1}^{n} \widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)-Y_{i} \approx 0
$$

This is also called the balance property that implies that we have an unbiased model on the portfolio level.

| model | balance property (2.7) <br> in-sample $\mathcal{L}$ | out-of-sample $\mathcal{T}$ | $\widehat{\sigma}_{n}$ |
| :-- | :--: | :--: | :--: |
| true model $p^{\dagger}$ | -0.0008 | 0.0011 | 0.0034 |
| model $\widehat{p}_{0}$ | 0 | 0.0019 | 0.0038 |
| model $\widehat{p}_{1}$ | 0 | 0.0019 | 0.0036 |
| model $\widehat{p}_{2}$ | 0 | 0.0019 | 0.0034 |
| model $\widehat{p}_{3}$ | 0 | 0.0019 | 0.0033 |

Table 2: Balance property (2.7).
From Table 2, we observe that the balance property (2.7) is not identically equal to zero in the true model $p^{\dagger}$ which comes from the simulation noise in $\mathcal{L}$ and $\mathcal{T}$, respectively. This simulation noise can be assessed by the standard deviation (in the true Bernoulli model $p^{\dagger}$ )

$$
\sigma_{n}=\sqrt{\frac{1}{n^{2}} \sum_{i=1}^{n} p^{\dagger}\left(\boldsymbol{x}_{i}\right)\left(1-p^{\dagger}\left(\boldsymbol{x}_{i}\right)\right)}=0.0034
$$

We can estimate this quantity also in the estimated models. However, these are slightly biased in the estimated models, see the last column in Table 2. Out-of-sample on $\mathcal{T}$, approximations (2.7) are smaller than the estimated standard deviations $\widehat{\sigma}_{n}$ (in all models), see Table 2. This supports proper (unconditional) calibration. In-sample on $\mathcal{L}$ we have values exactly equal to zero which comes from the fact that we use logistic generalized linear models (GLMs) with the canonical link, the logit link, for the estimation of $\widehat{p}_{k}$. This provides an exact balance property (2.7), see Wüthrich [45].
${ }^{\text {o }}$ Summary. The models $\widehat{p}_{k}, 0 \leq k \leq 3$, are properly calibrated, which is a statement on the global portfolio level. We give preference to model $\widehat{p}_{2}$ because it minimizes the out-of-sample loss. This latter statement is based on the out-of-sample Bernoulli deviance loss (2.1) and the empirical KL divergence (2.6), respectively.

## Page 13
# 2.2 Lorenz curves of the fitted regression functions 

We study the Lorenz curve (1.7) that is generated by the regression functions $\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)_{1 \leq i \leq n}$ of the four different models $0 \leq k \leq 3$. This alone is not directly useful for model selection, but it expresses the disparity between the different regression models, which will be useful for our further understanding.
In analogy to the empirical distribution (1.6), we study an empirical distribution generated by the regression functions $\widehat{p}_{k}$

$$
y \mapsto \widehat{F}_{n}\left(y ; \widehat{p}_{k}\right)=\frac{1}{n} \sum_{i=1}^{n} \mathbb{1}_{\left\{y \leq \widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right\}}
$$

That is, we consider the empirical distribution of the "data" $\widehat{p}_{k}\left(\boldsymbol{x}_{1}\right), \ldots, \widehat{p}_{k}\left(\boldsymbol{x}_{n}\right)$, under the assumption of having i.i.d. covariates $\boldsymbol{x}_{i} \sim \mathbb{P} . \widehat{F}_{n}\left(\cdot ; \widehat{p}_{k}\right)$ then expresses the empirical distribution of $\widehat{p}_{k}(\boldsymbol{x})$ as a function of the (random) covariate $\boldsymbol{x} \sim \mathbb{P}$, we also refer to Footnote 6 on page 9. This allows us to calculate the empirical Lorenz curve of the regression model $\widehat{p}_{k}$, see also (1.7),

$$
\alpha \in(0,1) \quad \mapsto \quad \widehat{L}_{n}\left(\alpha ; \widehat{p}_{k}\right)=\frac{1}{\frac{1}{n} \sum_{i=1}^{n} \widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)} \frac{1}{n} \sum_{i=1}^{\lceil\alpha n\rceil} \widehat{p}_{k}\left(\boldsymbol{x}_{(i)}\right)
$$

with order statistics $\widehat{p}_{k}\left(\boldsymbol{x}_{(1)}\right) \leq \widehat{p}_{k}\left(\boldsymbol{x}_{(2)}\right) \leq \ldots \leq \widehat{p}_{k}\left(\boldsymbol{x}_{(n)}\right) .{ }^{10}$ Compared to Section 1.2, the only difference is that we replace the observations $Y_{i}$ by the regression estimates $\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)$ and, thus, we do not study disparity in claim sizes but rather the disparity in the regression function. This is highlighted in the notation by adding a second argument to the empirical Lorenz curve $\widehat{L}_{n}\left(\cdot ; \widehat{p}_{k}\right)$.

Figure 4: Lorenz curves $\alpha \mapsto \widehat{L}_{n}\left(\alpha ; \widehat{p}_{k}\right)$ of the fitted regression models $\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)_{1 \leq i \leq n}, 0 \leq k \leq 3$.
The resulting Lorenz curves of the fitted regression models $\widehat{p}_{k}, 0 \leq k \leq 3$, are shown in Figure 4. The null model $\widehat{p}_{0}$ sits on the diagonal (cyan color) because it does not have any disparity, and we observe an ordering of the remaining models according to the in-sample losses given

[^0]
[^0]:    ${ }^{10}$ Remark that the order statistics $\widehat{p}_{k}\left(\boldsymbol{x}_{(1)}\right) \leq \widehat{p}_{k}\left(\boldsymbol{x}_{(2)}\right) \leq \ldots \leq \widehat{p}_{k}\left(\boldsymbol{x}_{(n)}\right)$ orders w.r.t. the regression probabilities $\widehat{p}\left(\boldsymbol{x}_{i}\right)$ and not w.r.t. the (plain) covariates $\boldsymbol{x}_{i}$.
![Page 13 Image 1](cs13_gini_index_and_friends_assets/cs13_gini_index_and_friends_p13_img1.jpg)

## Page 14
in Table 1. Typically, a smaller in-sample loss means that the model follows more closely the observations, which often implies more disparity. The orange Lorenz curve reflects the optimal model $\widehat{p}_{2}$, which is the critical case between under- and overfitting. It also indicates the amount of disparity that we should expect in the true regression function.
Note that Figure 4 only considers the estimated regression functions $\widehat{p}_{k}$, but it does not assess these regression functions (out-of-sample) on observations. Below, we are going to modify these considerations to receive a version of the Gini index as it is often used for model selection in binary classification problems in ML; see, e.g., Section 6.3.7 in Ferrario-Hämmerli [16] and Tasche [43]. This version of the Gini index will also detect in-sample overfitting in our example, we refer to Figure 6, below, where the order of the curves will change compared to Figure 4.
For later purposes we also state the Lorenz curve (not its empirical version) of $\widehat{p}_{k}(\boldsymbol{x})$ with covariates $\boldsymbol{x} \sim \mathbb{P}$, under the assumption that $\widehat{p}_{k}(\boldsymbol{x})$ has a continuous distribution function $F_{\widehat{p}_{k}(\boldsymbol{x})}$. The Lorenz curve is then given by, see also (1.2),

$$
\alpha \in(0,1) \mapsto L_{F_{\widehat{p}_{k}(\boldsymbol{x})}}(\alpha)=\frac{1}{\mathbb{E}\left[\widehat{p}_{k}(\boldsymbol{x})\right]} \mathbb{E}\left[\widehat{p}_{k}(\boldsymbol{x}) \mathbb{1}_{\left\{\widehat{p}_{k}(\boldsymbol{x}) \leq F_{\widehat{p}_{k}(\boldsymbol{x})}^{-1}(\alpha)\right\}}\right]
$$

where $F_{\widehat{p}_{k}(\boldsymbol{x})}^{-1}$ denotes the left-continuous generalized inverse of the distribution function $F_{\widehat{p}_{k}(\boldsymbol{x})}$ of $\widehat{p}_{k}(\boldsymbol{x})$, and we consider the regression function $\widehat{p}_{k}(\boldsymbol{x})$ as a function of the (random) covariates $\boldsymbol{x} \sim \mathbb{P}$ in $(2.10)$.

# 2.3 The Gini index in machine learning for binary classification 

We modify the Lorenz curve of Figure 4 such that it supports us in model selection. In ML, the graph is typically mirrored at the diagonal line. Thus, using an upper index ${ }^{+}$to indicate the mirroring, the empirical Lorenz curve (2.9) is modified to its mirrored counterpart

$$
\begin{aligned}
\alpha \in(0,1) \mapsto \widehat{L}_{n}^{+}\left(\alpha ; \widehat{p}_{k}\right) & =\frac{1}{\frac{1}{n} \sum_{i=1}^{n} \widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)} \frac{1}{n} \sum_{i=[(1-\alpha) n]+1}^{n} \widehat{p}_{k}\left(\boldsymbol{x}_{(i)}\right) \\
& \stackrel{(*)}{=} \frac{1}{\frac{1}{n} \sum_{i=1}^{n} \widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)} \frac{1}{n} \sum_{i=1}^{n} \widehat{p}_{k}\left(\boldsymbol{x}_{i}\right) \mathbb{1}_{\left\{\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)>\widehat{p}_{k}\left(\boldsymbol{x}_{(( }(1-\alpha) n)) \mid\right\}}
\end{aligned}
$$

This results in a Lorenz curve mirrored at the diagonal line in Figure 4. For the identity $\stackrel{(*)}{=}$ to hold, we need to assume that we have a strict ordering $\widehat{p}_{k}\left(\boldsymbol{x}_{(1)}\right)<\widehat{p}_{k}\left(\boldsymbol{x}_{(2)}\right)<\ldots<\widehat{p}_{k}\left(\boldsymbol{x}_{(n)}\right)$, i.e., there are no ties in $\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)_{1 \leq i \leq n}$.
Empirical formula (2.11) is motivated by the following mirrored Lorenz curve

$$
\begin{aligned}
\alpha \in(0,1) \mapsto L_{F_{\widehat{p}_{k}}(\boldsymbol{x})}^{+}(\alpha) & =\frac{1}{\mathbb{E}\left[\widehat{p}_{k}(\boldsymbol{x})\right]} \mathbb{E}\left[\widehat{p}_{k}(\boldsymbol{x}) \mathbb{1}_{\left\{\widehat{p}_{k}(\boldsymbol{x})>F_{\widehat{p}_{k}(\boldsymbol{x})}^{-1}(1-\alpha)\right\}}\right] \\
& =1-\frac{1}{\mathbb{E}\left[\widehat{p}_{k}(\boldsymbol{x})\right]} \mathbb{E}\left[\widehat{p}_{k}(\boldsymbol{x}) \mathbb{1}_{\left\{\widehat{p}_{k}(\boldsymbol{x}) \leq F_{\widehat{p}_{k}(\boldsymbol{x})}^{-1}(1-\alpha)\right\}}\right] \\
& =1-L_{F_{\widehat{p}_{k}(\boldsymbol{x})}}(1-\alpha)
\end{aligned}
$$

see also $(2.10)$.
The general idea now is the following: if the regression function $\boldsymbol{x} \mapsto \widehat{p}_{k}(\boldsymbol{x})$ manages to perfectly separate the responses $Y_{i}=1$ from the responses $Y_{i}=0$ (out-of-sample), then we should first

## Page 15
consider all 1's and afterwards all 0 's of the responses since $1 \geq 1 \geq \ldots \geq 1 \geq 0 \geq \ldots \geq 0$. The mirrored Lorenz curve for this is a straight line with slope $>1,{ }^{11}$ and once it reaches 1 it is constantly equal to 1 , this perfect ordering is illustrated by the orange dotted line in Figure 5 called perfect model. On the other hand, the null model that cannot explain any structure in the observations should still sit on the diagonal line, represented by the blue dotted line in Figure 5. Intuitively, the model $\boldsymbol{x} \mapsto \widehat{p}_{k}(\boldsymbol{x})$ that produces a curve (whose construction still needs to be discussed) that is closest (out-of-sample) to the perfect model is the one that explains the (ordering of the) observations (out-of-sample) best; we also refer to Tasche [43], GourierouxJasiak [25] and Schatz [39].

Figure 5: Cumulative accuracy profile (CAP) given by $\alpha \mapsto \widehat{C}_{n}^{+}\left(\alpha ; \widehat{p}_{k}\right)$; the colors are in line with Figure 1 and also the labels of areas A and B.

For this construction we modify the mirrored empirical Lorenz curve (2.11) as follows

$$
\alpha \in(0,1) \quad \mapsto \quad \widehat{C}_{n}^{+}\left(\alpha ; \widehat{p}_{k}\right)=\frac{1}{\frac{1}{n} \sum_{i=1}^{n} Y_{i}} \frac{1}{n} \sum_{i=1}^{n} Y_{i} \mathbb{1}_{\left\{\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)>\widehat{p}_{k}\left(\boldsymbol{x}_{\left(\lceil(1-\alpha) n\rceil\right)}\right)\right\}}
$$

That is, we aggregate the responses $Y_{i}$ in the ordering of their expectations $\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)$. In the actuarial literature, this object is called (empirical) concentration curve, see Section 3 in Denuit-Trufin [11]. In the ML community and in the financial literature, it is called (empirical) cumulative accuracy profile (CAP), see Section 6.3.7 in Ferrario-Hämmerli [16] and Tasche [43], and it has further names such as gain curve or (cumulative) lift curve, see, e.g., Ling-Li [30].

Function (2.13) provides us with the red CAP in Figure 5. In the case of a perfect joint ordering of $Y_{i}$ and $\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)$, we would get the orange dotted CAP (perfect model), saying that the regression function can perfectly predict the ordering of the out-of-sample claims $\mathcal{T}$; for more discussion we also refer to Remark 2.6 and Section 2.5, below.

Remark 2.2 In the case of a perfect joint ordering of $Y_{i}$ and $\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)$, the orange area B in Figure 5 is zero. Such a perfect ordering can be achieved, e.g., if we manage to perfectly distinguish

[^0]
[^0]:    ${ }^{11}$ The slope is $n / \sum_{i=1}^{n} Y_{i}$, i.e., we have the inverse observed empirical frequency.
![Page 15 Image 1](cs13_gini_index_and_friends_assets/cs13_gini_index_and_friends_p15_img1.jpg)

## Page 16
pictures of cats $\left(Y_{i}=1\right)$ and dogs $\left(Y_{i}=0\right)$. Distinguishing cats from dogs is not a random experiment, but rather a deterministic classification task. In random experiments, i.e., if we sample $Y_{i} \sim \operatorname{Bernoulli}\left(p^{\dagger}\left(\boldsymbol{x}_{i}\right)\right)$, there is always an irreducible risk part because the probability $p^{\dagger}\left(\boldsymbol{x}_{i}\right) \in(0,1)$ cannot fully explain the response $Y_{i} \in\{0,1\}$. Therefore, we do not expect the orange area B to completely vanish in random experiments. On the contrary, if the orange area B on the in-sample data $\mathcal{L}$ is too small, this is a strong evidence of overfitting.
The irreducible risk in the random experiment case can be quantified by the standard deviation

$$
\sigma\left(\boldsymbol{x}_{i}\right)=\sqrt{\operatorname{Var}\left(Y_{i}\right)}=\sqrt{p^{\dagger}\left(\boldsymbol{x}_{i}\right)\left(1-p^{\dagger}\left(\boldsymbol{x}_{i}\right)\right)} \in(0,1 / 2]
$$

In Remark 2.6 below, we come back to the idea of perfect joint ordering, which is closely related to rank correlation and concordance.

The machine learning ML Gini index of classification model $\widehat{p}_{k}$ is then defined by

$$
\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}=\frac{\operatorname{area}(\mathrm{A})}{\operatorname{area}(\mathrm{A}+\mathrm{B})} \leq 1
$$

Note that this differs from the Gini index in economics $G_{F}^{\text {eco }}$, see (1.4), because the area B is smaller in this ML case, compare Figures 1 and 5. Naturally, the maximal disparity is determined by an optimal ordering of the responses in the CAP (2.13). Thus, the average observed out-ofsample default rate determines the slope of the orange dotted line in Figure 5, see Footnote 11 on page 15. This also restricts area B compared to Figure 1, having the effect that the perfect model attains the upper bound in (2.14). As explained in Remark 2.2, such a perfect model is unlikely in the random experiment case because the ordering of the responses $Y_{i}$ and the probabilities $\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)$ typically are not fully in line due to the irreducible risk from sampling.

Figure 6: Out-of-sample CAPs of the fitted models $\widehat{p}_{k}, 0 \leq k \leq 3$; the colors are identical to Figure 4.

Figure 6 gives the resulting CAPs (out-of-sample) with the coloring being identical to the Lorenz curves in Figure 4. We observe that the CAPs can indeed be used for model selection in this example as we receive the same ordering as from the out-of-sample deviance losses given in
![Page 16 Image 1](cs13_gini_index_and_friends_assets/cs13_gini_index_and_friends_p16_img1.jpg)

## Page 17
Table 3. This is to be expected given that the DSC components in Table 1 dominate the MSC components by far. Furthermore, deviance losses try to minimize KL divergences which is a distributional description of the fitted models, whereas ML Gini indices $\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}$ and CAPs rely on positive rank correlations that we try to maximize, see also Remark 2.6, below, for more explanation on rank correlations and concordance.

| model | Bernoulli deviance loss $\mathfrak{D}$ <br> in-sample $\mathcal{L}$ | out-of-sample $\mathcal{T}$ | Gini index <br> $\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}$ |
| :-- | :--: | :--: | :--: |
| true model $p^{\dagger}$ | 0.7633 | 0.7653 | 0.5534 |
| model $\widehat{p}_{0}$ | 0.9130 | 0.9070 | 0.0000 |
| model $\widehat{p}_{1}$ | 0.8369 | 0.8380 | 0.3969 |
| model $\widehat{p}_{2}$ | 0.7633 | 0.7654 | 0.5532 |
| model $\widehat{p}_{3}$ | 0.7171 | 0.8089 | 0.4983 |

Table 3: In-sample and out-of-sample Bernoulli deviance losses $\mathfrak{D}$ (small is good) and (out-ofsample) ML Gini indices $\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}$ (large is good) in the binary classification case.

We emphasize that the CAPs detect overfitting in this example, and the resulting out-of-sample ML Gini indices give $\widehat{G}_{\widehat{p}_{2}}^{\mathrm{ML}}>\widehat{G}_{\widehat{p}_{3}}^{\mathrm{ML}}$, providing the right model choice in this case. This can be seen from Figure 4 and Figure 6 as the order of the red and orange curves changes. Thus, Figure 4 gives the in-sample losses that are prone to overfitting, and the out-of-sample CAPs in Figure 6 correct these in-sample losses for overfitting.

More formally, the ML Gini index (2.14) in the binary classification case can be calculated as follows, see Example 2 in Byrne [5]. Set $n_{1}(\boldsymbol{Y})=\sum_{i=1}^{n} Y_{i}$ and $n_{0}(\boldsymbol{Y})=n-n_{1}(\boldsymbol{Y})$, and assign to each instance $1 \leq i \leq n$ the following rank vector in model $\widehat{p}_{k}$

$$
\rho\left(\hat{p}_{k} ; \boldsymbol{x}_{i}\right)=\sum_{j=1}^{n} \mathbb{1}_{\left\{\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right) \geq \widehat{p}_{k}\left(\boldsymbol{x}_{j}\right)\right\}}-\mathbb{1}_{\left\{\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right) \leq \widehat{p}_{k}\left(\boldsymbol{x}_{j}\right)\right\}}
$$

The ML Gini index in the binary classification case is given by

$$
\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}=\mathbb{1}_{\left\{n_{1}(\boldsymbol{Y}) \notin\{0, n\}\right\}} \sum_{i=1}^{n} \frac{Y_{i}}{n_{0}(\boldsymbol{Y}) n_{1}(\boldsymbol{Y})} \rho\left(\hat{p}_{k} ; \boldsymbol{x}_{i}\right)
$$

Note that this ML Gini index in the binary classification case can only be different from zero if we do not have a degenerate case, that is, $n_{1}(\boldsymbol{Y}) \notin\{0, n\}$. In the degenerate case, we would find an MLE of either 0 or 1 , which does not lead to a sensible stochastic (Bernoulli) model.

# Remarks 2.3 

- Formula (2.15) formally introduces the ML Gini index in the binary classification case. Below, in Section 2.7, we discuss the regression case.
- There is another derivation of the ML Gini index that is specific to the binary classification case, see the next section. This is the reason for considering a binary classification problem to discuss the ML Gini index.

## Page 18
- The reader may wonder why we put a 'hat' on top of $G$ in the ML version of the Gini index (2.14), but not in its economics counterpart (1.4). The reason is that the ML version considers an empirical quantity, whereas the economics one does not. We further elaborate on this in the next two bullet points of this remark.
- Gini index in economics: For regression function $\boldsymbol{x} \mapsto \widehat{p}(\boldsymbol{x})$ we can define the Gini index in economics for the distribution $F_{\widehat{p}(\boldsymbol{x})}$ of $\widehat{p}(\boldsymbol{x})$ by $G_{F_{\widehat{p}(\boldsymbol{x})}^{\text {eco }}}^{\text {eco }}$, see (1.4). This assumes $\boldsymbol{x} \sim \mathbb{P}$. Its empirical counterpart $G_{F_{n}(\cdot ; \widehat{p})}^{\text {eco }}$ is then obtained by replacing the distribution $F_{\widehat{p}(\boldsymbol{x})}$ by the empirical one $\widehat{F}_{n}(\cdot ; \widehat{p})$, see (1.8) and (2.8). Therefore, we do not need a 'hat' on top of $G$ in the economics version, and we have

$$
G_{F_{\widehat{p}(\boldsymbol{x})}}^{\mathrm{eco}}=\frac{1}{2 \mathbb{E}[\widehat{p}(\boldsymbol{x})]} \mathbb{E}\left[\left|\widehat{p}(\boldsymbol{x})-\widehat{p}\left(\boldsymbol{x}^{\prime}\right)\right|\right]
$$

with $\widehat{p}\left(\boldsymbol{x}^{\prime}\right)$ being an independent copy of $\widehat{p}(\boldsymbol{x})$, see (1.5).

- Gini index in ML: Definition (2.15) is a purely empirical one that at the same time uses the estimated probabilities $\widehat{p}\left(\boldsymbol{x}_{i}\right)$ on the (sampled) instances $1 \leq i \leq n$, as well as their responses $Y_{i}$. We can define the (non-empirical) Gini index in ML of regression function $\boldsymbol{x} \mapsto \widehat{p}(\boldsymbol{x})$ as follows

$$
G_{\widehat{p}}^{\mathrm{ML}}=\frac{\int_{0}^{1} C_{Y ; F_{\widehat{p}(\boldsymbol{x})}}^{+}(\alpha) d \alpha-1 / 2}{G_{\widehat{F}_{Y}}^{\mathrm{eco}} / 2}=\frac{\int_{0}^{1} C_{Y ; F_{\widehat{p}(\boldsymbol{x})}}^{+}(\alpha) d \alpha-1 / 2}{\left(1-p^{\dagger}\right) / 2}
$$

with CAP for $\alpha \in(0,1)$, see also (2.13),

$$
C_{Y ; F_{\widehat{p}(\boldsymbol{x})}}^{+} \alpha=\frac{1}{\mathbb{E}[Y]} \mathbb{E}\left[Y \mathbb{1}_{\left\{\widehat{p}(\boldsymbol{x})>F_{\widehat{p}(\boldsymbol{x})}^{-1}(1-\alpha)\right\}}\right]
$$

and with, see (1.5) and (1.9),

$$
G_{F_{Y}}^{\mathrm{eco}}=\frac{1}{2 \mu} \mathbb{E}[|Y-\widetilde{Y}|]=1-p^{\dagger}=\mathbb{P}[Y=0]
$$

with independent random variables $Y, \widetilde{Y} \sim F_{Y}=$ Bernoulli $\left(p^{\dagger}\right)$ having (unconditional) probability $p^{\dagger}=\mathbb{E}\left[p^{\dagger}(\boldsymbol{x})\right]=\mathbb{E}[Y]=\mu \in(0,1)$. The numerator in (2.16) corresponds to area A in Figure 5, and the denominator to the areas of A plus B.

- The non-empirical CAP (2.16) allows for a nice reformulation in the Bernoulli case

$$
\begin{aligned}
C_{Y ; F_{\widehat{p}(\boldsymbol{x})}}^{+} \alpha & =\frac{1}{\mathbb{E}[Y]} \mathbb{E}\left[Y \mathbb{1}_{\left\{\widehat{p}(\boldsymbol{x})>F_{\widehat{p}(\boldsymbol{x})}^{-1}(1-\alpha)\right\}}\right] \\
& =\frac{1}{\mathbb{P}[Y=1]} \mathbb{E}\left[\mathbb{1}_{\left\{Y=1, \widehat{p}(\boldsymbol{x})>F_{\widehat{p}(\boldsymbol{x})}^{-1}(1-\alpha)\right\}}\right] \\
& =\mathbb{P}\left[\widehat{p}(\boldsymbol{x})>F_{\widehat{p}(\boldsymbol{x})}^{-1}(1-\alpha) \mid Y=1\right] \\
& =1-F_{\widehat{p}(\boldsymbol{x}) \mid Y=1}\left(F_{\widehat{p}(\boldsymbol{x})}^{-1}(1-\alpha)\right)
\end{aligned}
$$

This corresponds to formula (5.2) in Tasche [43].

## Page 19
# 2.4 Receiver operating characteristics curve 

Another object that is often considered in binary classification problems is the so-called receiver operating characteristics (ROC) curve. ${ }^{12}$ Assume we have an estimated regression function $\boldsymbol{x} \mapsto \widehat{p}(\boldsymbol{x}) \in(0,1)$. This gives us the estimated probability of observing a response $Y=1$, given covariates $\boldsymbol{x}$, i.e.,

$$
\widehat{\mathbb{E}}[Y]=\widehat{\mathbb{P}}[Y=1]=\widehat{p}(\boldsymbol{x})
$$

For receiving a binary classifier with values in the set $\{0,1\}$, we typically choose a threshold $\tau \in(0,1)$ and we define the predicted class of $Y$ by the indicator

$$
\widehat{Y}=\widehat{Y}_{\tau}=\mathbb{1}_{\{\widehat{p}(\boldsymbol{x}) \geq \tau\}}
$$

Naturally, this binary classifier depends on the choice of the threshold $\tau$. In view of our simulated example from above, this allows us to construct the confusion matrix on the test data $\mathcal{T}$ that analyzes correct and wrong predictions in terms of true positive (TP), true negative (TN), false positive (FP) and false negative (FN) counts, the latter two being related to Type I and II errors in statistics.

|  |  | predicted |  |
| :-- | :--: | :--: | :--: |
|  |  | $\widehat{Y}=1$ | $\widehat{Y}=0$ |
| actually | $Y=1$ | TP | FN |
| observed | $Y=0$ | FP | TN |


|  |  | predicted |  |
| :-- | :--: | :--: | :--: |
|  |  | $\widehat{Y}=1$ | $\widehat{Y}=0$ |
| actually | $Y=1$ | 474 | 1 '211 |
| observed | $Y=0$ | 494 | 7'821 |

Table 4: Confusion matrix of model $\widehat{p}_{2}$ on the test data $\mathcal{T}$ for the choice $\tau=40 \%$.
Using the confusion matrix of Table 4, we can calculate the true positive rate (TPR) and the false positive rate (FPR) given by

$$
\begin{aligned}
& \operatorname{TPR}(\tau)=\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FN}}=\frac{474}{474+1^{\prime} 211}=28 \%, \\
& \operatorname{FPR}(\tau)=\frac{\mathrm{FP}}{\mathrm{FP}+\mathrm{TN}}=\frac{494}{494+7^{\prime} 821}=6 \%
\end{aligned}
$$

The ROC curve is obtained by plotting the TPR against the FPR for $\tau \in(0,1)$

$$
(\operatorname{FPR}(\tau), \operatorname{TPR}(\tau)) \in[0,1]^{2}
$$

The ROC curve of model $\widehat{p}_{2}$ on the test data $\mathcal{T}$ is illustrated in Figure 7. We emphasize that the ROC curve and the CAP in Figure 3 are different. ${ }^{13}$ In a next step, one calculates the so-called area under the curve (AUC), indicated in Figure 7 by the orange color. Table 5 gives the corresponding AUCs.

[^0]
[^0]:    ${ }^{12}$ The ROC was introduced by the US army in 1941 (during World War II) for the analysis of radar signals, this also explains the origin of the name ROC.
    ${ }^{13}$ Similarly to (2.18), we can describe the ROC curve by the function $\alpha \mapsto 1-F_{\widehat{p}(\boldsymbol{x}) \mid Y=1}\left(F_{\widehat{p}(\boldsymbol{x}) \mid Y=0}^{-1}(1-\alpha)\right)$, see formula (5.6a) of Tasche [43]. This highlights the difference between the CAP and the ROC curve.

## Page 20
Figure 7: The ROC curve and the AUC of model $\widehat{p}_{2}$ on the test data $\mathcal{T}$.

| model | Bernoulli deviance loss $\mathfrak{D}$ <br> in-sample $\mathcal{L}$ | Gini index <br> out-of-sample $\mathcal{T}$ | $\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}$ | $\frac{\text { ROC curve }}{\widehat{\mathrm{AUC}}_{\widehat{p}_{k}}}$ |
| :-- | :--: | :--: | :--: | :--: |
| true model $p^{\dagger}$ | 0.7633 | 0.7653 | 0.5534 | 0.7767 |
| model $\widehat{p}_{0}$ | 0.9130 | 0.9070 | 0.0000 | 0.5000 |
| model $\widehat{p}_{1}$ | 0.8369 | 0.8380 | 0.3969 | 0.6984 |
| model $\widehat{p}_{2}$ | 0.7633 | 0.7654 | 0.5532 | 0.7766 |
| model $\widehat{p}_{3}$ | 0.7171 | 0.8089 | 0.4983 | 0.7491 |

Table 5: In-sample and out-of-sample Bernoulli deviance losses $\mathfrak{D}$ (small is good), (out-ofsample) ML Gini indices $\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}$ (large is good), and $\widehat{\mathrm{AUC}}_{\widehat{p}_{k}}$ (large is good) in the binary classification case.

The crucial result is that this AUC is directly related to the ML Gini index (in binary classification models) by

$$
\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}=2 \widehat{\mathrm{AUC}}_{\widehat{p}_{k}}-1
$$

Thus, in the binary classification case we have two different ways of computing the Gini indices of Table 5 and, obviously, they provide the same rankings of the models.

Remarks 2.4 Statement (2.19) can be proved, see Engelmann et al. [14] and Tasche [43], and thus, there are two different ways of calculating the ML Gini index $\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}$. However, in practice, this requires some care because $\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}$ and $\widehat{\mathrm{AUC}}_{\widehat{p}_{k}}$ are only given in the discrete points of the observations, and the interpolation of these discrete points can be done either by straight lines (giving trapezoids) or by step functions. These will give small numerical differences that vanish as the sample size $n \rightarrow \infty$. Moreover, the situation where $\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)$ cannot be strictly ordered (due to multiple occurrences of the same values, called ties) also needs special care.
![Page 20 Image 1](cs13_gini_index_and_friends_assets/cs13_gini_index_and_friends_p20_img1.jpg)

## Page 21
In view of (2.19) and (2.15) we have the formula for the AUC of model $\widehat{p}_{k}$

$$
\widehat{\operatorname{AUC}}_{\widehat{p}_{k}}=\frac{1}{2}+\mathbb{1}_{\left\{n_{1}(\boldsymbol{Y}) \notin\{0, n\}\right\}} \frac{1}{2} \sum_{i=1}^{n} \frac{Y_{i}}{n_{0}(\boldsymbol{Y}) n_{1}(\boldsymbol{Y})} \rho\left(\widehat{p}_{k} ; \boldsymbol{x}_{i}\right)
$$

Remark 2.5 (Wilcoxon-Mann-Whitney's $U$ ) The Wilcoxon-Mann-Whitney $U$-test compares the ranks of two different populations. In our case this $U$-test can be applied to the regression probabilities $\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)_{1 \leq i \leq n}$ and the binary response vector $\boldsymbol{Y}=\left(Y_{1}, \ldots, Y_{n}\right)$. The $U$-statistics in this binary case is defined by

$$
U\left(\boldsymbol{Y}, \widehat{p}_{k}\right)=\sum_{i: Y_{i}=0} \sum_{j: Y_{j}=1} \mathbb{1}_{\left\{\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)<\widehat{p}_{k}\left(\boldsymbol{x}_{j}\right)\right\}}+\frac{1}{2} \mathbb{1}_{\left\{\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)=\widehat{p}_{k}\left(\boldsymbol{x}_{j}\right)\right\}}
$$

It can be shown, see Hanley-McNeil [26] and Example 2 in Byrne [5], that this $U$-statistics is equivalent to the AUC up to scaling, i.e.,

$$
U\left(\boldsymbol{Y}, \widehat{p}_{k}\right)=n_{0}(\boldsymbol{Y}) n_{1}(\boldsymbol{Y}) \widehat{\operatorname{AUC}}_{\widehat{p}_{k}}
$$

Thus, the ML Gini index $\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}$, the $\widehat{\mathrm{AUC}}_{\widehat{p}_{k}}$ from the ROC curve and the Wilcoxon-MannWhitney $U$-statistics $U\left(\boldsymbol{Y}, \widehat{p}_{k}\right)$ all describe the same quantity (up to scaling) in the binary classification case.

Remark 2.6 (Kendall's $\tau$ and Somers' $D$ ) In Remark 2.2 we have mentioned a perfect joint ordering of the responses $Y_{i}$ and the probabilities $\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right), 1 \leq i \leq n$. Mathematically speaking, such a perfect joint ordering considers rank correlations and the notion of concordance. Two pairs $\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right), Y_{i}\right)$ and $\left(\widehat{p}_{k}\left(\boldsymbol{x}_{j}\right), Y_{j}\right)$ are called concordant if

$$
\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)<\widehat{p}_{k}\left(\boldsymbol{x}_{j}\right) \text { and } Y_{i}<Y_{j}\right) \quad \text { or } \quad\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)>\widehat{p}_{k}\left(\boldsymbol{x}_{j}\right) \text { and } Y_{i}>Y_{j}\right)
$$

Two pairs $\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right), Y_{i}\right)$ and $\left(\widehat{p}_{k}\left(\boldsymbol{x}_{j}\right), Y_{j}\right)$ are called discordant if

$$
\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)<\widehat{p}_{k}\left(\boldsymbol{x}_{j}\right) \text { and } Y_{i}>Y_{j}\right) \quad \text { or } \quad\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)>\widehat{p}_{k}\left(\boldsymbol{x}_{j}\right) \text { and } Y_{i}<Y_{j}\right)
$$

Note that the definitions of concordant and discordant use strict inequalities. If we have an identity in one of the components (due to ties), then the corresponding pair is neither concordant nor discordant. Remark that these definitions apply to general real-valued random variables $Y_{i}$. Kendall's $\tau$ is a rank correlation measure that quantifies concordance

$$
\tau\left(\boldsymbol{Y}, \widehat{p}_{k}\right)=\frac{2}{n(n-1)}\left(n_{C}-n_{D}\right)
$$

where $n_{C}$ is the number of concordant pairs and $n_{D}$ the number of discordant pairs in our sample $\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right), Y_{i}\right)_{1 \leq i \leq n}$ of size $n$. Somers' $D[42]$ of $\boldsymbol{Y}$ w.r.t. $\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)_{1 \leq i \leq n}$ is defined by the ratio

$$
D_{\boldsymbol{Y}, \widehat{p}_{k}}=\frac{\tau\left(\boldsymbol{Y}, \widehat{p}_{k}\right)}{\tau(\boldsymbol{Y}, \boldsymbol{Y})}
$$

Somers' $D$ turns the symmetric Kendall's $\tau$ into an asymmetric measure for rank correlation, and the denominator in Somers' $D$ is equal to $n$ if we do not have any ties in the responses $\boldsymbol{Y}$, in

## Page 22
particular, for general real-valued random variables $Y_{i}$ with a continuous distribution. Somers' $D$ and Kendall's $\tau$ are also used to generalize the $R^{2}$-statistics, see, e.g., Harrell [27].
For our binary responses $\boldsymbol{Y}$, Somers' $D$ and the ML Gini index are equal, see Newson [35],

$$
\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}=D_{\boldsymbol{Y}, \widehat{p}_{k}} \quad \text { and } \quad \widehat{\mathrm{AUC}}_{\widehat{p}_{k}}=\frac{1}{2}+\frac{1}{2} D_{\boldsymbol{Y}, \widehat{p}_{k}}
$$

This essentially expresses that the ML Gini index and the AUC are measures of rank correlation, and if two different regression functions $\widehat{p}_{k}$ and $\widehat{p}_{l}$ have the same ordering (regardless of their absolute values), we receive the same ML Gini indices $\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}=\widehat{G}_{\widehat{p}_{l}}^{\mathrm{ML}}$, we also refer to Example 2.9 below. This indicates that the 'perfect model' in Figure 5 is only perfect w.r.t. to the ordering of the observations (concordance), but it does not say anything about (auto-)calibration.

Summary. The ML Gini index $\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}$, the $\widehat{\mathrm{AUC}}_{\widehat{p}_{k}}$ from the ROC curve, the Wilcoxon-Mann-Whitney $U$-statistics $U\left(\boldsymbol{Y}, \widehat{p}_{k}\right)$ and Somers' $D_{\boldsymbol{Y}, \widehat{p}_{k}}$ all describe the same quantity (up to scaling) in the binary classification case. These measures are based on rank correlations and concordance between the regression function $\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)_{1 \leq i \leq n}$ and the responses $\boldsymbol{Y}$. The higher Kendall's $\tau$ between these two vectors the bigger the corresponding ML Gini score, saying that the ordering in the regression function $\left(\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)\right)_{1 \leq i \leq n}$ and the responses $\boldsymbol{Y}$ align. Of course, this scoring should be done out-of-sample on $\mathcal{T}$.

# 2.5 A critical discussion of the ML Gini index for model selection 

Typically, model selection is done by maximizing a score. However, this paradigm only makes sense if the true data generating model maximizes this score. This is exactly the motivation to introduce the notion of strict consistency.
Assume $T: \mathcal{F} \rightarrow \mathbb{A}$ is a functional that maps from a family of distribution functions $\mathcal{F}$ to some action space $\mathbb{A} .{ }^{14}$ For our purposes it is sufficient to assume that $\mathcal{F}$ only contains distributions of $n$-dimensional random vectors with binary components, and we denote by $\mathcal{Y}=\{0,1\}^{n}$ the response space of these binary observation vectors $\boldsymbol{Y}=\left(Y_{1}, \ldots, Y_{n}\right) \sim F \in \mathcal{F}$.
A scoring function $s: \mathcal{Y} \times \mathbb{A}$ is called consistent for $T$ on $\mathcal{F}$ if

$$
\mathbb{E}[s(\boldsymbol{Y}, T(F))] \geq \mathbb{E}[s(\boldsymbol{Y}, T(H))]
$$

for all $\boldsymbol{Y} \sim F \in \mathcal{F}$ and $H \in \mathcal{F}$. It is strictly consistent if equality holds if and only if $F=H$.
In definition (2.21) of consistency, we have that "larger is better". We use this sign convention because, typically, a larger (out-of-sample) Gini index is better. However, one could also use the opposite sign convention "smaller is better". This is the sign convention used for the deviance loss (2.3) and for the KL divergence (2.4). In this second sign convention, we rather call the scoring function a loss function that we try to minimize.
We also note that for binary classification, the notions of scoring function and scoring rule coincide as the mean equals the probability (distribution) $p=\mathbb{E}[Y]$; see Gneiting-Raftery [24]. Propriety of a scoring rule is the equivalent of consistency of a scoring function.

[^0]
[^0]:    ${ }^{14}$ The action space $\mathbb{A}$ is a formal set in which potential decisions (actions) lie. In our example, the action space $\mathbb{A}$ is a space that contains the estimated probabilities (as these are the decisions (choices) that we make).

## Page 23
The existence of a strictly consistent scoring function for $T$ on $\mathcal{F}$ implies that this functional $T$ is elicitable on $\mathcal{F}$. This means that the functional $T$ can be estimated by

$$
T(F)=\underset{a \in \mathbb{A}}{\arg \max } \mathbb{E}[s(\boldsymbol{Y}, a)]
$$

This also implies that we can perform strictly proper model selection, see Gneiting [23] and Gneiting-Raftery [24]. Note that elicitability and consistency (2.21) is not restricted to binary random vectors.
For the sign-flipped version of a loss function $L: \mathcal{Y} \times \mathbb{A}$, strict consistency for $T$ on $\mathcal{F}$ implies, see also $(2.3)$,

$$
T(F)=\underset{a \in \mathbb{A}}{\arg \min } \mathbb{E}[L(\boldsymbol{Y}, a)]=\underset{a \in \mathbb{A}}{\arg \max } \mathbb{E}[-L(\boldsymbol{Y}, a)]
$$

Optimization problem (2.3) provides an example, saying that the true default probability $p$ is the argument that minimizes the expected deviance loss.
Having multiple i.i.d. data $\boldsymbol{Y}_{i}$ with the same distribution as $\boldsymbol{Y} \sim F \in \mathcal{F}$, we can empirically estimate this (elicitable) functional $T$ on $\mathcal{F}$ by

$$
\widehat{T}(F)=\underset{a \in \mathbb{A}}{\arg \max } \frac{1}{n} \sum_{i=1}^{n} s\left(\boldsymbol{Y}_{i}, a\right)
$$

This provides us with an estimate of $T(F)$, even if the true underlying distribution function $F$ from which the data $\left(\boldsymbol{Y}_{i}\right)_{1 \leq i \leq n}$ has been generated, is unknown. The most common example is MLE with the log-likelihood choice for the scoring function. More generally, (2.22) relates to M-estimation for scoring functions $s$.

We are going to analyze the ML Gini index from the viewpoint of consistency. We consider Example 3 of Byrne [5].

Example 2.7 (non-consistency of the ML Gini index, Byrne [5]) We consider the following (true) distribution for the binary vector $\boldsymbol{Y}=\left(Y_{1}, \ldots, Y_{4}\right) \sim F$ :

$$
\mathbb{P}[\boldsymbol{Y}=(1,1,0,0)]=1 / 2, \quad \mathbb{P}[\boldsymbol{Y}=(0,0,1,0)]=7 / 16, \quad \mathbb{P}[\boldsymbol{Y}=(0,0,0,1)]=1 / 16
$$

That is, $\boldsymbol{Y}$ only takes three different values and the components of $\boldsymbol{Y}$ are dependent. Denote by $\mathcal{F}$ the set of all distributions on the binary vectors in $\mathcal{Y}=\{0,1\}^{4}$. We then consider the functional $T: \mathcal{F} \rightarrow \mathbb{A}:=[0,1]^{4}$ that assigns the expected value to each component of the binary vectors. That is, $T$ is the mean functional on $\mathcal{F}$. For our example (2.23) we have (true) mean

$$
F \mapsto p^{\dagger}:=T(F)=\mathbb{E}[\boldsymbol{Y}]=\left(\frac{1}{2}, \frac{1}{2}, \frac{7}{16}, \frac{1}{16}\right) \in[0,1]^{4}
$$

The goal is to reconstruct this mean functional using the Gini index. Choose some distribution $H \in \mathcal{F}$ with mean vector $T(H)=q=\left(q_{1}, \ldots, q_{4}\right) \in[0,1]^{4}$. We choose scoring function $s(\boldsymbol{Y}, T(H))=\widehat{G}_{T(H)}^{\mathrm{ML}}=\widehat{G}_{q}^{\mathrm{ML}}$ with $\boldsymbol{Y} \sim F$. We have, see (2.15),

$$
\begin{aligned}
\mathbb{E}[s(\boldsymbol{Y}, T(H))]=\mathbb{E}\left[\widehat{G}_{q}^{\mathrm{ML}}\right] & =\mathbb{E}\left[\mathbb{1}_{\left\{n_{1}(\boldsymbol{Y}) \notin\{0, n\}\right\}} \sum_{i=1}^{n} \frac{Y_{i}}{n_{0}(\boldsymbol{Y}) n_{1}(\boldsymbol{Y})} \rho(q ; i)\right] \\
& =\sum_{i=1}^{n} \mathbb{E}\left[\frac{Y_{i}}{n_{0}(\boldsymbol{Y}) n_{1}(\boldsymbol{Y})}\right] \rho(q ; i)
\end{aligned}
$$

## Page 24
for $n=4$, and with rank vector

$$
\rho(q ; i)=\sum_{j=1}^{n} \mathbb{1}_{\left\{q_{i} \geq q_{j}\right\}}-\mathbb{1}_{\left\{q_{i} \leq q_{j}\right\}}
$$

Under model assumptions (2.23), i.e., distribution $F$, the above expectations are given by

$$
\widetilde{p}:=\mathbb{E}\left[\frac{\boldsymbol{Y}}{n_{0}(\boldsymbol{Y}) n_{1}(\boldsymbol{Y})}\right]=\left(\frac{1}{8}, \frac{1}{8}, \frac{7}{48}, \frac{1}{48}\right) \in[0,1]^{4}
$$

Choose a distribution $H \in \mathcal{F}$ with $T(H)=q=\widetilde{p}$. The rank vectors of $p^{\dagger}=T(F)$ and $q=\widetilde{p}$ are given by

$$
\rho\left(p^{\dagger}\right)=\rho\left(p^{\dagger} ; \cdot\right)=(2,2,-1,-3) \quad \text { and } \quad \rho(q)=\rho(q ; \cdot)=(0,0,3,-3)
$$

This allows us to calculate the expectation of the empirical ML Gini indices for $\boldsymbol{Y} \sim F$ and $T(H)=q=\widetilde{p}$

$$
\mathbb{E}[s(\boldsymbol{Y}, T(F))]=\mathbb{E}\left[\widehat{G}_{p^{\dagger}}^{\mathrm{ML}}\right]=\rho\left(p^{\dagger}\right) \widetilde{p}^{\top}=\frac{7}{24}<\frac{9}{24}=\mathbb{E}[s(\boldsymbol{Y}, T(H))]=\mathbb{E}\left[\widehat{G}_{q}^{\mathrm{ML}}\right]=\rho(q) \widetilde{p}^{\top}
$$

This implies that the empirical ML Gini index is not a consistent scoring function for the mean functional on this class $\mathcal{F}$ of distribution functions on $\mathcal{Y}=\{0,1\}^{4}$. In particular, by maximizing the expected empirical ML Gini index, we do not find the true mean (2.24) in model (2.23).

Conclusion. Example 2.7 shows that, in general, the empirical ML Gini index $\widehat{G}_{\widetilde{p}}^{\mathrm{ML}}$ is not a consistent scoring function for mean estimation. As a result, we may make wrong decisions by simply choosing the model $\widetilde{p}$ that maximizes this expected ML Gini index. The main problem arises from the normalization $n_{0}(\boldsymbol{Y}) n_{1}(\boldsymbol{Y})$ in (2.15) which may change the ranking of the corresponding components (i.e., we lose concordance between $p^{\dagger}$ and $\widetilde{p}$ in the previous example). The same applies to the AUC of the ROC curve.

Remark 2.8 Example 2.7 is a disappointing result for a general use of the ML Gini index $\widehat{G}_{\widetilde{p}}^{\mathrm{ML}}$ for model selection through mean estimation. If we reduce the family $\mathcal{F}$ of potential distributions on $\{0,1\}^{n}$ we can make the ML Gini index a consistent scoring function. Theorems 6 and 7 of Byrne [5] prove the following two results (for the detailed assumptions we refer to that reference): (1) If the total number of positive outcomes $n_{1}(\boldsymbol{Y})$ is constant, a.s., for all $F \in \mathcal{F}^{\prime} \subset \mathcal{F}$, then the ML Gini index is strictly consistent on $\mathcal{F}^{\prime}$. (2) If the components of $\boldsymbol{Y} \sim F$ are independent for all $F \in \mathcal{F}^{\prime} \subset \mathcal{F}$, then the ML Gini index is strictly consistent on $\mathcal{F}^{\prime}$.
Moreover, note that the use of the ML Gini index in Example 2.7 is slightly different from our use. In particular, in Example 2.7, we have dependence between the components of $\boldsymbol{Y}$, see (2.23). This is not the case in our examples as we assume i.i.d. observations $\left(Y_{i}, \boldsymbol{X}_{i}\right)$. In this latter case, one can prove that the expected empirical ML Gini index is directly related to the (non-empirical) ML Gini index, see Lemma 2 of Agarwal et al. [1] and Theorem 3 in Byrne [5]. This latter situation is going to be studied in detail in Section 2.6, below. In particular, the ML Gini index on auto-calibrated regression functions will provide a strictly consistent scoring function.

## Page 25
Example 2.9 (only ranks matter in the ML Gini index, non-empirical example) The major drawback of the ML Gini index $\widehat{G}_{p_{k}}^{\mathrm{ML}}$ is that it only considers rank correlations. Consider the regression functions:

| instance $i$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | Gini <br> $\widehat{G}_{p_{k}}^{\mathrm{ML}}$ |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| model $p_{1}\left(\boldsymbol{x}_{i}\right)$ | 0.46 | 0.47 | 0.48 | 0.49 | 0.50 | 0.51 | 0.52 | 0.53 | 0.54 | $g$ |
| model $p_{2}\left(\boldsymbol{x}_{i}\right)$ | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | $g$ |
| model $p_{3}\left(\boldsymbol{x}_{i}\right)$ | 0.86 | 0.87 | 0.88 | 0.89 | 0.90 | 0.91 | 0.92 | 0.93 | 0.94 | $g$ |

These three regression functions will provide the same ML Gini index $\widehat{G}_{p_{k}}^{\mathrm{ML}} \equiv g$ on (identical) test data $\mathcal{T}$ because their ordering is identical. However, the resulting classification models are very different, the first one $\left(p_{1}\right)$ being very concentrated around 0.5 , the second one $\left(p_{2}\right)$ being dispersed around 0.5 , and the third one $\left(p_{3}\right)$ having a bias compared to the first one. Remark that in the first two models, the average default rate is 0.5 , i.e., we have an identical balance property (2.7), only the dispersion is different. The last model has a balance property of 0.9 . These three models will be ranked equally by the ML Gini index $\widehat{G}_{p_{k}}^{\mathrm{ML}} \equiv g$. We could also construct skewed examples with the same conclusion.

Example 2.10 (only ranks matter in the ML Gini index, empirical example) Another interesting example is the following:

|  |  |  |  |  |  |  |  |  |  | deviance <br> loss $\mathfrak{D}$ | Gini <br> $\widehat{G}_{p_{k}}^{\mathrm{ML}}$ | KL to <br> $p^{\dagger}\left(\boldsymbol{x}_{i}\right)$ |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| instance $i$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |  |  |  |
| model $p^{\dagger}\left(\boldsymbol{x}_{i}\right)$ | 0.01 | 0.02 | 0.03 | 0.04 | 0.05 | 0.86 | 0.87 | 0.88 | 0.89 | 1.21 | 0.9 | 0 |
| data $Y_{i}$ | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 |  |  |  |
| model $\widehat{p}_{1}\left(\boldsymbol{x}_{i}\right)$ | 0.01 | 0.02 | 0.03 | 0.05 | 0.04 | 0.86 | 0.87 | 0.88 | 0.89 | 1.26 | 0.8 | 0.002 |
| model $\widehat{p}_{2}\left(\boldsymbol{x}_{i}\right)$ | 0.91 | 0.92 | 0.93 | 0.94 | 0.95 | 0.96 | 0.97 | 0.98 | 0.99 | 3.05 | 0.9 | 12.81 |

According to the ML Gini index $\widehat{G}_{p_{k}}^{\mathrm{ML}}$ we give preference (large is good) to the second model $\widehat{p}_{2}$ because it has the same ML Gini index of 0.9 as the true model $p^{\dagger}$, which is bigger than the one of model $\widehat{p}_{1}$. This is implied by the fact that the two models $\widehat{p}_{2}$ and $p^{\dagger}$ have the same ranking. However, the estimated probabilities in $\widehat{p}_{2}$ are completely misspecified in this second estimated model, and nobody would seriously consider the second model $\widehat{p}_{2}$ as being a good model.
In terms of Bernoulli deviance losses $\mathfrak{D}$ we give clear preference (small is good) to the first estimated model $\widehat{p}_{1}$. In fact, we have an almost perfect first model, only the probabilities $\widehat{p}_{1}\left(\boldsymbol{x}_{4}\right)=0.05$ and $\widehat{p}_{1}\left(\boldsymbol{x}_{5}\right)=0.04$ are slightly imprecise (and this swaps the order statistics), but apart from that we have an excellent model $\widehat{p}_{1}$. The KL divergence (2.5) from model $\widehat{p}_{1}$ to model $p^{\dagger}$ is 0.002 , and the KL divergence from model $\widehat{p}_{2}$ to model $p^{\dagger}$ is 12.81 . This says that the first two models are rather similar (close in KL divergence), and the last model is rather different. ${ }^{15}$

Conclusion. Examples 2.9 and 2.10 illustrate that focusing on rank correlations is not sufficient for model selection. Ranks neither consider whether the models are properly calibrated

[^0]
[^0]:    ${ }^{15}$ Note that these are finite sample (empirical) statements, therefore, these have to be considered with a reservation because consistency $(2.21)$ is a statement on the expected value level.

## Page 26
(through an identification function) nor do ranks specify any dispersion or skewness property of the resulting regression function. In view of these examples, there is no support for using the ML Gini index $\widehat{G}_{p}^{\mathrm{ML}}$ and the AUC as a model selection tool.

# 2.6 Auto-calibration 

The results of the previous section are disappointing because they basically say that we should not use the ML Gini index $\widehat{G}_{p}^{\mathrm{ML}}$ for model selection. The missing piece of the puzzle is that the ML Gini index is not a calibration-sensitive measure as it is based on rank correlations, see Remark 2.6 on Kendall's $\tau$ and Somers' $D$. We therefore consider the important property of auto-calibration; see Krüger-Ziegel [29]. ${ }^{16}$ In this section we understand the covariate $\boldsymbol{x}$ as a random vector with covariate distribution $\boldsymbol{x} \sim \mathbb{P}$, see also Footnote 6 on page 9.
Definition 2.11 (auto-calibration) We call a predictor $\boldsymbol{x} \mapsto \widehat{p}(\boldsymbol{x})$ auto-calibrated for $Y$ if, a.s.,

$$
\widehat{p}(\boldsymbol{x})=\mathbb{E}[Y \mid \widehat{p}(\boldsymbol{x})]
$$

The auto-calibration property (2.25) will rule out at least two of the three models in Example 2.9, because their auto-calibration behavior differs, and the same applies to Example 2.10. Note that for an auto-calibrated model $\widehat{p}(\boldsymbol{x})$, the auto-miscalibration component MCB in (2.2) is 0 .

We consider auto-calibration to be a crucial requirement that predictors in insurance (pricing) should satisfy. Basically, it says that the cohort of insurance policies that is charged an identical price $\widehat{p}(\boldsymbol{x})$ is on average self-financing because this price exactly covers the expected claim $Y$ on that cohort (with that price $\widehat{p}(\boldsymbol{x})$ ). Remark that this does not tell us anything about the formation of these self-financing price cohorts and, in general, there are different systems of price cohorts that fulfill the auto-calibration property. E.g., the true model $p^{\dagger}(\boldsymbol{x})=\mathbb{E}[Y \mid \boldsymbol{x}]^{17}$ satisfies auto-calibration, apply the tower property to the $\sigma$-algebras $\sigma\left(p^{\dagger}(\boldsymbol{x})\right) \subset \sigma(\boldsymbol{x})$,

$$
\mathbb{E}\left[Y \mid p^{\dagger}(\boldsymbol{x})\right]=\mathbb{E}\left[\mathbb{E}[Y \mid \boldsymbol{x}] \mid p^{\dagger}(\boldsymbol{x})\right]=\mathbb{E}\left[p^{\dagger}(\boldsymbol{x}) \mid p^{\dagger}(\boldsymbol{x})\right]=p^{\dagger}(\boldsymbol{x})
$$

but also the homogeneous (null) model $p_{0}=\mathbb{E}[Y]$ satisfies the auto-calibration property

$$
\mathbb{E}\left[Y \mid p_{0}\right]=\mathbb{E}[Y]=p_{0}
$$

In this latter null model case we have only one price cohort because we charge the identical price $p_{0}$ to all insurance policies. In view of (2.26) and (2.27), there are arbitrarily many models in between the true model $p^{\dagger}(\boldsymbol{x})$ and the null model $p_{0}$, and these can be obtained by conditioning on part of the information $\sigma(\boldsymbol{x})$.
Since building self-financing homogeneous risk pools (price cohorts) is at the very heart of insurance tariffication, we subsequently require auto-calibration for $Y$ in general. This also implies that we do not have any systematic cross-financing between the price cohorts. If we

[^0]
[^0]:    ${ }^{16}$ An early version of auto-calibration in a binary classification context has been introduced by Schervish [40], but in that reference it has been called well-calibrated, see Section 2 of Schervish [40].
    ${ }^{17}$ In contrast to the previous sections, we now explicitly write the conditioning on $\boldsymbol{x}$ in $\mathbb{E}[Y \mid \boldsymbol{x}]$ to indicate that the response $Y$ belongs to covariate $\boldsymbol{x}$, which is then understood as a conditional distribution of response $Y$, given covariate $\boldsymbol{x}$.

## Page 27
have a general regression function $\boldsymbol{x} \mapsto \widehat{p}(\boldsymbol{x})$ we can always restore the auto-calibration property by setting

$$
\boldsymbol{x} \mapsto \widehat{p}^{(\text {auto })}(\boldsymbol{x}):=\mathbb{E}[Y \mid \widehat{p}(\boldsymbol{x})]
$$

Proposition 4.6 of Wüthrich [46] proves that $\widehat{p}^{(\text {auto })}(\cdot)$ is auto-calibrated for $Y$ (using the tower property).

Remark 2.12 (2-step estimation procedure) The restoration of the auto-calibration property through (2.28) has motivated the 2 -step estimation procedure promoted in Menon et al. [34] and in Section 5.3 of Tasche [44]. A first regression step has to get the correct rankings $\widehat{p}(\boldsymbol{x})$ over all covariates $\boldsymbol{x}$. The second regression step then uses an isotonic regression that lifts these ranks to the right level, basically using the auto-calibration step (2.28). An isotonic regression leads to a monotonically increasing regression function in $\widehat{p}(\boldsymbol{x})$ by imposing the corresponding restriction, see Barlow-Brunk [4], Dimitriadis et al. [12] and Zadrozny-Elkan [49].

Assume we have a family of auto-calibrated predictors $\boldsymbol{x} \mapsto \widehat{p}_{k}(\boldsymbol{x}), k \in \mathcal{K}$, for $Y$. From an auto-calibration point of view, these models are equivalent, and they all provide unbiasedness on portfolio level which we consider to be a minimal requirement that insurance prices should fulfill,

$$
\mathbb{E}\left[\widehat{p}_{k}(\boldsymbol{x})\right]=\mathbb{E}\left[\mathbb{E}\left[Y \mid \widehat{p}_{k}(\boldsymbol{x})\right]\right]=\mathbb{E}[Y]
$$

Theorem 4.5 of Wüthrich [46] gives the following statement, and an earlier binary classification result has been provided in Proposition 1 of Menon et al. [34].

Theorem 2.13 The true regression function $\boldsymbol{x} \mapsto p^{\dagger}(\boldsymbol{x})$ maximizes the ML Gini index among all auto-calibrated predictors $\boldsymbol{x} \mapsto \widehat{p}(\boldsymbol{x})$, i.e., $G_{p^{\dagger}}^{\mathrm{ML}} \geq G_{\widehat{p}}^{\mathrm{ML}}$, and we have an equality if and only if $p^{\dagger}(\boldsymbol{x})=\widehat{p}(\boldsymbol{x})$, a.s.

If we want to rely on the ML Gini index $G_{\widehat{p}}^{\mathrm{ML}}$ for model selection, we have to restrict to the class of auto-calibrated predictors $\boldsymbol{x} \mapsto \widehat{p}(\boldsymbol{x})$ for $Y$. This choice is auto-calibrated for $Y$ by definition (and, hence, unbiased) and it provides the true model as the argument that maximizes the ML Gini index.

Intuitively, auto-calibration pushes the predictors into the right positions (w.r.t. calibration), and then the Gini index selects the auto-calibrated predictor that best explains the observations. The remaining problem is to check the predictors for auto-calibration. In Figure 8 we provide a graphical analysis; in Corollary 2.16, below, we provide a mathematical result that allows one to develop a statistical test; and Fissler et al. [17], Section 4.1, provide a general approach using test functions, see, e.g., their Table 5.

Example 2.14 (binary classification of Section 2.1, revisited) We revisit our running binary classification example introduced in Section 2.1. We analyze the auto-calibration property (2.25) of these models. For this we fit a spline to the out-of-sample observations $Y_{i}$ against their predictions $\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)$ using the locfit function from the R library locfit [31]. As splines we choose polynomials of degree 2, and for fitting these splines we select a nearest neighbor fraction of $10 \%$. The results of the true model $p^{\dagger}(\boldsymbol{x})$ and the estimated models $\widehat{p}_{k}(\boldsymbol{x}), 1 \leq k \leq 3$, are

## Page 28
Figure 8: Out-of-sample auto-calibration property of the true model $p^{\dagger}(\boldsymbol{x})$ and the estimated models $\widehat{p}_{k}(\boldsymbol{x}), 1 \leq k \leq 3$; the $x$ - and $y$-scales are identical in all plots.
presented in Figure 8. We cannot perform a sensible auto-calibration plot for the homogeneous model $\widehat{p}_{0}$ because this model only takes one value in the prediction space, see (2.27). Therefore, we only show the results of the true model $p^{\dagger}(\boldsymbol{x})$ (top-left) and the models $\widehat{p}_{k}(\boldsymbol{x}), 1 \leq k \leq 3$ (top-right and bottom).
The true model $p^{\dagger}(\boldsymbol{x})$ provides an auto-calibration plot (local fit of $Y$ against $p^{\dagger}(\boldsymbol{x})$ ) that lies fairly much on the orange diagonal line. Since the true model satisfies the auto-calibration property precisely, see (2.26), Figure 8 (top-left) shows the typical magnitudes of fluctuations implied by the random sampling of $Y_{i}$ (with finite sample size $n$ ). The auto-calibration plot of the estimated model $\widehat{p}_{2}(\boldsymbol{x})$ looks fairly similar to the one of the true model, from which we conclude that this estimated model is roughly auto-calibrated. Models $\widehat{p}_{1}(\boldsymbol{x})$ (underfitting) and $\widehat{p}_{3}(\boldsymbol{x})$ (overfitting) are more difficult to assess. First, the underfitted model leads to less dispersed predictions, this can be seen from Figure 6, but also from the fact that the maximal prediction $\max _{1 \leq i \leq n} \widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)$ is much smaller in model $k=1$ compared to model $k=2$, see $x$-axes in Figure 8 (all $x$ - and $y$-axes have the same scale in the different plots). The opposite holds true for the overfitted model $k=3$. From Figure 8 we conclude that the auto-calibration for $Y$
![Page 28 Image 1](cs13_gini_index_and_friends_assets/cs13_gini_index_and_friends_p28_img1.jpg)

## Page 29
holds for models $k=1,2$, but it does not seem to hold for model $k=3$; this is what we use in Table 6 .
For a more formal treatment of auto-calibration in these examples we refer to Section 2.8, below, and to Section 4.1 in Fissler et al. [17]. Figure 8 plots the locally averaged responses $Y_{i}$ (local spline fit) against their predictions $\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)$. We could also plot the locally averaged negative residuals (called biases) $\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)-Y_{i}$ against their predictions $\widehat{p}_{k}\left(\boldsymbol{x}_{i}\right)$, this is exactly the proposal considered in Figures 4 and 5 of Fissler et al. [17].
We (empirically) auto-calibrate model $k=3$. Formula (2.28) gives the mathematical framework for doing this. An empirical version of (2.28) is received by the local spline fit of Figure 8, i.e., in this plot we map the non-auto-calibrated predictions $\widehat{p}_{3}\left(\boldsymbol{x}_{i}\right)$ to empirically auto-calibrated predictions $\widehat{p}_{3}^{(\text {auto })}\left(\boldsymbol{x}_{i}\right)$. We use this latter as our new (auto-calibrated) regression function $\boldsymbol{x} \mapsto$ $\widehat{p}_{3}^{(\text {auto })}(\boldsymbol{x})$. Remark that, alternatively, we could sort the $Y_{i}$ by increasing $\widehat{p}_{3}\left(\boldsymbol{x}_{i}\right)$ and then use an isotonic regression; see Barlow-Brunk [4] and Dimitriadis et al. [12]. An isotonic regression preserves the ranks, we also refer to Remark 2.12.

| model | Bernoulli deviance loss $\mathfrak{D}$ <br> in-sample $\mathcal{L}$ | out-of-sample $\mathcal{T}$ | auto- <br> calibration | Gini index <br> $\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}$ |
| :-- | :--: | :--: | :--: | :--: |
| true model $p^{\dagger}$ | 0.7633 | 0.7653 | yes | 0.5534 |
| model $\widehat{p}_{0}$ | 0.9130 | 0.9070 | yes | 0.0000 |
| model $\widehat{p}_{1}$ | 0.8369 | 0.8380 | yes | 0.3969 |
| model $\widehat{p}_{2}$ | 0.7633 | 0.7654 | yes | 0.5532 |
| model $\widehat{p}_{3}$ | 0.7171 | 0.8089 | no | - |
| model $\widehat{p}_{3}^{(\text {auto })}$ | 0.7341 | 0.7893 | yes | 0.5049 |

Table 6: In-sample and out-of-sample Bernoulli deviance losses $\mathfrak{D}$ (small is good), autocalibration property and (out-of-sample) ML Gini indices $\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}$ (large is good) in the binary classification case.

Table 6 shows the model selection results of the auto-calibrated predictors. Both, w.r.t. the out-of-sample Bernoulli deviance loss $\mathfrak{D}$ and the Gini index $\widehat{G}_{\widehat{p}_{k}}^{\mathrm{ML}}$, we give (clear) preference to model $\widehat{p}_{2}(\boldsymbol{x})$. The auto-calibration step improves the performance of model $k=3$, see last line of Table 6. However, this improvement of model $k=3$ is not sufficient to be competitive w.r.t. model $k=2$. In principle, we could always apply the 2 -step estimation procedure of Remark 2.12. This restricts to auto-calibrated models, which is a general requirement in insurance pricing, and it generally improves the model as has been observed, e.g., in Ciatto et al. [7].

# 2.7 Regression modeling 

All derivations above have been considering a binary classification problem because this has allowed us to compare the CAP to the ROC curve. Most considerations translate to the regression set-up, where the real-valued and non-negative response $Y$ may describe claim counts, claim sizes or total aggregate claim amounts. We assume that the response $Y$ is described by covariates $\boldsymbol{x}$, giving us the true mean regression function

$$
\boldsymbol{x} \mapsto \mu^{\dagger}(\boldsymbol{x})=\mathbb{E}[Y \mid \boldsymbol{x}]
$$

## Page 30
This true mean is auto-calibrated for $Y$, i.e., a.s.

$$
\mathbb{E}\left[Y \mid \mu^{\dagger}(\boldsymbol{x})\right]=\mu^{\dagger}(\boldsymbol{x})
$$

The general goal now is to estimate this true (unknown) regression function $\boldsymbol{x} \mapsto \mu^{\dagger}(\boldsymbol{x})$ by an (auto-calibrated) regression function $\boldsymbol{x} \mapsto \widehat{\mu}(\boldsymbol{x})$ for $Y$. The following items indicate how the binary classification case translates to the regression case.

- Deviance loss $\mathfrak{D}$ : The presented relationship between the deviance loss and the MLE generally holds true within the exponential dispersion family (EDF), and the EDF contains, e.g., the Poisson, the negative binomial, the Bernoulli, the binomial, the gamma, the inverse Gaussian or Tweedie's compound Poisson models, see Chapters 2 and 4 of Wüthrich-Merz [47]. Thus, the model selection process within the EDF can be done completely analogously to Section 2.1. Moreover, also the KL divergence considerations carry over to the EDF case, and the corresponding consistency results hold for mean estimation because deviance losses $\mathfrak{D}$ are Bregman divergences; we also refer to Theorem 7 in Gneiting [23] which goes back to Savage [38].
- Mirrored Lorenz curve $\widetilde{L}_{n}^{+}(\alpha ; \widehat{\mu})$, CAP $\widehat{C}_{n}^{+}(\alpha ; \widehat{\mu})$, and Gini index $\widehat{G}_{\widehat{\mu}}^{\mathrm{ML}}$ : The results of Sections 2.2 and 2.3 translate one-to-one to the regression case. Note that for the regression case, we typically change the notation from $\widehat{p}(\boldsymbol{x})$ to $\widehat{\mu}(\boldsymbol{x})=\widehat{\mathbb{E}}[Y \mid \boldsymbol{x}]$, reflecting the estimated conditional mean of response $Y$, given the covariate $\boldsymbol{x}$, see (2.29).
- Auto-calibration: The results of Section 2.6 translate to the regression case.

The only part that is specific to binary classification is Section 2.4 about the ROC curve. However, this section is less important for model selection as it mainly serves at explaining that in the binary classification case, the AUC and the ML Gini index are equivalent, see (2.19). On the other hand, Kendall's $\tau$ and Somers' $D$ are not specific to binary classification and can be translated to the general regression case.

Finally, we remark that all our statements do not depend on a certain type of regression model. That is, these statements hold true, e.g., for GLMs, regression trees, neural network regression models, or boosting models. There are, however, two points to be considered. (1) If the regression function $\widehat{p}$ has ties, we should connect by straight lines within the ties, similar to the case of complete equality. (2) The auto-calibration step (2.27) may not comply with the selected model class, i.e., $\widehat{p}$ may come from a logistic GLM, but its auto-calibrated version $\widehat{p}^{(\text {auto) }}$ will in general no longer be a GLM.

# 2.8 Mathematical results on auto-calibration 

This section presents results for further reading and understanding, and it mainly follows DenuitTrufin $[11]$.

Proposition 2.15 (Property 3.1 in Denuit-Trufin [11]) Assume that $\boldsymbol{x} \mapsto \widehat{p}(\boldsymbol{x})$ is an autocalibrated predictor for $Y$ having mean $p$. For any $\alpha \in(0,1)$

$$
L_{F_{\widehat{p}(\boldsymbol{x})}}^{+}(\alpha)=C_{Y ; F_{\widehat{p}(\boldsymbol{x})}}^{+} \alpha
$$

## Page 31
Proof. Auto-calibration implies $p=\mathbb{E}[Y]=\mathbb{E}[\widehat{p}(\boldsymbol{x})]$. The proof then uses the tower property of conditional expectation w.r.t. $\widehat{p}(\boldsymbol{x})$, and auto-calibration of $\widehat{p}$ for $Y$ to receive

$$
C_{Y ; F_{\widehat{p}(\boldsymbol{x})}}^{+}(\alpha)=\frac{1}{p} \mathbb{E}\left[Y \mathbb{1}_{\left\{\widehat{p}(\boldsymbol{x})>F_{\widehat{p}(\boldsymbol{x})}^{-1}(\alpha)\right\}}\right]=\frac{1}{p} \mathbb{E}\left[\mathbb{E}[Y \mid \widehat{p}(\boldsymbol{x})] \mathbb{1}_{\left\{\widehat{p}(\boldsymbol{x})>F_{\widehat{p}(\boldsymbol{x})}^{-1}(\alpha)\right\}}\right]=L_{F_{\widehat{p}(\boldsymbol{x})}^{+}}(\alpha)
$$

This closes the proof.
Proposition 2.15 states that under auto-calibration the mirrored Lorenz curve $L_{\widehat{F}_{\widehat{p}(\boldsymbol{x})}}^{+}(\alpha)$ and the CAP $C_{Y ; F_{\widehat{p}(\boldsymbol{x}}}^{+}(\alpha)$ coincide. This motivates to study the area between the curves (ABC) of model predictors $\boldsymbol{x} \mapsto \widehat{p}(\boldsymbol{x})$ defined by

$$
\mathrm{ABC}_{\widehat{p}}=\int_{0}^{1}\left(C_{Y ; F_{\widehat{p}(\boldsymbol{x})}}^{+}(\alpha)-L_{F_{\widehat{p}(\boldsymbol{x})}^{+}}^{+}(\alpha)\right) d \alpha
$$

The following corollary is an immediate consequence of Proposition 2.15.
Corollary 2.16 If $\widehat{p}$ is an auto-calibrated predictor for $Y$, then $\mathrm{ABC}_{\widehat{p}}=0$. Moreover, under auto-calibration of $\widehat{p}$ for random variable $Y$ we have

$$
G_{F_{\widehat{p}(\boldsymbol{x})}}^{\mathrm{ML}}=\frac{G_{F_{\widehat{p}(\boldsymbol{x})}}^{\mathrm{eco}}}{G_{F_{Y}}^{\mathrm{eco}}}
$$

where the positive denominator does not depend on the chosen predictor $\widehat{p}$.

# Example 2.17 (binary classification of Section 2.1 and Example 2.14, revisited) 

We come back to our auto-calibration plots of Figure 8, where we need to decide whether these models are auto-calibrated for $Y$. Figure 9 shows the ABCs of the 3 models $\widehat{p}_{k}(\boldsymbol{x})$, $1 \leq k \leq 3$, where we replace the quantities in (2.30) by their empirical counterparts $\widetilde{C}_{n}^{+}\left(\alpha ; \widehat{p}_{k}\right)$ and $\widetilde{L}_{n}^{+}\left(\alpha ; \widehat{p}_{k}\right)$, respectively. The models $k=1,2$ provide $\mathrm{ABC}_{\widehat{p}_{k}} \approx 0$. In view of Corollary 2.16, this means that we cannot reject the null hypothesis that these models are auto-calibrated for $Y$ (based on a visual inspection). Whereas the last model $k=3$ has a clearly negative $\mathrm{ABC}_{\widehat{p}_{3}}<0$, see Figure 9 (bottom), which rejects the null hypothesis of model $k=3$ being auto-calibrated for $Y$. This exactly reflects our decisions made in Table 6 to replace $\widehat{p}_{3}$ by $\widehat{p}_{3}^{(\text {auto })}$.
Note that for a more formal treatment we would need to work out the distribution of $\mathrm{ABC}_{\widehat{p}_{k}}$ under the null hypothesis which would allow us for a formal statistical test on a given significance level.

We close this section with a final remark on Gini indices. Throughout this manuscript, we have carefully distinguished between the Gini index in economics $G_{F_{\widehat{p}(\boldsymbol{x})}}^{\text {eco }}$ and the ML Gini index $\widetilde{G}_{\widehat{F}_{\widehat{p}(\boldsymbol{x})}}^{\mathrm{ML}}$. A main difference between these two Gini indices lies in the choice of area B, see Figures 1 and 5. The reason for modifying the area B for model selection using the CAP in the binary classification case has been that we wanted the optimally ordered prediction to attain the upper bound 1 in (2.14). The difference between these two areas B can be quantified, and it is in the binary classification case given by $\sum_{i=1}^{n} Y_{i} /(2 n) \in(0,1 / 2]$, assuming that at least one response is non-zero. The crucial observation is that this difference does not depend on the chosen regression model $\widehat{p}$. As a consequence, it does not influence model selection maximizing the Gini index under auto-calibration, see Corollary 2.16.

## Page 32
Figure 9: $\mathrm{ABC}_{\widehat{p}_{k}}$ of the models $\widehat{p}_{k}, 1 \leq k \leq 3$.

# 3 Conclusion 

This tutorial describes the Gini index for model selection. There are two different versions of the Gini index, an economic version and a machine learning version. The economic version is based on the Lorenz curve and the machine learning version is based on the cumulative accuracy profile (CAP). We illustrate these two definitions, and we show that the two definitions can easily be related under auto-calibrated regression models. Moreover, auto-calibration is also the crucial property to make the Gini index a strictly consistent score, and, thus, maximizing the Gini index within auto-calibrated families gives a sensible model selection tool. Moreover, we consider autocalibration as a general property that every regression model should satisfy because this means, in an insurance pricing context, that every price cohort is on average self-financing and there is no systematic cross-financing between the price cohorts.

Acknowledgment. The authors kindly thank Jürg Schelldorfer and Daniel Meier for a very careful review of an earlier version of this tutorial and for their suggestions made. Moreover, we kindly thank Dirk Tasche for interesting discussions and for highlighting the literature on this topic in the field of credit risk modeling.
![Page 32 Image 1](cs13_gini_index_and_friends_assets/cs13_gini_index_and_friends_p32_img1.jpg)

## Page 33
# References 

[1] Agarwal, S., Graepel, T., Herbrich, R., Har-Peled, S., Roth, D. (2005). Generalization bounds for the area under the ROC curve. Journal of Machine Learning Research 6, 393-425.
[2] Akaike, H. (1974). A new look at the statistical model identification. IEEE Transactions on Automatic Control 19/6, 716-723.
[3] Arratia, R., Goldstein, L. (2010). Size bias, sampling, the waiting time paradox, and infinite divisibility: when is the increment independent? arXiv: 1007.3910.
[4] Barlow, R.E., Brunk, H.D. (1972). The isotonic regression problem and its dual. Journal of the American Statistical Association 67/337, 140-147.
[5] Byrne, S. (2016). A note on the use of empirical AUC for evaluating probabilistic forecasts. Electronic Journal of Statistics 10, 380-393.
[6] Cantelli, F.P. (1933). Sulla determinazione empirica delle leggi di probabilità. Giornale Dell'Istituto Italiano Degli Attuari 4, 421-424.
[7] Ciatto, N., Verelst, H., Trufin, J., Denuit, M. (2022). Does autocalibration improve goodness of lift? European Actuarial Journal, in press.
[8] Dawid, A. P. (1986). Probability forecasting. In Encyclopedia of Statistical Sciences, volume 7, pages 210-218. Wiley-Interscience.
[9] Denuit, M., Charpentier, A., Trufin, J. (2021). Autocalibration and Tweedie-dominance for insurance pricing in machine learning. Insurance: Mathematics $\mathcal{E}$ Economics 101/B, 485-497.
[10] Denuit, M., Sznajder, D., Trufin, J. (2019). Model selection based on Lorenz and concentration curves, Gini indices and convex order. Insurance: Mathematics and Economics 89, 128-139.
[11] Denuit, M., Trufin, J. (2021). Lorenz curve, Gini coefficient, and Tweedie dominance for autocalibrated predictors. LIDAM Discussion Paper ISBA 2021/36.
[12] Dimitriades, T., Gneiting, T., Jordan, A.I. (2021). Stable reliability diagrams for probabilistic classifiers. PNAS, 118/8, e2016191118.
[13] Embrechts, P., Klüppelberg, C., Mikosch, T. (2003). Modelling Extremal Events for Insurance and Finance. Springer.
[14] Engelmann, B., Hayden, E., Tasche, D. (2003). Testing rating accuracy. Risk 16/1, 82-86.
[15] Fellman, J. (1976). The effect of transformations on Lorenz curves. Econometrica 44/4, 823-824.
[16] Ferrario, A., Hämmerli, R. (2019). On boosting: theory and applications. SSRN Manuscript ID 3402687.
[17] Fissler, T., Lorentzen, C., Mayer, M. (2022). Model comparison and calibration assessment: user guide for consistent scoring functions in machine learning and actuarial practice. arXiv:2202.12780.
[18] Frees, E.W., Meyers, G., Cummings, A.D. (2011). Summarizing insurance scores using a Gini index. Journal of the American Statistical Association 106, 1085-1098.
[19] Frees, E.W., Meyers, G., Cummings, A.D. (2013). Insurance ratemaking and a Gini index. Journal of Risk and Insurance 81, 335-366.
[20] Gini, C. (1912). Variabilità e Mutuabilità. Contributo allo Studio delle Distribuzioni e delle Relazioni Statistiche. C. Cuppini, Bologna.
[21] Gini, C. (1936). On the measure of concentration with special reference to income and statistics. Colorado College Publication, General Series No. 208, 73-79.

## Page 34
[22] Glivenko, V. (1933). Sulla determinazione empirica delle leggi di probabilità. Giornale Dell'Istituto Italiano Degli Attuari 4, 92-99.
[23] Gneiting, T. (2011). Making and evaluating point forecasts. Journal of the American Statistical Association 106/494, 746-762.
[24] Gneiting, T., Raftery, A.E. (2007). Strictly proper scoring rules, prediction, and estimation. Journal of the American Statistical Association 102/477, 359-378.
[25] Gourieroux, C., Jasiak, J. (2007). The Econometrics of Individual Risk: Credit, Insurance and Marketing. Princeton University Press.
[26] Hanley, J.A., McNeil, B.J. (1982). The meaning and use of the area under a receiver operating characteristic (ROC) curve. Radiology 143, 29-36.
[27] Harrell, Jr., F.E. (2015). Regression Modeling Strategies: With Applications to Linear Models, Logistic and Ordinal Regression, and Survival Analysis. 2nd edition. Springer.
[28] Hastie, T., Tibshirani, R., Friedman, J. (2001). The Elements of Statistical Learning. Springer.
[29] Krüger, F., Ziegel, J.F. (2021). Generic conditions for forecast dominance. Journal of Business 8 Economics Statistics 39/4, 972-983.
[30] Ling, C.X., Li, C. (1998). Data mining for direct marketing: problems and solutions. Fourth International Conference on Knowledge Discovery and Data Mining, 73-79.
[31] Loader, C., Sun, J., Lucent Technologies, Liaw, A. (2022). locfit: local regression, likelihood and density estimation. https://cran.r-project.org/web/packages/locfit/index.html
[32] Lorenz, M.O. (1905). Methods of measuring the concentration of wealth. Publications of the American Statistical Association 9/70, 209-219.
[33] McDonald, J.B., Jensen, B.C. (1979). An analysis of some properties of alternative measures of income inequality based on the gamma distribution function. Journal of the American Statistical Association 74/368, 856-860.
[34] Menon, A.K., Jiang, X., Vembu, S., Elkan, C., Ohno-Machado, L. (2012). Predicting accurate probabilities with ranking loss. ICML'12: Proceedings of the 29th International Conference on Machine Learning, 659-666.
[35] Newson, R. (2002). Parameters behind "nonparametric" statistics: Kendall's tau, Somers' D and median differences. Stata Journal 2/1, 45-64.
[36] Noll, A., Salzmann, R., Wüthrich, M.V. (2018). Case study: French motor third-party liability claims. SSRN Manuscript ID 3164764. Version March 4, 2020.
[37] Pohle, M.-O. (2020). The Murphy decomposition and the calibration-resolution principle: A new per-spective on forecast evaluation. arxiv:2005.01835.
[38] Savage, L.J. (1971). Elicitable of personal probabilities and expectations. Journal of the American Statistical Association 66/336, 783-810.
[39] Schatz, I. (2020). Using the Gini coefficient to evaluate the performance of credit score models. Towards Data Science, January 4, 2020. Accessed 2022/04/03.
[40] Schervish, M.J. (1989). A general method of comparing probability assessors. The Annals of Statistics 17/4, 1856-1879.
[41] So, B., Boucher, J., Valdez, E. (2021). Cost-sensitive multi-class AdaBoost for understanding driving behavior based on telematics. ASTIN Bulletin 51/3, 719-751.

## Page 35
[42] Somers, R.H. (1962). A new asymmetric measure of association for ordinal variables. American Sociological Review 27/6, 799-811.
[43] Tasche, D. (2006). Validation of internal rating systems and PD estimates. arXiv:0606071.
[44] Tasche, D. (2021). Calibrating sufficiently. Statistics: A Journal of Theoretical and Applied Statistics 55/6, 1356-1386.
[45] Wüthrich, M.V. (2020). Bias regularization in neural network models for general insurance pricing. European Actuarial Journal 10/1, 179-202.
[46] Wüthrich, M.V. (2022). Model selection with Gini indices under auto-calibration. arXiv:2207.14372.
[47] Wüthrich, M.V., Merz, M. (2022). Statistical Foundations of Actuarial Learning and its Applications. Springer Actuarial, in press.
[48] Yitzhaki, S., Schechtman, E. (2013). The Gini Methodology: A Primer on a Statistical Methodology. Springer.
[49] Zadrozny, B., Elkan, C. (2002). Transforming classifier scores into accurate multiclass probability estimates. KDD '02: Proceedings of the 8th ACM SIGKDD International Conference on Knowledge Discovery and Data Nining, 694-699.