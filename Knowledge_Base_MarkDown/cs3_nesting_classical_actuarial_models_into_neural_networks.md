_Note: Source document was split into 4 OCR chunks (pages 1-10, pages 11-18, pages 19-25, pages 26-27) to stay within token limits._

# CS3 Nesting Classical Actuarial Models into Neural Networks

## Page 1
# Nesting Classical Actuarial Models into Neural Networks 

Jürg Schelldorfer* ${ }^{*}$ Mario V. Wüthrich ${ }^{\dagger}$<br>Prepared for:<br>Fachgruppe "Data Science"<br>Swiss Association of Actuaries SAV

Version of January 22, 2019


#### Abstract

Neural network modeling often suffers the deficiency of not using a systematic way of improving classical statistical regression models. In this tutorial we exemplify the proposal of [17]. We embed a classical generalized linear model into a neural network architecture, and we let this nested network approach explore model structure not captured by the classical generalized linear model. In addition, if the generalized linear model is already close to optimal, then the maximum likelihood estimator of the generalized linear model can be used as initialization of the fitting algorithm of the neural network. This saves computational time because we start the fitting algorithm in a reasonable parameter. As a by-product of our derivations, we present embedding layers and representation learning which often provides a more efficient treatment of categorical features within neural networks than dummy and one-hot encoding.


Keywords. neural networks, architecture, car insurance, generalized linear models, embedding, nesting, embedding layers, one-hot encoding, dummy coding, representation learning, claims frequency, Poisson regression model, machine learning, deep learning.

## 0 Introduction and overview

This data analytics tutorial has been written for the working group "Data Science" of the Swiss Association of Actuaries SAV, see
https://www.actuarialdatascience.org
The main purpose of this tutorial is to provide a systematic approach of improving classical actuarial regression models using the toolbox of neural networks. We follow the CANN proposal [17] which stands for Combined Actuarial Neural Network approach. The CANN approach proposes nesting a classical parametric regression model into a neural network architecture so that we can benefit from both worlds simultaneously. This tutorial follows up the two previous ones of Noll et al. [10] and Ferrario et al. [4], in particular, we further develop the same numerical example of the French motor third-party liability (MTPL) insurance data set included in the R package CASdatasets, see Charpentier [3].

[^0]
[^0]:    *Swiss Re, Juerg_Schelldorfer@swissre.com
    ${ }^{\dagger}$ RiskLab, Department of Mathematics, ETH Zurich, mario.wuethrich@math.ethz.ch

## Page 2
# 1 The data and revisiting generalized linear models 

### 1.1 French motor third-party liability insurance data

We revisit the data freMTPL2freq which is included in the R package CASdatasets, see Charpentier [3]. ${ }^{1}$ This data comprises a French MTPL insurance portfolio with corresponding claim counts observed within one accounting year. This data has already been illustrated and studied in the previous two tutorials of Noll et al. [10] and Ferrario et al. [4]. Listing 1 provides a short summary of the data.

Listing 1: output of command str(freMTPL2freq)

```
> str(freMTPL2freq)
'data.frame': 678013 obs. of 12 variables:
$ IDpol : num 1 3 5 10 11 13 15 17 18 21 ...
$ ClaimNb : num [1:678013(1d)] 1 1 1 1 1 1 1 1 1 1 ...
    ..- attr(*, "dimnames")=List of 1
    .. ..$ : chr "139" "414" "463" "975" ...
$ Exposure : num 0.1 0.77 0.75 0.09 0.84 0.52 0.45 0.27 0.71 0.15 ...
$ Area : Factor w/ 6 levels "A","B","C","D",..: 4 4 2 2 2 2 5 5 3 3 2 ...
$ VehPower : int 5 5 6 7 7 6 6 7 7 7 ...
$ VehAge : int 0 0 2 0 0 2 2 0 0 0 ...
$ DrivAge : int 55 55 52 46 46 38 38 33 33 41 ...
$ BonusMalus: int 50 50 50 50 50 50 50 68 68 50 ...
$ VehBrand : Factor w/ 11 levels "B1","B10","B11",..: 4 4 4 4 4 4 4 4 4 4 ...
$ VehGas : Factor w/ 2 levels "Diesel","Regular": 2 2 1 1 1 1 2 2 1 1 1 ...
$ Density : int 1217 1217 54 76 76 3003 3003 137 137 60 ...
$ Region : Factor w/ 22 levels "R11","R21","R22",..: 18 18 3 15 15 8 8 20 20 12
```

A detailed descriptive analysis of this data is provided in the tutorial of Noll et al. [10]. The analysis in that reference also includes a (minor) data cleaning part on the original data which is used but not further discussed in the present manuscript. ${ }^{2}$

### 1.2 Poisson claims frequency modeling

One conclusion of the tutorial of Ferrario et al. [4] has been that the volume (time Exposure in yearly units) needs a careful treatment in regression modeling, in particular, it may enter the regression function in a non-linear fashion. In order to make the present analysis of this tutorial not too complicated we will neglect this finding and we will focus on the generalized linear model (GLM) as introduced in Noll et al. [10].
Our data set comprises 678 '013 insurance policies $i$ for which we assume that the numbers of claims $N_{i}$ (ClaimNb on line 4 in Listing 1) are independent and Poisson distributed with

$$
N_{i} \stackrel{\text { ind. }}{\sim} \operatorname{Poi}\left(\lambda\left(\boldsymbol{x}_{i}\right) v_{i}\right)
$$

for the given volumes $v_{i}>0$ (time Exposure in years on line 7 in Listing 1) and a given claims frequency function $\boldsymbol{x}_{i} \mapsto \lambda\left(\boldsymbol{x}_{i}\right)$, where $\boldsymbol{x}_{i}$ describes the feature information of policy $i$, see Assumptions 2.1 in Noll et al. [10] and lines 8-16 in Listing 1. All policies have been active within one accounting year, and the volumes are considered pro-rata temporis $v_{i} \in(0,1]$ for the corresponding time exposures.

[^0]
[^0]:    ${ }^{1}$ CASdatasets website http://cas.uqam.ca; the data is described on page 55 of the reference manual [2].
    ${ }^{2}$ The R code is available from https://github.com/JSchelldorfer/ActuarialDataScience

## Page 3
Task. The main problem to be solved is to find the regression function $\lambda(\cdot)$ such that it appropriately describes the data, and such that it generalizes to similar data which has not been seen, yet. Remark that the task of finding an appropriate regression function $\lambda: \mathcal{X} \rightarrow \mathbb{R}_{+}$ also includes the definition of the feature space $\mathcal{X}$ which typically varies over different modeling approaches.

# 1.3 Warming-up exercise in generalized linear modeling 

In Section 3 of Noll et al. [10] we have presented a GLM approach as a first possible regression model to estimate the unknown regression function $\lambda(\cdot)$. In the present section we are going to refine that GLM. The starting point of the modeling exercise is to perform a thorough descriptive analysis to better understand the data; we do not repeat this here but refer to [10, 4]. In a second step we need to pre-process the data, in particular, feature pre-processing is done. We use the same feature pre-processing as in Section 3.1 of Noll et al. [10]:

- Area: we choose a continuous (log-linear) feature component for the Area code and we therefore map $\{\mathrm{A}, \ldots, \mathrm{F}\} \mapsto\{1, \ldots, 6\}$
- VehPower: we build 6 categorical classes by merging vehicle power groups bigger and equal to 9 (totally 6 labels);
- VehAge: we build 3 categorical classes $[0,1),[1,10],(10, \infty)$;
- DrivAge: we build 7 categorical classes $[18,21),[21,26),[26,31),[31,41),[41,51),[51,71)$, $[71, \infty)$
- BonusMalus: continuous log-linear feature component (we cap at value 150);
- VehBrand: categorical feature component (totally 11 labels);
- VehGas: binary feature component;
- Density: log-density is chosen as continuous log-linear feature component;
- Region: categorical feature component (totally 22 labels).

Thus, we consider 3 continuous feature components (Area, BonusMalus, log-Density), 1 binary feature component (VehGas) and 5 categorical feature components (VehPower, VehAge, DrivAge, VehBrand, Region). The latter two are categorical by nature; the former three are continuous but their functional forms are far from being log-linear, therefore, we group them categorically, we also refer to Marra-Wood [9] for smooth variable selection. These categorical classes for VehPower, VehAge and DrivAge have been done based on expert opinion, only. This expert opinion has tried to find homogeneity within class labels and every class label should receive a sufficient volume (of observations), we refer to Sections 1 and 3 of Noll et al. [10]. Categorical features are implemented by dummy coding, see Section 2.2 in Ferrario et al. [4], and the resulting feature space $\mathcal{X}$ is given by

$$
\mathcal{X} \subset[1,6] \times\{0,1\}^{5} \times\{0,1\}^{2} \times\{0,1\}^{6} \times[50,150] \times\{0,1\}^{10} \times\{0,1\} \times[0,11] \times\{0,1\}^{21}
$$

## Page 4
That is, we have a $q_{0}=1+5+2+6+1+10+1+1+21=48$ dimensional feature space $\mathcal{X}$, and the feature components in $\{0,1\}^{k}$ add up either to 0 or 1 (dummy coding), this side constraint is the reason for using the symbol " $\subset$ " in formula (1.2), we also refer to Listing 3 in Noll et al. [10] for more details. Based on this feature pre-processing we set up a first GLM.
Model Assumptions 1.1 (Model GLM1) Choose feature space $\mathcal{X}$ as in (1.2) and define the regression function $\lambda: \mathcal{X} \rightarrow \mathbb{R}_{+}$by

$$
\boldsymbol{x} \mapsto \log \lambda(\boldsymbol{x})=\beta_{0}+\sum_{l=1}^{q_{0}} \beta_{l} x_{l} \stackrel{\text { def. }}{=}\langle\boldsymbol{\beta}, \boldsymbol{x}\rangle
$$

for parameter vector $\boldsymbol{\beta}=\left(\beta_{0}, \ldots, \beta_{q_{0}}\right)^{\prime} \in \mathbb{R}^{q_{0}+1}$. Assume for $i \geq 1$

$$
N_{i} \stackrel{\text { ind. }}{=} \operatorname{Poi}\left(\lambda\left(\boldsymbol{x}_{i}\right) v_{i}\right)
$$

