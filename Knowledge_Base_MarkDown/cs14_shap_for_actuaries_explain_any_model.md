_Note: Source document was split into 2 OCR chunks (pages 1-16, pages 17-25) to stay within token limits._

# CS14 SHAP for Actuaries Explain any Model

## Page 1
# SHAP for Actuaries: Explain any Model 

Michael Mayer* Daniel Meier ${ }^{\dagger}$ Mario V. Wüthrich ${ }^{\ddagger}$<br>Prepared for:<br>Fachgruppe "Data Science"<br>Swiss Association of Actuaries SAV<br>Version of March 15, 2023


#### Abstract

This tutorial gives an overview of SHAP (SHapley Additive exPlanation), one of the most commonly used techniques for examining a black-box machine learning (ML) model. Besides providing the necessary game theoretic background, we show how typical SHAP analyses are performed and used to gain insights about the model. The methods are illustrated on a simulated insurance data set of car claim frequencies using different ML models and different SHAP algorithms.


Keywords. XAI, explainability, machine learning, SHAP, Shapley values, regression modeling, interaction, partial dependence plot, motor insurance, claims frequency.

## 0 Introduction and overview

This study has been carried out for the working group "Data Science" of the Swiss Association of Actuaries SAV, see
https://www.actuarialdatascience.org
Parts of the text are based on the lecture notes of the lecture "Responsible Machine Learning" at ETH Zurich that can be found under
https://github.com/lorentzenchr/responsible_ml_material
SHAP (SHapley Additive exPlanation) is a key player in explaining a Machine Learning (ML) model locally, i.e., around a single observation. It was introduced in Lundberg-Lee [14], and since it has received much attention, not only when working with tabular data in ML but also with unstructured data like text or image data. The basic idea of SHAP is to decompose a model prediction into additive contributions of the features in a fair way, and repeating this process for many observations provides a powerful method for explaining the model as a whole. The roots of the method (fair additive decomposition) go back to a classical result on cooperative game theory by Shapley [17]. Thus, and in contrast to many other local explainability methods, SHAP

[^0]
[^0]:    *Actuarial Department, La Mobilière, Bern, michael.mayer@mobiliar.ch
    ${ }^{\dagger}$ Swiss Re Institute, Zurich, daniel_meier@swissre.com
    ${ }^{\ddagger}$ RiskLab, Department of Mathematics, ETH Zurich, mario.wuethrich@math.ethz.ch

## Page 2
is based on a solid theoretic foundation. This tutorial explains both theory and application of SHAP using a synthetic dataset of motor insurance claims, and for a recent actuarial application in life insurance we refer to Godin et al. [8].

# Organization. 

In the following section, we introduce the synthetic claim frequency data used in this tutorial. We then describe different regression models using classical model explanation methods like partial dependence plots. Then, we introduce the economic background of Shapley values and translate its theory into the domain of ML. The last section concludes.

## Software and code.

All results in this tutorial were produced using R 4.2.2 with TensorFlow 2.11. Accompanying compact Python and R notebooks with similar (yet not identical) results can be found at
https://github.com/JSchelldorfer/ActuarialDataScience

## 1 Data

Throughout this tutorial, we work with a simulated dataset with information on motor thirdparty liability (MTPL) insurance policies and claims. Simulated data has the advantage that we know the true model, which allows us to compare the gained insights to the ground truth. The synthetic dataset consists of 1 million insurance policies providing the following observations:

- year: year of coverage (binary being either 2018 or 2019);
- town: location of registration being a town (binary 0 or 1 );
- driver_age: age of driver in years (between 18 and 88);
- car_weight: weight of car in kg (between 950 and 3120);
- car_power: horse power of car engine (between 50 and 341);
- car_age: age of car in years (between 0 and 23);
- claim_nb: number of claims observed within 1 calendar year (response).

For simplicity, we assume that all considered insurance policies have full year exposures. Table 1 shows the top six rows of the simulated dataset. The model response claim_nb as well as all features are illustrated univariate (marginally) in Figure 1. They show the typical behavior of MTPL data, most policies do not suffer any claim, the maximal number of claims on a single policy within one calendar year being 4.
To create realistic and correlated features, we used Bernoulli margins for the binary features, and (scaled, shifted and rounded) Beta distributions for the other features, coupled together by a Gaussian copula. Table 1 shows the pairwise Pearson correlation coefficients between all variables.
The values of the response variables claim_nb have been sampled from a Poisson distribution with (true) expected values (on the log scale)

$$
\log \mu^{*}(\boldsymbol{x})=0.15 \cdot \text { town }+h(\text { driver_age })+\frac{(0.3+0.15 \cdot \text { town }) \cdot \text { car_power }}{100}-0.02 \cdot \text { car_age }
$$

## Page 3
| year | town | driver_age | car_weight | car_power | car_age | claim_nb |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| 2018 | 1 | 51 | 1760 | 173 | 3 | 0 |
| 2019 | 1 | 41 | 1760 | 248 | 2 | 0 |
| 2018 | 1 | 25 | 1240 | 111 | 2 | 0 |
| 2019 | 0 | 40 | 1010 | 83 | 9 | 0 |
| 2018 | 0 | 43 | 2180 | 169 | 5 | 0 |
| 2018 | 1 | 45 | 1170 | 149 | 1 | 1 |

Table 1: First six data rows of the simulated dataset.

Figure 1: Univariate description of the simulated dataset.

|  | year | town | driver_age | car_weight | car_power | car_age | claim_nb |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| year | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| town | 0.00 | 1.00 | -0.16 | 0.00 | 0.00 | 0.00 | 0.05 |
| driver_age | 0.00 | -0.16 | 1.00 | 0.09 | 0.10 | 0.28 | -0.03 |
| car_weight | 0.00 | 0.00 | 0.09 | 1.00 | 0.68 | 0.00 | 0.04 |
| car_power | 0.00 | 0.00 | 0.10 | 0.68 | 1.00 | 0.09 | 0.06 |
| car_age | 0.00 | 0.00 | 0.28 | 0.00 | 0.09 | 1.00 | -0.02 |
| claim_nb | 0.00 | 0.05 | -0.03 | 0.04 | 0.06 | -0.02 | 1.00 |

Table 2: Pairwise empirical Pearson correlations between the variables.
![Page 3 Image 1](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p03_img1.jpg)

## Page 4
Figure 2: True effect of the age of driver variable driver_age (on log frequency scale).
for features $\boldsymbol{x} \in \mathbb{R}^{6}$ given by

$$
\boldsymbol{x}=\left(\text { year, town, driver_age, car_weight, car_power, car_age }\right)^{\top}
$$

and where the age effect $h$ (driver_age) equals the logarithm of a polynomial of degree 8 depicted in Figure 2.
The true regression function $\boldsymbol{x} \mapsto \mu^{*}(\boldsymbol{x})$ has the following properties on the log scale:

- No effect of year; i.e., we have stationarity over time.
- Linear and additive car_age effect.
- Highly non-linear and additive driver_age effect.
- Linear effect of car_power, with slope depending on town, i.e., there is an interaction effect between these two variables.
- The variable car_weight has no effect on the expected response, but it is strongly correlated with the car_power variable, allowing for a potential leakage of information.

This synthetic data can be downloaded as a Parquet file from
https://github.com/JSchelldorfer/ActuarialDataScience
$\rightarrow$ "14 SHAP for Actuaries: Explain any Model" $\rightarrow$ "rdata".

# 2 Regression models and first results 

The main goal in statistical (regression) modeling is to find the true regression function $\boldsymbol{x} \mapsto$ $\mu^{*}(\boldsymbol{x})$ from data $\mathcal{D}=\left\{\left(y_{i}, \boldsymbol{x}_{i}\right) ; i=1, \ldots, n\right\}$, where we assume that the data points $\left(y_{i}, \boldsymbol{x}_{i}\right)$, $1 \leq i \leq n$, have been generated independently and from the same model. The vectors $\boldsymbol{x}_{i}=\left(x_{i, 1}, \ldots, x_{i, p}\right)^{\top} \in \mathbb{R}^{p}$ describe the feature information (covariates, predictors, independent variables), and $y_{i} \in \mathbb{N}_{0}$ describe the responses which in our case have been generated from Poisson distributions with conditional means, for features $\boldsymbol{x} \in \mathbb{R}^{p}$,

$$
\mu^{*}(\boldsymbol{x})=\mathbb{E}(Y \mid \boldsymbol{X}=\boldsymbol{x})>0
$$
![Page 4 Image 1](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p04_img1.jpg)

## Page 5
we use the upper symbol * to denote the true regression function. Since the true regression function $\mu^{*}$ typically is not known we use a model

$$
\boldsymbol{x} \mapsto \mu(\boldsymbol{x})
$$

where the regression function $\mu$ is chosen from a pre-selected model class that (hopefully) can approximate the true regression function $\mu^{*}$ well. More explicitly, we try to select a regression function $\widehat{\mu}$ from the pre-selected model class based on the data $\mathcal{D}$ such that the resulting Poisson deviance loss is minimized within that model class. ${ }^{1}$ The hat in $\widehat{\mu}$ indicates that the model $\mu$ has been selected/fitted based on the sample $\mathcal{D}$. This sample has responses $\boldsymbol{y}=\left(y_{1}, \ldots, y_{n}\right)^{\top}$, and we denote the predicted/fitted values by

$$
\widehat{\boldsymbol{y}}=\left(\widehat{y}_{1}, \ldots, \widehat{y}_{n}\right)^{\top}=\left(\widehat{\mu}\left(\boldsymbol{x}_{1}\right), \ldots \widehat{\mu}\left(\boldsymbol{x}_{n}\right)\right)^{\top}
$$

The average Poisson deviance loss is given by

$$
\mathfrak{D}(\boldsymbol{y}, \widehat{\boldsymbol{y}})=\frac{1}{n} \sum_{i=1}^{n} 2\left(y_{i} \log \left(y_{i} / \hat{y}_{i}\right)-\left(y_{i}-\widehat{y}_{i}\right)\right)
$$

we refer to Table 4.1 in Wüthrich-Merz [21]. We consider the following three model classes:

1. Log-additive generalized linear model (GLM): $\boldsymbol{x} \mapsto \log (\mu(\boldsymbol{x}))=\beta_{0}+\sum_{j=1}^{p} \beta_{j} x_{j}$ for regression parameter $\boldsymbol{\beta}=\left(\beta_{0}, \ldots, \beta_{p}\right)^{\top} \in \mathbb{R}^{p+1}$;
2. Deep feed-forward neural network (NN) of depth 3 with number of neurons $(40,20,10)$ in the three hidden layers, with hyperbolic tangent activation function in the hidden layers and with exponential activation in the output layer; the deep network is implemented via Keras and TensorFlow [2], we use a $10 \%$ validation set from the training data to exercise early stopping and we use the adam optimizer with a $1 / 10000$ learning rate;
3. Gradient boosted tree was built using the LightGBM (LGB) package [10], its hyperparameters were chosen by grid-search and five-fold cross-validation, the number of boosting rounds was determined by early-stopping on the cross-validation performance, and the learning rate was fixed at 0.05 ;
(4.) Ground Truth $\mu^{*}$ as benchmark (which is available in this synthetic example).

We partition the entire sample $\mathcal{D}$ of size $n=10^{6}$ at random into a learning dataset and a test dataset in a ratio of $9: 1$, and we use the learning dataset for fitting (in-sample) the three models GLM, NN and LGB, and the test dataset for analyzing the model performance (out-of-sample). Before heading into SHAP, we provide a short classic model interpretation in terms of performance measurements, Table 3 shows in-sample and out-of-sample average Poisson deviance losses, and these are also illustrated in Figure 3. Note that the differences between the models are comparably small in Figure 3 (lhs). This reflects the typical behavior in non-life insurance claim counts modeling, namely, that we have a low signal-to-noise ratio, meaning that the random