We split our data into a learning data set $\mathcal{D}$ and a test data set $\mathcal{T}$. We use exactly the same partition as in Listing 2 of Noll et al. [10]. Then, we fit Model GLM1 with maximum likelihood estimation (MLE) on the learning data set $\mathcal{D}$ by minimizing the corresponding in-sample Poisson deviance loss (objective function) ${ }^{3}$

$$
\boldsymbol{\beta} \mapsto \mathcal{L}(\mathcal{D}, \lambda)=\frac{1}{n} \sum_{i=1}^{n} 2 N_{i}\left[\frac{\lambda\left(\boldsymbol{x}_{i}\right) v_{i}}{N_{i}}-1-\log \left(\frac{\lambda\left(\boldsymbol{x}_{i}\right) v_{i}}{N_{i}}\right)\right]
$$

for $\boldsymbol{\beta}$-dependent parametric regression function $\lambda(\cdot)=\lambda_{\boldsymbol{\beta}}(\cdot)$, and where the summation runs over all policies $1 \leq i \leq n=610^{i} 212$ in the learning data set $\mathcal{D}$. Denote the resulting MLE ${ }^{4}$ by $\widehat{\boldsymbol{\beta}}$. This provides estimated regression function $\widehat{\lambda}(\cdot)=\lambda_{\widehat{\boldsymbol{\beta}}}(\cdot)$. The quality of this model is assessed on the out-of-sample Poisson deviance loss (generalization loss) on the test data set $\mathcal{T}$ given by

$$
\mathcal{L}(\mathcal{T}, \widehat{\lambda})=\frac{1}{n_{\mathcal{T}}} \sum_{t=1}^{n_{\mathcal{T}}} 2 N_{t}\left[\frac{\widehat{\lambda}\left(\boldsymbol{x}_{t}\right) v_{t}}{N_{t}}-1-\log \left(\frac{\widehat{\lambda}\left(\boldsymbol{x}_{t}\right) v_{t}}{N_{t}}\right)\right]
$$

where the summation runs over all policies $1 \leq t \leq n_{\mathcal{T}}=67^{\prime} 801$ in the test data set $\mathcal{T}$. This provides the numerical results of Table 1, see also Table 5 in Noll et al. [10]. We observe that

|  | run <br> time | $\#$ <br> param. | in-sample <br> loss | out-of-sample <br> loss | average <br> frequency |
| :-- | :--: | :--: | :--: | :--: | :--: |
| homogeneous model $(\lambda \equiv$ constant) | 0.1 s | 1 | 32.93518 | 33.86149 | $10.02 \%$ |
| Model GLM1 | 20 s | 49 | 31.26738 | 32.17123 | $10.01 \%$ |
| Model GLM2 | 17 s | 48 | 31.25674 | 32.14902 | $10.01 \%$ |

Table 1: run time, number of model parameters, in-sample and out-of-samples losses (units are in $10^{-2}$ ), average estimated frequency on $\mathcal{T}$ (the empirically observed value is $10.41 \%$, see Table 3 in $[10]$ ).
this Model GLM1 leads to a substantial improvement over the model with constant frequency parameter $\lambda$ (estimated by MLE). The last column of Table 1 gives the estimated frequency on the test data set $\mathcal{T}$, the empirically observed value being $10.41 \%$, see Table 3 in [10].

[^0]
[^0]:    ${ }^{3}$ Recall that minimizing the deviance loss is equivalent to maximizing the log-likelihood.
    ${ }^{4}$ The run time of the corresponding R function glm on a personal laptop Intel(R) Core(TM) i7-8550U CPU @ 1.80 GHz 1.99 GHz with 16 GB RAM to find the MLE $\widehat{\boldsymbol{\beta}}$ is roughly 20 seconds; the optimization method used is iteratively weighted least squares (IWLS).

## Page 5
Figure 1: Model GLM1: estimated frequencies w.r.t. the categorized (continuous) feature components VehPower, VehAge and DrivAge (the corresponding reference group is normalized to the overall frequency of $10 \%$, illustrated by the dotted line).

In Figure 1 we present the resulting estimated frequencies of the (categorized) feature components VehPower, VehAge and DrivAge of Model GLM1 (the corresponding reference group is normalized to the overall frequency of $10 \%$, illustrated by the dotted line). Note that these feature components are continuous in nature, but we have been turning them into categorical ones for modeling purposes (as mentioned above). Having so much data, we can further explore these categorical feature components by trying to replace them by ordinal ones assuming an appropriate continuous functional form, still fitting into the GLM framework. ${ }^{5}$
As an example we show how to bring DrivAge into a continuous functional form. We therefore modify the feature space $\mathcal{X}$ from (1.2) and the regression function $\lambda$ from (1.3). We replace the 7 categorical age classes by the following continuous function

$$
\text { DrivAge } \mapsto \beta_{l} \text { DrivAge }+\beta_{l+1} \log (\text { DrivAge })+\sum_{j=2}^{4} \beta_{l+j}(\text { DrivAge })^{j}
$$

with regression parameters $\beta_{l}, \ldots, \beta_{l+4}$. Thus, we replace the 7 categorical classes (involving 6 regression parameters from dummy coding) by the above continuous functional form having 5 regression parameters. The remaining parts of the regression function in (1.3) are kept unchanged, and we call this new model Model GLM2.
On lines 1-4 of Listing 2 we specify Model GLM2 in detail, it shows the specific functional form for DrivAge, and it keeps unchanged all other terms, in particular, the two categorized (continuous) variables VehPower and VehAge are kept as in Model GLM1. On lines 14-18 of Listing 2 we provide the resulting MLEs of this continuous implementation (1.6) of the feature component DrivAge. We observe that all terms in the chosen functional form for DrivAge are significant.
The resulting out-of-sample performance on the test data $\mathcal{T}$ of this second model fitted to the learning data $\mathcal{D}$ is given in Table 1. We observe a slight improvement in (out-of-sample) predictive power (generalization loss). Henceforth, we prefer this latter model over the former one. Note that this transformation has reduced the number of estimated parameters by 1 from $q_{0}+1=49$ to 48 . This Model GLM2 will be the benchmark for all subsequent considerations.

[^0]
[^0]:    ${ }^{5}$ We could also consider generalized additive models (GAMs), but we refrain from doing so for the moment.
![Page 5 Image 1](cs3_nesting_classical_actuarial_models_into_neural_networks_assets/cs3_nesting_classical_actuarial_models_into_neural_networks_p05_img1.jpg)

## Page 6
Figure 2: comparison of the estimated frequencies in Models GLM1 and GLM2 for feature component DrivAge (normalized to age 46).

In Figure 2 we compare the resulting estimated frequencies of the two modeling approaches for DrivAge. The continuous Model GLM2 for driver's age looks similar to the categorical labeling, but it provides a smooth transition between the age classes compared to Model GLM1, and it leads to a substantially higher estimate for drivers of ages 18-19. Concluding, we do not have any reservation to use this continuous version.
We could proceed in a similar way for VehPower and VehAge. In order to not overload this tutorial, we refrain from doing so, and we choose Model GLM2 as benchmark model for all our subsequent derivations.
![Page 6 Image 1](cs3_nesting_classical_actuarial_models_into_neural_networks_assets/cs3_nesting_classical_actuarial_models_into_neural_networks_p06_img1.jpg)

## Page 7
Conclusion. We choose Model GLM2 as our benchmark model. This model is illustrated in Listing 2, and it has 48 parameters to be estimated. One weakness of this model is that it does not explore interactions between feature components beyond multiplications. This and other points are going to be challenged in the following sections.

# 2 Embedding layers in neural networks 

### 2.1 Definition of a neural network

We start by defining a generic feed-forward neural network, subsequently abbreviated as network. We recall Ferrario et al. [4]. Choose $k \geq 1$ and hyperparameters $q_{k-1}, q_{k} \in \mathbb{N}$. A network layer is a mapping

$$
\boldsymbol{z}^{(k)}: \mathbb{R}^{q_{k-1}} \rightarrow \mathbb{R}^{q_{k}}, \quad \boldsymbol{z} \mapsto \boldsymbol{z}^{(k)}(\boldsymbol{z})=\left(z_{1}^{(k)}(\boldsymbol{z}), \ldots, z_{q_{k}}^{(k)}(\boldsymbol{z})\right)^{\prime}
$$

with $q_{k}$ hidden neurons in the $k$-th hidden layer given by

$$
z_{j}^{(k)}(\boldsymbol{z})=\phi\left(w_{j, 0}^{(k)}+\sum_{l=1}^{q_{k-1}} w_{j, l}^{(k)} z_{l}\right) \stackrel{\text { def. }}{=} \phi\left\langle\boldsymbol{w}_{j}^{(k)}, \boldsymbol{z}\right\rangle, \quad \text { for } j=1, \ldots, q_{k}
$$

with weights $\boldsymbol{w}^{(k)}=\left(\boldsymbol{w}_{1}^{(k)}, \ldots, \boldsymbol{w}_{q_{k}}^{(k)}\right)^{\prime}=\left(w_{1,0}^{(k)}, \ldots, w_{q_{k}, q_{k-1}}^{(k)}\right)^{\prime} \in \mathbb{R}^{q_{k}\left(1+q_{k-1}\right)}$ and activation function $\phi: \mathbb{R} \rightarrow \mathbb{R}$. We emphasize two points from $[10,4]$ :

- $q_{0}$ is the dimension of the feature space $\mathcal{X}$ with input neurons $\boldsymbol{z}^{(0)}=\boldsymbol{x} \in \mathcal{X}$ (input layer).
- $\phi: \mathbb{R} \rightarrow \mathbb{R}$ is a (non-linear) activation function. In the sequel we choose the hyperbolic tangent activation function $\phi(x)=\tanh (x)$.

A general network architecture with $K$ hidden layers for our Poisson regression problem is then obtained by adding an output layer as follows

$$
\lambda: \mathcal{X} \rightarrow \mathbb{R}_{+}, \quad \boldsymbol{x} \mapsto \lambda(\boldsymbol{x})=\exp \left\{\left\langle\boldsymbol{w}^{(K+1)},\left(\boldsymbol{z}^{(K)} \circ \cdots \circ \boldsymbol{z}^{(1)}\right)(\boldsymbol{x})\right\rangle\right\}
$$