[^0]
[^0]:    ${ }^{1}$ Remark that the Poisson deviance loss is a strictly consistent loss function for mean estimation and, henceforth, if the pre-selected model class contains the true model $\mu^{*}$, asymptotically, this true model is selected by the Poisson deviance loss minimization; see Gneiting [7], Fissler et al. [5] and Wüthrich-Merz [21].

## Page 6
|  | Poisson deviance loss |  |
| :-- | :--: | :--: |
|  | in-sample | out-of-sample |
| Ground Truth | 0.4333 | 0.4329 |
| model GLM | 0.4367 | 0.4362 |
| model NN | 0.4345 | 0.4339 |
| model LGB | 0.4330 | 0.4332 |

Table 3: Average Poisson deviance losses: in-sample on the learning dataset and out-of-sample on the test dataset.

Figure 3: Left: Average Poisson deviance losses evaluated on the test dataset for the GLM, the NN, the LGB and the Ground Truth. Right: Corresponding relative improvements with respect to an intercept-only model (null model).
(noise) part is the dominant term in the deviance loss. Furthermore, Figure 4 shows permutation importance regarding average Poisson deviance losses on the test data. From this figure we conclude that the important variables are car_power, town and driver_age. Furthermore, we see that the GLM, as currently specified, cannot deal with the non-linear driver_age variable. Later, we will extend the model equation of the GLM to include non-linear terms, fixing this deficiency. We emphasize that permutation importance permutes one variable at a time and, therefore, does not properly respect the dependence structure within the covariates $\boldsymbol{x}$. This also applies to the partial dependence plots (PDPs) which we show in Figure 5 on a common vertical scale. For more interpretation of these types of graphs we refer to Mayer-Lorentzen [16] and Section 7.6 in Wüthrich-Merz [21].
![Page 6 Image 1](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p06_img1.jpg)

## Page 7
Figure 4: Permutation importance regarding average Poisson deviance losses.

# 3 Shapley values in economic theory 

What is SHAP? To answer this question, we first introduce Shapley values from a cooperative game theory perspective; see Shapley [17].
Let $\mathcal{M}=\{1, \ldots, p\}$ denote a set of $p \in \mathbb{N}_{>1}$ players. They play a cooperative game with a numeric payoff to be maximized. The contribution (total expected sum of payoffs) of a subset $\mathcal{L} \subseteq \mathcal{M}$ (or coalition) of the players is measured by a function

$$
v: \mathcal{L} \mapsto v(\mathcal{L}) \in \mathbb{R}
$$

How can the total expected payoff $v(\mathcal{M})$ be distributed fairly among the individual players? We first need to characterize fairness. Shapley [17] postulated the following axioms to be desirable properties of a fair distribution $\left(\phi_{j}\right)_{j=1}^{p}=\left(\phi_{j}^{(v)}\right)_{j=1}^{p}$ of the total expected payoff $v(\mathcal{M})$ among the $p$ players; see also Aas et al. [1]:
(A1) Efficiency: $v(\mathcal{M})=\sum_{j=0}^{p} \phi_{j}$, where $\phi_{0}=v(\emptyset)$ denotes the non-distributed payoff (often set to 0 in cooperative games).
(A2) Symmetry: If $v(\mathcal{L} \cup\{j\})=v(\mathcal{L} \cup\{k\})$ for every $\mathcal{L} \subseteq \mathcal{M} \backslash\{j, k\}$, then $\phi_{j}=\phi_{k}$.
(A3) Dummy player: If $v(\mathcal{L} \cup\{j\})=v(\mathcal{L})$ for all coalitions $\mathcal{L} \subseteq \mathcal{M} \backslash\{j\}$, then $\phi_{j}=0$.
(A4) Linearity: Consider two cooperative games with gain functions $v$ and $w$. Then, $\phi_{j}^{(v+w)}=$ $\phi_{j}^{(v)}+\phi_{j}^{(w)}$ and $\phi_{j}^{(\alpha v)}=\alpha \phi_{j}^{(v)}$ for all $1 \leq j \leq p$ and $\alpha \in \mathbb{R}$.

The Shapley values [17] are the only way to distribute a total expected payoff $v(\mathcal{M})$ among $p$ players so that these four axioms (A1)-(A4) are fulfilled. They are given as follows: The amount
![Page 7 Image 1](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p07_img1.jpg)

## Page 8
Figure 5: PDPs of all features and models.
![Page 8 Image 1](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p08_img1.jpg)

## Page 9
that player $j \in \mathcal{M}$ receives equals

$$
\phi_{j}=\phi_{j}^{(v)}=\sum_{\mathcal{L} \subseteq \mathcal{M} \backslash\{j\}} \underbrace{\frac{|\mathcal{L}|!(p-|\mathcal{L}|-1)!}{p!}}_{\text {Shapley weight }}\left[\underbrace{v(\mathcal{L} \cup\{j\})-v(\mathcal{L})}_{\text {Contribution of player } j}\right]
$$

Thus, a player's contribution is equal to the weighted average of her/his contribution to each possible coalition $\mathcal{L}$ of other players. Alternatively, Formula (3.1) can be expressed by using permutations $\pi \in S_{p}$ of $\mathcal{M}=\{1, \ldots, p\}$, namely,

$$
\phi_{j}=\phi_{j}^{(v)}=\frac{1}{p!} \sum_{\pi \in S_{p}}\left[v\left(\mathcal{L}_{\pi} \cup\{j\}\right)-v\left(\mathcal{L}_{\pi}\right)\right]
$$

where $\mathcal{L}_{\pi} \in \mathcal{M} \backslash\{j\}$ denotes the subset of all predecessors of index $j$ in permutation $\pi$.
As an illustration of Formula (3.1), the coauthors of this tutorial play a deterministic cooperative game with payoffs $v(\mathcal{L}), \mathcal{L} \subseteq \mathcal{M}$, summarized in Table 4 - imagine the average number of text lines written per minute. To calculate the Shapley value of Mario, we collect in Table 5 all components appearing in Formula (3.1), this provides