That is, we map the neurons $\boldsymbol{z}^{(K)}$ of the last hidden layer to the output layer $\mathbb{R}_{+}$using the exponential activation function and weights $\boldsymbol{w}^{(K+1)}$ (including an intercept). This network architecture has depth $K$ and receives a network parameter $\theta \in \mathbb{R}^{r}$ of dimension $r=\sum_{k=1}^{K+1} q_{k}(1+$ $q_{k-1}$ ) collecting all network weights $\boldsymbol{w}^{(k)}, k=1, \ldots, K+1$, we set $q_{K+1}=1$. Three examples with $K=3$ hidden layers are given in Figure 3. The example in the middle of Figure 3 has an input layer of dimension $q_{0}=9$ and $q_{1}=20, q_{2}=15$ and $q_{3}=10$ hidden neurons which results in a network parameter $\theta$ of dimension $r=686$.

The network in Figure 3 (middle) shows for each feature component one single neuron in the input layer (blue, green and magenta colors), thus, an input layer of dimension $q_{0}=9$. However, we have two categorical feature components VehBrand and Region with more than 2 different categorical labels. One-hot encoding requires that these two components receive 11 and 22 input neurons, respectively. Thus, one-hot encoding implies that the input layer has dimension $q_{0}=40$ (if we assume that all other feature components need one single input neuron). This results in

## Page 8
Figure 3: networks with $K=3$ hidden layers having $q_{1}=20, q_{2}=15$ and $q_{3}=10$ hidden neurons in the three hidden layers; the input layer has dimensions $q_{0}=40$ (lhs), $q_{0}=9$ (middle) and $q_{0}=11$ (rhs) resulting in network parameter dimensions $r=1^{\prime} 306,686$ and 726 , respectively.
dimension $r=1^{\prime} 306$ for the network parameter $\theta$. This is exactly the network illustrated in Figure 3 (lhs), with one-hot encoding for VehBrand in green color and one-hot encoding for Region in magenta color. Brute-force network calibration then simply fits this model using a version of the gradient descent algorithm; this is exactly what has been demonstrated in our previous tutorial [4].
We should ask ourselves whether the brute-force implementation of categorical feature components using one-hot encoding is optimal, since it seems to introduce an excessive number of network parameters (in our case $r=1^{\prime} 306$ ). There is a second reason why one-hot encoding seems to be sub-optimal for our purposes. In general, we would like to identify (cluster) labels that are similar for the regression modeling problem. This is not the case with one-hot encoding. If we consider, for instance, the 11 vehicle brands $\mathcal{B}=\{\mathrm{B} 1, \mathrm{~B} 10, \ldots, \mathrm{~B} 6\}$, one-hot encoding assigns a different unit vector $\boldsymbol{x}^{\text {VehBrand }} \in \mathbb{R}^{11}$ to each VehBrand $\in \mathcal{B}$. For two different brands VehBrand1 $\neq$ VehBrand2 $\in \mathcal{B}$ we always receive $\left\|\boldsymbol{x}^{\text {VehBrand1 }}-\boldsymbol{x}^{\text {VehBrand2 }}\right\|=\sqrt{2}$, thus, the (Euclidean) distance between all vehicle brands is the same under one-hot encoding. In the next section we present embedding layers which aim at embedding categorical feature components into low dimensional Euclidean spaces, clustering labels that are more similar for the regression modeling problem.

# 2.2 Embedding layers for categorical feature components 

Recently, Richman [12] has proposed to use embedding layers for categorical feature components, and he has noted that this can lead to better results compared to one-hot encoding, see Table 5 in [12]. Embedding layers are very common in natural language processing (NLP), we refer to Bengio et al. [1], Sahlgren [14] and Section 3 in Richman [12] for an overview of embedding layers. Embedding layers are used in NLP in order to represent words by numerical coordinates in a low dimensional space. This approach has two advantages. First, the dimension is reduced (compared to one-hot encoding with a large sparse matrix). Second, similarities between words can be examined and provide additional insights to one-hot encoding. See also Richman [12] for the rationales behind embedding layers.
![Page 8 Image 1](cs3_nesting_classical_actuarial_models_into_neural_networks_assets/cs3_nesting_classical_actuarial_models_into_neural_networks_p08_img1.jpg)

## Page 9
We exemplify the construction of an embedding layer on the categorical feature component VehBrand. For an embedding layer, we need to choose an embedding dimension $d \in \mathbb{N}$ (hyperparameter). The embedding is then defined by an embedding mapping

$$
e: \mathcal{B} \rightarrow \mathbb{R}^{d}, \quad \text { VehBrand } \mapsto e^{\text {VehBrand }} \stackrel{\text { def. }}{=} e(\text { VehBrand })
$$

Thus, we allocate to every label VehBrand $\in \mathcal{B}$ a $d$-dimensional vector $e^{\text {VehBrand }} \in \mathbb{R}^{d}$. This is called an embedding of $\mathcal{B}$ into $\mathbb{R}^{d}$, and the embedding weights $e^{\text {VehBrand }}$ are learned during the model calibration which is called representation learning.

Figure 4: schematic illustration of a two-dimensional embedding of VehBrand $\in \mathcal{B}$.
In Figure 4 we illustrate a two-dimensional embedding of $\mathcal{B}$. It shows for every vehicle brand a two-dimensional representation, i.e.

$$
\begin{aligned}
& \text { B1 } \mapsto e^{\mathrm{B} 1} \in \mathbb{R}^{2}, \\
& \text { B10 } \mapsto e^{\mathrm{B} 10} \in \mathbb{R}^{2}, \\
& \vdots \\
& \text { B6 } \mapsto e^{\mathrm{B} 6} \in \mathbb{R}^{2} .
\end{aligned}
$$

The schematic illustration of Figure 4 has the interpretation that, for instance, vehicle brand B12 is rather different from all other vehicle brands, and vehicle brands B1 and B3 have similarities, illustrated by a small Euclidean distance between these two vehicle brands.
If we embed the two categorical feature components VehBrand and Region into embedding layers of dimension $d=1$ each, then, these embeddings use $11+22=33$ embedding weights. For an embedding of dimension $d=2$ each, we receive $11 \cdot 2+22 \cdot 2=66$ embedding weights.
Having one-dimensional embeddings provides the network in Figure 3 (middle), with embedding vector $e^{\text {VehBrand }} \in \mathbb{R}^{1}$ in green color and embedding vector $e^{\text {Region }} \in \mathbb{R}^{1}$ in magenta color. This model results in $33+686=719$ parameters to be learned, thus, substantially less than the 1'306 parameters from one-hot encoding. On the other hand it adds an additional layer for the embeddings which may slow down calibration.
In Figure 3 (rhs) we show the resulting network with two-dimensional embeddings $e^{\text {VehBrand }} \in \mathbb{R}^{2}$ and $e^{\text {Region }} \in \mathbb{R}^{2}$ resulting in a parameter of dimension $66+726=792$.
![Page 9 Image 1](cs3_nesting_classical_actuarial_models_into_neural_networks_assets/cs3_nesting_classical_actuarial_models_into_neural_networks_p09_img1.jpg)

## Page 10
# 2.3 Embedding layer example 

We compare brute-force one-hot encoding and embedding layers on an explicit example. We choose a network of depth $K=3$, having hidden neurons $\left(q_{1}, q_{2}, q_{2}\right)=(20,15,10)$, and using one-hot encoding for the feature components VehBrand and Region, this network is illustrated in Figure 3 (lhs). As described above this results in $r=1^{\prime} 306$ network parameters to be calibrated. In order to fit this model we use the R interface to Keras. ${ }^{6}$ The code is provided in

Listing 3: network of depth 3 with one-hot coding for categorical features

```
Design <- layer_input(shape = c(40), dtype = 'float32', name = 'Design')
LogVol <- layer_input(shape = c(1), dtype = 'float32', name = 'LogVol')
Network = Design %>%
    layer_dense(units=20, activation='tanh', name='hidden1') %>%
    layer_dense(units=15, activation='tanh', name='hidden2') %>%
    layer_dense(units=10, activation='tanh', name='hidden3') %>%
    layer_dense(units=1, activation='linear', name='Network',
        weights=list(array(0, dim=c(10,1)), array(log(lambda.hom), dim=c(1))))
Response = list(Network, LogVol) %>% layer_add(name='Add') %>%
    layer_dense(units=1, activation=k_exp, name = 'Response', trainable=FALSE,
        weights=list(array(1, dim=c(1,1)), array(0, dim=c(1))))
model <- keras_model(inputs = c(Design, LogVol), outputs = c(Response))
model %>%
    compile(optimizer = optimizer_nadam(), loss = 'poisson')
```

Listing 3. Network on lines 4-9 of Listing 3 defines a network of depth $K=3$ having neurons $\left(q_{1}, q_{2}, q_{3}\right)=(20,15,10)$ and hyperbolic tangent activation function. This network produces a one-dimensional output (lines 8 of Listing 3). It is initialized such that we start in the MLE of the homogeneous model (constant frequency parameter, line 9 of Listing 3). On lines 11-13 we add the non-trainable offset $\log$ (Exposure), and on line 16 we specify the nadam optimizer, see Section 8.5 in Goodfellow et al. [6], and the Poisson deviance loss as objective function.

Figure 5: performance of the gradient descent algorithm, the blue graphs show the training losses and the red graphs the validation losses: (lhs) one-hot encoding for categorical feature components; (middle) 1-dimensional embeddings of categorical feature components; (rhs) 2dimensional embeddings of categorical feature components.

[^0]
[^0]:    ${ }^{6}$ Keras is a user-friendly API to TensorFlow, see https://tensorflow.rstudio.com/keras/
![Page 10 Image 1](cs3_nesting_classical_actuarial_models_into_neural_networks_assets/cs3_nesting_classical_actuarial_models_into_neural_networks_p10_img1.jpg)

## Page 11
We use that same feature pre-processing as in Section 2 of $[4]^{7}$, and we run the gradient descent algorithm for 500 epochs on the learning data set $\mathcal{D}$ on mini-batches of size 10'000 policies. To track over-fitting we split the learning data at the ratio of $9: 1$ to a training data set and a validation data set. In Figure 5 (lhs) we plot the decrease of training loss (blue color) and validation loss (red color), respectively, over 500 epochs. We see that after roughly 250 epochs we may exercise early stopping.

|  | epochs | run <br> time | $\#$ <br> param. | in-sample <br> loss | out-of-sample <br> loss | average <br> frequency |
| :-- | --: | --: | --: | --: | --: | --: |
| homogeneous model |  | 0.1 s | 1 | 32.93518 | 33.86149 | $10.02 \%$ |
| Model GLM2 |  | 17 s | 48 | 31.25674 | 32.14902 | $10.01 \%$ |
| Network One-Hot | 250 | 152 s | 1 '306 | 30.26768 | 31.67343 | $10.19 \%$ |
| Network Emb $(d=1)$ | 700 | 419 s | 719 | 30.24464 | 31.50647 | $9.90 \%$ |
| Network Emb $(d=2)$ | 600 | 365 s | 792 | 30.16513 | 31.45327 | $9.70 \%$ |