$$
\phi_{\text {Mario }}=3 \cdot 2 / 6+2.5 / 6+2.5 / 6+2.5 \cdot 2 / 6=8 / 3 \approx 2.67
$$

| $\mathcal{L}$ | $v(\mathcal{L})$ |
| :--: | :--: |
| $\emptyset$ | 0 |
| $\{$ Mario $\}$ | 3 |
| $\{$ Daniel $\}$ | 1 |
| $\{$ Michael $\}$ | 1 |
| $\{$ Mario, Daniel $\}$ | 3.5 |
| $\{$ Mario, Michael $\}$ | 3.5 |
| $\{$ Daniel, Michael $\}$ | 1.3 |
| $\mathcal{M}=\{$ Mario, Daniel, Michael $\}$ | 3.8 |

Table 4: Payoffs $v(\mathcal{L})$ for all combinations $\mathcal{L} \subseteq \mathcal{M}$ of the coauthors with $p=3$.

| Subsets <br> $\mathcal{L} \subseteq \mathcal{M} \backslash\{$ Mario $\}$ | Contribution of Mario <br> $v(\mathcal{L} \cup\{$ Mario $\})-v(\mathcal{L})$ | Shapley <br> weight |
| :--: | :--: | :--: |
| $\emptyset$ | $3-0=3$ | $2 / 6$ |
| $\{$ Daniel $\}$ | $3.5-1=2.5$ | $1 / 6$ |
| $\{$ Michael $\}$ | $3.5-1=2.5$ | $1 / 6$ |
| $\{$ Daniel, Michael $\}$ | $3.8-1.3=2.5$ | $2 / 6$ |

Table 5: Components in Formula (3.1) required to calculate the Shapley value $\phi_{\text {Mario }}$ of Mario.

## Page 10
# 4 Shapley values in statistics and machine learning 

### 4.1 From economic theory to statistics and machine learning

In statistics, Shapley values were proposed by Lipovetsky-Conklin [11] as a strategy to decompose the R-squared of a linear regression into additive contributions of the covariates. Their approach was based on retraining the model for every feature subset. Other early work on Shapley values in statistics and ML include Strumbelj-Kononenko [18, 19] and Lundberg-Lee [14]. These authors propose to use Shapley values to decompose predictions into feature contributions. Thus, the outcome of the cooperative game is the prediction, and the feature components are the players which are assumed to contribute according to the above fairness axioms.
Formally, the prediction $\mu(\boldsymbol{x})$ of a given feature vector $\boldsymbol{x} \in \mathbb{R}^{p}$ is to be decomposed into contributions $\phi_{j}=\phi_{j}^{(\mu(\boldsymbol{x}))} \in \mathbb{R}, 1 \leq j \leq p$, such that we have the efficiency axiom (A1)

$$
\mu(\boldsymbol{x})=\phi_{0}+\sum_{j=1}^{p} \phi_{j}
$$

where, typically, $\phi_{0}=\mathbb{E}(\mu(\boldsymbol{X}))$. Only if the selected values $\phi_{j}$ are Shapley values, the decomposition is fair according to the above axioms (A1)-(A4). In order to apply Shapley's formula, a contribution function $\mathcal{L} \mapsto v(\mathcal{L})$ must be selected. A natural candidate is

$$
v(\mathcal{L})=\mu\left(\boldsymbol{x}_{\mathcal{L}}\right)
$$

where $\boldsymbol{x}_{\mathcal{L}}=\left(x_{j}\right)_{j \in \mathcal{L}}$ represents the components of feature $\boldsymbol{x}=\left(x_{1}, \ldots, x_{p}\right)^{\top}$ in the feature subset $\mathcal{L} \subseteq \mathcal{M}$, selected from the full feature set $\mathcal{M}=\{1, \ldots, p\}$. Since models cannot simply turn off some features during prediction, the calculation/estimation of $\mu\left(\boldsymbol{x}_{\mathcal{L}}\right)$ is highly non-trivial, and there is some controversy whether to define it using marginal expectations $\mathbb{E}\left(\mu\left(\boldsymbol{x}_{\mathcal{L}}, \boldsymbol{X}_{\mathcal{M} \backslash \mathcal{L}}\right)\right)$ or conditional expectations $\mathbb{E}\left(\mu\left(\boldsymbol{x}_{\mathcal{L}}, \boldsymbol{X}_{\mathcal{M} \backslash \mathcal{L}}\right) \mid \boldsymbol{X}_{\mathcal{L}}=\boldsymbol{x}_{\mathcal{L}}\right)$ for $\mu\left(\boldsymbol{x}_{\mathcal{L}}\right)$; see, e.g., Sundararajan-Najmi [20] or Janzing et al. [9]. The core question (material difference) between these two is: Should the statistical dependence between the feature components in $\mathcal{L}$ and the feature components in $\mathcal{M} \backslash \mathcal{L}$ be broken (marginal) or not (conditional)? The rules of causal inference require the former (supposed we have a corresponding causal graph), while, statistically, the latter seems more natural. In the following section we present algorithms to calculate both of these versions.

### 4.2 Algorithms to calculate SHAP values

There exist several different algorithms to calculate SHAP values for a feature $\boldsymbol{x}$ with prediction $\mu(\boldsymbol{x})$. They use different representations, interpretations and approximations, and they (may) differ in their results. Three particularly important ones are described in the following (in chronological order as published):

- Monte-Carlo sampling of Strumbelj-Kononenko [19]: This model-agnostic method is an application of Formula (3.2): To calculate $\phi_{j}$ for a particular index $j \in \mathcal{M}$, the contributions $v\left(\mathcal{L}_{\pi} \cup\{j\}\right)-v\left(\mathcal{L}_{\pi}\right)$ of (3.2) are averaged for many randomly sampled permutations $\pi \in S_{p}$, filling the components not contained in $\mathcal{L}_{\pi}$ by random observations repeatedly drawn from a background dataset (implying marginal expectations; see last section). A pseudo-code listing is provided in Algorithm 1 of Appendix 5.