Table 2: run time, number of model parameters, in-sample and out-of-samples losses (units are in $10^{-2}$ ) of Models GLM2, $\left(q_{1}, q_{2}, q_{3}\right)=(20,15,10)$ network with one-hot encoding and embedding layers with dimensions $d=1,2$ for the categorical feature components VehBrand and Region.

The resulting losses of this network after 250 epochs on the entire learning data are given in Table 2 on row "Network One-Hot". We note that we obtain a clearly better model than Model GLM2 in terms of Poisson deviance losses (at the price of more run time). Fine-tuning of the network architecture and the gradient descent algorithm could further improve this model. For the time-being we stay with the current network architecture and its calibration, because we would like to see whether we get an improvement using embedding layers for categorical feature components.
The code for designing the network architecture with embedding layers for the categorical explanatory variables VehBrand and Region is given in Listing 4, with the first line defining the dimension $d$ of the embedding layers (we use the same embedding dimension for both categorical feature components). The network results of these architectures with $d=1$ and $d=2$, respectively, are provided in Table 2, and Figure 5 gives the convergence behaviors on training and validation sets (being a 9:1 partition of the learning data $\mathcal{D}$ ). In view of Figure 5 (middle and rhs) we use 700 epochs and 600 epochs for $d=1$ and $d=2$, respectively. The latter model has more parameters which also provides more degrees of freedom to the gradient descent method. This seems to slightly accelerate the fitting behavior.
On the one hand we observe that embedding layers provide a slower rate of convergence and longer run times than one-hot encoding of categorical variables. We suppose that this is caused by the fact that an embedding layer adds an additional layer to the network, see green and magenta arrows in Figure 3 (middle, rhs). Therefore, the back-propagation method for network calibration needs to be performed over 4 hidden layers for embedding layer coding compared to 3 hidden layers in one-hot encoding of categorical feature components.
On the other hand, the fitted models with embedding layers clearly outperform the model with one-hot encoding in terms of the out-of-sample loss, if the former models are trained sufficiently long. What is more worrying is that the calibration of the network models are very unstable

[^0]
[^0]:    ${ }^{7}$ The corresponding R code is available from https://github.com/JSchelldorfer/ActuarialDataScience

## Page 12
Listing 4: network of depth 3 with embeddings for categorical features

```
d <- 1 # dimension of the embedding layers
Design <- layer_input(shape = c(7), dtype = 'float32', name = 'Design')
VehBrand <- layer_input(shape = c(1), dtype = 'int32', name = 'VehBrand')
Region <- layer_input(shape = c(1), dtype = 'int32', name = 'Region')
LogVol <- layer_input(shape = c(1), dtype = 'float32', name = 'LogVol')
BrEmb = VehBrand %>%
    layer_embedding(input_dim = 11, output_dim = d, input_length = 1, name = 'BrEmb') %>%
    layer_flatten(name='Br_flat')
ReEmb = Region %>%
    layer_embedding(input_dim = 22, output_dim = d, input_length = 1, name = 'ReEmb') %>%
    layer_flatten(name='Re_flat')
Network = list(Design, BrEmb, ReEmb) %>%
    layer_concatenate(name='concate') %>%
    layer_dense(units=20, activation='tanh', name='hidden1') %>%
    layer_dense(units=15, activation='tanh', name='hidden2') %>%
    layer_dense(units=10, activation='tanh', name='hidden3') %>%
    layer_dense(units=1, activation='linear', name='Network',
        weights=list(array(0, dim=c(10,1)), array(log(lambda.hom), dim=c(1))))
Response = list(Network, LogVol) %>%
    layer_add(name='Add') %>%
    layer_dense(units=1, activation=k_exp, name = 'Response', trainable=FALSE,
        weights=list(array(1, dim=c(1,1)), array(0, dim=c(1))))
model <- keras_model(inputs = c(Design, VehBrand, Region, LogVol), outputs = c(Response))
```

(in the choice of the initial value of the gradient descent algorithm). This results in fluctuating average frequencies, see last column in Table 2. In fact, these numbers (not being part of the objective function during model calibration) fluctuate quite a bit which is a major issue for insurance pricing.

Figure 6: (lhs) histogram of exposures per VehBrand, (middle) observed frequency per VehBrand, (rhs) resulting weights in the embedding layer for $d=2$.

The embedding layers have an other advantage, namely, we can graphically illustrate the findings of the network (at least if $d$ is small). This is very useful in NLP as it allows us to explore similar words graphically in 2 or 3 dimensions, after some further dimension reduction techniques have been applied, see [1, 14, 12]. In Figures 6 (rhs) and 7 (rhs) we illustrate for $d=2$ the resulting embedding weights, see also (2.4). We observe clustering in both categorical labels, which
![Page 12 Image 1](cs3_nesting_classical_actuarial_models_into_neural_networks_assets/cs3_nesting_classical_actuarial_models_into_neural_networks_p12_img1.jpg)

## Page 13
Figure 7: (lhs) histogram of exposures per Region, (middle) observed frequency per Region, (rhs) resulting weights in the embedding layer for $d=2$.
indicates that some labels could be merged. For VehBrand we observe that car brand B12 is different from all other car brands, B10 and B11 seem to have similarities, and the remaining car brands cluster. For Region the result is more diverse, in fact, Figure 7 (rhs) suggests that a 1-dimensional embedding is not sufficient. This is in contrast to Figure 6 (rhs) where we have high co-linearity between the two dimensions. Figures 6 (lhs, middle) and 7 (lhs, middle) are taken from Figures 8 and 11 of [10], they show the observed marginal frequencies and the underlying volumes.

Conclusions. The networks improve the GLM results in terms of out-of-sample losses because we have not been investing sufficient efforts in finding the optimal GLM with respect to feature engineering and potential interactions. From the analysis in this section we prefer embedding layers over one-hot encoding for categorical feature components, however, at the price of longer run times. Besides that embedding layers might improve the out-of-sample performance of the network they allow us to visually identify relationships between the different levels of categorical inputs. The downsides of networks are that calibrations lead to volatile average frequency estimates and bias fluctuations. This is also going to be studied in the next section.

# 3 Combined actuarial neural network approach 

### 3.1 Nesting the actuarial model into a network architecture

In this section we combine the classical GLM and the network. This approach can be seen as rather universal because it applies to many other parametric regression problems, for another example see [5]. The idea is to nest the GLM into a network architecture.

Model Assumptions 3.1 (CANN approach: part I) Choose a feature space $\mathcal{X} \subset \mathbb{R}^{q_{0}}$ and define the regression function $\lambda: \mathcal{X} \rightarrow \mathbb{R}_{+}$by

$$
\boldsymbol{x} \mapsto \log \lambda(\boldsymbol{x})=\langle\boldsymbol{\beta}, \boldsymbol{x}\rangle+\left\langle\boldsymbol{w}^{(K+1)},\left(\boldsymbol{z}^{(K)} \circ \cdots \circ \boldsymbol{z}^{(1)}\right)(\boldsymbol{x})\right\rangle
$$

where the first term on the right-hand side of (3.1) is the regression function from Model Assumptions 1.1 with parameter vector $\boldsymbol{\beta}$, and the second term the regression function from (2.3) with network parameter $\theta$. Assume $N_{i} \stackrel{\text { ind. }}{\sim} \operatorname{Poi}\left(\lambda\left(\boldsymbol{x}_{i}\right) v_{i}\right)$ for all $i \geq 1$.
![Page 13 Image 1](cs3_nesting_classical_actuarial_models_into_neural_networks_assets/cs3_nesting_classical_actuarial_models_into_neural_networks_p13_img1.jpg)

## Page 14
Figure 8: CANN approach illustrating in orange color the classical GLM in the skip connection added to a network of depth $K=3$ with $\left(q_{1}, q_{2}, q_{3}\right)=(20,15,10)$ hidden neurons.

The CANN approach of Model Assumptions 3.1 is illustrated in Figure 8. The skip connection in orange color contains the GLM (note that for the moment we neglect that categorical feature components may use a different encoding for the GLM and the network parts).

We provide some remarks.

- Formula (3.1) combines our previous two models, in particular, it embeds the GLM into a network architecture by packing it into a so-called skip connection that directly links the input layer to the output layer, see orange arrow in Figure 8. Skip connections are used in deep networks because they have good calibration properties, potentially avoiding the vanishing gradient problem, see He et al. [7] and Huang et al. [8]. We use the skip connection for a different purpose here.
- The two models are combined in the output layer by a (simple) addition. This addition makes one of the intercepts $\beta_{0}$ and $w_{0}^{(K+1)}$ superfluous. Therefore, we typically fix one of the intercepts, in most cases $\beta_{0}$, and we only train the other intercept, say, $w_{0}^{(K+1)}$ in the new network parameter $\vartheta=(\boldsymbol{\beta}, \theta)$ of regression function (3.1).
- Regression function (3.1) requires that the GLM and the network model are defined on the same feature space $\mathcal{X}$. This may require that we merge the feature space of the GLM model and the network approach, and not both parts in the regression function (3.1) may consider all components of that merged feature space, for instance, when GLM considers a component in a dummy coding representation and the network part considers the same component in a continuous coding fashion.

The second important ingredient is the following idea.
Initialization 3.2 (CANN approach: part II) Assume that Model Assumptions 3.1 hold and that $\widetilde{\boldsymbol{\beta}}$ denotes the MLE for $\boldsymbol{\beta}$ under Model Assumptions 1.1. Initialize regression function
![Page 14 Image 1](cs3_nesting_classical_actuarial_models_into_neural_networks_assets/cs3_nesting_classical_actuarial_models_into_neural_networks_p14_img1.jpg)

## Page 15
(3.1) as follows: set for network parameter $\vartheta=(\boldsymbol{\beta}, \theta)$ the initial value

$$
\vartheta_{0}=\left(\widehat{\boldsymbol{\beta}}, \theta_{0}\right) \quad \text { with output layer weight } \boldsymbol{w}^{(K+1)} \equiv 0 \text { in } \theta_{0}
$$

Note that initialization (3.2) exactly provides the MLE prediction of the GLM part of the CANN model (3.1), i.e. it minimizes the Poisson deviance loss under Model Assumptions 1.1. If we start the gradient descent algorithm for fitting the CANN model (3.1) in this initial value $\vartheta_{0}$, and if we use the Poisson deviance loss as objective function, then the algorithm explores the network architecture for additional model structure that is not present in the GLM and which lowers the initial Poisson deviance loss related to the (initial) network parameter $\vartheta_{0}$. In this way we obtain an improvement of the GLM by network features. This provides a more systematic way of using network architectures to improve the GLM. We will highlight this with several examples.

# 3.2 Variants of the CANN approach 

Before providing explicit examples we would like to briefly discuss some variants of the CANN approach (3.1)-(3.2). The CANN approach starts the gradient descent algorithm in regression model

$$
\boldsymbol{x} \mapsto \lambda(\boldsymbol{x})=\exp \left\{\langle\widehat{\boldsymbol{\beta}}, \boldsymbol{x}\rangle+\left\langle\boldsymbol{w}^{(K+1)},\left(\boldsymbol{z}^{(K)} \circ \cdots \circ \boldsymbol{z}^{(1)}\right)(\boldsymbol{x})\right\rangle\right\}
$$

where $\widehat{\boldsymbol{\beta}}$ is the MLE of $\boldsymbol{\beta}$. There are two different ways of applying the gradient descent algorithm to (3.3): (1) we train the entire network parameter $\vartheta=(\boldsymbol{\beta}, \theta)$, (2) we declare the GLM part $\widehat{\boldsymbol{\beta}}$ to be non-trainable and only train the second term in $\vartheta=(\widehat{\boldsymbol{\beta}}, \theta)$. In the latter case, the optimal GLM always remains in the CANN regression function and it is modified by the network part. In the former case, the optimal GLM is modified interacting with the network part.
A variant of (3.3) in the case where we declare $\widehat{\boldsymbol{\beta}}$ to be non-trainable is to introduce a trainable (credibility) weight $\alpha \in[0,1]$ and we define a new regression model

$$
\boldsymbol{x} \mapsto \lambda(\boldsymbol{x})=\exp \left\{\alpha\langle\widehat{\boldsymbol{\beta}}, \boldsymbol{x}\rangle+(1-\alpha)\left\langle\boldsymbol{w}^{(K+1)},\left(\boldsymbol{z}^{(K)} \circ \cdots \circ \boldsymbol{z}^{(1)}\right)(\boldsymbol{x})\right\rangle\right\}
$$

If we train this model, then we learn a credibility weight $\alpha$ at which the GLM is considered in the CANN approach.
An extension of the CANN approach also allows us to learn across multiple insurance portfolios. Assume we have $J$ insurance portfolios, all living on the same feature space $\mathcal{X}$ and with $\widehat{\boldsymbol{\beta}}_{j}$ denoting the MLE of portfolio $j=1, \ldots, J$ in the GLM. Let $\chi \in\{1, \ldots, J\}$ be a categorical variable denoting which portfolio we consider. We define the regression function

$$
(\boldsymbol{x}, \chi) \mapsto \lambda(\boldsymbol{x}, \chi)=\exp \left\{\sum_{j=1}^{J}\left\langle\widehat{\boldsymbol{\beta}}_{j}, \boldsymbol{x}\right\rangle \mathbb{1}_{\{\chi=j\}}+\left\langle\boldsymbol{w}^{(K+1)},\left(\boldsymbol{z}^{(K)} \circ \cdots \circ \boldsymbol{z}^{(1)}\right)(\boldsymbol{x})\right\rangle\right\}
$$

In this case, the neural network part allows us to learn across portfolio because it describes the interaction between the portfolios. This approach has been considered in Gabrielli et al. [5].

### 3.3 A CANN example

### 3.3.1 Generic CANN implementation

We present a first example that implements the CANN approach (3.3) where we declare the MLE $\widehat{\boldsymbol{\beta}}$ of Model GLM2 to be non-trainable and where we use $d=1$ for the embedding layers

## Page 16
of the network part. We call this first example Model CANN0. The R script of this architecture is given in Listing 9 in the appendix. We comment on this in more detail. This model has 686 trainable network parameters, which are exactly the network weights shown in Figure 3 (middle), i.e. these are the weights $\theta$ that come from the neural network part. Then, it has 58 non-trainable network parameters, these are the 48 GLM parameters in $\widehat{\boldsymbol{\beta}}$ of Model GLM2 which we choose as non-trainable (see lines $14,20,26,32,38$ and 39 of Listing 9), as well as 10 non-trainable parameters, where 4 non-trainable parameters stem from the embedding identification (one-hot versus dummy coding for VehPower, VehAge, VehBrand and Region), 4 non-trainable parameters come from concatenating the GLM network (line 38 of Listing 9), and 2 non-trainable parameters are from blending the GLM with the network part (line 50 of Listing 9).
On lines 1-8 of Listing 9 we define the input variables: ContGLM $\in \mathbb{R}^{4}$ collects the four ordinal variables BonusMalus, VehGas, Density, Area; on lines 2-3 there are the GLM-categorized variables VehPowerGLM and VehAgeGLM; on lines 4-5 the categorical variables VehBrand and Region; line 6 collects all DrivAge related variables from line 3 of Listing 2, i.e. DrivAgeGLM $\in \mathbb{R}^{5}$ has 5 continuous components, see also (1.6); line 7 collects the continuous variables VehPower, VehAge and DrivAge. Thus, the latter three variables enter the CANN model twice in a different form for the GLM part and for the network part in (3.3). Moreover, we pre-process all feature components that enter the network part of the architecture with the MinMaxScaler (for the MinMaxScaler we refer to Section 2.2 of Ferrario et al. [4]). Finally, line 8 defines the offset $\log ($ Exposure).
On lines 11-33 we define the embedding layers for the 4 categorical variables VehPowerGLM, VehAgeGLM, VehBrand and Region using the MLE $\widehat{\boldsymbol{\beta}}$ as non-trainable weights. On lines 35-39 these categorical variables are concatenated with the continuous ones of the GLM part again using $\widehat{\boldsymbol{\beta}}$ as non-trainable weights. This provides the non-trainable GLMNetwork, see lines 3539. On lines 41-46 we define the $\left(q_{1}, q_{2}, q_{3}\right)=(20,15,10)$ network architecture. This considers the 9-dimensional variable consisting of ContGLM $\in \mathbb{R}^{4}$, ContNN $\in \mathbb{R}^{3}$, as well as the two onedimensional $(d=1)$ embedding weights for VehBrand and Region. These embedding weights are exactly the GLM parameters (and they are declared to be non-trainable). Therefore, this part exactly corresponds to Figure 3 (middle) with 686 trainable weights illustrated by the black arrows. We blend the two models on lines 48-50 also including the offset $\log ($ Exposure) from the underlying volumes.

# 3.3.2 Poisson CANN implementation 

Having the R script of Listing 9 we are ready to calibrate Model CANN0. Before doing so, we mention that this code is a bit cumbersome for the task we try to achieve. In the case of the Poisson distribution we can substantially simplify the CANN implementation. From (3.3) we see that if the GLM part is non-trainable with MLE $\widehat{\boldsymbol{\beta}}$, then we can merge this term with the given volumes $v_{i}$. Thus, we consider a network function

$$
\boldsymbol{x} \mapsto \log \lambda^{\mathrm{NN}}(\boldsymbol{x})=\left\langle\boldsymbol{w}^{(K+1)},\left(\boldsymbol{z}^{(K)} \circ \cdots \circ \boldsymbol{z}^{(1)}\right)(\boldsymbol{x})\right\rangle
$$

and we assume that

$$
N_{i} \stackrel{\text { ind. }}{\sim} \operatorname{Poi}\left(\lambda^{\mathrm{NN}}\left(\boldsymbol{x}_{i}\right) v_{i}^{\mathrm{GLM}}\right), \quad \text { with working weights } \quad v_{i}^{\mathrm{GLM}}=v_{i} \exp \langle\widehat{\boldsymbol{\beta}}, \boldsymbol{x}\rangle
$$

## Page 17
This leads to a (much) simpler representation of the CANN model, in particular, we can replace Listing 9 of the appendix by Listing 5 (which is almost identical to Listing 4).

Listing 5: Model CANN1/2 with embedding layers with dimensions $d=1,2$

```
Design <- layer_input(shape = c(7), dtype = 'float32', name = 'Design')
VehBrand <- layer_input(shape = c(1), dtype = 'int32', name = 'VehBrand')
Region <- layer_input(shape = c(1), dtype = 'int32', name = 'Region')
LogVolGLM <- layer_input(shape = c(1), dtype = 'float32', name = 'LogVol')
5
6}\mathrm{ BrEmb = VehBrand %>%
7 layer_embedding(input_dim = 11, output_dim = d, input_length = 1, name = 'BrEmb') %>%
8 layer_flatten(name='Br_flat')
9
10}\mathrm{ ReEmb = Region %>%
11 layer_embedding(input_dim = 22, output_dim = d, input_length = 1, name = 'ReEmb') %>%
12 layer_flatten(name='Re_flat')
13
14 Network = list(Design, BrEmb, ReEmb) %>%
15 layer_concatenate(name='concate') %>%
16 layer_dense(units=20, activation='tanh', name='hidden1') %>%
17 layer_dense(units=15, activation='tanh', name='hidden2') %>%
18 layer_dense(units=10, activation='tanh', name='hidden3') %>%
19
20
21 Response = list(Network, LogVolGLM) %>%
22
    23
24
25 model <- keras_model(inputs = c(Design, VehBrand, Region, LogVolGLM), outputs = c(Response))
```

We observe that this code has become much simpler, and in fact also calibration in Keras runs faster. Line 4 of Listing 5 specifies the offsets $\log v_{i}^{\mathrm{GLM}}$ and lines 14-19 define the network part $\lambda^{\mathrm{NN}}$. This network is based on embedding layers for the categorical feature components VehBrand and Region which may have (general) dimensions $d$. Note that in Listing 5 the embedding weights for VehBrand and Region are trainable, if we choose embedding dimension $d=1$, initialize these embedding layers with the corresponding parts of $\widehat{\boldsymbol{\beta}}$ and declare these two embedding layers to be non-trainable, then we exactly receive Model CANN0 from the previous section.