## Page 11
- Kernel SHAP of Lundberg-Lee [14]: Another model-agnostic algorithm is called Kernel SHAP, where Shapley values are derived by minimizing the weighted loss function

$$
\sum_{\emptyset \neq \mathcal{L} \subsetneq \mathcal{M}} \underbrace{\frac{p-1}{\binom{p}{|\mathcal{L}|}|\mathcal{L}|(p-|\mathcal{L}|)}}_{\text {Shapley kernel }}\left(\mu\left(\boldsymbol{x}_{\mathcal{L}}\right)-\phi_{0}-\sum_{j \in \mathcal{L}} \phi_{j}\right)^{2}
$$

under the side constraints $\phi_{0}=\mathbb{E}(\mu(\boldsymbol{X}))$ and $\phi_{0}+\sum_{j=1}^{p} \phi_{j}=\mu(\boldsymbol{x})$. It estimates $\mu\left(\boldsymbol{x}_{\mathcal{L}}\right)$ via marginal expectations for many $\mathcal{L} \subsetneq \mathcal{M}$; see Covert et al. [4] for an overview of various kernels and the connection to LIME (local interpretable model-agnostic explanations). Then, it uses a constrained weighted regression to obtain all $\phi_{j}$ directly without plugging it into Shapley's formula; see Covert-Lee [3] for further details and Aas et al. [1] for a version using conditional expectations instead, to capture the dependence structure in the features $\boldsymbol{x}$.

- TreeSHAP of Lundberg et al. [12]: TreeSHAP is a method tailored for decision trees. It estimates $\mu\left(\boldsymbol{x}_{\mathcal{L}}\right)$ by a conditional expectation using a recursive (path-dependent) algorithm identical to a method for calculating exact PDPs for decision trees; see Friedman [6], page 27. To evaluate Shapley's formula, the basic algorithm must be applied to each $\mathcal{L} \subseteq \mathcal{M}$, and it is therefore exponentially slow in $p$. Fortunately, the algorithm has been implemented in a way that evaluates all subsets $\mathcal{L}$ simultaneously, resulting in an exponential speed-up. Also a slower "interventional" version exists that estimates marginal expectations. Thanks to the additivity of SHAP values, TreeSHAP works well for tree ensembles such as boosted trees, and LGBs in our case. For a pseudo-code listing see Algorithm 2 of Lundberg et al. [13].

We provide a comparison of the algorithms in Appendix 5, and note:
SHAP has a solid theoretical foundation. In practice, part of it is lost because statistics is not mathematics, and we need to appropriately approximate and estimate certain quantities.

Remark 4.1 (exact Shapley values in statistics). In the following two situations, exact Shapley values can be calculated:

- $p=1$, i.e., there is only a single (real-valued) feature $\boldsymbol{X}=X$. Here, the contribution of $X$ is simply $\phi_{1}=\mu(x)-\phi_{0}$.
- $\mu$ is a linear regression model with $p$ uncorrelated feature components:

$$
\mu(\boldsymbol{x})=\underbrace{\beta_{0}}_{\phi_{0}}+\underbrace{\beta_{1} x_{1}}_{\phi_{1}}+\cdots+\underbrace{\beta_{p} x_{p}}_{\phi_{p}}
$$

using mean-centered feature components for notational simplicity; we refer to Aas et al. [1] for a proof.

## Page 12
Figure 6: Typical plot to visualize a SHAP decomposition of a single prediction of instance $i$ with feature $\boldsymbol{x}_{i}$ (all values on the log frequency scale, and using the LBG model).

What does the SHAP decomposition of the LGB model for the first instance $i=1$ look like? In Figure 6, we present a waterfall graph of a SHAP decomposition of a single prediction $\mu\left(\boldsymbol{x}_{i}\right)$ (on the log scale).

# Comments: 

- Figure 6 shows the expected frequency on the log scale, i.e., $f\left(\boldsymbol{x}_{i}\right):=\log \left(\mu\left(\boldsymbol{x}_{i}\right)\right)$. Note that this is the canonical scale of the Poisson model because the log function is the canonical link in the Poisson model.
- The empirical mean over all instances provides us with an estimate of -2.47 for $\phi_{0}=$ $\mathbb{E}[f(\boldsymbol{X})]$. This gives the calibration of the waterfall graph. We then add the SHAP values $\phi_{j}=\phi_{j}^{\left(f\left(\boldsymbol{x}_{i}\right)\right)}, 1 \leq j \leq p$, one at a time to this calibration (yellow for positive values and red for negative values), giving us the log-prediction $f\left(\boldsymbol{x}_{i}\right)=-2.24$. The lengths of the arrows show the contributions, instance $i$ is a young driver with driver_age $=25$ which provides the most significant (negative) impact on the expected number of claims for this driver.


### 4.3 From local to global explanations

Interpreting the model locally around a particular observation, while of key importance in certain applications, provides little information about the model as a whole, i.e., at the global level. We can compute SHAP decompositions for a sufficiently large set of $m \leq n$ observations $\left(y_{i}, \boldsymbol{x}_{i}\right)$, and then use descriptive statistics to derive the global properties of the model. Thanks to the very fast TreeSHAP algorithm, this works especially well for tree-based models.
![Page 12 Image 1](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p12_img1.jpg)

## Page 13
Let $\mathfrak{X} \in \mathbb{R}^{m \times p}$ be the $m \times p$ feature matrix with elements $x_{i, j}$ and $\Phi \in \mathbb{R}^{m \times p}$ the corresponding $m \times p$ matrix of the SHAP values with elements $\phi_{i, j}:=\phi_{j}^{\left(\mu\left(\boldsymbol{x}_{i}\right)\right)}, 1 \leq i \leq m$ and $1 \leq j \leq p$. Furthermore, let $\phi_{0}=\frac{1}{m} \sum_{i=1}^{m} \mu\left(\boldsymbol{x}_{i}\right)$ be the average prediction over the $m$ observations with feature vectors $\boldsymbol{x}_{i}$. By construction, SHAP values satisfy axiom (A1)

$$
\mu\left(\boldsymbol{x}_{i}\right)=\phi_{0}+\sum_{j=1}^{p} \phi_{i, j}
$$

for all instances $1 \leq i \leq m$. Based on $\mathfrak{X}$ and $\Phi$, we can investigate feature importance and feature effects using descriptive statistics.

# 4.3.1 SHAP feature importance 

The absolute SHAP value $\left|\phi_{i, j}\right|$ quantifies the importance of feature $j$ in predicting instance $i$. Taking the average over the $m$ selected observations results in a variable importance measure called SHAP feature importance, defined as

$$
I_{j}=\frac{1}{m} \sum_{i=1}^{m}\left|\phi_{i, j}\right| \quad \text { for } 1 \leq j \leq p
$$

The interpretation is simple: $I_{j}$ indicates the average absolute impact of feature $j$ on the prediction.
The values of $I_{j}$ can be visualized as a bar plot, see Figure 7 (top). An alternative is the so-called SHAP summary plot, see Figure 7 (bottom). It shows for each feature $j$ a horizontal scatter plot of the SHAP values $\phi_{i, j}, 1 \leq i \leq m$, where the vertical scatter (diameter) is proportional to their density. Such a beeswarm plot is usually enhanced by highlighting the (min-max scaled) feature values $f\left(\boldsymbol{x}_{i}\right)=\log \mu\left(\boldsymbol{x}_{i}\right)$ on the color axis (log frequency scale). In this way, the direction of the effect can be seen, i.e., whether high feature values would increase or decrease predictions.
Let us now decompose the predictions of $m=1000$ randomly selected instances from the training data and examine the SHAP importance for all four models. The results are shown in Figure 7. Note that all decompositions are made on the log frequency scale.

The code to produce the SHAP importance plots in Figure 7:

```
library(shapviz)
library(kernelshap)
# Select rows to explain, and a small background dataset for Kernel SHAP
with_seed{
    3948, {
        X_explain <- train[sample(nrow(train), 1000), x]
        bg <- train[sample(nrow(train), 200), ]
    }
}
# Model-agnostic Kernel SHAP for the GLM (-20 seconds)
shap_glm <- shapviz(kernelshap(fit_glm, X = X_explain, bg_X = bg))
# TreeSHAP internally calculated by LightGEM (0.05 seconds)
shap_lgb <- shapviz(fit_lgb, X_pred = data.matrix(X_explain))
# Importance
sv_importance(shap_glm)
sv_importance(shap_lgb)
```

## Page 14
Figure 7: Top: Bar plots of SHAP feature importance $I_{j}$. Bottom: SHAP summary plots (beeswarm plots).
![Page 14 Image 1](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p14_img1.jpg)

## Page 15
# Comments: 

- town and car_power are the two most important features across all models. Also compare this to Figure 4.
- The bar heights have an objective meaning: For instance, we can say that the feature town increases or decreases the log frequency prediction (calibration) $\phi_{0}$ on average by 0.15 .
- car_weight and, especially, year are clearly the least important features.
- The beeswarm plot also shows the direction of the effects: For instance, we see that high car_power tends to increase expected claim frequencies. The features in such a beeswarm plot are ordered by mean absolute SHAP values, i.e., SHAP feature importance $I_{j}, 1 \leq j \leq p$.
- We remark that the computation of TreeSHAP is blazingly fast.


### 4.3.2 Effects

The SHAP summary (beeswarm) plots have already given us a first impression about the direction of the feature effects. To see in more detail how a feature impacts the predictions, so-called SHAP dependence plots are considered. The SHAP dependence plot of a given feature component $j$ plots the SHAP values $\phi_{i, j}$ against the corresponding feature values $x_{i, j}$ for $1 \leq i \leq m$. Thus, it represents the graph

$$
\left\{\left(x_{i, j}, \phi_{i, j}\right), 1 \leq i \leq m\right\} \quad \text { for a fixed component } 1 \leq j \leq p
$$

see Figures 8-10. Vertical scatter around a neighborhood of a feature value indicates the presence of interaction effects, this can nicely be seen in Figure 9 (bottom-right), where we illustrate the true model $\mu^{*}$ for the variable car_power which has an interaction with town. There exist heuristics to determine which feature explains most of this vertical scatter, and this feature is highlighted on the color scale. Note that seeing vertical scatter and highlighting the potentially strongest interacting variable is a clear advantage over PDPs.

Figures 8-10 show the SHAP dependence plots for selected features of all models. In order to stress the different effect strengths, all plots use the same vertical axis. The variables shown on the color scale have been selected individually per feature and model using above mentioned heuristic.

The code to produce one of the dependence plots in Figure 8:

```
library(ggplot2)
sv_dependence(shap_lgb, "driver_age") +
    ggtitle("LGB") +
    ylin(-0.5, 1.05)
```


## Comments:

- Figure 8: driver_age has a non-linear effect on the response and it does not interact with any other variable, this can nicely be seen from the true model $\mu^{*}$, Figure 8 (bottom-right).

## Page 16
Figure 8: SHAP dependence plot for driver_age.


Figure 9: SHAP dependence plot for car_power.
![Page 16 Image 1](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p16_img1.jpg)
![Page 16 Image 2](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p16_img2.jpg)

## Page 17
Figure 10: SHAP dependence plot for car_weight.

Therefore, the color scale is not meaningful here. Interestingly, the LGB model finds best the true shape, where as the GLM can clearly not cope with this non-linear structure. The NN seems to slightly overfit as it shows vertical scatter.

- Figure 9: car_power has an interaction with town, and the true model $\mu^{*}$ and the LGB model find this interaction. NN finds an interaction, but cannot allocate it to the correct pair. The GLM is not able to model this interaction because we did not include (manually) any interaction terms in its specification.
- Figure 10: car_weight does not enter the true regression model, which is found by all models; also in this case the color scale is not meaningful because this variable does not have any interactions. The NN plot shows a slight vertical scatter which is probably induced by the strong correlation between car_weight and car_power.
- We conclude that the LGB model finds best the true regression structure, the GLM cannot cope with non-linearities and interactions, and the NN seems to overfit and has some difficulties to find the true regression structure. The latter is not very surprising because NN fitting involves several elements of randomness, and it is generally recommended to ensemble over different network fits (of the same network architecture) to receive good predictive models, see Section 7.4.4 in Wüthrich-Merz [21].