Remark. We would like to emphasize that (3.6) is by no means restricted to the GLM. In fact, we can choose any regression model for the skip connection (volume adjustments using working weights similar to (3.6)), for instance, we can replace the GLM prediction by a generalized additive model (GAM) prediction in the working weight definition. This is exactly the idea behind the Poisson boosting machine as it has been presented in Section 5.2 of our tutorial [10]. We choose two different versions for our CANN approach (3.5)-(3.6), the first one has embedding dimension $d=1$ and the second one has embedding dimension $d=2$ for the categorical feature components VehBrand and Region, see also lines 7 and 11 in Listing 5. Both versions use Model GLM2 in the skip connection (3.6). We call these two Models CANN1 and CANN2. In Figure 9 (lhs) we show the convergence statistics of the gradient descent algorithm where, again, we split the learning data 9:1 for a training set (blue) and a validation set (red). The left-hand side shows the calibration for embedding layers with $d=1$ (Model CANN1), and the right-hand

## Page 18
Figure 9: performance of the gradient descent algorithm, the blue graphs show the training losses and the red graphs the validation losses: (lhs) Model CANN1; (rhs) Model CANN2.
side uses embedding layers with $d=2$ (Model CANN2). We observe over-fitting after roughly 200 gradient descent steps. Note that this is much faster than in the network models of Figure 5, the reason being that the MLE of Model GLM2 provides a reasonable initial value for the gradient descent algorithm.

|  | epochs | run <br> time | $\#$ <br> param. | in-sample <br> loss | out-of-sample <br> loss | average <br> frequency |
| :-- | --: | --: | --: | --: | --: | --: |
| homogeneous model |  | 0.1 s | 1 | 32.93518 | 33.86149 | $10.02 \%$ |
| Model GLM2 |  | 17 s | 48 | 31.25674 | 32.14902 | $10.01 \%$ |
| Network Emb $(d=1)$ | 700 | 419 s | 719 | 30.24464 | 31.50647 | $9.90 \%$ |
| Network Emb $(d=2)$ | 600 | 365 s | 792 | 30.16513 | 31.45327 | $9.70 \%$ |
| CANN1 Emb $(d=1)$ | 200 | 115 s | 719 | 30.39966 | 31.50136 | $10.02 \%$ |
| CANN2 Emb $(d=2)$ | 200 | 117 s | 792 | 30.47557 | 31.56555 | $10.34 \%$ |

Table 3: run time, number of model parameters, in-sample and out-of-samples losses (units are in $10^{-2}$ ) of Models GLM2, $\left(q_{1}, q_{2}, q_{3}\right)=(20,15,10)$ network with embedding layers with dimensions $d=1,2$ for the categorical feature components VehBrand and Region, Models CANN1 and CANN2 with embeddings $d=1,2$, respectively.

The results are presented in Table 3. We observe that the performance of all network models with embedding layers are comparable in out-of-sample losses which range from 31.45327 to 31.50647 (last 4 rows of Table 3). More remarkable is that the GLM2 skip connection adds some stability to the average frequency, last column in Table 3, note that the empirically observed frequency on the test data $\mathcal{T}$ is $10.41 \%$.
A bit disappointing seems that the CANN approach does not lead to a clear improvement over the classical network approach in terms of out-of-sample losses. The main issue in the current set-up is that Model GLM2 is not sufficiently good so that the CANN approach could benefit from a very good initial model. In fact, we are penalized here for not having invested sufficient efforts in building a good GLM. However, the CANN approach will allow us to explicitly analyze the weaknesses of Model GLM2. This is what we are going to do next.
![Page 18 Image 1](cs3_nesting_classical_actuarial_models_into_neural_networks_assets/cs3_nesting_classical_actuarial_models_into_neural_networks_p18_img1.jpg)

## Page 19
# 3.4 Analyzing the GLM marginals 

The aim of the subsequent sections is to analyze the modeling of the regression function $\lambda(\cdot)$ in a more modular way. We therefore start with Model GLM2 given in Listing 2. This model considers a log-linear structure

$$
\boldsymbol{x} \mapsto \log \lambda(\boldsymbol{x})=\beta_{0}+\sum_{l=1}^{q_{0}} \beta_{l} x_{l}=\langle\boldsymbol{\beta}, \boldsymbol{x}\rangle
$$

with continuous feature components BonusMalus, Density, Area and DrivAge, categorized feature components VehPower and VehAge, and categorical feature components VehBrand, VehGas, Region. The goal is to see whether the functional form used to model the continuous and the categorized feature components is sufficiently good. We therefore change the modeling of one feature component at a time, keeping the modeling of the other components fixed. For instance, we choose VehPower and we consider

$$
\boldsymbol{x} \mapsto \log \lambda(\boldsymbol{x})=\langle\boldsymbol{\beta}, \boldsymbol{x}\rangle+\left\langle\boldsymbol{w}^{(2)}, \boldsymbol{z}^{(1)}(\text { VehPower })\right\rangle
$$

where the last term reflects a network of depth 1 (having $q_{1}$ hidden neurons) applied to the feature component VehPower, only. Note that we use a slight abuse of notation in (3.7) because VehPower enters feature $\boldsymbol{x}$ also as a categorical variable with 6 labels for the GLM approach. For the explicit implementation of (3.7) we again use approach (3.6) with working weights.

|  | epochs | run <br> time | \# train. <br> param. | in-sample <br> NN | out-of-sample <br> NN | out-of-sample <br> GAM |
| :-- | --: | --: | --: | --: | --: | --: |
| homogeneous model |  |  | 1 | 32.93518 | 33.86149 |  |
| Model GLM2 |  | 17 s | 48 | 31.25674 | 32.14902 |  |
| Area | 200 | 54 s | 22 | 31.25684 | 32.14768 | - |
| VehPower | 200 | 54 s | 22 | 31.25626 | 32.14965 | 32.15306 |
| VehAge | 200 | 54 s | 22 | 31.23750 | 32.12474 | 32.12724 |
| DrivAge | 200 | 54 s | 22 | 31.25681 | 32.14764 | 32.14138 |
| BonusMalus | 500 | 130 s | 22 | 31.19411 | 32.10286 | 32.09712 |
| Density | 200 | 54 s | 22 | 31.25679 | 32.14813 | 32.14945 |

Table 4: in-sample and out-of-samples losses (units are in $10^{-2}$ ) of Model GLM2, compared to a marginal network adjustment according to (3.7).

In Table 4 we present the results where we consider one continuous feature component in the form (3.7) at a time, and where we choose a single hidden layer network with $q_{1}=7$ hidden neurons. ${ }^{8}$ From Table 4 we see that the marginal modeling in Model GLM2 is quite good, the only two feature components that may be modeled in a better way are VehAge, i.e. the three age classes $[0,1),[1,10]$ and $(10, \infty)$ should be refined, and BonusMalus where a log-linear functional form is not fully appropriate. We would like to highlight that the variable BonusMalus needs more gradient descent steps, i.e. a later early stopping point. It seems that Model GLM2 sits in a rather "strong saddle point" for the variable BonusMalus which is difficult to leave for the gradient descent algorithm.

[^0]
[^0]:    ${ }^{8}$ In many cases one hidden layer is sufficient for modeling one-dimensional functions, for multivariate functionals deep networks show better fitting performance because they can model more easily interactions.

## Page 20
In the last column of Table 4 we have been adding the out-of-sample losses obtained from generalized additive model (GAM) predictions. GAMs are obtained by replacing the last term in (3.7) by a natural cubic spline, that is, we set

$$
\boldsymbol{x} \mapsto \log \lambda(\boldsymbol{x})=\langle\boldsymbol{\beta}, \boldsymbol{x}\rangle+\mathrm{ns}^{2}(\text { VehPower })
$$

where the first term on the right-hand side is the part originating from Model GLM2 and $\mathrm{ns}^{2}: \mathbb{R} \rightarrow \mathbb{R}$ denotes a natural cubic spline. For GAMs we refer to Wood [15], OhlssonJohansson [11] and Chapter 3 in Wüthrich-Buser [16]. We would like to emphasize that this GAM for marginals can be fit very efficiently, i.e. in less than 1s. But efficient fitting requires that we aggregate data for each label (marginally we have only few labels) using that aggregation leads to sufficient statistics under our Poisson model assumptions, see Section 3.1.2 in [16], and line 4 in Listing 6. The GAM fit is performed on lines 6-7 of Listing 6 where VolGLM specifies the working weights $v_{i}^{\mathrm{GLM}}$, see (3.6). The prediction can be done (again) on individual policies. Unfortunately, the GAM cannot be applied to the feature component Area because it has only 6 different labels. The out-of-sample results of the neural network approach and of the GAM approach are in line which can be interpreted as a "proof of concept" that these two methods work.

Listing 6: marginal GAM fitting of VehPower
1 library(plyr)
2 library(mgcv)
3 \# data compression of the learning data set
4 learn.GAM <- ddply(learn, .(VehPower), summarize, VolGLM=sum(VolGLM), ClaimNb=sum(ClaimNb))
\# GAM fitting
6 d.gam <- gam(ClaimNb s(VehPower, bs="cr"), data=learn.GAM, method="GCV.Cp", offset=log(VolGLM), family=poisson)
8 summary(d.gam)

In Figure 10 we provide the resulting marginal regression functions from approach (3.7) which exactly correspond to the results of Table 4. These plots confirm our findings, namely, that the modeling of VehAge in Model GLM2 can be improved (top-right), the log-linear assumption for BonusMalus is not fully appropriate (bottom-middle), and the other (marginal) adjustments do not lead to visible improvements.

Conclusion. The marginal modeling used in Model GLM2 can be (slightly) improved, but it does not explain the big differences between Model GLM2 and the neural network models of Table 3. Therefore, the major weakness of Model GLM2 compared to the neural network models must come from missing interactions in the former model. Note that in this former model all interactions are of multiplicative type between the feature components. This deficiency is going to be explored next.

Base Model GAM1. For all our subsequent derivations we enhance Model GLM2 by improving the marginal modeling of the feature components VehAge and BonusMalus using a joint GAM adjustment. That is, we consider the regression function

$$
\boldsymbol{x} \mapsto \log \lambda^{\mathrm{GAM}}(\boldsymbol{x})=\langle\boldsymbol{\beta}, \boldsymbol{x}\rangle+\mathrm{ns}_{1}^{2}(\text { VehAge })+\mathrm{ns}_{2}^{2}(\text { BonusMalus })
$$