# 4.3.3 Compact SHAP analysis 

In case one is interested in only one model, more compact SHAP illustrations are possible, see Figures 11 and 12. The former gives the SHAP importance plot of the LGB model, and the latter
![Page 17 Image 1](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p17_img1.jpg)

## Page 18
Figure 11: SHAP importance plot for the LGB model; the numbers equal the mean absolute SHAP value of each feature component.
shows the SHAP dependence plots of the LGB model over all variables. In case of TreeSHAP, the run-time is negligible. For non-tree based models, calculating SHAP values (unfortunately) can take a while (see also Remark 4.2), but the code stays compact also in these cases. More time-consuming is the case when combining multiple neural networks, as the prediction function can be (very) slow in deep networks.

The code to produce Figures 11 and 12:

```
with_seed(3948, X_explain <- train[sample(nrow(train), 1000), x])
shap_lgb <- shapviz(fit_lgb, X_pred = data.matrix(X_explain))
sv_importance(shap_lgb, show_numbers = TRUE)
for (xvar in x) {
    (sv_dependence(shap_lgb, xvar, alpha = 0.5) +
        ggtitle(xvar) +
        ylim(-0.5, 1.05)) %>%
        print()
}
```


# Remarks 4.2. 

- Frequency-Severity split: In insurance pricing, the pure premium is usually modeled as the product of two models: a claim frequency model and a severity model, both using a log link. Thanks to additivity, their SHAP values (both on the log link scale) can be aggregated to provide an explanation for the combined (log) pure risk model.
- SHAP interactions: Lundberg et al. [12] introduced SHAP interaction values that decompose a prediction into additive contributions of feature pairs. This allows for a detailed
![Page 18 Image 1](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p18_img1.jpg)

## Page 19
Figure 12: SHAP dependence plots for the LGB model.
![Page 19 Image 1](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p19_img1.jpg)

## Page 20
analysis of interaction effects, e.g., when selecting interaction effects for a GLM based on the results of a boosted trees model. Due to their computational complexity, at the time of writing, SHAP interaction values have been implemented only for TreeSHAP, e.g., for XGBoost. The computational complexity compared to standard TreeSHAP increases by a factor of $p$, which is sufficiently fast in many cases.

- Additive feature effects: The SHAP dependence plots of the GLM and of the true model in Figure 8 suggest a 1:1 correspondence between Kernel SHAP dependence plots and PDPs (evaluated at the observed values, and up to a vertical shift). A similar result was observed for additively modeled features with TreeSHAP in a technical report in Mayer [15].
- Software: The main software reference for SHAP is Scott Lundberg's "shap" package in Python (https://github.com/slundberg/shap). In R, the landscape is scattered over multiple packages: TreeSHAP is available in h2o, xgboost, lightgbm, and treeshap; shapr and kernelshap provide implementations of Kernel SHAP; fastshap offers an efficient implementation of SHAP sampling; SHAPforxgboost and shapviz provide typical SHAP plots and serve as wrapper packages. The results in this tutorial are based on the packages highlighted in bold face.
- Comparison of SHAP algorithms: Figure 14 in the appendix shows dependence plots for the LGB model calculated by TreeSHAP, Kernel SHAP, as well as by Monte-Carlo sampling. The differences are barely visible in this case. To calculate the SHAP values of 1000 observations, TreeSHAP took only 0.04 seconds, while Kernel SHAP and MonteCarlo sampling ( 650 samples per feature) each had a run-time of 50 seconds on an ordinary laptop with an Intel(R) Core(TM) i7-8650U CPU (4 cores).


# 4.4 SHAP analysis to improve linear models 

It is amazing how much information can be generated with so few lines of code. If the ultimate goal of the modeling task is to obtain a strong (generalized) linear model, we can explore a ML method, evaluate its performance, perform a compact SHAP analysis, and then use these findings to (manually) craft a strong(er) GLM. What does this mean specifically in our case? We have seen in our example that the test performance of the LGB model is much higher than the one of the GLM, so there is space for improvement of the GLM. We have found the following items:

- year and car_weight: Due to their extremely small effects (and almost zero mean average SHAP values), we decide to drop these two feature components.
- town and car_power: Based on the SHAP dependence plot for car_power (and also for town) in Figure 12, we add an interaction term between the two variables. (This could also have been found using SHAP interaction values.)
- driver_age: We represent the feature non-linearly by a natural cubic spline with five knots, i.e., we model this component with a generalized additive model (GAM) component.

These findings suggest the following modified GLM/GAM approach:

## Page 21
Figure 13: Relative deviance gain (test set) and a PDP, now including the improved GLM/GAM.

```
library(splines)
fit_glm2 <- glm(
    claim_nb - town * car_power + ns(driver_age, 5) + car_weight + car_age,
    data = train,
    family = poisson()
)
r_squared_poisson(test[[y]], predict(fit_glm2, test, type = "response")) # 2.36%
```

Comment: The relative deviance gain has almost approached the test performance of the true model $\mu^{*}$. This is not surprising as we have almost reconstructed the true underlying model, see Figure 13.

# 5 Conclusion 

Originally, SHAP was intended as a local model explanation tool, i.e., to explain individual predictions of a black-box model. Thanks to efficient implementations, multiple predictions can now be decomposed by SHAP within a reasonable runtime. The decompositions can then be analyzed by simple graphical techniques to describe the model and its feature effects as a whole. In this way, SHAP has become an excellent addition to the classical model explainability tools. Not all properties of SHAP have been explored, yet. We hope to gain further insights here in the upcoming years.

## Acknowledgment

We would like to thank Christian Lorentzen and Andreas Troxler for their comprehensive review and their many inputs that led to a significant improvement of this tutorial. Furthermore, we would like to thank the Data Science Working Group of the Swiss Association of Actuaries SAV and our employers for supporting this work.
![Page 21 Image 1](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p21_img1.jpg)

## Page 22
# References 

[1] Kjersti Aas, Martin Jullum, and Anders Løland. Explaining individual predictions when features are dependent: More accurate approximations to Shapley values. Artificial Intelligence, 298:103502, 2021.
[2] JJ Allaire and François Chollet. Keras: R Interface to 'Keras', 2021. R package version 2.4.0.
[3] Ian Covert and Su-In Lee. Improving KernelSHAP: Practical Shapley value estimation using linear regression. In Arindam Banerjee and Kenji Fukumizu, editors, Proceedings of The 24th International Conference on Artificial Intelligence and Statistics, volume 130 of Proceedings of Machine Learning Research, pages 3457-3465. PMLR, 13-15 Apr 2021.
[4] Ian Covert, Scott Lundberg, and Su-In Lee. Explaining by removing: A unified framework for model explanation. arXiv, 2020.
[5] Tobias Fissler, Christian Lorentzen, and Michael Mayer. Model comparison and calibration assessment: User guide for consistent scoring functions in machine learning and actuarial practice. arXiv, 2022.
[6] Jerome H. Friedman. Greedy function approximation: A gradient boosting machine. The Annals of Statistics, 29(5):1189-1232, 2001.
[7] Tilmann Gneiting. Making and evaluating point forecasts. Journal of the American Statistical Association, 106(494):746-762, 2011.
[8] Frédéric Godin, Emmanuel Hammel, Patrice Gaillardetz, and Edwin Hon-Man Ng. Risk allocation through Shapley decompositions, with applications to variable annuities. ASTIN Bulletin, 53(2), 2023.
[9] Dominik Janzing, Lenon Minorics, and Patrick Bloebaum. Feature relevance quantification in explainable AI: A causal problem. In Silvia Chiappa and Roberto Calandra, editors, Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics, volume 108 of Proceedings of Machine Learning Research, pages 2907-2916. PMLR, 26-28 Aug 2020.
[10] Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma, Qiwei Ye, and Tie-Yan Liu. LightGBM: A highly efficient gradient boosting decision tree. In Advances in Neural Information Processing Systems, volume 30, pages 3149-3157. Curran Associates, Inc., 2017.
[11] Stan Lipovetsky and Michael Conklin. Analysis of regression in game theory approach. Applied Stochastic Models in Business and Industry, 17(4):319-330, 2001.
[12] Scott M. Lundberg, Gabriel Erion, Hugh Chen, Alex DeGrave, Jordan M. Prutkin, Bala Nair, Ronit Katz, Jonathan Himmelfarb, Nisha Bansal, and Su-In Lee. From local explanations to global understanding with explainable AI for trees. Nature Machine Intelligence, $2(1): 2522-5839,2020$.

## Page 23
[13] Scott M. Lundberg, Gabriel G. Erion, and Su-In Lee. Consistent individualized feature attribution for tree ensembles. arXiv, 2018.
[14] Scott M. Lundberg and Su-In Lee. A unified approach to interpreting model predictions. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, Advances in Neural Information Processing Systems 30, pages 47654774. Curran Associates, Inc., 2017.
[15] Michael Mayer. SHAP for additively modeled features in a boosted trees model. arXiv, 2022.
[16] Michael Mayer and Christian Lorentzen. Peeking into the black box: An actuarial case study for interpretable machine learning. arXiv, 2020.
[17] Lloyd S. Shapley. A value for n-person games. In Harold William Kuhn and Albert William Tucker, editors, Contributions to the Theory of Games (AM-28), Volume II, pages 307-318. Princeton University Press, dec 1953.
[18] Erik Strumbelj and Igor Kononenko. An efficient explanation of individual classifications using game theory. Journal of Machine Learning Research, 11:1-18, 2010.
[19] Erik Strumbelj and Igor Kononenko. Explaining prediction models and individual predictions with feature contributions. Knowledge and Information Systems, 41(3):647-665, dec 2014.
[20] Mukund Sundararajan and Amir Najmi. The many Shapley values for model explanation. arXiv, 2019.
[21] Mario V. Wüthrich and Michael Merz. Statistical Foundations of Actuarial Learning and its Application. Actuarial. Springer Cham, 2023.

## Page 24
# Appendix 

## Comparison of SHAP Algorithms


Figure 14: Comparison of different SHAP algorithms for the LGB model. Each column represents an algorithm, each row a feature. The differences are very small here. Thanks to the intentionally small scale, they can be best spotted for the car_weight (in the middle row).
![Page 24 Image 1](cs14_shap_for_actuaries_explain_any_model_assets/cs14_shap_for_actuaries_explain_any_model_p24_img1.jpg)

## Page 25
# Sampling SHAP 

```
Algorithm 1: Sampling SHAP
    Input: An observation \(\boldsymbol{x}_{i} \in \mathcal{D}\), feature index \(j\), number of iterations \(m\)
    Output: Shapley value \(\phi_{i, j}\)
    \(\phi_{i, j} \leftarrow 0\)
    for \(\ell=1\) to \(m\) do
        Choose a random permutation \(\pi \in S_{p}\)
        Define the subset \(\mathcal{L}_{\pi} \in \mathcal{M} \backslash\{j\}\) by all predecessors of index \(j\) in \(\pi\)
        Choose a random \(\boldsymbol{x}_{k} \in \mathcal{D}\)
        \(\phi_{i, j} \leftarrow \phi_{i, j}+\mu\left(\boldsymbol{x}_{i, \mathcal{L}_{\pi}}, x_{i, j}, \boldsymbol{x}_{k, \mathcal{M} \backslash\left(\mathcal{L}_{\pi} \cup\{j\}\right)}\right)-\mu\left(\boldsymbol{x}_{i, \mathcal{L}_{\pi}}, x_{k, j}, \boldsymbol{x}_{k, \mathcal{M} \backslash\left(\mathcal{L}_{\pi} \cup\{j\}\right)}\right)\)
    return \(\phi_{i, j} / m\)
```