## Page 21
Figure 10: comparison of the marginals in Model GLM2 and the marginal network adjustment according to (3.7).
where the first term on the right-hand side (scalar product) is the part originating from Model GLM2, and $\mathrm{ns}_{1}^{2}: \mathbb{R} \rightarrow \mathbb{R}$ and $\mathrm{ns}_{2}^{2}: \mathbb{R} \rightarrow \mathbb{R}$ are two natural cubic splines enhancing Model GLM2 by GAM features. We fit these two natural cubic splines simultaneously using the GAM framework and we call this improvement Model GAM1. The corresponding code is given in Listing 7. On line 4 we compress the data w.r.t. the two selected feature components VehAge and BonusMalus. On lines $7-8$ we fit the natural cubic splines for these two variables using the logged working weights $\log \left(v_{i}^{\mathrm{GLM}}\right)$ as offsets, see also (3.6).

Listing 7: Model GAM1 with VehAge and BonusMalus improvements

```
library(plyr)
library(mgcv)
# data compression of the learning data set
learn.GAM <- ddply(learn, .(VehAge, BonusMalus), summarize, VolGLM=sum(VolGLM),
                                    ClaimNb=sum(ClaimNb))
# Model GAM fitting
d.gam <- gam(ClaimNb ~ s(VehAge, bs="cr") + s(BonusMalus, bs="cr"), data=learn.GAM,
                                    method="GCV.Cp", offset=log(VolGLM), family=poisson)
```

In Table 5 we present the results. We see the expected improvement in out-of-sample loss from 32.14902 (Model GLM2) to 32.07597 (Model GAM1). However, there is still a big gap compared to the neural network approaches. Note that Model GAM1 is based on multiplicative interactions that we are going to challenge next.
![Page 21 Image 1](cs3_nesting_classical_actuarial_models_into_neural_networks_assets/cs3_nesting_classical_actuarial_models_into_neural_networks_p21_img1.jpg)

## Page 22
|  | epochs | run <br> time | $\#$ <br> param. | in-sample <br> loss | out-of-sample <br> loss | average <br> frequency |
| :-- | --: | --: | --: | --: | --: | --: |
| homogeneous model |  | 0.1 s | 1 | 32.93518 | 33.86149 | $10.02 \%$ |
| Model GLM2 |  | 17 s | 48 | 31.25674 | 32.14902 | $10.01 \%$ |
| Model GAM1 |  | 1 s | $63.2^{\dagger}$ | 31.14450 | 32.07597 | $10.01 \%$ |
| Network Emb $(d=1)$ | 700 | 419 s | 719 | 30.24464 | 31.50647 | $9.90 \%$ |
| Network Emb $(d=2)$ | 600 | 365 s | 792 | 30.16513 | 31.45327 | $9.70 \%$ |
| CANN1 Emb $(d=1)$ | 200 | 115 s | 719 | 30.39966 | 31.50136 | $10.02 \%$ |
| CANN2 Emb $(d=2)$ | 200 | 117 s | 792 | 30.47557 | 31.56555 | $10.34 \%$ |

Table 5: run time, number of model parameters, in-sample and out-of-samples losses (units are in $10^{-2}$ ) of Models GLM2, GAM1, $\left(q_{1}, q_{2}, q_{3}\right)=(20,15,10)$ network with embedding layers with dimensions $d=1,2$ for the categorical feature components VehBrand and Region, Models CANN1 and CANN2 with embeddings $d=1,2$, respectively; ${ }^{\dagger}$ the number of parameters for Model GAM1 considers the 48 GLM parameters plus the effective degrees of freedom of the GAM splines being $6.6+8.6=15.2$.

# 3.5 Analyzing missing pair-wise interactions 

Completely similarly as in (3.7) we may explore missing interactions in the models considered above. As base model we choose Model GAM1 here, see Table 5. In analogy to (3.5)-(3.6), we may analyze, say, a missing (non-multiplicative) interaction between DrivAge and BonusMalus. We therefore define the following bivariate interaction (2IA) model

$$
\boldsymbol{x} \mapsto \log \lambda^{2 \mathrm{IA}}(\boldsymbol{x})=\left\langle\boldsymbol{w}^{(4)},\left(\boldsymbol{z}^{(3)} \circ \boldsymbol{z}^{(2)} \circ \boldsymbol{z}^{(1)}\right)(\text { DrivAge, BonusMalus })\right\rangle
$$

and we assume that

$$
N_{i} \stackrel{\text { ind. }}{\sim} \operatorname{Poi}\left(\lambda^{2 \mathrm{IA}}\left(\boldsymbol{x}_{i}\right) v_{i}^{\mathrm{GAM}}\right), \quad \text { with working weights } v_{i}^{\mathrm{GAM}}=v_{i} \tilde{\lambda}^{\mathrm{GAM}}(\boldsymbol{x})
$$

where $\boldsymbol{x} \mapsto \tilde{\lambda}^{\mathrm{GAM}}(\boldsymbol{x})$ is the regression function obtained from the base Model GAM1. Thus, the 2IA regression model (3.10) challenges the GAM-improved GLM2 model by allowing for pairwise interactions between DrivAge and BonusMalus. This can be interpreted as a boosting step. For this boosting step we choose a neural network of depth $K=3$ having $\left(q_{1}, q_{2}, q_{3}\right)=(20,15,10)$ hidden neurons. Categorical feature components are modeled with two-dimensional embedding layers (2.4). We fit these pair-wise boosting improvements over 1'000 gradient descent epochs on batches of size 10'000 policies.
The pair-wise results are illustrated in Figure 11. The rows provide the components Area, VehPower, VehAge, DrivAge, BonusMalus, VehBrand, VehGas and Density (in this order) and the columns provide the components VehPower, VehAge, DrivAge, BonusMalus, VehBrand, VehGas, Density and Region (in this order). Black and blue graphs show the out-of-samples losses over the 1'000 epochs, and the orange dotted lines shows the out-of-sample loss of Model GAM1. Note that the scale on the $y$-axis is the same in all plots. In blue color we identify the pairs that lead to a major decrease in loss. These are the pairs (VehPower, VehAge), (VehPower, VehBrand), (VehAge, VehBrand), (VehAge, VehGas), (DrivAge, BonusMalus). Thus, between these pairs we observe a major (non-multiplicative) interaction that should be integrated into the model. The advantage of approach (3.10) is that we do not need to specify the explicit form of these (missing) interactions, this is in contrast to the GLM and GAM approaches.

## Page 23
Figure 11: exploring pair-wise interactions: out-of-sample losses over 1'000 gradient descent epochs for all pairs of feature components, the orange dotted line shows Model GAM1 (the scale on the $y$-axis is identical in all plots).

Interaction improved GAM1 model. This leads us to the following interaction improvements of Model GAM1. We consider regression function

$$
\begin{aligned}
\boldsymbol{x} \mapsto \log \lambda^{\mathrm{GAM}+}(\boldsymbol{x})= & \left\langle\boldsymbol{w}_{1}^{(4)},\left(\boldsymbol{z}_{1}^{(3)} \circ \boldsymbol{z}_{1}^{(2)} \circ \boldsymbol{z}_{1}^{(1)}\right)(\text { VehPower, VehAge, VehBrand, VehGas })\right\rangle \\
& +\left\langle\boldsymbol{w}_{2}^{(4)},\left(\boldsymbol{z}_{2}^{(3)} \circ \boldsymbol{z}_{2}^{(2)} \circ \boldsymbol{z}_{2}^{(1)}\right)(\text { DrivAge, BonusMalus })\right\rangle
\end{aligned}
$$

where we consider two parallel deep neural networks of depth $K=3$ for the two component vectors (VehPower, VehAge, VehBrand, VehGas) and (DrivAge, BonusMalus). Moreover, we set

$$
N_{i} \stackrel{\text { ind. }}{\sim} \operatorname{Poi}\left(\lambda^{\mathrm{GAM}+}\left(\boldsymbol{x}_{i}\right) v_{i}^{\mathrm{GAM}}\right), \quad \text { with working weights } v_{i}^{\mathrm{GAM}}=v_{i} \widehat{\lambda}^{\mathrm{GAM}}(\boldsymbol{x})
$$
![Page 23 Image 1](cs3_nesting_classical_actuarial_models_into_neural_networks_assets/cs3_nesting_classical_actuarial_models_into_neural_networks_p23_img1.jpg)

## Page 24
In (3.11) we define two parallel neural networks that only interact in the last step where we concatenate them by adding up the terms. The reason for the choice is that we did not observe major interactions between the components of the two parallel networks in Figure 11.

Listing 8: R code of Model GAM+

```
d <- 2
Cont1 <- layer_input(shape = c(3), dtype = 'float32', name = 'Cont1')
VehBrand <- layer_input(shape = c(1), dtype = 'int32', name = 'Cat1')
Cont2 <- layer_input(shape = c(2), dtype = 'float32', name = 'Cont2')
LogVol <- layer_input(shape = c(1), dtype = 'float32', name = 'LogVol')
x.input <- c(Cont1, VehBrand, Cont2, LogVol)
BrEmb = VehBrand %>%
    layer_embedding(input_dim = 11, output_dim = d, input_length = 1, name = 'BrEmb') %>%
    layer_flatten(name='Br_flat')
Network1 = list(Cont1, BrEmb) %>%
    layer_concatenate(name='concate') %>%
    layer_dense(units=20, activation='tanh', name='hidden1') %>%
    layer_dense(units=15, activation='tanh', name='hidden2') %>%
    layer_dense(units=10, activation='tanh', name='hidden3') %>%
    layer_dense(units=1, activation='linear', name='Network1',
        weights=list(array(0, dim=c(10,1)), array(0, dim=c(1))))
Network2 = Cont2 %>%
    layer_dense(units=20, activation='tanh', name='hidden4') %>%
    layer_dense(units=15, activation='tanh', name='hidden5') %>%
    layer_dense(units=10, activation='tanh', name='hidden6') %>%
    layer_dense(units=1, activation='linear', name='Network2',
        weights=list(array(0, dim=c(10,1)), array(0, dim=c(1))))
Response = list(Network1, Network2, LogVol) %>%
    layer_add(name='Add') %>%
    layer_dense(units=1, activation=k_exp, name = 'Response', trainable=FALSE,
        weights=list(array(1, dim=c(1,1)), array(0, dim=c(1))))
model <- keras_model(inputs = x.input, outputs = c(Response))
```

We fit Model GAM+ given in (3.11) based on two parallel neural networks of depth $K=3$, both having $\left(q_{1}, q_{2}, q_{3}\right)=(20,15,10)$ hidden neurons. The R code is given in Listing 8. We run the gradient descent algorithm over 400 epochs on batches of size 10'000 policies. The results are presented in Table 6.
We observe excellent fitting results of Model GAM+ compared to the other neural network models, see Table 6. This illustrates that in (3.11) we capture the main interaction terms. In fact, from Figure 11 we see that the second interaction term in (3.11), based on the variables (DrivAge,BonusMalus), accounts for a decrease of out-of-sample loss from 32.07597 (Model GAM1) to roughly 31.97, see Figure 11, plot (DrivAge,BonusMalus). Therefore, the first interaction term in (3.11) must account for the residual decrease of out-of-sample loss from roughly 31.97 to 31.49574 . This closes our example.

# 4 Conclusions 

We have started our case study from a classical generalized linear model (GLM) for predicting claims frequencies. Therefore we have assumed a log-linear functional form for the regression function which leads to a multiplicative tariff structure in the feature components. Categorical

## Page 25
|  | epochs | run <br> time | $\#$ <br> param. | in-sample <br> loss | out-of-sample <br> loss | average <br> frequency |
| :-- | --: | --: | --: | --: | --: | --: |
| homogeneous model |  | 0.1 s | 1 | 32.93518 | 33.86149 | $10.02 \%$ |
| Model GLM2 |  | 17 s | 48 | 31.25674 | 32.14902 | $10.01 \%$ |
| Model GAM1 |  | 1 s | $63.2^{\dagger}$ | 31.14450 | 32.07597 | $10.01 \%$ |
| Model GAM+ | 400 | 278 s | $1^{\prime} 174^{\ddagger}$ | 30.54186 | 31.49574 | $10.33 \%$ |
| Network Emb $(d=1)$ | 700 | 419 s | 719 | 30.24464 | 31.50647 | $9.90 \%$ |
| Network Emb $(d=2)$ | 600 | 365 s | 792 | 30.16513 | 31.45327 | $9.70 \%$ |
| CANN1 Emb $(d=1)$ | 200 | 115 s | 719 | 30.39966 | 31.50136 | $10.02 \%$ |
| CANN2 Emb $(d=2)$ | 200 | 117 s | 792 | 30.47557 | 31.56555 | $10.34 \%$ |

Table 6: run time, number of model parameters, in-sample and out-of-samples losses (units are in $10^{-2}$ ) of Models GLM2, GAM1, $\left(q_{1}, q_{2}, q_{3}\right)=(20,15,10)$ network with embedding layers with dimensions $d=1,2$ for the categorical feature components VehBrand and Region, Models CANN1 and CANN2 with embeddings $d=1,2$, respectively; ${ }^{\dagger}$ the number of parameters for Model GAM1 considers the 48 GLM parameters plus the effective degrees of freedom of the GAM splines being $6.6+8.6=15.2 ;^{\ddagger}$ only accounts for the network parameters in (3.11) and not for the parameters which have been used to receive the working weights $v_{i}^{\mathrm{GAM}}$ from Model GAM1.
variables have been considered using dummy coding.
In a second step, this GLM has been enhanced by improving the log-linear functional forms in the regression function, if necessary. This has been done within the framework of generalized additive models (GAMs) using natural cubic splines.
In a third step, the resulting model of the previous two steps has been embedded (nested) into a bigger model which additionally considers neural network features. This embedding results in the combined actuarial neural network (CANN) approach. Thereby the neural network architecture is used to boost the GAM improved GLM.
During this third step, we have also learned that embedding layers can lead to a more efficient treatment of categorical variables compared to dummy coding and one-hot encoding.
In the last step, we have used the CANN approach to systematically find missing interactions in the GAM improved GLM regression function. These missing interactions are of nonmultiplicative type because the GAM-GLM approach considers multiplicative interactions in the regression function. In our analysis we have been able to explicitly find all these missing interactions. These steps lead to a systematic use of neural networks, in particular, they are systematically used to identify weaknesses of existing regression models.

# References 

[1] Bengio, Y., Schwenk, H., Senécal, J.-S., Morin, F., Gauvain, J.-L. (2006). Neural probabilistic language models. In: Innovations in Machine Learning. Studies in Fuzziness and Soft Computing, Vol. 194. Springer, 137-186.
[2] CASdatasets Package Vignette (2016). Reference Manual, May 28, 2016. Version 1.0-6. Available from http://cas.uqam.ca.
[3] Charpentier, A. (2015). Computational Actuarial Science with R. CRC Press.

## Page 26
[4] Ferrario, A., Noll, A., Wüthrich, M.V. (2018). Insights from inside neural networks. SSRN Manuscript ID 3226852. Version November 14, 2018.
[5] Gabrielli, A., Richman, R., Wüthrich, M.V. (2018). Neural network embedding of the over-dispersed Poisson reserving model. SSRN Manuscript ID 3288454. Version November 21, 2018.
[6] Goodfellow, I., Bengio, Y., Courville, A. (2016). Deep Learning. MIT Press, http://www.deeplearningbook.org
[7] He, K., Zhang, X., Ren, S., Sun, J. (2015). Deep residual learning for image recognition. CoRR, abs/1512.03385.
[8] Huang, G., Liu, Z., Weinberger, K.Q. (2016). Densely connected convolutional networks. CoRR, abs/1608.06993.
[9] Marra, G., Wood, S.N., (2011). Practical variable selection for generalized additive models. Computational Statistics and Data Analysis 55, 2372-2387.
[10] Noll, A., Salzmann, R., Wüthrich, M.V. (2018). Case study: French motor third-party liability claims. SSRN Manuscript ID 3164764. Version November 8, 2018.
[11] Ohlsson, E., Johansson, B. (2010). Non-Life Insurance Pricing with Generalized Linear Models. Springer.
[12] Richman, R. (2018). AI in actuarial science. SSRN Manuscript, ID 3218082, Version August 20, 2018.
[13] Richman, R., Wüthrich, M.V. (2018). A neural network extension of the Lee-Carter model to multiple populations. SSRN Manuscript, ID 3270877, Version October 22, 2018.
[14] Sahlgren, M. (2015). A brief history of word embeddings. https://www.linkedin.com/pulse/brief-history-word-embeddings-some-clarifications-magnus-sahlgren/
[15] Wood, S.N. (2017). Generalized Additive Models: An Introduction with R. 2nd edition. Chapman and Hall/CRC.
[16] Wüthrich, M.V., Buser, C. (2016). Data Analytics for Non-Life Insurance Pricing. SSRN Manuscript ID 2870308. Version October 24, 2017.
[17] Wüthrich, M.V., Merz, M. (2019). Editorial: Yes, we CANN! ASTIN Bulletin 49/1.

## Page 27
# Listing 9: Model CANN1 architecture 

```
ContGLM <- layer_input(shape = c(4), dtype = 'float32', name = 'ContGLM')
VehPowerGLM <- layer_input(shape = c(1), dtype = 'int32', name = 'VehPowerGLM')
VehAgeGLM <- layer_input(shape = c(1), dtype = 'int32', name = 'VehAgeGLM')
VehBrand <- layer_input(shape = c(1), dtype = 'int32', name = 'VehBrand')
Region <- layer_input(shape = c(1), dtype = 'int32', name = 'Region')
5}\mathrm{ DriveAgeGLM <- layer_input(shape = c(5), dtype = 'float32', name = 'DrivAgeGLM')
7}\mathrm{ ContNN <- layer_input(shape = c(3), dtype = 'float32', name = 'ContNN')
8 LogExposure <- layer_input(shape = c(1), dtype = 'float32', name = 'LogExposure')
9 x.input <- c(ContGLM,DrivAgeGLM, VehPowerGLM, VehAgeGLM, VehBrand, Region, ContNN, LogExposure)
10 #
11 VehPowerGLM_embed = VehPowerGLM %>%
12 layer_embedding(input_dim = length(beta.VehPower), output_dim = 1, trainable=FALSE,
13 input_length = 1, name = 'VehPowerGLM_embed',
14 weights=list(array(beta.VehPower, dim=c(length(beta.VehPower),1)))) %>%
15 layer_flatten(name='VehPowerGLM_flat')
16
17 VehAgeGLM_embed = VehAgeGLM %>%
18 layer_embedding(input_dim = length(beta.VehAge), output_dim = 1, trainable=FALSE,
19 input_length = 1, name = 'VehAgeGLM_embed',
20 weights=list(array(beta.VehAge, dim=c(length(beta.VehAge),1)))) %>%
21 layer_flatten(name='VehAgeGLM_flat')
22
23 VehBrand_embed = VehBrand %>%
24 layer_embedding(input_dim = length(beta.VehBrand), output_dim = 1, trainable=FALSE,
25 input_length = 1, name = 'VehBrand_embed',
26 weights=list(array(beta.VehBrand, dim=c(length(beta.VehBrand),1)))) %>%
27 layer_flatten(name='VehBrand_flat')
28
29 Region_embed = Region %>%
30 layer_embedding(input_dim = length(beta.Region), output_dim = 1, trainable=FALSE,
31 input_length = 1, name = 'Region_embed',
32 weights=list(array(beta.Region, dim=c(length(beta.Region),1)))) %>%
33 layer_flatten(name='Region_flat')
34 #
35 GLMNetwork = list(ContGLM, DrivAgeGLM, VehPowerGLM_embed, VehAgeGLM_embed,
36 VehBrand_embed, Region_embed) %>%
37 layer_concatenate() %>%
38 layer_dense(units=1, activation='linear', name='GLMNetwork', trainable=FALSE,
39 weights=list(array(c(beta.continuous, beta.DrivAge, rep(1,4)), dim=c(13,1)),
40 array(beta.0, dim=c(1))))
41
42 NNetwork = list(ContGLM, ContNN, VehBrand_embed, Region_embed) %>%
43 layer_dense(units=20, activation='tanh', name='hidden1') %>%
44 layer_dense(units=15, activation='tanh', name='hidden2') %>%
45 layer_dense(units=10, activation='tanh', name='hidden3') %>%
46 layer_dense(units=1, activation='linear', name='NNetwork',
47 weights=list(array(0, dim=c(10,1)), array(0, dim=c(1))))
48
49 CANNoutput = list(GLMNetwork, NNetwork, LogExposure) %>%
50 layer_add() %>%
51 # 
52 model <- keras_model(inputs = x.input, outputs = c(CANNoutput))
```