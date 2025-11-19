_Note: Source document was split into 20 OCR chunks (pages 1-14, pages 15-27, pages 28-42, pages 43-56, pages 57-71, pages 72-85, pages 86-99, pages 100-112, pages 113-126, pages 127-139, pages 140-152, pages 153-168, pages 169-180, pages 181-195, pages 196-210, pages 211-227, pages 228-241, pages 242-254, pages 255-268, pages 269-271) to stay within token limits._

# 20250303 AI Tools for Actuaries

## Page 1
# AI Tools for Actuaries 

- Course Material -


## Authors:

Mario V. Wüthrich (ETH Zurich)
Ronald Richman (InSUREAI)
Benjamin Avanzi (The University of Melbourne)
Mathias Lindholm (Stockholm University)
Michael Mayer (la Mobilière)
Jürg Schelldorfer (Swiss Re)
Salvatore Scognamiglio (University of Naples Parthenope)

## Page 2
VERSION M ARCH 3, 2025, @AI TOOLS FOR ACTUARIES

## Page 3
# Preface and Terms of Use 

## About these Lecture Notes

There are many different initiatives around the globe that aim at upskilling the actuarial profession in data science and AI related subjects. The aim of these notes is to give a comprehensive set of lecture notes and teaching material to this effect. To help to define its scope, we have taken the proposal of the Actuarial Association of Europe (AAE) Education Committee, called 'CPD in Data Science', ${ }^{1}$ which is a strategy paper that proposes a syllabus for actuaries in data science and AI related topics. Based on this strategy paper we have developed our own view on what the actuarial profession should be familiar with in this field, and these lecture notes are the result of this process. Since data science, machine learning and AI are vastly evolving fields, we expect that the emphasis given to the different subjects in this field will change over time, and similarly these lecture notes should evolve.
These lecture notes only contain a limited number of (explicit) examples. In parallel we develop comprehensive notebooks that provide explicit data examples and code to the theory presented in these notes; for the notebooks see
notebook-insert-link

## Terms of Use

These lecture notes are an ongoing project which is continuously revised, updated and extended. We highly appreciate any comments that readers may have to improve these notes. The use of these lecture notes is subject to the following rules:

- These notes are provided to reusers to distribute, remix, adapt, and build upon the material in any medium or format for noncommercial purposes only, and only so long as attribution and credit is given to the original authors and source, and if you indicate if changes were made. This aligns with the Creative Commons Attribution 4.0 International License CC BY-NC.
- The authors may update the manuscript or withdraw it at any time. There is no right of availability of any (old) version of these notes. The authors may also change these terms of use at any time.
- The authors disclaim all warranties, including but not limited to the use of the contents of these notes and the related notebooks and statistical code. When using these notes, notebooks and statistical code, you fully agree to this.

[^0]
[^0]:    ${ }^{1}$ https://actuary.eu/about-the-aae/continuous-professional-development/

## Page 4
4

Version March 3, 2025, @AI Tools for Actuaries

## Page 5
# Contents 

1 Introduction and prerequisites ..... 11
1.1 Introduction ..... 11
1.2 Notation in probability theory ..... 12
1.2.1 Probability distribution functions ..... 13
1.2.2 Expected values ..... 14
1.2.3 Covariates and regression functions ..... 14
1.3 Generalized linear models - in short ..... 15
1.4 Strictly consistent loss functions ..... 17
1.4.1 Introduction ..... 17
1.4.2 Strictly consistent loss functions for mean estimation ..... 18
1.4.3 Regression fitting on finite samples ..... 19
1.5 Model validation and model selection ..... 22
1.5.1 Out-of-sample (generalization) loss ..... 23
1.5.2 Cross-validation ..... 24
1.5.3 Akaike's information criterion for model selection ..... 25
1.5.4 Bootstrap and out-of-bag validation ..... 26
1.5.5 Summary on model validation and model selection ..... 28
2 Regression models ..... 31
2.1 Exponential dispersion family ..... 32
2.1.1 Introduction of the exponential dispersion family ..... 32
2.1.2 Cumulant function, mean and variance function ..... 32
2.1.3 Maximum likelihood estimation and deviance loss ..... 34
2.2 Regression models ..... 35
2.3 Covariate pre-processing ..... 37
2.3.1 Notation ..... 37
2.3.2 Categorical covariates ..... 38
2.3.3 Continuous covariates ..... 41
2.4 Regularization and sparsity ..... 42
2.4.1 Introduction and overview ..... 42
2.4.2 Regularization ..... 43
2.4.3 Ridge regularization ..... 44
2.4.4 LASSO regularization ..... 44
2.4.5 Best-subset selection regularization ..... 45
2.4.6 Elastic net regularization ..... 45

## Page 6
2.4.7 Group and fused LASSO regularizations ..... 46
2.5 Outlook ..... 47
3 Generalized linear models ..... 49
3.1 Generalized linear model regressions ..... 49
3.1.1 Generalized linear model regression functions ..... 49
3.1.2 Canonical link ..... 52
3.2 Generalized linear model fitting ..... 53
3.2.1 MLE via log-likelihoods ..... 53
3.2.2 MLE via deviance loss functions ..... 53
3.2.3 Numerical solution of the GLM problem ..... 54
3.3 Likelihood-ratio test ..... 55
3.3.1 Introduction ..... 55
3.3.2 Lab: a real data example ..... 55
3.3.3 Likelihood ratio test and Wald test ..... 56
4 Interlude ..... 63
4.1 Unbiasedness and calibration ..... 63
4.1.1 Statistical biases ..... 63
4.1.2 The balance property ..... 65
4.1.3 Auto-calibration ..... 66
4.2 General purpose non-parametric regressions ..... 68
4.2.1 Local regression ..... 68
4.2.2 Isotonic regression ..... 70
4.3 Model analysis tools ..... 73
4.3.1 Gini score ..... 73
4.3.2 Murphy's score decomposition ..... 75
5 Feed-forward neural networks ..... 77
5.1 Feed-forward neural network architecture ..... 78
5.1.1 Feature extractor and readout ..... 78
5.1.2 Activation function ..... 79
5.1.3 Feed-forward neural network layer ..... 80
5.1.4 Feed-forward neural network architecture ..... 81
5.2 Universality theorems ..... 82
5.3 Network fitting with gradient descent ..... 83
5.3.1 The standard gradient descent method ..... 84
5.3.2 Covariate pre-processing ..... 85
5.3.3 Gradient calculation via back-propagation ..... 86
5.3.4 Learning rate and higher order Taylor approximations ..... 86
5.3.5 Early stopping rule ..... 87
5.3.6 Regularization and drop-out ..... 90
5.3.7 Stochastic gradient descent ..... 91
5.3.8 Summarizing feed-forward neural networks and their training ..... 92
5.4 Nagging ..... 93

## Page 7
5.4.1 Aggregating ..... 94
5.4.2 Network ensembling ..... 94
5.5 Summary on feed-forward neural networks ..... 96
5.6 Combing a GLM and a neural network ..... 97
5.7 LocalGLMnet ..... 99
5.8 Outlook: Kolmogorov-Arnold networks ..... 101
6 Regression trees and random forests ..... 103
6.1 Regression trees ..... 103
6.2 Bagging ..... 107
6.3 Random forests ..... 108
7 Gradient boosting machines ..... 111
7.1 (Generalized additive) boosting ..... 111
7.2 Gradient boosting machines ..... 114
7.2.1 Functional gradient boosting ..... 114
7.2.2 Tree-based gradient boosting machines ..... 117
7.3 Interpretability measures and variable importance ..... 119
7.4 State-of-the-art gradient boosting machines ..... 120
8 Deep learning for tensor and unstructured data ..... 123
8.1 Introduction ..... 123
8.2 Tokenization and the art of entity embedding ..... 125
8.2.1 Tensors ..... 125
8.2.2 (Supervised) entity embedding ..... 125
8.2.3 (Unsupervised) word embedding ..... 127
8.2.4 Summary of Section 8.2 ..... 135
8.3 Convolutional neural networks ..... 135
8.3.1 1D convolutional neural networks ..... 136
8.3.2 2D convolutional neural networks ..... 139
8.3.3 Deep convolutional neural networks ..... 141
8.3.4 Locally-connected networks ..... 142
8.3.5 Pooling layers ..... 143
8.3.6 Padding ..... 144
8.3.7 Conclusions and flatten layers ..... 145
8.4 Recurrent neural networks ..... 145
8.4.1 Plain-vanilla recurrent neural networks ..... 146
8.4.2 Long short-term memory networks ..... 147
8.4.3 Gated recurrent unit networks ..... 149
8.4.4 Deep recurrent neural networks and conclusion ..... 150
8.5 Transformers ..... 151
8.5.1 Basic components of transformers ..... 151
8.5.2 Transformers for sequential data ..... 154
8.5.3 Transformers for tabular data ..... 157
8.5.4 The credibility transformer ..... 158

## Page 8
9 Unsupervised learning ..... 165
9.1 Introduction ..... 165
9.2 Dimension reduction methods ..... 166
9.2.1 Standardization ..... 167
9.2.2 Auto-encoders ..... 168
9.2.3 Principal component analysis ..... 170
9.2.4 Bottleneck neural network ..... 173
9.2.5 Kernel principal component analysis ..... 175
9.3 Clustering methods ..... 179
9.3.1 Hierarchical clustering ..... 181
9.3.2 $K$-means and $K$-medoids clusterings ..... 184
9.3.3 Clustering using Gaussian mixture models ..... 187
9.3.4 Density-based clustering ..... 188
9.4 Low-dimensional visualization methods ..... 189
10 Generative modeling ..... 193
10.1 Introduction ..... 193
10.2 Variational auto-encoders ..... 196
10.2.1 Introduction and motivation ..... 196
10.2.2 Variational auto-encoder model architecture ..... 196
10.2.3 Variational objective: the evidence lower bound ..... 197
10.2.4 Reparameterization trick and training ..... 198
10.2.5 Discussion ..... 199
10.3 Other approaches related to latent factor models ..... 199
10.3.1 Generative adversarial networks ..... 200
10.3.2 Diffusion models ..... 201
10.4 Decoder transformer models ..... 203
10.4.1 Introduction and motivation ..... 203
10.4.2 Architecture overview ..... 203
10.4.3 Self-attention with causal masking ..... 204
10.4.4 Softmax outputs and probability calibration ..... 205
10.4.5 Training and inference ..... 206
10.5 Conclusion on generative models ..... 207
10.6 Large language models ..... 209
10.6.1 From auto-regressive transformers to LLMs ..... 209
10.6.2 Foundation models and pretraining ..... 213
10.6.3 Use cases of large language models ..... 213
10.6.4 Fine-tuning with reinforcement learning from human feedback ..... 213
10.6.5 Parameter-efficient fine-tuning ..... 215
10.6.6 Prompting ..... 216
10.6.7 Building and refining reasoning models for LLMs ..... 219
10.6.8 LLMs as a judge and self-consistency mechanisms ..... 221
10.6.9 Responsible use of large language models ..... 223
10.6.10 Sparse auto-encoders and mechanistic interpretability ..... 225
10.6.11 Summary ..... 228

## Page 9
10.7 Conclusion: From empirical scaling to broad AI ..... 228
11 Reinforcement learning ..... 229
11.1 Introduction ..... 229
11.2 Multi-armed bandit problem ..... 230
11.3 Incremental learning ..... 234
11.4 Tabular learning problems ..... 235
11.5 Known environment's dynamics ..... 237
11.5.1 Policy iteration ..... 238
11.5.2 Value iteration ..... 239
11.6 Unknown environment's dynamics: Monte Carlo ..... 239
11.7 Temporal difference learning ..... 243
11.7.1 SARSA on-policy control ..... 244
11.7.2 $Q$-learning off-policy control ..... 245
11.8 Beyond tabular learning ..... 248
11.9 Actor-critic reinforcement learning algorithms ..... 251
11.9.1 Policy gradient control ..... 251
11.9.2 Actor-critic reinforcement learning ..... 252
12 Outlook ..... 257

## Page 10
Version March 3, 2025, @AI Tools for Actuaries

## Page 11
# Chapter 1 

## Introduction and prerequisites

### 1.1 Introduction

The actuarial profession is rapidly evolving, with machine learning (ML) and artificial intelligence (AI) tools becoming increasingly incorporated into practical actuarial methodology. This book explains the evolution of AI tools from more familiar regression models all the way up to generative AI systems, to equip actuaries with technical knowledge about these tools and to enable actuaries to apply these within their work.
Why do we believe that these AI tools represent such an important advance that they are worthy of a book length analysis? As we explain next, the methodology underlying modern AI tools is surprisingly similar to the methodology of actuarial science, and the advances in AI tools therefore can be applied easily and with great effect within the work that actuaries do.
Actuaries, through their education within and study of actuarial science, are equipped with tools from many disciplines to solve the challenges they encounter in their work, which often focuses on managing risk within financial institutions. These tools are, on the one hand, drawn from a variety of other disciplines such as statistics, finance, demography and economics, and, on the other hand, also includes specialized techniques developed within the field of actuarial science. Examples of the former are the valuation of options and guarantees using risk-neutral techniques and projection of mortality using the Lee-Carter model [132], and, of the latter, is the chain-ladder technique, used to predict outstanding claims liabilities. Combining these tools with expert knowledge of the particular industries in which they work allows actuaries to build models to provide insight and analysis of a variety of important problems within these industries.
Actuarial modeling often takes the approach of approximating and predicting empirically observed phenomena without spending too much time building full theories explaining these observations in detail; in this sense, actuarial science is different from economics or physics which use empirical phenomena to build theories. Of course, actuarial science is grounded in the study of rigorous mathematics, probability theory and statistics and, moreover, has developed deep theoretical frameworks for topics such as credibility theory. Nonetheless, the practical application of actuarial modeling is to make predictions and not to develop theories explaining the observations. Take, for example, an actuary who is tasked with estimating the required reserve for the outstanding liabilities

## Page 12
in a non-life insurer. Using datasets comprised of observations of past delays in claims emergence, he/she will use tools to estimate factors which predict the amount of future claim emergence and apply these to recent cohorts of reported claims. While the actuary will understand what produces claims delays and how these underlying causes relate to the claims development factors, nonetheless, the analysis is performed from an empirical standpoint.
Remarkably, exactly this approach of building models to approximate and predict empirical phenomena underlies the highly successful field of ML and AI, which, has, in recent years, built models capable of solving tasks in computer vision, natural language processing, generative modeling and, which more recently, is beginning to tackle the problem of building more generally intelligent AI systems. At the risk of oversimplifying, many approaches within ML and AI work by compiling a dataset relevant to the problem at hand and then specifying a class of models that is well-suited to the type of data. After calibrating the parameters of the model appropriately, predictions are then be made, if needed, can be interpreted. At the largest scale, so-called foundation models are trained on significant proportions of the text available on the Internet; this training process involves making predictions of the next expected word in a sentence, given some previous context about what the sentence is discussing. Despite the seemingly simple task that these models are given, nonetheless, by learning to approximate the empirical (conditional) distribution of words within natural language, these foundation models are now becoming capable of providing useful output across a wide range of applications from writing computer code to editing documents.
Of course, the scale of data involved in building these large-scale AI models, and the complexity of the models applied, can be different from typical actuarial applications. Nonetheless, borrowing, modifying and integrating these new tools within actuarial science represents - in our view - a remarkable opportunity to enhance the practice of our discipline; making this task much easier is the similar approach to building models that is common within both disciplines.
In this book, we aim to equip actuaries with both a practical and a theoretically sound understanding of these powerful AI tools that is specifically tailored to the unique challenges and demands of the actuarial profession. The book will journey through the landscape of AI tools, starting with familiar regression models as a foundation and then introducing more advanced techniques, including neural networks, deep learning architectures, and the emerging field of generative AI. We will emphasize statistical rigor, model validation, and careful consideration of data limitations that are already core competencies of actuarial science and show how these apply equally to AI tools, allowing these to be integrated easily into the existing actuarial toolkit.

# 1.2 Notation in probability theory 

An introduction to probability theory and statistics is part of the core syllabus of actuarial science, and its contents is taught in every introductory course on probability theory. In this section, we summarize some of the probability concepts that will be necessary to be able to formalize the following chapters and the methods presented in these notes.

## Page 13
# 1.2.1 Probability distribution functions 

We generally work on a sufficiently rich probability space $(\Omega, \mathcal{F}, \mathbb{P})$ with sample space $\Omega$, $\sigma$-field $\mathcal{F}$, and probability function $\mathbb{P}: \mathcal{F} \rightarrow[0,1]$ that assigns the probabilities $\mathbb{P}(A)$ to the events $A \in \mathcal{F}$. This probability space $(\Omega, \mathcal{F}, \mathbb{P})$ supports random variables $Y$ which are real-valued measurable functions on this probability space. Random variables can be characterized by probability distribution functions (distributions in short) $F: \mathbb{R} \rightarrow[0,1]$ given by

$$
F(y):=\mathbb{P}[Y \leq y] \quad \text { for } y \in \mathbb{R}
$$

This describes the probability that the random variable $Y$ takes a value of less or equal to $y \in \mathbb{R}$. We write $Y \sim F$ for a random variable $Y$ having distribution $F$. In most practical applications, these distributions are unknown, and the general aim in statistics and data science is to infer the correct distribution from observed realizations of the random variables.
There are two main types of distributions. There are discrete distributions and absolutely continuous ones. Discrete distributions are step functions having countably many steps $\left(y_{j}\right)_{j \geq 1} \subset \mathbb{R}$, allowing for positive probability masses $\left(p_{j}\right)_{j \geq 1}$ in these steps. That is,

$$
p_{j}=\mathbb{P}\left[Y=y_{j}\right]>0 \quad \text { with } \quad \sum_{j \geq 1} p_{j}=1
$$

Figure 1.1 (lhs) shows a discrete distribution with finitely many steps in $\left(y_{j}\right)_{j=1}^{J}, J=8$. Typical examples with discrete distributions are count random variables $Y$ taking values in the integers $\left(y_{j}\right)_{j \geq 1} \subseteq \mathbb{N}_{0}$. In insurance, count random variables are used to model the numbers of claims; examples are the binomial distribution, the Poisson distribution and the negative binomial distribution. We discuss these distributions below.

Figure 1.1: (lhs) Discrete distribution with finitely many steps in $\left(y_{j}\right)_{j=1}^{J}, J=8$, (rhs) density of an absolutely continuous distribution.

Absolutely continuous distributions have a (probability) density representation, $f \geq 0$,
![Page 13 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p13_img1.jpg)

## Page 14
w.r.t. the Lebesgue measure, providing us with

$$
F(y)=\int_{-\infty}^{y} f(z) \mathrm{d} z
$$

for all $y \in \mathbb{R}$. Typical examples in actuarial science are the gamma or the log-normal distributions which are used to model positive claim sizes. Figure 1.1 (rhs) shows a (gamma) density $y \mapsto f(y)$ with the area of the blue region being equal to one.

# 1.2.2 Expected values 

Random variables are used to describe (future) outcomes of experiments (insurance claims) that cannot be perfectly predicted. E.g., will a car driver have an accident over the next calendar year and, if yes, how big will his insurance claim be? Such questions are modeled by random variables $Y$, which are used to describe the quantitative outcomes stemming from uncertain events. For forecasting, one typically uses the expected value (mean) of $Y \sim F$ given by the Riemann-Stieltjes integral

$$
\mathbb{E}[Y]=\int_{\mathbb{R}} y \mathrm{~d} F(y)
$$

subject to existence. In the discrete distribution case, this expected value is equal to

$$
\mathbb{E}[Y]=\sum_{j \geq 1} y_{j} p_{j}
$$

and, in the absolutely continuous case, we compute the integral

$$
\mathbb{E}[Y]=\int_{\mathbb{R}} y f(y) \mathrm{d} y
$$

Remark 1.1. The expected value (1.1) is generally not the most likely outcome, e.g., if we have skewed densities, as in Figure 1.1 (rhs), the expected value, the mode and the median will generally differ. The expected value corresponds to the average outcome of the uncertain (claim) event. In insurance, one typically assumes that one has a large insurance portfolio of independent and identically distributed (i.i.d.) claims $\left(Y_{i}\right)_{i \geq 1}$. The selection of the mean $\mathbb{E}\left[Y_{1}\right]$ is then justified by the fact that the law of large numbers implies that the average claim $n^{-1} \sum_{i=1}^{n} Y_{i}$ converges to the expected value $\mathbb{E}\left[Y_{1}\right]$, a.s., as the sample size increases $n \rightarrow \infty$. One can also view the mean $\mathbb{E}\left[Y_{1}\right]$ as the value that minimizes the expected quadratic difference between our forecast and the actual outcome of the random event, thus, on average it provides the most accurate prediction w.r.t. the expected quadratic difference; this and similar statements are going to be discussed further in Section 1.4, below, especially, we refer to Remarks 1.4.

### 1.2.3 Covariates and regression functions

For forecasting a random variable $Y$, there is often additional information available in the form of covariates $\boldsymbol{X}$ (also called features, independent variables or explanatory variables). We assume that covariates $\boldsymbol{X}=\left(X_{1}, \ldots, X_{q}\right)^{\top}$ are $q$-dimensional real-valued random vectors (or realizations of these random vectors); pre-processing of categorical covariates is going to be discussed in Section 2.3, below.

## Page 15
When we write $(Y, \boldsymbol{X}) \sim \mathbb{P}$ in an actuarial context, we describe the random selection of an insurance policy with covariates $\boldsymbol{X}$ from a population (portfolio) distribution $\mathbb{P}$, and the resulting insurance claim (response) $Y$ should be understood conditionally, given the covariates (insurance policy features) $\boldsymbol{X}$, that is,

$$
\left.Y\right|_{\boldsymbol{X}} \sim F(\cdot \mid \boldsymbol{X})
$$

for $F(\cdot \mid \boldsymbol{X})$ being a distribution depending on (varies with) the covariates $\boldsymbol{X}$, e.g., $\boldsymbol{X}$ may describe a translation of the expected value relative to a base case.

Having covariate information $\boldsymbol{X}$ about the insurance claim $Y$ specifies the following regression consideration. Denote by $\mathcal{X} \subseteq \mathbb{R}^{q}$ the support of the covariates $\boldsymbol{X}$; the set $\mathcal{X}$ is called covariate space or feature space. The general aim in regression modeling is to find the (true) regression function $\mu^{*}:\mathcal{X} \rightarrow \mathbb{R}$ that describes the conditional expectation of the response variable $Y$ having covariate $\boldsymbol{X}$, that is,

$$
\mu^{*}(\boldsymbol{X}):=\mathbb{E}[Y \mid \boldsymbol{X}]
$$

This regression function can be determined (estimated) non-parametrically, e.g., we are going to discuss regression trees, gradient boosting machines (GBMs) and isotonic regressions, below, or we are going to use parametric regression models, such as generalized linear models (GLMs) or neural network regression architectures to find (approximate) this true regression function $\mu^{*}$.

Generally speaking, $\mu^{*}(\boldsymbol{X})$ is called best-estimate because it is the most accurate prediction of $Y$, given $\boldsymbol{X}$, w.r.t. the mean squared error (MSE). It is also called pure risk premium or actuarial premium because it does not include any safety loadings, nor does it rely on any commercial considerations.

# 1.3 Generalized linear models - in short 

To be able to better illustrate the following sections, we briefly introduce a specific GLM in this section. We have decided for a log-link GLM because actuaries are very familiar with this GLM; the general theory of GLMs is going to be discussed in Chapter 3, below.

The main problem in most applications is that the true regression function $\mu^{*}$ in (1.2) is unknown, and we have only observed a finite sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$ from that model.

Goal: Infer the (true) regression function $\mu^{*}$ from this finite sample $\mathcal{L}$.

One way to estimate the unknown (true) regression function $\mu^{*}$ is to assume that it takes a specific functional form. Assuming GLMs with log-link implies that we consider the regression functions $\mu_{\vartheta}: \mathcal{X} \rightarrow \mathbb{R}$ of type

$$
\boldsymbol{X} \mapsto \log \left(\mu_{\vartheta}(\boldsymbol{X})\right)=\vartheta_{0}+\sum_{j=1}^{q} \vartheta_{j} X_{j}
$$

## Page 16
for regression parameters $\vartheta \in \mathbb{R}^{q+1} \cdot{ }^{1}$ If we bring the log-link to the other side, we receive the equivalent formulation

$$
\boldsymbol{X} \mapsto \mu_{\vartheta}(\boldsymbol{X})=\exp \left(\vartheta_{0}+\sum_{j=1}^{q} \vartheta_{j} X_{j}\right)
$$

This gives us a parametrized family

$$
\mathcal{M}=\left\{\mu_{\vartheta}\right\}_{\vartheta}
$$

of candidates to approximate the true regression function $\mu^{*}$.
To find the best candidate $\mu_{\vartheta} \in \mathcal{M}$ for $\mu^{*}$, one typically chooses an objective function to select the best parameter (candidate) $\vartheta \in \mathbb{R}^{q+1}$ for the given observed sample $\mathcal{L}$. For this, select a loss function

$$
L: \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}, \quad(y, m) \mapsto L(y, m)
$$

in this loss function, $y$ plays the role of the outcome of $Y$, and $m$ plays the role of the mean of $Y$. The loss function $L$ is then used to assess the difference between $y$ and $m$; we are going to discuss the required properties of this loss function in Section 1.4, below, to make this a sensible model selection tool. This then motivates to solve the following optimization problem

$$
\widehat{\vartheta}=\underset{\vartheta \in \mathbb{R}^{q+1}}{\arg \min } \sum_{i=1}^{n} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)
$$

supposed there exists a unique solution. Thus, we try to minimize the loss between $Y_{i}$ and (its prediction) $\mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)$ for a suitable loss function $L$.

The solution $\mu_{\widehat{\vartheta}}$ from (1.6) is the best candidate in $\mathcal{M}$ w.r.t. the selected loss function $L$ and for given observations $\mathcal{L}$ generated by $\mu^{*}$. In this sense, we do not compare the candidates $\mu_{\vartheta}$ to the unknown $\mu^{*}$, but rather to the data $\left(Y_{i}, \boldsymbol{X}_{i}\right)$ generated by $\mu^{*}$.

Example 1.2 (Gaussian log-link GLM). A common example for the loss function is the square loss function $L(y, m)=(y-m)^{2}$. The previous optimization problem (1.6) then reads as

$$
\begin{aligned}
\widehat{\vartheta} & =\underset{\vartheta \in \mathbb{R}^{q+1}}{\arg \min } \sum_{i=1}^{n}\left(Y_{i}-\mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)^{2} \\
& =\underset{\vartheta \in \mathbb{R}^{q+1}}{\arg \min } \sum_{i=1}^{n}\left(Y_{i}-\exp \left(\vartheta_{0}+\sum_{j=1}^{q} \vartheta_{j} X_{j}\right)\right)^{2}
\end{aligned}
$$

and we obtain the estimated regression function $\mu_{\widehat{\vartheta}}$ to approximate $\mu^{*}$. We call the square loss function approach (1.7) the Gaussian log-link GLM, and the reason for this name will become clear in (1.11), below.

[^0]
[^0]:    ${ }^{1}$ We generally do not use boldface notation for $\vartheta$, even if $\vartheta$ is a real-valued vector. The reason for this is that we would like to understand $\vartheta$ generically as the model parameter, which can be a real-valued vector, but which could also be a different object that parametrizes a model.

## Page 17
The main question is whether this is a sensible model estimation technique?

- First, clearly, the true model $\mu^{*}$ should be 'close' to the selected model class $\mathcal{M}$, otherwise it is impossible to identify a model in $\mathcal{M}$ being similar to $\mu^{*}$. E.g., the GLM has a linear structure (1.3) which may not be suitable in some problems, and this requires to select other regression function classes.
- Second, is the selected loss function $L$ sensible to find a good candidate model $\mu_{\widehat{\mathcal{J}}} \in \mathcal{M}$ by solving (1.6)? We discuss this in the next Section 1.4, and we also argue why the square loss function (1.7) is not always the best choice on finite samples.


# 1.4 Strictly consistent loss functions 

### 1.4.1 Introduction

Finding good predictive models and regression functions for (1.2) crucially depends on model fitting, model selection and forecast evaluation. These are core topics in mathematical statistics, and there is a broad literature and distinguished theory behind finding good predictive models. Some key references in mathematical statistics on these topics are Gneiting-Raftery [78] and Gneiting [77]. We give a brief introduction and present the main tools that are relevant for our purposes.

Broadly speaking, model fitting in an algorithmic world is understood as minimizing some loss function (objective function) on given observations; for an example see (1.6). The result is a predictive model, but is this predictive model fit for its purpose? One may argue that the specific choices of the potential models and the objective function do not matter too much, because having an almost infinite amount of data, we will find the ground truth anyway. This argumentation is often used in the machine learning community. (1) It is based on the assumption that one has almost infinite resources of observations. (2) Implicitly, it is often considered in classification problems. We argue why actuarial problems are generally different.
(1) In many situations one does not have unlimited data resources in actuarial problems. E.g., for a certain insurance product we may only have very few claims.
(2) In classification problems, one estimates probabilities in the unit interval $(0,1)$, which is a nice and bounded space. Insurance claims can be heavy-tailed, and very few large claims can heavily distort the fitting procedure on finite samples. Therefore, the selection of the loss function needs special care.

For these reasons, one has to carefully analyze the choices of the potential models, the loss function and the fitting algorithm, otherwise, one may result in an inappropriate predictive model. The purpose of this section is to introduce the theory behind model fitting and model evaluation in a broader sense, and we are going to be more specific in Chapter 2 by relating these statistical concepts to actuarial problems.

## Page 18
# 1.4.2 Strictly consistent loss functions for mean estimation 

Denote by $\mathcal{M}$ the class of (sufficiently nice) regression functions $\mu: \mathcal{X} \rightarrow \mathbb{R}$ under consideration as candidates for (1.2). Select a loss function $L$ according to (1.5). The best candidate within the class $\mathcal{M}$ for the true regression function (1.2) w.r.t. the selected loss function $L$ is the solution to, subject to existence,

$$
\widehat{\mu} \in \underset{\mu \in \mathcal{M}}{\arg \min } \mathbb{E}[L(Y, \mu(\boldsymbol{X}))]
$$

In words, we try to find the regression function $\widehat{\mu} \in \mathcal{M}$ that provides us with the smallest expected loss (the expectation is over the population distribution $\mathbb{P}$ ). To make this a sensible model selection tool, we require some properties on the chosen loss function $L$. This is introduced in the next definition. ${ }^{2}$

Definition 1.3. Denote the true regression function by $\mu^{*}$, see (1.2). The loss function $L$ is consistent for mean estimation w.r.t. $\mathcal{M}$ if

$$
\mathbb{E}\left[L\left(Y, \mu^{*}(\boldsymbol{X})\right)\right] \leq \mathbb{E}[L(Y, \mu(\boldsymbol{X}))]
$$

for all $\mu \in \mathcal{M}$, and where we assume that the left-hand side of (1.9) takes a finite value. The loss function is strictly consistent for mean estimation if we have an equality in (1.9) if and only if $\mu(\boldsymbol{X})=\mu^{*}(\boldsymbol{X})$, a.s.

Definition 1.3 tells us that we should only select strictly consistent loss functions for mean estimation for regression model fitting, otherwise the expected loss minimization (1.8) is not a sensible model fitting strategy as we may not discover the true model $\mu^{*}$ by this minimization (assumed it belongs to $\mathcal{M}$ ).
Mathematical result. The strictly consistent loss functions for mean estimation are the Bregman divergences; see Savage [198] and Gneiting [77]. Under certain assumptions, this statement is an "if and only if"-statement. This implies that we should always consider a Bregman divergence for regression model fitting of conditional mean type (1.2).

Bregman divergences take the following form

$$
L(y, m)=\psi(y)-\psi(m)-\psi^{\prime}(m)(y-m) \geq 0
$$

for a strictly convex function $\psi$ with (sub-)gradient $\psi^{\prime}$.
Generally, Kullback-Leibler (KL) divergences and deviance loss functions are Bregman divergences; examples include the square loss, the Poisson deviance loss, the gamma deviance loss or the categorical loss; see Table 2.2, below.

Remarks 1.4. We have mentioned in Remark 1.1 that, typically, for insurance pricing we use (conditional) means. This is justified by the law of large numbers that ensures that we charge the correct price level. These (conditional) means are estimated based on strictly consistent loss functions for mean estimation.

[^0]
[^0]:    ${ }^{2}$ It is probably in the genes of actuaries to try to minimize losses. By a sign switch $-L$, we obtain a score, and economists would probably rather want to maximize scores.

## Page 19
In contrast, we could also be interested into medians and quantiles, e.g., for risk management purposes. Strictly consistent loss functions for median and quantile estimation are the mean absolute error (MAE) and the Pinball losses, more generally; see Thomson [216] and Saerens [197]. These losses are not Bregman divergences, and they should not be used for regression model fitting if we are interested in (conditional) expectations. The same applies for model validation and model selection, i.e., if one fits regression models on conditional means, one should not use MAE figures to validate them.

# 1.4.3 Regression fitting on finite samples 

The difficulty in practice is that we cannot compute (1.8) because, typically, the true data generating model is unknown. The general solution to this problem is to replace the true model by an empirical one. For this, we assume to have a sample of i.i.d. data $\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$ that follow the same law as $(Y, \boldsymbol{X})$. The empirical version of (1.8) is given by

$$
\widehat{\mu} \in \underset{\mu \in \mathcal{M}}{\arg \min } \frac{1}{n} \sum_{i=1}^{n} L\left(Y_{i}, \mu\left(\boldsymbol{X}_{i}\right)\right)
$$

We give a couple of remarks on (1.10).

- The law of large numbers provides convergence of the empirical loss in (1.10) to the true expected one, a.s. This uses the i.i.d. property of the sample $\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$.
- Compared to (1.6), we scale by $1 / n$. This does not change the solution on finite samples $n<\infty$, but it is necessary for the law of large numbers argument to hold.
- Generally, we only work with strictly consistent loss functions $L$ for mean estimation, this also applies to the empirical version (1.10).
- The solution $\widehat{\mu}$ of (1.10) depends on the realization of the sample $\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$, and repeating this experiment typically gives a different solution $\widehat{\mu}$. In this sense, the solution $\widehat{\mu}$ of (1.10) is itself a random variable, a function of the sample $\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$, and atypical observations may give atypical solutions.
- The difference between the solutions of (1.8) and (1.10) is coined estimation error. Typically, for increasing sample size, the estimation error decreases on average. In many problems, estimation errors decay at rate $1 / \sqrt{n}$ for i.i.d. data $\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$, which usually can be attributed to a central limit theorem (strict consistency and asymptotic normality).

If we study the model fitting problem (1.8) and if the true model $\mu^{*} \in \mathcal{M}$ belongs to the selected model class, then any strictly consistent loss function $L$ finds the true model $\mu^{*}$, and there are infinitely many strictly consistent loss functions for mean estimation. This statement is an asymptotic (infinite sample size) statement, in contrast to its empirical counterpart (1.10).

The specific selection of the loss function $L$ becomes important on finite sample sizes $n<\infty$.

## Page 20
More specifically, Gourieroux et al. [87, Theorem 4] proved (in a GLM context) that optimal regression models are found if the chosen strictly consistent loss function $L$ for mean estimation reflects the correct variance behavior of the response $Y$. In that case, the model fitting procedure results in a so-called best asymptotically normal estimation.

We illustrate the Gourieroux et al. [87] result by an example. Consider the Gaussian, the Poisson, the gamma and the inverse Gaussian distributions for $Y$, given $\boldsymbol{X}$, with corresponding conditional mean $\mu^{*}(\boldsymbol{X})$ (being the same in all four cases). The conditional variances in these four models are given by

$$
\begin{aligned}
\text { Gaussian model: } & \mathbb{V}(Y \mid \boldsymbol{X})=\varphi \\
\text { Poisson model: } & \mathbb{V}(Y \mid \boldsymbol{X})=\mu^{*}(\boldsymbol{X}) \\
\text { gamma model: } & \mathbb{V}(Y \mid \boldsymbol{X})=\varphi\left(\mu^{*}(\boldsymbol{X})\right)^{2} \\
\text { inverse Gaussian model: } & \mathbb{V}(Y \mid \boldsymbol{X})=\varphi\left(\mu^{*}(\boldsymbol{X})\right)^{3}
\end{aligned}
$$

where $\varphi>0$ is a given dispersion parameter. We observe that in these four models the conditional variances are power functions of the mean functional $\mu^{*}(\boldsymbol{X})$ with different power variance parameters $p \in\{0,1,2,3\}$. These different variance functions can be translated to deviance loss functions by selecting the corresponding distribution within the exponential dispersion family (EDF); for details see (2.6) and the subsequent discussion. In particular, the Gaussian case translates to the square loss

$$
L(y, m)=(y-m)^{2}
$$

the Poisson case to the Poisson deviance loss

$$
L(y, m)=2\left(m-y-y \log \left(\frac{m}{y}\right)\right)
$$

the gamma case to the gamma deviance loss

$$
L(y, m)=2\left(\frac{y-m}{m}+\log \left(\frac{m}{y}\right)\right)
$$

and the inverse Gaussian case to the inverse Gaussian deviance loss

$$
L(y, m)=\frac{(y-m)^{2}}{m^{2} y}
$$

All of these deviance loss functions are strictly consistent for mean estimation, but the one with the correct conditional variance behavior for the response $Y$, given $\boldsymbol{X}$, has the best finite sample properties (on average).

More examples are provided in Table 2.2, below, and in Section 2.1.3, below, we give more mathematical justification to this statement.

Figure 1.2 shows the four deviance loss functions (1.11)-(1.14) with power variance parameters $p \in\{0,1,2,3\}$. For this figure, we select a fixed mean parameter $m=1000$ and the dispersion parameters $\varphi>0$ are chosen such that all four models have the same variance of 1000 . Figure 1.2 shows the resulting deviance losses $y \mapsto L(y, m) / \varphi$, scaled by

## Page 21
Figure 1.2: Deviance loss functions (1.11)-(1.14), $y \mapsto L(y, m) / \varphi$ for fixed mean $m=$ 1000; the circles are at $y=800,1200$ (symmetric around $m=1000$ ) for better orientation.
$\varphi^{-1}$ so that they all live on the same scale; the colored circles are at $y=800,1200$ (symmetric around $m=1000$ ) for better orientation. The square loss of the Gaussian model (in blue color) is symmetric around $m=1000$, and all other deviance losses are asymmetric around this value (compared the colored circles). This asymmetry is the property that should match the response distribution so that we receive (on average) optimal finite sample properties in model estimation according to Gourierioux et al. [87]. That is, if the response distribution is very right-skewed, the selected deviance loss should account for this to receive a best asymptotically normal estimation of the expected values; we come back to this in Section 2.1, below.

Remarks 1.5. - All losses in (1.11)-(1.14) satisfy $L(y, m) \geq 0$, and these losses are zero if and only if $y=m$. The square loss (1.11) is defined on $\mathbb{R} \times \mathbb{R}$, and the other three losses on the positive real line $\mathbb{R}_{+} \times \mathbb{R}_{+}$, i.e., they need positive inputs.

- There is a deep connection between the distributions of the EDF, maximum likelihood estimation (MLE) and deviance loss minimization which we did not explain here. First, minimizing the above deviance loss functions is equivalent to MLE in the corresponding distributional model. That is, e.g., minimizing the Poisson deviance loss results in the MLE $\widehat{\mu}^{\text {MLE }}$ for the Poisson model. We will come back to this, below. Second, all considered models (1.11)-(1.14) have in common that they belong to the EDF, and each member of the EDF is characterized by a certain functional form of its conditional variance function $\mathbb{V}(Y \mid \boldsymbol{X})$; we refer to Jørgensen [112, Theorem 2.11] and Bar-Lev-Kokonendji [13, Section 2.4]. In fact, the conditional variance function determines the specific distribution within the EDF, and this, in turn, gives us the optimal deviance loss function choice for model fitting on finite samples.
![Page 21 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p21_img1.jpg)

## Page 22
- Distributions within the EDF with conditional variance functions of the form

$$
\mathbb{V}(Y \mid \boldsymbol{X})=\varphi\left(\mu^{*}(\boldsymbol{X})\right)^{p}
$$

are called Tweedie's distributions with power variance parameter $p \in \mathbb{R} \backslash(0,1)$. This class of distributions has simultaneously been introduced by Tweedie [222] and Bar-Lev-Enis [12], and for $p \in(0,1)$ there do not exist any Tweedie's distributions; see Jørgensen [111]. For $p \in(1,2)$ we have Tweedie's compound Poisson model which is absolutely continuous on $\mathbb{R}_{+}$and which has a point mass in zero.

- In cases where the conditional variance function is unknown or rather unclear, one can exploit an iterative estimation procedure by alternating mean and variance estimation to get optimal regression models. Under isotonicity of the conditional variance in the conditional mean behavior, this has recently been studied in DelongWüthrich [51], and it is verified in this study that this iterative estimation procedure can be very beneficial for improving model accuracy, i.e., getting closer to best asymptotically normal in the sense of Gourieroux et al. [87].

We conclude this section with the log-link GLM example (1.3)-(1.4). We call Example 1.2 a Gaussian log-link GLM because the square loss minimization emphasizes that the responses $Y$ are conditionally Gaussian, given $\boldsymbol{X}$. Similarly, we can define a Poisson and a gamma log-link GLM.

Example 1.6 (Poisson log-link GLM). Select the Poisson deviance loss (1.12) for $L$. This gives optimization in the log-link GLM case

$$
\widehat{\vartheta}=\underset{\vartheta \in \mathbb{R}^{q+1}}{\arg \min } \sum_{i=1}^{n} 2\left(\mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)-Y_{i}-Y_{i} \log \left(\frac{\mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)}{Y_{i}}\right)\right)
$$

for log-link GLM (1.3)-(1.4). This is a Poisson log-link GLM, and it emphasizes that the responses $Y_{i}$ have conditional Poisson distributions, given $\boldsymbol{X}_{i}$.

Example 1.7 (gamma log-link GLM). Select the gamma deviance loss (1.13) for $L$. This gives optimization in the log-link GLM case

$$
\widehat{\vartheta}=\underset{\vartheta \in \mathbb{R}^{q+1}}{\arg \min } \sum_{i=1}^{n} 2\left(\frac{Y_{i}-\mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)}{\mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)}+\log \left(\frac{\mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)}{Y_{i}}\right)\right)
$$

for log-link GLM (1.3)-(1.4). This is a gamma log-link GLM, and it emphasizes that the responses $Y_{i}$ have conditional gamma distributions, given $\boldsymbol{X}_{i}$.

Table 2.2, below, gives more examples and it describes how certain distributions are linked to deviance losses.

# 1.5 Model validation and model selection 

In general, one should always start to analyze data and fitted models by exploiting different visualizations and graphical tools, such as QQ-plots, lift plots, T-reliability

## Page 23
diagrams, etc. We will come back to graphical illustrations, below. In this section we describe model validation and model selection.
Section 1.4 has been focusing on model fitting, and the crucial message was that this should be done under strictly consistent loss functions for mean estimation. The same methodology can be used for model validation and model selection, that is, by a strictly consistent scoring of the fitted models. The objective of expected loss minimization is turned into the new objective of generalization loss minimization. In other words, one would like to know which of several models has the best forecast accuracy, and this is evaluated by studying their generalization loss, meaning that one wants to know "which of the fitted models generalizes best to new unseen data" in the sense of giving the most accurate forecasts for new data.
This section focuses on the core (model-agnostic) methods for model validation and model selection that are in the intersection between machine learning and statistics, such as cross-validation, Akaike's information criterion or out-of-bag validation. Out-of-bag validation requires to introduce the bootstrap which is also done in this section. More sophisticated tools for model validation and model selection (model-agnostic and modelspecific ones) will be described in later chapters, but for this we first need to introduce the relevant techniques.

# 1.5.1 Out-of-sample (generalization) loss 

Definition 1.3 motivates to select the model with the smallest expected loss for a given strictly consistent loss function $L$, see (1.9). As highlighted in (1.10), this selection needs to be done empirically because the true data generating mechanism is unknown. There is a specific point that needs special attention in this model validation and model selection procedure.

Model estimation and model validation should not be done on the identical sample.

This is most easily understood by realizing that if one would use the identical data, always a more complex model would outperform a nested simpler model. This is related to the in-sample bias that may judge the more complex model too optimistically because it solves the same minimization problem (1.10) under more degrees of freedom.

The standard way of analyzing the generalization loss (forecast performance) is to partition the entire sample into two data sets a learning sample $\mathcal{L}$ for model fitting and a test sample (hold-out sample) $\mathcal{T}$ for model testing (generalization loss analysis). These two samples should be mutually independent, and contain i.i.d. data $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$ and $\mathcal{T}=\left(Y_{t}, \boldsymbol{X}_{t}\right)_{t=1}^{m}$, respectively, following the same law as $(Y, \boldsymbol{X})$; the two samples are distinguished here by the different lower indices $1 \leq i \leq n$ and $1 \leq t \leq m$, respectively. Model fitting (model learning) is then performed solely on the learning sample $\mathcal{L}$ by minimizing the in-sample loss

$$
\widehat{\mu}_{\mathcal{L}} \in \underset{\mu \in \mathcal{M}}{\arg \min } \frac{1}{n} \sum_{i=1}^{n} L\left(Y_{i}, \mu\left(\boldsymbol{X}_{i}\right)\right)
$$

Version March 3, 2025, @AI Tools for Actuaries

## Page 24
The selected model(s) are evaluated (compared to each other) on the hold-out sample $\mathcal{T}$ by analyzing their out-of-sample loss (empirical generalization loss (GL))

$$
\widehat{\mathrm{GL}}\left(\mathcal{T}, \widehat{\mu}_{\mathcal{L}}\right):=\frac{1}{m} \sum_{t=1}^{m} L\left(Y_{t}, \widehat{\mu}_{\mathcal{L}}\left(\boldsymbol{X}_{t}\right)\right)
$$

Thus, the learning sample $\mathcal{L}$ is only used for the estimation of the regression function $\widehat{\mu}_{\mathcal{L}}(\cdot)$, which is then evaluated on the independent hold-out sample $\mathcal{T}$. This out-of-sample loss (1.16) is the main workhorse for model selection in machine learning models (e.g., between a neural network and a gradient boosting model). A main reason for this is that computationally it is not very demanding.

# 1.5.2 Cross-validation 

Out-of-sample loss validation (1.16) may not be the most economic way of dealing with small data, i.e., with a statistical problem where no big data is available. By this we mean that, unlike in many machine learning problems, in actuarial problems we do not have unlimited data resources, but the available data is determined by the size of the insurance portfolio. In this case, $K$-fold cross-validation (CV) is an alternative.
In a first step, $K$-fold cross-validation fits the model $K$ times to different sub-samples of the data to derive the generalization loss estimate (1.17), below, and in a second final step, all data is used to receive the optimal predictive model $\widehat{\mu}$. For the first step, we partition (at random) the index set $\mathcal{I}=\{1, \ldots, n\}$ into $K$ roughly equally sized folds $\left(\mathcal{I}_{k}\right)_{k=1}^{K}$, see Figure 1.3. $K$ is a hyper-parameter that is usually selected as $K=10$, but for small sample sizes $n$ we may also select a smaller $K$ to receive reliable results; in Figure 1.3 it is set to $K=5$. We then learn the model on the data with indices $\mathcal{I} \backslash \mathcal{I}_{k}$, and we perform an out-of-sample validation on the indices $\mathcal{I}_{k}$. That is, for $1 \leq k \leq K$, we compute the estimated models

$$
\widehat{\mu}_{(\backslash k)} \in \underset{\mu \in \mathcal{M}}{\arg \min } \sum_{i \in \mathcal{I} \backslash \mathcal{I}_{k}} L\left(Y_{i}, \mu\left(\boldsymbol{X}_{i}\right)\right)
$$

These estimated models are cross-validated (mutually out-of-sample) by

$$
\widehat{\mathrm{GL}}^{\mathrm{CV}}:=\frac{1}{K} \sum_{k=1}^{K} \frac{1}{\left|\mathcal{I}_{k}\right|} \sum_{i \in \mathcal{I}_{k}} L\left(Y_{i}, \widehat{\mu}_{(\backslash k)}\left(\boldsymbol{X}_{i}\right)\right)
$$

Note that each term under the $k$-summation uses a (disjoint) partition of the entire data into a learning sample with indices $\mathcal{I} \backslash \mathcal{I}_{k}$ and a test sample with indices $\mathcal{I}_{k}$. Thus, we perform a proper (mutual) out-of-sample validation for each $1 \leq k \leq K$.

Remarks 1.8. - Both the out-of-sample loss (1.16) and the $K$-fold cross-validation loss (1.17) give estimates for the true (expected) generalization loss. The crossvalidation loss has the advantage that it does not only estimate this generalization loss, but we can also quantify uncertainty by computing the empirical standard deviation of the $K$ folds under the $k$-summation in (1.17).

## Page 25
Figure 1.3: Partitions of $K$-fold cross-validation with $K=5$ folds.

- $K$-fold cross-validation can be demanding because it requires fitting the model $K+1$ times, once to get the optimal regression function $\widehat{\mu}$, and $K$ times to compute the $K$-fold cross-validation loss (1.17).
- Above, we have partitioned the index set $\mathcal{I}$ completely at random into the folds $\left(\mathcal{I}_{k}\right)_{k=1}^{K}$. Stratified $K$-fold cross-validation does not partition $\mathcal{I}$ completely at random. For instance, one may order the instances $1 \leq i \leq n$ w.r.t. the sizes of the responses $\left(Y_{i}\right)_{i=1}^{n}$, and then allocate the $K$ largest claims at random to the different folds $\left(\mathcal{I}_{k}\right)_{k=1}^{K}$ of the partition, then the next $K$ largest claims likewise, etc. This provides more similarity between the folds, which can be an advantage in model selection, especially under right-skewed or heavy-tailed loss size distributions.


# 1.5.3 Akaike's information criterion for model selection 

In Section 1.5.1, we have emphasized that model validation and generalization loss analysis should be done on a disjoint hold-out sample $\mathcal{T}$ that has not been used for model fitting to avoid an in-sample bias in model selection. Akaike [2], in Akaike's information criterion (AIC), and Schwarz [204], in the Bayesian information criterion (BIC), tried to (asymptotically) quantify this in-sample bias (under different assumptions). Naturally, AIC and BIC only apply under these assumptions. We start from a parametrized density $\left.Y\right|_{\boldsymbol{X}} \sim f_{\vartheta}(\cdot \mid \boldsymbol{X})$ with an unknown $r$-dimensional model parameter $\vartheta \in \mathbb{R}^{r}$. Application of AIC and BIC requires to fit this density with MLE. Denote the log-likelihood function based on the i.i.d. sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$ by

$$
\vartheta \mapsto \ell_{\mathcal{L}}(\vartheta)=\sum_{i=1}^{n} \log \left(f_{\vartheta}\left(Y_{i} \mid \boldsymbol{X}_{i}\right)\right)
$$

We compute the MLE of $\vartheta$, subject to existence and uniqueness, by solving

$$
\widehat{\vartheta}^{\mathrm{MLE}}=\underset{\vartheta}{\arg \max } \ell_{\mathcal{L}}(\vartheta)
$$

Since $\widehat{\vartheta}^{\mathrm{MLE}}$ maximizes (1.18), the quantity $\ell_{\mathcal{L}}\left(\widehat{\vartheta}^{\mathrm{MLE}}\right)$ gives an in-sample biased view of this model. AIC and BIC determine asymptotically an in-sample bias correction (in
![Page 25 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p25_img1.jpg)

## Page 26
different settings) and based on the fact that model fitting was done by MLE. The AIC value of this MLE fitted model is defined by

$$
\mathrm{AIC}=-2 \ell_{\mathcal{L}}\left(\widehat{\vartheta}^{\mathrm{MLE}}\right)+2 r
$$

where $r \in \mathbb{N}$ is the dimension of the model parameter $\vartheta$. If we have different MLE fitted models, preference should be given to the model that has the smallest AIC value. Likewise we can proceed with the BIC value defined by

$$
\mathrm{BIC}=-2 \ell_{\mathcal{L}}\left(\widehat{\vartheta}^{\mathrm{MLE}}\right)+\log (n) r
$$

where $n$ is the sample size. Remark that these model selection criteria may not be valid in machine learning models, such as neural networks, as these models do not use the MLE for model fitting. Moreover, in many machine learning models, the dimension of the model parameter is unclear because such models are often over-parametrized resulting in redundancy; we refer to Abbas et al. [1] who discuss the effective dimension of neural networks. Therefore, AIC and BIC are mainly useful tools for model selection among GLMs supposed they were fitted with MLE.

We summarize the important points about AIC and BIC.

- First, we need MLE estimated models for applying AIC and BIC.
- Second, (1.19) and (1.20) require to consider all terms of the log-likelihood function $\ell_{\mathcal{L}}(\vartheta)$. This also applies to models where some of the terms cannot be computed analytically, like, e.g., in Tweedie's compound Poisson model.
- Third, model selection can be done for any two models and these models do not need to be nested and they do not need to be Gaussian. This makes AIC and BIC very attractive and widely applicable.
- Fourth, the responses need to be on the identical scale in all compared models.
- Fifth, AIC and BIC only give preference to a model, but they do not confirm that the selected model is suitable, i.e., it could simply be the best option of a class of inappropriate models.


# 1.5.4 Bootstrap and out-of-bag validation 

Starting from an i.i.d. sample $\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$, one often would like to have more observations of the same nature, but because (typically) the data generating mechanism is unknown, this cannot be achieved. Bootstrap is a method that aims at generating more data that is similar to $\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$. Bootstrap simulation goes back to Efron [61] and Efron-Tibshirani [62]. There are parametric versions and non-parametric ones.

## Parametric bootstrap

For a parametric bootstrap version, we assume that the independent observations follow a given model $\left.Y_{i}\right|_{\boldsymbol{X}_{i}} \sim F_{\vartheta}\left(\cdot \mid \boldsymbol{X}_{i}\right)$, for $1 \leq i \leq n$, being parametrized by an unknown

## Page 27
model parameter $\vartheta \in \mathbb{R}^{r}$. This allows one to estimate the model parameter $\vartheta$ from the i.i.d. sample $\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$, giving an estimated model $F_{\widehat{\vartheta}}(\cdot \mid \boldsymbol{X})$ for given covariates $\boldsymbol{X}$. A bootstrap sample $\left(Y_{i}^{\star}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$ is then obtained by simulating new conditionally independent observations $\left.Y_{i}^{\star}\right|_{\boldsymbol{X}_{i}} \sim F_{\widehat{\vartheta}}(\cdot \mid \boldsymbol{X}_{i})$ from the estimated model, for $1 \leq i \leq n$. If the estimated model is sufficiently accurate, the bootstrap sample $\left(Y_{i}^{\star}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$ has similar distributional properties as the original sample $\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$. Based on this bootstrap sample $\left(Y_{i}^{\star}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$, we can re-estimate the model parameter $\vartheta$ providing us with a bootstrap estimate $\widehat{\vartheta}^{\star} \in \mathbb{R}^{r}$. Repeating this procedure $m$ times gives us an empirical distribution of the estimated model parameter (called empirical bootstrap distribution)

$$
\widehat{G}(\theta):=\frac{1}{m} \sum_{j=1}^{m} \mathbb{1}_{\{\theta \leq \widehat{\vartheta}^{(k j)}\}} \quad \text { for } \theta \in \mathbb{R}^{r}
$$

with $\widehat{\vartheta}^{(k j)} \in \mathbb{R}^{r}$ denoting the estimated model parameter from the $j$-th bootstrap sample $\left(Y_{i}^{(k j)}, \boldsymbol{X}_{i}\right)_{i=1}^{n}, 1 \leq j \leq m$.
This is one version of a parametric bootstrap. It keeps the covariates $\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$ fixed, and it only re-simulates the responses from the estimated model. There are many different variants of the parametric bootstrap, e.g., also re-simulating the covariates or only re-simulating the residuals, called residual bootstrap; we refer to Wüthrich-Merz [243, Section 4.3] and the references therein for more discussion.

# Non-parametric bootstrap 

The non-parametric bootstrap is even simpler than its parametric counterpart. For a non-parametric bootstrap we directly start from the observed sample $\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$. A non-parametric bootstrap sample $\left(Y_{j}^{\star}, \boldsymbol{X}_{j}^{\star}\right)_{j=1}^{n}$ is generated by drawing with replacements from the original data $\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$. This naturally also re-simulates the covariates, and some samples appear multiple times in the bootstrap sample $\left(Y_{j}^{\star}, \boldsymbol{X}_{j}^{\star}\right)_{j=1}^{n}$, and others are not selected by this drawing with replacements. Denote by $\mathcal{I}^{\star} \subseteq \mathcal{I}=\{1, \ldots, n\}$ the set of indices that have been selected from the original data $\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$ for the bootstrap sample $\left(Y_{j}^{\star}, \boldsymbol{X}_{j}^{\star}\right)_{j=1}^{n}$. We estimate a new model from this bootstrap sample

$$
\widehat{\mu}^{\star} \in \underset{\mu \in \mathcal{M}}{\arg \min } \sum_{j=1}^{n} L\left(Y_{j}^{\star}, \mu\left(\boldsymbol{X}_{j}^{\star}\right)\right)
$$

and we can study the empirical bootstrap distribution as above by repeating this bootstrap procedure many times.

## Out-of-bag cross-validation

The interesting point about the non-parametric bootstrap now is that the instances $i \in \mathcal{I} \backslash \mathcal{I}^{\star}$ have not been used in this estimation procedure to receive the bootstrap estimate $\widehat{\mu}^{\star}$ in (1.21). We call the set of observations $\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i \in \mathcal{I} \backslash \mathcal{I}^{\star}}$ an out-of-bag (OoB) sample. This presents a valid (disjoint) sample for cross-validation (i.e., an empirical generalization loss)

$$
\widehat{\mathrm{GL}}^{\mathrm{OoB}}:=\frac{1}{\left|\mathcal{I} \backslash \mathcal{I}^{\star}\right|} \sum_{i \in \mathcal{I} \backslash \mathcal{I}^{\star}} L\left(Y_{i}, \widehat{\mu}^{\star}\left(\boldsymbol{X}_{i}\right)\right)
$$

## Page 28
This gives an alternative to $K$-fold cross-validation (1.17). This out-of-bag validation is natural in random forests regression modeling, because random forests model fitting is based on bootstrapping. However, it could be used as well for any other regression technique for model validation.

We determine the average size of the out-of-bag sample. Not selecting a sample in a single draw has a probability of $(n-1) / n$, and repeating this $n$ times raises this probability to the power $n$. For large sample sizes we obtain convergence

$$
\lim _{n \rightarrow \infty}\left(\frac{n-1}{n}\right)^{n}=\lim _{n \rightarrow \infty}\left(1-n^{-1}\right)^{n}=e^{-1}=36.8 \%
$$

Thus, on average, the out-of-bag sample has a reasonably big size; see Breiman [28].

# 1.5.5 Summary on model validation and model selection 

In practice, in machine learning tasks, an out-of-sample validation based on a disjoint learning sample $\mathcal{L}$ and test sample $\mathcal{T}$ is predominant. First, in many applications one has a vast amount of data, so scarcity is not an issue. Second, in complex algorithmic models one can have very sophisticated and time-consuming model fitting procedures which makes it impossible to perform, e.g., $K$-fold cross-validation. $K$-fold cross-validation is only feasible in smaller problems. It has the advantage that we can not only give preference to a model, but we can also quantify the uncertainty in this decision. This is, e.g., done in regression tree modeling for the tree size selection, that is, this is a way of controlling the randomness in model selection. AIC and BIC only apply for MLE estimated models, which clearly limits their scope to simple models. Finally, out-of-bag validation is not used very often except for random forests. Computationally, it is similar to $K$-fold cross-validation and we see quite some potential of out-of-bag validation for model evaluation.

To keep the discussion as simple as possible in this chapter, we have avoided to talk about weights or exposures. Regression modeling is typically done within the exponential dispersion family (EDF) which is going to be introduced in Section 2.1. The EDF considers volume-scaled quantities and this requires that generally all losses $L$ are replaced by scaled losses

$$
L\left(Y_{i}, \mu\left(\boldsymbol{X}_{i}\right)\right) \rightarrow \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu\left(\boldsymbol{X}_{i}\right)\right)
$$

where $v_{i}>0$ is an instance specific weight and $\varphi>0$ is a general parameter for dispersion that is not instance specific; for details see Section 2.1. This instance specific factor $v_{i} / \varphi$ is going to be added in front of all loss functions $L$ in all subsequent considerations.

## Page 29
# Summary of model fitting and model selection procedure 

- Assume we have two independent data sets, a learning sample $\mathcal{L}=$ $\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$ and a test sample $\mathcal{T}=\left(Y_{t}, \boldsymbol{X}_{t}, v_{t}\right)_{t=1}^{m}$, both containing i.i.d. data following the same law as $(Y, \boldsymbol{X}, v)$.
- Assume we want to consider two model classes $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ that are significantly different, e.g., GLMs and gradient boosting models, and we would like to select the best model from these two classes to predict a new observation $Y$, given $\boldsymbol{X}$.
- Select a suitable strictly consistent loss function $L$ for mean estimation, e.g., if the responses $Y$ are gamma like, given $\boldsymbol{X}$, we select the gamma deviance loss for $L$.
- Based on the learning sample $\mathcal{L}$, select the best models w.r.t. the selected loss function $L$ from both model classes $\mathcal{M}_{k}, k=1,2$,

$$
\widehat{\mu}_{k} \in \underset{\mu \in \mathcal{M}_{k}}{\arg \min } \sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu\left(\boldsymbol{X}_{i}\right)\right)
$$

Note, this only uses the learning sample $\mathcal{L}$.

- For predicting $Y$, given $\boldsymbol{X}$, select the model from $\widehat{\mu}_{1}$ and $\widehat{\mu}_{2}$ that has the smaller out-of-sample loss on the test sample $\mathcal{T}$

$$
\widehat{\operatorname{GL}}\left(\mathcal{T}, \widehat{\mu}_{k}\right)=\frac{1}{m} \sum_{t=1}^{m} \frac{v_{t}}{\varphi} L\left(Y_{t}, \widehat{\mu}_{k}\left(\boldsymbol{X}_{t}\right)\right)
$$

That is, select $\widehat{\mu}_{1} \in \mathcal{M}_{1}$ if $\widehat{\mathrm{GL}}\left(\mathcal{T}, \widehat{\mu}_{1}\right)<\widehat{\mathrm{GL}}\left(\mathcal{T}, \widehat{\mu}_{2}\right)$, otherwise select $\widehat{\mu}_{2} \in \mathcal{M}_{2}$.

## Page 30
Version March 3, 2025, @AI Tools for Actuaries

## Page 31
# Chapter 2 

## Regression models

We begin with remarks before diving into predictive modeling. Before starting with modeling, we should ask ourselves about the desirable characteristics a predictive model should possess. Typically, we cannot comply with all of them, and the best model will be a compromise of all of these desirable characteristics.

Let us mention some points in a slightly unstructured manner.
(a) Clearly, the model should have a good predictive performance giving us very accurate forecasts.
(b) The model should have a certain smoothness so that the forecasts do not dramatically change, if one slightly perturbs the inputs.
(c) The model should have a certain sparsity and simplicity, which means that we target for a model that is as small as possible, but still predicts sufficiently accurately; i.e., we aim for a parsimonious model.
(d) Towards stakeholder we should be able to explain the inner functioning of the model, and the results should intuitively make sense and be explainable.
(e) It should have good finite sample properties in estimation, so that all parts of the model can be determined with credibility.
(f) We should be able to quantify prediction uncertainty.
(g) We should be able to manually change parts of the model to integrate expert knowledge, if available and necessary.
(h) It should comply with regulation, and we should be able to verify this.

The starting point of a machine learner would probably be to just run the available data through a gradient boosting machine (GBM) or a neural network, and then study its outputs. As already discussed at the beginning of Section 1.4, this may not be the best way of dealing with the problem, especially, in scarce data settings that may have a large variability in their responses (class imbalance is a related buzzword). This is one of the key differences between machine learning and actuarial data science, namely, the

## Page 32
actuary first tries to understand the (raw) data, and then designs an optimal architecture according to the insights that she/he has gained from this initial data analysis. This insight can significantly improve predictive models, already, e.g., choosing a more suitable strictly consistent loss function for mean estimation than the square loss can make a huge difference. This is the main motivation for us to first study the most important family of distributions, the exponential dispersion family (EDF). This knowledge can then be translated into optimal choices of the objective function for a certain type of data and problem; in fact, this will justify the deviance loss choices (1.11)-(1.14). In this sense, the statistical theory matters beyond algorithmic forecasting.

# 2.1 Exponential dispersion family 

Distribution functions $F(Y \mid \boldsymbol{X})$ play a surprisingly marginal role in regression modeling because most attention is paid to the estimation of the regression function. This regression function estimation is almost solely based on the first moments and strictly consistent loss functions, see Definition 1.3. Higher moments and distributions only become relevant for uncertainty quantification. But even for this, one often does not rely on explicit distributions, but one uses asymptotic normality results which typically only require i.i.d. data with finite second moments. Only, once one studies finite sample properties the underlying distributions become more important, see discussion in Section 1.4.3.

### 2.1.1 Introduction of the exponential dispersion family

We briefly introduce the EDF in this section and we give its most important properties. This allows us to more specifically discuss the selection of the strictly consistent loss function $L$ for regression fitting. The EDF was introduced by Sir Fisher [68], and the most relevant references are Jørgensen [110, 111, 112] and Barndorff-Nielsen [16]; this short outline follows Wüthrich-Merz [243] and we also use the notation of that reference. We say that $Y \sim \operatorname{EDF}(\theta, \varphi / v ; \kappa)$ belongs to the EDF if it has a density of the form

$$
Y \sim f_{\theta}(y) \mathrm{d} \nu(y)=\exp \left\{\frac{y \theta-\kappa(\theta)}{\varphi / v}+c(y, \varphi / v)\right\} \mathrm{d} \nu(y)
$$

for a $\sigma$-finite measure $\nu$ on $\mathbb{R}$ (determining the support of $Y$ ), with canonical parameter $\theta \in \boldsymbol{\Theta}$ in the effective domain $\boldsymbol{\Theta} \subseteq \mathbb{R}$, for cumulant function

$$
\kappa: \boldsymbol{\Theta} \rightarrow \mathbb{R}
$$

with dispersion parameter $\varphi>0$, weight/volume $v>0$, and normalizing function $c(y, \varphi / v)$ such that the density in (2.1) integrates to one.

### 2.1.2 Cumulant function, mean and variance function

In any non-trivial setting, the effective domain $\boldsymbol{\Theta} \subseteq \mathbb{R}$ is a (possibly infinite) interval with a non-empty interior $\hat{\boldsymbol{\Theta}}$, and the cumulant function $\kappa$ is infinitely often differentiable (smooth) and strictly convex on $\hat{\boldsymbol{\Theta}}$.

## Page 33
Furthermore, we have the first two moments

$$
\mu_{0}=\mathbb{E}[Y]=\kappa^{\prime}(\theta) \quad \text { and } \quad \mathbb{V}(Y)=\frac{\varphi}{v} \kappa^{\prime \prime}(\theta)=\frac{\varphi}{v} \kappa^{\prime \prime}\left(\left(\kappa^{\prime}\right)^{-1}\left(\mu_{0}\right)\right)
$$

for the canonical parameters $\theta \in \hat{\Theta}$.

This indicates the crucial role played by the cumulant function $\kappa$ in the EDF.
The inverse function $h:=\left(\kappa^{\prime}\right)^{-1}$ is called the canonical link of the chosen EDF, and it provides us with the identity

$$
\mu_{0}=\mathbb{E}[Y]=\kappa^{\prime}(\theta) \quad \Longleftrightarrow \quad h\left(\mu_{0}\right)=h(\mathbb{E}[Y])=\theta
$$

This motivates the definition of the mean parameter space

$$
\kappa^{\prime}(\hat{\boldsymbol{\Theta}})=\left\{\kappa^{\prime}(\theta) ; \theta \in \hat{\boldsymbol{\Theta}}\right\}
$$

which is one-to-one with the interior of the effective domain $\hat{\boldsymbol{\Theta}}$, thus, the EDF can either be parametrized by the canonical parameter $\theta$ or by its mean parameter $\mu_{0}$.
Finally, we introduce the variance function $\mu_{0} \mapsto V\left(\mu_{0}\right)=\left(\kappa^{\prime \prime} \circ h\right)\left(\mu_{0}\right)$, which has the property

$$
\mathbb{V}(Y)=\frac{\varphi}{v} V\left(\mu_{0}\right)
$$

All the models discussed in (1.11)-(1.14) and (1.15) are of this EDF type, with power variance function $V\left(\mu_{0}\right)=\mu_{0}^{p}$ for $p \in \mathbb{R} \backslash(0,1)$; for simplicity we have set weight $v=1$ in these previous examples. This variance function $V$ fully characterizes the cumulant function $\kappa$, supposed it exists on the selected mean parameter space; see Jørgensen [112, Theorem 2.11] and Bar-Lev-Kokonendji [13, Section 2.4].

The EDF is attractive because it contains many popular statistical models used to solve actuarial problems such as the Bernoulli, Gaussian, gamma, inverse Gaussian, Poisson or negative binomial models. These examples are distinguished by the choice of the cumulant function $\kappa$; Table 2.1 gives the most relevant examples.

| EDF distribution | cumulant function $\kappa(\theta)$ | mean $\mu_{0}=\kappa^{\prime}(\theta)$ |
| :-- | :--: | :--: |
| Gaussian | $\theta^{2} / 2$ | $\theta$ |
| gamma | $-\log (-\theta)$ | $-1 / \theta$ |
| inverse Gaussian | $-\sqrt{-2 \theta}$ | $1 / \sqrt{(-2 \theta)}$ |
| Poisson | $e^{\theta}$ | $e^{\theta}$ |
| negative binomial | $-\log \left(1-e^{\theta}\right)$ | $e^{\theta} /\left(1-e^{\theta}\right)$ |
| Tweedie's compound Poisson | $\frac{((1-p) \theta)^{\frac{1-p}{1-p}}}{2-p}, \quad p \in(1,2)$ | $((1-p) \theta)^{\frac{1}{1-p}}$ |
| Bernoulli | $\log \left(1+e^{\theta}\right)$ | $e^{\theta} /\left(1+e^{\theta}\right)$ |

Table 2.1: Commonly used examples of the EDF with corresponding means.

## Page 34
# 2.1.3 Maximum likelihood estimation and deviance loss 

The special parametrization of the EDF through the canonical parameter $\theta$ makes this family of distributions very attractive for MLE because maximization of the density (2.1) in $\theta \in \boldsymbol{\Theta}$ is very simple. For a single observation $Y$ (i.e., for sample size $n=1$ ), we have MLE

$$
\widehat{\theta}^{\mathrm{MLE}}=h(Y) \quad \Longleftrightarrow \quad \widehat{\mu}_{0}^{\mathrm{MLE}}=Y
$$

this statement only holds up to the possibly degenerate behavior at the boundary of $\boldsymbol{\Theta} .{ }^{1}$
This allows us to define the deviance loss function within the EDF.
Definition 2.1. Select $Y \sim \operatorname{EDF}(\theta, \varphi / v ; \kappa)$ with steep cumulant function $\kappa$, see footnote 1 on page 34. The deviance loss function of the selected EDF is defined by

$$
L(y, m)=2 \frac{\varphi}{v}\left(\log \left(f_{h(y)}(y)\right)-\log \left(f_{h(m)}(y)\right)\right) \geq 0
$$

with $m \in \kappa^{\prime}(\hat{\boldsymbol{\Theta}})$ and $y$ in the convex closure of the support of the response $Y$.

## Deviance losses for building actuarial models

The deviance losses provide an important way of building actuarial models.

- Every member of the EDF is characterized by its cumulant function $\kappa$.
- Using (2.6), the EDF density $f_{\theta}(y)$ with cumulant function $\kappa$, given in (2.1), is transformed into a deviance loss function $L(y, m)$; this uses the canonical link relation $h(m)=\theta$, see (2.3).
- Maximizing the likelihood of the EDF density $f_{\theta}$ in canonical parameter $\theta$ is equivalent to minimizing the deviance loss $L(y, m)$ in mean parameter $m$.
- The latter is precisely the property that motivated the choices of the deviance losses (1.11)-(1.14), e.g., if the responses $Y$ are Poisson distributed, we can either perform MLE in the Poisson model or we can minimize the Poisson deviance loss (1.12) providing us with the same model.

Table 2.2 presents the most popular EDF models in actuarial science and their deviance loss functions (2.6). Tweedie's CP refers to Tweedie's compound Poisson model that has a power variance function (1.15) with $p \in(1,2)$. This can be extended to $p \in\{0\} \cup[1, \infty)$, where $p=1,2$ has to be understood in the limiting sense for the cumulant function $\kappa$ and the corresponding deviance loss $L .{ }^{2}$ The power variance parameter $p=0$ gives the Gaussian model, $p=1$ the Poisson model, $p=2$ the gamma model and $p=3$ the inverse Gaussian model. These are the only models of the EDF with a power variance

[^0]
[^0]:    ${ }^{1}$ In fact, we need to be slightly more careful with statement (2.5). Generally, we request that the cumulant function $\kappa$ is steep at the boundary of the effective domain $\Theta$; see Barndorff-Nielsen [16, Theorem 9.2]. This aligns the mean parameter space with the convex closure of the support of the response $Y$. Then, (2.5) is correct up to the boundary of $\Theta$. At the boundary we may get a degenerate model having a finite mean estimate $\widehat{\mu}_{0}^{\text {MLE }}$, but an undefined canonical parameter estimate.
    ${ }^{2}$ The cases $p<0$ do not have steep cumulant functions $\kappa$ and are therefore disregarded here.

## Page 35
| EDF distribution | cumulant function $\kappa(\theta)$ | deviance loss $L(y, m)$ |
| :-- | :--: | :--: |
| Gaussian | $\theta^{2} / 2$ | $(y-m)^{2}$ |
| gamma | $-\log (-\theta)$ | $2((y-m) / m+\log (m / y))$ |
| inverse Gaussian | $-\sqrt{-2 \theta}$ | $(y-m)^{2} /\left(m^{2} y\right)$ |
| Poisson | $e^{\theta}$ | $2(m-y-y \log (m / y))$ |
| negative binomial | $-\log \left(1-e^{\theta}\right)$ | $2\left(y \log \left(\frac{y}{m}\right)-(y+1) \log \left(\frac{y+1}{m+1}\right)\right)$ |
| Tweedie's CP | $\frac{((1-p) \theta)^{2-p}}{2-p}, p \in(1,2)$ | $2\left(y^{\frac{y^{1-p}-m^{1-p}}{1-p}}-\frac{y^{2-p}-m^{2-p}}{2-p}\right)$ |
| Bernoulli | $\log \left(1+e^{\theta}\right)$ | $2(-y \log (m)-(1-y) \log (1-m))$ |

Table 2.2: Commonly used examples of the EDF with corresponding deviance losses; the corresponding canonical links $h$ are provided in Table 3.1, below.
function for which the normalizing term $c(y ; \varphi / v)$ has a closed from, see Blæsild-Jensen [23]. This becomes relevant for AIC and BIC, see (1.19) and (1.20), but also for MLE of the dispersion parameter $\varphi$.

| $p$ | distribution | support of $Y$ | $\boldsymbol{\Theta}$ | $\kappa^{\prime}(\hat{\boldsymbol{\Theta}})$ |
| :--: | :-- | :--: | :--: | :--: |
| $p=0$ | Gaussian distribution | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}$ |
| $p=1$ | Poisson distribution | $\mathbb{N}_{0}$ | $\mathbb{R}$ | $(0, \infty)$ |
| $1<p<2$ | Tweedie's CP distribution | $(0, \infty)$ | $(-\infty, 0)$ | $(0, \infty)$ |
| $p=2$ | gamma distribution | $(0, \infty)$ | $(-\infty, 0)$ | $(0, \infty)$ |
| $p>2$ | generated by positive stable distributions | $(0, \infty)$ | $(-\infty, 0]$ | $(0, \infty)$ |
| $p=3$ | inverse Gaussian distribution | $(0, \infty)$ | $(-\infty, 0]$ | $(0, \infty)$ |

Table 2.3: Tweedie's models for power variance parameters $p \in\{0\} \cup[1, \infty)$; this table is taken form Jørgensen [112].

We close this section with a technical remark. Table 2.3 gives the supports of the responses $Y$, the effective domains $\boldsymbol{\Theta}$ and the mean parameter spaces $\kappa^{\prime}(\hat{\boldsymbol{\Theta}})$ of Tweedie's distributions, having power variance function (1.15). In all these examples, the convex closure of the support of $Y$ is equal to the closure of the mean parameter space $\kappa^{\prime}(\hat{\boldsymbol{\Theta}})$. This is a characterization of steep cumulant functions $\kappa$; see Barndorff-Nielsen [16, Theorem 9.2]. If $Y$ is in the boundary of the mean parameter space, the deviance loss (2.6) needs to be understood in the limiting sense; see Wüthrich-Merz [243, formula (4.8)].

# 2.2 Regression models 

The general regression problem has already been introduced in Section 1.4. Namely, we start from a candidate class $\mathcal{M}=\{\mu\}$ of sufficiently nice regression functions $\mu: \mathcal{X} \rightarrow \mathbb{R}$. Based on an i.i.d. learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$, we aim at minimizing the in-sample loss

$$
\widehat{\mu} \in \underset{\mu \in \mathcal{M}}{\arg \min } \frac{1}{n} \sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu\left(\boldsymbol{X}_{i}\right)\right)
$$

## Page 36
for a strictly consistent loss function $L$ for mean estimation. There is a (minor) change to (1.10), namely, we add factors $v_{i} / \varphi$ to receive weighted losses in (2.7). The motivation for these weightings is that we assume of having selected a deviance loss function for $L$, being implied by a distributional model coming from the EDF (2.1). In view of the variance behavior (2.2), this requires a suitable weighting of all the individual instances $1 \leq i \leq n$. The weighting proposed in (2.7) is precisely the one that selects the MLE $\widehat{\mu}^{\mathrm{MLE}}$ w.r.t. the log-likelihood function of the i.i.d. sample $\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$, with responses $Y_{i}$ following the corresponding (conditional) EDF (2.1), given means $\mu\left(\boldsymbol{X}_{i}\right)$ and weights $v_{i}$, for $1 \leq i \leq n .^{3}$ In summary, as already mentioned before, deviance loss minimization in (2.7) is equivalent to MLE in the corresponding EDF.
This is the core of regression modeling with the recurrent goal of finding the true regression function $\mu^{*}$, see (1.2). The different statistical and machine learning methods mainly differ in selecting different classes $\mathcal{M}$ of candidate regression functions $\mu: \mathcal{X} \rightarrow \mathbb{R}$, e.g., we can select a class of GLMs, of deep neural networks of a certain architecture, or of regression trees. Some of these classes are non-parametric and others are parametric families. Optimization (2.7) looks more like a non-parametric version, for a parametrized class of regression functions $\mathcal{M}=\left\{\mu_{\vartheta}\right\}_{\vartheta}$, we rather solve

$$
\widehat{\vartheta} \in \underset{\vartheta}{\arg \min } \frac{1}{n} \sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)
$$

Example 2.2 (Poisson log-link GLM, revisited). We revisit Example 1.6. Assume $Y_{i}$, given $\boldsymbol{X}_{i}$ and $v_{i}$, is Poisson distributed with log-link GLM regression function

$$
\boldsymbol{X} \mapsto \log \left(\mu_{\vartheta}(\boldsymbol{X})\right)=\vartheta_{0}+\sum_{j=1}^{q} \vartheta_{j} X_{j}
$$

for regression parameter $\vartheta \in \mathbb{R}^{q+1}$, see (1.3). Assume the instances $i$ are independent, and select the Poisson deviance loss for $L$. This gives the optimal solution

$$
\widehat{\vartheta}^{\mathrm{MLE}}=\underset{\vartheta \in \mathbb{R}^{q+1}}{\arg \min } \frac{1}{n} \sum_{i=1}^{n} 2 v_{i}\left(\mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)-Y_{i}-Y_{i} \log \left(\frac{\mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)}{Y_{i}}\right)\right)
$$

$Y_{i}=N_{i} / v_{i}$ are the observed claims frequencies, if $N_{i} \in \mathbb{N}_{0}$ denote the observed claims counts; see Remark 2.3. In the Poisson model we have $\varphi=1$. Based on (2.6), we conclude that $\widehat{\vartheta}^{\mathrm{MLE}}$ is the MLE from a Poisson log-link GLM that could also be obtained by maximizing the corresponding log-likelihood function.

[^0]
[^0]:    ${ }^{3}$ There is a subtle point that should be highlighted in the notation of the i.i.d. sample $\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$. The i.i.d. property concerns the random sampling of the entire triple $\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)$ including the weight $v_{i}$. In this sense, there is a slight abuse of notation here because one should use a capital letter for the (random) weight. We have decided to use a small letter to have the identical notation as in the (standard) definition of the EDF (2.1). Having the weight $v_{i}$ as a random variable moreover implies that for the response distribution of $Y_{i}$ one always needs to condition on $\boldsymbol{X}_{i}$ and $v_{i}$; this is the typical situation because, generally, the joint distribution of $\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)$ is not of interest. For notational convenience (and to align with the standard EDF definition) we have not done so in the text, see, e.g., formula (3.3). With this said, the (implicit) randomness in $v_{i}$ may play a role, but this will then be clear from the context.

## Page 37
Remark 2.3. From (2.2) we observe that the expected value of $Y$ is invariant under changes of the volume/weight $v>0$ and the variance decreases linearly in this volume parameter. This indicates that the responses $Y$ within the EDF consider normalized quantities, see Example 2.2. In Jørgensen [112], the normalized quantities correspond to the so-called reproductive form.

These are the basics of regression modeling. The selected class $\mathcal{M}$ of candidate models will also depend on the purpose of its use. In some cases, we want to use regression techniques to explain (or understand) the specific impact of the covariates $\boldsymbol{X}$ on the responses $Y$. For instance, does a new medication (reflected in $\boldsymbol{X}$ ) have a positive impact on the state of health (reflected in $Y$ ). ${ }^{4}$ In other cases, we are just aiming for optimal predictive accuracy, being less interested into the specific impact of $\boldsymbol{X}$ on $Y$. An interesting discussion on explain vs. predict is given in Shmueli [207]. For actuarial pricing, we are somehow in between the two requirements. We would like to have very accurate (risk-adjusted) pricing schemes, however, stakeholders like customers, management and regulators want to know the risk factors and how they impact the prices. That is why actuaries typically have to compromise between explain vs. predict, and the extent to which this is necessary depends on societies, countries, different regulations and companies' business strategies.

# 2.3 Covariate pre-processing 

In this section, we discuss covariate pre-processing in the case of tabular input data. In the previous sections, we have always been speaking about $q$-dimensional real-valued covariates $\boldsymbol{X}=\left(X_{1}, \ldots, X_{q}\right)^{\top}$, being supported in a covariate space $\mathcal{X} \subseteq \mathbb{R}^{q}$. Categorical covariate pre-processing make a major part of actuarial modeling because of the abundance of these kinds of information within traditional actuarial domains, for example, we are thinking of vehicle brands, vehicle models, vehicle details, etc. Such information needs to be pre-processed to real-valued vectors so that it can be used in regression models. Not only categorical variables need pre-processing, but it can be that also realvalued/continuous input variables need pre-processing. This is going to be discussed in this section.

### 2.3.1 Notation

We start with a few words on the notation. The $q$-dimension real-valued covariate information is denoted by $\boldsymbol{X}=\left(X_{1}, \ldots, X_{q}\right)^{\top}$, and it takes values in the covariate space $\mathcal{X} \subseteq \mathbb{R}^{q}$. If we have a sample $\left(\boldsymbol{X}_{i}\right)_{i=1}^{n} \subset \mathcal{X}$ of such covariates, we can stack them into a design matrix $\mathfrak{X}$. For this we typically extend the covariates $\boldsymbol{X}_{i}$ by an initial component (bias component, zero component) being equal to one, to receive the new (extended) covariates

$$
\boldsymbol{X}_{i}=\left(1, X_{i, 1}, \ldots, X_{i, q}\right)^{\top} \in \mathbb{R}^{q+1}
$$

this uses a slight abuse of notation because we do not indicate in $\boldsymbol{X}_{i}$ whether it includes the bias component or not. However, this will always be clear from the context. The

[^0]
[^0]:    ${ }^{4}$ We have purposefully avoided a causal language here, since causal statements can only be made from statistical models in certain circumstances.

## Page 38
design matrix is defined by

$$
\mathfrak{X}=\left[\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{n}\right]^{\top}=\left(\begin{array}{cccc}
1 & X_{1,1} & \cdots & X_{1, q} \\
\vdots & \vdots & \ddots & \vdots \\
1 & X_{n, 1} & \cdots & X_{n, q}
\end{array}\right) \in \mathbb{R}^{n \times(q+1)}
$$

This collects all covariates $\boldsymbol{X}_{i}$ of all instances $1 \leq i \leq n$ on the rows, and it adds an initial bias column being identically equal to one. This is the input information in tabular form; it has the shape of a matrix, which is equal to a tensor of order 2 (also called 2D tensor). It is important to highlight that the different fonts $\boldsymbol{X}, X, \mathcal{X}$ and $\mathfrak{X}$ have different meanings.

# 2.3.2 Categorical covariates 

Categorical covariates (nominal or ordinal) need pre-processing to bring them into a numerical form. This is done by an entity embedding which we are going to discuss in this section.
Consider a categorical covariate $X$ that takes values in a finite set $\mathcal{A}=\left\{a_{1}, \ldots, a_{K}\right\}$ having $K$ levels. The running example in this section will have $K=6$ levels

$$
\mathcal{A}=\{\text { accountant, actuary, economist, quant, statistician, underwriter }\}
$$

## Ordinal encoding

If we have ordinal (ordered) levels $\left(a_{k}\right)_{k=1}^{K}$, we can use a one-dimensional ordinal entity embedding

$$
X \in \mathcal{A} \mapsto \sum_{k=1}^{K} k \mathbb{1}_{\left\{X=a_{k}\right\}}
$$

This assigns to each level $a_{k}$ the corresponding integer $k \in \mathbb{N}$. In our running example (2.11) we have an alphabetical ordering which can be regarded as ordinal. This provides the one-dimensional ordinal entity embedding given in Table 2.4.

| accountant | 1 |
| :-- | :--: |
| actuary | 2 |
| economist | 3 |
| quant | 4 |
| statistician | 5 |
| underwriter | 6 |

Table 2.4: Ordinal one-dimensional ordinal entity embedding.

## One-hot encoding

One may argue that this ordinal (alphabetic) order does not make much sense for risk classification, and one should treat these variables rather as nominal variables. The first

## Page 39
solution for a numerical embedding of nominal variables is one-hot encoding which maps each level $a_{k}$ to a basis vector in $\mathbb{R}^{K}$ resulting in a $K$-dimensional entity embedding

$$
X \in \mathcal{A} \mapsto\left(\mathbb{1}_{\left\{X=a_{1}\right\}}, \ldots, \mathbb{1}_{\left\{X=a_{K}\right\}}\right)^{\top} \in \mathbb{R}^{K}
$$

Table 2.5 illustrates one-hot encoding (as row vectors).

| accountant | 1 | 0 | 0 | 0 | 0 | 0 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| actuary | 0 | 1 | 0 | 0 | 0 | 0 |
| economist | 0 | 0 | 1 | 0 | 0 | 0 |
| quant | 0 | 0 | 0 | 1 | 0 | 0 |
| statistician | 0 | 0 | 0 | 0 | 1 | 0 |
| underwriter | 0 | 0 | 0 | 0 | 0 | 1 |

Table 2.5: One-hot encoding (as row vectors).

# Dummy coding 

One-hot encoding does not lead to full rank design matrices $\mathfrak{X}$ because there is a redundancy. If we know that $X$ does not take the first $K-1$ levels $\left(a_{k}\right)_{k=1}^{K-1}$, it is immediately clear that it has the be of the last level $a_{K}$. If full rank design matrices is an important prerequisite, one should therefore change it to dummy coding (note that for GLMs full rank design matrices are important, but not for neural networks as going to be explained below). For dummy coding one selects a reference level, e.g., $a_{2}=$ actuary. Based on this selection, all other levels are measured relative to this reference level

$$
X \in \mathcal{A} \mapsto\left(\mathbb{1}_{\left\{X=a_{1}\right\}}, \mathbb{1}_{\left\{X=a_{3}\right\}}, \mathbb{1}_{\left\{x=a_{4}\right\}}, \ldots, \mathbb{1}_{\left\{X=a_{K}\right\}}\right)^{\top} \in \mathbb{R}^{K-1}
$$

Table 2.6 illustrates dummy coding (as row vectors).

| accountant | 1 | 0 | 0 | 0 | 0 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| actuary | 0 | 0 | 0 | 0 | 0 |
| economist | 0 | 1 | 0 | 0 | 0 |
| quant | 0 | 0 | 1 | 0 | 0 |
| statistician | 0 | 0 | 0 | 1 | 0 |
| underwriter | 0 | 0 | 0 | 0 | 1 |

Table 2.6: Dummy coding (as row vectors).

In actuarial practice, usually the level with the biggest exposure is chosen as reference level.

## Entity embedding

One-hot encoding and dummy coding lead to so-called sparse design matrices $\mathfrak{X}$, meaning that most of the entries will be zero by these encoding schemes if we have many categorical covariates with many levels. Such sparse design matrices can lead to issues in statistical

## Page 40
modeling and model estimation, e.g., resulting estimated model parameters may not be credible, and matrices may not be well-conditioned because of too sparse levels which can cause numerical issues when inverting these matrices. Therefore, less sparse encodings are considered. One should note that in one-hot encoding and dummy coding there is no notion of adjacency and similarity. However, it might be that some job profiles have a more similar risk behavior than others; another popular actuarial example are car brands, certainly sports car brands have a more similar claims behavior than car brands that typically produce family cars. Borrowing ideas from natural language processing (NLP), one should therefore consider low(er)-dimensional entity embeddings where proximity is related to similarity; see by Brébisson et al. [27], Guo-Berkhahn [88], Richman [186, 187], Delong-Kozak [49] and Richman-Wüthrich [192].
Select an embedding dimension $b \in \mathbb{N}$, this is a hyper-parameter that needs to be selected by the modeler, typically $b \ll K$. We define an entity embedding (EE) as follows

$$
\boldsymbol{e}^{\mathrm{EE}}: \mathcal{A} \rightarrow \mathbb{R}^{b}, \quad X \mapsto \boldsymbol{e}^{\mathrm{EE}}(X)
$$

This assigns to each level $a_{k} \in \mathcal{A}$ an embedding vector $\boldsymbol{e}^{\mathrm{EE}}\left(a_{k}\right) \in \mathbb{R}^{b}$. In total this entity embedding involves $b \cdot K$ parameters (called embedding weights). These need to be determined either by the modeler (manually) or during the model fitting procedure (algorithmically), and proximity in embedding should reflect similarity in (risk) behavior.

|  | finance | maths | statistics | liabilities |
| :-- | :--: | :--: | :--: | :--: |
| accountant | 0.5 | 0 | 0 | 0 |
| actuary | 0.5 | 0.3 | 0.5 | 0.5 |
| economist | 0.5 | 0.2 | 0.5 | 0 |
| quant | 0.7 | 0.3 | 0.3 | 0 |
| statistician | 0 | 0.5 | 0.8 | 0 |
| underwriter | 0 | 0.1 | 0.1 | 0.8 |

Table 2.7: Entity embedding with embedding dimension $b=4$.

Table 2.7 illustrates an entity embedding with embedding dimension $b=4<K=6$. This is a manually chosen example with $b \cdot K=24$ parameters. Typically, in machine learning, these embedding weights are part of model fitting (learning); we will come back to entity embedding in Section 8.2, below.

# Target encoding 

Especially for regression trees, one sometimes uses target encoding, meaning that one does not only consider the categorical covariate, but also the corresponding response. We assume to have a sample $\left(Y_{i}, X_{i}, v_{i}\right)_{i=1}^{n}$ with categorical covariates $X_{i} \in \mathcal{A}$, realvalued responses $Y_{i}$ and weights $v_{i}>0$. We compute the weighted sample means on all levels $a_{k} \in \mathcal{A}$ by

$$
\bar{y}_{k}=\frac{\sum_{i=1}^{n} v_{i} Y_{i} \mathbb{1}_{\left\{X_{i}=a_{k}\right\}}}{\sum_{i=1}^{n} v_{i} \mathbb{1}_{\left\{X_{i}=a_{k}\right\}}}
$$

Version March 3, 2025, @AI Tools for Actuaries

## Page 41
These weighted sample means $\left(\bar{y}_{k}\right)_{k=1}^{K}$ are used like ordinal levels, replacing the nominal ones, and we obtain similarly to (2.12) the one-dimensional target encoding embedding

$$
X \in \mathcal{A} \mapsto \sum_{k=1}^{K} \bar{y}_{k} \mathbb{1}_{\left\{X=a_{k}\right\}}
$$

Though convincing at the first sight, one has to be aware of the fact that this does not consider any interactions within the covariates, e.g., for scarce levels it may happen that a high or low value is mainly implied by another covariate, and the resulting target encoding value (marginal value) $\bar{y}_{k}$ is misleading. This is especially an issue in regression tree constructions if some of the leaves of the regression tree only contain very few instances (under high-cardinality categorical covariates). A method to deal with scarce levels is to combine this target encoding scheme with Bühlmann credibility [34]; see also Micci-Barreca [155]. For this, we try to assess how credible the individual estimates $\bar{y}_{k}$ are, and we improve unreliable ones by mixing them with the global weighted empirical mean $\bar{y}=\sum_{i=1}^{n} v_{i} Y_{i} / \sum_{i=1}^{n} v_{i}$ providing a convex credibility combination

$$
\bar{y}_{k}^{\text {cred }}=\omega_{k} \bar{y}_{k}+\left(1-\omega_{k}\right) \bar{y}
$$

with credibility weights for $1 \leq k \leq K$

$$
\omega_{k}=\frac{\sum_{i=1}^{n} v_{i} \mathbb{1}_{\left\{X_{i}=a_{k}\right\}}}{\sum_{i=1}^{n} v_{i} \mathbb{1}_{\left\{X_{i}=a_{k}\right\}}+\tau} \in[0,1]
$$

and shrinkage parameter $\tau \geq 0$. This shrinkage parameter is a hyper-parameter, also called credibility coefficient in Bühlmann credibility. The bigger the credibility coefficient, the closer is the shrunk value $\bar{y}_{k}^{\text {cred }}$ to the global average $\bar{y}$.

# 2.3.3 Continuous covariates 

In theory, continuous covariates do not need any pre-processing. However, in practice, it might be that the continuous covariates do not provide the right functional form, or they may live on the wrong scale. For example, we may replace a positive covariate $X>0$ by a 4 -dimensional pre-processed covariate

$$
X \mapsto\left(X, \log (X), \exp (X),(X-10)^{2}\right)^{\top}
$$

This has a linear, a logarithmic, an exponential and a non-monotone quadratic term.

## Standardization

Often, one standardizes covariates. Assume that we have $n$ instances with a continuous covariates $\left(X_{i}\right)_{i=1}^{n}$. Standardization considers the transformation

$$
X \mapsto \frac{X-\widehat{m}}{\widehat{s}}
$$

where $\widehat{m} \in \mathbb{R}$ is the empirical mean and $\widehat{s}>0$ the empirical standard deviation of $\left(X_{i}\right)_{i=1}^{n}$.

## Page 42
# MinMaxScaler 

The MinMaxScaler is given by the transformation

$$
X \mapsto 2 \frac{X-\min _{1 \leq i \leq n} X_{i}}{\max _{1 \leq i \leq n} X_{i}-\min _{1 \leq i \leq n} X_{i}}-1
$$

## Categorization

Finally, especially in GLMs, one often discretizes continuous covariates by binning them into categorical classes, e.g., one builds age classes. This is often done to provide more robust functional forms to particular covariates within a GLM framework; of course, this could also be achieved by splines. Select a finite partition $\left(I_{k}\right)_{k=1}^{K}$ of the support of the continuous covariate $X$. Then, we can assign a categorical value $a_{k} \in \mathcal{A}$ to $X$ if it falls into $I_{k}$, that is,

$$
X \mapsto \sum_{k=1}^{K} a_{k} \mathbb{1}_{\left\{X \in I_{k}\right\}}
$$

This categorization then allows one to treat the continuous covariate $X$ as a categorical one, e.g., using dummy encoding in regression modeling; this is very frequently used in actuarial GLMs.

### 2.4 Regularization and sparsity

### 2.4.1 Introduction and overview

Generally speaking, a regression model $\boldsymbol{X} \mapsto \mu(\boldsymbol{X})$ is correctly specified if it integrates all relevant covariates in the correct form, and if there is no redundant, missing or wrong covariate in the regression function. Redundant means that we include multiple covariates that essentially present the same information (e.g., being collinear), missing means that we have forgotten important covariate information that would be available, and wrong means that the covariate does not impact the response. In real world problems, with unknown regression functions, this is part of covariate pre-processing, covariate selection and model selection.
One might be tempted to include any available information into the regression model, to ensure that nothing gets forgotten. However, fitting on finite samples, this is usually not a good strategy, because one may easily run into over-fitting issues, difficulties with collinearity in covariates (also resulting in in-sample over-fitting), in identifiability issues, and, generally, in a poor predictive model because model fitting has not been successful. Model complexity control is crucial in a successful model fitting and predictive modeling procedure, and, typically, one aims for a sparse model, meaning that one aims for a parsimonious model having the fewest necessary variables but still providing accurate predictions.
In this sense, sparse regression is an umbrella term for searching for small (parsimonious) models by penalizing large models and enforcing the fitting procedure to perform variable selection by only including the (in some sense) most significant information into the regression function. Typically, only having the most significant variables in the model

## Page 43
provides the lowest generalization error under finite sample fitting, it avoids in-sample noise (over-)fitting, and it is very beneficial in explaining a model. We have already touched upon this topic in the AIC model selection (1.19), that quantifies a penalization for model complexity under MLE.
In practice, neither knowing the true model nor the (causal) regression structure and the factors that impact the responses, one often starts with slightly too large models, and one tries to shrink them by regularization. Regularization penalizes model complexity and/or extreme regression coefficients; typically, a zero coefficient means that the corresponding term is dropped from the regression function, making a model more sparse.
The most popular regularization techniques include ridge regularization (also known as Tikhonov regularization [219] or $L^{2}$-regularization), the LASSO regularization of Tibshirani [217] (also known as $L^{1}$-regularization) and the elastic net regularization of ZouHastie [250]. Furthermore, there are more specialized techniques like the fused LASSO of Tibshirani et al. [218] for ordered features, or the group LASSO by Yuan-Lin [246], which we are also going to present in this section. There are more methods, e.g., smoothly clipped absolute deviation (SCAD) regularization of Fan-Li [66], which are less relevant for our purposes. An excellent reference on sparse regression is the monograph of Hastie et al. [94].

# 2.4.2 Regularization 

We come back to the parametric regression estimation problem (2.8). It involves selecting the optimal regression function $\mu_{\widehat{\vartheta}}$ from a class of candidate models $\mathcal{M}=\left\{\mu_{\vartheta}\right\}_{\vartheta}$ that are parametrized by $\vartheta$. Let us assume that the parameter $\vartheta$ is a $(r+1)$-dimensional vector

$$
\vartheta=\left(\vartheta_{0}, \vartheta_{1}, \ldots, \vartheta_{r}\right)^{\top} \in \mathbb{R}^{r+1}
$$

where we typically assume that $\left(\vartheta_{j}\right)_{j=1}^{r}$ parametrizes the terms in $\mu_{\vartheta}(\boldsymbol{X})$ that involve the covariates $\boldsymbol{X}$, and $\vartheta_{0}$ is a parameter for the covariate-free part of the regression function that determines the overall level of the regression; $\vartheta_{0}$ is referred to the bias term and this is best understood from the log-link GLM structure (1.3). For reasons explained in Section 4.1, below, this bias term $\vartheta_{0}$ should always be excluded from regularization. In other words, if we regularize the entire regression parameter $\vartheta$, we drop out of the framework of strictly consistent loss functions, even if the selected loss function $L$ is strictly consistent. Denote by $\vartheta_{\backslash 0}=\left(\vartheta_{1}, \ldots, \vartheta_{r}\right)^{\top} \in \mathbb{R}^{r}$ the parameter vector excluding the bias term $\vartheta_{0}$.
A regularized parameter estimation is achieved by considering the optimization problem

$$
\widehat{\vartheta} \in \underset{\vartheta}{\arg \min }\left(\sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)+\eta R\left(\vartheta_{\backslash 0}\right)\right)
$$

where $R: \mathbb{R}^{r} \rightarrow \mathbb{R}_{+}$is a penalty function and $\eta \geq 0$ is the regularization parameter. We will give the most common examples, below. There is one noteworthy change from (2.8) to (2.21). The former objective function is an empirical version of the strictly consistent scoring problem given in (1.8), and this empirical version naturally scales with $1 / n$. This scaling does not affect the optimal solution in (2.8). For the regularized version (2.21) we prefer to drop this factor in order to make the regularization parameter $\eta$ scale-free.

## Page 44
Note that for larger sample sizes $n$, regularization should be weaker which is naturally achieved by dropping any scaling $1 / n$ in (2.21).

# 2.4.3 Ridge regularization 

Ridge regularization or ridge regression selects a squared $L^{2}$-norm penalty function for $R$

$$
\widehat{\vartheta}^{\text {ridge }} \in \underset{\vartheta}{\arg \min }\left(\sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)+\eta\left\|\vartheta_{\backslash 0}\right\|_{2}^{2}\right)
$$

Ridge regularization generally punishes large values in $\left(\widehat{\vartheta}_{j}^{\text {ridge }}\right)_{j=1}^{r}$, this is called shrinkage. The level of shrinkage is determined by the regularization parameter $\eta \geq 0$, and an optimal choice can be determined, e.g., by cross-validation. This intuition of shrinkage also indicates why we exclude the bias term $\vartheta_{0}$ from regularization.
Example 2.4 (Ridge regularized Poisson log-link GLM). We revisit Example 2.2 which considers a Poisson log-link GLM with GLM regression function

$$
\boldsymbol{X} \mapsto \log \left(\mu_{\vartheta}(\boldsymbol{X})\right)=\vartheta_{0}+\sum_{j=1}^{q} \vartheta_{j} X_{j}
$$

The ridge regularized model is found by solving

$$
\widehat{\vartheta}^{\text {ridge }}=\underset{\vartheta \in \mathbb{R}^{q+1}}{\arg \min }\left(\sum_{i=1}^{n} 2 v_{i}\left(\mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)-Y_{i}-Y_{i} \log \left(\frac{\mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)}{Y_{i}}\right)\right)+\eta \sum_{j=1}^{q} \vartheta_{j}^{2}\right)
$$

In this case we have parameter dimension $r=q$.

### 2.4.4 LASSO regularization

LASSO regularization (least absolute shrinkage and selection operator regularization) selects a $L^{1}$-norm penalty function for $R$

$$
\widehat{\vartheta}^{\mathrm{LASSO}} \in \underset{\vartheta}{\arg \min }\left(\sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)+\eta\left\|\vartheta_{\backslash 0}\right\|_{1}\right)
$$

The behavior of LASSO regularization is fundamentally different from ridge regularization. This difference results from the fact that the squared $L^{2}$-norm is differentiable in the origin and the $L^{1}$-norm is not, see Figure 2.1 (lhs). The consequence of this degeneracy of the $L^{1}$-norm in the origin is that some of the components of $\left(\widehat{\vartheta}_{j}^{\mathrm{LASSO}}\right)_{j=1}^{r}$ may be optimal in (2.23) if they are exactly equal to zero, and the more we increase the regularization parameter $\eta$, the more components of $\left(\widehat{\vartheta}_{j}^{\mathrm{LASSO}}\right)_{j=1}^{r}$ are optimal in precisely setting them to zero. Thus, increasing the regularization parameter $\eta$ leads to sparsity of non-zero values in $\left(\widehat{\vartheta}_{j}^{\mathrm{LASSO}}\right)_{j=1}^{r}$, and, consequently, there results a sparse regression model for large regularization parameters $\eta$. For this reason, LASSO regularization is a very popular method for variable selection, because only the most significant terms for prediction will remain in the model for large regularization parameters $\eta$, and we may interpret this as a kind of variable importance. On the other hand, ridge regression just generally shrinks parameters, but it does not set them exactly to zero. Remark that LASSO regularization (2.23) is often used for variable selection, and after this selection, a non-regularized regression model is fitted on the selected variables to receive a higher level of discrimination on the selected variables.

## Page 45
Figure 2.1: Ridge vs. LASSO penalization.

# 2.4.5 Best-subset selection regularization 

Best-subset selection regularization selects a $L^{0}$-norm penalty function for $R$

$$
\widehat{\vartheta}^{\mathrm{BSS}} \in \underset{\vartheta}{\arg \min }\left(\sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)+\eta \sum_{j=1}^{r} \mathbb{1}_{\left\{\vartheta_{j} \neq 0\right\}}\right)
$$

This version is not used very often in applications mainly because optimizing (2.24) is difficult, in fact, LASSO regularization (2.23) is considered as a tractable version instead.

### 2.4.6 Elastic net regularization

Elastic net regularization combines LASSO and ridge regularization by setting

$$
\widehat{\vartheta}^{\text {ElastNet }} \in \underset{\vartheta}{\arg \min }\left(\sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)+\eta\left(\alpha\left\|\vartheta_{\backslash 0}\right\|_{1}+(1-\alpha)\left\|\vartheta_{\backslash 0}\right\|_{2}^{2}\right)\right)
$$

with $\alpha \in[0,1]$. The elastic net regularization overcomes some issues of LASSO, e.g., LASSO does not necessarily provide a unique solution for a linear regression problem with square loss function $L$. It also has the tendency to group effects by assigning similar weights to correlated covariate components.

We give some further remarks to these standard regularization methods.

- In case of a linear regression with the square loss function, there is always a unique (closed-form) solution to the ridge regression problem, because we minimize a convex (quadratic) objective function. The LASSO regression is more complicated, uniqueness is not guaranteed, and it is typically solved by the method of Karush-Kuhn-Tucker (KKT) [114, 129], and using the so-called soft-thresholding operator; see Hastie et al. [94].
- The best-subset selection regression does not lead to a convex minimization problem, nor the SCAD regression.
![Page 45 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p45_img1.jpg)

## Page 46
- Generally, these regularized regression problems can be interpreted geometrically using the method of Lagrange. The feasible set of solutions in the ridge regression case is a $L^{2}$-ball, and in the LASSO regression case a $L^{1}$-cube; see Figure 2.1 (rhs). This geometric difference (having corners or not) precisely distinguishes sparsity of LASSO from shrinkage of ridge regression, i.e., this is related to the difference of these convex geometric sets having differentiable boundaries or not.
- The above regularization methods can also be understood in a Bayesian context. E.g., focusing on ridge regression (2.22): if we replace the strictly consistent loss function by a negative log-likelihood function of the responses, given the covariates, then the penalty term in (2.22) can be interpreted as a Gaussian prior distribution on the parameter $\vartheta_{\backslash 0}$. The resulting estimate $\widehat{\vartheta}^{\mathrm{MAP}}$ is then called maximal-aposteriori (MAP) estimator which results from maximizing the posterior distribution of $\vartheta$, given the sample $\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$.
- Following up in the previous item, if we interpret these regularization problems in a Bayesian context, we can use methods different from MAP estimation for model fitting. One could compute the posterior distribution of the parameter given the observations, e.g., using Markov chain Monte Carlo (MCMC) methods. This has the advantage that one can also (easily) quantify parameter estimation uncertainty. For computational reasons, in most machine learning applications this full posterior analysis is not feasible, and the MCMC methods do not converge on large parameter sets as the MCMC chains do not mix well across the entire parameter space in highdimensional problems. Therefore, the MAP estimator or variational Bayes (VB) methods are studied as approximations.


# 2.4.7 Group and fused LASSO regularizations 

The previous regularization proposals have been focusing on shrinking the regression parameters $\left(\vartheta_{j}\right)_{j=1}^{r}$ and/or to make regression models sparse by setting some of these parameters $\vartheta_{j}$ exactly to zero. In these regularization methods all terms and parameters $\left(\vartheta_{j}\right)_{j=1}^{r}$ are considered individually. However, it could be that we want to treat some of them jointly in a group, e.g., if we have a dummy coded categorical covariate (2.14), regularization should act simultaneously on all parameters that belong to that categorical covariate. For this, we group the (categorical) covariates. Assume we have $G$ groups

$$
\vartheta_{\backslash 0}=\left(\vartheta^{(1)}, \ldots, \vartheta^{(G)}\right)^{\top} \in \mathbb{R}^{d_{1} \times \cdots \times d_{G}}=\mathbb{R}^{r}
$$

where each group $\vartheta^{(k)} \in \mathbb{R}^{d_{k}}$ contains $d_{k}$ components of the regression parameter $\vartheta_{\backslash 0}$.
Group LASSO regularization is obtained by solving

$$
\widehat{\vartheta} \in \underset{\vartheta}{\arg \min }\left(\sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)+\sum_{k=1}^{G} \eta_{k}\left\|\vartheta^{(k)}\right\|_{2}\right)
$$

for regularization parameters $\eta_{k} \geq 0$. For increasing regularization parameters $\eta_{k}$, group LASSO regularization leads to sparsity in setting the entire block of covariates $\vartheta^{(k)} \in \mathbb{R}^{d_{k}}$ simultaneously equal to zero.

## Page 47
The next regularization version we discuss is related to graduation in mortality table smoothing. Assume that we have an adjacency relation on the covariate components, i.e., the covariate component $X_{j}$ is naturally embedded between the components $X_{j-1}$ and $X_{j+1}$, and the lower index $j$ is not set at an arbitrary order. In that case, we may want the corresponding regression parameters $\vartheta_{j}$ to be similar for adjacent variables, assuming for the moment that the parameter $\vartheta_{j}$ corresponds to covariate component $X_{j}$. This motivates the fused LASSO regularization.

Fused LASSO regularization is obtained by solving

$$
\widehat{\vartheta} \in \underset{\vartheta}{\arg \min }\left(\sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)+\sum_{j=2}^{r} \eta_{j}\left|\vartheta_{j}-\vartheta_{j-1}\right|\right)
$$

for regularization parameters $\eta_{j} \geq 0$. The fused LASSO proposal enforces sparsity in the non-zero components, but also sparsity in the different regression parameter values for adjacent variables. It considers first order differences, which are related to derivatives of functions, but one could also consider second (or higher) order differences.

Finally, one may want to enforce that parameters are positive or that first differences are positive. This suggests to consider, respectively, for positivity

$$
\widehat{\vartheta} \in \underset{\vartheta}{\arg \min }\left(\sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)+\sum_{j=1}^{r} \eta_{j}\left(0-\vartheta_{j}\right)_{+}\right)
$$

and to enforce a monotone increasing property

$$
\widehat{\vartheta} \in \underset{\vartheta}{\arg \min }\left(\sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)+\sum_{j=1}^{r} \eta_{j}\left(\vartheta_{j-1}-\vartheta_{j}\right)_{+}\right)
$$

where the function

$$
u \mapsto(u)_{+}=\max \{u, 0\}=u \mathbb{1}_{\{u>0\}}
$$

considers only the positive part. This function is called rectified linear unit (ReLU) function in machine learning, but it is also known as the ramp function or the hinge function, and it is the crucial object in European call and put pricing in financial mathematics.

# 2.5 Outlook 

We have introduced all the technical and mathematical tools to now dive into predictive modeling. Roughly speaking, there are three main types of regression model classes that are used for actuarial modeling. (1) There are parametric GLM-type models, these include feed-forward neural networks, recurrent and convolutional neural networks as well as transformers. These models have in common that the architecture is fixed before model fitting, and this gives a fixed number of parameters $\vartheta$ to be determined. (2) There are no-parametric regression tree-type models, these include random forests and gradient boosting machines. These models have in common that we do not start from a fixed complexity, but we let the models grow during fitting by searching for more structure in the data. (3) There are nearest neighbor and kernel based models. These models are

## Page 48
based on topologies and adjacency relations, under the assumption that locally we have similar predictions, and these predictions can be obtained by locally smoothing the noisy responses. For example, local regression and isotonic regression belong to this class.

## Page 49
# Chapter 3 

## Generalized linear models

Generalized linear models (GLMs) are the core models in predictive modeling, and, still today, they are the state-of-the-art in practice for solving actuarial and financial problems because they have many advantages over more advanced (and more complicated) machine learning models; we refer to the introduction to Chapter 2. GLMs were introduced in 1972 by Nelder-Wedderburn [164] and the standard monograph on GLMs is the book of McCullagh-Nelder [150]. This chapter on GLMs will set the stage for later chapters on machine learning methods and AI tools. In these later chapters, we will see that neural networks can be seen as a generalization of GLMs.
GLMs are based on the EDF (2.1). Model fitting is done by MLE which can either be achieved by maximizing the log-likelihood function of the selected EDF (2.1) or by minimizing the corresponding deviance loss function, see (2.6) and Table 2.2. Numerical optimization for parameter fitting is usually done by Fisher's scoring method and the iteratively re-weighted least squares (IRLS) algorithm; this is one of the key contributions in the original work of Nelder-Wedderburn [164].

### 3.1 Generalized linear model regressions

This section is sightly more technical because it lays the foundation for any other regression approach, and once we have provided the full details within a GLM framework, later chapters will be more straightforward.

### 3.1.1 Generalized linear model regression functions

Consider $q$-dimensional real-valued covariates $\boldsymbol{X}=\left(X_{1}, \ldots, X_{q}\right)^{\top}$; for covariate preprocessing we refer to Section 2.3. For a GLM regression function one selects a smooth and strictly increasing link function $g$, and defines the class of (parametrized) regression functions $\mathcal{M}=\left\{\mu_{\vartheta}\right\}_{\vartheta}$ by

$$
\boldsymbol{X} \mapsto g\left(\mu_{\vartheta}(\boldsymbol{X})\right)=\vartheta_{0}+\sum_{j=1}^{q} \vartheta_{j} X_{j}=:\langle\vartheta, \boldsymbol{X}\rangle
$$

for a given regression parameter $\vartheta \in \mathbb{R}^{q+1}$. Thus, after applying the link function $g$, one postulates a linear functional form in the components of $\boldsymbol{X}$, expressed by the scalar

## Page 50
(dot) product $\langle\vartheta, \boldsymbol{X}\rangle$ between $\vartheta$ and $\boldsymbol{X}$; we implicitly extend the covariate $\boldsymbol{X}$ by a bias component $X_{0} \equiv 1$ in this GLM chapter, see (2.9). The parameter $\vartheta_{0}$ is called intercept or bias. In this chapter, $\vartheta \in \mathbb{R}^{q+1}$ is generally a $(q+1)$-dimensional vector; for the chosen notation we also refer to the footnote on page 16 .

The GLM assumption (3.1) provides the following GLM structure for the conditional mean of the response $Y$, given the covariates $\boldsymbol{X}$,

$$
\mu_{\vartheta}(\boldsymbol{X})=\mathbb{E}[Y \mid \boldsymbol{X}]=g^{-1}\langle\vartheta, \boldsymbol{X}\rangle
$$

Example 3.1 (log-link GLM, revisited). The most popular link function in actuarial pricing is the log-link $g(\cdot)=\log (\cdot)$. This log-link GLM has already been introduced in Section 1.3, in particular, we refer to the regression function defined in (1.3) and (1.4), respectively. We can rewrite this conditional mean functional as

$$
\boldsymbol{X} \mapsto \mu_{\vartheta}(\boldsymbol{X})=\mathbb{E}[Y \mid \boldsymbol{X}]=\exp \langle\vartheta, \boldsymbol{X}\rangle=e^{\vartheta_{0}} \prod_{j=1}^{q} e^{\vartheta_{j} X_{j}}
$$

This is a multiplicative best-estimate pricing structure with price factors (price relativities) $e^{\vartheta_{j} X_{j}}$. This multiplicative pricing structure is transparent and interpretable, e.g., if $\vartheta_{j}>0$ we can easily read off the increase in best-estimate implied by an increase in $X_{j}$. The bias term $e^{\vartheta_{0}}$ gives the base premium and the calibration of the GLM (note that the base premium is not the same as the average premium, the latter averages over the covariate distribution $\boldsymbol{X} \sim \mathbb{P}$ and considers the entire regression parameter $\vartheta$ ). Shifting the bias term $\vartheta_{0}$ shifts the average price level.

Figure 3.1: GLM regression function $\boldsymbol{X} \mapsto \mu_{\vartheta}(\boldsymbol{X})$ with log-link.

Figure 3.1 shows a log-link GLM regression function $\boldsymbol{X} \mapsto \mu_{\vartheta}(\boldsymbol{X})=\exp \langle\vartheta, \boldsymbol{X}\rangle$, with a two-dimensional covariate $\boldsymbol{X} \in \mathbb{R}^{2}$ and a regression parameter $\vartheta \in \mathbb{R}^{3}$. The first component $X_{1} \in[18,90]$ models the age of the policyholder, given on the $x$-axis of the graph, and the second component $X_{2} \in\{0,1\}$ is a binary categorical component
![Page 50 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p50_img1.jpg)

## Page 51
with $X_{2}=0$ for male and $X_{2}=1$ for female (blue and red colors). That is, it uses dummy coding with male being the reference level, see (2.14). The choice of the log-link gives the easy interpretation that females differ from males (at the same age $X_{1}$ ) by a multiplicative factor of $e^{\vartheta_{2}}$, the selected regression parameter $\vartheta_{2}<0$ is negative in the picture. Increasing age $X_{1}$ by one year, increases the best estimate by a multiplicative factor of $e^{\vartheta_{1}}$, since the selected regression parameter $\vartheta_{1}>0$ is positive, here. Finally, the bias term $e^{\vartheta_{0}}$ globally shifts (calibrates) the overall level.

Figure 3.1 gives a nice picture of a transparent and interpretable regression function based on the log-link, and it shows the main advantages of using the log-link. In practice, this regression function is not known and needs to be estimated from noisy data, i.e., we need to find the (true) regression parameter $\vartheta \in \mathbb{R}^{q+1}$ from a (noisy) learning sample $\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$, after having chosen a suitable link function $g$. We could just select any strictly consistent loss function $L$, see Section 1.4, and then perform model fitting, or rather loss minimization ${ }^{1}(2.8)$, to find a regression parameter estimate $\widehat{\vartheta}$ for $\vartheta$. We have seen three examples of that type for the log-link GLM, see Examples 1.2, 1.6 and 1.7. However, we have argued in Section 1.4.3 that on finite samples $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$ one can find the most accurate models (on average) if the selected strictly consistent loss function $L$ reflects the properties of the responses $\left(Y_{i}\right)_{i=1}^{n}$; this is grounded in the theoretical work of Gourieroux et al. [87].
Select the member of the EDF that is a reasonable distributional choice for the responses, given the covariates, and set the assumption

$$
\left.Y_{i}\right|_{\boldsymbol{X}_{i}} \sim \operatorname{EDF}\left(\theta\left(\boldsymbol{X}_{i}\right), \varphi / v_{i}, \kappa\right)
$$

That is, we make the canonical parameter $\theta=\theta\left(\boldsymbol{X}_{i}\right) \in \boldsymbol{\Theta}$ dependent on the covariates. Assuming the GLM regression structure (3.1), applying the EDF mean property (2.2), and using the one-to-one correspondence between the canonical parameter and the mean gives us

$$
g\left(\kappa^{\prime}(\theta)\right)=\langle\vartheta, \boldsymbol{X}\rangle
$$

or equivalently, using the canonical link $h=\left(\kappa^{\prime}\right)^{-1}$ of the selected EDF, we can solve this for the canonical parameter

$$
\theta=\theta(\boldsymbol{X})=\theta_{\vartheta}(\boldsymbol{X})=h\left(g^{-1}\langle\vartheta, \boldsymbol{X}\rangle\right)
$$

This explains the relationship between the canonical parameter $\theta=\theta(\boldsymbol{X})=\theta_{\vartheta}(\boldsymbol{X}) \in \boldsymbol{\Theta}$ of the selected EDF and the selected GLM regression function. The unknown regression parameter $\vartheta \in \mathbb{R}^{q+1}$ enters this canonical parameter; pay attention to the distinguished use of $\theta \in \boldsymbol{\Theta}$ for the canonical parameter and $\vartheta \in \mathbb{R}^{r+1}$ for the regression parameter.

[^0]
[^0]:    ${ }^{1}$ Often we call minimization of a loss function as 'model fitting', however, at the current stage we do not really have a 'model', but only a regression function assumption, see page 32. For having a 'model', we also need a distributional assumption. This is often disregarded within the machine learning community, but this has played a key role in advancing actuarial modeling, see, e.g., the claims reserving uncertainty results developed by Mack [146].

## Page 52
# 3.1.2 Canonical link 

From (3.4) we observe that there is a distinguished link choice for a GLM, called the canonical link choice. Namely, select $g=h$. In the case of this canonical link choice $g=h$, the canonical parameter coincides with the linear predictor

$$
\theta_{\vartheta}(\boldsymbol{X})=\langle\vartheta, \boldsymbol{X}\rangle
$$

Mathematically speaking, the canonical link choice has some real advantages, e.g., MLE is always a concave maximization problem and, thus, a solution is unique (supposed we have a full rank design matrix $\boldsymbol{X}$ ). However, practical needs often overrule mathematical properties, for a dozen of other reasons the modeler typically prefers the log-link for $g$. The log-link is the canonical link (if and only if) we select the Poisson model within the EDF. Therefore, in many regression problems, we do not work with the canonical link for $g$.

| distribution | canonical link $h(\mu)$ | $\boldsymbol{\Theta}$ | $\kappa^{\prime}(\hat{\boldsymbol{\Theta}})$ |
| :-- | :--: | :--: | :--: |
| Gaussian distribution | $\mu$ | $\mathbb{R}$ | $\mathbb{R}$ |
| Poisson distribution | $\log (\mu)$ | $\mathbb{R}$ | $(0, \infty)$ |
| Tweedie's CP distribution | $\mu^{1-p} /(1-p)$ | $(-\infty, 0)$ | $(0, \infty)$ |
| gamma distribution | $-1 / \mu$ | $(-\infty, 0)$ | $(0, \infty)$ |
| inverse Gaussian distribution | $-1 /\left(2 \mu^{2}\right)$ | $(-\infty, 0]$ | $(0, \infty)$ |
| Bernoulli distribution | $\log (\mu /(1-\mu))$ | $\mathbb{R}$ | $(0,1)$ |

Table 3.1: Canonical link $h(\mu)=\left(\kappa^{\prime}\right)^{-1}(\mu)$ of selected EDF distributions.

Table 3.1 shows the canonical links $h$ of the most popular members of the EDF. Usually, the canonical link is chosen for $g$ in case of the Gaussian, the Poisson and the Bernoulli models. In these cases we have an effective domain $\boldsymbol{\Theta}=\mathbb{R}$, and, as a result, there is no domain conflict resulting from the linear predictor (3.5) for any possible choices of the covariates $\boldsymbol{X} \in \mathbb{R}^{q}$. This does not hold in the other cases, e.g., in the gamma case we have a one-side bounded effective domain $\boldsymbol{\Theta}=(-\infty, 0)$. This gives constraints on the possible choices of $\vartheta$ and $\boldsymbol{X}$ in (3.5) to have a well-defined model. This difficulty can be circumvented in the gamma case by selecting the log-link for $g$, i.e.,

$$
\theta_{\vartheta}(\boldsymbol{X})=h\left(g^{-1}\langle\vartheta, \boldsymbol{X}\rangle\right)=-1 / \exp \langle\vartheta, \boldsymbol{X}\rangle=-\exp \langle-\vartheta, \boldsymbol{X}\rangle<0
$$

being a well-defined canonical parameter for any $\vartheta \in \mathbb{R}^{q+1}$ and $\boldsymbol{X} \in \mathbb{R}^{q}$. This is a main reason in practice to choose a link function $g$ different from the canonical link $h$ of the selected EDF distribution.
We also remark that the balance property that is going to be introduced in Section 4.1, below, is important in insurance pricing. This balance property is only (if and only if) fulfilled for MLE fitted GLMs if we work with the canonical link $g=h$. Otherwise, a balance correction will be necessary; for more discussion we also refer to LindholmWüthrich [140].

## Page 53
# 3.2 Generalized linear model fitting 

There remains fitting the regression function (3.1) based on a learning sample $\mathcal{L}=$ $\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$. As outlined in Section 2.1.3, there are two different ways to receive the MLE of $\vartheta$. We can either maximize the log-likelihood function or we can minimize the corresponding deviance loss function.

### 3.2.1 MLE via log-likelihoods

For the given learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$ we receive the log-likelihood function under the previous choices (and assuming independence between the instances), see (2.1),

$$
\vartheta \mapsto \ell(\vartheta)=\sum_{i=1}^{n} \frac{v_{i}}{\varphi}\left[Y_{i} \theta_{\vartheta}\left(\boldsymbol{X}_{i}\right)-\kappa\left(\theta_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)\right]+c\left(Y_{i}, \varphi / v_{i}\right)
$$

where $\theta_{\vartheta}\left(\boldsymbol{X}_{i}\right)$ contains the regression parameter $\vartheta$, see (3.4). Solving the resulting maximization problem gives the MLE, subject to existence,

$$
\widehat{\vartheta}^{\mathrm{MLE}} \in \underset{\vartheta}{\arg \max } \ell(\vartheta)
$$

One may argue that working with the log-likelihood function (3.6) looks too complicated because the formula seems quite involved. In all future derivations we will translate the MLE problem (3.7) to the corresponding deviance loss minimization problem.

### 3.2.2 MLE via deviance loss functions

We translate the selected EDF to the corresponding deviance loss function $L$, see (2.6) and Table 2.2. This gives us the (same) MLE as in (3.7) by solving the minimization problem

$$
\widehat{\vartheta}^{\mathrm{MLE}} \in \underset{\vartheta}{\arg \min } \sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)
$$

for the GLM regression function

$$
\boldsymbol{X} \mapsto \mu_{\vartheta}(\boldsymbol{X})=g^{-1}\langle\vartheta, \boldsymbol{X}\rangle
$$

Version March 3, 2025, @AI Tools for Actuaries

## Page 54
# Regression fitting problem 

The regression fitting problem (3.8) is now in an attractive form that is going to be used throughout and in more generality below according to the following recipe:
(1) Specify the distributional model within the EDF for modeling the responses $Y$, given $\boldsymbol{X}$; see (3.3). This gives us the choice of the cumulant function $\kappa$.
(2) The choice of the cumulant function $\kappa$ is translated to the corresponding deviance loss function $L$ by (2.6), see, e.g., Table 2.2.
(3) Then, one can choose any family $\mathcal{M}=\left\{\mu_{\vartheta}\right\}_{\vartheta}$ of regression functions $\mu_{\vartheta}$ : $\mathcal{X} \rightarrow \mathbb{R}$, and the optimal one is found by solving (3.8) for this family $\mathcal{M}$.

- Outlook: This procedure is fairly general, as it does not require a GLM family for $\mathcal{M}$. In fact, it can be a general class of regression models, not necessarily being a non-parametric one. Below, we are going to use neural networks or regression trees for $\mathcal{M}$, and the foundation of their fitting/learning always lies in solving (3.8). Thus, all that we need to do is to select the 'right' strictly consistent loss function $L$ for mean estimation, and then we solve (3.8) for the selected regression model class $\mathcal{M}$.


### 3.2.3 Numerical solution of the GLM problem

Coming back to the GLM model class (3.9) for $\mathcal{M}$ in (3.8). Computationally, this can be solved either by Fisher's scoring method or by the IRLS algorithm. ${ }^{2}$ Basically, this fully solves the GLM fitting problem and we obtain the MLE fitted GLM regression function $\boldsymbol{X} \mapsto \mu_{\hat{\vartheta} \mathrm{MLE}}(\boldsymbol{X})$. We give some remarks:

- For GLM fitting we always require the design matrix $\mathfrak{X}$ to have full rank $q+1 \leq n$. For categorical inputs this requires dummy coding, see Section 2.3.2.
- Under the canonical link choice $g=h$, the deviance loss minimization (3.8) is convex. Thus, a solution is always unique.
- For non-canonical link choices, the objective function in (3.8) is not necessarily convex, and this needs to be checked case by case; compare Examples 5.5 and 5.6 of Wüthrich-Merz [243] which show that the gamma log-link GLM is a convex fitting problem, whereas the inverse Gaussian log-link GLM is not.

We can then apply the model validation and model selection tools of Chapter 1 such as cross-validation. One could also compute a regularized MLE, e.g., adding a LASSO penalization to (3.8) to receive a sparse GLM, see Section 2.4. For a more detailed outline

[^0]
[^0]:    ${ }^{2}$ One could also use the gradient descent methods described in Section 5.3, below. Gradient descent has the advantage of being able to deal with big data and big models, Fisher's scoring method and the IRLS algorithm usually converge faster, because they do not only consider the gradient, but also the second derivatives (Hessians). The size of the data and the model will decide whether these Hessians can be computed efficiently.

## Page 55
about model fitting and validation we refer to Wüthrich-Merz [243, Chapter 5], and we discuss some GLM related techniques in Section 3.3, below.

Remark 3.2. In general, the GLM fitted model does not fulfill the balance property discussed below in (4.4). Therefore, one often adjusts the estimated bias term $\widehat{\vartheta}_{0}^{\text {MLE }}$ to rectify this balance property. An exception is the choice of the canonical link $g=h$ under which the balance property always holds, i.e., under the canonical link choice, the GLM estimated model is an (in-sample) re-allocation of the totally observed claim; this is explained below in Section 4.1, and we also refer to Lindholm-Wüthrich [140].

# 3.3 Likelihood-ratio test 

### 3.3.1 Introduction

First model validation and model selection tools have been introduced in Chapter 1, and we are going to discuss more tools in Chapter 4, below. All these tools are model-agnostic, meaning that they can be applied to any class of regression problems and models. A little bit less general are AIC and BIC, discussed in Section 1.5.3, because they require MLE fitted models. Apart from that AIC and BIC are still general, e.g., we can compare a MLE fitted Poisson GLM to a MLE fitted negative binomial GLM, even if they have completely different GLM functions. In this section we discuss the likelihood ratio test (LRT) and the Wald test which require nested GLMs to be applicable.
Under fairly general assumptions, MLE is consistent and asymptotically normal, meaning that for increasing sample sizes $n \rightarrow \infty$, the MLE $\widehat{\vartheta}^{\text {MLE }}$ converges to the true parameter $\vartheta^{*}$, supposed that the true model is a GLM with the same parametrization. The speed of convergence is determined by the inverse of Fisher's information matrix. This links to Gourieroux et al. [87, Theorem 4] who prove that this Fisher's information matrix is minimal if we select the deviance loss function of the correct EDF under which the data has been generated. In Gourieroux et al. [87], this is called best asymptotically normal, and it means that this deviance loss function choice provides on average the best finite sample behavior in regression parameter estimation. These asymptotic normality results are at the heart of the LRT and the Wald test, which we present next.

### 3.3.2 Lab: a real data example

The analysis in the next section is based on an explicit real data example. We use the well-known French motor third party liability (MTPL) claims frequency data set freMTPL2freq of Dutang et al. [60]. We apply the same data cleaning as described in Wüthrich-Merz [243, Appendix B], and we apply the identical partition into learning sample $\mathcal{L}$ and test sample $\mathcal{T}$ as in that reference; ${ }^{3}$ see Wüthrich-Merz [243, Listing 5.2 and Table 5.2]. Also further chapters of these notes will be based on this data set and on this partition.

[^0]
[^0]:    ${ }^{3}$ The cleaned French MTPL claims frequency data can be downloaded from https://people.math. ethz.ch/ wueth/Lecture/freMTPL2freqClean.rda. The label LearnTest with levels 'L' and 'T' indicates whether the instances belong to the learning sample $\mathcal{L}$ or the test sample $\mathcal{T}$.

## Page 56
We then pre-process the covariates, and we fit a Poisson log-link GLM to the learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$, i.e., using the Poisson deviance loss for $L$, we solve

$$
\begin{aligned}
\widehat{\vartheta}^{\mathrm{MLE}} & =\underset{\vartheta \in \mathbb{R}^{q+1}}{\arg \min } \frac{1}{n} \sum_{i=1}^{n} v_{i} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right) \\
& =\underset{\vartheta \in \mathbb{R}^{q+1}}{\arg \min } \frac{1}{n} \sum_{i=1}^{n} 2 v_{i}\left(\mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)-Y_{i}-Y_{i} \log \left(\frac{\mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)}{Y_{i}}\right)\right) \\
& =\underset{\vartheta \in \mathbb{R}^{q+1}}{\arg \min } \frac{1}{n} \sum_{i=1}^{n} 2\left(v_{i} \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)-N_{i}-N_{i} \log \left(\frac{v_{i} \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)}{N_{i}}\right)\right)
\end{aligned}
$$

This is precisely Example 2.2. Recall, $Y_{i}=N_{i} / v_{i}$ are the observed claims frequencies, if $N_{i} \in \mathbb{N}_{0}$ denote the observed claims counts.
The results of the GLM fitting procedure are presented in Listing 3.1, below. We discuss this example in the next section, and a more detailed description and analysis of this GLM example is contained in the accompanying notebook on GLMs; see
notebook-insert-link

# 3.3.3 Likelihood ratio test and Wald test 

The LRT and the Wald test are two MLE-based model selection tools that allow one to perform (in-sample) model selection. A necessary requirement to be able to apply these two tests is that we compare two nested GLMs. Two GLMs for $Y$, given $\boldsymbol{X}$, are nested if they are based on the same EDF distribution (3.3), and if their only difference is that one model is bigger including the other one as a special case (via the regression function). Call the bigger model the 'full model' and assume it has a regression function

$$
g\left(\kappa^{\prime}\left(\theta_{\vartheta^{\text {full }}}(\boldsymbol{X})\right)\right)=\left\langle\vartheta^{\text {full }}, \boldsymbol{X}\right\rangle=\vartheta_{0}^{\text {full }}+\sum_{j=1}^{q} \vartheta_{j}^{\text {full }} X_{j}
$$

with $(q+1)$-dimensional regression parameter $\vartheta^{\text {full }} \in \mathbb{R}^{q+1}$. A smaller nested model is obtained by setting some of these regression parameter components equal to zero, i.e., dropping the corresponding covariate components from the model. Since the ordering of the covariate components in $\boldsymbol{X}$ is arbitrary, we can assume w.l.o.g. that we want to set the last components to zero. Thus, we consider a nested (null-hypothesis) model

$$
g\left(\kappa^{\prime}\left(\theta_{\vartheta^{\mathrm{H} 0}}(\boldsymbol{X})\right)\right)=\vartheta_{0}^{\mathrm{H} 0}+\sum_{j=1}^{q^{\prime}} \vartheta_{j}^{\mathrm{H} 0} X_{j}
$$

with $q^{\prime}<q$. This nested model has a $\left(q^{\prime}+1\right)$-dimensional regression parameter $\vartheta^{\mathrm{H} 0} \in$ $\mathbb{R}^{q^{\prime}+1}$. We can now set up a statistical test for the null-hypothesis that the data has been generated by the smaller nested model (3.12) against the alternative of the full model (3.11). Based on the learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$, we estimate in both models the regression parameter with MLE, providing us with the MLEs $\widehat{\vartheta}^{\text {full }}$ in the full model and $\widehat{\vartheta}^{\mathrm{H} 0}$ in the nested model, respectively. The resulting likelihood ratio of the two fitted models gives us, refer to (2.1) for the EDF densities,

$$
\frac{\prod_{i=1}^{n} f_{\theta_{\widehat{\vartheta} \text { H0 }}\left(\boldsymbol{X}_{i}\right)}\left(Y_{i}\right)}{\prod_{i=1}^{n} f_{\theta_{\widehat{\vartheta} \text { full }}\left(\boldsymbol{X}_{i}\right)}\left(Y_{i}\right)} \leq 1
$$

## Page 57
This likelihood ratio is upper bounded by one because we apply MLE to two nested models; the one in the nominator having more degrees of freedom in MLE. The rationale behind the LRT now is as follows. If this ratio is fairly close to one, the null-hypothesis model is as good as the full model, and one cannot reject the null-hypothesis that the data has been generated by the smaller model.
The test statistics (3.13) is not in a convenient form and, instead, one considers a logged version thereof

$$
T=-2 \sum_{i=1}^{n}\left(f_{\theta_{\overline{2} \mathrm{H} 0}\left(\boldsymbol{X}_{i}\right)}\left(Y_{i}\right)-f_{\theta_{\overline{2} \text { full }}\left(\boldsymbol{X}_{i}\right)}\left(Y_{i}\right)\right) \geq 0
$$

If this test statistics $T$ is large, the null-hypothesis should be rejected. Using asymptotic MLE theory, the distribution of this test statistics $T$ under the null-hypothesis can be approximated by a $\chi^{2}$-distribution with $q-q^{\prime}$ degrees of freedom; see Fahrmeir-Tutz [65, Section 2.2.2].

Figure 3.2: $\chi^{2}$-density rejection area (in orange) for a significance level of $5 \%$ with $q-q^{\prime}=$ 3 degrees of freedom.

Figure 3.2 shows in orange color the rejection region for the test statistics $T$ defined in (3.14) on a significance level of $5 \%$ for dropping $q-q^{\prime}=3$ covariate components from $\boldsymbol{X}$. If the learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$ provides an observed test statistics $T$ that has a $p$-value less than $5 \%$ (lies in the orange region) we reject the null-hypothesis on this significance level and we go for the bigger model, otherwise this LRT does not support working with the bigger model.

We give some remarks.

- The LRT test statistics $T$ in (3.14) can also be expressed as a difference of deviance losses. It then receives the interpretation of measuring the distance of the two models to the empirical sample in terms of a KL divergence; see Wüthrich-Merz [243, Section 5.1.7].
![Page 57 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p57_img1.jpg)

## Page 58
- The LRT can only be applied to nested models, i.e., with responses having the same distributions under both models, and one having a nested regression function within the other one. For non-nested models, only AIC (1.19) and BIC (1.20) apply. Alternatively, we could employ (group) LASSO regularization during model fitting, see Section 2.4. This already leads to sparsity and parsimony during model fitting, but it requires fine-tuning of the regularization parameter $\eta$. Often, LASSO is only used for parameter (covariate) selection, and once the covariates are selected, in an additional step, a non-regularized GLM is fitted.
- The LRT requires that we fit two models, the full model and the nested model. The Wald test [230] is rather similar but with a smaller computational effort. For the Wald test, one only needs to fit the full model, and the nested one is then approximated by asymptotic MLE arguments. This is computationally more attractive, but it is less accurate because it involves more approximations; see Wüthrich-Merz [243, Section 5.3.2].
- The LRT test statistics (3.14) requires the true dispersion parameter $\varphi$. Usually, this is not available. However, if we estimate this dispersion parameter by MLE (consistently in a statistical sense) in the bigger (full) model, the asymptotic normality results carry over to the case with consistently estimated dispersion parameter.

We illustrate the LRT and the Wald test on the French MTPL claims frequency data introduced in Section 3.3.2. Listing 3.1 shows the results of the fitted Poisson log-link GLM (3.10). We consider 5 covariates: a continuous covariate DrivAge which was discretized into age classes and which was then implemented by dummy coding, the categorical VehBrand variable implemented by dummy coding, a binary VehGas variable also implemented by dummy coding, and two continuous variables Density and Area. This results in a regression parameter $\vartheta \in \mathbb{R}^{q+1}$ of dimension $q+1=20$.
The last column p value of Listing 3.1 shows the $p$-values of the Wald tests. As explained above, these Wald tests are essentially the same as the LRTs, but with less computational efforts because only the full model needs to be fitted, and we do not need to refit a nullhypothesis model for all $q+1=20$ Wald tests in Listing 3.1. These Wald tests consider dropping one component of $\vartheta$ at a time against the full model. As a result, we cannot just drop all the variables that have a small $p$-value because simultaneous consideration of multiple individual variable droppings is not a nested model consideration. That is, a multiple comparison does not work if these multiple models are not nested. In other words, variable dropping needs to be done recursively, i.e., once we have dropped the least significant variable, we have a new full model, and we need to re-perform the whole exercise based on this new full model. This precisely results in the variable selection process that is typically known as backward selection, because every Wald or LRT has to be done recursively in a full vs. null-hypothesis model context. If this model reduction is combined with increasing a model by adding (new) variables, it is called backward-forward-stepwise selection, e.g., we may decide to drop recursively variable A, then variable B, and then variable C, and after these three reductions it may turn out that adding again variable A is beneficial. This allows one to stepwise (recursively) decrease

## Page 59
Listing 3.1: Poisson log-link GLM example on the French MTPL claims frequency data.

```
glm(formula = ClaimNb - DrivAge + VehBrand + VehGas + Density +
    Area, family = poisson(), data = learn, offset = log(Exposure))
Deviance Residuals:
    Min 1Q Median 3Q Max
-0.8890 -0.3393 -0.2535 -0.1387 7.6569
Coefficients:
    Estimate Std. Error z value p value
(Intercept) -3.258957 0.034102 -95.564 < 2e-16 ***
DrivAge18-20 1.275057 0.044964 28.358 < 2e-16 ***
DrivAge21-25 0.641668 0.028659 22.390 < 2e-16 ***
DrivAge26-30 0.153978 0.025703 5.991 2.09e-09 ***
DrivAge41-50 0.121999 0.018925 6.447 1.14e-10 ***
DrivAge51-70 -0.017036 0.018525 -0.920 0.357776
DrivAge71+ -0.047132 0.029964 -1.573 0.115726
VehBrandB2 0.007238 0.018084 0.400 0.688958
VehBrandB3 0.085213 0.025049 3.402 0.000669 ***
VehBrandB4 0.034577 0.034523 1.002 0.316553
VehBrandB5 0.122826 0.028792 4.266 1.99e-05 ***
VehBrandB6 0.080310 0.032325 2.484 0.012976 *
VehBrandB10 0.067790 0.040607 1.669 0.095032 .
VehBrandB11 0.221375 0.043348 5.107 3.27e-07 ***
VehBrandB12 -0.152185 0.020866 -7.294 3.02e-13 ***
VehBrandB13 0.101940 0.047062 2.166 0.030306 *
VehBrandB14 -0.201833 0.093754 -2.153 0.031336 *
VehGasRegular -0.198766 0.013323 -14.920 < 2e-16 ***
Density 0.094453 0.014623 6.459 1.05e-10 ***
Area 0.028487 0.019909 1.431 0.152471
---
Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
(Dispersion parameter for poisson family taken to be 1)
Null deviance: 153852 on 610205 degrees of freedom
Residual deviance: 151375 on 610186 degrees of freedom
AIC: 197067
Number of Fisher Scoring iterations: 6
```

and increase models.
Another issue with the Wald tests in Listing 3.1 is that these tests are performed on the individual components of $\vartheta$. Considering DrivAge and VehBrand, it seems more sensible to consider all components of a dummy coded categorical variable simultaneously, because we want to keep, e.g., VehBrand in the model or not. This requires to consider the whole group at once exactly as in the group LASSO regularization, see (2.26). In the case of VehBrand we can perform the LRT with $q-q^{\prime}=10$ degrees of freedom.
Listing 3.2 shows a LRT analysis that performs LRTs for dropping one variable at a time from the full model, i.e., the resulting five reduced models are always compared to the full model; in R this is called a drop1 analysis. In case of DrivAge we drop 6 regression parameters, in case of VehBrand 10 regression parameters, and in the remaining cases 1 parameter each. This gives the resulting degrees of freedom $q-q^{\prime}$ for the LRTs (and the Wald tests). The $p$-values (in the last column) only support to drop Area. This is also

## Page 60
Listing 3.2: GLM example: drop1 analysis.

```
Single term deletions
Model:
ClaimNb - DrivAge + VehBrand + VehGas + Density + Area
    Df Deviance AIC LRT Pr(>Chi)
<none> 151375 197067
DrivAge 6 152483 198163 1107.98<2.2e-16 ***
VehBrand 10 151550 197222 175.15<2.2e-16 ***
VehGas 1 151598 197287 222.58<2.2e-16 ***
Density 1 151417 197106 41.77 1.029e-10 ***
Area 1 151377 197067 2.05 0.1524
---
Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

justified by AIC (1.19) because dropping Area has roughly the same AIC value as the full model, and because of aiming for parsimony we should go for the smaller model in such a situation. In all other cases, the AIC value increases by dropping the corresponding variables, see Listing 3.2.

Listing 3.3: GLM example: anova analysis.

```
Analysis of Deviance Table
Model: poisson, link: log
Response: ClaimNb
Terms added sequentially (first to last)
Df Deviance Resid. Df Resid. Dev Pr(>Chi)
NULL 610205 153852
DrivAge 6 1174.40 610199 152678 <2e-16 ***
VehBrand 10 156.40 610189 152522 <2e-16 ***
VehGas 1 112.24 610188 152409 <2e-16 ***
Density 1 1032.18 610187 151377 <2e-16 ***
Area 1 2.05 610186 151375 0.1524
~
Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

Finally, we show an analysis in Listing 3.3, where we sequentially add one variable after the other, providing the corresponding reduction in the deviance loss (LRT test statistics). The conclusions are essentially the same as above. A critical point that needs to be emphasized for Listing 3.3 is that the order of inclusion matters in this stepwise forward selections. Changing its order may provide different conclusions. For instance, if two covariate components are highly collinear, then they serve at essentially explaining the same phenomenon, and once we have included the first one, we do not need the second one any more in the model, though the second one may have a marginally slightly better explanatory power (or slightly different interactions with other variables). That is, the order of inclusion matters in these stepwise forward selections, and the $p$-values depend on this order; in the example of Listing 3.3 the variables Density and Area are highly collinear, and by exchanging the order of these two variables in Listing 3.3 gives a high $p$-value to Density. The accompanying notebook on GLMs gives more discussions on this example, see

Version March 3, 2025, @AI Tools for Actuaries

## Page 61
# notebook-insert-link 

We conclude that variable selection is as much art as science. Increasing the size of the model quickly leads to a combinatorial complexity that does not allow one to exploit all possible sub-models (and combinations). This section has been focusing on LRTs and Wald tests because there is a well-founded and understood statistical theory behind the LRT and the Wald test, but, in essence, they are not any different from other model selection procedures. For instance, we can replace all LRTs by LASSO regressions, but then computational efforts will become bigger as LASSO regression needs hyper-parameter (regularization parameter) tuning. This increased computational complexity is common to any machine learning method, because in complex algorithmic models we will no longer be able to rely on an asymptotic likelihood theory. Therefore, first trying to understand the (raw) data is always very beneficial. This allows the modeler to already make a reasonable model choice in the first place, which can then be further refined. Otherwise, we have to go through the tedious backward-forward LRT model selection process because we can only test nested GLMs, and likely we eventually result in a sort of non-uniqueness having equally good non-nested models. This is quite similar to the regression tree constructions below, and in regression trees a technique called pruning is used to select the optimal tree.

## Summary

This chapter has set the ground for machine learning methods by giving the basic tools and intuition from classical statistical and actuarial methods, we especially refer to the boxes on pages 29 and 54, as well as to the Poisson Example 2.2. We are now ready to dive into the theory of machine learning tools.

## Page 62
Version March 3, 2025, @AI Tools for Actuaries

## Page 63
# Chapter 4 

## Interlude

Chapters 1 to 3 introduced statistical methods that are part of the core syllabus of actuarial science, and these chapters have laid a solid foundation for diving into the machine learning tools. We are going to introduce these tools from Chapter 5 onwards. The present chapter discusses some general techniques that are useful in various situations, but which are not strictly necessary to understand the machine learning tools. For this reason, the fast reader may skip this chapter and come back to it at a later stage.

This chapter discusses a collection of different topics:

- We start this chapter by discussing unbiasedness and the balance property. These are important properties in insurance pricing to ensure that the overall price level is not misspecified. Next, we discuss auto-calibration which is another important property that insurance pricing schemes should fulfill.
- In the second part of this chapter, we discuss two general purpose non-parametric regression methods, local regression and isotonic regression. These are useful in various situations.
- In the final part of this chapter, we discuss further model selection tools, such as the Gini score and Murphy's score decomposition. These are model-agnostic tools, i.e., they can be used for any regression method.


### 4.1 Unbiasedness and calibration

### 4.1.1 Statistical biases

Generally, unbiasedness is an important property in actuarial pricing. This applies regardless of what specific meaning we underpin unbiasedness:

- In Section 1.5.1, we discussed the in-sample bias that we need to avoid in model selection, otherwise the predictor may generalize poorly to new data.
- In regression modeling, we want to ensure that the estimated model is void of a statistical bias to ensure that the average price level is not misspecified.

## Page 64
- Most regression models include an intercept term which is the part of the regression function that is not influenced by the covariates, see GLM (3.1). In deep learning, this intercept term is coined bias term, and we need to ensure that it is correctly specified to avoid the statistical bias.
- There is some concern about unfair discrimination in insurance pricing, and algorithmic decision making more generally. Any kind of unfair treatment of individuals or groups with similar features is related to a bias in the model construction and/or the decision making process. This is called an unfair discrimination bias.

In the present section, we focus on the statistical bias which studies the average price level over the entire insurance portfolio. We assume in all considerations that the first moments exist.

Definition 4.1. The regression function $\boldsymbol{X} \mapsto \mu(\boldsymbol{X})$ is (globally, statistically) unbiased for $(Y, \boldsymbol{X}, v)$, if

$$
\mathbb{E}[v \mu(\boldsymbol{X})]=\mathbb{E}[v Y]
$$

Global unbiasedness means that the average price level $\mathbb{E}[v \mu(\boldsymbol{X})]$ provided by the selected regression function $\mu$ is sufficient to cover the portfolio claim $v Y$ on average. This global unbiasedness is stated w.r.t. the population distribution $(Y, \boldsymbol{X}, v) \sim \mathbb{P}$.
If we work with an estimated model $\widehat{\mu}_{\mathcal{L}}$, which has been fitted on a learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$, we typically also average over the learning sample $\mathcal{L}$ to state the global unbiasedness

$$
\mathbb{E}\left[v \widehat{\mu}_{\mathcal{L}}(\boldsymbol{X})\right]=\mathbb{E}[v Y]
$$

assuming that $(Y, \boldsymbol{X}, v)$ is independent of $\mathcal{L}$. This reflects an out-of-sample global unbiasedness verification, see also Section 1.5.1.

We give some remarks.

- The left-hand side of (4.1) reflects that we re-sample both $\mathcal{L}$ and $(\boldsymbol{X}, v)$ to verify this global unbiasedness. In insurance, this may be questionable, as we cannot repeat an experiment, i.e., we only have one past claims history reflected in the learning sample $\mathcal{L}$. Bootstrap may be a way of generating different past histories, however, this in itself maybe problematic because if we have a biased model, this bias remains in the bootstrap samples as we re-simulate from the very same observations, or in other words, a bias remains latent and is not discovered by bootstrapping.
- Global unbiasedness (4.1) also re-samples over the covariates $\boldsymbol{X}$, and an insurer may argue that the company (only) wants to be unbiased for its specific portfolio $\mathcal{T}=\left(Y_{t}, \boldsymbol{X}_{t}, v_{t}\right)_{t=1}^{m}$. This would then result in verifying the conditional global unbiasedness

$$
\sum_{t=1}^{m} v_{t} \mathbb{E}\left[\widehat{\mu}_{\mathcal{L}}\left(\boldsymbol{X}_{t}\right) \mid \boldsymbol{X}_{t}\right]=\sum_{t=1}^{m} v_{t} \mathbb{E}\left[Y_{t} \mid \boldsymbol{X}_{t}, v_{t}\right]
$$

This averages over the learning sample $\mathcal{L}$ on the left-hand side, and over the claims $\left(Y_{t}\right)_{t=1}^{m}$ on the right-hand side, but it keeps the (forecast) portfolio $\left(\boldsymbol{X}_{t}, v_{t}\right)_{t=1}^{m}$ fixed.

## Page 65
Note that (4.2) will also require an assumption about the dependence between $\mathcal{L}$ and $\mathcal{T}$. In fact, one can even go one step further and require that the learning sample $\mathcal{L}$ and the test sample $\mathcal{T}$ have the identical covariates, i.e., working on a fixed portfolio $\left(\boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$ for learning and forecasting. In that case, we require instead

$$
\sum_{i=1}^{n} v_{i} \mathbb{E}\left[\widehat{\mu}_{\mathcal{L}}\left(\boldsymbol{X}_{i}\right) \mid\left(\boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}\right]=\sum_{i=1}^{n} v_{i} \mathbb{E}\left[Y_{i} \mid \boldsymbol{X}_{i}, v_{i}\right]
$$

On both sides, this only averages over the responses. On the left-hand side, these responses reflect past responses in $\mathcal{L}$ used for fitting, and on the right-hand side these are the future claims to be forecast.

- These considerations bear the difficulty that the average claims level on the righthand sides of (4.1)-(4.3) needs to be available, which is typically not the case. That is why we discuss the balance property next.


# 4.1.2 The balance property 

Related to the last item of the previous remarks, we introduce the balance property which is easier to verify. The notion of the balance property has been introduced in BühlmannGisler [35, Theorem 4.5] and it is studied in detail in Lindholm-Wüthrich [140]. The balance property is formulated for an estimation procedure $\mathcal{L} \mapsto \widehat{\mu}_{\mathcal{L}}$, and it refers to a point-wise property in the learning sample $\mathcal{L}$, i.e., for any possible realization of the learning sample.
Definition 4.2. A regression model fitting procedure $\mathcal{L} \mapsto \widehat{\mu}_{\mathcal{L}}$ satisfies the balance property if for a.e. realization of the learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$ the following identity holds

$$
\sum_{i=1}^{n} v_{i} \widehat{\mu}_{\mathcal{L}}\left(\boldsymbol{X}_{i}\right)=\sum_{i=1}^{n} v_{i} Y_{i}
$$

We give some remarks.

- The balance property is an in-sample property that holds for almost every (a.e.) realization of the learning sample $\mathcal{L}$. A crucial difference to the unbiasedness definitions above is that for verifying the balance property we do not need to know the right price level, but it is fully empirical.
- The correct interpretation of the balance property (4.4) is that we re-allocate the total (aggregate) portfolio claim $\sum_{i=1}^{n} v_{i} Y_{i}$ to all insurance policyholders $1 \leq i \leq n$, such that this collective bears the entire aggregate claim. This view is at the core of insurance, namely, the collective shares all risks (and claims) within the risk community (solidarity).
- Generally, in actuarial science, model fitting procedures that have this balance property should be preferred. MLE estimated GLMs using the canonical link comply with the balance property; see Nelder-Wedderburn [164]. That is, for a MLE fitted GLM we have estimated means

$$
\mu_{\widehat{\vartheta} \mathrm{MLE}}\left(\boldsymbol{X}_{i}\right)=\widehat{\mathbb{E}}\left[Y_{i} \mid \boldsymbol{X}_{i}\right]=g^{-1}\left\langle\widehat{\vartheta}^{\mathrm{MLE}}, \boldsymbol{X}_{i}\right\rangle
$$

## Page 66
These estimated means fulfill the balance property if the selected link $g=h$ was the canonical link of the chosen EDF. Otherwise, the balance property fails to hold. It can be rectified by modifying the intercept estimate

$$
\widehat{\vartheta}_{0}^{\mathrm{MLE}} \mapsto \widehat{\vartheta}_{0}^{\text {corrected }}=\widehat{\vartheta}_{0}^{\mathrm{MLE}}+\delta
$$

for a suitable (data dependent) $\delta \in \mathbb{R}$; this is studied in Lindholm-Wüthrich [140].

- We emphasize that the balance property is an in-sample property. Generally, we expect the mean of the total claim $\sum_{i} v_{i} Y_{i}$ to vary in the future, too, compared to the learning and test samples, e.g., due to inflation or other external factors. In this case, we may want to re-calibrate our model such that the left-hand side of (4.4) matches our global portfolio forecast, integrating any extrapolation consideration and expert knowledge about the future claims level. This can easily be done by shifting the intercept (bias term) similar to (4.5).


# 4.1.3 Auto-calibration 

For actuarial pricing auto-calibration is an important property. We discuss this in this section. Auto-calibration has been introduced by Schervish [199] in the context of meteorology, and it is discussed in the statistical literature by Tsyplakov [221], Menon et al. [153], Gneiting-Ranjan [79], Pohle [177], Gneiting-Resin [80] and Tasche [214]. Actuarial literature discussing auto-calibration is Krüger-Ziegel [127], Denuit et al. [53], Fissler et al. [69], Lindholm et al. [138], Lindholm-Wüthrich [140], Wüthrich [240] and Wüthrich-Ziegel [244].
Definition 4.3. A regression function $\mu: \mathcal{X} \rightarrow \mathbb{R}$ is auto-calibrated for $(Y, \boldsymbol{X})$ if, a.s.,

$$
\mu(\boldsymbol{X})=\mathbb{E}[Y \mid \mu(\boldsymbol{X})]
$$

Assume $\mu(\boldsymbol{X})$ are the actuarial prices that are charged to the insurance policyholders with covariates $\boldsymbol{X}$ to cover their financial risks $Y$. Auto-calibration (4.6) of the pricing functional $\mu: \mathcal{X} \rightarrow \mathbb{R}$ provides the property that every price cohort $\mu(\boldsymbol{X})$ is on average self-financing for its corresponding claims $Y$. Thus, there is no systematic cross-financing (subsidy) between the different price cohorts. This is a property that actuarial pricing schemes should generally fulfill. Figure 4.1 gives an example where price cohort 1 is systematically under-estimated and cross-financed by price cohort 3 .

The following statements are proved in Wüthrich-Buser [241, Section 2.5].

- The true regression function $\mu^{*}$, given in (1.2), is auto-calibrated. This immediately implies that any non-auto-calibrated regression function cannot be the true one.
- The global mean $\mu_{0}:=\mathbb{E}[Y]$, not considering any covariates, is auto-calibrated.
- Typically, there are infinitely many auto-calibrated regression models $\mu: \mathcal{X} \rightarrow \mathbb{R}$.
- Consider any regression function $\mu: \mathcal{X} \rightarrow \mathbb{R}$. The following re-calibration step gives an auto-calibrated regression function

$$
\mu_{\mathrm{rc}}(\boldsymbol{X}):=\mathbb{E}[Y \mid \mu(\boldsymbol{X})]
$$

Version March 3, 2025, @AI Tools for Actuaries

## Page 67
Figure 4.1: Violation of auto-calibration: price cohort 3 cross-subsidizes price cohort 1.

This re-calibration step can be performed empirically by an isotonic regression; we come back to this in Section 4.2.2, below, we also refer to Wüthrich-Ziegel [244].

- From a statistical point of view, we should test any fitted regression model for auto-calibration. Developing powerful statistical tests for auto-calibration is still an open field of research; see Wüthrich [240].

Figure 4.2: Lift plot using decile binning.
Figure 4.2 gives a graphical example of an auto-calibration analysis; it is based on the French MTPL Poisson log-link GLM example introduced in Section 3.3.2.

To analyze auto-calibration in regression fitting one performs a two-step fitting procedure:
(1) In the first step, one fits a (GLM) regression function $\boldsymbol{X} \mapsto \mu(\boldsymbol{X})$ by regressing the responses $Y_{i}$ from the covariates $\boldsymbol{X}_{i}$, i.e., by considering the regression problem
![Page 67 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p67_img1.jpg)
![Page 67 Image 2](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p67_img2.jpg)

## Page 68
$Y_{i} \sim \boldsymbol{X}_{i}$ for independent instances $1 \leq i \leq n$. This first step is performed on the learning sample $\mathcal{L}$. The resulting estimated regression values $\left(\widehat{\mu}\left(\boldsymbol{X}_{t}\right)\right)_{t=1}^{m}$ are plotted on the $x$-axis in Figure 4.2; these are shown out-of-sample on the test sample $\mathcal{T}$.
(2) To assess the auto-calibration property of this fitted regression function $\widehat{\mu}(\cdot)$, one applies a second regression step. This second fitting step is a "regression on the regression", i.e., one regresss the responses $Y_{t}$ but this time from the real-valued estimates $\widehat{\mu}\left(\boldsymbol{X}_{t}\right)$, i.e., by considering the regression problem $Y_{t} \sim \widehat{\mu}\left(\boldsymbol{X}_{t}\right)$ for the independent instances $1 \leq t \leq m$. This second step is performed on the test sample $\mathcal{T}$. These second fitted regression values are plotted on the $y$-axis in Figure 4.2, and they provide us with the blue dots in Figure 4.2. If these blue dots are on the orange diagonal line we have a perfectly auto-calibrated model.

We need suitable regression techniques to perform this second regression step $Y_{t} \sim \widehat{\mu}\left(\boldsymbol{X}_{t}\right)$. In Sections 4.2.1 and 4.2.2, below, we meet two non-parametric regression methods that may serve at performing this second regression step. The method used in Figure 4.2 is a more simple one. It uses a discrete binning w.r.t. the empirical deciles of $\left(\widehat{\mu}\left(\boldsymbol{X}_{t}\right)\right)_{t=1}^{m}$, and then it computes the empirical means of the responses belonging to the corresponding bins (and on the $x$-axis we select the barycenters of the bins).
The resulting two-step fitting procedure is illustrated by the blue dots in Figure 4.2, and they are compared to the orange diagonal line. If the blue dots lie on this orange diagonal line, the second regression step does not learn any new estimated means compared to the first estimates $\widehat{\mu}$. This indicates that auto-calibration holds for $\widehat{\mu}$. From Figure 4.2, there is some indication that on some values $\widehat{\mu}\left(\boldsymbol{X}_{t}\right)$ the average responses are misspecified, $\widehat{\mu}\left(\boldsymbol{X}_{t}\right) \neq \mathbb{E}\left[Y_{t} \mid \widehat{\mu}\left(\boldsymbol{X}_{t}\right)\right]$, and, thus, these insurance policies are likely cross-subsidized by other policies to cover the entire portfolio claim. It is also striking that there seems to be non-monotonicity in the blue dots, which indicates that first regression function $\left(\widehat{\mu}\left(\boldsymbol{X}_{t}\right)\right)_{t=1}^{m}$ does not provide the correct ranking.
Note that the type of plot in Figure 4.2 has different names, sometimes they are called lift plots, auto-calibration plots or T-reliability diagrams; see Gneiting-Resin [80]. There is not a unique terminology for these kinds of plots, and sometimes it is even contradictory. In some cases, plots that show both regression steps on the $x$-axis are called lift plots, and in some literature the cumulative accuracy profile, studied in Section 4.3.1, below, is called lift plot.

# 4.2 General purpose non-parametric regressions 

In the previous section on auto-calibration, we have seen that it is sometimes useful to have a general purpose non-parametric regression tool. In this section, we introduce two such tools, local regression and isotonic regression, and we are going to revisit Figure 4.2 with these new tools.

### 4.2.1 Local regression

We start by discussing a non-parametric local regression method. This non-parametric local regression method is based on splines and it gives us a general purpose tool to smooth

## Page 69
graphs and results. The standard reference for local regression is Loader [142], who is also the owner of the R package locfit; the present section is taken from Loader [142, Chapter 2]. The goal is to locally fit a non-parametric polynomial regression function to a sample $\left(Y_{i}, X_{i}, v_{i}\right)_{i=1}^{n}$ that has one-dimensional real-valued covariates $X_{i} \in \mathbb{R}$.
Assume we want to fit a regression value $\widehat{\mu}^{\text {loc }}(X)$ in a fixed covariate value $X \in \mathbb{R}$ by only considering the instances $\left(Y_{i}, X_{i}, v_{i}\right)$ with covariates $X_{i}$ in the neighborhood of $X$. First, we select a bandwidth $\delta(X)>0$ to define the smoothing window

$$
\Delta(X)=(X-\delta(X), X+\delta(X))
$$

This determines the neighborhood around $X$. Only instances with $X_{i} \in \Delta(X)$ are considered for estimating $\widehat{\mu}^{\text {loc }}(X)$. Second, we introduce a weighting function. Often the tricube weighting function $w(u)=(1-|u|^{3})^{3}$ is used, $u \in[-1,1]$. This weights the instances $i$ within the smoothing window w.r.t. their relative distances $u_{i}=\left(X_{i}-\right.$ $X) / \delta(X)$ to $X$. The goal then is to fit a spline to the weighted observations in this smoothing window. For illustration, let us select a quadratic spline

$$
x \mapsto \mu_{\vartheta}(x ; X)=\vartheta_{0}+\vartheta_{1}(x-X)+\vartheta_{2}(x-X)^{2}
$$

with regression parameter $\vartheta=\left(\vartheta_{j}\right)_{j=0}^{3} \in \mathbb{R}^{3}$. This motivates us to consider the following weighted local regression problem around $X$

$$
\widehat{\vartheta}=\underset{\vartheta}{\arg \min } \sum_{i=1}^{n} v_{i} \mathbb{1}_{\left\{X_{i} \in \Delta(X)\right\}} w\left(\frac{X_{i}-X}{\delta(X)}\right)\left(Y_{i}-\mu_{\vartheta}\left(X_{i} ; X\right)\right)^{2}
$$

The fitted local regression value in $X$ is then obtained by setting

$$
\widehat{\mu}^{\mathrm{loc}}(X):=\mu_{\widehat{\vartheta}}(X ; X)=\widehat{\vartheta}_{0}
$$

We revisit Figure 4.2 which studies the auto-calibration property of a fitted GLM $\widehat{\mu}$. We revisit the two-step fitting procedure discussed in Section 4.1.3, but this time we apply a local regression for the second fitting step $X_{t} \sim \widehat{\mu}\left(\boldsymbol{X}_{t}\right)$, based on the independent instances $1 \leq t \leq m$. For this, we select quadratic splines, and the bandwidth $\delta(X)$ is chosen such that the smoothing window $\Delta(X)$ contains a nearest neighbor fraction of $\alpha=10 \%$ of the data $\mathcal{T}$. The results are presented in Figure 4.3. The conclusion of this plot is that a priori (without further investigation) we cannot reject the null-hypothesis of having an auto-calibrated GLM $\widehat{\mu}$, because the resulting blue dots fluctuate around the orange diagonal line. The main question is whether these fluctuations are too large, and a second question is why do we not receive a monotone picture. These two issues may indicate that the ordering received by $\left(\widehat{\mu}\left(\boldsymbol{X}_{t}\right)\right)_{t=1}^{m}$ is not correct. But to come to a firm conclusion further analysis is necessary.
Naturally, the hyper-parameters of the nearest neighbor fraction $\alpha \in(0,1]$ and the degree of the splines have a crucial influence on the results, and changing these parameters can provide rather different results. Especially, the choice in the nearest neighbor fraction $\alpha$ can be very sensitive, for a small value of $\alpha$ we do not receive a credible estimate $\widehat{\mu}^{\text {loc }}(X)$ because the (random) noise dominates the systematic effects, and for $\alpha$ close to one, we consider remote instances $i$ from $X$ which may have a completely different systematic response behavior. Thus, there is a critical trade-off between small and large values of nearest neighbor fractions $\alpha$. This also impacts the conclusions gained from Figure 4.3.

## Page 70
Figure 4.3: Lift plot using a local regression fit.

# 4.2.2 Isotonic regression 

A disadvantage of the above local regression is that it is very sensitive in hyper-parameter selection; often more robust methods are preferred. Isotonic regression is a non-parametric regression method that does not involve any hyper-parameter tuning, but it is based on the assumption of isotonicity between the one-dimensional real-valued covariates $X_{i}$ and the regression values $\mu^{*}\left(X_{i}\right)=\mathbb{E}\left[Y_{i} \mid X_{i}\right]$ explaining the responses $Y_{i}$. That is, for an isotonic regression we assume for all $1 \leq i, i^{\prime} \leq n$ the following property to hold

$$
X_{i} \leq X_{i^{\prime}} \quad \Longleftrightarrow \quad \mu^{*}\left(X_{i}\right) \leq \mu^{*}\left(X_{i^{\prime}}\right)
$$

or, in other words, an isotonic regression is rank-preserving.
Isotonic regression goes back to Ayer et al. [8], Brunk et al. [33], Miles [158], Barlow et al. [14], Barlow-Brunk [15], Kruskal [128], and the pool adjacent violators (PAV) algorithm gives a fast implementation for solving an isotonic regression numerically; see Leeuw et al. [133].
To perform an isotonic regression on a sample $\left(Y_{i}, X_{i}, v_{i}\right)_{i=1}^{n}$ with one-dimensional realvalued covariates $X_{i} \in \mathbb{R}$, we assume w.l.o.g. that there are no ties in the covariates, and that the instances are labeled such that $X_{1}<X_{2}<\ldots<X_{n}$. Excluding ties is w.l.o.g. because we can replace instances with ties by merging them and we obtain the same isotonic regression solution. Merging means the following, assume that $X_{i}=\ldots=$ $X_{i+k}$ take the same value. Then, we merge these instances by assigning them to one single instance with covariate $X_{i} \leftarrow X_{i+l}, 0 \leq l \leq k$, with weight and response, respectively,

$$
v_{i} \leftarrow v_{i}+\ldots+v_{i+k} \quad \text { and } \quad Y_{i} \leftarrow \frac{v_{i} Y_{i}+\ldots+v_{i+k} Y_{i+k}}{v_{i}+\ldots+v_{i+k}}
$$

this reduces the sample size, but accounts for this smaller sample size by increasing the corresponding weight. Basically, this merging means that we build sufficient statistics on instances with identical covariates.
![Page 70 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p70_img1.jpg)

## Page 71
The isotonic regression solution $\widehat{\boldsymbol{\mu}}^{\text {iso }} \in \mathbb{R}^{n}$ under the assumption $X_{1}<X_{2}<\ldots<X_{n}$ is obtained by solving the following constraint optimization problem

$$
\widehat{\boldsymbol{\mu}}^{\mathrm{iso}}=\underset{\boldsymbol{\mu} \in \mathbb{R}^{n}}{\arg \min } \sum_{i=1}^{n} v_{i}\left(Y_{i}-\mu_{i}\right)^{2}, \quad \text { subject to } \mu_{1} \leq \ldots \leq \mu_{n}
$$

We give some remarks.
Remarks 4.4. - The isotonic regression (4.9) is based on the (strictly consistent) square loss function for mean estimation. However, every strictly consistent loss function for mean estimation gives the identical solution; see Barlow et al. [14, Theorem 1.10].

- The PAV algorithm due to Ayer et al. [8], Miles [158] and Kruskal [128] is used to solve the constraint optimization problem (4.9). Essentially, the PAV algorithm is based on merging neighboring classes by applying (4.8) if the isotonic assumption is violated by the corresponding sample means of adjacent bins (indices); for details see Wüthrich-Ziegel [244, Appendix]. Thus, the PAV algorithm is constructing the isotonic estimate $\widehat{\boldsymbol{\mu}}^{\text {iso }}$ by optimally binning the instances, optimal w.r.t. the square loss objective function and w.r.t. the ranking of the covariates. This precisely replaces any hyper-parameter choice in isotonic regression that would otherwise need to be set, e.g., in local regression.
- The isotonic regression only gives regression values in the discrete covariate values $\widehat{\mu}^{\text {iso }}\left(X_{i}\right):=\widehat{\mu}_{i}^{\text {iso }}, 1 \leq i \leq n$, and typically a step-function interpolation is used.

A major argument for the isotonic regression is that it provides an empirically autocalibrated regression solution. That is, through (optimally) binning and empirical mean computations, we obtain

$$
\widehat{\mu}^{\mathrm{iso}}\left(X_{i}\right)=\widehat{\mu}_{i}^{\mathrm{iso}}=\frac{\sum_{j=1}^{n} v_{j} Y_{j} \mathbb{1}_{\left\{\widehat{\mu}_{j}^{\text {iso }}=\widehat{\mu}_{i}^{\text {iso }}\right\}}}{\sum_{j=1}^{n} v_{j} \mathbb{1}_{\left\{\widehat{\mu}_{j}^{\text {iso }}=\widehat{\mu}_{i}^{\text {iso }}\right\}}}=\widehat{\mathbb{E}}\left[Y_{i} \mid \widehat{\mu}^{\mathrm{iso}}\left(X_{i}\right)\right]
$$

the latter denoting the empirical mean of the instances having regression estimate $\widehat{\mu}^{\text {iso }}\left(X_{i}\right)$. Empirical auto-calibration (4.10) expresses that we perform binning in the PAV algorithm, and the bin labels are precisely the empirical means of the bins; see also target encoding (2.16). This verifies empirical auto-calibration.
We revisit the auto-calibration analysis of Figures 4.2 and 4.3, but instead of using decile binning or a local regression, we perform an isotonic re-calibration (regression). For this we fit a first regression function $\boldsymbol{X} \mapsto \widehat{\mu}(\boldsymbol{X})$ to the learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$. As discussed in Section 4.1.3, this first regression function $\widehat{\mu}$ does not necessarily fulfill the auto-calibration property (4.6). The idea of isotonic re-calibration is to apply the re-calibration step (4.7), under the assumption that the first fitted regression function $\widehat{\mu}$ provides the right risk ranking for the true regression function $\mu^{*}$, that is,

$$
\widehat{\mu}\left(\boldsymbol{X}_{t}\right) \leq \widehat{\mu}\left(\boldsymbol{X}_{t^{\prime}}\right) \quad \Longleftrightarrow \quad \mu^{*}\left(\boldsymbol{X}_{t}\right) \leq \mu^{*}\left(\boldsymbol{X}_{t^{\prime}}\right)
$$

Version March 3, 2025, @AI Tools for Actuaries

## Page 72
for all $1 \leq t, t^{\prime} \leq m$. Under this assumption it is sensible to apply an isotonic regression to the sample $\left(Y_{t}, \widehat{\mu}\left(\boldsymbol{X}_{t}\right), v_{t}\right)_{t=1}^{m}$ with new real-valued covariates $X_{t}:=\widehat{\mu}\left(\boldsymbol{X}_{t}\right)$ used as rankings to perform the re-calibration step (4.7). Isotonic regression (4.9) provides us with the isotonically re-calibrated estimates

$$
\widehat{\mu}\left(\boldsymbol{X}_{t}\right) \mapsto \widehat{\mu}_{\mathrm{rc}}\left(\boldsymbol{X}_{t}\right):=\widehat{\mu}_{t}^{\mathrm{iso}}
$$

These new isotonically re-calibrated estimates $\left(\widehat{\mu}_{\mathrm{rc}}\left(\boldsymbol{X}_{t}\right)\right)_{t=1}^{m}$ have the same ranking as the initial estimates $\left(\widehat{\mu}\left(\boldsymbol{X}_{t}\right)\right)_{t=1}^{m}$, modulo ties, but these new isotonically re-calibrated estimates $\left(\widehat{\mu}_{\mathrm{rc}}\left(\boldsymbol{X}_{t}\right)\right)_{t=1}^{m}$ fulfill (empirical) auto-calibration, see (4.10), and this re-calibrated model also fulfills the balance property (4.4). These are pretty strong results!

Figure 4.4: Lift plot with isotonic re-calibration; this continues from Figures 4.2-4.3.
We come back to the lift plots of Figures 4.2-4.3, but we use an isotonic re-calibration step this time to receive the blue dots in Figure 4.4. The crucial differences to previous two plots are: (1) the isotonically re-calibrated lift plot is rank preserving giving a monotone regression in Figure 4.4; (2) the binning is optimal w.r.t. any strictly consistent loss function for mean estimation and subject to the initial ranking; (3) the solution $\widehat{\boldsymbol{\mu}}^{\text {iso }}$ is auto-calibrated and the balance property holds, (4) the Gini score, introduced in Section 4.3.1, below, gives a valid model selection criterion because of auto-calibration.

We conclude with the following result; which is mentioned in Wüthrich-Ziegel [244].
Corollary 4.5. Assume the estimated regression function $\widehat{\mu}: \mathcal{X} \rightarrow \mathbb{R}$ gets the ranking correct, i.e., $\widehat{\mu}(\boldsymbol{X})$ and $\mu^{*}(\boldsymbol{X})$ are strictly comonotonic. The true regression function $\mu^{*}$ is found by the re-calibration step

$$
\mu^{*}(\boldsymbol{X})=\mathbb{E}[Y \mid \widehat{\mu}(\boldsymbol{X})], \quad \text { a.s. }
$$

If an auto-calibrated predictor is needed, isotonic regression is suggested. An advantage clearly is that the order of the prices is not changed, and the levels are only locally perturbed. The three disadvantages we see are that the final regression model is a twostep procedure with the second model dropping out of the initial model class $\mathcal{M}$, i.e., this
![Page 72 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p72_img1.jpg)

## Page 73
is a non-parametric solution that is no longer, e.g., a GLM, even if the first regression model is a GLM. As a consequence, it is no longer as easily explainable as a GLM, and it is also more difficult to manually change the model. The second disadvantage is that the resulting regression function has discontinuities, which is not very appreciated in insurance pricing. The latter disadvantage can be removed by replacing the step function by linearly interpolating functions between the observations. The third problem is that the isotonic re-calibration step needs special attention at the lower and upper boundaries of the support, as it tends to over-fit in this part of the covariate space, which may require to manually merge the largest and the smallest bins, respectively. Coming back to Figure 4.4, the lowest three bins have been merged to ensure that all predicted values are strictly positive, and Figure 4.4 suggests to also merge the two or three highest bins because the largest prediction seems an outlier, over-fitting to a single observation.

# 4.3 Model analysis tools 

We close this interlude by discussing two model validation tools that are used in machine learning and statistics. These two tools require some care because they need auto-calibrated regression functions and/or isotonic regression. We highlight this in the following discussion.

### 4.3.1 Gini score

The Gini score is often used in practice for model validation and model selection. The Gini score goes back to an economic concept introduced 1912 by Gini [74, 75], called the Gini index. The Gini index is based on the Lorenz [144] curve. It is a measure for the disparity of the wealth distribution across a given population; see Lorentzen et al. [143] for a broader discussion. This concept of disparity quantification has been adapted to a machine learning context for model validation and model selection, typically, meaning that a higher Gini score gives better a discrimination of the regression function $\mu(\boldsymbol{X})$ for the claims prediction of $Y$.
Assume we have an observed sample $\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}=1\right)_{i=1}^{n}$ and, we let its indices be ordered such that $\mu\left(\boldsymbol{X}_{1}\right)<\mu\left(\boldsymbol{X}_{2}\right)<\ldots<\mu\left(\boldsymbol{X}_{n}\right)$ for the given regression function $\mu: \mathcal{X} \rightarrow \mathbb{R}$. This requires that we may need to relabel the instances $1 \leq i \leq n$, and for simplicity we assume that there are no ties in this ordering. The empirical version of the (mirrored) Lorenz [144] curve is defined by ${ }^{1}$

$$
\alpha \in(0,1) \quad \mapsto \quad \tilde{L}_{\mu}(\alpha)=\frac{1}{\frac{1}{n} \sum_{i=1}^{n} \mu\left(\boldsymbol{X}_{i}\right)} \frac{1}{n} \sum_{i=[(1-\alpha) n]+1}^{n} \mu\left(\boldsymbol{X}_{i}\right)
$$

[^0]
[^0]:    ${ }^{1}$ We call the curve in (4.11) an empirical Lorenz curve, because we take the sample average over the covariates $\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$, and the non-empirical version would consider the population distribution for $\boldsymbol{X} \sim \mathbb{P}$, instead. There is a second ingredient which is the regression function $\mu$. On purpose, we did not put hats on $\mu$ because the Gini score (4.13) should be evaluated out-of-sample (this applies to the subsequent cumulative accuracy profile (4.12)). That is, if the regression function $\widehat{\mu}$ is estimated from a learning sample $\mathcal{L}$, then the cumulative accuracy profile $\widehat{C}_{\widehat{\mu}}(\alpha)$ should be computed on an independent test sample $\mathcal{T}$, and there should be two hats in the notation $\widehat{C}_{\hat{\mu}}$. In this section, we use a generic regression function $\mu$ to explain the theory.

## Page 74
This empirical mirrored Lorenz curve measures the contribution of the largest regression values $\left(\mu\left(\boldsymbol{X}_{i}\right)\right)_{i=\lceil(1-\alpha) n\rceil+1}^{n}$ to the portfolio average. ${ }^{2}$ It is precisely this property that allows Gini $[74,75]$ to describe discrimination or disparity in wealth distribution by computing the resulting area under the curve (AUC). The bigger this area, the more disperse are the regression values $\left(\mu\left(\boldsymbol{X}_{i}\right)\right)_{i=1}^{n} .{ }^{3}$
For statistical modeling, we replace the empirical Lorenz curve (4.11) by the cumulative accuracy profile (CAP); see Ferrario-Hämmerli [67, Section 6.3.7] and Tasche [213]; Denuit-Trufin [54] call the same construction concentration curve. The (empirical) cumulative accuracy profile of regression function $\mu(\cdot)$ is given by

$$
\alpha \in(0,1) \quad \mapsto \quad \widehat{C}_{\mu}(\alpha)=\frac{1}{\frac{1}{n} \sum_{i=1}^{n} Y_{i}} \frac{1}{n} \sum_{i=\lceil(1-\alpha) n\rceil+1}^{n} Y_{i}
$$

compared to (4.11), we replace the predictions $\mu\left(\boldsymbol{X}_{i}\right)$ by the observations $Y_{i}$, but, importantly, we keep the order of the regression values $\mu\left(\boldsymbol{X}_{1}\right)<\mu\left(\boldsymbol{X}_{2}\right)<\ldots<\mu\left(\boldsymbol{X}_{n}\right)$ in the indices $1 \leq i \leq n$. Similarly to the empirical Lorenz curve, a better discrimination results in a bigger AUC, and the maximal AUC is obtained if the claim sizes $\left(Y_{i}\right)_{i=1}^{n}$ provide the same ordering as the regression values $\left(\mu\left(\boldsymbol{X}_{i}\right)\right)_{i=1}^{n}$. This is precisely the motivation to use this concept for model selection. We illustrate this in Figure 4.5.

Figure 4.5: Cumulative accuracy profile (CAP) given by $\alpha \mapsto \widehat{C}_{\mu}(\alpha)$ used to define the Gini score (4.13); this plot is taken from [241].

The orange dotted line in Figure 4.5 shows the cumulative accuracy profile of perfectly aligned responses $\left(Y_{i}\right)_{i=1}^{n}$ and regression values, and the red line the cumulative accuracy

[^0]
[^0]:    ${ }^{2}$ These considerations are also a well-known method in extreme value theory and risk management. E.g., one speaks about the 20-80 Pareto rule, which means that the $20 \%$ largest claims make up $80 \%$ of the total claim amount; see Embrechts et al. [63, Section 8.2.3].
    ${ }^{3}$ Remark that in an economic context the Lorenz curve is usually below the $45^{\circ}$ line because the summation in the upper tail in (4.11) is switched to the lower tail, compare Figure 4.5 and Goldburd et al. [81, Figure 25]. In machine learning, one typically considers the curve mirrored at the diagonal, giving a sign switch in all inequalities.
![Page 74 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p74_img1.jpg)

## Page 75
profile w.r.t. the selected regression function $\left(\mu\left(\boldsymbol{X}_{i}\right)\right)_{i=1}^{n}$. The dotted blue line corresponds to the null model $\widehat{\mu}_{0}=\frac{1}{n} \sum_{i=1}^{n} Y_{i}$ not considering any covariates, but the global empirical mean $\widehat{\mu}_{0}$ instead. The Gini score is defined by, see Figure 4.5,

$$
\operatorname{Gini}(\mu)=\frac{\operatorname{area}(\mathrm{A})}{\operatorname{area}(\mathrm{A}+\mathrm{B})} \leq 1
$$

where the areas under the curves, area $(\mathrm{A})$ and $\operatorname{area}(\mathrm{A}+\mathrm{B})$, have precisely the meaning as in Figure 4.5. Generally, a bigger Gini score is interpreted as a better discrimination of the selected regression model $\mu(\cdot)$ for the responses $Y$. We remark that this Gini score (defined by the AUC) is equivalent to the so-called receiver operating curve (ROC) method for binary responses $Y$; see Tasche [213, formula (5.6a)].
There is one critical issue with this model selection technique. Namely, the Gini score is not a strictly consistent model selection tool. The Gini score is fully rank based, but it does not consider whether the model lives on the right scale; this is precisely the point raised in Wüthrich [239]. However, if we can additionally ascertain that the regression functions $\mu(\cdot)$ under consideration are auto-calibrated for $(Y, \boldsymbol{X})$, the Gini score is a sensible model selection tool; see Wüthrich [239, Theorem 4.3]. Basically, autocalibration lifts the models to the right level (the level of the responses), and the Gini score then verifies whether the ordering of the policies w.r.t. their responses is optimal.

# 4.3.2 Murphy's score decomposition 

We may want to analyze how well a given regression model $\mu$ discriminates the responses $Y$ w.r.t. the covariates $\boldsymbol{X}$. One possible method is Murphy's [161] score decomposition. For related literature we refer to Pohle [177], Gneiting-Resin [80], Fissler et al. [69] and Semenovich-Dolman [206].
Select a strictly consistent loss function $L$ for mean estimation that is lower-bounded by zero, and such that all the following terms exist. Murphy's score decomposition is given by

$$
\mathbb{E}[L(Y, \mu(\boldsymbol{X}))]=\operatorname{UNC}_{L}-\operatorname{DSC}_{L}+\operatorname{MSC}_{L}
$$

with uncertainty, discrimination (resolution) and miscalibration, respectively,

$$
\begin{aligned}
& \mathrm{UNC}_{L}=\mathbb{E}\left[L\left(Y, \mu_{0}\right)\right] \geq 0 \\
& \mathrm{DSC}_{L}=\mathbb{E}\left[L\left(Y, \mu_{0}\right)\right]-\mathbb{E}\left[L\left(Y, \mu_{\mathrm{rc}}(\boldsymbol{X})\right)\right] \geq 0 \\
& \mathrm{MSC}_{L}=\mathbb{E}[L(Y, \mu(\boldsymbol{X}))]-\mathbb{E}\left[L\left(Y, \mu_{\mathrm{rc}}(\boldsymbol{X})\right)\right] \geq 0
\end{aligned}
$$

The uncertainty term $\mathrm{UNC}_{L}$ quantifies the total prediction uncertainty not using any covariates in its prediction $\mu_{0}=\mathbb{E}[Y]$, this is the global mean. The discrimination (resolution) term $\mathrm{DSC}_{L}$ quantifies the reduction in prediction uncertainty if we use the auto-calibrated regression function $\mu_{\mathrm{rc}}(\boldsymbol{X})$ based on covariate information $\boldsymbol{X}$, see (4.7). Finally, the miscalibration term $\mathrm{MSC}_{L}$ vanishes if the regression function $\mu(\boldsymbol{X})$ is autocalibrated, otherwise it quantifies the auto-calibration misspecification.
In applications, we need to compute these quantities empirically, out-of-sample, similarly to the previous sections. The auto-calibrated model $\mu_{\mathrm{rc}}$ can be determined with an isotonic re-calibration step (4.9).

## Page 76
There are other decompositions which, e.g., compare a regression model $\mu$ to the true one $\mu^{*}$ w.r.t. the available covariate information; see Fissler et al. [69, formula (17)],

$$
\mathbb{E}[L(Y, \mu(\boldsymbol{X}))]=\operatorname{UNC}_{L}-\operatorname{DSC}_{L}^{*}+\operatorname{MSC}_{L}^{*}
$$

with maximal discrimination (resolution) and conditional miscalibration, respectively,

$$
\begin{aligned}
\operatorname{DSC}_{L}^{*} & =\mathbb{E}\left[L\left(Y, \mu_{0}\right)\right]-\mathbb{E}\left[L\left(Y, \mu^{*}(\boldsymbol{X})\right)\right] \geq 0 \\
\operatorname{MSC}_{L}^{*} & =\mathbb{E}[L(Y, \mu(\boldsymbol{X}))]-\mathbb{E}\left[L\left(Y, \mu^{*}(\boldsymbol{X})\right)\right] \geq 0
\end{aligned}
$$

Because the true regression model $\mu^{*}$ is unknown, this decomposition is of less practical value. These considerations are not restricted to the true regression model $\mu^{*}$, but one can also compare two regression functions $\mu_{1}$ and $\mu_{2}$. Positivity of the conditional miscalibration is then related to convex orders of regression functions. In particular, if we choose the square loss function for $L$, such a convex order can easily be obtained by martingale arguments on filtrations (which reflect increasing sets of information, i.e., if we increase the information set $\sigma(\boldsymbol{X})$ by including more covariate information $\sigma\left(\boldsymbol{X}^{+}\right) \supset$ $\sigma(\boldsymbol{X})$, we receive a higher resolution in the resulting true regression function based on $\boldsymbol{X}^{+}$); see Wüthrich-Buser [241, Section 2.5]. ${ }^{4}$

[^0]
[^0]:    ${ }^{4}$ Basically, this reflects a martingale construction from an integrable random variable and a filtration.

## Page 77
# Chapter 5 

## Feed-forward neural networks

In this chapter, we introduce feed-forward neural networks (FNNs) for tabular data, and in this introduction we put special emphasis on FNN architectures that are particularly suitable for solving actuarial problems. Chapters 1 to 3 have introduced the statistical foundation for now being able to consider FNNs.

FNNs are also called artificial neural networks (ANNs), multi-layer perceptrons (MLPs), if they have multiple layers, and more generally, deep learning (DL) architectures. In this chapter, we study plain-vanilla (standard) FNNs.

Figure 5.1: Feed-forward neural network architecture.

In a nutshell, networks perform representation learning, meaning that a feature extractor learns a new representation of the covariates, such that this new representation has a
![Page 77 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p77_img1.jpg)

## Page 78
suitable structure to enter a (generalized) linear model, this is illustrated in Figure 5.1 by the blue and green boxes. Having done all the preparatory work in the GLM Chapter 3 , this FNN extension is a natural one:

# Generalized linear models (GLMs) vs. feed-forward neural networks (FNNs) 

Recall the GLM regression structure (3.1)

$$
\boldsymbol{X} \mapsto g(\mu(\boldsymbol{X}))=\langle\vartheta, \boldsymbol{X}\rangle
$$

Inserting a feature extractor $z^{(d: 1)}$ modifies this GLM structure to the FNN equation

$$
\boldsymbol{X} \mapsto g(\mu(\boldsymbol{X}))=\left\langle\vartheta, z^{(d: 1)}(\boldsymbol{X})\right\rangle
$$

This is precisely the (natural) FNN extension going to be discussed in this chapter. It allows for non-linear structures and interactions of the covariate components.

### 5.1 Feed-forward neural network architecture

This section formalizes the FNN equation (5.1) by introducing all the relevant terms. The fitting (learning) procedure of FNNs is discussed in Section 5.3, below. In this chapter we work with tabular data, meaning that the covariates $\boldsymbol{X}$ are $q$-dimensional real-valued vectors that can be stacked into design matrices (tables) $\mathfrak{X}$; see (2.10).

### 5.1.1 Feature extractor and readout

Deep FNNs consist of multiple hidden layers $\boldsymbol{z}^{(m)}$, called FNN layers. A FNN layer

$$
\boldsymbol{z}^{(m)}: \mathbb{R}^{q_{m-1}} \rightarrow \mathbb{R}^{q_{m}}
$$

performs a non-linear transformation of the covariates; this is formalized in (5.5), below. The main ingredients of such a FNN layer $\boldsymbol{z}^{(m)}$ are:
(a) the number $q_{m} \in \mathbb{N}$ of neurons, also called units;
(b) the non-linear activation function $\phi: \mathbb{R} \rightarrow \mathbb{R}$; and
(c) the network weights representing part of the model parameter $\vartheta$.

Items (a) and (b) are hyper-parameters that are selected by the modeler, and the network weights of item (c) are parameters that are learned during network training (model fitting).
Having $d \in \mathbb{N}$ of these FNN layers $\left(\boldsymbol{z}^{(m)}\right)_{m=1}^{d}$, with matching input and output dimensions, we compose them to a feature extractor of depth $d$

$$
\boldsymbol{X} \mapsto \boldsymbol{z}^{(d: 1)}(\boldsymbol{X}):=\left(\boldsymbol{z}^{(d)} \circ \cdots \circ \boldsymbol{z}^{(1)}\right)(\boldsymbol{X}) \in \mathbb{R}^{q_{d}}
$$

where the input dimension of the first FNN layer $\boldsymbol{z}^{(1)}$ is the dimension of the covariates $\boldsymbol{X}$, given by $q_{0}:=q$. This feature extractor is illustrated in the blue box of Figure 5.1

## Page 79
for an architecture of depth $d=2$, with input dimension $q_{0}=q=16$, and units $q_{1}=8$ and $q_{2}=8$ in the two FNN layers.
The final step of the FNN architecture is to use the learned representation $\boldsymbol{z}^{(d: 1)}(\boldsymbol{X})$ as input to a GLM; this is called the readout. This provides us with a FNN architecture of depth $d$

$$
\mu(\boldsymbol{X})=\mathbb{E}[Y \mid \boldsymbol{X}]=g^{-1}\left\langle\boldsymbol{w}^{(d+1)}, \boldsymbol{z}^{(d: 1)}(\boldsymbol{X})\right\rangle
$$

where $\boldsymbol{w}^{(d+1)} \in \mathbb{R}^{q_{d}+1}$ is the output/readout parameter, including a bias term $w_{0}^{(d+1)}$, and $g^{-1}$ is the inverse of the chosen link function. Compared to the GLM in (3.2), the (only) difference is that we replace the original covariates $\boldsymbol{X} \in \mathbb{R}^{q+1}$ by the newly learned representation $\boldsymbol{z}^{(d: 1)}(\boldsymbol{X}) \in \mathbb{R}^{q_{d}+1}$ from the feature extractor (5.3). For notational convenience, we change the notation of the readout parameter in (5.1) to $\boldsymbol{w}^{(d+1)}$, compare to $(5.4)$.

In the next sections, we discuss the construction of the FNN layers $\boldsymbol{z}^{(m)}$ in careful detail.

# 5.1.2 Activation function 

Because feature extractors $\boldsymbol{z}^{(d: 1)}$ should be able to learn non-linear feature transformations of the original covariates, we need to select non-linear activation functions $\phi: \mathbb{R} \rightarrow \mathbb{R}$. Table 5.1 gives popular choices.

|  | activation function $\phi$ | derivative $\phi^{\prime}$ |
| :-- | :-- | :-- |
| sigmoid (logistic) | $\phi(x)=\sigma(x)=\left(1+e^{-x}\right)^{-1}$ | $\phi(1-\phi)$ |
| hyperbolic tangent | $\phi(x)=\tanh (x)=2 \sigma(2 x)-1$ | $1-\phi^{2}$ |
| rectified linear unit (ReLU) | $\phi(x)=x \mathbb{1}_{\{x \geq 0\}}$ | $\mathbb{1}_{\{x>0\}}, x \neq 0$ |
| sigmoid linear unit (SiLU) | $\phi(x)=x \sigma(x)$ | $\sigma(x)(1-\phi(x))+\phi(x)$ |
| Gaussian error linear unit (GELU) | $\phi(x)=x \Phi(x)$ | $\Phi(x)+x \Phi^{\prime}(x)$ |

Table 5.1: Popular choices of non-linear activation functions $\phi$ and their derivatives $\phi^{\prime}$; $\Phi$ denotes the standard Gaussian distribution, and $\Phi^{\prime}(x)=e^{-x^{2} / 2} / \sqrt{2 \pi}$ its density.

The activation functions and their derivatives in Table 5.1 are illustrated in Figure 5.2. They have different properties, e.g., the first two activation functions are bounded which can be an advantage or a disadvantage, depending on the problem to be solved (do we want bounded or unbounded functions?). The hyperbolic tangent is symmetric in zero which can be an advantage over the sigmoid in deep neural network fitting (because it is naturally calibrated to zero and does not require to adjust biases). The ReLU is an activation function that is very popular in the machine learning community, it leads to sparsity in networks, and it is not differentiable in zero but it has a sub-gradient because it is a convex function. The SiLU is a smooth version of the ReLU, but it is neither monotone nor convex, see Figure 5.2. The GELU has recently gained popularity in transformer architectures, and it has some similarity with the SiLU, see Figure 5.2. Generally, it is difficult to give a good advise for a specific selection of the 'best' activation function, and this should rather be part of the hyper-parameter tuning for the specific actuarial problem to be solved.

## Page 80
Figure 5.2: Activation functions and their derivatives of Table 5.1.

# 5.1.3 Feed-forward neural network layer 

In this section, we formalize the FNN layer $\boldsymbol{z}^{(m)}: \mathbb{R}^{q_{m-1}} \rightarrow \mathbb{R}^{q_{m}}$ introduced in (5.2). This step is a bit technical, but basically it relates to defining all the connections between the neurons (units) illustrated by the lines between the circles in Figure 5.1.
Selected an activation function $\phi$. The FNN layer $\boldsymbol{z}^{(m)}$ is for $\boldsymbol{x} \in \mathbb{R}^{q_{m-1}}$ defined by

$$
\boldsymbol{z}^{(m)}(\boldsymbol{x})=\left(z_{1}^{(m)}(\boldsymbol{x}), \ldots, z_{q_{m}}^{(m)}(\boldsymbol{x})\right)^{\top}
$$

with neurons (units), for $1 \leq j \leq q_{m}$ given by

$$
z_{j}^{(m)}(\boldsymbol{x})=\phi\left(w_{j, 0}^{(m)}+\sum_{l=1}^{q_{m-1}} w_{j, l}^{(m)} x_{l}\right)=: \phi\left\langle\boldsymbol{w}_{j}^{(m)}, \boldsymbol{x}\right\rangle
$$

with network weights $\boldsymbol{w}_{j}^{(m)}=\left(w_{j, 0}^{(m)}, \ldots, w_{j, q_{m-1}}^{(m)}\right)^{\top} \in \mathbb{R}^{q_{m-1}+1}$, including the bias $w_{j, 0}^{(m)}$.

We interpret this as follows. Every neuron $z_{j}^{(m)}(\cdot)$ is corresponds to a circle in Figure 5.1. Each of these neurons performs a GLM operation with inverse link $\phi$, see (5.6). That is, every neuron performs a data compression (projection) from $\boldsymbol{x} \in \mathbb{R}^{q_{m-1}}$ to the real line $z_{j}^{(m)}(\boldsymbol{x}) \in \mathbb{R}, 1 \leq j \leq q_{m}$. This inevitably results in a loss of information. To compensate for this loss of information, every of the $q_{m}$ neurons $z_{j}^{(m)}(\cdot)$ performs a different compression, reflected by different network weights $\boldsymbol{w}_{j}^{(m)}$, so that (hopefully) the relevant information for prediction is extracted by the feature extractor $\boldsymbol{z}^{(d: 1)}$.

As mentioned above, the selections of the activation function $\phi$ and of the number of neurons $q_{m}$ are hyper-parameters selected by the modeler, whereas the (optimal) network weights $\boldsymbol{w}_{j}^{(m)}$ are learned during network training, see Section 5.3, below.
![Page 80 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p80_img1.jpg)

## Page 81
# 5.1.4 Feed-forward neural network architecture 

We can now paste everything together by composing the FNN layers (assuming matching input and output dimensions) to the feature extractor (5.3), and then apply the readout to this feature extracted covariate information. From (5.5)-(5.6), it follows that each FNN layer $\boldsymbol{z}^{(m)}$ has network weights $\left(\boldsymbol{w}_{1}^{(m)}, \ldots, \boldsymbol{w}_{q_{m}}^{(m)}\right)$ of dimension $q_{m}\left(q_{m-1}+1\right)$. Collecting all network weights of all layers, including the output parameter of (5.4), gives network weights (for the notation, see also footnote on page 16)

$$
\vartheta=\left(\boldsymbol{w}_{1}^{(1)}, \ldots, \boldsymbol{w}_{q_{d}}^{(d)}, \boldsymbol{w}^{(d+1)}\right) \in \mathbb{R}^{r}
$$

of total dimension

$$
r=\sum_{m=1}^{d} q_{m}\left(q_{m-1}+1\right)+\left(q_{d}+1\right)
$$

Indicating the network parameter in the notation motivates us to replace (5.4) by the slightly adapted notation

$$
\mu_{\vartheta}(\boldsymbol{X})=\mathbb{E}[Y \mid \boldsymbol{X}]=g^{-1}\left\langle\boldsymbol{w}^{(d+1)}, \boldsymbol{z}^{(d: 1)}(\boldsymbol{X})\right\rangle
$$

In this sense, a FNN architecture provides a class of parametric regression functions $\mathcal{M}=\left\{\mu_{\vartheta}\right\}_{\vartheta}$, being parametrized through the network weights $\vartheta \in \mathbb{R}^{r}$ given in (5.7). For network regression fitting we can (essentially) apply the same deviance loss minimization principle as stated in (3.8), we also refer to the box on page 54, or regularized versions thereof as presented in Section 2.4. We will come back to this below because it turns out that FNN fitting is more difficult than expected.

Example 5.1. We discuss the FNN example of depth $d=2$ given in Figure 5.1. It has a 16 -dimensional covariate vector $\boldsymbol{X}$ providing an input dimension of $q_{0}=q=16$. The first hidden layer $\boldsymbol{z}^{(1)}: \mathbb{R}^{q_{0}} \rightarrow \mathbb{R}^{q_{1}}$ has $q_{1}=8$ neurons providing $8 \cdot 17=136$ network weights. The second hidden layer $\boldsymbol{z}^{(1)}: \mathbb{R}^{q_{1}} \rightarrow \mathbb{R}^{q_{2}}$ has $q_{2}=8$ neurons providing $8 \cdot 9=72$ network weights. Finally, the output parameter has dimension 9, thus, altogether the FNN architecture of Figure 5.1 has network weights $\vartheta$ of dimension $r=217$. These network weights $\vartheta$ needs to be fitted from the learning sample $\mathcal{L}$.
The hyper-parameters selected by the modeler are the depth $d=2$, the number of hidden neurons $q_{1}=8$ and $q_{2}=8$, as well as the activation function $\phi$ and the inverse link $g^{-1}$. For model fitting, the modeler needs to additionally select the (strictly consistent) loss function $L$ for mean estimation, as well as the optimization algorithm to solve the optimization problem. This optimization algorithm will have a significant impact on the selected network, i.e., this is different from GLMs where the solution is fully determined by the model architecture and the loss function. This might be surprising in the first place, and we are going to discuss this in detail below.

## Page 82
There is the recurrent discussion about an optimal FNN architecture. Generally, this question is difficult to answer, and we are going to give more explicit instructions in Section 5.3.8, below. The choice of a good network architecture does not only depend on the predictive problem to be solved, but also on the selected model fitting algorithm. Therefore, we first discuss model fitting.

We close this section with some remarks before discussing the practical issues related to network fitting.

Remarks 5.2. - The above FNN architecture is also called a fully-connected FNN because every neuron $z_{k}^{(m-1)}$ is connected to a neuron $z_{j}^{(m)}$ by the network weight $w_{j, k}^{(m)}$.

- Sometimes, one makes a distinction between shallow FNNs of depth $d=1$ and deep FNNs with $d \geq 2$. In practical applications, one should always work with deep FNNs, because composing layers facilitates interaction modeling. For nonlife actuarial pricing problems often a value $d \in\{3, \ldots, 6\}$ is a suitable choice; we generally use $d=3$ for our French MTPL claims frequency example because this has proved to be suitable for this kind of (small) problem with 9 covariate components.
- The FNN defined in (5.9) has a one-dimensional output. We can also have a multioutput network for multi-task learning, e.g., if we want to predict claims frequency and claims severity (simultaneously), we may select a two-dimensional output

$$
\boldsymbol{X} \mapsto\left(g_{1}^{-1}\left\langle\boldsymbol{w}_{1}^{(d+1)}, \boldsymbol{z}^{(d: 1)}(\boldsymbol{X})\right\rangle, g_{2}^{-1}\left\langle\boldsymbol{w}_{2}^{(d+1)}, \boldsymbol{z}^{(d: 1)}(\boldsymbol{X})\right\rangle\right)^{\top}
$$

In this case, the feature extractor $\boldsymbol{z}^{(d: 1)}(\boldsymbol{X})$ should learn the relevant information for both claims frequency and claims severity prediction.

- We call FNNs parametric models because once the architecture is fixed, the size of the network parameter $\vartheta$ is determined. This is different from non-parametric models where the dimension of the parameter is not given a priori. For instance, in regression trees, discussed below, every iteration of the fitting algorithm will add a new parameter to the model. Sometimes, people call FNNs semi-parametric models. One reason for this is that the dimension of the network parameter $\vartheta$ does not determine the complexity of the FNN regression function. FNN regression functions are not parsimonious, i.e., they usually have much redundancy, and there is research on exploring the 'effective dimension' of FNNs; we refer, e.g., to Abbas et al. $[1]$.


# 5.2 Universality theorems 

The universality theorems are at the core of the great success of FNNs. The main universality theorem statement says that any compactly supported continuous (regression)

## Page 83
function can be approximated arbitrarily well by a suitable (and sufficiently large) FNN. This approximation can be w.r.t. different norms and the assumptions for such a statement to hold are comparably weak, e.g., the sigmoid activation function leads to a class of FNNs that are universal in the above sense. For precise mathematical statements and proofs about these denseness results we refer to Cybenko [47], Hornik et al. [103], Hornik [102], Leshno et al. [134] and Isenbeck-Rüschendorf [108]; and there is a vast literature with similar statements and proofs.
These universality statements imply that basically any (continuous and compactly support) regression function can be approximated arbitrarily well within the class of FNNs.

This sounds very promising:

- First, it means that the class of FNNs is very rich and flexible.
- Second, no matter what the specific true data generating model looks like, there is a FNN that is similar to this data generating mechanism, and our aim is to find it using the learning sample $\mathcal{L}$ that has generated that data.

Unfortunately, there is a backside of the coin of these exciting properties:

- There is no hope to find a (best) parsimonious FNN (on finite samples). In other words, within the class of FNN there are infinitely many (almost equally) good candidate models. Based on a finite sample there is no best selection, we can only distinguish clearly better from clearly worse models. This can almost be stated as a paradigm in FNN predictive modeling.
- The model selection/fitting problem is very high-dimensional and non-convex (for any reasonable choice of an objective function), and usually, at best, the found 'solutions' are (close to) local optimums.
- Model selection within the class of FNN has several elements of randomness, e.g., a fitting algorithm needs to be (randomly) initialized and this impacts the selected solution. To be able to replicate results, the fitting procedure has to be designed very carefully and seeds of random number generators need to be stored to be able to track and replicate the specific solutions.

Some of the previous items will only become clear once we have introduced stochastic gradient descent fitting, and the reader should keep these (critical) items in mind for the discussions below.

# 5.3 Network fitting with gradient descent 

Based on the fact that we cannot find a 'best' FNN approximation to the true model on finite samples (see discussion above), we try to find a 'reasonably good' FNN approximation to the true data generating mechanism. Reasonably good means that it usually outperforms a classical GLM, but at the same time there are infinitely many other FNNs that have a similarly good predictive performance (generalization to new data).

## Page 84
Due to the non-convexity and the complexity of the problem, computational aspects are crucial in designing a good FNN learning algorithm. The main tool is stochastic gradient descent (SGD) which stepwise adaptively improves the network weights $\vartheta$ w.r.t. a given objective function. We are going to derive the SGD algorithm step-by-step, and it will follow in Section 5.3.7, below. On the way to get there, we need to discuss several items and issues, which is done in the next sections. The next section starts by introducing the standard gradient descent method.

# 5.3.1 The standard gradient descent method 

Similarly to (3.8), we try to find network weights $\widehat{\vartheta}$ that provide a small empirical loss on the learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$; the empirical loss in network parameter $\vartheta$ on $\mathcal{L}$ is defined by

$$
L(\vartheta ; \mathcal{L}):=\sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)
$$

where $\mu_{\vartheta}$ is the FNN (5.9) with network weights $\vartheta \in \mathbb{R}^{r}$ and $L$ is a strictly consistent loss function for mean estimation. We add the learning sample $\mathcal{L}$ to the loss notation $L(\vartheta ; \mathcal{L})$ because for SGD training we are going to vary over different learning samples.
The standard gradient descent method works as follows. Assume that at algorithmic time $t \in \mathbb{N}_{0}$, we have network weights $\vartheta^{[t]} \in \mathbb{R}^{r}$ providing the empirical loss $L\left(\vartheta^{[t]} ; \mathcal{L}\right)$. We would like to stepwise adaptively improve these network weights $\vartheta^{[t]} \mapsto \vartheta^{[t+1]}$ such that the empirical loss decreases in each step $t \mapsto t+1$. We try to achieve this by a small perturbation of $\vartheta^{[t]}$ that leads to a local improvement of the network weights. Local (small) changes can be described by a first order Taylor expansion ${ }^{1}$

$$
L\left(\vartheta^{[t+1]} ; \mathcal{L}\right) \approx L\left(\vartheta^{[t]} ; \mathcal{L}\right)+\nabla_{\vartheta} L\left(\vartheta^{[t]} ; \mathcal{L}\right)^{\top}\left(\vartheta^{[t+1]}-\vartheta^{[t]}\right)
$$

for $\vartheta^{[t+1]}$ close to $\vartheta^{[t]}$; and $\nabla_{\vartheta}$ denotes the gradient (derivative) w.r.t. the network weights. The right-hand side of the above approximation (5.11) becomes minimal, if the second term is as negative as possible. Therefore, the update in the network weights should point into the opposite direction of the gradient.
This motivates the standard gradient descent update

$$
\vartheta^{[t]} \mapsto \vartheta^{[t+1]}=\vartheta^{[t]}-\varrho_{t+1} \nabla_{\vartheta} L\left(\vartheta^{[t]} ; \mathcal{L}\right)
$$

where $\varrho_{t+1}>0$ is a (small) learning rate, also called step size.
The learning rate needs to be small because the first order Taylor expansion is only a valid approximation in the neighborhood of $\vartheta^{[t]}$. On the other hand, the learning rate should not be too small, otherwise we need to run too many of these standard gradient descent steps.
An important point is that the initial value $\vartheta^{[0]}$ of the gradient descent algorithm should be selected at random to avoid that the gradient descent algorithm starts in a saddlepoint

[^0]
[^0]:    ${ }^{1}$ We assume differentiability in all gradient descent considerations. This is typically the case in the selected network architectures, except for the ReLU activation function which is not differentiable in the origin.

## Page 85
of the loss surface $\vartheta \mapsto L(\vartheta ; \mathcal{L})$. For instance, if one sets $\vartheta^{[0]}=\mathbf{0}$, there is no predetermined initial direction for the first gradient descent step because the FNN has symmetries around this initial value, i.e., we have a saddlepoint of the loss surface and the algorithm will not start to exploit the parameter space. A popular initializer is the glorot_uniform initializer of Glorot-Bengio [76, formula (16)]. It adjusts the volatility in the random uniform initialization to the sizes of the network layers.

The following points need to be addressed by the modeler for a successful gradient descent fitting:

- Covariate pre-processing; see Section 5.3.2.
- Gradient calculation by back-propagation for an efficient calculation of the gradients $\nabla_{\vartheta} L(\vartheta ; \mathcal{L})$ in (5.12); see Section 5.3.3.
- Learning rate and higher order Taylor approximations to accelerate the algorithm; see Section 5.3.4.
- Early stopping rule for the algorithm; see Section 5.3.5.
- Regularization and drop-out; see Section 5.3.6.
- Stochastic gradient descent to deal with big data, i.e., big learning samples $\mathcal{L}$; see Section 5.3.7.


# 5.3.2 Covariate pre-processing 

An important point in gradient descent methods is covariate pre-processing, also for continuous covariates; see Section 2.3 for covariate pre-processing. It is important for the gradient descent algorithm to work well that all covariate components live on the same scale, otherwise some covariate components will dominate the gradient, and the algorithm may not be able to adapt to the right scales (even for the momentum-based versions discussed below). Therefore, continuous covariates should be standardized (2.18) or the MinMaxScaler (2.19) should be applied. Under skewed covariates, often standardization works better because the MinMaxScaler tends to cluster at the boundary for skewed covariates. If the skewness is too large, i.e., if a given covariate lives on different scales (magnitudes), one should first apply a log-transformation. For example, the population density studied in Listing 3.1 may live on different magnitudes, and one should rather consider the log-population density instead in FNNs.
For categorical covariates usually one-hot encoding is used in the first place. Note that in FNNs a full rank design matrix is not an essential assumption/property. Since identifiability and parsimony is not given in FNNs in general, the discussion between one-hot encoding vs. dummy coding does not matter, and both choices are equally suitable. High-cardinality categorical covariates lead to large input dimensions $q_{0}$ to the feature extractor. This is generally problematic in network fitting as it gives a high potential for over-fitting. As a general recommendation in such situations, we propose to use entity embedding with a low-dimensional embedding dimension $b$, see (2.15). The entity

## Page 86
embedded variables are concatenated with the continuous ones, which then jointly enter the feature extractor of the FNN architecture. This adds $b \cdot K$ embedding weights to the network parameter $\vartheta$, if $K$ is the number of levels of the categorical covariate. These embedding weights are also learned during gradient descent training, i.e., they also enter the gradient computations. In many cases, this gives a superior performance over one-hot encoding and dummy coding, respectively. An example is given in the notebook:
notebook-insert-link
If the categorical covariates are high-cardinality and/or if there is a natural hierarchical structure in the categorical covariates (vehicle brand - vehicle model - vehicle details), one should regularize the entity embedding to receive a successful network training that prevents from over-fitting. We come back to this in later chapters in relation to variational Bayes' methods; and we also refer to Richman-Wüthrich [192].

# 5.3.3 Gradient calculation via back-propagation 

Generally the gradient computation $\nabla_{\vartheta} L(\vartheta ; \mathcal{L})$ is high-dimensional and computationally intensive. The network weights $\vartheta$ enter the readout, see (5.9), and they enter the different layers $\left(\boldsymbol{z}^{(m)}\right)_{m=1}^{d}$ in the feature extractor $\boldsymbol{z}^{(d: 1)}$. Theoretically, the gradient can be worked out using standard calculus, however, through the iterated application of the chain-rule the computations become very tedious.
The workhorse to compute these gradients efficiently, and to avoid tedious formulas, is the back-propagation method of Rumelhart et al. [196]. Mathematically speaking, the backpropagation method is a clever re-parametrization of the problem which allows one to efficiently compute these gradients recursively by matrix multiplications, also benefiting from the fact that the most popular activation functions $\phi$ have simple derivatives, see Table 5.1.
At this stage, we do not believe that it is very useful to give more technical details about the back-propagation method. The main takeaway is that the gradients can be computed efficiently, and that the (ready-to-use) standard FNN fitting software has implemented versions of this back-propagation method. The interested reader is referred to WüthrichMerz [243, Section 7.2.3] for more technical details.

### 5.3.4 Learning rate and higher order Taylor approximations

The first order Taylor expansion (5.11) computes the slopes and, hence, the direction of the optimal local updates. The optimal (directional) learning rates $\varrho_{t+1}>0$ in (5.12) can be determined by the curvature of the loss surface described by the second order derivatives (Hessian) of the empirical loss $L(\vartheta ; \mathcal{L})$. This is what Newton-Raphson teach us to do. Unfortunately, it is computationally infeasible to compute the Hessian in (bigger) FNNs, therefore, we cannot determine the optimal learning rates by second order derivatives. In physics, first order derivatives are related to speed and second order derivatives to acceleration. Since we cannot compute second order derivatives, inspired by physics, we try to mimic how speed and velocity build up by computing a momentum from past velocities. This is a way of mimicking second order derivatives. This motivates

## Page 87
to replace the standard gradient descent update (5.12) by a momentum-based gradient descent update

$$
\begin{aligned}
& \mathbf{v}^{[t]} \mapsto \mathbf{v}^{[t+1]}=\nu \mathbf{v}^{[t]}-\varrho_{t+1} \nabla_{\vartheta} L\left(\vartheta^{[t]} ; \mathcal{L}\right) \\
& \vartheta^{[t]} \mapsto \vartheta^{[t+1]}=\vartheta^{[t]}+\mathbf{v}^{[t+1]}
\end{aligned}
$$

with learning rate $\varrho_{t+1}>0$ and momentum parameter $\nu>0$, and where we initialize $\mathbf{v}^{[0]}=\mathbf{0}$. The learning rate and the momentum parameter are hyper-parameters that need to be fine-tuned by the modeler. This and slightly modified versions thereof are implemented in standard software, and this software often comes with suitable standard values for these hyper-parameters, i.e., they are ready-to-use. Therefore, we do not describe these points in more detail. Standard momentum-based algorithms are rmsprop or adam; see Hinton et al. [98], Kingma-Ba [118] and Goodfellow et al. [83, Sections 8.3 and 8.5].
Another noteworthy improvement is the Nesterov acceleration [165]. Nesterov has noticed that such algorithms often have a zig-zag behavior, meaning that they overshoot and then correct by moving back and forth, which does not seem to be very effective. The improvement suggested by Nesterov is to already anticipate the next gradient descent step in determining the optimal learning rates and momentums. This way an overshooting can be reduced. This is implemented, for example, in the nadam version of adam.
The described gradient descent algorithms are usually used in standard network architectures such as FNNs. If one works with more specific architectures, e.g., with transformers, there are more specialized gradient descent methods. For instance, for transformers, there is an adamW version of Loshchilov-Hutter [145] which better adapts to problems where the variables live on different scales.

# 5.3.5 Early stopping rule 

We come back to the universality statements of Section 5.2. Having a reasonably large FNN architecture, this architecture is very flexible because it is capable to approximate a fairly large function class. This implies that computing the MLE

$$
\widehat{\vartheta}^{\mathrm{MLE}} \in \underset{\vartheta}{\arg \min } L(\vartheta ; \mathcal{L})=\underset{\vartheta}{\arg \min } \sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)
$$

is not a sensible problem that we should try to solve. This MLE fitted FNN will not only extract the structural part (systematic effects) from the learning sample $\mathcal{L}=$ $\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$, but it will also largely adapt to the noisy part (pure randomness) in this learning sample. Obviously, such a FNN will badly generalize and it will have a poor predictive performance on out-of-sample test data $\mathcal{T}$.
Figure 5.3 gives an example that in-sample over-fits. The black dots are the observed responses $Y_{i}$ (in the learning sample $\mathcal{L}$ ), and the true regression function $\mu^{*}$ is shown in green color. The red graph shows a fitted regression model that over-fits to the learning sample $\mathcal{L}$. It follows the black dots quite closely, significantly deviating from the true green regression function. Out-of-sample (repeating this experiment), the black dots may likely also lie on the other side of the green line and, thus, the red estimated model will

## Page 88
Figure 5.3: An example of over-fitting; this figure is taken from [243, Figure 7.6].
generally not perform well in predictions (perform worse than an estimated model that is close to the green line).
Consequently, within a highly flexible model class, we need to try to find a model that only extracts the systematic part from a noisy sample. The key to this problem is early stopping, some scholars call early stopping a regularization method, however, technically it is different because it has an essential temporal component related to algorithmic time.

At this fitting step, FNN regression modeling significantly differs from GLM. In GLMs, there often is little over-fitting potential and one tries to minimize the empirical loss $L(\vartheta ; \mathcal{L})$ to find the optimal GLM parameter. In contrast, reasonably large FNNs have a high over-fitting potential and, therefore, one only tries to get the empirical loss $L(\vartheta ; \mathcal{L})$ reasonably small to find a good network parameter. Practically, this is achieved by exercising an early stopping rule during gradient descent training.

Let us first explain why early stopping works before discussing its implementation. Coming back to the empirical loss (5.10), we compute its gradient

$$
\nabla_{\vartheta} L(\vartheta ; \mathcal{L})=\sum_{i=1}^{n} \frac{v_{i}}{\varphi} \nabla_{\vartheta} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)
$$

We observe that this gradient consists of a sum of many individual gradients of each instance $1 \leq i \leq n$. In each gradient descent step we try to find the most effective/significant update. Systematic effects will impact many individual instances (otherwise these effects would not be systematic). At the beginning of the gradient descent algorithm, before having found these systematic effects, they will therefore dominate the gradient descent steps. Once these systematic effects acting on many instances $1 \leq i \leq n$ have been found, the relative importance of instance-individual factors (noise) starts to in-
![Page 88 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p88_img1.jpg)

## Page 89
crease. This is precisely the time-point to early stop the gradient descent algorithm; we call this early stopping because the algorithm has not yet reached a local minimum of the loss function and, as explained above, this is not our intention.
The previous outline also explains why all components of the covariates should live on a comparable scale. If one covariate component lives on a bigger scale than the other ones, it dominates the gradients. Thus, the gradient descent algorithm will find the systematic effects of that dominant covariate component and then its starts to exploit its noisy part (because this noise is still on a bigger magnitude than the systematic part of the remaining covariates). At this stage, we early stop because learning the noise does not generalize to the new data, and, henceforth, we have not found the systematic part of the other covariate components.

Implementation of early stopping requires a careful treatment of the available learning sample $\mathcal{L}$. For this, we partition the learning data $\mathcal{L}$ at random into a training sample $\mathcal{U}$ and a validation sample $\mathcal{V}$. The training sample $\mathcal{U}$ is used for computing the gradient descent steps, and the validation sample $\mathcal{V}$ is used to track over-fitting by an instantaneous (out-of-sample) validation analysis; this partition is illustrated in Figure 5.4.

Figure 5.4: Partition of the entire data (lhs) into learning sample $\mathcal{L}$ and test sample $\mathcal{T}$ (middle), and into training sample $\mathcal{U}$, validation sample $\mathcal{V}$ and test sample $\mathcal{T}$ (rhs); this figure is taken from [243, Figure 7.7].

Thus, we perform the gradient descent algorithm only on the training sample $\mathcal{U}$

$$
\nabla_{\vartheta} L(\vartheta ; \mathcal{U})=\sum_{i \in \mathcal{U}} \frac{v_{i}}{\varphi} \nabla_{\vartheta} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)
$$

and we perform an instantaneous out-of-sample validation on $\mathcal{V}$ giving us the validation loss $L\left(\vartheta^{[t]} ; \mathcal{V}\right)$ at algorithmic time $t$ for network weights estimate $\vartheta^{[t]}$. Naturally, the training loss $L\left(\vartheta^{[t]} ; \mathcal{U}\right)$ should decrease for $t \rightarrow \infty$. The validation loss $L\left(\vartheta^{[t]} ; \mathcal{V}\right)$ decreases as long as we learn systematic effects, and it starts to increase (deteriorate) once we learn the noise part. This change of behavior gives us the early stopping point $t^{\star}$ (and more generally the early stopping rule), and we estimate the network weights by $\widehat{\vartheta}=\vartheta^{\left[t^{\star}\right]}$. This is illustrated in Figure 5.5 where we stop at $t^{\star}=43$. Of course, the validation sample $\mathcal{V}$ should be sufficiently large to obtain a credible stopping rule (that itself is not
![Page 89 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p89_img1.jpg)

## Page 90
Figure 5.5: An example of early stopping at time $t^{\star}=43$ (orange line).
dominated by the noise in $\mathcal{V}$ ). Often one takes $20 \%$ or $10 \%$ of the learning data $\mathcal{L}$ as validation sample $\mathcal{V}$, depending on the sample size $n$.
Technically, for gradient descent training, one installs a so-called callback. This just means that one saves every weight $\vartheta^{[t]}, t \geq 0$, that decreases the validation loss $L\left(\vartheta^{[t]} ; \mathcal{V}\right)$, and after running the algorithm one 'calls back' the weight $\vartheta^{\left[t^{*}\right]}$ with the minimal validation loss, which then presents the estimated network weights $\widehat{\vartheta}=\vartheta^{\left[t^{*}\right]}$ from the early stopped gradient descent algorithm.

# 5.3.6 Regularization and drop-out 

Of course, there is no difficulty in using a regularized loss version in the gradient descent algorithm, see Section 2.4 for regularization. However, an attempt to use LASSO regularization to receive sparse network weights does not work. The problem is that the sparsity in LASSO regularization stems from the non-differentiability of the $L^{1}$-regularization in the origin, but the gradient descent algorithm (as its name says) cannot deal with this non-differentiability in the origin (in fact, it uses a sub-gradient in the origin). Thus, gradient descent methods can only get the regularized network weights small, but then these small weights need to be set manually to (exactly) zero, of course, this can be achieved by an integrated deterministic rule; see Richman-Wüthrich [191] for an example.
Another popular method to prevent from (in-sample) over-fitting is drop-out by Srivastava et al. [210] and Wager et al. [229]. Drop-out is an additional network layer between two FNN layers that removes neurons $z_{j}^{(m)}$ at random from the network, only during gradient descent training; at random means by an i.i.d. Bernoulli random variable with a given drop-out rate (which is a hyper-parameter selected by the modeler) in each gradient descent step. This random removal during network training prevents individual neurons to specialize to a certain task, because it is always the composite of non-dropped neurons that has to fulfill the forecasting task. This leads to better balanced networks, and
![Page 90 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p90_img1.jpg)

## Page 91
naturally to non-sparsity because every neuron needs to be able to comply with different tasks. We will come back to drop-out in Section 8.5.1 on page 153.

# 5.3.7 Stochastic gradient descent 

The gradient calculation in (5.13) involves large matrix multiplications if the dimension of the network weights $\vartheta$ and the size of the training sample $\mathcal{U}$ are large, which is usually the case. Matrix multiplications of large matrices can be very slow which hinders fast network fitting. For this reason, one typically considers a stochastic gradient descent (SGD) algorithm.

For the SGD method one chooses a fixed batch size $s \in \mathbb{N}$, and one randomly partitions the training sample $\mathcal{U}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$ into (mini-) batches $\mathcal{U}_{1}, \ldots, \mathcal{U}_{\lfloor n / s\rfloor}$ of roughly the same size $s$.

One then considers the SGD updates

$$
\vartheta^{[t]} \mapsto \vartheta^{[t+1]}=\vartheta^{[t]}-\varrho_{t+1} \nabla_{\vartheta} L\left(\vartheta^{[t]} ; \mathcal{U}_{k}\right)
$$

where one cyclically visits the batches $\left(\mathcal{U}_{k}\right)_{k=1}^{\lfloor n / s\rfloor}$ for the gradient descent step $t \rightarrow t+1$.

The batch size $s \in \mathbb{N}$ of the batches $\left(\mathcal{U}_{k}\right)_{k=1}^{\lfloor n / s\rfloor}$ should not be too small. Assuming that the observations $\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{s}$ are i.i.d., the law of large numbers will provide us with the (locally) optimal gradient descent step if we let the batch size $s \rightarrow \infty$. This suggests that we should choose very large batch sizes $s$. As explained above, computational reasons force us to choose small(er) batch sizes, which may provide certain 'erratic' gradient descent updates in view of the optimal next step. However, this is not the full story, and some erratic steps can even be beneficial for finding better network weights, as long as these erratic steps are not too numerous (and not too large). An infinite sample only gives the next optimal step, which is a one-step ahead consideration. This may guide us into a bottleneck, saddlepoint or local minimum that is far from optimal, because the next optimal step is only a local optimal consideration. Having some erratic steps from time to time may help us to escape from trapped situations like a bottleneck by slightly shifting in the parameter space, so that we have the opportunity to explore different environments (generally, such erratic steps are not too big for small step sizes, and usually the loss surface is smooth and not too steep, so that an erratic step does not dramatically change the situation). In this sense, finding a good trade-off between next best steps and erratic steps, leads to the best predictive FNNs.

## Page 92
We summarize SGD training:

- We use SGD training for FNN fitting. For insurance pricing problems, typically, reasonable mini-batch sizes $s$ are in the range of 1000 to 5000 .
- To speed up and improve the SGD fitting procedures, we use momentumbased versions of SGD, e.g., the adam version; often its standard parametrization works well. This can be complemented by the Nesterov acceleration, as implemented in the nadam version of SGD.
- For early stopping, we implement a call back which tracks the validation loss on the validation sample $\mathcal{V}$ during SGD training. The validation sample is typically $10 \%$ to $20 \%$ of the entire learning sample $\mathcal{L}$.
- Finally, SGD training can be improved by regularization and drop-out, this is part of hyper-parameter tuning and it needs to be checked case by case. Typically, more regularization and drop-out is needed with increasing sizes of the FNN architectures.


# 5.3.8 Summarizing feed-forward neural networks and their training 

We are now in the exciting position of being able to apply FNN regression models! But, the first attempts on real data will likely be a disappointment because choosing a good network architecture and a good training algorithm needs some practical experience.

There is the recurrent question of how to select a good network architecture. A general principle is that the selected network architecture should not be too small to be sufficiently flexible to approximate all potentially suitable regression functions. Generally, it is a bad guidance to attempt for a minimal and parsimonious FNN. Usually, there are many different, roughly equally good approximations to the real data generating mechanism, and the SGD algorithm can only find (some of) those if it has sufficiently many degrees of freedom to exploit the environment (this contradicts parsimony), otherwise the fitting will likely not result in the best possible predictive model. Of course, this is a bit against actuarial thinking. Optimizing neural network architectures (e.g., the hyper-parameters like the depth $d$ and the number of neurons $q_{m}$ ) is not a target that one should try to achieve, but one has to accommodate with the fact that the selected architectures should exceed a minimal complexity bound above parsimony for SGD training to be successful. Typically, this results in a lot of redundancy, which cannot be reduced by existing techniques. Specifically, the FNN architecture should have a certain depth $d$ that is not too small (depth promotes interactions), and each hidden layer should also not be chosen too small.

We make an attempt for a clearer instruction about the choice of the FNN architecture: In our examples, which are comparably small insurance pricing examples of roughly 500,000 insurance policies equipped with roughly 10 covariate components, it has turned out that FNN architectures of depth $d \in\{3, \ldots, 6\}$ with approximately 15 to 30 neurons in each hidden layer work well. For the French MTPL claims frequency example used in

## Page 93
these notes, see Section 3.3.2, we designed a standard FNN architecture of depth $d=3$ with $\left(q_{1}, q_{2}, q_{3}\right)=(20,15,10)$ neurons in the three FNN layers. This has proved to work well in this example; see our notebook notebook-insert-link

Another critical point is that network fitting involves several elements of randomness. Even if we fix the architecture and the fitting procedure, we typically end up with multiple equally good predictive models if we run the same fitting algorithm and strategy multiple times (with different seeds).

The elements of randomness involve:
(1) the initialization of the network weights $\vartheta^{[0]}$ for SGD;
(2) the random partition into learning sample $\mathcal{L}$ and test sample $\mathcal{T}$;
(3) the random partition into training sample $\mathcal{U}$ and validation sample $\mathcal{V}$;
(4) the partition into the batches $\left(\mathcal{U}_{k}\right)_{k=1}^{\lfloor n / s\rfloor}$; and
(5) there are further random items like drop-outs, if used during SGD training, etc.

All this makes the early stopped SGD solution (highly) non-unique.

This non-uniqueness is a fact that one has to live with in machine learning models. In Section 5.4 we present an ensemble predictor that reduces this randomness by averaging.

Remark 5.3 (balance correction). The early stopped SGD fitted FNN will not fulfill the balance property (4.4), even if we use the canonical link of the selected deviance loss function for $g$ in the readout (5.4). A reason for this failure is early stopping which stops the algorithm before having found a critical point of the loss surface. The balance property can be rectified by adjusting the estimate of the bias term of the readout $\hat{w}_{0}^{(d+1)}$ correspondingly. If we work with the canonical link for $g$, one can alternatively exercise another GLM step, using the feature extracted covariates $\left(\tilde{\boldsymbol{z}}^{(d+1)}\left(\boldsymbol{X}_{i}\right)\right)_{i=1}^{n}$ as new covariates for this GLM step; $\tilde{\boldsymbol{z}}^{(d+1)}$ denotes the SGD fitted feature extractor. Thus, we fit a GLM on the new learning sample $\left(Y_{i}, \tilde{\boldsymbol{z}}^{(d+1)}\left(\boldsymbol{X}_{i}\right), v_{i}\right)_{i=1}^{n}$ under the canonical link choice, see (5.1). This is the proposal of Wüthrich [238].

# 5.4 Nagging 

In Chapter 6 we will meet a method called bagging which was introduced by Breiman [29]. Bagging combines bootstrap and aggregating. Bootstrap is the re-sampling technique discussed in Section 1.5.4, and this is combined with aggregation which has an averaging effect, reducing the randomness.
In this section we do not bootstrap, but, because network fitting has several items of randomness as discussed in the previous section, we replace the bootstrap samples by

## Page 94
different SGD solutions. An ensembling of network predictors has first been considered by Dietterich $[56,57]$ and subsequently it has been studied in Richman-Wüthrich [189], where the name nagging for network aggregating was introduced.

# 5.4.1 Aggregating 

Aggregating can most easily be explained by considering an i.i.d. sequence of squareintegrable predictors $\left(\widehat{\mu}_{j}\right)_{j \geq 1}$, which are assumed to be unbiased for the true predictor $\mu^{*}$, that is, $\mathbb{E}\left[\widehat{\mu}_{j}\right]=\mu^{*}$, for $j \geq 1$. For a fixed predictor $\widehat{\mu}_{j}$, we have an approximation error, called estimation error (or, more broadly, model error),

$$
\widehat{\mu}_{j}-\mu^{*}
$$

which on average is zero due to the unbiasedness assumption. For unknown true predictor $\mu^{*}$, one estimates this estimation error by the variance (or the standard deviation, respectively) of the predictor, i.e., the average approximation error, called estimation uncertainty, is given by $\mathbb{V}\left(\widehat{\mu}_{j}\right)$ or $\sqrt{\mathbb{V}\left(\widehat{\mu}_{j}\right)}$, respectively, which can be determined empirically from the predictors $\left(\widehat{\mu}_{j}\right)_{j \geq 1}$.
On the other hand, having multiple independent unbiased predictors $\left(\widehat{\mu}_{j}\right)_{j=1}^{M}$, one can build the ensemble predictor

$$
\widehat{\mu}^{(M)}=\frac{1}{M} \sum_{j=1}^{M} \bar{\mu}_{j}
$$

This ensemble predictor has an estimation error $\widehat{\mu}^{(M)}-\mu^{*}$, and the estimation uncertainty is given by

$$
\mathbb{V}\left(\widehat{\mu}^{(M)}\right)=\frac{1}{M} \mathbb{V}\left(\widehat{\mu}_{1}\right) \rightarrow 0 \quad \text { for } M \rightarrow \infty
$$

Of course, all this is well-known in statistics, but the important takeaway is that ensembling over unbiased i.i.d. predictors substantially reduces estimation errors and uncertainty (through the law of large numbers).

There are two caveats:
(1) Where do we get the i.i.d. predictors from?
(2) How can we ensure that they are unbiased?

### 5.4.2 Network ensembling

We come back to the previous two questions. Since we do not know the true model of $(Y, \boldsymbol{X}, v)$, neither of the two questions (1) and (2) can be answered, i.e., we cannot resample and we do not know the right mean level.

We can only manipulate with conditional quantities, given the learning sample $\mathcal{L}=$ $\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$, and then we can still discuss whether the analysis we receive is of any interest. We come back to the elements of randomness that are involved in SGD fitting, see discussion on page 93 in Section 5.3.8. If we select all these random items in an i.i.d. manner (with an i.i.d. random seed), we receive conditional i.i.d. FNN models

## Page 95
$\mu_{\widehat{\vartheta}_{j}}(\boldsymbol{X})$, where $\widehat{\vartheta}_{j}$ denotes the SGD fitted network weights from the $j$-th conditionally independent SGD run, using always the identical fitting strategy, only the initialization and partitioning is done with a different random seed, and the conditional stems from the fact that it is conditional on the learning sample $\mathcal{L}$. Iterating this SGD fitting $M$ times, gives us $M$ conditionally independent FNNs $\left(\mu_{\widehat{\vartheta}_{j}}\right)_{j=1}^{M}$, given $\mathcal{L}$.
A first question is: how robust are the predictions $\mu_{\widehat{\vartheta}_{1}}(\boldsymbol{X}), \ldots, \mu_{\widehat{\vartheta}_{M}}(\boldsymbol{X})$ for a given covariate value $\boldsymbol{X}$ ? This question has been analyzed in Richman-Wüthrich [189] and Wüthrich-Merz [243, Figure 7.18] on a motor insurance claims frequency data set of sample size roughly $n=500,000$. The average fluctuations of the different fits $\left(\mu_{\widehat{\vartheta}_{j}}(\boldsymbol{X})\right)_{j=1}^{M}$ were of magnitude $10 \%$, this concerns the main body of the covariate distribution $\boldsymbol{X} \sim \mathbb{P}$. In this part of the covariate space we got reliable and quite robust models. However, there are less frequent covariate combinations where these fluctuations were up to $40 \%$, i.e., the different initializations of SGD gave fluctuations in the best-estimates of up to $40 \%$. Thus, there is clearly a credibility issue in the estimated FNNs in this (scarce) part of the covariate space. Aggregating helps to reduce these fluctuations.

This motivated the nagging predictor

$$
\widehat{\mu}_{M}^{\operatorname{nagg}}(\boldsymbol{X})=\frac{1}{M} \sum_{j=1}^{M} \mu_{\widehat{\vartheta}_{j}}(\boldsymbol{X})
$$

This ensembling reduces the average fluctuations by a factor $\sqrt{M}$ (on the standard deviation scale). That is, this determines the rate of convergence, and we obtain the law of large numbers, a.s.,

$$
\lim _{M \rightarrow \infty} \widehat{\mu}_{M}^{\operatorname{nagg}}(\boldsymbol{X})=E\left[\left.\mu_{\widehat{\vartheta}_{1}}(\boldsymbol{X})\right| \mathcal{L}, \boldsymbol{X}\right]
$$

where $E[\cdot \mid \mathcal{L}, \boldsymbol{X}]$ is the conditional expectation operator describing the selected SGD fitting procedure, and for a fixed covariate value $\boldsymbol{X}$, this is also the measure the 'a.s.' is referring to. This law of large numbers limit precisely states what kind of (conditional) unbiasedness we can receive by the nagging predictor. A difference of the limit (5.18) compared to the true mean $\mu^{*}(\boldsymbol{X})$ can originate from the following items: the particular learning sample $\mathcal{L}$ that is at our disposal, the FNN architecture that we choose, the specific version of the SGD algorithm with early stopping that we apply, but also the particular distribution we use for initializing the SGD algorithm.

A first conclusion is that the nagging predictor robustifies the best-estimate prediction. A second conclusion is that the nagging predictor significantly improves prediction accuracy, by reducing the estimation error. This is verified in many examples in the literature, see, e.g., Wüthrich-Merz [243, Table 7.9]. Figure 5.6 shows two different examples, the lefthand side gives a claims frequency example and the right-hand side a claims severity example. Both plots show the decrease of out-of-sample loss as a function of the number $M$ of ensembled network predictors $\left(\mu_{\widehat{\vartheta}_{j}}\right)_{j=1}^{M}$. From these examples we conclude that a good value for $M$ is either 10 or 20 , because afterwards the out-of-sample loss of the nagging predictor $\widehat{\mu}_{M}^{\text {nagg }}$ stabilizes.

## Page 96
Figure 5.6: Decrease of the out-of-sample loss of the nagging predictors $\tilde{\mu}_{M}^{\text {nag }}$ as a function of $M \geq 1$ : (lhs) Poisson frequency example, (rhs) gamma severity example; these figures are taken from [243, Figures 7.19 and 7.24].

Recommendation. In network predictions, always consider the nagging predictor $\tilde{\mu}_{M}^{\text {nag }}$ with $M=10$ or $M=20$, this will significantly improve the predictive model.

However, these improvements are always conditional on the learning sample $\mathcal{L}$, and conditional on the difficulty that the selected model class and the model fitting procedure should not be flaw, i.e., the true model is close to the selected model class in the sense of the universality statements and suitable models can be found by the selected SGD procedure. Moreover, computing the nagging predictor can be demanding because one needs to fit the network architecture $M$ times. There is a recent proposal that performs multiple predictions within the same model and learning procedure; see Gorishniy et al. $[85]$.

# 5.5 Summary on feed-forward neural networks 

The previous sections introduced FNNs and their SGD training. This builds the core of deep learning on tabular data. The following sections of this chapter present FNN architectures that are particularly useful for solving actuarial problems, and Chapter 8, below, presents deep learning architectures for tensor data and unstructured data.

We summarize the standard procedure of deep learning as follows.
![Page 96 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p96_img1.jpg)

## Page 97
# Summary of FNN regression modeling 

- Perform covariate pre-processing; see Section 5.3.2.
- Select a deviance loss function that reflects the properties of the responses.
- Select a suitable FNN architecture, a momentum-based SGD algorithm, and a suitable batch size; see Sections 5.3.7 and 5.3.8.
- Run SGD fitting with early stopping using a call back; see Section 5.3.5. This can be complemented with regularization and drop-out; see Section 5.3.6
- Apply a balance correction to comply with the balance property (4.4); see Remark 5.3.
- Repeat this $M$ times to compute the nagging predictor (5.17).

The next two sections present two FNN architectures that are attractive to solve actuarial problems. The first one combines a GLM with FNN features, and the second one locally looks like a GLM.
We close this short section by highlighting the reference Richman-Wüthrich [193] on the ICEnet architecture. Generally, it is non-trivial to enforce smoothness and monotonicity in FNN architectures. The ICEnet is a regularized FNN method that achieves these properties. This requires evaluation of first differences and to do so in the ICEnet, it is necessary to have a multi-output network to be able to simultaneously obtain predictions for adjacent inputs; see Richman-Wüthrich [193].

### 5.6 Combing a GLM and a neural network

This section discusses boosting of classical actuarial regression models such as a GLM with FNN features. The main idea is to apply a two step fitting procedure. In a first step, we fit a classical statistical model, and in a second boosting step, we let a machine learning model analyze the residuals of the first model. If the machine learning model does not find any structure in these residuals, the first model seems to perform well, otherwise, if it finds structure, it boosts the first model by adding this structure. This proposal has been discussed in an editorial of the ASTIN Bulletin called 'Yes, we CANN!' to promote machine learning research within the actuarial community; see Wüthrich-Merz [242]. Similar ideas have been developed known as ResNet (residual network) in He et al. [96]. Nowadays, these are standard modules in advanced network architectures such as the transformers of Vaswani et al. [228].
We start by first fitting a GLM to our predictive problem. This provides us with a MLE fitted GLM

$$
\widehat{\mu}^{\mathrm{GLM}}(\boldsymbol{X}):=\mu_{\widehat{\vartheta}^{\mathrm{MLE}}}^{\mathrm{GLM}}(\boldsymbol{X})=g^{-1}\left\langle\widehat{\vartheta}^{\mathrm{MLE}}, \boldsymbol{X}\right\rangle
$$

with MLE $\widehat{\vartheta}^{\mathrm{MLE}} \in \mathbb{R}^{q+1}$ and link function $g$. This first fitting has been performed on a learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$ and it provides us with the estimated residuals,

## Page 98
$1 \leq i \leq n$,

$$
\widehat{\varepsilon}_{i}=Y_{i}-\widehat{\mu}^{\mathrm{GLM}}\left(\boldsymbol{X}_{i}\right)
$$

If this fitted GLM is suitable for the collected data, these residuals should not show any systematic structure. That is, these residuals should be (roughly) independent and centered (on average), and there should not be any systematic effects in these residuals as a function of the covariates $\boldsymbol{X}$. This motivates us to study a new, second regression step, namely, we regress the residuals from the covariates on the new learning sample $\mathcal{L}^{i}=$ $\left(\widehat{\varepsilon}_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$. This is precisely the basic idea behind boosting, namely, one stage-wise adaptively tries to improve the model by specifically focusing on finding the weaknesses of the previous model(s). This is quite different from ensembling, which (only) averages over the models, but it does not let the individual models compete to improve them, see Section 5.4 for ensembling.

Remarks 5.4. The residuals defined in (5.19) need some care. First, they are not independent, even if the instances $1 \leq i \leq n$ are independent. Note that the learning sample $\mathcal{L}$ enters the estimated regression function $\widehat{\mu}^{\mathrm{GLM}}=\mu_{\mathrm{gMLE}}^{\mathrm{GLM}}$. This typically implies a negative correlation between the estimated residuals. This is also the reason why empirical variance estimators are normalized by $1 /(n-1)$ and not by $1 / n$ to receive unbiased variance estimators. Second, the residuals in (5.19) may have different variances, even under the true regression function $\mu^{*}$ because they are not standardized. If we know that the learning data has been generated by a member of the EDF with cumulant function $\kappa$, the standardization is straightforward from (2.4), i.e., using the variance function $V(\cdot)=\left(\kappa^{\prime \prime} \circ h\right)(\cdot)$ with canonical link $h$. That is, based on this variance function, we obtain Pearson's residuals

$$
\widehat{\varepsilon}_{i}^{P}=\frac{Y_{i}-\widehat{\mu}^{\mathrm{GLM}}\left(\boldsymbol{X}_{i}\right)}{\sqrt{V\left(\widehat{\mu}^{\mathrm{GLM}}\left(\boldsymbol{X}_{i}\right)\right) / v_{i}}}
$$

These Pearson's residuals should roughly look like an independent sequence of centered variables having the same dispersion, in particular, they should not show any structure in the covariates and as a function of the estimated regression function. Otherwise, either the estimated regression function is not correctly specified, or the selected cumulant function $\kappa$ does not provide the correct variance behavior; see also Delong-Wüthrich [51] for variance back-testing using isotonic regression. The residuals (5.20) can also be used to receive Pearson's dispersion estimate defined by

$$
\widehat{\varphi}^{P}=\frac{1}{n-(q+1)} \sum_{i=1}^{n}\left(\widehat{\varepsilon}_{i}^{P}\right)^{2}
$$

if the estimated GLM function $\widehat{\mu}^{\mathrm{GLM}}$ involves $q+1$ estimated regression parameters. Pearson's dispersion estimate is consistent, i.e., it converges to the true value, a.s., for increasing sample size.

The CANN proposal of Wüthrich-Merz [242] does not explicitly compute the residuals, but it directly adds a regression function to the first estimated model, i.e., it acts on the (linear) predictor scale. Based on a given regression function $\widehat{\mu}^{\mathrm{GLM}}$ with link $g$ it makes the Ansatz

$$
\mu^{\mathrm{CANN}}(\boldsymbol{X})=g^{-1}\left(g\left(\widehat{\mu}^{\mathrm{GLM}}(\boldsymbol{X})\right)+\left\langle\boldsymbol{w}^{(d+1)}, \boldsymbol{z}^{(d: 1)}(\boldsymbol{X})\right\rangle\right)
$$

Version March 3, 2025, @AI Tools for Actuaries

## Page 99
and since the first model is a GLM with link $g$, we can equivalently write

$$
\mu^{\mathrm{CANN}}(\boldsymbol{X})=g^{-1}\left(\left\langle\widehat{\vartheta}^{\mathrm{MLE}}, \boldsymbol{X}\right\rangle+\left\langle\boldsymbol{w}^{(d+1)}, \boldsymbol{z}^{(d: 1)}(\boldsymbol{X})\right\rangle\right)
$$

where we assume that $\widehat{\vartheta}^{\text {MLE }}$ has been fitted in a first GLM step and is kept fixed (frozen) in the second estimation step, and where the second part of (5.22) describes a FNN architecture. In this second CANN step, only this second (FNN) part is fitted to detect more systematic structure that has not been found by the initial GLM. If the fitted FNN part in this second CANN step is equal to zero, then we are back in the GLM. This expresses that the FNN could not find any additional systematic structure that is not already integrated into the GLM.
Remark that keeping the first part $\left\langle\widehat{\vartheta}^{\mathrm{MLE}}, \boldsymbol{X}\right\rangle$ frozen during the second boosting step (fitting the FNN) can also be interpreted as having an offset playing the role of known prior differences, and one wants to see whether one finds more differences beyond this offset.
For fitting the FNN we apply a SGD algorithm on training and validation data as explained above. This two step estimation concept has now been applied successfully in many studies, see, e.g., Brauer [26] and Havrylenko-Heger [95], the latter reference uses this CANN approach to detect interactions.
In view of (5.22) the similarity to ResNet is apparent. The second term in (5.22) describes a classic FNN architecture, the first term can be interpreted as a residual connection or a skip connection because it connects the input $\boldsymbol{X}$ directly to the output; for an illustration see Wüthrich-Merz [243, Figure 7.14]. We can also interpret (5.22) as having a linear (GLM) term and we build a non-linear FNN architecture around this linear term to capture interactions and non-linearities not present in the GLM-term.

# 5.7 LocalGLMnet 

Essentially, there are two different ways of explaining results of algorithmic models. Either one uses post-hoc methods, we discuss these in Chapter [insert], below, or one tries to integrate explainable features into the algorithmic models. The LocalGLMnet is a FNN architecture that attempts to design a model that provides these integrated explainable features; we refer to Richman-Wüthrich [190, 191]. The LocalGLMnet can be seen as a varying coefficient model; for varying coefficient models we refer to Hastie-Tibshirani [92], and in a tree-based context to Zhou-Hooker [249] and Zakrisson-Lindholm [247], the latter discussing parameter identifiability issues, which we are also going to face in this section.
The starting point is a GLM whose sensitivities can easily be understood, especially, under the log-link choice, see Example 3.1. Recall the GLM regression function

$$
\mu_{\vartheta}(\boldsymbol{X})=g^{-1}\langle\vartheta, \boldsymbol{X}\rangle=g^{-1}\left(\vartheta_{0}+\sum_{j=1}^{q} \vartheta_{j} X_{j}\right)
$$

with regression parameter $\vartheta \in \mathbb{R}^{q+1}$. This regression parameter takes a fixed value that is estimated with MLE. The LocalGLMnet architecture replaces this fixed parameter $\vartheta$

## Page 100
by a multi-output FNN architecture (function) $\boldsymbol{z}^{(d: 1)}=\left(z_{1}^{(d: 1)}, \ldots, z_{q}^{(d: 1)}\right)^{\top}$

$$
\mu_{\vartheta}(\boldsymbol{X})=g^{-1}\left(\vartheta_{0}+\sum_{j=1}^{q} z_{j}^{(d: 1)}(\boldsymbol{X}) X_{j}\right)
$$

with a real-valued bias parameter $\vartheta_{0} \in \mathbb{R}$ and having a multi-output FNN architecture

$$
\boldsymbol{z}^{(d: 1)}: \mathbb{R}^{q} \rightarrow \mathbb{R}^{q}
$$

Thus, the GLM parameters $\left(\vartheta_{j}\right)_{j=1}^{q}$ are replaced by network outputs $\left(z_{j}^{(d: 1)}(\boldsymbol{X})\right)_{j=1}^{q}$ of the same dimension $q$. Locally, these network outputs look like constants and, therefore, the LocalGLMnet behaves locally as a GLM. This is precisely the main motivation to study the architecture in (5.24). While we estimated the parameter $\vartheta \in \mathbb{R}^{q+1}$ with MLE in GLMs, we now learn these attention weights $\left(z_{j}^{(d: 1)}(\boldsymbol{X})\right)_{j=1}^{q}$ with SGD fitting within a FNN framework.
The learned attention weights $\left(z_{j}^{(d: 1)}(\boldsymbol{X})\right)_{j=1}^{q}$ allow for nice interpretations:
(1) We focus on the individual terms under the $j$-summation in (5.24). If for the $j$ th component $X_{j}$ the learned network output is constant, $z_{j}^{(d: 1)}(\boldsymbol{X}) \equiv \vartheta_{j} \neq 0$, we effectively have a GLM component in this term. Therefore, we aim at understanding whether the multi-output network provides sensitivities in the inputs or not. If there are no sensitivities we should go for a GLM.
(2) Property $z_{j}^{(d: 1)}(\boldsymbol{X}) \equiv 0$ for some $j$, proposes to completely drop this term from the regression function. This is a way of selecting or dropping terms from the LocalGLMnet regression function. In fact, Richman-Wüthrich [190] propose an empirical statistical test to check for this kind of model sparsity.
(3) If we obtain an attention weight $z_{j}^{(d: 1)}(\boldsymbol{X})=z_{j}^{(d: 1)}\left(X_{j}\right)$ that only depends on the covariate component $X_{j}$, we know that this term does not interact with any other covariate components. More generally, we can test for interactions by considering for a fixed component $j$ the gradient w.r.t. $\boldsymbol{X}$

$$
\nabla z_{j}^{(d: 1)}(\boldsymbol{X})=\left(\frac{\partial}{\partial X_{1}} z_{j}^{(d: 1)}(\boldsymbol{X}), \ldots, \frac{\partial}{\partial X_{q}} z_{j}^{(d: 1)}(\boldsymbol{X})\right)^{\top} \in \mathbb{R}^{q}
$$

This allows us to understand the local interactions in the $j$-th term in the neighborhood of $\boldsymbol{X}$.

This all looks very nice and convincing, however, there is a caveat that needs careful consideration. Namely, the LocalGLMnet regression function lacks identifiability. We briefly discuss this in the following items.
(4) Due to the flexibility of large FNNs we may find a term that gives us the function

$$
z_{j}^{(d: 1)}(\boldsymbol{X}) X_{j}=X_{j^{\prime}}
$$

by learning an attention weight $z_{j}^{(d: 1)}(\boldsymbol{X})=X_{j^{\prime}} / X_{j}$, for $j^{\prime} \neq j$. This is the reason, why we speak about dropping a 'term' and not a 'covariate component' in the previous items (1)-(3), because even if we drop the term for $X_{j}$, this covariate component may still play an important role in the attention weights of other terms.

## Page 101
(5) Related to item (4), for SGD training of the LocalGLMnet we need to initialize the gradient descent algorithm. We recommend to initialize the network weights that we precisely start in the MLE fitted GLM (5.23). In our examples, this has pre-determined the role of all $j$-terms such that we did not encounter any situation where an issue similar to (5.26) occurred.

Assume that all covariate components are standardized to be centered with unit variance, i.e., we have standardized columns in the design matrix $\mathfrak{X}$. This makes the attention weights $z_{j}^{(d: 1)}(\boldsymbol{X})$ directly comparable across the different components $1 \leq j \leq q$.
It motivates a measure of variable importance by defining the sample averages

$$
I_{j}=\frac{1}{n} \sum_{i=1}^{n}\left|z_{j}^{(d: 1)}\left(\boldsymbol{X}_{i}\right)\right|
$$

If this value is very small, the empirical test of Richman-Wüthrich [190] gives support to the null-hypothesis of dropping this term and, obviously, if $I_{j}$ is large it has a big impact on the regression function (because the centering of the covariates implies that the regression function is calibrated to zero); this is similar to the LRTs and the $p$-values in GLMs, see Listing 3.1.
Since the LocalGLMnet locally behaves like a GLM, if the attention weights do not take extreme values, there is also some similarity to the post-hoc interpretability tool called local interpretable model-agnostic explanations (LIME) by Ribeiro et al. [185]. LIME fits a LASSO regularized GLM locally to individual covariate values $\boldsymbol{X}$ to describe the most important variables that explain the regression value $\widehat{\mu}(\boldsymbol{X})$ of a fitted regression model. Using the attention weights $\left(z_{j}^{(d: 1)}(\boldsymbol{X})\right)_{j=1}^{q}$ we have similar, but more precise, information about this local behavior in $\boldsymbol{X}$; we come back to LIME in Section [insert], below.

# 5.8 Outlook: Kolmogorov-Arnold networks 

At the core of the great interest and success of FNNs (multi-layer perceptrons, MLPs) are the universality theorems that build the mathematical foundation of describing the approximation capacity of these function classes, see Section 5.2. More generally, this approximation question can be related to David Hilbert's 13th problem which looks for algebraic function solutions (of two arguments) to a certain class of problems. KolmogorovArnold $[125,5]$ solved a version of Hilbert's 13th problem, also known as the KolmogorovArnold representation theorem. This approach structurally resembles FNNs, with one essential difference, and this difference is precisely the basis of the so-called KolmogorovArnold networks (KANs) introduced by Liu et al. [141]. In FNNs we have fixed activation functions $\phi$ in the neurons (units), and the weights are the parts that are learnable from the data. If we illustrate this graphically, see Figure 5.1, we can think of nodes (units) being connected by edges. The nodes correspond to the neurons $z_{j}^{(m)}$, and they have a fixed functional structure given by the selected activation function $\phi$. The edges described by the network weights $w_{j, l}^{(m)}$ then connect these nodes, and these edges are the part of the network architecture that are trainable from the learning sample $\mathcal{L}$.

## Page 102
For KANs we exchange these roles by putting learnable activation functions on the edges in the form of learnable splines, and we set all weights (in the nodes) equal to one. Let $\left(B_{s}\right)_{s}$ be a family of B-splines. ${ }^{2}$ For a KAN we build the splines

$$
x \in \mathbb{R} \mapsto S(x)=\sum_{s} w_{s} B_{s}(x)
$$

with learnable weights $\left(w_{s}\right)_{s} \subset \mathbb{R}$. That is, every spline $S$ incorporates weights $\left(w_{s}\right)_{s}$ that can be trained with SGD methods. In the KAN proposal of Liu et al. [141], these splines are used as residual connections around the SiLU function, defining the KAN activation functions $\phi: \mathbb{R} \rightarrow \mathbb{R}$ by

$$
x \mapsto \phi(x)=w(\operatorname{SiLU}(x)+S(x))=w\left(\operatorname{SiLU}(x)+\sum_{s} w_{s} B_{s}(x)\right)
$$

with another weight $w \in \mathbb{R}$ and the SiLU function given in Table 5.1. These are highly flexible activation functions that can be trained on learning data.
We are now ready to define a KAN layer, which is the analogue to the FNN layer introduced in (5.5)-(5.6).

KAN layer. Based on the selected class of KAN activation functions (5.28), we define the KAN layer $\boldsymbol{z}^{(m)}: \mathbb{R}^{q_{m-1}} \rightarrow \mathbb{R}^{q_{m}}$ as follows. For $\boldsymbol{x}=\left(x_{1}, \ldots, x_{q_{m-1}}\right)^{\top} \in \mathbb{R}^{q_{m-1}}$, we set

$$
\boldsymbol{z}^{(m)}(\boldsymbol{x})=\left(z_{1}^{(m)}(\boldsymbol{x}), \ldots, z_{q_{m}}^{(m)}(\boldsymbol{x})\right)^{\top}
$$

with units for $1 \leq j \leq q_{m}$

$$
z_{j}^{(m)}(\boldsymbol{x})=\sum_{l=0}^{q_{m-1}} \phi_{j, l}^{(m)}\left(x_{l}\right)
$$

for KAN activation functions $\phi_{j, l}^{(m)}, 1 \leq j \leq q_{m}$ and $0 \leq l \leq q_{m-1}$, of structure (5.28).
Now, we are on familiar grounds because the only difference to FNNs is that we replace the FNN neurons (5.6) by the KAN units (5.29). The KAN layers can then be composed as in (5.3), and from this we construct the KAN output (5.4).
Liu et al. [141] give various examples of the superior behavior of KANs over FNNs, this comes at the price of higher computational efforts and more hyper-parameter tuning. E.g., it requires the selection of the number of knots in the selected B-splines. For this we need to set a grid across the real line, a finer grid gives higher local accuracy but also higher computational efforts and higher model storage costs. Most of the analysis presented in Liu et al. [141] focuses on function approximation in deterministic settings, which is a rather different kind of problem compared to training a predictive model on noisy data. When it comes to statistical modeling problems, it is unclear whether these higher computational and hyper-parameter tuning efforts are justified, in-sample over-fitting being the most serious concern (that is difficult to control in highly flexible models). Certainly, flexible KANs need sophisticated regularization techniques for a successful training which are not fully understood at the moment. With this we close this short section on KANs.

[^0]
[^0]:    ${ }^{2}$ Selecting a B-spline means that we need to select the polynomial degree of the spline, e.g., cubic, and we need to selected the knots where the piecewise polynomial functions are concatenated.

## Page 103
# Chapter 6 

## Regression trees and random forests

Regression trees (decision trees) have been introduced in the seminal monograph of Breiman et al. [31] called classification and regression trees (CARTs), published in 1984. Regression trees are based on recursively partitioning the covariate space, therefore, this technique is also known as rpart in R; see Therneau-Atkinson [215]. Nowadays, regression trees are not used any more in their pure form because they are not fully competitive with more advanced regression methods. However, they are the main building blocks of gradient boosting machines (GBMs) and random forests. For this reason, we give a short introduction to regression trees in this chapter. In GBMs many small regression trees (called weak learners) are combined to a powerful predictor, and in random forests many large and noisy regression trees are combined with bagging to a more powerful predictor. Random forest has been introduced by Breiman [30], and it will be discussed in this chapter, GBMs will be discussed in Chapter 7, below.

### 6.1 Regression trees

The main idea behind regression trees is to partition the covariate space $\mathcal{X} \subset \mathbb{R}^{q}$ into homogeneous subsets w.r.t. the prediction task at hand. This precisely reflects the core of actuarial pricing in trying to build homogeneous risk classes; see, e.g., Bailey-Simon [11]. A finite partition of the covariate space $\mathcal{X}$ is given by a finite index set T and a collection $\left(\mathcal{X}_{t}\right)_{t \in \mathrm{~T}}$ of non-empty subsets of $\mathcal{X}$ such that

$$
\mathcal{X}=\bigcup_{t \in \mathrm{~T}} \mathcal{X}_{t} \quad \text { and } \quad \mathcal{X}_{t} \cap \mathcal{X}_{s}=\emptyset \quad \text { for all } t \neq s
$$

This finite partition is constructed by a binary tree, and we call $\left(\mathcal{X}_{t}\right)_{t \in \mathrm{~T}}$ the leaves of this binary tree as these sets are the knots of the binary tree that do not have any descendants, see Figure 6.1 for an example with six leaves.
Assuming that all insurance policyholders $\boldsymbol{X} \in \mathcal{X}_{t}$, who belong to the same leaf $\mathcal{X}_{t}$, have the same risk behavior, motivates to define the regression function as

$$
\boldsymbol{X} \mapsto \mu(\boldsymbol{X})=\sum_{t \in \mathrm{~T}} \mu_{t} \mathbb{1}_{\left\{\boldsymbol{X} \in \mathcal{X}_{t}\right\}}
$$

## Page 104
Figure 6.1: Binary regression tree with three binary splits resulting in six leaves.
with conditional mean parameters $\mu_{t} \in \mathbb{R}$, for $t \in \mathrm{~T}$. We call $\mu_{t}$ conditional mean parameter because it reflects the conditionally expected response $\mathbb{E}[Y \mid \boldsymbol{X}]$ on the leaf $\boldsymbol{X} \in$ $\mathcal{X}_{t}$. Figure 6.2 (lhs) illustrates a partition of a two-dimensional rectangular covariate space $\mathcal{X} \subset \mathbb{R}^{2}$ into ten leaves $\left(\mathcal{X}_{t}\right)_{t \in \mathrm{~T}}$, and the different colors reflect the different conditional means $\left(\mu_{t}\right)_{t \in \mathrm{~T}}$ on the corresponding leaves. The right-hand side of the figure shows a GLM regression function with a multiplicative structure.

Figure 6.2: (lhs) Partition $\left(\mathcal{X}_{t}\right)_{t \in \mathrm{~T}}$ of a rectangular covariate space $\mathcal{X} \subset \mathbb{R}^{2}$ with differently colored conditional means $\left(\mu_{t}\right)_{t \in \mathrm{~T}}$ on the corresponding leaves; (rhs) GLM with multiplicative structure.

There are two main items to be selected to design the regression tree function (6.2):
(1) The partitioning of the covariate space $\mathcal{X}$ into the leaves $\left(\mathcal{X}_{t}\right)_{t \in \mathrm{~T}}$; and
(2) the selection of the conditional means $\left(\mu_{t}\right)_{t \in \mathrm{~T}}$ on the leaves.

We discuss the recursive partitioning algorithm to solve these two tasks.
![Page 104 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p104_img1.jpg)
![Page 104 Image 2](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p104_img2.jpg)

## Page 105
Recursive partitioning algorithm. We briefly give a non-technical description, and the fast reader can skip the following paragraphs which give a mathematical foundation to this brief description. Broadly speaking, the recursive partitioning algorithm analyzes in each loop of the algorithm which of the leaves $\left(\mathcal{X}_{t}\right)_{t \in \mathrm{~T}}$ is the least homogeneous one (measured in some loss metric). The least homogeneous leaf, say $\mathcal{X}_{t}$, is then partitioned into two parts $\mathcal{X}_{t 0}$ and $\mathcal{X}_{t 1}$ to increase the homogeneity. This is how the binary tree is grown, i.e., it replaces the old leaf $\mathcal{X}_{t}$ by its two descendants $\mathcal{X}_{t 0}$ and $\mathcal{X}_{t 1}$, which results in an increased partition; see Figure 6.1 for an example. This is recursively iterated until all the leaves are sufficiently homogeneous.

Covariate pre-processing. Continuous covariate components do not need any preprocessing. To control the computational complexity, target encoding (2.16) is applied to the categorical covariate components, and to improve accuracy, target encoding is performed individually on each leaf $\mathcal{X}_{t}, t \in \mathrm{~T}$, before applying the next recursive partitioning step. For large trees and many high-cardinality categorical covariates this can be prohibitive.

Initialization. The recursive partitioning algorithm is initialized by setting $\mathrm{T}=\{0\}$, selecting the so-called root tree $\mathcal{X}_{0}=\mathcal{X}$, and setting as mean estimate for $\mu_{0}$ the weighted empirical mean $\widehat{\mu}_{0}=\sum_{i=1}^{n} v_{i} Y_{i} / \sum_{i=1}^{n} v_{i}$. We now generally put hats $\widehat{\mu}$ on top of all $\mu$ values to indicate that these are estimated from the learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$.
(Binary) recursive partitioning iteration. Assume we have a partition $\left(\mathcal{X}_{t}, \widehat{\mu}_{t}\right)_{t \in \mathrm{~T}}$ of the covariate space $\mathcal{X}$ with corresponding estimated conditional means. Figure 6.1 gives an example where we have applied 5 binary splits resulting in 6 leaves, i.e., $|\mathrm{T}|=6$. For the next iteration of the algorithm, the following needs to be done:
(a) Assume we want to partition leaf $\mathcal{X}_{t}$. To control the combinatorial complexity, we only analyze standardized binary splits (SBS) meaning that the split criterion is based on one single covariate component of $\boldsymbol{X}$ only, say $X_{k}$, and we allocate all instances $i$ with $X_{i, k} \leq c$ to one descendant $\mathcal{X}_{t 0}$, and otherwise, if $X_{i, k}>c$, we allocate instance $i$ to the other descendant $\mathcal{X}_{t 1}$ of the selected leaf $\mathcal{X}_{t}$ to be partitioned. This gives so-called 'rectangular binary splits' as illustrated in Figure 6.2 (lhs). Remark that this can also be applied to the target encoded categorical covariate components (2.16).
(b) Select the least homogeneous leaf from $\left(\mathcal{X}_{t}\right)_{t \in \mathrm{~T}}$, i.e., the leaf for which we can find the most efficient SBS w.r.t. some objective function.
(c) Estimate the conditional means on these two new leaves $\mathcal{X}_{t 0}$ and $\mathcal{X}_{t 1}$.

Items (a)-(c) require to choose a leaf $\mathcal{X}_{t}$ of the actual tree $\left(\mathcal{X}_{t}\right)_{t \in \mathrm{~T}}$, a covariate component $X_{k}, 1 \leq k \leq q$, that serves for the next SBS, and a split level $c \in \mathbb{R}$ that partitions w.r.t. the selected covariate component $X_{k}$. To decide about these three choices, we need an objective function. Since we estimate conditional means, it is natural to take a strictly consistent loss function $L$ for mean estimation.

## Page 106
This then translates items (a)-(c) into the following optimization problem

$$
\begin{aligned}
(\hat{t}, \hat{k}, \hat{c})=\underset{t \in \Upsilon, 1 \leq k \leq q, c \in \mathbb{R}}{\arg \max } & \sum_{i: \boldsymbol{X}_{i} \in \mathcal{X}_{t}} \frac{v_{i}}{\varphi}\left[L\left(Y_{i}, \widehat{\mu}_{t}\right)\right. \\
& \left.-\left(L\left(Y_{i}, \widehat{\mu}_{t 0}\right) \mathbb{1}_{\left\{X_{i, k} \leq c\right\}}+L\left(Y_{i}, \widehat{\mu}_{t 1}\right) \mathbb{1}_{\left\{X_{i, k}>c\right\}}\right)\right]
\end{aligned}
$$

with weighted empirical means

$$
\widehat{\mu}_{t 0}=\frac{\sum_{i: \boldsymbol{X}_{i} \in \mathcal{X}_{t}} v_{i} Y_{i} \mathbb{1}_{\left\{X_{i, k} \leq c\right\}}}{\sum_{i: \boldsymbol{X}_{i} \in \mathcal{X}_{t}} v_{i} \mathbb{1}_{\left\{X_{i, k} \leq c\right\}}} \quad \text { and } \quad \widehat{\mu}_{t 1}=\frac{\sum_{i: \boldsymbol{X}_{i} \in \mathcal{X}_{t}} v_{i} Y_{i} \mathbb{1}_{\left\{X_{i, k}>c\right\}}}{\sum_{i: \boldsymbol{X}_{i} \in \mathcal{X}_{t}} v_{i} \mathbb{1}_{\left\{X_{i, k}>c\right\}}}
$$

This may look complicated, but it (only) says that we try to find the leaf $\mathcal{X}_{\hat{t}}$, the covariate component $X_{\hat{k}}$ and the split level $\hat{c}$ that provides the biggest decrease in loss (6.3) by this additional SBS. Moreover, the weighted empirical means (6.4) are the optimal predictors on both parts of the partitioned leaf $\mathcal{X}_{t}$ w.r.t. the selected strictly consistent loss function $L$. Therefore, the objective function in (6.3) is lower bounded by zero.
The solution of (6.3) gives us the new leaves, i.e., the descendants of $\mathcal{X}_{\hat{t}}$ defined by

$$
\mathcal{X}_{\hat{t} 0}=\left\{\boldsymbol{x} \in \mathcal{X}_{\hat{t}}: x_{\hat{k}} \leq \hat{c}\right\} \quad \text { and } \quad \mathcal{X}_{\hat{t} 1}=\left\{\boldsymbol{x} \in \mathcal{X}_{\hat{t}}: x_{\hat{k}}>\hat{c}\right\}
$$

with the new (updated) index set

$$
\top \leftarrow(\top \backslash\{\hat{t}\}) \cup\{\hat{t} 0, \hat{t} 1\}
$$

and the empirical weighted means $\widehat{\mu}_{\hat{t} 0}$ and $\widehat{\mu}_{\hat{t} 1}$ on the new leaves $\mathcal{X}_{\hat{t} 0}$ and $\mathcal{X}_{\hat{t} 1}$, respectively. This fully explains the SBS recursive partitioning algorithm, and this is the standard regression tree algorithm usually used.
We close this section with some remarks.

- The selection of the optimal split level $\hat{c}$ in (6.3) is not unique because we work with a finite sample on every leaf $\mathcal{X}_{t}$. Typically, the split levels $c \in \mathbb{R}$ are chosen precisely in the middle of adjacent observed covariate values to make them unique.
- In practice, one only considers potential SBS that exceed a minimal number of instances in both descendants $\mathcal{X}_{t 0}$ and $\mathcal{X}_{t 1}$ of leaf $\mathcal{X}_{t}$, otherwise one cannot reliably estimate the weighted empirical means (6.4). In implementations, there is a hyper-parameter related to the minimal leaf size which precisely accounts for this constraint. The choice of the minimal leaf size depends on the problem to be solved, e.g., for car insurance frequencies one typically requires 1000 insurance policies to receive reliable frequency estimates.
- It may happen that in one leave there are only instances with zero claims, which (of course) is a very homogeneous leaf. However, the mean estimate (6.4) typically leads to a degenerate model in that case. Therefore, often Bühlmann credibility is used with a credibility coefficient (shrinkage parameter) being selected as a hyperparameter; technically this is precisely done as in (2.17); see Therneau-Atkinson $[215]$.

## Page 107
- We did not discuss the stopping rule of the recursive partitioning algorithm. Of course, we should prevent from over-fitting. However, designing a good stopping rule is usually not feasible, also because optimization (6.3) only focuses on the next best split (greedy search), but maybe a next poor split can stimulate a second next excellent split. To account for such flexibility, a large binary regression tree can be constructed in a first step. In a second step, all parts of the large tree are pruned, if they do not sufficiently contribute to the required homogeneity in relation to the parameters involved; this is measured by analyzing how much a certain split contributes to the decrease in loss (including all its descendants and accounting for their complexity). This pruning step uses best-subset selection regularization (2.24), and, importantly, it can be performed efficiently by another recursive algorithm. The details are rather technical, they were proved in Breiman et al. [31], and, aligned to our notation, we refer to Wüthrich-Buser [241, Section 6.2]. We do not discuss this any further because we are not going to use regression trees in its pure form.
- Besides the insufficient predictive performance, also robustness of regression trees is an issue. It can happen that one of the first SBS looks completely different if one slightly perturbs a few instances in the learning sample $\mathcal{L}$, resulting in a very different predictive model. This missing robustness limits or even prevents using regression trees in insurance pricing. A way to control robustness is bagging and random forest, these will be discussed in Sections 6.2-6.3, below.


# 6.2 Bagging 

In view of the missing robustness of the plain-vanilla regression tree construction discussed in the previous section, there were many attempts to robustify regression tree predictors. For this, the non-parametric bootstrap, discussed in Section 1.5.4, is combined with aggregating, discussed in Section 5.4.1, resulting in Breiman's [29] bagging proposal.
We start by revisiting aggregation. As mentioned, the estimated regression tree related to (6.2) lacks robustness. Assume we have $M$ independent learning samples $\mathcal{L}^{(j)}, 1 \leq$ $j \leq M$, that follow the same data generating mechanism, and which have sample size $n$. This allows us to construct $M$ independent regression tree predictors (using the same methodology, but different independent learning data)

$$
\widehat{\mu}^{(j)}(\boldsymbol{X})=\sum_{t \in \Upsilon^{(j)}} \widehat{\mu}_{t}^{(j)} \mathbb{1}_{\left\{\boldsymbol{X} \in \mathcal{X}_{t}^{(j)}\right\}}
$$

where the upper index $1 \leq j \leq M$ denotes the different estimated regression trees. Since, by assumption, the underlying learning samples $\mathcal{L}^{(j)}$ and the resulting regression trees are i.i.d., the law of large numbers applies

$$
\lim _{M \rightarrow \infty} \frac{1}{M} \sum_{j=1}^{M} \widehat{\mu}^{(j)}=\mathbb{E}\left[\widehat{\mu}^{(1)}\right]
$$

a.s., and the randomness asymptotically vanishes, see (5.16). This highlights the advantages of aggregating, namely, the randomness (from the finite samples) asymptotically

## Page 108
vanishes. On the other hand, (6.5) also indicates a main issue of this technique. Namely, we have convergence to a deterministic limit $\mathbb{E}\left[\widehat{\mu}^{(1)}\right]$, but there is no guarantee that this limit is close to the true regression function $\mu^{*}$, i.e., if the individual regression tree constructions $\widehat{\mu}^{(j)}$ are biased (in some systematic way), so will the limit be. Therefore, aggregation is only a method to diminish uncertainty through randomness in the learning samples, but not for mitigating a (systematic) bias in the construction.

Example 6.1. An easy example for a biased estimation procedure is the following. If we set $\widehat{\mu}^{(j)}=\max _{1 \leq i \leq n} Y_{i}^{(j)}$, we certainly get a positive bias in this mean estimation procedure since the limit in (6.5) is equal to $\mathbb{E}\left[\max _{1 \leq i \leq n} Y_{i}^{(1)}\right]>\mathbb{E}\left[Y_{1}^{(1)}\right]=\mu^{*}$ in any non-deterministic situation with non-comonotonic responses and $n>1$.

For aggregation, we need multiple independent learning samples $\mathcal{L}^{(j)}$ and predictors $\widehat{\mu}^{(j)}$, respectively. Similarly to Section 5.4, it is not immediately clear where we can get these independent samples from. Breiman's [29] b in bagging refers to bootstrap simulation, or more precisely to the non-parametric bootstrap discussed in Section 1.5.4. Starting from the observed learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$, we draw with replacements independent bootstrap samples $\mathcal{L}^{(\star j)}=\left(Y_{i}^{(\star j)}, \boldsymbol{X}_{i}^{(\star j)}, v_{i}^{(\star j)}\right)_{i=1}^{n}$, where 'independent' applies to the drawing with replacements. The resulting bootstrapped learning samples $\left(\mathcal{L}^{(\star j)}\right)_{j=1}^{M}$ are conditionally i.i.d., given the learning sample $\mathcal{L}$. From these, we can construct conditionally i.i.d. regression tree predictors $\widehat{\mu}^{(\star j)}$ to which the law of large numbers applies, a.s.,

$$
\lim _{M \rightarrow \infty} \frac{1}{M} \sum_{j=1}^{M} \widehat{\mu}^{(\star j)}=\mathbb{E}\left[\left.\widehat{\mu}^{(\star 1)} \right\rvert\, \mathcal{L}\right]
$$

The same remark about the bias applies as above, but this time the bias additionally depends on the specific observations in the learning sample $\mathcal{L}$, e.g., having a small sample with an outlier will likely result in a largely biased predictor, if the outlier is not properly controlled. On the other hand, the out-of-bag method (unique to non-parametric bootstrapping) gives one an easy (and integrated) cross-validation technique that may allow to detect such biases; for out-of-bag validation, see (1.22).
A general issue with bagging is that the individual bootstrapped regression trees $\widehat{\mu}^{(\star j)}$ are highly correlated because the identical observations are recycled many times. This mutual dependence makes this whole modeling approach not very efficient, and hence these regression trees are not used in actuarial science. Random forests discussed in the next section precisely tries to improve on this point.

# 6.3 Random forests 

The careful reader will have noticed that in the previous section we have not been mentioning the sizes of the constructed regression trees, i.e., the number of resulting leaves $|\mathrm{T}|$. For Breiman's [30] random forests, we construct very large trees $|\mathrm{T}| \gg 1$ to introduce more randomness into the procedure, and to decorrelate these large trees, we employ a procedure that adds additional randomness to the regression tree construction by frequently missing the optimal partition in (6.3). Thus, in contrast to bagging, we aim at having more randomness in the regression tree construction. In particular, constructing

## Page 109
large regression trees frequently missing the optimal split provides some over-fitting but also a more random tree construction. This precisely has a decorrelating effect, resulting in the random forests predictor discussed next.

As for bagging, we generate i.i.d. bootstrap samples $\mathcal{L}^{(\star j)}=\left(Y_{i}^{(\star j)}, \boldsymbol{X}_{i}^{(\star j)}, v_{i}^{(\star j)}\right)_{t=1}^{n}$ from the learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$ by drawing with replacements. For each bootstrap sample, $\mathcal{L}^{(\star j)}=\left(Y_{i}^{(\star j)}, \boldsymbol{X}_{i}^{(\star j)}, v_{i}^{(\star j)}\right)_{i=1}^{n}$, we construct a large and noisy regression tree estimator $\tilde{\mu}^{(\star j)}$ as follows. Consider the $j$-th bootstrap sample $\mathcal{L}^{(\star j)}$, and assume we have constructed a binary tree $\left(\mathcal{X}_{t}^{(\star j)}, \tilde{\mu}_{t}^{(\star j)}\right)_{t \in \Upsilon}$ on that bootstrap sample that we want to further partition similar to (6.3). To add randomness, we select in each loop of the SBS recursive partitioning algorithm a non-empty random subset $\mathbb{Q} \subset\{1, \ldots, q\}$ of the covariate components $\boldsymbol{X}=\left(X_{1}, \ldots, X_{q}\right)^{\top}$, and we only consider the components in $\mathbb{Q}$ for the next SBS, that is, we replace (6.3) by

$$
\begin{aligned}
(\hat{t}, \hat{k}, \hat{c})=\underset{t \in \mathrm{~T}, k \in \mathbb{Q}, c \in \mathbb{R}}{\arg \max } & \sum_{i: \boldsymbol{X}_{i}^{(\star j)} \in \mathcal{X}_{t}^{(\star j)}} \frac{v_{i}^{(\star j)}}{\varphi}\left[L\left(Y_{i}^{(\star j)}, \tilde{\mu}_{t}^{(\star j)}\right)\right. \\
& \left.-\left(L\left(Y_{i}^{(\star j)}, \tilde{\mu}_{t 0}^{(\star j)}\right) \mathbb{1}_{\left\{X_{i, k}^{(\star j)} \leq c\right\}}+L\left(Y_{i}^{(\star j)}, \tilde{\mu}_{t 1}^{(\star j)}\right) \mathbb{1}_{\left\{X_{i, k}^{(\star j)}>c\right\}}\right)\right]
\end{aligned}
$$

the main difference to (6.3) being the random set $\mathbb{Q}$, highlighted in magenta color in (6.6). This algorithm gives us a randomized and bootstrapped regression tree predictor $\tilde{\mu}^{(\star j)}(\boldsymbol{X})$ for each bootstrap sample $\mathcal{L}^{(\star j)}, 1 \leq j \leq M$.
Aggregating over these regression trees allows us to define the random forest predictor

$$
\tilde{\mu}^{\mathrm{RF}}(\boldsymbol{X})=\frac{1}{M} \sum_{j=1}^{M} \tilde{\mu}^{(\star j)}(\boldsymbol{X})
$$

We give some remarks:

- By sampling a true subset $\mathcal{Q} \varsubsetneqq\{1, \ldots, q\}$ we may miss the optimal SBS. This introduces more randomness and decorrelation for i.i.d. sets $\mathcal{Q}$ in each iteration of the recursive partitioning algorithm.
- If $\mathcal{Q} \equiv\{1, \ldots, q\}$, there is no difference between bagging and random forests.
- Often, $\mathcal{Q}$ is set to have a fixed size in all recursive partitioning steps, popular choices are $\sqrt{q}$ or $\lfloor q / 3\rfloor$ for the size of $\mathcal{Q}$.
- Generally, random forest predictors are not as competitive as networks and GBMs, that is why these techniques are not used very frequently. Moreover, random forests can be computationally intensive, i.e., constructing large trees on potentially many high-cardinality categorical covariates can severely impact the fitting time.
- Standard random forest packages often work under the Gaussian loss assumption which is not appropriate in many actuarial problems, and this loss cannot easily be replaced in these implementations.

## Page 110
- Nevertheless, random forests are still considered to be useful in actuarial application. They are comparably simple in applications and they do not need much hyper-parameter tuning.
- First, they may help to detect interactions, and if there are interactions a more sophisticated method can be used.
- Second, they are used as a surrogate model for explainability, because through the splitting mechanism they provide a simple variable importance measure. This is explained next.

There is a nice application though of random forests that is used. Assume we have fitted a regression model $\widehat{\mu}: \mathcal{X} \rightarrow \mathbb{R}$ to the learning data $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$, and we would like to have a measure of variable importance, meaning that we would like to measure which of the components $X_{k}$ of the covariates $\boldsymbol{X}$ has a big impact on the regression function. A possible solution to this question is to fit a random forest surrogate model $\widehat{\mu}^{\mathrm{RF}}$ to the regression function $\widehat{\mu}$. That is, we fit a random forest regression function $\widehat{\mu}^{\mathrm{RF}}$ to the learning data $\widetilde{\mathcal{L}}=\left(\widehat{\mu}\left(\boldsymbol{X}_{i}\right), \boldsymbol{X}_{i}\right)_{i=1}^{n}$ by minimizing the square loss

$$
\frac{1}{n} \sum_{i=1}^{n}\left(\widehat{\mu}\left(\boldsymbol{X}_{i}\right)-\widehat{\mu}^{\mathrm{RF}}\left(\boldsymbol{X}_{i}\right)\right)^{2}
$$

If we find an accurate random forest regression model $\widehat{\mu}^{\mathrm{RF}} \approx \widehat{\mu}$, we can use this random forest as a surrogate model for analyzing variable importance. This random forest is an ensemble over multiple regression trees $\left(\widehat{\mu}^{(\star j)}\right)_{j=1}^{M}$, see (6.7), and we can analyze all the SBS that lead to these regression trees $\left(\widehat{\mu}^{(\star j)}\right)_{j=1}^{M}$. Each SBS can be allocated to a covariate component $X_{k}, 1 \leq k \leq q$, and aggregating the decreases of losses (6.6) for each component $1 \leq k \leq q$, gives us a measure of variable importance.

In summary, due computational costs and missing competitiveness, regression trees and random forests do not belong to the regression techniques that are frequently used. An important point is that regression trees applied differently, as weak learners in GBMs, will equip us with some of the most competitive predictive models on tabular data, see Chapter 7, below.

## Page 111
# Chapter 7 

## Gradient boosting machines

This chapter presents boosting and, in particular, gradient boosting machines (GBMs). GBMs belong to the most powerful machine learning methods on tabular data, often outperforming the FNN architectures studied in Chapter 5. The concept of boosting has already been mentioned in Section 5.6, where we boosted a GLM with FNN features. Before going into the theory of GBMs, we take a look at the idea of using (additive) iterative updating, i.e., boosting, we then study GBMs, and in the last part of this chapter we discuss XGBoost and LightGBM which are the state-of-the-art GBMs these days.

### 7.1 (Generalized additive) boosting

The idea of boosting is to use an iterative updating scheme to approximate the unknown true regression function $\boldsymbol{X} \mapsto \mu^{*}(\boldsymbol{X})$ introduced in (1.2). For this iterative scheme of deriving an approximation $\widehat{\mu}$ to $\mu^{*}$, one typically uses simple functions or so-called base learners. This makes boosting very closely connected to additive modeling. In agreement with Chapter 3, we adapt our boosting schemes to GLMs by trying to learn a regression function $\widehat{\mu}(\boldsymbol{X})$ on its transformed scale $g(\widehat{\mu}(\boldsymbol{X}))$, for a given link function $g$, see (3.1). The notation will become a bit cumbersome, but it will be more directly related to GLMs and FNNs.
Let $\mathcal{B}=\{\boldsymbol{X} \mapsto b(\boldsymbol{X} ; \vartheta)\}_{\vartheta}$ define a class of base learners being parametrised by $\vartheta$; concerning the parameter notation we refer to the footnote on page 16. Based on the learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)_{i=1}^{n}$, the boosting update in iteration $j \geq 1$ is described according to

$$
\widehat{\vartheta}^{(j)}=\underset{\vartheta}{\arg \min } \sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, g^{-1}\left(g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)+b\left(\boldsymbol{X}_{i} ; \vartheta\right)\right)\right)
$$

subject to existence and uniqueness. This gives us the updated regression function estimate

$$
\widehat{\mu}^{(j)}(\boldsymbol{X})=g^{-1}\left(g\left(\widehat{\mu}^{(j-1)}(\boldsymbol{X})\right)+b\left(\boldsymbol{X} ; \widehat{\vartheta}^{(j)}\right)\right)=g^{-1}\left(\sum_{s=0}^{j} b\left(\boldsymbol{X} ; \widehat{\vartheta}^{(s)}\right)\right)
$$

## Page 112
where we set for the initialization $b\left(\boldsymbol{X} ; \widehat{\vartheta}^{(0)}\right)$ the homogeneous MLE given by $b\left(\boldsymbol{X} ; \widehat{\vartheta}^{(0)}\right) \equiv$ $g\left(\widehat{\mu}_{0}\right)=g\left(\sum_{i=1}^{n} v_{i} Y_{i} / \sum_{i=1}^{n} v_{i}\right)$.
Note that (7.1) is a natural generalization of the one-step boosting described in Section 5.6 , see formula (5.22). The only difference is that in this former chapter we use very specific base learners. Moreover, (7.2) stresses the close connection to additive modeling, where the update in iteration $j$ is based on trying to capture the remaining signal after having adjusted the intercept according to

$$
g\left(\widehat{\mu}^{(j-1)}(\boldsymbol{X})\right)=\sum_{s=0}^{j-1} b\left(\boldsymbol{X} ; \widehat{\vartheta}^{(s)}\right)
$$

This can be reinterpreted by noting that the base learner $b\left(\boldsymbol{X} ; \widehat{\vartheta}^{(j)}\right)$ tries to find the weaknesses of the previous regression model $\widehat{\mu}^{(j-1)}(\boldsymbol{X})$. This is rather different from ensembling as described in Section 5.4.

The pseudo algorithm for (generalized) additive boosting is given in Algorithm 1, and is sometimes also referred to as stagewise additive boosting, see, e.g., Hastie et al. [93, Algorithm 10.2].

Algorithm 1 Generalized additive boosting

# Initialize. 

- Set the initial mean estimate to the global empirical mean $\widehat{\mu}^{(0)}(\boldsymbol{X})=\widehat{\mu}_{0}$.
- Select the maximum number of boosting iterations $j_{\max } \geq 1$.


## Iterate.

while $1 \leq j \leq j_{\max }$ do
Update

$$
\widehat{\mu}^{(j)}(\boldsymbol{X})=g^{-1}\left(g\left(\widehat{\mu}^{(j-1)}(\boldsymbol{X})\right)+b\left(\boldsymbol{X} ; \widehat{\vartheta}^{(j)}\right)\right)
$$

where $\widehat{\vartheta}^{(j)}$ is given by $(7.1)$ and increase $j$.
end.
Return.

$$
\widehat{\mu}^{\text {boost }}(\boldsymbol{X}):=\widehat{\mu}^{\left(j_{\max }\right)}(\boldsymbol{X})
$$

Remarks 7.1. - Note that for each boosting step $j$

$$
\sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \widehat{\mu}^{(j)}\left(\boldsymbol{X}_{i}\right)\right) \leq \sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)
$$

This is an in-sample loss improvement (on the learning sample $\mathcal{L}$ ).

- Apart from estimating the base learners' parameters $\widehat{\vartheta}^{(j)}$, one needs to decide on the maximum number of boosting iterations $j_{\max }$. In practice, one picks a large $j_{\max }$

Version March 3, 2025, @AI Tools for Actuaries

## Page 113
and uses early stopping based on cross-validation to decide on an effective number of boosting steps to receive a suitable out-of-sample performance, see Section 5.3.5.

- In boosting it is common to include a learning rate or shrinkage factor $\eta \in(0,1]$, or select a decreasing sequence of positive factors $\eta^{(j)}>0$. One then replaces the updating step in Algorithm 1 by

$$
\widehat{\mu}^{(j)}(\boldsymbol{X})=g^{-1}\left(g\left(\widehat{\mu}^{(j-1)}(\boldsymbol{X})\right)+\eta^{(j)} b\left(\boldsymbol{X} ; \widehat{\vartheta}^{(j)}\right)\right)
$$

The intuition behind this step is to avoid taking too large steps in each iteration of the algorithm.

Example 7.2. Assume that the true data generating mechanism is given by

$$
Y=\mu^{*}(\boldsymbol{X})+\varepsilon, \quad \text { with } \varepsilon \sim \mathcal{N}\left(0, \sigma^{2}\right)
$$

where $\mu^{*}(\boldsymbol{X}) \in \mathbb{R}$ is an unknown mean function, and $\sigma^{2}>0$ is an unknown variance parameter. For simplicity, we set $v_{i} \equiv 1$. Assume furthermore that we have an i.i.d. learning sample $\mathcal{L}=\left(Y_{i}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$ generated from (7.3).
Our goal is to approximate $\mu^{*}(\boldsymbol{X})$ with base learners $b(\boldsymbol{X} ; \vartheta)$ using Algorithm 1 under the square loss and with the identity link choice for $g$. In view of (7.1) this gives us for the loss in iteration $j$, we drop $\varphi=\sigma^{2}$ in the following identities,

$$
\begin{aligned}
\sum_{i=1}^{n} L\left(Y_{i}, g^{-1}\left(g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)+b\left(\boldsymbol{X}_{i} ; \vartheta\right)\right)\right) & =\sum_{i=1}^{n}\left(Y_{i}-\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)+b\left(\boldsymbol{X}_{i} ; \vartheta\right)\right)\right)^{2} \\
& =\sum_{i=1}^{n}\left(\tilde{\varepsilon}_{i}^{(j)}-b\left(\boldsymbol{X}_{i} ; \vartheta\right)\right)^{2}
\end{aligned}
$$

where we set

$$
\tilde{\varepsilon}_{i}^{(j)}=Y_{i}-\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)
$$

Thus, the base learners $b\left(\boldsymbol{X}_{i} ; \vartheta\right)$ try to exploit the present residuals $\tilde{\varepsilon}_{i}^{(j)}$ to find the next optimal parameter $\widehat{\vartheta}^{(j)}$. This is analogous to (5.19).

The boosting procedure described in Example 7.2 is also known as matching pursuit; see, e.g., Mallat-Zhang [148]. Matching pursuit was introduced in the signal processing literature. Typically, it focuses on the square loss which is most suitable for Gaussian responses, see Table 2.2. The situation in Example 7.2 is discussed in detail in Bühlmann [37], when using low depth and low interaction regression trees based on the square loss in (6.3), and this reference also includes results on convergence. The Gaussian assumption used in Example 7.2 is a special case of Tweedie's family, see Table 2.3, and it is possible to obtain similar iterative boosting schemes for Tweedie's family under the log-link choice. This is known as response boosting; see Hainaut et al. [90]. It is, however, important to note that when using a general Tweedie's deviance loss with trees as base learners, one should, of course, also optimize the regression trees in (6.3) w.r.t. that Tweedie's deviance loss.

## Page 114
# 7.2 Gradient boosting machines 

In Section 7.1, boosting was introduced as an iterative updating procedure, successively improving the fit of (and the complexity in) the approximation of $\mu(\boldsymbol{X})$ using base learners $\{b(\boldsymbol{X} ; \vartheta)\}_{\vartheta}$. This was done by using successive updates in the mean model under a link transformation, see (7.2). A different route forward is to consider learning an unknown function using functional gradient descent. We discuss this in the present section.

### 7.2.1 Functional gradient boosting

We take this introduction to functional gradient descent in different steps. We start with a single instance $i$, and we fit a one-dimensional real-valued parameter $\vartheta \in \mathbb{R}$ to the observation $Y_{i}$, providing a mean estimate $\mu=g^{-1}(\vartheta)$ for $Y_{i}$. That is, for the moment, we let the (generic) parameter $\vartheta$ play the role of the link transformed mean $g(\mu)$ of $Y_{i}$. In order to ease the notation of this exposition, we define

$$
v_{i} L^{g}\left(Y_{i}, \vartheta\right)=\frac{v_{i}}{\varphi} L\left(Y_{i}, g^{-1}(\vartheta)\right)
$$

for the selected link function $g$ and a strictly consistent loss function $L$ for mean estimation. Moreover, assume that the derivative of $v_{i} L^{g}\left(Y_{i}, \vartheta\right)$ w.r.t. $\vartheta$ exists, and we denote it by $v_{i} \nabla_{\vartheta} L^{g}\left(Y_{i}, \vartheta\right)$.
Using the standard gradient descent method, see (5.12), we aim at finding an optimal parameter $\widehat{\vartheta}$. The standard gradient descent step at algorithmic time $j$ reads as

$$
\widehat{\vartheta}^{(j)}=\widehat{\vartheta}^{(j-1)}-\eta^{(j)} v_{i} \nabla_{\vartheta} L^{g}\left(Y_{i}, \widehat{\vartheta}^{(j-1)}\right)
$$

for learning rate $\eta^{(j)}>0$. By choosing a sufficiently small learning rate $\eta^{(j)}>0$, it is possible to ascertain a loss improvement (unless the gradient in (7.5) is zero)

$$
L^{g}\left(Y_{i}, \widehat{\vartheta}^{(j)}\right) \leq L^{g}\left(Y_{i}, \widehat{\vartheta}^{(j-1)}\right)
$$

One option to select the learning rate $\eta^{(j)}>0$ is to use so-called full relaxation, which corresponds to doing a line search according to

$$
\widehat{\eta}^{(j)}=\underset{\eta>0}{\arg \min } L^{g}\left(Y_{i}, \widehat{\vartheta}^{(j-1)}-\eta v_{i} \nabla_{\vartheta} L^{g}\left(Y_{i}, \widehat{\vartheta}^{(j-1)}\right)\right)
$$

compare with (7.1). For more on this, including conditions for convergence and convergence rates; see Nesterov [166].
The procedure for learning an unknown parameter compared to learning an unknown function can be approached similarly, which is the intuition behind GBMs. Again consider a single instance $i$ with observation $\left(Y_{i}, \boldsymbol{X}_{i}, v_{i}\right)$. By using abbreviation (7.4), we obtain

$$
\frac{v_{i}}{\varphi} L\left(Y_{i}, \mu\left(\boldsymbol{X}_{i}\right)\right)=v_{i} L^{g}\left(Y_{i}, g(\mu(\boldsymbol{X}))\right)
$$

By differentiating the right-hand side w.r.t. $\vartheta=g\left(\mu\left(\boldsymbol{X}_{i}\right)\right)$ allows us to rewrite the standard gradient descent step (7.5) according to

$$
g\left(\widehat{\mu}^{(j)}\left(\boldsymbol{X}_{i}\right)\right)=g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)-\eta^{(j)} v_{i} \nabla_{\vartheta} L^{g}\left(Y_{i}, g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)\right)
$$

## Page 115
or, equivalently, by bringing the link $g$ to the other side

$$
\widehat{\mu}^{(j)}\left(\boldsymbol{X}_{i}\right)=g^{-1}\left(g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)-\eta^{(j)} v_{i} \nabla_{\vartheta} L^{g}\left(Y_{i}, g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)\right)\right)
$$

If we apply this iteration (7.7) for each instance $1 \leq i \leq n$, it will converge (under suitable learning rates) to a saturated model. Naturally, this provides an in-sample over-fitted model as each instance $i$ receives its individual mean parameter estimate.
Instead, the crucial step is to approximate the gradients $v_{i} \nabla_{\vartheta} L^{g}\left(Y_{i}, g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)\right)$ by base learners that are simple functions (low-dimensional objects), such as trees. This implies that the problem becomes regularized, and with a reduced the dimension of the problem.
Define, in iteration $j \geq 1$, the working responses for $1 \leq i \leq n$ by

$$
r_{i}^{(j)}=-v_{i} \nabla_{\vartheta} L^{g}\left(Y_{i}, g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)\right)
$$

For GBMs, one fits a base learner from the parametrized class $\mathcal{B}=\{\boldsymbol{X} \mapsto b(\boldsymbol{X} ; \vartheta)\}_{\vartheta}$ to the new learning sample $\mathcal{L}^{(j)}=\left(r_{i}^{(j)}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$. Since this is a regularization step, and since the idea is that the base learners should iteratively learn a gradient approximation, this suggests to use the square loss for this approximation step

$$
\widehat{\vartheta}^{(j)}=\underset{\vartheta}{\arg \min } \sum_{i=1}^{n}\left(r_{i}^{(j)}-b\left(\boldsymbol{X}_{i} ; \vartheta\right)\right)^{2}
$$

This implies that (the saturated) standard gradient descent iteration (7.7) is replaced by its regularized gradient approximated version, called GBM step,

$$
\widehat{\mu}^{(j)}\left(\boldsymbol{X}_{i}\right)=g^{-1}\left(g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)+\eta^{(j)} b\left(\boldsymbol{X}_{i} ; \widehat{\vartheta}^{(j)}\right)\right)
$$

Here, one can note the close resemblance between (7.10) and the updating step in the generalized additive boosting of Algorithm 1. In order to make the connection to generalized additive boosting even stronger, note that the full relaxation corresponds to doing a full line search w.r.t. $\eta^{(j)}$ in analogy to (7.6). That is, solve

$$
\widehat{\eta}^{(j)}=\underset{\eta>0}{\arg \min } \sum_{i=1}^{n} v_{i} L\left(Y_{i}, g^{-1}\left(g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)+\eta b\left(\boldsymbol{X}_{i} ; \widehat{\vartheta}^{(j)}\right)\right)\right)
$$

By iterating over (7.8)-(7.11), in analogy with the generalized additive boosting algorithm, see Algorithm 1, we obtain the general GBM procedure from Friedman [70]. This algorithm is summarized in Algorithm 2.

Remarks 7.3. - It is common to add yet another learning rate to Algorithm 2, the intuition again being that small steps are less harmful than taking too large ones; by taking too small steps one can always "catch up" in the coming iterations by taking a number of smaller similar steps.

- Note that depending on which software implementation that one is using, the loss function may or may not include a pre-defined link function.

## Page 116
# Algorithm 2 General gradient boosting machine 

## Initialize.

- Set the initial mean estimate to the global empirical mean $\widehat{\mu}^{(0)}(\boldsymbol{X})=\widehat{\mu}_{0}$.
- Select the maximum number of boosting iterations $j_{\max } \geq 1$.


## Iterate.

while $1 \leq j \leq j_{\max }$ do

1. Calculate the working responses $r_{i}^{(j)}$ from (7.8).
2. Fit a base learner from $\{b(\boldsymbol{X} ; \vartheta)\}_{\vartheta}$ to the working responses according to (7.9).
3. Calculate the optimal step length $\widehat{\eta}^{(j)}$ according to (7.11).
4. Update

$$
\widehat{\mu}^{(j)}(\boldsymbol{X})=g^{-1}\left(g\left(\widehat{\mu}^{(j-1)}(\boldsymbol{X})\right)+\widehat{\eta}^{(j)} b\left(\boldsymbol{X} ; \widehat{\vartheta}^{(j)}\right)\right)
$$

and increase $j$.
end.
Return.

$$
\widehat{\mu}^{\mathrm{GBM}}(\boldsymbol{X}):=\widehat{\mu}^{\left(j_{\max }\right)}(\boldsymbol{X})
$$

- In Algorithm 2, the weights $v_{i}>0$ are included, and depending on the software implementation, one needs to ensure to make proper use of the weights, intercepts and offsets, respectively.
- The general GBM described in Algorithm 2 shares the same problems as generalized additive boosting w.r.t. potential over-fitting, and one should again use early stopping based on cross-validation, or a similar technique, to prevent over-fitting.
- The general GBM of Algorithm 2 is closely connected to additive gradient based boosting, such as GAM-boost, being based on generalized additive models (GAMs), see, e.g., the gamboost class in the R package mboost [101].
- Consistency and convergence properties for GBMs tend to become technical. Such type of results can be found in Zhang-Yu [248], where the GBM from Algorithm 2 appears as a special case of a more general greedy boosting algorithm.

The close connections between additive boosting and general GBMs have already been established above, and to stress this further we continue Example 7.2:

Example 7.4. We revisit the set-up of Example 7.2. Calculating the working responses according to (7.8) for the square loss we get

$$
r_{i}^{(j)}=-\nabla_{\vartheta} L\left(Y_{i}, \widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)=2\left(Y_{i}-\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right) \propto Y_{i}-\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)
$$

## Page 117
where constants not depending on $i$ have been dropped; in this example we assumed $v_{i} \equiv 1$. Fitting a base learner $b(\boldsymbol{X} ; \vartheta)$ to the new learning sample $\mathcal{L}^{(j)}=\left(r_{i}^{(j)}, \boldsymbol{X}_{i}\right)_{i=1}^{n}$ using the square loss is equivalent to minimize the following expression in $\vartheta$, see (7.9),

$$
\begin{aligned}
\sum_{i=1}^{n}\left(r_{i}^{(j)}-b\left(\boldsymbol{X}_{i} ; \vartheta\right)\right)^{2} & =\sum_{i=1}^{n}\left(Y_{i}-\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)-b\left(\boldsymbol{X}_{i} ; \vartheta\right)\right)^{2} \\
& =\sum_{i=1}^{n}\left(Y_{i}-\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)+b\left(\boldsymbol{X}_{i} ; \vartheta\right)\right)\right)^{2}
\end{aligned}
$$

The latter expression is equivalent to additive boosting (7.1) under the square loss function choice and for the identity link for $g$.

# 7.2.2 Tree-based gradient boosting machines 

Up until now, we have not been discussing any particular choices of the base learners $\mathcal{B}=\{\boldsymbol{X} \mapsto b(\boldsymbol{X} ; \vartheta)\}_{\vartheta}$. The most popular class $\mathcal{B}$ of base learners are low depth and low interaction regression trees of a fixed cardinality. They are simple to implement, easy and fast to compute and have an excellent predictive performance in GBMs.
Recall the notation from Chapter 6. This chapter introduced a finite partition of the covariate space $\mathcal{X}=\sum_{t \in \mathrm{~T}} \mathcal{X}_{t}$, with a finite index set T of cardinality $|\mathrm{T}|$. Low depth and low interaction regression trees have a small cardinality $|\mathrm{T}|$, i.e., they only consider a few binary splits. Using a fixed small cardinality $|\mathrm{T}|$, we select the class $\mathcal{B}$ of regression tree base learners by, see (6.2),

$$
b(\boldsymbol{X} ; \vartheta)=\sum_{t \in \mathrm{~T}} m_{t} \mathbb{1}_{\left\{\boldsymbol{X} \in \mathcal{X}_{t}\right\}}
$$

where parameter $\vartheta$ collects the full description of the characterization of the binary regression tree (7.12). We insert this class $\mathcal{B}$ of fixed small cardinality $|\mathrm{T}|$ regression trees as base learners in Algorithm 2.
Reconsidering the line search (7.11) for the optimal selection of the learning rate $\eta^{(j)}>0$ in the $j$-th iteration of Algorithm 2. This line search (7.11) can be replaced by directly updating the piecewise constant estimates $\left(m_{t}\right)_{t \in \mathrm{~T}}$ on every leaf. That is, for all $t \in \mathrm{~T}$

$$
\widehat{m}_{t}^{(j)}=\underset{m \in \mathbb{R}}{\arg \min } \sum_{i: \boldsymbol{X}_{i} \in \widehat{\mathcal{X}}_{t}^{(j)}} v_{i} L^{g}\left(Y_{i}, g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)+m\right)
$$

This minimization relies on first having fitted a regression tree to the working responses to obtain the covariate space partition $\left(\widehat{\mathcal{X}}_{t}^{(j)}\right)_{t \in \mathrm{~T}}$ of the covariate space $\mathcal{X}$, see (7.9).
This results in the tree-based gradient boosting predictor in the $j$-th iteration

$$
\widehat{\mu}^{(j)}(\boldsymbol{X})=g^{-1}\left(g\left(\widehat{\mu}^{(j-1)}(\boldsymbol{X})\right)+\sum_{t \in \mathrm{~T}} \widehat{m}_{t}^{(j)} \mathbb{1}_{\left\{\boldsymbol{X} \in \widehat{\mathcal{X}}_{t}^{(j)}\right\}}\right)
$$

As mentioned above, tree-based GBMs have become very popular and can be found in off-the-shelf software, such as the gbm package in R. When using one of these packages, one always needs to carefully check what link functions $g$ are implemented and how

## Page 118
the algorithm deals with the weights $v_{i}$; we also refer to Remark 2.3. The tree-based GBM procedure is summarized in Algorithm 3, which corresponds to the regression tree boosting described in Friedman [70].

# Algorithm 3 Tree-based gradient boosting machine 

## Initialize.

- Set the initial mean estimate to the global empirical mean $\widehat{\mu}^{(0)}(\boldsymbol{X})=\widehat{\mu}_{0}$.
- Select the maximum number of boosting iterations $j_{\max } \geq 1$.
- Fix the cardinality $|\mathrm{T}|$ of the regression tree base learners.


## Iterate.

while $1 \leq j \leq j_{\max }$ do

1. Calculate the working responses $r_{i}^{(j)}$ from (7.8).
2. Fit a regression tree (7.12) of cardinality $|\mathrm{T}|$ to the working responses using the greedy minimization of (7.9).
3. Perform optimal leaf adjustments according to (7.13).
4. Update

$$
\widehat{\mu}^{(j)}(\boldsymbol{X})=g^{-1}\left(g\left(\widehat{\mu}^{(j-1)}(\boldsymbol{X})\right)+\sum_{t \in \mathrm{~T}} \widehat{m}_{t}^{(j)} \mathbb{1}_{\left\{\boldsymbol{X} \in \widehat{X}_{t}^{(j)}\right\}}\right)
$$

and increase $j$.
end.
Return.

$$
\widehat{\mu}^{\text {tree-GBM }}(\boldsymbol{X}):=\widehat{\mu}^{\left(j_{\max }\right)}(\boldsymbol{X})
$$

Remarks 7.5. - In (7.14) and in Algorithm 3 it is common to add yet another learning rate (shrinkage factor) in the update step.

- Note that compared with tree-based additive boosting, a tree-based GBM only makes use of square loss fitted trees, irrespective of the underlying data generating process motivating the use of the loss $L(Y, \mu)$. This makes the tree-based GBMs easy to apply to custom distributions. Furthermore, it is neither a problem to use count data responses or binary responses (classification). For general binary treefitting, see, e.g., the discussion concerning (6.3) above, and Hainaut et al. [90] on response boosting.
- In many applications, so-called tree stumps are used as base learners; tree stumps consider one single split and have $|\mathrm{T}|=2$ leaves. We suggest to consider bigger trees, because bigger trees promote interaction modeling. With tree stumps and

## Page 119
the log-link choice for $g$, the GBM results in a multiplicative model; see WüthrichBuser [241, Example 7.5].

# 7.3 Interpretability measures and variable importance 

The question of interpreting model output is an important and active field of research to which Chapter [insert] is devoted. That chapter presents model-agnostic tools that do not depend on a certain type of regression model, in this section we present a tree-based interpretability tool. As we have seen in Chapter 6, a single regression (or classification) tree is in itself explainable and interpretable. As we know, however, large trees tend to become unstable, whereas we have argued that (generalized additive) boosted tree models, making use of low-cardinality trees as base learners, tend to have an excellent predictive performance. But, when constructing a predictor by adding many small trees, the interpretability of the resulting predictor gets lost.

A simple and very popular interpretability measure based on trees was introduced in Breiman et al. [31]. It also generalizes to (generalized) additive tree models. It is called variable importance score (VI-score). The idea is simple and can be formalized as follows. Let $S(k ; \mathrm{T})$ denote which of the $q$ covariate components $\left(X_{l}\right)_{l=1}^{q}$ is used in split $k$ in the tree T , thus, $S(k ; \mathrm{T}) \in\{1, \ldots, q\}$. That is, if we have a tree of cardinality $|\mathrm{T}|$, this means that there are in total $|\mathrm{T}|-1$ splits in the tree T . The VI-score for covariate component $1 \leq l \leq q$ w.r.t. the tree T is given by

$$
\mathrm{VI}_{l}(\mathrm{~T})=\sum_{k=1}^{|\mathrm{T}|-1} \widehat{i}_{k}(\mathrm{~T})^{2} \mathbb{1}_{\{S(k ; \mathrm{T})=l\}}
$$

where $\widehat{i}_{k}(\mathrm{~T})^{2}$ corresponds to the loss improvement in the $k$-th split in T , i.e., this is obtained by evaluating the objective function of (6.3) in the selected split. Consequently, if we are using a method which is based on $j_{\max }$ additively boosted trees, $\mathrm{T}_{j}, 1 \leq j \leq j_{\max }$, this suggests to consider the average VI-score for covariate component $1 \leq l \leq q$ given by

$$
\mathrm{VI}_{l}=\frac{1}{j_{\max }} \sum_{j=1}^{j_{\max }} \mathrm{VI}_{l}\left(\mathrm{~T}_{j}\right)
$$

For more on VI-scores and other tree-based methods, see, e.g., Hastie et al. [93, Chapter 10.13], and the references therein.

Remarks 7.6. - Note that the VI-scores from (7.15) and (7.16) will naturally weigh the importance of covariate components that occur rarely in splits but have large loss reductions and covariate components that often occur in splits, but with low loss reductions.

- In practice these VI-scores are often normalized to sum to one.
- When using these VI-scores in GBMs it is typically the case that the importance is measured on the tree scale, hence, focusing on the loss improvement w.r.t. the

## Page 120
gradient approximations, not w.r.t. the (empirical) loss given by a deviance loss function.

# 7.4 State-of-the-art gradient boosting machines 

In the previous sections the basic ideas underpinning (generalized additive) boosting and gradient boosting, with an extra focus on the situation when using low-cardinality trees as base learners, was presented. These base learners are the most commonly used ones in practice.

When it comes to practical considerations, we have already discussed adding additional shrinkage factors, in order to avoid taking too large boosting steps, see, e.g., Remark 7.5. Another consideration, both improving speed and robustness, is to limit the number of data points used in each iteration by using sub-sampling techniques, i.e., bagging.

Another consideration when it comes to speed, as already commented on in Chapter 6.1, trees are theoretically able to handle high-cardinality nominal categorical covariates, but in practice, when greedily searching for optimal binary splits, this may become problematic w.r.t. computational time. In the standard tree-based GBM implemented in the R package gbm [194], this is partly alleviated by pre-sorting the covariate components when searching for (greedy) optimal splits.

LightGBM. A popular high-speed version of GBMs targeting the issue of the highcardinality nominal categorical covariates is LightGBM by Ke et al. [116]. The idea behind LightGBM is to (i) focus on data instances with large gradients, and (ii) to exploit sparsity in the covariate space. Step (i) is what is referred to as gradient-based one sided sampling (GOSS) and is an alternative to uniform sampling in bagging, and step (ii) is what is called exclusive feature bundling (EFB), which is a type of histogram procedure combining both covariate (feature) selection and merging of covariates (features). The intuition behind the merging of covariates is that covariates whose one-hot encoded categories are not jointly active can be merged, which is likely to happen if the covariate space is large. For more details, see Ke et al. [116]. The LightGBM method has been proved to be both fast and accurate.

XGBoost. Another popular fast gradient based boosting procedure is XGBoost, see Chen-Guestrin [41]. It is based on a functional second order approximation of the loss function. In terms of the previously used notation for a single instance $i$, this can be

## Page 121
expressed as the following second order Taylor expansion

$$
\begin{aligned}
& L^{g}\left(Y_{i}, g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)+b\left(\boldsymbol{X}_{i} ; \vartheta\right)\right) \\
& \approx L^{g}\left(Y_{i}, g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)\right)+\nabla_{\vartheta} L^{g}\left(Y_{i}, g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)\right) b\left(\boldsymbol{X}_{i} ; \vartheta\right) \\
& +\frac{1}{2} \nabla_{\vartheta}^{2} L^{g}\left(Y_{i}, g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)\right) b\left(\boldsymbol{X}_{i} ; \vartheta\right)^{2} \\
& \propto \nabla_{\vartheta} L^{g}\left(Y_{i}, g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)\right) b\left(\boldsymbol{X}_{i} ; \vartheta\right)+\frac{1}{2} \nabla_{\vartheta}^{2} L^{g}\left(Y_{i}, g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right)\right)\right) b\left(\boldsymbol{X}_{i} ; \vartheta\right)^{2} \\
& =: L_{\mathrm{XGB}}^{g}\left(Y_{i}, g\left(\widehat{\mu}^{(j-1)}\left(\boldsymbol{X}_{i}\right) ; b\left(\boldsymbol{X}_{i} ; \vartheta\right)\right)\right)
\end{aligned}
$$

where $\nabla_{\vartheta}^{2}$ denotes the second derivative (Hessian) w.r.t. $\vartheta$. Consequently, even though derivatives appear in $L_{\mathrm{XGB}}^{g}(\cdot)$ from (7.17), they do not appear in the same way as in the GBMs described by Algorithms 2 and 3. In fact, this second order Taylor expansion (7.17) is related to a Newton step and the working residuals are suitably scaled by their Hessians before being approximated by the base learners. Thus, effectively, (7.9) is replaced by a Hessian scaled and weighted version. Furthermore, by using low-cardinality trees as base learners applied to $L_{\mathrm{XGB}}^{g}(\cdot)$ from (7.17), the leaf values for a given part in the partition is given explicitly, and the criterion for finding the greedy optimal split point is given explicitly. Thus, by using the approximate loss $L_{\mathrm{XGB}}^{g}(\cdot)$ from (7.17) combined with trees makes it possible to skip (costly) line searches. Note that this also will result in a different type of trees than standard trees that are grown recursively leaf-wise, for more details; see Chen-Guestrin [41]. XGBoost also allows for regularization by using a penalized deviance loss (log-likelihood), and it can be equipped with histogram-based techniques handling high-cardinality nominal categorical covariates. For more details, see Chen-Guestrin [41].

Multi-parametric losses and further extensions. Above the loss functions considered have all been effectively one-dimensional, trying to learn an unknown regresssion function $\boldsymbol{X} \mapsto \mu(\boldsymbol{X}) \in \mathbb{R}$; in the presence of a nuisance parameter $\varphi \in \mathbb{R}_{+}$referred to as a dispersion parameter. The above discussed boosting techniques can be naturally extended to the situation with a functional dispersion $\varphi(\boldsymbol{X})$, or more generally, when the loss function is expressed in terms of a $p$-dimensional real-valued argument $\boldsymbol{\vartheta} \in \mathbb{R}^{p}$, and we want to learn an unknown $p$-dimensional function $\boldsymbol{X} \mapsto \boldsymbol{\vartheta}(\boldsymbol{X})$; we use boldface notation in $\boldsymbol{\vartheta}$ to emphasize that this is a multi-dimensional object. This situation is similar to considering a multi-task (and multi-output) FNN, see Remarks 5.2. Examples of methods addressing this situation are, e.g., gamboostLSS, see Mayr et al. [149], NGBoost, see Duan et al. [59], Cyclic GBMs (CGBMs), see Delong et al. [50]. Both gamboostLSS and CGBMs use cyclic updating over the $p$ parameter dimensions of $\boldsymbol{\vartheta}$. In addition gamboostLSS allows for component-wise optimization, which means that one may specify covariate specific base learners. NGBoost uses so-called natural gradients, which aims for improving speed and stability.

## Page 122
Version March 3, 2025, @AI Tools for Actuaries

## Page 123
# Chapter 8 

## Deep learning for tensor and unstructured data

### 8.1 Introduction

This chapter builds on the feed-forward neural network (FNN) architecture that was introduced in Chapter 5. The FNN architecture can be seen as a prototype of more sophisticated deep learning architectures, with the recurrent goal of an optimal feature extraction for predictive modeling. The FNNs discussed in Chapter 5 act on so-called tabular input data, which means that one has a $q$-dimensional cross-section $\boldsymbol{X}_{i, t} \in \mathbb{R}^{q}$ of (structured) real-valued input data over all instances $1 \leq i \leq n$ at a given time point $t$. It is useful to interpret $t$ as discrete time. More generally, it is just a positional index. This structured data has the format of $q$-dimensional real-valued vectors, and it is called tabular because we can collect the cross-sectional input data $\left(\boldsymbol{X}_{i, t}\right)_{i=1}^{n}$ at a given time point $t$ in a table $\mathfrak{X}_{t}$, resulting in the design matrix at time $t$

$$
\mathfrak{X}_{t}=\left[\boldsymbol{X}_{1, t}, \ldots, \boldsymbol{X}_{n, t}\right]^{\top}=\left(\begin{array}{ccc}
X_{1, t, 1} & \cdots & X_{1, t, q} \\
\vdots & \ddots & \vdots \\
X_{n, t, 1} & \cdots & X_{n, t, q}
\end{array}\right) \in \mathbb{R}^{n \times q}
$$

Compared to (2.10), we drop the intercept (bias) component. This describes the covariate information at time $t$ for predicting the responses $\left(Y_{i, t}\right)_{i=1}^{n}$.

Naturally, this allows for a time-series extension, called panel data or longitudinal data. If one has only one instance, one typically drops the instance index $i$, and in that case one speaks about time-series data. The time-series data of a given instance comprises responses, covariates and volumes, respectively, given by

$$
\begin{aligned}
Y_{1: t} & =\left(Y_{1}, \ldots, Y_{t}\right)^{\top} \in \mathbb{R}^{t} \\
\boldsymbol{X}_{1: t} & =\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{t}\right)^{\top} \in \mathbb{R}^{t \times q} \\
v_{1: t} & =\left(v_{1}, \ldots, v_{t}\right)^{\top} \in \mathbb{R}^{t}
\end{aligned}
$$

We do not use boldface notation in $Y_{1: t}$ and $v_{1: t}$ to highlight that these are time-series of one-dimensional variables.

## Page 124
We can illustrate this data by mapping the time to the vertical axis

$$
Y_{1: t}=\left(\begin{array}{c}
Y_{1} \\
\vdots \\
Y_{t}
\end{array}\right), \quad \boldsymbol{X}_{1: t}=\left(\begin{array}{ccc}
X_{1,1} & \cdots & X_{1, q} \\
\vdots & \ddots & \vdots \\
X_{t, 1} & \cdots & X_{t, q}
\end{array}\right) \quad \text { and } \quad v_{1: t}=\left(\begin{array}{c}
v_{1} \\
\vdots \\
v_{t}
\end{array}\right)
$$

A major change is that the input vector of a given instance at time $t, \boldsymbol{X}_{t} \in \mathbb{R}^{q}$, is replaced by an input tensor of order 2 (called $2 D$ tensor), given by $\boldsymbol{X}_{1: t} \in \mathbb{R}^{t \times q}$ and describing the entire historical input data. 2D tensors are matrices, but, more generally, tensors can have any integer order. The 2 D tensor $\boldsymbol{X}_{1: t}$ has a time-causal structure, i.e., the adjacency in time index $t$ has a specific meaning, and the main question is how to design network architectures that respect (benefit from) this adjacency. Naturally, classical FNN architectures that are designed for input vectors, and not time-series data, do not respect time-causality.
This tensor approach can be made fully general, i.e., it can be extended from 2D tensors for time-series data to tensors of any order. We give an example of a 3D tensor having a spatial structure.

Example 8.1 (RGB color image). An example for a 3D tensor is a color image

$$
\boldsymbol{X}_{1: t, 1: s}=\left(X_{u, v, j}\right)_{1 \leq u \leq t, 1 \leq v \leq s, 1 \leq j \leq 3} \in \mathbb{R}^{t \times s \times 3}
$$

This color image has a spatial structure described by the first two indices $(u, v)$, in fact, in this example we have a rectangle with $t$ pixels on the $x$-axis and $s$ pixels on the $y$-axis. The last index $j$ then labels the three color channels red-green-blue (RGB). This is the typical way of encoding color pictures into a 3D tensor. An example is given in Figure 8.1 for a $30 \times 30$ color picture.

Figure 8.1: RGB channels for a $30 \times 30$ color picture: R channel, G channel, B channel, and overlap of the three channels.

The common approach of using unstructured data such as texts, speech and images in predictive models, is to map such unstructured data to tensors. For images, this is solved as in Example 8.1. For texts and speech, this is achieved by an entity embedding which uses tokenization. That is, we tokenize speech by assigning integers to all words, and then we apply an entity embedding (2.15) to these integers and words, respectively. This turns sentences (and speech) into 2 D tensors of shape $\mathbb{R}^{t \times b}$, with $t$ being the length of the sentence and $b$ the dimension of the entity embedding. We discuss this in careful detail in Section 8.2, below.
![Page 124 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p124_img1.jpg)

## Page 125
# Typical image recognition problems 

Image recognition problems are very different from actuarial problems. A classical image recognition problem is to determine whether there is a cat, $Y=0$, or a dog, $Y=1$, on an image, thus, one tries to determine $Y$ from an RGB image $\boldsymbol{X}_{1: t, 1: s} \in \mathbb{R}^{t \times s \times 3}$. Purposefully we wrote 'determine' to this image recognition task, because this is not a forecast problem. There is no randomness in terms of irreducible risk involved in this cat vs. dog image recognition problem. Therefore, we will not elaborate any further on such image recognition problems, but we will focus on actuarial forecasting problems, below, where the irreducible risk is a significant factor in the prediction task. The techniques though are the same, but we put different emphasis on the different features.

### 8.2 Tokenization and the art of entity embedding

Any (input) data for predictive modeling needs to be in tensor form. This section discusses tokenization of unstructured (text) data that builds the process of mapping unstructured text data to tensors. Remark that we focus on texts and speech, because images can be treated as in Example 8.1.

### 8.2.1 Tensors

The input data to networks (and regression functions) is usually in tensor form. For single instances, the input information is either a single vector $\boldsymbol{X} \in \mathbb{R}^{q}$ (1D tensor), a time-series $\boldsymbol{X}_{1: t} \in \mathbb{R}^{t \times q}$ (2D tensor) or a spatial image $\boldsymbol{X}_{1: t, 1: s} \in \mathbb{R}^{t \times s \times q}$ (3D tensor), where we generally assume that a color image has three color channels expressed by setting $q=3$, see Example 8.1 and Figure 8.1. If we have a black-and-white picture, we typically want to preserve this spatial structure and, therefore, use a 3D tensor with a single gray color channel $\boldsymbol{X}_{1: t, 1: s} \in \mathbb{R}^{t \times s \times 1}$, i.e., we set $q=1$. In this notation, typically, the first indices of the tensor describe a time-series or a spatial structure, and the last index (referring to $q$ ) are the channels.
Having multiple instances $1 \leq i \leq n$ increases the tensors by one order, e.g., for images as covariates, we have an input, $4 D$ design tensor, over all instances

$$
\mathfrak{X}=\left[\boldsymbol{X}_{1,1: t, 1: s}, \ldots, \boldsymbol{X}_{n, 1: t, 1: s}\right] \in \mathbb{R}^{n \times t \times s \times 3}
$$

Assuming independence between the instances then applies to the first index $1 \leq i \leq n$ of this 4 D design tensor $\mathfrak{X}$.

### 8.2.2 (Supervised) entity embedding

Before turning our attention to unsupervised word embedding, we revisit supervised entity embedding which links our discussion to Section 2.3.2. We discussed that it is very common to actuarial problems to have many categorical covariates, and quite some of those may have many levels, i.e., may be high-cardinality categorical; examples are car brands, vehicle models, provinces, job profiles, etc. Dummy or one-hot encoding then

## Page 126
results in high-dimensional input tensors. A similar situation occurs for unstructured text data. The Oxford English Dictionary estimates that there are roughly 170,000 English words in regular use, which results in an input dimension of 170,000 if one uses one-hot encoding for these words. Aiming at making the input data smaller, we revisit entity embedding discussed in (2.15). Select a (small) embedding dimension $b \in \mathbb{N}$, and consider the entity embedding

$$
\boldsymbol{e}^{\mathrm{EE}}: \mathcal{A} \rightarrow \mathbb{R}^{b}, \quad X_{1} \mapsto \boldsymbol{e}^{\mathrm{EE}}\left(X_{1}\right)
$$

where $\mathcal{A}=\left\{a_{1}, \ldots, a_{K}\right\}$ is the set of all levels of a categorical covariate component $X_{1}$ contained in $\boldsymbol{X}$ (for the moment we do not assume that all components of $\boldsymbol{X}$ are real-valued).
This results in $K$ embedding weights $\boldsymbol{e}_{k}^{\mathrm{EE}}:=\boldsymbol{e}^{\mathrm{EE}}\left(a_{k}\right) \in \mathbb{R}^{b}, 1 \leq k \leq K$. In FNN fitting, these embedding weights are part of the network parameter $\vartheta$, and they are learned with SGD that aims at making a strictly consistent loss function (generally) small

$$
L(\vartheta ; \mathcal{L})=\sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right) \stackrel{!}{=} \min
$$

see Section 5.3. Hence, the embedding weights involved in (8.1) are learned in a supervised learning manner using the targets (responses) $\left(Y_{i}\right)_{i=1}^{n}$. Changing the targets will lead to different embeddings. E.g., job profiles impact accident or liability insurance claims differently, and using these two different responses will result in different embeddings of the job profiles. In contrast, we could also try to use an unsupervised learning embedding, which requires that we can put the categorical covariates into some context. This unsupervised learning embedding will be discussed in Section 8.2.3, and it also relates to the clustering methods studied in Section 9, below.
Often, gradient descent fitting does not work well if one has many high-cardinality categorical covariates. High-cardinality categorical covariates give a significant potential for over-fitting, and, as a result, usually gradient descent methods exercise a very early stopping time. In such cases, it is beneficial to regularize the embedding, similarly to Section 2.4. Assume that we have one categorical covariate $X_{i, 1} \in \mathcal{A}$ in $\boldsymbol{X}_{i}$ with $K$ levels. This gives the embedding weights $\left(\boldsymbol{e}_{k}^{\mathrm{EE}}\right)_{k=1}^{K} \subset \mathbb{R}^{b}$; these embedding weights are part of the network weights $\vartheta$. Using ridge regularization (2.22) on these embedding weights, motivates to consider the regularized loss

$$
\sum_{i=1}^{n} \frac{v_{i}}{\varphi} L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)+\frac{\eta}{\varphi} \sum_{k=1}^{K}\left\|\boldsymbol{e}_{k}^{\mathrm{EE}}\right\|_{2}^{2}
$$

for regularization parameter $\eta>0$. There is one point that we want to highlight; this has been discussed in Richman-Wüthrich [192]. The regularized loss (8.2) balances between the sample size $n$ and the number of occurrences of a given categorical level $a_{k} \in \mathcal{A}$. The issue in SGD training is that one does not consider the loss simultaneously over the entire learning sample $\mathcal{L}$, but only over the random (mini-)batch used for the next SGD step, see (5.14). As a result, (8.2) cannot be evaluated in SGD, because we only see one mini-batch at a time. To account for this issue, we change the regularized loss (8.2) into a different form. Taking the notation from Avanzi et al. [7], we define

$$
k[i]=\left\{k \in\{1, \ldots, K\} ; X_{i, 1}=a_{k}\right\}
$$

Version March 3, 2025, @AI Tools for Actuaries

## Page 127
that is, $k[i]$ indicates to which level $a_{k[i]}$ the categorical variable $X_{i, 1}$ of instance $1 \leq i \leq n$ belongs to. We define the totally observed exposure on each level $1 \leq k^{\prime} \leq K$ by

$$
v_{k^{\prime}}^{+}=\sum_{i=1}^{n} v_{i} \mathbb{1}_{\left\{k[i]=k^{\prime}\right\}}=\sum_{i=1}^{n} v_{i} \mathbb{1}_{\left\{X_{i, 1}=a_{k^{\prime}}\right\}}
$$

This allows us to rewrite the regularized loss (8.2) as follows

$$
\frac{1}{\varphi} \sum_{i=1}^{n} v_{i}\left(L\left(Y_{i}, \mu_{\vartheta}\left(\boldsymbol{X}_{i}\right)\right)+\frac{\eta}{v_{k[i]}^{+}}\left\|\boldsymbol{\epsilon}_{k[i]}^{\mathrm{EE}}\right\|_{2}^{2}\right)
$$

The crucial difference of this latter expression to (8.2) is that the regularization is integrated into the round brackets under the $i$-summation. This allows one to apply SGD on partitions (mini-batches) of $\{1, \ldots, n\}$; this requires that one changes the loss function correspondingly in SGD implementations, and that one equips all instances $1 \leq i \leq n$ with the volume information $v_{k[i]}^{+}$so that on every instance $i$ (and batch) one can evaluate both terms under the $i$-summation in (8.3)
We observe from (8.3) that the regularization on individual instances $i$ is inversely proportional to the volumes $v_{k[i]}^{+}$, and more frequent levels $a_{k}$ receive a less strong regularization towards zero compared to scarce ones. This scaling is quite common, and it is a natural consequence of a Bayesian interpretation of this regularization approach; see RichmanWüthrich [192]. This reference also discusses regularized entity embedding in case of hierarchical categorical covariates, e.g., vehicle brand - vehicle model - vehicle details build a natural hierarchy, and a certain Toyota make cannot appear under a Volkswagen brand. This may give further regularization restrictions, e.g., similar to fused regularization, see (2.27), we can bring hierarchies into a context.

# 8.2.3 (Unsupervised) word embedding 

Fitting a model (8.3) gives a supervised (and regularized) entity embedding. When it comes to large unstructured inputs such as texts, this regularized approach may not work. Therefore, in an initial step, one first tries to get an entity embedding in an unsupervised learning manner, which can then be further processed. To arrive at an unsupervised embedding, we need to be able to bring categorical covariates into a context. This is most easily understood in text recognition problems where, e.g., certain verbs only appear in the context of certain nouns and activities. We discuss this in this section and we use texts (sentences) as our basic example.
Compared to the previous section, we change the notation from $k \in\{1, \ldots, K\}$ to $w \in$ $\{1, \ldots, W\}$. The index $k$ has been labeling the levels $a_{k} \in \mathcal{A}=\left\{a_{1}, \ldots, a_{K}\right\}$ of a categorical covariate, in the present section it is more natural to associate $w$ with words in a text recognition context. Assume there are $W \in \mathbb{N}$ words $\left(a_{w}\right)_{w=1}^{W}$ in the entire considered vocabulary $\mathcal{A}$. To make the notation simpler, we tokenize these words $a_{w}$ by their integer indices $1 \leq w \leq W$, that is, the token $w$ corresponds to the word $a_{w}$ in vocabulary $\mathcal{A}$; the ordering is completely irrelevant for our purposes. Thus, the entire vocabulary $\mathcal{A}$ is tokenized by the integers

$$
\mathcal{W}=\{1, \ldots, W\} \subset \mathbb{N} \quad \text { and } \quad \mathcal{W}_{0}=\mathcal{W} \cup\{0\}
$$

## Page 128
where we add a token zero for an empty word. This is going to be useful if we need to bring different sentences to equal length. In machine learning jargon, this is called padding shorter sentences with zeros to equal length.
A sentence consists of different words $a_{w}$ and their tokens $w$, respectively, and the order of the words and tokens matters for the meaning of the sentence. Therefore, we use the positional index $t \in \mathbb{N}$ to indicate the position of a word in a sentence.
A sentence text of length $T$ is given by

$$
\text { text }=\left(w_{1}, \ldots, w_{T}\right) \in \mathcal{W}_{0}^{T}
$$

Remark. We speak about words and sentences or texts. This determines the units of the tokenization, i.e., turning words into tokens. However, there is no restriction in selecting words as units. One can also tokenize parts of speech (bigger units) or syllable and morphemes that make up words (smaller units). The methodology will be completely the same. We present it on the level of words because this is the most intuitive and natural unit to discuss the technology.

# Bag-of-words 

The method of bag-of-words is the most crude one to make a text $=\left(w_{1}, \ldots, w_{T}\right)$ numerical for predictive modeling. It drops the positional index and it defines the bag-of-word mapping

$$
\psi: \mathcal{W}_{0}^{T} \rightarrow \mathbb{N}_{0}^{W}, \quad \text { text } \mapsto \psi(\text { text })=\left(\sum_{t=1}^{T} \mathbb{1}_{\left\{w_{t}=w\right\}}\right)_{w \in \mathcal{W}}
$$

This is called bag-of-words because one places all words into the same bag. As a result, one loses the order and the positional index, and one only counts how often a certain word appears in text. This is very crude because, e.g., the following two sentences provide the same bag-of-words: 'the car is red' and 'is the car red', but their meaning is rather different. That is, the semantics of the sentence gets lost by the bag-of-words embedding (by dropping the positional index). Moreover, the range $\mathbb{N}_{0}^{W}$ of $\psi$ is very high-dimensional, and $\psi$ (text) is likely scarce if the text is small and the vocabulary large. In this approach, one often removes so-called stop words such as 'at', 'to', 'the', etc., to put more emphasis on the more important parts of the sentences and to reduce the dimension of the vocabulary.

## Word embeddings: unsupervised learning

Referring to Bengio et al. [20, 21, 22], we start with an entity embedding of the vocabulary $\mathcal{A}$ and its tokenization $\mathcal{W}_{0}$, respectively. Select an embedding dimension $b \ll W$ and consider the word embedding (WE)

$$
\boldsymbol{e}^{\mathrm{WE}}: \mathcal{W}_{0} \rightarrow \mathbb{R}^{b}, \quad w \mapsto \boldsymbol{e}^{\mathrm{WE}}(w)
$$

that assigns to each token $w$ an embedding vector $\boldsymbol{e}^{\mathrm{WE}}(w)$. In an unsupervised learning manner, one tries to learn the embedding vectors from their contexts. E.g., 'I'm driving by car to the city' and 'I'm driving my vehicle to the town center' uses similar words in a similar context. Therefore, their embedding vectors should be close because they are

## Page 129
almost interchangeable. The goal is to learn such similarity in the meanings from the context in which these words are used. For this, consider a sentence

$$
\text { text }=\left(w_{1}, \ldots, w_{t-1}, w_{t}, w_{t+1}, \ldots, w_{T}\right)
$$

where the positional indices $t \in \mathbb{N}$ become important now.

Question: Can we predict the word $w_{t}$ by knowing that it is sandwiched between $w_{t-1}$ and $w_{t+1}$ ?

Assume we have a collection of different sentences

$$
\mathcal{C}=\left\{\text { text }=\left(w_{1}, \ldots, w_{T}\right)\right\}
$$

to which we can assign positive probabilities

$$
p(\text { text })=p\left(w_{1}, \ldots, w_{T}\right)>0
$$

These probabilities should reflect the frequencies of the sentences text $=\left(w_{1}, \ldots, w_{T}\right)$ in speeches and texts (in the domain we are interested in).
Applying Bayes' rule, we can determine how likely a certain word $w_{t} \in \mathcal{W}_{0}$ occurs in a given sentence text $=\left(w_{1}, \ldots, w_{T}\right)$ at position $t$

$$
p\left(w_{t} \mid w_{1}, \ldots, w_{t-1}, w_{t+1}, \ldots, w_{T}\right)=\frac{p\left(w_{1}, \ldots, w_{T}\right)}{p\left(w_{1}, \ldots, w_{t-1}, w_{t+1}, \ldots, w_{T}\right)}
$$

In general, these probabilities (8.6)-(8.7) are unknown, and they need to be estimated (learned) from a learning sample $\mathcal{L}$. Learning these probabilities will be based on embedding the tokens into low dimensional spaces, and this is precisely the step where the word embedding (8.5) is learned. There are two classic approaches for this: word-tovector (word2vec) by Mikolov et al. [156, 157] and global vectors (GloVe) by Pennington et al. [175] and Chaubard et al. [40]. We describe these two methods next, this description is taken from Wüthrich-Merz [243, Chapter 10].

There are two opposite ways of learning the (conditional) probabilities $p$ :
(i) One can try to predict the center word $w_{t}$ from its context $w_{1}, \ldots, w_{t-1}, w_{t+1}, \ldots, w_{T}$ as described in (8.7). In this approach, to reduce complexity, one often neglects the positional indices of the context words, and one considers the bag-of-words $\left\{w_{s}\right\}_{s \neq t}$ instead. This method is called continuous bag-of-words (CBOW).
(ii) One can revert the problem and try to predict the context from the center word $w_{t}$

$$
p\left(w_{1}, \ldots, w_{t-1}, w_{t+1}, \ldots, w_{T} \mid w_{t}\right)
$$

This is obtained by Bayes's rule from (8.7). This gives the skip-gram approach.

## Page 130
We present word2vec of Mikolov et al. [156, 157] in detail. For this we discuss the two different approaches:
(1) Skip-gram approach of predicting the context from the center word;
(2) CBOW approach of predicting the center word from the context.

Both of these two approaches are computationally intensive:
(3) Negative sampling is a method of coping with the computational complexity in the skip-gram and the CBOW approach.

As a result of these approaches, we receive the word embeddings $\boldsymbol{e}^{\mathrm{WE}}(w)$, because they enter the probabilities (8.7) and (8.8) through a cosine similarity and a softmax implementation.

# Word2vec: skip-gram approach 

For the skip-gram approach one tries to determine the probabilities (8.8) from a learning sample $\mathcal{L}=\left(\right.$ text $\left._{i}\right)_{i=1}^{n}$ of different sentences. Since this problem is too complex in its full generality, one solves a simpler problem.
(1) First, one restricts to a fixed small context (window) size $c \in \mathbb{N}$, and one tries to find the probabilities in this context window of $w_{t}$, given by

$$
p\left(w_{t-c}, \ldots, w_{t-1}, w_{t+1}, \ldots, w_{t+c} \mid w_{t}\right)
$$

(2) Second, one assumes conditional independence of the context words, given the center word $w_{t}$.

Of course, the second assumption is generally not satisfied by real texts, but it significantly simplifies the estimation problem. In particular, this crude (wrong) version is still sufficient to receive a good word embedding (8.5), which is our main incentive to look at this method. Under this conditional independence assumption, we have log-likelihood for learning sample $\mathcal{L}$ and for given context size $c \in \mathbb{N}$

$$
\ell_{\mathcal{L}}=\sum_{i=1}^{n} \sum_{t} \sum_{-c \leq j \leq c, j \neq 0} \log p\left(w_{i, t+j} \mid w_{i, t}\right)
$$

Our goal is to maximize this log-likelihood $\ell_{\mathcal{L}}$ in the conditional probabilities $p(\cdot \mid \cdot)$ to learn the most common context words of a given center word $w_{t}$. If we embed all tokens $w \in \mathcal{W}_{0}$, using a word embedding (8.5), we can learn the embeddings $\boldsymbol{e}^{\mathrm{WE}}(w) \in \mathbb{R}^{b}$ by letting them enter the conditional probabilities $p(\cdot \mid \cdot)$. There is one point though that needs to be considered. We need two different word embeddings $\boldsymbol{e}^{(1)}(w) \in \mathbb{R}^{b}$ and $\boldsymbol{e}^{(2)}(w) \in \mathbb{R}^{b}$ for center and context words, respectively, as these two different usages play different roles in the conditional probabilities in (8.9).

## Page 131
Assume that the conditional probabilities in (8.9) can be modeled by the softmax function

$$
p\left(w_{s} \mid w_{t}\right)=\frac{\exp \left\langle\boldsymbol{e}^{(1)}\left(w_{t}\right), \boldsymbol{e}^{(2)}\left(w_{s}\right)\right\rangle}{\sum_{w=1}^{W} \exp \left\langle\boldsymbol{e}^{(1)}\left(w_{t}\right), \boldsymbol{e}^{(2)}(w)\right\rangle} \in(0,1)
$$

Thus, if the scalar (dot) product between $\boldsymbol{e}^{(1)}\left(w_{t}\right)$ and $\boldsymbol{e}^{(2)}\left(w_{s}\right)$ is large, we get a high probability that $w_{s}$ is in the context of the center word $w_{t} .^{1}$
Inserting (8.10) into (8.9), we receive a log-likelihood function $\ell_{\mathcal{L}}$ in the two word embedding mappings

$$
\boldsymbol{e}^{(1)}: \mathcal{W}_{0} \rightarrow \mathbb{R}^{b} \quad \text { and } \quad \boldsymbol{e}^{(2)}: \mathcal{W}_{0} \rightarrow \mathbb{R}^{b}
$$

Maximizing this log-likelihood $\ell_{\mathcal{L}}$ for the given learning sample $\mathcal{L}$ gives us the two (different) word embeddings. The optimization is done by variants of the SGD algorithm, the only difficulty is that this high-dimensional problem can result in very expensive computations, and negative sampling is a method that can circumvent this problem. We discuss this in the next subsection.

2-dimensional embedding of center word

Figure 8.2: Word2vec skip-gram embedding with embedding dimension $b=2$, obtained by negative sampling; this figure is taken from Wüthrich-Merz [243, Figure 10.2].

Figure 8.2 gives a low-dimensional example with embedding dimension $b=2$. It shows frequent words in claims texts, and the embeddings correspond to the center words $\boldsymbol{e}^{(1)}(w)$ obtained by a word2vec skip-gram approach. The red words show the insured hazards, and we observe that the remaining words cluster around these insured hazards,

[^0]
[^0]:    ${ }^{1}$ This scalar product is related to the cosine similarity between two vectors $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^{b}$ defined by $\langle\boldsymbol{a}, \boldsymbol{b}\rangle /\left(\|\boldsymbol{a}\|_{2}\|\boldsymbol{b}\|_{2}\right)$. This is a popular similarity measure in machine learning; we also refer to Definition 9.2 for the definition of a dissimilarity function.
![Page 131 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p131_img1.jpg)

## Page 132
e.g., 'house' is next to 'water' or 'pole' is next to 'vehicle'. We have chosen an embedding dimension of $b=2$ to nicely illustrate the results, typically, word embedding dimensions range from 50 to 300 .

# Negative sampling 

For computational reasons, it can be difficult to solve the word2vec skip-gram approach (8.9)-(8.10), the categorical distribution in (8.10) has $W$ different levels, and likewise the input has this cardinality. Negative sampling turns this learning problem into a supervised learning problem of a lower complexity; see Mikolov et al. [157].
For this, we consider the pairs $(w, \widetilde{w}) \in \mathcal{W} \times \mathcal{W}$ of center words $w$ and context words $\widetilde{w}$. To each of these pairs we add a binary response variable $Y \in\{0,1\}$, resulting in observation $(Y, w, \widetilde{w})$. There will be two types of center-context pairs, real ones that are obtained from the learning sample $\mathcal{L}$ and fake ones that are generated purely randomly. We construct these two types of pairs as follows:
(1) We extract all center-context pairs $(w, \widetilde{w})$ from the learning sample $\mathcal{L}$ and we assign a response $Y=1$ to these pairs, for indicating that these are true pairs. This gives us the first part of the learning data, denoted by $\mathcal{L}_{1}=\left(Y_{i}=1, w_{i}, \widetilde{w}_{i}\right)_{i=1}^{n}$.
(2) We take all real pairs $\left(w_{i}, \widetilde{w}_{i}\right)_{i=1}^{n}$, and we randomly permute the index of the context word indicated by a permutation $\pi$. This gives us a second (fake) learning data set, we shift the index by $n$ for later purposes, $\mathcal{L}_{2}=\left(Y_{n+i}=0, w_{n+i}, \widetilde{w}_{n+\pi(i)}\right)_{i=1}^{n}$, with $Y=0$ as response.

Merging real and fake learning data gives us a learning sample $\mathcal{L}=\mathcal{L}_{1} \cup \mathcal{L}_{2}$ of sample size of $2 n$. This now allows us to turn the unsupervised learning problem into a supervised logistic regression problem by studying the new log-likelihood

$$
\begin{aligned}
\ell_{\mathcal{L}}= & \sum_{i=1}^{2 n} \log \mathbb{P}\left[Y=Y_{i} \mid w_{i}, \widetilde{w}_{i}\right] \\
= & \sum_{i=1}^{n} \log \left(\frac{1}{1+\exp \left\langle-\boldsymbol{e}^{(1)}\left(w_{i}\right), \boldsymbol{e}^{(2)}\left(\widetilde{w}_{i}\right)\right\rangle}\right) \\
& \quad+\sum_{k=n+1}^{2 n} \log \left(\frac{1}{1+\exp \left\langle\boldsymbol{e}^{(1)}\left(w_{k}\right), \boldsymbol{e}^{(2)}\left(\widetilde{w}_{k}\right)\right\rangle}\right)
\end{aligned}
$$

The first $n$ instances $1 \leq i \leq n$ come from the real data $\mathcal{L}_{1}$, and the second $n$ instances $n+1 \leq k \leq 2 n$ from the fake data $\mathcal{L}_{2}$ with the $\pi$-permuted context words. The two parts of the log-likelihood then correspond to the logistic probabilities for the responses $Y_{i}=1$ and $Y_{k}=0$ being real or fake, respectively. Maximizing this log-likelihood $\ell_{\mathcal{L}}$, we can learn the two embeddings (8.11). The example in Figure 8.2 has been obtained in this way.
For SGD training to work properly in this negative sampling learning, one should randomly permute the instances in $\mathcal{L}=\mathcal{L}_{1} \cup \mathcal{L}_{2}$, to ensure that all (mini-)batches contain instances of both types.

## Page 133
# Word2vec: continuous bag-of-words 

For the CBOW method we aim at predicting the center word $w_{t}$ from its context, see (8.7). As in the skip-gram approach, we select a fixed context (window) size $c \in \mathbb{N}$. For given learning sample $\mathcal{L}$, this provides us with the log-likelihood

$$
\sum_{i=1}^{n} \sum_{t} \log p\left(w_{i, t} \mid w_{i, t-c}, \ldots, w_{i, t-1}, w_{i, t+1}, \ldots, w_{i, t+c}\right)
$$

To solve this problem, we need again to reduce the complexity. As in the bag-of-words approach (8.4), we drop the positional index $t$. Moreover, for the (continuous) CBOW version, we average over the bag-of-words to receive the average embedding of the context words

$$
\bar{e}_{i, t}^{(2)}=\frac{1}{2 c} \sum_{-c \leq j \leq c, j \neq 0} \boldsymbol{e}^{(2)}\left(w_{i, t+j}\right)
$$

for the context word embedding $\boldsymbol{e}^{(2)}$, see (8.11). This averaging can be done because the word embedding gives a numerical representation to the context words. The CBOW approach then considers the following log-likelihood

$$
\begin{aligned}
\ell_{\mathcal{L}} & =\sum_{i=1}^{n} \sum_{t} \log p\left(\left.w_{i, t} \mid \bar{e}_{i, t}^{(2)}\right)\right. \\
& =\sum_{i=1}^{n} \sum_{t} \log \left(\frac{\exp \left\langle\boldsymbol{e}^{(1)}\left(w_{i, t}\right), \bar{e}_{i, t}^{(2)}\right\rangle}{\sum_{w=1}^{W} \exp \left\langle\boldsymbol{e}^{(1)}(w), \bar{e}_{i, t}^{(2)}\right\rangle}\right) \\
& =\sum_{i=1}^{n} \sum_{t}\left\langle\boldsymbol{e}^{(1)}\left(w_{i, t}\right), \bar{e}_{i, t}^{(2)}\right\rangle-\log \left(\sum_{w=1}^{W} \exp \left\langle\boldsymbol{e}^{(1)}(w), \bar{e}_{i, t}^{(2)}\right\rangle\right)
\end{aligned}
$$

Thus, we measure the similarity between the center word embedding $\boldsymbol{e}^{(1)}(w)$ and its average context word embedding $\bar{e}_{i, t}^{(2)}$. From this we can again learn the two embeddings (8.11) using a version of the SGD algorithm to minimize the negative log-likelihood.

Compared to skip-gram, CBOW is usually faster in fitting, but skip-gram performs better on less frequent words. Naturally, we can apply a negative sampling version to CBOW, by randomly permuting the average context words $\bar{e}_{i, t}^{(2)}$, and then designing a logistic regression that tries to identify the true and the fake pairs.

## Global vectors algorithm

Whereas word2vec is based on solid statistical methods, using well-defined and explainable log-likelihoods, GloVe is a word embedding approach that is more of an engineering type. GloVe was developed by Pennington et al. [175] and Chaubard et al. [40].
GloVe is more in the sense of clustering; clustering is going to be presented in Section 9.3, below. Select a fixed context size $c \in \mathbb{N}$ and count the different context words $\widetilde{w}$ in the context window of the given center word $w \in \mathcal{W}$. This defines the matrix of co-occurrences

$$
\boldsymbol{C}=(C(w, \widetilde{w}))_{w, \widetilde{w} \in \mathcal{W}} \in \mathbb{N}_{0}^{W \times W}
$$

Version March 3, 2025, @AI Tools for Actuaries

## Page 134
Matrix $\boldsymbol{C}$ is a symmetric matrix, and typically it is sparse as many words do not appear in the context of other words (on finitely many texts). Empirical analysis and intuitive arguments lead to an approach of approximating this co-occurrence matrix by

$$
\log C(w, \widetilde{w}) \approx\left\langle\boldsymbol{e}^{(1)}(w), \boldsymbol{e}^{(2)}(\widetilde{w})\right\rangle+\alpha_{w}+\beta_{\widetilde{w}}
$$

with intercepts $\alpha_{w}, \beta_{\widetilde{w}} \in \mathbb{R}$; see Pennington et al. [175]. To ensure that everything is well-defined, Pennington et al. [175] come up with the following objective function to be minimized

$$
\sum_{w, \widetilde{w} \in \mathcal{W}} \chi(C(w, \widetilde{w}))\left(\log C(w, \widetilde{w})-\left\langle\boldsymbol{e}^{(1)}(w), \boldsymbol{e}^{(2)}(\widetilde{w})\right\rangle-\alpha_{w}-\beta_{\widetilde{w}}\right)^{2}
$$

with a weighting function that takes care of zero co-occurrences

$$
x \geq 0 \mapsto \chi(x)=\left(\frac{x \wedge x_{\max }}{x_{\max }}\right)^{\gamma}
$$

for hyper-parameters $x_{\max }>0$ and $\gamma>0$. From this we can again learn the two embeddings (8.11) using the available learning data $\mathcal{L}$.
Clearly, GloVe is more difficult to implement and to fine-tune than the word2vec methods; some small scale examples in an insurance context are given in Wüthrich-Merz [243, Chapter 10]. This short introduction was not meant to explain GloVe to the level of explicit implementation and reasoning why it is sensible, but for GloVe (as well as for other methods) there is a large pre-trained version available that can be downloaded; ${ }^{2}$ other pre-trained open-source models that can be downloaded include, e.g., spaCy ${ }^{3}$ and FastText. ${ }^{4}$
These pre-trained word embeddings are ready to use, and they can be downloaded in different scales and embedding dimensions. A point that needs careful attention is that these word embeddings have been trained on a large corpus of texts from internet. These texts consider any sorts of topics. When it comes to a specific use of such pre-trained libraries, this needs some care because certain words have different meanings in different contexts. Wüthrich-Merz [243, Section 10] computed a non-life insurance example that considered insurance coverage of public institutions. In this example, the word Lincoln appears in several claims texts. Lincoln is a former US president, there are Lincoln memorials, there are towns called Lincoln, there is a Lincoln car brand, there are restaurants named Lincoln, but in the claims texts Lincoln is the school insured. Therefore, a pre-trained embedding may not be fully suitable for the purpose needed, because specific insurance related terminology may not have been used while training the embedding. This will require additional training of the pre-trained libraries to the specific purpose, while fitting the entire predictive model. Nevertheless, having a pre-trained data basis is often an excellent starting point for an actuarial application, and, in the sense of transfer learning, a pre-trained library can be refined for the specific task to be solved.

[^0]
[^0]:    ${ }^{2}$ https://nlp.stanford.edu/projects/glove/
    ${ }^{3}$ https://spacy.io/models/en\#en_core_web_md
    ${ }^{4}$ https://fasttext.cc

## Page 135
# 8.2.4 Summary of Section 8.2 

After this section, all input data has been tokenized and embedded, and we are equipped with input tensors, that can be of different form. They can be of

- vector form (1D tensor) from tabular data;
- matrix form (2D tensor) from time-series and text data;
- tensor form of order 3 (3D tensor) from image data.

Naturally, we can simultaneously use all these different input formats by designing suitable network architectures. E.g., we can use a FNN on the tabular input data providing us with a first intermediate output, we can use a recurrent neural network (RNN) on the times-series and text data providing us with second intermediate output, and we can use a convolutional neural network (CNN) on the image data providing us with third intermediate output. These intermediate outputs are concatenated and then further processed through a FNN providing a predictor variable. Such an example is illustrated in Figure 8.3.

Figure 8.3: Network architecture to process different types of input data.

FNNs have already been introduced in Chapter 5, and the following sections are going to be devoted to RNNs, CNNs as well as transformers, which is another popular way of dealing either with time-series data or with tabular data.

### 8.3 Convolutional neural networks

When data is represented as 2 D or 3 D tensors, as discussed in the previous sections, and characterized by large size, applying traditional FNN layers can be inappropriate. This relates to three issues.
(1) FNNs ignore spatial and/or time-series structure in the data, treating input elements equally regardless of their relative proximity in the positional index.
(2) FNN demand a large number of parameters, leading to significant computational costs.
(3) FNN cannot deal with time-series observations that are increasing over time.
![Page 135 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p135_img1.jpg)

## Page 136
To solve these issues, specialized network architectures like convolutional neural networks (CNNs) and recurrent neural networks (RNNs) have been introduced. In the present section, we study CNNs, introduced by LeCun-Bengio [130]. CNNs derive their name from the use of the convolution operator to extract features from the input tensors.

CNNs differ from FNNs in two key aspects:

- local connectivity; and
- parameter sharing.

First, regarding local connectivity, each unit (neuron) in a CNN layer is connected only to a localized region (window) of the input, known as the receptive field. The resulting weight matrices, called filters, present a smaller size than the entire input data because they focus on the receptive field (window) only, and the features extracted depend only on that portion of the input data.
Second, CNN layers employ parameter sharing, wherein the same filter is applied across all different regions of the input. That is, by sliding the filter across the input surface, we compute features in each receptive field using the identical filter (single set of weight matrix). One can imagine a rolling window similar to time-series applications.
$\Longrightarrow$ This design of local connectivity and parameter sharing significantly reduces the number of parameters to be learned compared to FNNs layers.

Different CNN layers are available; they differ in the number of dimensions over which the convolutional operation is applied to. The choice of dimension depends on the characteristics of the input data and the specific prediction task. In the following sections, we formally describe the mechanisms of 1D and 2D CNN layers. However, it should be noted that that these principles can be generalized to any higher dimension.

# 8.3.1 1D convolutional neural networks 

1D CNNs are specifically designed to handle data organized in a one-dimensional grid-like structure, such as sequences or time-series (panel) data.

1D CNN architectures apply a convolution operation along a single axis (position/time axis) making them effective for capturing sequential patterns and temporal dependencies in the data. In this sense, the filters act as rolling windows over the input data.
When applying a 1D CNN layer the modeler needs to specify some hyper-parameters. Among them, the kernel size $K \in \mathbb{N}$ and the stride $\delta \in \mathbb{N}$ play a key role since they define the size and the number of receptive fields.

- The kernel size defines the length of the filters (window size) used in the convolutional operation. This parameter determines the size of the receptive field, or the range of input values each filter can 'see' at a time. A larger kernel size allows the model to detect features that span longer sequences. However, this also increases the number of parameters and the computational complexity of the model.

## Page 137
- The stride specifies the step size with which the kernel moves along the input sequence during the convolution process. A smaller stride (e.g., $\delta=1$ ) results in overlapping receptive fields, which can provide a more detailed representation of the input but at the cost of higher computational costs. On the other hand, a larger stride (e.g., $\delta \geq 2$ ) reduces the overlap, leading to faster computation at the risk of losing information.

Figure 8.4: CNN filter of kernel size $K=3$ and using (lhs) stride $\delta=1$ and (rhs) stride $\delta=3$.

A 1D CNN layer can be thought of as operating like a rolling window procedure. The kernel directly corresponds to the size of the rolling window, which slides across the input sequence, examining a fixed number of consecutive elements at each step. The stride, meanwhile, defines the step size, determining how far the rolling window advances along the input after each computation. Figure 8.4 shows two examples with kernel size $K=3$, the left-hand side has stride $\delta=1$ giving overlapping windows on the time axis $t$, whereas the right-hand side has stride $\delta=3$ giving non-overlapping windows. These input parameters $K$ and $\delta$ need to be selected by the modeler and their choices depend on the trade-off between computational efficiency and the desired level of feature resolution.

1D CNN filter. We begin by illustrating the mechanism of a 1D CNN layer by considering a single filter for simplicity. Let $\boldsymbol{X}_{1: t} \in \mathbb{R}^{t \times q}$ be the input data matrix. An 1D CNN layer with a single filter of size $K$ with stride $\delta$ is a mapping

$$
\boldsymbol{z}_{1}^{(1)}: \mathbb{R}^{t \times q} \rightarrow \mathbb{R}^{t^{\prime}}, \quad \boldsymbol{X}_{1: t} \mapsto \boldsymbol{z}_{1}^{(1)}\left(\boldsymbol{X}_{1: t}\right)=\left(z_{u, 1}^{(1)}\left(\boldsymbol{X}_{1: t}\right)\right)_{1 \leq u \leq t^{\prime}}
$$

where $t^{\prime}=\left\lfloor\frac{t-K}{\delta}+1\right\rfloor \in \mathbb{N}$ represents the number of receptive fields. Unit $z_{u, 1}^{(1)}\left(\boldsymbol{X}_{1: t}\right) \in \mathbb{R}$ is extracted by convolving the filter with the $u$-th receptive field

$$
z_{u, 1}^{(1)}\left(\boldsymbol{X}_{1: t}\right)=\phi\left(w_{0,1}^{(1)}+\sum_{k=1}^{K}\left\langle\boldsymbol{w}_{k, 1}^{(1)}, \boldsymbol{X}_{(u-1) \delta+k}\right\rangle\right)
$$

with bias term $w_{0,1}^{(1)} \in \mathbb{R}$, filter weights $\boldsymbol{w}_{k, 1}^{(1)} \in \mathbb{R}^{q}, 1 \leq k \leq K$, and activation function $\phi: \mathbb{R} \rightarrow \mathbb{R}$.
The total number of parameters to be learned in a 1D CNN layer with 1 filter is $1+K q$. The size of the output of the filter $\boldsymbol{z}_{1}^{(1)}$, defined as the number of receptive fields $t^{\prime}$, depends on $K$ and $\delta$. Remark that (8.14) (almost) takes the form of a mathematical convolution (up to a sign switch in one of the two indices).
![Page 137 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p137_img1.jpg)

## Page 138
1D CNN layer. In practice, a single filter may not be sufficient to capture the complexity of the features in the input data; this is similar to the number of neurons in a FNN layer. To address this issue, multiple filters can be concatenated, each learning a different set of features, i.e., using different filter weights.

A 1D CNN layer with $q_{1} \in \mathbb{N}$ filters is a mapping

$$
\boldsymbol{z}^{(1)}: \mathbb{R}^{t \times q} \rightarrow \mathbb{R}^{t^{\prime} \times q_{1}}, \quad \boldsymbol{X}_{1: t} \mapsto \boldsymbol{z}^{(1)}\left(\boldsymbol{X}_{1: t}\right)=\left(z_{u, j}^{(1)}\left(\boldsymbol{X}_{1: t}\right)\right)_{1 \leq u \leq t^{\prime}, 1 \leq j \leq q_{1}}
$$

In particular, each element of the matrix is, denoted as $z_{u, j}^{(1)}\left(\boldsymbol{X}_{1: t}\right)$, is a unit obtained by convolving the $j$-th filter with the $u$-th receptive field

$$
z_{u, j}^{(1)}\left(\boldsymbol{X}_{1: t}\right)=\phi\left(w_{0, j}^{(1)}+\sum_{k=1}^{K}\left\langle\boldsymbol{w}_{k, j}^{(1)}, \boldsymbol{X}_{(u-1) \delta+k}\right\rangle\right)
$$

with bias term $w_{0, j}^{(1)} \in \mathbb{R}$ and filter weights $\boldsymbol{w}_{k, j}^{(1)} \in \mathbb{R}^{q}, 1 \leq k \leq K$. In this case, the total number of parameters to be learned is $(1+K q) q_{1}$.

In this context we have:

- The $j$-th column of the matrix $\boldsymbol{z}^{(1)} \in \mathbb{R}^{t^{\prime} \times q_{1}}$ given in (8.15), containing the elements $z_{1, j}^{(1)}, z_{2, j}^{(1)}, \ldots, z_{t^{\prime}, j}^{(1)}$, represents a set of features extracted by applying the same filter to the different receptive fields (sliding along the time axis). This provides a representation of all receptive fields in a common feature space.
- The $u$-th row of the matrix $\boldsymbol{z}^{(1)} \in \mathbb{R}^{t^{\prime} \times q_{1}}$ given in (8.15), containing the elements $z_{u, 1}^{(1)}, z_{u, 2}^{(1)}, \ldots, z_{u, q_{1}}^{(1)}$, represents a set of features obtained by applying $q_{1}$ different filters to the $u$-th receptive field. These features provide multiple representations of the same receptive field, or in other words, a slice across the different filters. This enables the model to extract different sets of features from each receptive field, capturing different aspects of the data and resulting in multi-dimensional representations; this is analogous to having multiple neurons in a FNN layer.

Figure 8.5 provides a graphical illustration of how a 1D CNN layer with $q_{1}$ filters works. It emphasizes that these layers perform computations based on a convolutional operator, where the filters are convolved across different regions of the input, similar to how the two functions interact in a mathematical convolution. In the figure, the blue matrix represents the input data $\boldsymbol{X}_{1: t}$. Each filter is applied to the input data, generating a corresponding set of features that are graphically represented by a colored rectangular block; e.g., the yellow filter weights $\left(w_{0,1}^{(1)},\left(\boldsymbol{w}_{k, 1}^{(1)}\right)_{k=1}^{K}\right)$ map to the first block $\boldsymbol{z}_{1}^{(1)}=\left(z_{u, 1}^{(1)}\right)_{u=1}^{t^{\prime}}$ (in yellow). The feature vectors $\boldsymbol{z}_{1}^{(1)}, \ldots, \boldsymbol{z}_{q_{1}}^{(1)}$ obtained from the $q_{1}$ filters are then concatenated along the appropriate dimension, resulting in the matrix (1D tensor) $\boldsymbol{z}^{(1)}$, see (8.15). This output matrix can be interpreted as a learned multi-dimensional representation of the time-series input data (respecting time adjacency), ready to be passed to subsequent layers for further processing.

## Page 139
Figure 8.5: A graphical illustration of a 1D CNN layer.

# 8.3.2 2D convolutional neural networks 

2D CNNs are specifically designed to process data structured in a two-dimensional grid, such as images or spatially structured data sets.

The input data consists of three dimensions and is represented as 3 D tensors in $\mathbb{R}^{t \times s \times q}$, where $q$ represents the number of channels (e.g., $q=3$ for the RGB color channels in images, see Example 8.1). The convolution operation involves sliding a small window across the two axes $t$ and $s$, while simultaneously processing all $q$ channels at each position. This enables the model to perform convolution operations along both the vertical $t$ and horizontal $s$ axes, making it highly effective at detecting spatial patterns and local structure in the input data $\boldsymbol{X}_{1: t, 1: s} \in \mathbb{R}^{t \times s \times q}$. Popular applications in the actuarial literature of 2D CNNs are pattern recognition problems, e.g., for telematics data, see Gao et al. [72], or mortality modeling, see Wang et al. [231].

In the case of a 2D CNN, both the kernel size and stride are represented as pairs of elements that specify the size and movement of the filter in two dimensions.

- The kernel size is denoted by $K=\left(K_{t}, K_{s}\right) \in \mathbb{N}^{2}$, where $K_{t}$ represents the height of the kernel (number of rows), and $K_{s}$, represents the width of the kernel (number of columns). This pair defines the filter's spatial extent, determining the window size of the regions over which the convolution operation slides and applies the kernel to the input data.
- The stride in a 2 D CNN is represented by $\delta=\left(\delta_{t}, \delta_{s}\right) \in \mathbb{N}^{2}$, where $\delta_{t}$ denotes the vertical stride (the number of rows the filter moves after each step), and $\delta_{s}$ denotes the horizontal stride (the number of columns the filter moves after each step).

Also in the case of a 2D CNN layer, the kernel size $\left(K_{t}, K_{s}\right)$ and stride $\delta=\left(\delta_{t}, \delta_{s}\right)$ directly affect both the size of the output feature map and the computational complexity of the convolution operation. The output of a 2D CNN layer with a single filter is a feature
![Page 139 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p139_img1.jpg)

## Page 140
matrix with $t^{\prime}=\left\lfloor\frac{t-K_{t}}{\delta_{t}}+1\right\rfloor$ rows and $s^{\prime}=\left\lfloor\frac{s-K_{s}}{\delta_{s}}+1\right\rfloor$ columns. In this case, the total number of receptive fields is given by $t^{\prime} s^{\prime}$.

2D CNN filter. Let $\boldsymbol{X}_{1: t, 1: s} \in \mathbb{R}^{t \times s \times q}$ be the input tensor with $q$ channels. A 2D CNN layer with a single filter of size $K_{t} \times K_{s}$ and stride $\delta_{t} \times \delta_{s}$ is a mapping

$$
\boldsymbol{z}_{1}^{(1)}: \mathbb{R}^{t \times s \times q} \rightarrow \mathbb{R}^{t^{\prime} \times s^{\prime}}, \quad \boldsymbol{X}_{1: t, 1: s} \mapsto \boldsymbol{z}_{1}^{(1)}\left(\boldsymbol{X}_{1: t, 1: s}\right)=\left(z_{u, v, 1}^{(1)}\left(\boldsymbol{X}_{1: t, 1: s}\right)\right)_{1 \leq u \leq t^{\prime}, 1 \leq v \leq s^{\prime}}
$$

Unit $z_{u, v, 1}^{(1)}\left(\boldsymbol{X}_{1: t, 1: s}\right)$ is extracted by convolving the filter with the receptive field $(u, v)$

$$
z_{u, v, 1}^{(1)}\left(\boldsymbol{X}_{1: t, 1: s}\right)=\phi\left(w_{0,1}^{(1)}+\sum_{k_{t}=1}^{K_{t}} \sum_{k_{s}=1}^{K_{s}}\left\langle\boldsymbol{w}_{k_{t}, k_{s}, 1}^{(1)}, \boldsymbol{X}_{(u-1) \delta_{t}+k_{t},(v-1) \delta_{s}+k_{s}}\right\rangle\right)
$$

with bias term $w_{0,1}^{(1)} \in \mathbb{R}$ and filter weights $\boldsymbol{w}_{k_{t}, k_{s}, 1}^{(1)} \in \mathbb{R}^{q}$, for $1 \leq k_{t} \leq K_{t}$ and $1 \leq k_{s} \leq K_{s}$. The total number of parameters to be optimized is $1+K_{t} K_{s} q$. The rows of the matrix $\boldsymbol{z}_{1}^{(1)}\left(\boldsymbol{X}_{1: t, 1: s}\right)$ are obtained by sliding the filter (window) across the input data in a horizontal direction, i.e., the filter moves from left to right across the rows of the input. Each row of the matrix corresponds to a different receptive field $(u, v)$ along this horizontal pass. On the other hand, the columns of the matrix are obtained by sliding the filter vertically over the input data. In this case, the filter moves from top to bottom across the columns of the input. Each column in the matrix corresponds to a different receptive field in this vertical pass.

2D CNN layer. Also in the case of 2D CNN layer, multiple filters can be applied.
A 2D CNN layer with $q_{1}$ filters is a mapping

$$
\begin{aligned}
\boldsymbol{z}^{(1)}: \mathbb{R}^{t \times s \times q} & \rightarrow \mathbb{R}^{t^{\prime} \times s^{\prime} \times q_{1}} \\
\boldsymbol{X}_{1: t, 1: s} & \mapsto \boldsymbol{z}^{(1)}\left(\boldsymbol{X}_{1: t, 1: s}\right)=\left(z_{u, v, j}^{(1)}\left(\boldsymbol{X}_{1: t, 1: s}\right)\right)_{1 \leq u \leq t^{\prime}, 1 \leq v \leq s^{\prime}, 1 \leq j \leq q_{1}}
\end{aligned}
$$

with $\boldsymbol{z}_{j}^{(1)}\left(\boldsymbol{X}_{1: t, 1: s}\right) \in \mathbb{R}^{t^{\prime} \times s^{\prime}}, 1 \leq j \leq q_{1}$, being 2D CNN filters (8.17) with different filter weights. Each element of the $j$-th feature map is computed as the double summation (convolution)

$$
z_{u, v, j}^{(1)}\left(\boldsymbol{X}_{1: t, 1: s}\right)=\phi\left(w_{0, j}^{(1)}+\sum_{k_{t}=1}^{K_{t}} \sum_{k_{s}=1}^{K_{s}}\left\langle\boldsymbol{w}_{k_{t}, k_{s}, j}^{(1)}, \boldsymbol{X}_{(u-1) \delta_{t}+k_{t},(v-1) \delta_{s}+k_{s}}\right\rangle\right)
$$

where $w_{0, j}^{(1)} \in \mathbb{R}$ is the bias term of the $j$-th filter, and $\boldsymbol{w}_{k_{t}, k_{s}, j}^{(1)} \in \mathbb{R}^{q}, 1 \leq k_{t} \leq K_{t}$ and $1 \leq k_{s} \leq K_{s}$, represents the filter weights for that $j$-th filter. The total number of coefficients to learn in a 2D CNN layer with $q_{1}$ filters of size $K_{t} \times K_{s}$ is $\left(1+K_{t} K_{s} q\right) q_{1}$.

The graphical representation of how a 2D CNN layer works is shown in Figure 8.6. The 3 D object in blue represents the input data, while the 3 D yellow object represents the first filter. By sliding this filter horizontally and vertically over the input tensor a feature map is produced, resulting in the yellow 2 D CNN filter output $\boldsymbol{z}_{1}^{(1)}\left(\boldsymbol{X}_{1: t, 1: s}\right) \in \mathbb{R}^{t^{\prime} \times s^{\prime}}$. Concatenating the feature maps obtained from the $q_{1}$ different filters generates the output of the 2D CNN layer.

## Page 141
Figure 8.6: A graphical illustration of a 2D CNN layer.

# 8.3.3 Deep convolutional neural networks 

Multiple CNN layers can be composed to capture increasingly complex and hierarchical features from the input data. This allows for learning low-level (local) patterns in the initial layers, which are subsequently combined into higher-level (more global) abstractions in deeper layers. As is standard in FNN architectures, the output of one layer serves as input to the next layer, allowing information to propagate through the network. For instance, in a two-layer 2D CNN architecture, the output of the first 2D CNN layer, denoted as $\boldsymbol{z}^{(1)}\left(\boldsymbol{X}_{1: t, 1: s}\right)$, becomes the input to the second 2D CNN layer. Each CNN layer is characterized by a specific set of input parameters such as the kernel size and the stride, which can vary across layers to optimally extract feature information.

To distinguish the layer-specific parameters, an additional upper index is introduced. We denote the kernel sizes of the first and second layers by $K^{(1)}$ and $K^{(2)}$, respectively, and correspondingly we denote their strides by $\delta^{(1)}$ and $\delta^{(2)}$.

For illustrative purposes, we consider the 2D CNN case. Assume that the output dimension $\left(t^{\prime}, s^{\prime}, q_{1}\right)$ of a first 2D CNN layer $\boldsymbol{z}^{(1)}$, see (8.18), coincides with the input dimension of a second 2D CNN layer $\boldsymbol{z}^{(2)}$, having the same structure as (8.18), that is,

$$
\boldsymbol{z}^{(2)}: \mathbb{R}^{t^{\prime} \times s^{\prime} \times q_{1}} \rightarrow \mathbb{R}^{t^{\prime \prime} \times s^{\prime \prime} \times q_{2}}
$$

where

$$
t^{\prime \prime}=\left\lfloor\frac{t^{\prime}-K_{t}^{(2)}}{\delta_{t}^{(2)}}+1\right\rfloor \in \mathbb{N} \quad \text { and } \quad s^{\prime \prime}=\left\lfloor\frac{s^{\prime}-K_{s}^{(2)}}{\delta_{s}^{(2)}}+1\right\rfloor \in \mathbb{N}
$$

and where we select $q_{2} \in \mathbb{N}$ filters for this second 2D CNN layer.
We can then compose these two 2D CNN layers to a deep 2D CNN architecture

$$
\boldsymbol{z}^{(2: 1)}: \mathbb{R}^{t \times s \times q} \rightarrow \mathbb{R}^{t^{\prime \prime} \times s^{\prime \prime} \times q_{2}} \quad \text { with } \quad \boldsymbol{z}^{(2: 1)}=\boldsymbol{z}^{(2)} \circ \boldsymbol{z}^{(1)}
$$

Naturally, this mechanism also works for 1D CNN layers, and we can generalize it to any depth $d$, resulting in a deep CNN architectures $\boldsymbol{z}^{(d: 1)}=\boldsymbol{z}^{(d)} \circ \cdots \circ \boldsymbol{z}^{(1)}$. Importantly, always the output dimension of the CNN layer $\boldsymbol{z}^{(m-1)}$ has to match in the input dimension of the next CNN layer $\boldsymbol{z}^{(m)}$. This is completely analogous to deep FNN architectures $(5.3)$.
![Page 141 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p141_img1.jpg)

## Page 142
This almost fully describes (deep) CNN architectures. There are some more points that we would like to discuss:

- Locally-connnected networks which are a special case of CNNs.
- Pooling layers which are useful to reduce tensor dimensions.
- Padding which increases tensors.
- Flatten layer which restructures tensors.

This is discussed in the next sections. When it comes to CNN fitting, we apply a version of SGD, see Section 5.3.

# 8.3.4 Locally-connected networks 

A notable variant of CNNs is the locally-connected network (LCN). LCNs preserve the concept of local connectivity while removing the parameter sharing mechanism that characterizes CNNs. As a result, LCNs can be seen as a middle ground between CNNs and FNNs. In a LCN, each receptive field is assigned a unique set of weights, enhancing the model's flexibility and allowing it to capture location-specific patterns that CNNs might overlook. However, this extra flexibility comes at the cost of significantly more parameters than for CNNs. LCN layers have been introduced to the actuarial literature in Scognamiglio [205] for 1D LCNs and in Perla et al. [176] for 2D LCNs.

For simplicity, we use the 1D case for explaining a LCN layer, and the 2D case is completely analogous. Formally, a 1D LCN layer with $q_{1} \in \mathbb{N}$ filters is a mapping

$$
\boldsymbol{z}^{(1)}: \mathbb{R}^{t \times q} \rightarrow \mathbb{R}^{t^{\prime} \times q_{1}}, \quad \boldsymbol{X}_{1: t} \mapsto \boldsymbol{z}^{(1)}\left(\boldsymbol{X}_{1: t}\right)=\left(z_{u, j}^{(1)}\left(\boldsymbol{X}_{1: t}\right)\right)_{1 \leq u \leq t^{\prime}, 1 \leq j \leq q_{1}}
$$

with element of the matrix is a features obtained by

$$
z_{u, j}^{(1)}\left(\boldsymbol{X}_{1: t}\right)=\phi\left(w_{0, u, j}^{(1)}+\sum_{k=1}^{K}\left\langle\boldsymbol{w}_{k, u, j}^{(1)}, \boldsymbol{X}_{(u-1) \delta+k}\right\rangle\right)
$$

with bias terms $w_{0, u, j}^{(1)} \in \mathbb{R}$ and filter weights $\boldsymbol{w}_{k, u, j}^{(1)} \in \mathbb{R}^{q}, 1 \leq k \leq K$, related to the $u$-th receptive field. In this case, the total number of parameters to be learned is $(1+K q) q_{1} t^{\prime}$. Compared to (8.15) and (8.16) there is only one difference, namely, the bias terms and filter weights have a lower index $u$ that corresponds to the $u$-th receptive field considered. This increases the size of the parameters by a factor $t^{\prime}$ compared to the 1D CNN case.
Figure 8.7 provides a graphical representation of the FNN, LCN and CNN layers; the number of parameters exclude the bias terms. For an input tensor $\boldsymbol{X}_{1: 6} \in \mathbb{R}^{6 \times 1}$ we have 18 parameters by mapping this to a FNN layer with $q_{1}=3$ neurons, see Figure 8.7 (lhs). The right-hand side shows an example of a 1D CNN layer with kernel size $K=2$ and stride $\delta=2$, resulting in 2 parameters. The LCN layer (with the same kernel size and stride) in between has 6 parameters.

## Page 143
Figure 8.7: A graphical comparison of the FNN, LCN and CNN layers; the number of parameters excludes the bias terms.

# 8.3.5 Pooling layers 

Pooling layers are designed to summarize local information and to reduce the dimensions of tensors. They are commonly used in architectures involving CNN layers. Typically applied after a CNN layer, pooling reduces the tensor's dimension while preserving its most significant information. One of the earliest papers to make use of this kind of layers is LeCun et al. [131]. A pooling function replaces the network's output at a specific location with a summary statistics derived from nearby values, such as the maximum or the average value. In a sense, pooling layers are similar to CNN layers, as both operate on local regions (windows) of the inputs. However, instead of performing a convolution (which involves multiplying the input by a set of weights and summing the results), a pooling layer performs a down-sampling operation. Pooling layers require specifying the pooling size, which is the analogue to the kernel size in CNN layers, denoted as $K$, and the stride $\delta$. In most cases, the stride is set to its default value $\delta=K$.
There are several types of pooling layers, and the choice of the specific pooling technique depends on the task to be performed. Among the most popular pooling layers, there are:

- MaxPooling: It selects the maximum value from a set of input values in the selected pooling windows. This operation is commonly preferred when the goal is to emphasize the most relevant features while ignoring the less significant ones.
- AveragePooling: It computes the average of the values within the given pooling windows. This operation results in smoother feature maps, as it considers the overall characteristics of a local neighborhood, rather than focusing on extreme values. AveragePooling is especially appropriate when the objective is to capture the overall structure or distribution.

Guidance on selecting the appropriate types of pooling for various scenarios is provided in Boureau et al. [25]. Again, as a several other items, to find the right pooling and its parameterization is part of hyper-parameter tuning that needs to be performed by the modeler. Notably, we remark that pooling layers can be applied along multiple dimensions, depending on the structure of the input data.

For illustrative purposes, we consider the 1D pooling case, and the 2D case is completely similar. For this we keep the 1D CNN layer in mind, see (8.15). The only difference is
![Page 143 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p143_img1.jpg)

## Page 144
that we replace the convolutional operation (8.16) by pooling operations. For this we select a pooling size $K \in \mathbb{N}$ and a stride $\delta \in \mathbb{N}$ giving the mapping

$$
\boldsymbol{z}^{\mathrm{pool}}: \mathbb{R}^{t \times q} \rightarrow \mathbb{R}^{t^{\prime} \times q}, \quad \boldsymbol{X}_{1: t} \mapsto \boldsymbol{z}^{(1)}\left(\boldsymbol{X}_{1: t}\right)=\left(z_{u, j}^{\mathrm{pool}}\left(\boldsymbol{X}_{1: t}\right)\right)_{1 \leq u \leq t^{\prime}, 1 \leq j \leq q}
$$

Here, we note that the 1D pooling layer reduces the first dimension of the data from $t$ to $t^{\prime}=\left\lfloor\frac{t-K}{\delta}+1\right\rfloor$ while preserving the original covariate dimension $q$. The elements of the output depend on the type of pooling used:

- In the case of MaxPooling, we consider

$$
z_{u, j}^{\mathrm{pool}}\left(\boldsymbol{X}_{1: t}\right)=\max _{(u-1) \delta+1 \leq k \leq u \delta} X_{k, j}
$$

- In the case of AveragePooling, we consider

$$
z_{u, j}^{\mathrm{pool}}\left(\boldsymbol{X}_{1: t}\right)=\sum_{k=(u-1) \delta+1}^{u \delta} X_{k, j}
$$

The case of 2D pooling is completely analogous. For the default stride $\delta=K$, we consider a partition of the tensor, and in each of these subsets of the partition we either extract the maximum or the average, depending on the type of pooling, this also relates to Figure 8.4 (rhs).

# 8.3.6 Padding 

Padding refers to the process of adding extra values, generally zeros, to the edges of a tensor before applying the convolution operation. This technique is used to control the dimension of the output feature map and to ensure that the network effectively captures information located at the edges. When a CNN layer is applied to the input data tensor, it typically reduces the dimension from $(t, s)$ to $\left(t^{\prime}, s^{\prime}\right)$ because the filter does not fully operate on the edges of the input even if we have a stride $\delta=1$. A widely used solution to this problem, known as padding, involves adding zeros to the edges of the input data to ensure that the output feature map maintains the same spatial dimensions as the original input tensor. This allows for the filter to operate effectively at the borders without reducing the size of the output. Padding can be applied to various types of input tensors. For example, in 1D CNNs (used for time-series data), padding may be applied at the start and end of the sequence. Similarly, in 2D CNNs, padding is applied along both dimensions and so on for higher-dimensional CNNs. The amount of padding is typically determined based on the filter size $K$, we assume stride $\delta=1$ for the moment. For instance, in the case of a 2D CNN layer with a filter of size $3 \times 3$, padding of 1 pixel is commonly added to each side of the input to preserve its original dimensions.
Figure 8.8 graphically illustrates the process of applying padding to data in both onedimensional and two-dimensional cases.

## Page 145
Figure 8.8: 1D and 2D padding.

# 8.3.7 Conclusions and flatten layers 

We have now met all the modules that are necessary to use CNNs as feature extractors. Generally, the output of a deep CNN architecture is a tensor that has the same order as the input tensor, e.g., in a time-series example, the output tensor is an element $\boldsymbol{z}^{(d: 1)}\left(\boldsymbol{X}_{1: t}\right) \in \mathbb{R}^{t^{\prime} \times q_{d}}$. If we want to use this new data representation $\boldsymbol{z}^{(d: 1)}\left(\boldsymbol{X}_{1: t}\right)$ for predictive modeling, say, to forecast an insurance claim in the next period, it needs further processing, e.g., through a FNN layer; this is illustrated in Figure 8.3. In particular, this requires to transform the tensor $\boldsymbol{z}^{(d: 1)}\left(\boldsymbol{X}_{1: t}\right)$ into a vector of length $t^{\prime} q_{1}$. In machine learning lingo, this shape transformation is called flatten, and it is implemented by a so-called flatten layer (which only performs that shape transformation of a tensor to a vector). After this flatten layer, the extracted information can be concatenated with other vector information, as illustrated in Figure 8.3.

### 8.4 Recurrent neural networks

Recurrent neural networks (RNNs) are a class of neural networks specifically designed to process sequential data.

RNNs generate predictions at a given time step, by taking into account the preceding elements of the sequence. This mechanism is implemented through the introduction of cyclic/recurrent connections within the network which feed the output of a network layer back into the network as input enabling information to persist across several time steps. This design makes RNNs promising methods for tasks where the order of data is relevant (time-causality), such as text processing or time-series forecasting.
The two most popular RNN architectures are the long short-term memory (LSTM) architecture of Hochreiter-Schmidhuber [100] and the gated recurrent unit (GRU) architecture of Cho et al. [42]. These two architectures are presented in Sections 8.4.2 and 8.4.3, below. An early actuarial application of RNNs is the mortality example of Nigri et al. [167], and Lindholm-Palmborg [139] discuss the efficient use of data in time-series mortality problems.
![Page 145 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p145_img1.jpg)

## Page 146
# 8.4.1 Plain-vanilla recurrent neural networks 

We begin by introducing the simplest form of a RNN architecture, termed plain-vanilla $R N N$. This architecture represents the starting point for building more complex RNN models, and it is useful to understand the recurrent mechanism. We explain the mechanism behind the RNN with a focus on time-series data.

Consider a multivariate time-series $\boldsymbol{X}_{1: t} \in \mathbb{R}^{t \times q}$ with components $\boldsymbol{X}_{u} \in \mathbb{R}^{q}$ at times $1 \leq$ $u \leq t$. RNNs generate predictions at specific time steps $u$ by processing the past observed values of the time-series. Specifically, past observations $\boldsymbol{X}_{1: u-1}$ are compressed into a statistics $\boldsymbol{z}_{u-1}^{(1)}$, which is concatenated with the new covariate $\boldsymbol{X}_{u}$. The concatenation of these two objects is then used to predict the next response $Y_{u}$. Note that the covariate $\boldsymbol{X}_{u}$ may also include the past observation $Y_{u-1}$, which corresponds to a look-back of size one. Of course, the look-back can have any length.

At each time step $1 \leq u \leq t$, the RNN receives two inputs:
(1) the value $\boldsymbol{X}_{u}$ of the sequence $\boldsymbol{X}_{1: t}$ at the current time step $u$, and
(2) the output of the $R N N$ cell $\boldsymbol{z}_{u-1}^{(1)}$ from the previous time step $u-1$.

The output $\boldsymbol{z}_{u-1}^{(1)}$ of the previous RNN step can be seen as a compressed summary (learned representation) of the past observations $\boldsymbol{X}_{1: u-1}$ prior to $u$. These two components are concatenated to generate the next prediction.

RNN layer. A RNN layer with $q_{1} \in \mathbb{N}$ units is given by the mapping

$$
\boldsymbol{z}^{(1)}: \mathbb{R}^{q \times q_{1}} \rightarrow \mathbb{R}^{q_{1}}, \quad\left(\boldsymbol{X}_{u}, \boldsymbol{z}_{u-1}^{(1)}\right) \mapsto \boldsymbol{z}_{u}^{(1)}:=\boldsymbol{z}^{(1)}\left(\boldsymbol{X}_{u}, \boldsymbol{z}_{u-1}^{(1)}\right)
$$

where $\boldsymbol{X}_{u}$ is the covariate at time $u \geq 1$ and $\boldsymbol{z}_{u-1}^{(1)}$ is the output from the previous RNN loop; we initialize $\boldsymbol{z}_{0}^{(1)}=\mathbf{0}$. The vector $\boldsymbol{z}_{u}^{(1)}=\left(z_{u, 1}^{(1)}, \ldots, z_{u, q_{1}}^{(1)}\right)^{\top}$ is interpreted as a learned representation considering all information $\boldsymbol{X}_{1: u}$. The $j$-th unit is computed as

$$
z_{u, j}^{(1)}=z_{u, j}^{(1)}\left(\boldsymbol{X}_{1: u}\right)=\phi\left(w_{0, j}^{(1)}+\left\langle\boldsymbol{w}_{j}^{(1)}, \boldsymbol{X}_{u}\right\rangle+\left\langle\boldsymbol{v}_{j}^{(1)}, \boldsymbol{z}_{u-1}^{(1)}\right\rangle\right)
$$

with bias $w_{0, j}^{(1)} \in \mathbb{R}$, network weights $\boldsymbol{w}_{j}^{(1)} \in \mathbb{R}^{q}$ and $\boldsymbol{v}_{j}^{(1)} \in \mathbb{R}^{q_{1}}$, and activation function $\phi: \mathbb{R} \rightarrow \mathbb{R}$.

Comparing (8.21)-(8.22) to the FNN layer (5.5)-(5.6), we observe that we have precisely the same structure, that is, we can consider the concatenated input $\left(\boldsymbol{X}_{u}, \boldsymbol{z}_{u-1}^{(1)}\right) \in \mathbb{R}^{q+q_{1}}$ which is processed through a FNN layer that has input dimension $q+q_{1}$ and output dimension $q_{1}$, see (5.5). The change is that we have a recurrent loop, reflected by the lower index in the compressed past information (RNN cell) $\boldsymbol{z}_{u-1}^{(1)}$.

The parameters of an RNN layer are time-independent, since they remain constant across all time steps $1 \leq u \leq t$. This mechanism is similar to the parameter sharing mechanism adopted in the 1D CNNs. The main difference is that, in CNNs, each output is calculated using a small window of neighboring inputs, resulting in a shallow structure. In contrast, RNNs rely on a recurrent mechanism where each output depends on the previous outputs,

## Page 147
with the same update rule applied recursively. This design creates a deep computational graph allowing to learn long-run time dependencies in the data. The total number of parameters to optimize in an RNN layer with $q_{1}$ cells is given by $q_{1}\left(1+q+q_{1}\right)$. A visual representation of the recurrent mechanism of an RNN unit is provided in Figure 8.9. At each time step, the unit produces an output, with the final output of the sequence highlighted in red. In most applications of neural networks, particularly in tasks involving

Figure 8.9: The recurrent mechanism of a RNN cell.
sequential data, only the last RNN cell state $\boldsymbol{z}_{t}^{(1)}=\boldsymbol{z}_{t}^{(1)}\left(\boldsymbol{X}_{1: t}\right)$ is used to generate the prediction of response $Y_{t}$. However, in some cases, the model can be beneficial to consider the entire sequence (called return sequence) of RNN cell states across the different time steps, represented as $\left(\boldsymbol{z}_{u}^{(1)}\right)_{u=1}^{t}$. This provides a more comprehensive/granular representation of the input data. In such scenarios, one may apply flatting to further process the data, see Section 8.3.7 and Figure 8.3.

For training RNNs, one commonly uses the back-propagation through time (BPTT) algorithm, see Werbos [235]. BPTT unrolls the RNN across the entire sequence during optimization. While effective, BPTT often suffers from issues such as slow convergence, vanishing gradients, and difficulties in learning long-term dependencies. To overcome these challenges, more advanced RNN architectures such as LSTM and GRU networks were introduced. These are discussed next.

# 8.4.2 Long short-term memory networks 

LSTM networks, introduced in Hochreiter-Schmidhuber [100], extend the basic structure of traditional RNNs by incorporating a specialized mechanism to handle long-term dependencies more effectively. The core of this more advanced RNN model is the memory cell, which is designed to store and regulate the flow of long-term information throughout the network. The memory cell in LSTMs operates using a system of gates (namely the input, output, and forget gates) that control how information is stored, updated, and
![Page 147 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p147_img1.jpg)

## Page 148
released. This gating mechanism allows the network to select important information that has to be kept in the memory and discard irrelevant or outdated data, making it more effective in capturing long-term dependencies. By combining this long-term memory with the short-term memory provided by the recurrent connections, LSTMs are able to learn both long and short-term dependencies simultaneously.
To calculate the output of the LSTM layer, three activation functions are applied. The sigmoid function $\sigma \in(0,1)$, the hyperbolic tangent function $\tanh (x) \in(-1,1)$, and a general activation function $\phi$, we refer for their definitions to Table 5.1.

LSTM layer. We formally introduce an LSTM layer.
An LSTM layer with $q_{1}$ units is obtained by the mapping, for $u \geq 1$,

$$
\boldsymbol{z}^{(1)}: \mathbb{R}^{q \times q_{1} \times q_{1}} \rightarrow \mathbb{R}^{q_{1} \times q_{1}}, \quad\left(\boldsymbol{X}_{u}, \boldsymbol{z}_{u-1}^{(1)}, \boldsymbol{c}_{u-1}^{(1)}\right) \mapsto\left(\boldsymbol{z}_{u}^{(1)}, \boldsymbol{c}_{u}^{(1)}\right)
$$

where $\boldsymbol{z}_{u}^{(1)}$ is called hidden state and $\boldsymbol{c}_{u}^{(1)}$ is the memory cell.
At each timestep, the LSTM layer takes the current input $\boldsymbol{X}_{u}$, the previous state $\boldsymbol{z}_{u-1}^{(1)}$, and the previous memory cell $\boldsymbol{c}_{u-1}^{(1)}$. These inputs are used to compute the two outputs of the LSTM layer:

- The updated hidden state

$$
\boldsymbol{z}_{u}^{(1)}=\boldsymbol{o}_{u}^{(1)} \odot \phi\left(\boldsymbol{c}_{u}^{(1)}\right) \in \mathbb{R}^{q_{1}}
$$

where $\odot$ is the Hadamard product, which applies elementwise multiplication, and the activation fucntion $\phi$ is applied elementwise. The output gate $\boldsymbol{o}_{u}^{(1)}$ dynamically regulates how much of the transformed memory cell $\phi\left(\boldsymbol{c}_{u}^{(1)}\right)$ is outputted.

- The updated memory cell

$$
\boldsymbol{c}_{u}^{(1)}=\boldsymbol{f}_{u}^{(1)} \odot \boldsymbol{c}_{u-1}^{(1)}+\boldsymbol{i}_{u}^{(1)} \odot \tilde{\boldsymbol{c}}_{u}^{(1)} \in \mathbb{R}^{q_{1}}
$$

with forget gate $\boldsymbol{f}_{u}^{(1)}$, input gate $\boldsymbol{i}_{u}^{(1)}$, and candidate new memory cell $\tilde{\boldsymbol{c}}_{u}^{(1)}$.
The three gates and candidate new memory cell are defined by

$$
\begin{aligned}
\boldsymbol{f}_{u}^{(1)} & =\sigma\left(\boldsymbol{w}_{0, f}^{(1)}+W_{f}^{(1)} \boldsymbol{X}_{u}+V_{f}^{(1)} \boldsymbol{z}_{u-1}^{(1)}\right) \in(0,1)^{q_{1}} \\
\boldsymbol{i}_{u}^{(1)} & =\sigma\left(\boldsymbol{w}_{0, i}^{(1)}+W_{i}^{(1)} \boldsymbol{X}_{u}+V_{i}^{(1)} \boldsymbol{z}_{u-1}^{(1)}\right) \in(0,1)^{q_{1}} \\
\boldsymbol{o}_{u}^{(1)} & =\sigma\left(\boldsymbol{w}_{0, o}^{(1)}+W_{o}^{(1)} \boldsymbol{X}_{u}+V_{o}^{(1)} \boldsymbol{z}_{u-1}^{(1)}\right) \in(0,1)^{q_{1}} \\
\tilde{\boldsymbol{c}}_{u}^{(1)} & =\tanh \left(\boldsymbol{w}_{0, c}^{(1)}+W_{c}^{(1)} \boldsymbol{X}_{u}+V_{c}^{(1)} \boldsymbol{z}_{u-1}^{(1)}\right) \in(-1,1)^{q_{1}}
\end{aligned}
$$

with biases $\boldsymbol{w}_{0, f}^{(1)}, \boldsymbol{w}_{0, i}^{(1)}, \boldsymbol{w}_{0, o}^{(1)}, \boldsymbol{w}_{0, c}^{(1)} \in \mathbb{R}^{q_{1}}$, network weights $W_{f}^{(1)}, W_{i}^{(1)}, W_{o}^{(1)}, W_{c}^{(1)} \in \mathbb{R}^{q_{1} \times q}$ and $V_{f}^{(1)}, V_{i}^{(1)}, V_{o}^{(1)}, V_{c}^{(1)} \in \mathbb{R}^{q_{1} \times q_{1}}$. These gates work together to dynamically regulate the flow of information into, out of, and within the cell. During training, the parameters of the LSTM layer are adjusted to optimize this gating mechanism. The total number of weights in an LSTM layer is given by $4 q_{1}\left(q+q_{1}+1\right)$.
A graphical illustration of the LSTM layer is shown in Figure 8.10. This diagram highlights the flow of data through the gates and the interaction between the memory cell and the hidden state over time.

## Page 149
Figure 8.10: Graphical representation of a LSTM unit.

# 8.4.3 Gated recurrent unit networks 

The GRU networks of Cho et al. [42] have emerged as a promising alternative to LSTM networks. Although GRUs were developed more recently, they offer a simplified architecture compared to LSTMs, making them computationally more efficient while still addressing the issue of vanishing gradients that traditional RNNs face. Unlike LSTMs, GRUs do not have an explicit memory cell. Instead, they rely on two gates: the update gate and the reset gate. The first determines how much of the previous hidden state should be carried forward, essentially controlling the flow of information. The second one, on the other hand, decides how much of the previous information should be discarded when generating the current state. This design simplifies the architecture while still allowing it to capture long-term dependencies. In essence, GRUs can be seen as a more compact version of LSTMs, offering similar benefits in terms of handling long-range dependencies but with fewer parameters.

GRU layer. Choose weights $W_{o}^{(1)}, W_{r}^{(1)}, W_{z}^{(1)} \in \mathbb{R}^{q_{1} \times q}$ and $V_{o}^{(1)}, V_{r}^{(1)}, V_{z}^{(1)} \in \mathbb{R}^{q_{1} \times q_{1}}$, and biases $\boldsymbol{w}_{0, o}^{(1)}, \boldsymbol{w}_{0, r}^{(1)}, \boldsymbol{w}_{0, z}^{(1)} \in \mathbb{R}^{q_{1}}$. The output of the $q_{1}$-dimensional GRU layer is determined as follows

$$
\boldsymbol{z}_{u}^{(1)}=\left(1-\boldsymbol{o}_{u}^{(1)}\right) \odot \boldsymbol{z}_{u-1}^{(1)}+\boldsymbol{o}_{u}^{(1)} \odot \hat{\boldsymbol{z}}_{u}^{(1)}
$$

This equation defines the hidden state $\boldsymbol{z}_{u}^{(1)}$ at time step $u$, which is a weighted combination of the previous hidden state $\boldsymbol{z}_{u-1}^{(1)}$ and the candidate state $\hat{\boldsymbol{z}}_{u}^{(1)}$. The balance between these two components is controlled by the state of the update gate $\boldsymbol{o}_{u}^{(1)}$, which determines how much of the previous state should be retained and how much of the new information should be incorporated. The states $\boldsymbol{o}_{u}^{(1)}$ and $\hat{\boldsymbol{z}}_{u}^{(1)}$, with $\hat{\boldsymbol{z}}_{u}^{(1)}$ further influenced by the
![Page 149 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p149_img1.jpg)

## Page 150
reset gate $\boldsymbol{r}_{u}^{(1)}$, are expressed as follows

$$
\begin{aligned}
\boldsymbol{o}_{u}^{(1)} & =\sigma\left(\boldsymbol{w}_{0, o}^{(1)}+W_{o}^{(1)} \boldsymbol{X}_{u}+V_{o}^{(1)} \boldsymbol{z}_{u-1}^{(1)}\right) \in(0,1)^{q_{1}} \\
\boldsymbol{r}_{u}^{(1)} & =\sigma\left(\boldsymbol{w}_{0, r}^{(1)}+W_{r}^{(1)} \boldsymbol{X}_{u}+V_{r}^{(1)} \boldsymbol{z}_{u-1}^{(1)}\right) \in(0,1)^{q_{1}} \\
\tilde{\boldsymbol{z}}_{u}^{(1)} & =\tanh \left(\boldsymbol{w}_{0, z}^{(1)}+W_{z}^{(1)} \boldsymbol{X}_{u}+V_{z}^{(1)}\left(\boldsymbol{r}_{u}^{(1)} \odot \boldsymbol{z}_{u-1}^{(1)}\right)\right) \in(-1,1)^{q_{1}}
\end{aligned}
$$

The number of weights in a GRU layer with $q_{1}$ units, equal to $3 q_{1}\left(q+q_{1}+1\right)$, is lower compared to the number of parameters in a LSTM layer with the same number of units.

# 8.4.4 Deep recurrent neural networks and conclusion 

RNN layers, including LSTM and GRU layers, can be stacked to form deep RNNs. Note that we have carefully used upper indices ${ }^{(1)}$ in all notation above to indicate a first RNN layer. Such layers can now be composed. The way of designing deep RNN structures is not unique, and different approaches can be considered. The following gives a proposal for a RNN of depth $d=2$. At each time step $1 \leq u \leq t$, consider the recurrent structure

$$
\begin{aligned}
\boldsymbol{z}_{u}^{(1)} & =\boldsymbol{z}^{(1)}\left(\boldsymbol{X}_{u}, \boldsymbol{z}_{u-1}^{(1)}\right) \\
\boldsymbol{z}_{u}^{(2)} & =\boldsymbol{z}^{(2)}\left(\boldsymbol{z}_{u}^{(1)}, \boldsymbol{z}_{u-1}^{(2)}\right)
\end{aligned}
$$

where $\boldsymbol{z}_{u}^{(2)}$ represents the state of the second RNN layer at time $u$. Of course, this can be generalized to any depth $d \geq 2$.
In the deep LSTM case, we consider for the $m$-th RNN layer, $m \geq 1$,

$$
\boldsymbol{z}^{(m)}: \mathbb{R}^{q_{m-1} \times q_{m} \times q_{m}} \rightarrow \mathbb{R}^{q_{m} \times q_{m}}, \quad\left(\boldsymbol{z}_{u}^{(m-1)}, \boldsymbol{z}_{u-1}^{(m)}, \boldsymbol{c}_{u-1}^{(m)}\right) \mapsto\left(\boldsymbol{z}_{u}^{(m)}, \boldsymbol{c}_{u}^{(m)}\right)
$$

where we initialize the input for $m=1$ by $\boldsymbol{z}_{u}^{(0)}=\boldsymbol{X}_{u}$ and $q_{0}=q$.
We conclude this RNN chapter with some remarks.

- Deep RNN architectures, like the LSTM layers (8.23), consider the entire return sequence $\left(\boldsymbol{z}_{u}^{(m-1)}\right)_{u=1}^{t}$ of the previous RNN layer $m-1$. For predicting a response $Y_{t}$, in the last time period $t$, one typically only extracts the last state $\boldsymbol{z}_{t}^{(d)} \in \mathbb{R}^{q_{d}}$ in the last RNN layer $m=d$. This can then be concatenated with other covariate information, see Figure 8.3.
- Following up on the previous item, if one wants to process the entire return sequence $\left(\boldsymbol{z}_{u}^{(d)}\right)_{u=1}^{t}$ of the last RNN layer $m=d$, one typically needs to flatten this return sequence to further process it, see Section 8.3.7 for flatten layers.
- The previous examples have all been dealing with information $\boldsymbol{X}_{1: t}$ of equal length $t$. However, RNN can process information of any length, if only the last state $\boldsymbol{z}_{t}^{(d)} \in \mathbb{R}^{q_{d}}$ is extracted. For example, we can have insurance policyholders $1 \leq i \leq n$ with claims histories of different lengths $\boldsymbol{X}_{\tau_{i}: t}$, where $\tau_{i} \in\{1, \ldots, t-1\}$ is the starting point of the history of policyholder $i$. This can easily be handled by RNNs.

## Page 151
# 8.5 Transformers 

Transformers are a class of deep learning architectures that have revolutionized natural language processing (NLP) and they are at core of the great success of large language models (LLMs). Introduced by Vaswani et al. [228], these models replace traditional recurrent and convolutional structures with attention mechanisms. These attention mechanisms use weighting schemes to identify and prioritize the most relevant information and their interactions. While originally developed for tasks involving data with a sequential structure, transformers have been adapted to tabular input data, increasing the potential of these models in actuarial science. First applications of transformers for tabular data were considered by Huang et al. [106] and Brauer [26]. In their work, continuous and categorical information is tokenized and embedded so that this pre-processed input information has a 2D tensor structure, making them suitable to enter a transformer; see also the feature tokenizer transformer (FTT) of Gorishniy et al. [86]. More recently, Richman et al. [188] advanced transformer-based models for tabular data by incorporating a novel weighting scheme inspired by the credibility mechanism of Bühlmann's seminal work $[34,36]$.

### 8.5.1 Basic components of transformers

Transformers are sophisticated architectures that combine multiple layers. Before illustrating specific transformer architectures, we describe the key layers that serve as the building blocks for these advanced models.

## Attention layer

The core of transformers is the attention layer, which is designed to identify the most relevant information in the input data. The central idea is to learn a weighting scheme that prioritizes the most important parts of the input, thereby enhancing the model's ability to perform a given predictive task.
Different attention mechanisms are available in the literature. Our focus is on the most commonly used variant, the scaled dot-product attention of Vaswani et al. [228]. To illustrate this attention mechanism, we consider three matrices $Q, K, V \in \mathbb{R}^{t \times q}$ of the same dimensions. These three matrices represent the query, the key, and the value, respectively, of the attention mechanism.
The scaled dot-product attention mechanism is given by the mapping, called attention head,

$$
H: \mathbb{R}^{(t \times q) \times(t \times q) \times(t \times q)} \rightarrow \mathbb{R}^{t \times q}, \quad(Q, K, V) \mapsto H=H(Q, K, V)
$$

The attention mechanism is applied to the value matrix $V$, with the output $H$ calculated as a weighted sum of its elements. The (attention) weights, dependent on the query matrix $Q$ and the key matrix $K$, are computed through a scalar/dot-product multiplication, followed by the softmax function to normalize the scores

$$
H=A V=\operatorname{softmax}\left(\frac{Q K^{\top}}{\sqrt{q}}\right) V \in \mathbb{R}^{t \times q}
$$

## Page 152
Here, $q$ is a scaling factor which tries to make the matrices free of the input dimension $q$, while the matrix of scores $A \in \mathbb{R}^{t \times t}$ is derived from the matrix $A^{\prime}=Q K^{\top} / \sqrt{q}$ by applying the softmax operator to the rows of $A^{\prime}$

$$
A=\operatorname{softmax}\left(A^{\prime}\right), \quad \text { where } \quad a_{u, s}=\frac{\exp \left(a_{u, s}^{\prime}\right)}{\sum_{k=1}^{t} \exp \left(a_{u, k}^{\prime}\right)} \in(0,1)
$$

for $1 \leq u, s \leq t$. This transformation ensures that the elements of each row of the matrix $A$ sum to one. To provide some intuition: the learned attention scores in $A$ are multiplied by the value vectors in $V$. Each row of the resulting matrix $A V$ is a weighted average of the vectors in $V$, where the weights, which sum to one, determine the (relative) importance of each row vector in $V$. It is important to note that the scaled dot-product attention mechanism is highly efficient computationally, as it performs matrix operations, such as dot-products and softmax, in parallel across all queries, keys and values. This eliminates the need for recursive or sequential computation, making it particularly wellsuited for implementation on Graphics Processing Units (GPUs).

Let us briefly illustrate the attention mechanism implied by the query $Q$ and the key $K$. These two matrices can be express by

$$
Q=\left[\boldsymbol{q}_{1}, \ldots, \boldsymbol{q}_{t}\right]^{\top} \in \mathbb{R}^{t \times q} \quad \text { and } \quad K=\left[\boldsymbol{k}_{1}, \ldots, \boldsymbol{k}_{t}\right]^{\top} \in \mathbb{R}^{t \times q}
$$

with row vectors $\boldsymbol{q}_{s}, \boldsymbol{k}_{s} \in \mathbb{R}^{q}, 1 \leq s \leq t$. The elements $a_{u, s}^{\prime}$ of matrix $A^{\prime}$ are given by

$$
a_{u, s}^{\prime}=\frac{1}{\sqrt{q}} \boldsymbol{q}_{u}^{\top} \boldsymbol{k}_{s}=\frac{1}{\sqrt{q}}\left\langle\boldsymbol{q}_{u}, \boldsymbol{k}_{s}\right\rangle
$$

From this we conclude that if the query $\boldsymbol{q}_{u}$ points in the same direction as the key $\boldsymbol{k}_{s}$, we receive a large attention weight $a_{u, s}$ (supposed all queries and keys have roughly the same absolute values). This then implies that the corresponding entries on the $s$-th row of the value matrix $V$ get a large attention (weight).

Figure 8.11: Construction of attention matrix $A$ using transposed query matrix $Q^{\top}$ (in blue) and key matrix $K^{\top}$ (in yellow).

Figure 8.11 illustrates the scalar products (8.26). Basically, every query $\boldsymbol{q}_{u}$ tries to find the keys $\boldsymbol{k}_{s}$ that provide a large scalar product (8.26), which is mapped to a large
![Page 152 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p152_img1.jpg)

## Page 153
attention weight $a_{u, s}$; this is related to the cosine similarity mentioned in the footnote on page 131 .

# Time-distributed layer 

Transformer architectures generally include time-distributed layers, which process sequential data by applying the same transformation to each time step. The transformation can be any type of neural network layer, such as a FNN or a CNN layer; however, the most of the transformer models utilize time-distributed FNN layers. Consider a time-distributed FNN layer with $q_{1}$ units applied to the input tensor $\boldsymbol{X}_{1: t} \in \mathbb{R}^{t \times q}$. This performs the following mapping

$$
\boldsymbol{z}^{t-\mathrm{FNN}}: \mathbb{R}^{t \times q} \rightarrow \mathbb{R}^{t \times q_{1}}, \quad \boldsymbol{X}_{1: t} \mapsto \boldsymbol{z}^{t-\mathrm{FNN}}\left(\boldsymbol{X}_{1: t}\right)=\left(\boldsymbol{z}^{\mathrm{FNN}}\left(\boldsymbol{X}_{1}\right), \ldots, \boldsymbol{z}^{\mathrm{FNN}}\left(\boldsymbol{X}_{t}\right)\right)^{\top}
$$

where $\boldsymbol{z}^{\mathrm{FNN}}: \mathbb{R}^{q} \rightarrow \mathbb{R}^{q_{1}}$ is a FNN layer. This transformation leaves the time dimension $t$ unchanged, as the FNN layer $\boldsymbol{z}^{\mathrm{FNN}}$ is applied separately to each time step $1 \leq u \leq t$. Importantly, the same parameters (network weights and biases) are shared across all time steps. This invariance across time steps is what makes the layer time-distributed.

## Drop-out layer

Drop-out is a widely used regularization technique in neural networks introduced in Srivastava et al. [210] and Wager et al. [229]; we have already met drop-out in Section 5.3.6. It works by randomly ignoring a subset of neurons (units) during the training process, to enhance the model's generalization capabilities. This is typically implemented by multiplying the output of a specific layer by i.i.d. realizations of Bernoulli random variables with a fixed drop-out rate $\alpha \in(0,1)$ in each step of SGD training.

A drop-out layer can be expressed as

$$
\boldsymbol{z}^{\mathrm{drop}}: \mathbb{R}^{q} \rightarrow \mathbb{R}^{q}, \quad \boldsymbol{X} \mapsto \boldsymbol{z}^{\mathrm{drop}}(\boldsymbol{X})=\boldsymbol{Z} \odot \boldsymbol{X}
$$

where $\boldsymbol{Z}=\left(Z_{1}, Z_{2}, \ldots, Z_{q}\right)^{\top} \in\{0,1\}^{q}$ is a vector of i.i.d. Bernoulli random variables that are resampled in each SGD step, and $\odot$ is the elementwise Hadamard product.

## Layer normalization

Layer normalization, introduced by Ba et al. [9], is a technique used to stabilize the learning process, to accelerate convergence, and to improve the model's predictive performance. For this kind of layer, normalization is applied to the inputs within a single layer, in contrast to batch normalization of Ioffe-Szegedy [107].
Mathematically, layer normalization is a mapping

$$
\boldsymbol{z}^{\text {norm }}: \mathbb{R}^{q} \rightarrow \mathbb{R}^{q}, \quad \boldsymbol{X} \mapsto \boldsymbol{z}^{\text {norm }}(\boldsymbol{X})=\left(\gamma_{j}\left(\frac{X_{j}-\bar{X}}{\sqrt{\sigma^{2}+\epsilon}}\right)+\delta_{j}\right)_{1 \leq j \leq q}
$$

## Page 154
where $\epsilon>0$ is a small constant added for numerical stability, $\mu \in \mathbb{R}$ and $\sigma \in \mathbb{R}^{+}$are calculated as follows

$$
\bar{X}=\frac{1}{q} \sum_{j=1}^{q} X_{j} \quad \text { and } \quad \sigma^{2}=\frac{1}{q} \sum_{j=1}^{q}\left(X_{j}-\bar{X}\right)^{2}
$$

and $\boldsymbol{\gamma}=\left(\gamma_{1}, \ldots, \gamma_{q}\right)^{\top} \in \mathbb{R}^{q}$ and $\boldsymbol{\delta}=\left(\delta_{1}, \ldots, \delta_{q}\right)^{\top} \in \mathbb{R}^{q}$ are vectors of trainable parameters.

# 8.5.2 Transformers for sequential data 

We are now ready to introduce the attention head and the transformer layer in detail. In this section, we discuss transformers designed for sequential data.

## Transformer layer

Consider input data with a sequential structure (time-series) represented as a tensor $\boldsymbol{X}_{1: t} \in \mathbb{R}^{t \times q}$. The first foundational component of the transformer model is the attention layer ${ }^{5}$. To implement the attention mechanism on the input data $\boldsymbol{X}_{1: t}$, we first need to derive the query, key and value matrices $Q, K$ and $V$, respectively. For this, we select three time-distributed $q$-dimensional FNN layers

$$
\boldsymbol{z}_{j}^{\mathrm{t}-\mathrm{FNN}}: \mathbb{R}^{t \times q} \rightarrow \mathbb{R}^{t \times q}, \quad \boldsymbol{X}_{1: t} \mapsto \boldsymbol{z}_{j}^{\mathrm{t}-\mathrm{FNN}}\left(\boldsymbol{X}_{1: t}\right)
$$

for $j \in\{Q, K, V\}$. These provide us with the time-slices for fixed time points $1 \leq u \leq t$, see $(8.27)$,

$$
\begin{aligned}
& \boldsymbol{q}_{u}=\boldsymbol{z}_{Q}^{\mathrm{FNN}}\left(\boldsymbol{X}_{u}\right)=\phi_{Q}\left(\boldsymbol{w}_{0}^{(Q)}+W_{Q} \boldsymbol{X}_{u}\right) \in \mathbb{R}^{q} \\
& \boldsymbol{k}_{u}=\boldsymbol{z}_{K}^{\mathrm{FNN}}\left(\boldsymbol{X}_{u}\right)=\phi_{K}\left(\boldsymbol{w}_{0}^{(K)}+W_{K} \boldsymbol{X}_{u}\right) \in \mathbb{R}^{q} \\
& \boldsymbol{v}_{u}=\boldsymbol{z}_{V}^{\mathrm{FNN}}\left(\boldsymbol{X}_{u}\right)=\phi_{V}\left(\boldsymbol{w}_{0}^{(V)}+W_{V} \boldsymbol{X}_{u}\right) \in \mathbb{R}^{q}
\end{aligned}
$$

with corresponding network weights, biases and activation functions. Writing this in matrix notation gives us the query, key and value matrices

$$
\begin{aligned}
& Q=\boldsymbol{z}_{Q}^{\mathrm{t}-\mathrm{FNN}}\left(\boldsymbol{X}_{1: t}\right)=\left[\boldsymbol{q}_{1}, \ldots, \boldsymbol{q}_{t}\right]^{\top} \in \mathbb{R}^{t \times q} \\
& K=\boldsymbol{z}_{K}^{\mathrm{t}-\mathrm{FNN}}\left(\boldsymbol{X}_{1: t}\right)=\left[\boldsymbol{k}_{1}, \ldots, \boldsymbol{k}_{t}\right]^{\top} \in \mathbb{R}^{t \times q} \\
& V=\boldsymbol{z}_{V}^{\mathrm{t}-\mathrm{FNN}}\left(\boldsymbol{X}_{1: t}\right)=\left[\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{t}\right]^{\top} \in \mathbb{R}^{t \times q}
\end{aligned}
$$

see also Figure 8.11. This allows us to define the attention head implied by input $\boldsymbol{X}_{1: t}$ as follows, see (8.24),

$$
H=H\left(\boldsymbol{X}_{1: t}\right)=\operatorname{softmax}\left(\frac{Q K^{\top}}{\sqrt{q}}\right) V \in \mathbb{R}^{t \times q}
$$

[^0]
[^0]:    ${ }^{5}$ Some authors suggest pre-processing the input by applying layer normalization; however, we omit this step in our notation to keep it as simple as possible.

## Page 155
A transformer layer is constructed by combining the attention head with the augmented input tensor through a skip-connection mechanism

$$
\boldsymbol{X}_{1: t} \mapsto \boldsymbol{z}^{\text {skip }}\left(\boldsymbol{X}_{1: t}\right)=\boldsymbol{X}_{1: t}+H\left(\boldsymbol{X}_{1: t}\right) \in \mathbb{R}^{t \times q}
$$

After the attention mechanism, the transformed input is typically processed through a series of additional layers. Generally, a normalization layer $\boldsymbol{z}^{\text {norm }}$ is applied first, followed by a time-distributed FNN layer $\boldsymbol{z}^{\mathrm{t}-\mathrm{FNN}}$ having output dimension $q$.
In this setting, the output of the transformer layer can be expressed as

$$
\boldsymbol{z}^{\text {trans }}\left(\boldsymbol{X}_{1: t}\right)=\boldsymbol{z}^{\text {skip }}\left(\boldsymbol{X}_{1: t}\right)+\left(\boldsymbol{z}^{\mathrm{t}-\mathrm{FNN}} \circ \boldsymbol{z}^{\text {norm }}\right)\left(\boldsymbol{z}^{\text {skip }}\left(\boldsymbol{X}_{1: t}\right)\right)
$$

based on skip-connection (8.29) and on attention head (8.28).
More layers can be employed at this stage to further enhance the model's flexibility. Moreover, drop-out layers can be included to regularize the network and mitigate the risk of overfitting.

The layers described in (8.30) operate on the original input $\boldsymbol{X}_{1: t}$, and this can be formalized to the transformer layer

$$
\boldsymbol{z}^{\text {trans }}: \mathbb{R}^{t \times q} \rightarrow \mathbb{R}^{t \times q}, \quad \boldsymbol{X}_{1: t} \mapsto \boldsymbol{z}^{\text {trans }}\left(\boldsymbol{X}_{1: t}\right)
$$


Figure 8.12: Graphical representation of a transformer architecture.
Figure 8.12 illustrates the transformer layer (8.30)-(8.31). The input $\boldsymbol{X}_{1: t}$ corresponds to the blue box and the output $\boldsymbol{z}^{\text {trans }}\left(\boldsymbol{X}_{1: t}\right)$ to the yellow box, and the feature extraction by the transformer layer is sketch in the magenta box.

# Multi-head transformers 

A transformer layer can also have multiple attention heads, allowing the model to focus on different parts of the input sequence simultaneously. Rather than computing a single
![Page 155 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p155_img1.jpg)

## Page 156
attention output, multi-head attention applies the attention mechanism multiple times in parallel, with each attention head using different weights and parameters. That is, each attention head operates on a separate set of query, key and value matrices, producing multiple output tensors. These output tensors are then concatenated and projected once more to generate the final attention result.
Formally, we can define the multi-head attention mechanism with $n_{h}$ attention heads as follows. For each head $j$, we apply the attention mechanism to the input tensor $\boldsymbol{X}_{1: t}$ to obtain the matrices $Q_{j}, K_{j}, V_{j}$, which are derived from separate projections of the input tensor. This gives attention heads for $1 \leq j \leq n_{h}$

$$
H_{j}\left(\boldsymbol{X}_{1: t}\right)=\operatorname{softmax}\left(\frac{Q_{j} K_{j}^{\top}}{\sqrt{q}}\right) V_{j} \in \mathbb{R}^{t \times q}
$$

These attention head outputs are concatenated along the feature dimension, yielding the multi-head $(\mathrm{MH})$ attention output

$$
H_{\mathrm{MH}}\left(\boldsymbol{X}_{1: t}\right)=\operatorname{Concat}\left(H_{1}\left(\boldsymbol{X}_{1: t}\right), H_{2}\left(\boldsymbol{X}_{1: t}\right), \ldots, H_{n_{h}}\left(\boldsymbol{X}_{1: t}\right)\right) W^{\mathrm{O}} \in \mathbb{R}^{t \times q}
$$

where $W^{\mathrm{O}} \in \mathbb{R}^{h q \times q}$ is the output weight matrix. This multi-head attention output is then incorporated into the subsequent layers, as in the original architecture. Specifically, after computing the multi-head attention output, it is added to the input tensor $\boldsymbol{X}_{1: t}$ using a skip-connection (8.29), followed by normalization and FNN layers (8.30).

# Working with tensors and unstructured data for predictive modeling 

- Bring all data in tensor form using feature tokenization, see Section 8.2.
- The tensors are processed by FNN layers, CNN layers, RNN layers and/or (multi-)head transformer layers, see also Figure 8.3.
- Flatten all outputs of the previous layers to be able to concatenate them to a vector, see Section 8.3.7.
- This vector is further processed through FNN layers to form the output, see Figure 8.3.
- Based on the training, validation and test split, $(\mathcal{U}, \mathcal{V}, \mathcal{T})$, we train this architecture using a strictly consistent loss function $L$, see Section 5.3.

Remark 8.2 (RNN vs. transformer). We close this section with a remark highlighting a key difference between RNN layers and transformer layers. RNN layers have a natural notion of time/position because RNN layers move sequentially across the time-series data $\boldsymbol{X}_{1: t}$. In contrast, attention layers do not respect time-causality, in the sense that any query $\boldsymbol{q}_{u}$ can communicate with any key $\boldsymbol{k}_{s}$ through (8.26). To make transformers aware of time, one typically adds a positional encoding to the input tensor, meaning that, e.g., the last column $q$ of $\boldsymbol{X}_{1: t} \in \mathbb{R}^{t \times q}$ contains the (normalized) entries $u / t \in[0,1]$ on the $u$-th row of $\boldsymbol{X}_{1: t}$. This add a notion of time to the algorithm, though, it does not imply that the algorithm will respect time causality. Time causality would only be the case, if queries $\boldsymbol{q}_{u}$ can only communicate with keys $\boldsymbol{k}_{s}$ having occurred before $s \leq u$.

## Page 157
# 8.5.3 Transformers for tabular data 

The transformer architecture discussed above cannot be directly applied to tabular data, which limits its applicability to actuarial problems. Several extensions of transformers for tabular data have been proposed in the literature. We focus on the model proposed by Gorishniy et al. [86]; this has also explored by Brauer [26] in an actuarial context. The key innovation in the architecture of Gorishniy et al. [86] lies in the so-called feature tokenization transformation, which converts the original covariates, both categorical and continuous ones, into a format suitable for being processed by transformer layers.
We consider the raw tabular (vector) input $\boldsymbol{X}$, which comprises both categorical and continuous covariates. Specifically, it includes $q_{c}$ categorical covariates $\left(X_{j}\right)_{j=1}^{c_{q}}$ and $q_{n}=$ $q-q_{c}$ continuous (numerical) covariates $\left(X_{j}\right)_{j=c_{q}+1}^{q}$. We embed both types of covariates into a $b$-dimensional Euclidean space $\mathbb{R}^{b}$, where $b$ is an integer (hyper-parameter) that needs to be selected by the modeler; in fact, this is precisely the embedding dimension as introduced in (2.15) and (8.1). We apply a $b$-dimensional entity embedding to each categorical covariate $X_{j}, 1 \leq j \leq q_{c}$, given by

$$
\boldsymbol{e}_{j}^{\mathrm{EE}}: \mathcal{A}_{j} \rightarrow \mathbb{R}^{b}, \quad X_{j} \mapsto \boldsymbol{e}_{j}^{\mathrm{EE}}:=\boldsymbol{e}_{j}^{\mathrm{EE}}\left(X_{j}\right)
$$

where $\mathcal{A}_{j}$ denotes the levels of categorical covariate $X_{j}$. Note that for every categorical covariate we use the same embedding dimension $b$. This results in $b \sum_{j=1}^{q_{c}}\left|\mathcal{A}_{j}\right|$ embedding weights that need to be learned.
For the continuous covariates $X_{j}, q_{c}+1 \leq j \leq q$, we also perform a $b$-dimensional embedding. For this we select FNNs. for $q_{c}+1 \leq j \leq q$, providing

$$
\boldsymbol{z}_{j}: \mathbb{R} \rightarrow \mathbb{R}^{b}, \quad X_{j} \mapsto \boldsymbol{z}_{j}:=\boldsymbol{z}_{j}\left(X_{j}\right)
$$

This uses $(b+1) *\left(q-q_{c}\right)$ network weights that need to be learned.
After processing both categorical and continuous covariates to $b$-dimensional embeddings, we collect all these embeddings in a tensor

$$
\boldsymbol{X}_{1: q}^{\circ}=\left[\boldsymbol{e}_{1}^{\mathrm{EE}}, \ldots, \boldsymbol{e}_{q_{c}}^{\mathrm{EE}}, \boldsymbol{z}_{q_{c}+1}, \ldots, \boldsymbol{z}_{q}\right]^{\top} \in \mathbb{R}^{q \times b}
$$

This tensor $\boldsymbol{X}_{1: q}^{\circ}$ contains the transformed covariate information, and it serves as input to subsequent layers in our model. It is further augmented by introducing an additional component, the so-called the classification (CLS) token. This additional component is inspired by the bidirectional encoder representations from transformers (BERT) architecture discussed in Devlin et al. [55]. The purpose of the CLS token is to encode every column $1 \leq k \leq b$ of the input tensor $\boldsymbol{X}_{1: q}^{\circ} \in \mathbb{R}^{q \times b}$ into a single variable.

This results in the augmented input tensor

$$
\boldsymbol{X}_{1: q+1}=\left[\begin{array}{c}
\boldsymbol{X}_{1: q}^{\circ} \\
\boldsymbol{c}^{\top}
\end{array}\right]=\left[\boldsymbol{e}_{1}^{\mathrm{EE}}, \ldots, \boldsymbol{e}_{q_{c}}^{\mathrm{EE}}, \boldsymbol{z}_{q_{c}+1}, \ldots, \boldsymbol{z}_{q}, \boldsymbol{c}\right]^{\top} \in \mathbb{R}^{(q+1) \times b}
$$

where $\boldsymbol{c}=\left(c_{1}, c_{2}, \ldots, c_{b}\right)^{\top} \in \mathbb{R}^{b}$ denotes the CLS token. Each of the scalars $c_{k} \in \mathbb{R}$ comprising the CLS token, $1 \leq k \leq b$, will encode one column of the input tensor $\boldsymbol{X}_{1: q}^{\circ} \in \mathbb{R}^{q \times b}$, i.e., it will provide a one-dimensional projection of the corresponding $k$-th

## Page 158
Figure 8.13: Transposed augmented input tensor $\boldsymbol{X}_{1: q+1}^{\top}$.
$q$-dimensional vector to a scalar $c_{k} \in \mathbb{R}$, this is illustrated in Figure 8.13 by the yellow CLS token $\boldsymbol{c}$.
For further processing, only the information contained in the CLS token $\boldsymbol{c}$ will be forwarded to make predictions, as it reflects a compressed (encoded) version of the entire tensor information (after training of course). The augmented tensor $\boldsymbol{X}_{1: q+1}$ serves as the input to a transformer layer (8.31), that is,

$$
\boldsymbol{z}^{\text {trans }}: \mathbb{R}^{(q+1) \times b} \rightarrow \mathbb{R}^{(q+1) \times b}, \quad \boldsymbol{X}_{1: q+1} \mapsto \boldsymbol{z}^{\text {trans }}\left(\boldsymbol{X}_{1: q+1}\right)
$$

This mapping can also be implemented using the multi-head attention mechanism. Predictions are derived considering only the final row of the output tensor $\boldsymbol{z}^{\text {trans }}\left(\boldsymbol{X}_{1: q+1}\right)$, which corresponds to the position of the CLS token before the transformer layer is applied. Let $\boldsymbol{c}^{\text {trans }}(\boldsymbol{X}):=\boldsymbol{z}_{q+1}^{\text {trans }}\left(\boldsymbol{X}_{1: q+1}\right) \in \mathbb{R}^{b}$ denote the CLS token after being processed by the transformer layer. It encodes the tokenized information of the input covariates. Through the attention mechanism within the transformer layer, interactions between all covariates are captured and integrated into the CLS token. As a result, $\boldsymbol{c}^{\text {trans }}(\boldsymbol{X})$ becomes a optimized representation of the raw tabular input data $\boldsymbol{X}$

$$
\boldsymbol{X} \mapsto \boldsymbol{c}^{\text {trans }}(\boldsymbol{X})
$$

The final step involves decoding this tokenized variable $\boldsymbol{c}^{\text {trans }}(\boldsymbol{X})$ into a set of covariates suitable for predicting the response variable $Y$. This decoding process is problem-specific. For instance, Gorishniy et el. [86] used layer normalization, followed by a ReLU activation and a one-dimensional FNN layer with linear activation, such that

$$
\boldsymbol{X} \mapsto \mu^{\text {trans }}(\boldsymbol{X})=\boldsymbol{z}^{\mathrm{FNN}}\left(\operatorname{ReLU}\left(\boldsymbol{z}^{\text {norm }}\left(\boldsymbol{c}^{\text {trans }}(\boldsymbol{X})\right)\right)\right)
$$

Of course, for claims counts and claims size modeling we would rather consider a different architecture, having a the log-link for $g^{-1}$ to ensure positivity, see Section 5.1. Figure 8.14 graphically illustrates all the blocks constituting the transformer architecture described above.

# 8.5.4 The credibility transformer 

Recently, Richman et al. [188] proposed an extension of the standard transformer model for tabular data, designed to align more closely with the actuarial concept of credibility. Specifically, it introduces a credibility mechanism into the transformer architecture,
![Page 158 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p158_img1.jpg)

## Page 159
Figure 8.14: Graphical representation of the transformer architecture for tabular data.
which is inspired by the seminal work of Bühlmann [34] and Bühlmann-Straub [36]; this new architecture was named the credibility transformer (CT). The resulting architecture presents some modifications to enhance model flexibility and to fully leverage the benefits of the credibility mechanism.

# Positional encodings 

The first modification concerns the input tensor (8.33). Additional positional encodings were added, this is a common modification for transformers to capture the notion of time and/or position. However, unlike the sequential data typically processed by traditional transformers, tabular data lacks a natural ordering. Indeed, in this context, positional encodings are adapted to encode information specific to the covariates, ensuring the model can receive additional information about the structure of the tabular data.
While sophisticated positional encoding mechanisms exist, such as the sine-cosine encoding scheme proposed by Vaswani [228], the CT architecture adopts a simpler approach based on embedding layers. More formally, the embedding layer maps the position of each covariate $j \in\{1, \ldots, q\}$ into a $b$-dimensional representation inducing the mapping

$$
\boldsymbol{e}^{\mathrm{pos}}:\{1, \ldots, q\} \rightarrow \mathbb{R}^{b}, \quad j \mapsto \boldsymbol{e}_{j}^{\mathrm{pos}}:=\boldsymbol{e}^{\mathrm{pos}}(j)
$$

This positional encoding scheme introduces $q b$ additional parameters. These learned representations are incorporated to augment the input tensor (8.33) obtained from the feature tokenization transformation of the original covariates and the CLS token. In this context, the augmented input tensor is represented as

$$
\boldsymbol{X}_{1: q+1}^{+}=\left[\begin{array}{c}
\boldsymbol{X}_{1: q}^{\circ} \\
\boldsymbol{c}_{1}
\end{array}\left(\begin{array}{c}
\left(\boldsymbol{e}_{1}^{\mathrm{pos}}\right)^{\top} \\
\vdots \\
\left(\boldsymbol{e}_{q}^{\mathrm{pos}}\right)^{\top}
\end{array}\right)\right] \in \mathbb{R}^{(q+1) \times 2 b}
$$
![Page 159 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p159_img1.jpg)

## Page 160
where the enlarged CLS token is now defined as $\boldsymbol{c}=\left(\boldsymbol{c}_{1}^{\top}, \boldsymbol{c}_{2}^{\top}\right)^{\top}=\left(c_{1}, \ldots, c_{2 b}\right)^{\top} \in \mathbb{R}^{2 b}$. It is worth noting that the use of positional encoding increases the size of both the augmented input tensor and the CLS token. A detailed discussion on the benefits of incorporating positional encoding schemes can be found in Huang et al. [106]. This augmented input tensor extended by the positional encoding is shown in Figure 8.15, and it should be compared to Figure 8.13.

Figure 8.15: Transposed augmented input tensor with positional encoding $\left(\boldsymbol{X}_{1: q+1}^{+}\right)^{\top}$.

# Transformer layer 

The augmented tensor $\boldsymbol{X}_{1: q+1}^{+}$represents the input to the standard transformer architecture. Considering a single transformer layer, we have a mapping

$$
\boldsymbol{z}^{\text {trans }}: \mathbb{R}^{(q+1) \times 2 b} \rightarrow \mathbb{R}^{(q+1) \times 2 b}, \quad \boldsymbol{X}_{1: q+1}^{+} \mapsto \boldsymbol{z}^{\text {trans }}\left(\boldsymbol{X}_{1: q+1}^{+}\right)
$$

Within the transformer layer, the CT architecture of Richman et al. [188] introduces some differences compared to the standard layer (8.30). Specifically, it incorporates additional time-distributed FNN and normalization layers to increase the model's flexibility. Starting from $\boldsymbol{z}^{\text {skip }}\left(\boldsymbol{X}_{1: T+1}^{+}\right)$obtained as in (8.29), the output of the transformer layer used in the CT architecture is then defined as

$$
\begin{aligned}
& \boldsymbol{z}^{\text {trans }}\left(\boldsymbol{X}_{1: T+1}^{+}\right)=\boldsymbol{z}^{\text {skip }}\left(\boldsymbol{X}_{1: T+1}^{+}\right) \\
& \quad+\left(\boldsymbol{z}^{\text {norm2 }} \circ \boldsymbol{z}^{\text {drop2 }} \circ \boldsymbol{z}^{\text {t-FNN2 }} \circ \boldsymbol{z}^{\text {drop1 }} \circ \boldsymbol{z}^{\text {t-FNN1 }} \circ \boldsymbol{z}^{\text {norm1 }}\right)\left(\boldsymbol{z}^{\text {skip }}\left(\boldsymbol{X}_{1: T+1}^{+}\right)\right)
\end{aligned}
$$

In this process, the tensor is first normalized, resulting in $\boldsymbol{z}^{\text {norm1 }}$, and then processed through a time-distributed FNN layer, denoted as $\boldsymbol{z}^{\text {t-FNN1 }}$, combined with drop-out layer $\boldsymbol{z}^{\text {drop1 }}$. This is followed by a second time-distributed FNN layer, $\boldsymbol{z}^{\text {t-FNN2 }}$, with another drop-out $\boldsymbol{z}^{\text {drop2 }}$. Finally, the process concludes with a second normalization step, $\boldsymbol{z}^{\text {norm2 }}$. The result of these transformations is combined through a second skip-connection, producing an output tensor with shape $\mathbb{R}^{(q+1) \times 2 b}$.

## Prior and transformer-based tokens

The next component of the CT architecture stands out from other models as it focuses on implementing the core credibility mechanism. Unlike Gorishniy et al. [86], which relies
![Page 160 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p160_img1.jpg)

## Page 161
solely on the transformer-tokenized CLS token for predictions, the CT combines two distinct versions of the CLS token through a credibility-based weighting scheme. More precisely, the first version of the CLS token, referred to as the prior, is extracted before the covariates undergo interactions through the attention mechanism. As a result, it reflects the initial representation of the input covariates without any interactions between them. The prior version is extracted from the value matrix $V=\left[\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{q+1}\right]^{\top}$. To ensure that this token is represented exactly in the same embedding space as the outputs of the transformer, it is processed through the same transformations as the transformer layer in equation (8.35), using the same weights.
This gives us the following representation for the prior token

$$
\boldsymbol{c}^{\text {prior }}=\left(\boldsymbol{z}^{\text {norm2 }} \circ \boldsymbol{z}^{\text {drop2 }} \circ \boldsymbol{z}^{\mathrm{FNN} 2} \circ \boldsymbol{z}^{\text {drop1 }} \circ \boldsymbol{z}^{\mathrm{FNN} 1} \circ \boldsymbol{z}^{\text {norm1 }}\right)\left(\boldsymbol{v}_{q+1}\right) \in \mathbb{R}^{2 b}
$$

that is, we use the layers from (8.35), but we do not need its time-distributed versions because we only process a single vector $\boldsymbol{v}_{q+1}$. The second version of the CLS token is derived after processing everything through the transformer layer. This version incorporates the effects of the attention mechanism, reflecting the interactions among the covariates. The second version of the CLS token holds the tokenized information of the covariates $\boldsymbol{X}$ as well as their positional embeddings.
This transformer-based token is given by

$$
\boldsymbol{c}^{\text {trans }}=\boldsymbol{z}_{q+1}^{\text {trans }}\left(\boldsymbol{X}_{1: q+1}^{+}\right) \in \mathbb{R}^{2 b}
$$

which corresponds to the $(q+1)$-st row of $\boldsymbol{z}^{\text {trans }}\left(\boldsymbol{X}_{1: T+1}^{+}\right)$being calculated according to (8.35).

The two tokens, $\boldsymbol{c}^{\text {prior }}$ and $\boldsymbol{c}^{\text {trans }}$, provide two different representations of the data and both can be used for predicting the response variable. The prior token $\boldsymbol{c}^{\text {prior }}$ captures only the initial covariate information, while the transformer-based token $\boldsymbol{c}^{\text {trans }}$ augments this information by incorporating the interactions among the covariates.

# Credibility mechanism 

Both tokens $\boldsymbol{c}^{\text {prior }}$ and $\boldsymbol{c}^{\text {trans }}$ are used for making predictions in the CT architecture, with weights assigned to each representation. This process involves selecting a fixed probability weight, $\alpha \in(0,1)$, and sampling independent Bernoulli random variables $Z \sim \operatorname{Bernoulli}(\alpha)$ during SGD training. These random variables determine which CLS token is passed forward through the network to make predictions.
Specifically, the two tokens are combined as follows by

$$
\boldsymbol{c}^{\text {cred }}=Z \boldsymbol{c}^{\text {trans }}+(1-Z) \boldsymbol{c}^{\text {prior }} \in \mathbb{R}^{2 b}
$$

Thus, in $\alpha \cdot 100 \%$ of the gradient descent steps, the transformer-based token $\boldsymbol{c}^{\text {trans }}$ is used, which has been augmented by covariate interactions. In the remaining $(1-\alpha) \cdot 100 \%$ of the steps, the prior token $\boldsymbol{c}^{\text {prior }}$ is selected. This mechanism effectively assigns a credibility of $\alpha$ to the transformer-based token $\boldsymbol{c}^{\text {trans }}$ and a complementary credibility of $1-\alpha$ to the prior token $\boldsymbol{c}^{\text {prior }}$ in SGD, guiding the network to learn reasonable parameters during

## Page 162
training. This credibility token $\boldsymbol{c}^{\text {cred }}$ then enters an encoder for prediction, similar to (8.34).

The probability $\alpha$ is treated as a hyper-parameter and can be optimized via grid search. One could select $\alpha>1 / 2$ to give greater weight to the tokenized covariate information, reflecting its increased importance in the prediction process; in the examples of Richman et al. [188], the best results have been obtain by a choice of roughly $\alpha=95 \%$.
The credibility mechanism in equation (8.36) is applied only during the SGD fitting. For out-of-sample predictions, one sets $Z \equiv 1$, and uses the transformer-based token.

# The hidden credibility mechanism 

The CT architecture introduces another and less obvious credibility mechanism which is realized during the dot-product attention. To understand how it works, consider that, according to equation (8.28), the last row of the attention head, denoted as $H_{q+1}$, is obtained by multiplying the elements of $A_{q+1}=\left(a_{q+1,1}, \ldots, a_{q+1, q+1}\right)$ with the corresponding columns of the value matrix $V \in \mathbb{R}^{(q+1) \times 2 b}$ :

$$
H_{q+1}=A_{q+1} V
$$

Furthermore, since $A$ results from applying the softmax operator (see (8.25)), the elements of the vector $A_{q+1}$ are strictly positive and satisfy the normalization condition

$$
\sum_{j=1}^{q+1} a_{q+1, j}=1, \quad \text { and with } \quad a_{q+1, j}>0
$$

In this context, the $k$-th element of the attention head $H_{q+1}$ can be expressed as a convex combination of the elements in the $k$-th column of the value matrix $V$, with coefficients given by $A_{q+1}$. Additionally, decomposing the value matrix $V$ into two parts, the first part, $\boldsymbol{v}^{\text {covariate }} \in \mathbb{R}^{q \times 2 b}$, contains the first $q$ rows of $V$, while the second part, $\boldsymbol{v}_{q+1} \in \mathbb{R}^{b}$, corresponds to the row associated with the CLS token, equation (8.37) can be reformulated as:

$$
H_{q+1}=P \boldsymbol{v}_{q+1}+(1-P) \boldsymbol{v}^{\text {covariate }}
$$

where $P=a_{q+1, q+1} \in(0,1)$ is the last element of the attention row $A_{q+1}$ and represents the weight assigned to the CLS token. The remaining weight, $\sum_{j=1}^{q} a_{q+1, j}=1-P$, is distributed across the covariate information. This formulation reveals that the attention mechanism for the CLS token can be interpreted as a credibility-weighted average. The CLS token's own information (representing collective experience) is combined with the covariates' information (representing individual experience) according to their respective credibility weights. In essence, this is a Bühlmann [34] type linear credibility formula, or a dynamic version of it, with the credibility weights learned during training and depending on the input.

## Decoder

The final block of the CT architecture is the decoder that derives from the represention $\boldsymbol{c}^{\text {cred }}(\boldsymbol{X})$, given in (8.36), the predictions. The proposal of Richman et al. [188] performs

## Page 163
this task considering an additional FNN layer $\boldsymbol{z}^{\mathrm{FNN}}$ and a suitable link-function $g$, so that we obtain the regression function

$$
\boldsymbol{X} \mapsto \mu^{\mathrm{cred}}(\boldsymbol{X})=g^{-1}\left\langle\boldsymbol{w}, \boldsymbol{z}^{\mathrm{FNN}}\left(\boldsymbol{c}^{\mathrm{cred}}(\boldsymbol{X})\right)\right\rangle
$$

with readout parameter $\boldsymbol{w}$. This is illustrated in Figure 8.16.

Figure 8.16: Graphical representation of the credibility transformer.

We conclude that transformers for tabular data (using the feature tokenization transformation) and its credibility transformer extension present interesting network architectures for solving actuarial problems. The credibility transformer is inspired by a Bühlmann [34] credibility mechanism, that is useful to stabilize and improve network training. In fact, in examples, the credibility transformer has proved excellent performance, though at higher computational costs than a classical FNN architecture. Moreover, the hidden credibility mechanism (8.38) allows for an integrated variable importance measure; for further details, see Richman et al. [188].
![Page 163 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p163_img1.jpg)

## Page 164
Version March 3, 2025, @AI Tools for Actuaries

## Page 165
# Chapter 9 

## Unsupervised learning

### 9.1 Introduction

Unsupervised learning covers the topic of learning the structure in the covariates $\boldsymbol{X}$ without considering any response variable $Y$. This means that unsupervised learning aims at understanding the population distribution of the covariates $\boldsymbol{X} \sim \mathbb{P}$. This can be achieved by learning the inherent pattern in $\boldsymbol{X}$ from an i.i.d. learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$. This learning sample is called unlabelled because it does not include any responses.

Broadly speaking, there are the following main tasks that can be studied and solved with unsupervised learning.
(1) Dimension reduction. Starting from $q$-dimensional real-valued covariates $\boldsymbol{X} \in \mathbb{R}^{q}$, we may ask the question whether there is a lower dimensional representation of $\boldsymbol{X}$ without a significant loss of information (i.e., only with a small reconstruction error). E.g., if we have the three-dimensional covariates $\boldsymbol{X}=\left(X_{1}, X_{2}, X_{1}-X_{2}\right)^{\top}$, it is clear that we can drop one coordinate without any loss of information, because two components are sufficient to fully describe $\boldsymbol{X}$ in this case. The most commonly used technique for dimension reduction is the principle component analysis (PCA) which is based on the singular value decomposition (SVD). The PCA provides a linear approximation by projecting the covariates to a new orthonormal coordinate system. A non-linear extension of the PCA is obtained by a bottleneck neural network (BNN) that transforms the data non-linearly to receive a lower dimensional representation of the original data at a minimal reconstruction error.
(2) Clustering. Clustering techniques are methods that are based on classifying (or binning), meaning that they group similar covariates $\boldsymbol{X}$ into (homogeneous) classes (clusters, bins). This leads to a segmentation of a heterogeneous population into homogeneous classes. Popular methods are hierarchical clustering methods, $K$ means clustering, K-medoids clustering, distribution-based Gaussian mixture models (GMMs) clustering or density-based spatial clustering of applications with noise (DBSCAN).
(3) Low-dimensional visualization. Low-dimensional visualization of high-dimensional data has some similarity with the dimension reduction problem from the first item,

## Page 166
but instead of trying to minimize a loss of information (reconstruction error), these methods rather aim at preserving the local structure (topology), so that a certain adjacency relation in a neighborhood of a given instance is kept. Popular methods are $t$-distributed stochastic neighbor embedding ( $t$-SNE), uniform manifold approximation and projection (UMAP) or self-organizing maps (SOM) also called Kohonen map.

The previous methods are mainly used to understand, simplify and illustrate the covariate distribution $\boldsymbol{X} \sim \mathbb{P}$. In financial and insurance applications, unsupervised learning methods can also be used for anomaly detection. Based on similarity measures, unsupervised learning methods may be used for outlier detection, e.g., indicating fraud or other abnormal structure or behavior in the data.

We give a selected overview of some of these unsupervised learning techniques, and for more methods and a more in-depth discussion we refer the interested reader to the unsupervised learning literature. A general difficulty in most unsupervised learning methods is that they work well for real-valued vectors $\boldsymbol{X} \in \mathbb{R}^{q}$, but they struggle to deal with categorical variables. Naturally, actuarial problems heavily rely on categorical covariates, and there is only little guidance on how to deal with those categorical variables in an unsupervised learning context, e.g., how can we reasonably quantify dissimilarity between different colors of cars? Section 2.3.2 has been discussing pre-processing of categorical covariates, such as one-hot encoding, entity embedding or target encoding. This has been extended by considering a contextual entity embedding in Section 8.2.2. These are possible ways of pre-processing categorical covariates before considering unsupervised learning methods.

# 9.2 Dimension reduction methods 

We start from a learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$ having $q$-dimensional real-valued features $\boldsymbol{X}_{i} \in \mathbb{R}^{q}$. The goal is to understand whether this learning sample is contained in a lower dimensional manifold (object or surface).
Figure 9.1 gives an example of a learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$ in $\mathbb{R}^{2}$. The features $\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$ form a noisy unit circle. Therefore, if we know that the features roughly live on the unit circle $B_{1}=\left\{\boldsymbol{x} \in \mathbb{R}^{2} ; x_{1}^{2}+x_{2}^{2}=1\right\}$, it is sufficient to record the angle in the polar coordinate system. Based on this angle, we can almost perfectly reconstruct the original feature $\boldsymbol{X}_{i}$.
Of course, this is a very simple example because it can nicely be plotted in $\mathbb{R}^{2}$ and the underlying functional form can easily be identified. However, in general, we work in high-dimensional spaces $\mathbb{R}^{q}, q \gg 1$, where such a graphical solution does not work. First, finding such manifolds in high-dimensional spaces is difficult, typically, we cannot even determine the dimension of the embedded object; in some sense this relates to the discussion on the effective dimension of FNNs, see last item of the discussion on page 82. Second, though looking simple, already Figure 9.1 may pose some challenges. A problem is that the unit circle is a non-linear object in the Euclidean coordinate system, and the most popular dimension reduction method, the PCA, is (only) designed to deal with linear problems.

## Page 167
Figure 9.1: Learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$ in $\mathbb{R}^{2}$.

# 9.2.1 Standardization 

Throughout this chapter, we assume to work with standardized data, meaning the following. Based on the learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n} \subset \mathbb{R}^{q}$, we construct the design matrix

$$
\mathfrak{X}=\left[\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{n}\right]^{\top}=\left(\begin{array}{ccc}
X_{1,1} & \cdots & X_{1, q} \\
\vdots & \ddots & \vdots \\
X_{n, 1} & \cdots & X_{n, q}
\end{array}\right) \in \mathbb{R}^{n \times q}
$$

compared to (2.10), we drop the intercept column from the design matrix in this chapter. The columns of this design matrix $\mathfrak{X}$ describe different quantities, e.g., the first column may describe the weight of the vehicle, the second one the age of the policyholder, etc. Thus, these columns live on different scales (and units). Since we would like to apply a unit-free dimension reduction technique to $\mathfrak{X}$, we need to standardize the columns of $\mathfrak{X}$ beforehand. For this foregoing standardization, we apply (2.18) to all covariate components, such that the columns of the resulting design matrix $\mathfrak{X}$ are centered and have the same empirical variance. The empirical variance is either $(n-1) / n$ or 1 depending on which empirical standard deviation estimator was applied. Standardization is done to ensure that all columns of the design matrix $\mathfrak{X}$ live on the same scale, are unit-free, before applying the PCA to this design matrix $\mathfrak{X}$.

A general difficulty in most of the unsupervised learning methods is the treatment of categorical variables. They can be embedded using one-hot encoding, but if we have many levels, the resulting design matrix $\mathfrak{X}$ will be sparse, i.e., with lots of zero entries (before standardization), and most unsupervised learning methods struggle with this sparsity; intuitively, the higher the dimension $q$ the more collinear sparse vectors become and the less well-conditioned the design matrix $\mathfrak{X}$ will be. Therefore, it is advantageous if one can use a low-dimensional entity embedding (2.15) for categorical variables, though, it is not always clear where one can get it from. E.g., if one uses a supervised learning method for this entity embedding, the utilized target may not be the right label that reflects the clustering that one wants to get. For instance, if one has different provinces,
![Page 167 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p167_img1.jpg)

## Page 168
there are many different targets (population density, average salary, area of the province, average rainfall, etc.), and each target may lead to a different entity embedding.

# 9.2.2 Auto-encoders 

The general principle of finding a lower dimensional object that encodes the learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$ can be described by an auto-encoder. An auto-encoder maps a high-dimensional object $\boldsymbol{X} \in \mathbb{R}^{q}$ to a low-dimensional representation, say, in $\mathbb{R}^{p}, p<q$, so that this dimension reduction still allows to (almost perfectly) reconstruct the original data $\boldsymbol{X}$. To measure the loss of information, we introduce a dissimilarity function.
Definition 9.1 (dissimilarity function). A dissimilarity function

$$
L(\cdot, \cdot): \mathbb{R}^{q} \times \mathbb{R}^{q} \rightarrow \mathbb{R}_{+}, \quad\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right) \mapsto L\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right) \geq 0
$$

has the property that $L\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right)=0$ if and only if $\boldsymbol{X}=\boldsymbol{X}^{\prime}$.
Note that we use the same notation $L$ for the dissimilarity function as for the loss function (1.5) because, essentially, they play the same role, only the input dimensions differ. In general, a dissimilarity function does not need to be a proper distance function. That is, a dissimilarity function does not need to be symmetric in its arguments, nor does it need to satisfy the triangle inequality, e.g., the KL divergence is a non-symmetric example that does not satisfy the triangle inequality.

Definition 9.2 (auto-encoder). Select dimensions $p<q$. An auto-encoder is a pair $(\Phi, \Psi)$ of mappings, called encoder and decoder, respectively,

$$
\Phi: \mathbb{R}^{q} \rightarrow \mathbb{R}^{p} \quad \text { and } \quad \Psi: \mathbb{R}^{p} \rightarrow \mathbb{R}^{q}
$$

such that their composition $\Psi \circ \Phi$ has a small reconstruction error w.r.t. the chosen dissimilarity function $L(\cdot, \cdot)$, that is,

$$
\boldsymbol{X} \mapsto L(\boldsymbol{X}, \Psi \circ \Phi(\boldsymbol{X})) \quad \text { is small for all instances } \boldsymbol{X} \text { of interest. }
$$

Strictly speaking, Definition 9.2 is not a proper mathematical definition, because the clause in (9.3) is not a well-defined mathematical term. We allow ourselves to be a bit sloppy at this point; we are just going to explain it, and it will not harm any mathematical arguments below.
Naturally, a small reconstruction error in (9.3) cannot be achieved for all $\boldsymbol{X} \in \mathbb{R}^{q}$, because the dimension reduction $p<q$ always leads to a loss of information on the entire space $\mathbb{R}^{q}$. However, if all $\boldsymbol{X}$ "of interest" live in a lower dimensional object $B_{1}$ of dimension $p$, then it is possible to find an encoder (coordinate mapping) $\Phi: \mathbb{R}^{q} \rightarrow \mathbb{R}^{p}$ so that one can perfectly reconstruct the original object $B_{1}$ by the decoder $\Psi: \mathbb{R}^{p} \rightarrow \mathbb{R}^{q}$. We give an example.

Example 9.3. We come back to Figure 9.1. If the covariates live in the unit circle, $\boldsymbol{X} \in B_{1} \subset \mathbb{R}^{2}$, the encoder (coordinate mapping) is received by $\Phi: \mathbb{R}^{2} \rightarrow[0,2 \pi)$ describing the angle in polar coordinates, and the decoder $\Psi:[0,2 \pi) \rightarrow B_{1} \subset \mathbb{R}^{2}$ maps these angles to the unit circle. This auto-encoder preserves the information of the

## Page 169
polar angle and it loses the information about the size of the radius. However, if all covariates $\boldsymbol{X} \in B_{1}$ "of interest" lie in the unit circle, the information about the radius is not necessary, and, in fact, the object $B_{1}$ is one-dimensional $p=1$ in this case. In other words, the auto-encoder $\Psi \circ \Phi$ is the identity map on $B_{1}$, and generally it is an (orthogonal) projection from $\mathbb{R}^{2}$ to $B_{1}$. We conclude that in this case, the interval $[0,2 \pi)$ is the low-dimensional representation of the unit circle $B_{1}$.

Working in Euclidean spaces $\mathbb{R}^{q}$, one can take the classical $L^{k}$-norms, $k \in(0, \infty]$, as dissimilarity measures

$$
L\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right)=\left\|\boldsymbol{X}-\boldsymbol{X}^{\prime}\right\|_{k}=\left(\sum_{j=1}^{q}\left|X_{j}-X_{j}^{\prime}\right|^{k}\right)^{1 / k}
$$

For $k=2$, we have the Euclidean distance, $k=1$ corresponds to the $L^{1}$-distance (also known as Manhattan distance), and the limiting case $k=\infty$ is the supremums norm. The Euclidean distance is a special case of the Mahalanobis distance defined by

$$
L\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right)=\sqrt{\left(\boldsymbol{X}-\boldsymbol{X}^{\prime}\right)^{\top} A\left(\boldsymbol{X}-\boldsymbol{X}^{\prime}\right)}
$$

for a positive definite matrix $A \in \mathbb{R}^{q \times q}$.
When it comes to categorical covariates, things start to become more difficult. Assume that $X$ is categorical taking $K$ levels. Using one-hot encoding we can embed $X \mapsto \boldsymbol{X} \in$ $\{0,1\}^{K}$ into the $K$-dimensional Euclidean space $\mathbb{R}^{K}$. The Hamming distance counts the number of positions where two one-hot encoded vectors $\boldsymbol{X}$ and $\boldsymbol{X}^{\prime}$ differ. The Hamming distance is equal to the Manhattan distance for binary vectors. Up to a factor of two, the one-hot encoded Hamming distance is equal to

$$
L\left(X, X^{\prime}\right)=\mathbb{1}_{\left\{X \neq X^{\prime}\right\}}
$$

A disadvantage of this approach, equivalently to one-hot encoding, is that all mutual distances between the levels are equal, and there is no notion of similarity between different levels. This is precisely the step where a low-dimensional entity embedding may be useful, see Sections 2.3.2 and 8.2.2.
For multiple categorical covariates, one can scale them to bring them to the same units. To account for the number of levels $K$, the scaled (probability) version is given by

$$
L\left(X, X^{\prime}\right)=\frac{1}{K^{2}} \mathbb{1}_{\left\{X \neq X^{\prime}\right\}}
$$

This is inspired by the fact that if $X$ and $X^{\prime}$ are independent and uniform on $\left\{a_{1}, \ldots, a_{K}\right\}$, we receive the contingency Table 9.1 (lhs). For non-uniform i.i.d. categorical variables it may be adapted to a weighted version as sketched on the right-hand side of Table 9.1

$$
L\left(X, X^{\prime}\right)=\frac{1}{p_{X} p_{X^{\prime}}} \mathbb{1}_{\left\{X \neq X^{\prime}\right\}}
$$

with (positive) categorical probabilities $\left(p_{a_{k}}\right)_{k=1}^{K}$ summing up to one.

## Page 170
| $X \backslash X^{\prime}$ | $a_{1}$ | $\cdots$ | $a_{K}$ |
| :--: | :--: | :--: | :--: |
| $a_{1}$ | $1 / K^{2}$ | $\cdots$ | $1 / K^{2}$ |
| $\vdots$ | $\vdots$ | $\ddots$ | $\vdots$ |
| $a_{K}$ | $1 / K^{2}$ | $\cdots$ | $1 / K^{2}$ |


| $X \backslash X^{\prime}$ | $a_{1}$ | $\cdots$ | $a_{K}$ |
| :--: | :--: | :--: | :--: |
| $a_{1}$ | $1 / p_{a_{1}}^{2}$ | $\cdots$ | $1 /\left(p_{a_{1}} p_{a_{K}}\right)$ |
| $\vdots$ | $\vdots$ | $\ddots$ | $\vdots$ |
| $a_{K}$ | $1 /\left(p_{a_{K}} p_{a_{1}}\right)$ | $\cdots$ | $1 / p_{a_{K}}^{2}$ |

Table 9.1: Contingency tables of two i.i.d. categorical random variables.

# 9.2.3 Principal component analysis 

## Linear auto-encoder

The PCA is a linear dimension reduction technique that has different interpretations, one of them is a linear auto-encoder interpretation, according to Definition 9.2. We have decided to give the technical explanation behind the PCA that describes an explicit construction that will result in the auto-encoder interpretation. Basically, this only uses linear algebra.
Consider the design matrix $\mathfrak{X}=\left[\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{n}\right]^{\top}$ given by (9.1). The rows of this design matrix contain the transposed covariates $\boldsymbol{X}_{i} \in \mathbb{R}^{q}, 1 \leq i \leq n$. Select the standard unit basis $\left(\boldsymbol{e}_{j}\right)_{j=1}^{q}$ of the Euclidean space $\mathbb{R}^{q}$. This allows us to write the covariates $\boldsymbol{X}_{i}$ as

$$
\boldsymbol{X}_{i}=X_{i, 1} \boldsymbol{e}_{1}+\ldots+X_{i, q} \boldsymbol{e}_{q}=\sum_{j=1}^{q} X_{i, j} \boldsymbol{e}_{j} \in \mathbb{R}^{q}
$$

The PCA represents these covariates $\boldsymbol{X}_{i}$ in a different orthonormal basis ${ }^{1}\left(\boldsymbol{v}_{j}\right)_{j=1}^{q}$, i.e., by a linear transformation we can rewrite these covariates $\boldsymbol{X}_{i}$ as

$$
\boldsymbol{X}_{i}=a_{i, 1} \boldsymbol{v}_{1}+\ldots+a_{i, q} \boldsymbol{v}_{q}=\sum_{j=1}^{q}\left\langle\boldsymbol{X}_{i}, \boldsymbol{v}_{j}\right\rangle \boldsymbol{v}_{j} \in \mathbb{R}^{q}
$$

for the new coefficients $a_{i, j}=\left\langle\boldsymbol{X}_{i}, \boldsymbol{v}_{j}\right\rangle \in \mathbb{R}$.
The two representations (9.7) and (9.8) are equivalent, however, in different parametrizations (bases) of the (same) Euclidean space $\mathbb{R}^{q}$.

The PCA performs the following steps that provide the dimension reduction at a minimal loss of information:
(1) Select the encoding dimension $p<q$ and define the encoder $\Phi_{p}: \mathbb{R}^{q} \rightarrow \mathbb{R}^{p}$ by

$$
\boldsymbol{X} \mapsto \Phi_{p}(\boldsymbol{X})=\left(\left\langle\boldsymbol{X}, \boldsymbol{v}_{1}\right\rangle, \ldots,\left\langle\boldsymbol{X}, \boldsymbol{v}_{p}\right\rangle\right)^{\top} \in \mathbb{R}^{p}
$$

That is, we only keep the first $p$ principal components in the alternative orthonormal basis $\left(\boldsymbol{v}_{j}\right)_{j=1}^{q}$ representation (9.8), and we truncate the rest.
(2) For the decoder $\Psi_{p}: \mathbb{R}^{p} \rightarrow \mathbb{R}^{q}$ we use a simple embedding

$$
\boldsymbol{Z} \mapsto \Psi_{p}(\boldsymbol{Z})=\sum_{j=1}^{p} Z_{j} \boldsymbol{v}_{j}=\sum_{j=1}^{p} Z_{j} \boldsymbol{v}_{j}+\sum_{j=p+1}^{q} 0 \cdot \boldsymbol{v}_{j} \in \mathbb{R}^{q}
$$

[^0]
[^0]:    ${ }^{1}$ An orthonormal basis of $\mathbb{R}^{q}$ is a set of normalized and orthogonal vectors $\left(\boldsymbol{v}_{j}\right)_{j=1}^{q}$ spanning the whole space $\mathbb{R}^{q}$. In particular, we have scalar (dot) product $\left\langle\boldsymbol{v}_{j}, \boldsymbol{v}_{k}\right\rangle=\mathbb{1}_{\{j=k\}}$.

## Page 171
That is, we pad the vector $\boldsymbol{Z} \in \mathbb{R}^{p}$ with zeros to get the right length $q>p$; in network modeling this is called padding with zeros to length $q$, see Section 8.3.6.
(3) Composing the encoder $\Phi_{p}$ and the decoder $\Psi_{p}$ gives us the auto-encoder

$$
\boldsymbol{X} \mapsto \Psi_{p} \circ \Phi_{p}(\boldsymbol{X})=\sum_{j=1}^{\nu}\left\langle\boldsymbol{X}, \boldsymbol{v}_{j}\right\rangle \boldsymbol{v}_{j} \in \mathbb{R}^{q}
$$

This is nothing else than an orthogonal projection of $\boldsymbol{X}$ to the sub-space spanned by $\left(\boldsymbol{v}_{j}\right)_{j=1}^{\nu}$. This auto-encoder has a reconstruction error of

$$
\boldsymbol{X}-\Psi_{p} \circ \Phi_{p}(\boldsymbol{X})=\sum_{j=\rho+1}^{q}\left\langle\boldsymbol{X}, \boldsymbol{v}_{j}\right\rangle \boldsymbol{v}_{j}
$$

that is, the reconstruction error is precisely determined by the components that were truncated by the encoder $\Phi_{p}$. The main idea behind the PCA is to select the orthonormal basis $\left(\boldsymbol{v}_{j}\right)_{j=1}^{q}$ of $\mathbb{R}^{q}$ such that this reconstruction error (9.11) becomes minimal (in some dissimilarity measure) over the learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$. This is achieved by selecting the directions of the biggest variabilities in the design matrix $\mathfrak{X}$.

We want to minimize the reconstruction error (9.11) over all learning samples $\mathcal{L}=$ $\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$. For this we select the squared $L^{2}$-distance dissimilarity measure

$$
L\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right)=\left\|\boldsymbol{X}-\boldsymbol{X}^{\prime}\right\|_{2}^{2}
$$

and for aggregating over the instances $1 \leq i \leq n$, we simply take the sum of the dissimilarity terms. In view of (9.11), a straightforward computation gives us the total dissimilarity on the learning sample $\mathcal{L}$, expressed by the design matrix $\mathfrak{X}$,

$$
\sum_{i=1}^{n} L\left(\boldsymbol{X}_{i}, \Psi_{p} \circ \Phi_{p}\left(\boldsymbol{X}_{i}\right)\right)=\sum_{i=1}^{n}\left\|\boldsymbol{X}_{i}-\Psi_{p} \circ \Phi_{p}\left(\boldsymbol{X}_{i}\right)\right\|_{2}^{2}=\sum_{j=\rho+1}^{q}\left\|\mathfrak{X} \boldsymbol{v}_{j}\right\|_{2}^{2}
$$

The latter term tells us how we should select the orthonormal basis $\left(\boldsymbol{v}_{j}\right)_{j=1}^{q}$, namely, the terms $\left\|\mathfrak{X} \boldsymbol{v}_{j}\right\|_{2}^{2}$ should be maximally decreasing in $j$. This implies that any linear auto-encoder $\Psi_{p} \circ \Phi_{p}$ (i.e., for any $1 \leq p \leq q$ ) has minimal total dissimilarity across the learning sample $\mathcal{L}$. This requirement can be solved by recursive convex Lagrange problems.
A first orthonormal basis vector $\boldsymbol{v}_{1} \in \mathbb{R}^{q}$ is given by a solution of

$$
\boldsymbol{v}_{1} \in \underset{\|\boldsymbol{v}\|_{2}=1}{\arg \max }\|\mathfrak{X} \boldsymbol{v}\|_{2}^{2}
$$

and the $j$-th orthonormal basis vector $\boldsymbol{v}_{j} \in \mathbb{R}^{q}, 2 \leq j \leq q$, is computed recursively by

$$
\boldsymbol{v}_{j} \in \underset{\|\boldsymbol{v}\|_{2}=1}{\arg \max }\|\mathfrak{X} \boldsymbol{v}\|_{2}^{2} \quad \text { subject to }\left\langle\boldsymbol{v}_{k}, \boldsymbol{v}\right\rangle=0 \text { for all } 1 \leq k \leq j-1
$$

This solves the total reconstruction error (dissimilarity) minimization (9.12) for the linear auto-encoders (9.10) simultaneously for all $1 \leq p \leq q$, and the single terms $\left\langle\boldsymbol{X}, \boldsymbol{v}_{j}\right\rangle \boldsymbol{v}_{j}$ are the principal components in the lower dimensional representations.

## Page 172
# Singular value decomposition 

At this stage, we could close the chapter on the PCA, because (9.10), (9.13) and (9.14) fully solve the problem. However, there is a more efficient way of computing the PCA than recursively solving the convex Lagrange problems (9.13)-(9.14). This alternative way of computing the orthonormal basis $\left(\boldsymbol{v}_{j}\right)_{j=1}^{q}$ uses a singular value decomposition (SVD) and the algorithm of Golub-Van Loan [82]; see Hastie et al. [93, Section 14.5.1]. The SVD is based on the following mathematical result:

There exist orthogonal matrices $U \in \mathbb{R}^{n \times q}$ and $V \in \mathbb{R}^{q \times q}$, with $U^{\top} U=V^{\top} V=\operatorname{Id}_{q}$, and a diagonal matrix $\Lambda=\operatorname{diag}\left(\lambda_{1}, \ldots, \lambda_{q}\right) \in \mathbb{R}^{q \times q}$ with singular values $\lambda_{1} \geq \ldots \geq \lambda_{q} \geq 0$ such that we have the SVD of $\mathfrak{X}$

$$
\mathfrak{X}=U \Lambda V^{\top}
$$

The matrix $U$ is called left-singular matrix of $\mathfrak{X}$, and the matrix $V$ is called right-singular matrix of $\mathfrak{X}$. The crucial property of the SVD is that the column vectors of the rightsingular matrix $V=\left[\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{q}\right] \in \mathbb{R}^{q \times q}$ precisely give the orthonormal basis $\left(\boldsymbol{v}_{j}\right)_{j=1}^{q}$ that we are looking for. This is justified by the computation

$$
\left\|\mathfrak{X} \boldsymbol{v}_{j}\right\|_{2}^{2}=\boldsymbol{v}_{j}^{\top} \mathfrak{X}^{\top} \mathfrak{X} \boldsymbol{v}_{j}=\boldsymbol{v}_{j}^{\top} V \Lambda^{2} V^{\top} \boldsymbol{v}_{j}=\lambda_{j}^{2}
$$

Crucially, the singular values are ordered $\lambda_{1} \geq \ldots \geq \lambda_{q} \geq 0$, and the orthonormal basis vectors $\left(\boldsymbol{v}_{j}\right)_{j=1}^{q}$ are the eigenvectors of $\mathfrak{X}^{\top} \mathfrak{X}$ to the squared singular values $\lambda_{j}^{2}$. Thus, (9.16) shows that the first principal component has the biggest potential reconstruction error, and this is decreasing in $j$, minimizing the reconstruction error (9.11) for any $p$.

## Example

We provide a two-dimensional example, and we use the R command svd which is included in the base package of R [179].

Figure 9.2: Two PCAs for two different learning samples $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$ in $\mathbb{R}^{2}$.
Figure 9.2 shows two PCAs for two different learning samples $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$ in $\mathbb{R}^{2}$, i.e., in two dimensions $q=2$. The plot on the left-hand side has a very dominant first principal
![Page 172 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p172_img1.jpg)

## Page 173
component, and the first basis vector $\boldsymbol{v}_{1}$ can fairly well describe the data. The plot on the right-hand side shows much more dispersion, and the singular values $\lambda_{1} \approx \lambda_{2}$. Therefore, we need both basis vectors $\boldsymbol{v}_{1}$ and $\boldsymbol{v}_{2}$ to accurately describe the second learning sample. The principle components are received by computing $\left\langle\boldsymbol{X}_{i}, \boldsymbol{v}_{j}\right\rangle$, and these are obtained by the orthogonal projections of the black dots $\boldsymbol{X}_{i}$ in Figure 9.2 to the red $(j=1)$ and orange $(j=2)$ line, respectively.

The right-singular matrix $V=\left[\boldsymbol{v}_{1}, \ldots, \boldsymbol{v}_{q}\right]$ of the SVD of $\mathfrak{X}$ is computed with the algorithm of Golub-Van Loan [82], from which we can calculate the representation (9.8) and the corresponding principal components $\left\langle\boldsymbol{X}, \boldsymbol{v}_{j}\right\rangle \boldsymbol{v}_{j}$ of the PCA. The magnitudes of the singular values $\left(\lambda_{j}\right)_{j=1}^{q}$ determine how many principal components we need to select for a good description of the learning sample $\mathcal{L}$.

# 9.2.4 Bottleneck neural network 

The PCA presented in the last section is a linear auto-encoder. A natural attempt to receive a non-linear auto-encoder is to set-up a FNN architecture that aims at compressing the input data at a low reconstruction error; this has been introduced and studied by Kramer [126] and Hinton-Salakhutdinov [97].
Select a deep FNN architecture $\boldsymbol{z}^{(d: 1)}=\boldsymbol{z}^{(d)} \circ \cdots \circ \boldsymbol{z}^{(1)}$, see (5.3). This deep FNN architecture needs to have two special features:
(i) The output dimension is equal to the input dimension, $q_{d}=q_{0}=q$, where $q$ is the dimension of the covariates $\boldsymbol{X} \in \mathbb{R}^{q}$.
(ii) One FNN layer $\boldsymbol{z}^{(m)}, 1 \leq m<d$, should have a very small dimension (number of units) $q_{m}=p<q$. This dimension corresponds to the number of principal components we consider in (9.9)-(9.10) for the PCA, and $\boldsymbol{z}^{(m)}$ is called the bottleneck of the FNN. This bottleneck has size $p$, being a hyper-parameter selected by the modeler.

This two features give us the $B N N$ encoder

$$
\boldsymbol{X} \mapsto \Phi_{p}(\boldsymbol{X}):=\boldsymbol{z}^{(m: 1)}(\boldsymbol{X})=\left(\boldsymbol{z}^{(m)} \circ \cdots \circ \boldsymbol{z}^{(1)}\right)(\boldsymbol{X}) \in \mathbb{R}^{p}
$$

and the $B N N$ decoder, for $\boldsymbol{Z} \in \mathbb{R}^{p}$,

$$
\boldsymbol{Z} \mapsto \Psi_{p}(\boldsymbol{Z}):=\left(\boldsymbol{z}^{(d)} \circ \cdots \circ \boldsymbol{z}^{(m+1)}\right)(\boldsymbol{Z}) \in \mathbb{R}^{q}
$$

Composing the BNN encoder and BNN decoder, provides us with the $B N N$ auto-encoder $\Psi_{p} \circ \Phi_{p}: \mathbb{R}^{q} \rightarrow \mathbb{R}^{q}$ given by

$$
\boldsymbol{X} \mapsto \Psi_{p} \circ \Phi_{p}(\boldsymbol{X})=\left(\boldsymbol{z}^{(d)} \circ \cdots \circ \boldsymbol{z}^{(1)}\right)(\boldsymbol{X})
$$

Figure 9.3 illustrates a BNN auto-encoder of depth $d=4$, input dimension $q_{0}=q_{4}=5$, and with a bottleneck of size $q_{2}=p=2$.
This BNN auto-encoder can be trained on the learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$ using the SGD algorithm as described in Section 5.3.1. As loss function we select a dissimilarity

## Page 174
Figure 9.3: BNN auto-encoder with bottleneck dimension $q_{m}=p=2, m=2$; this graph was plotted with [71].
function, so that the SGD algorithm tries to minimize the reconstruction error w.r.t. the selected dissimilarity function. The low-dimensional representation of the data is then received by evaluating the bottleneck of the trained FNN

$$
\left\{\Phi_{p}\left(\boldsymbol{X}_{i}\right)\right\}_{i=1}^{n}=\left\{\boldsymbol{z}^{(m: 1)}\left(\boldsymbol{X}_{i}\right)\right\}_{i=1}^{n} \subset \mathbb{R}^{p}
$$

The advantage of the BNN auto-encoder over the PCA is that the BNN auto-encoder can deal with non-linear structures in the data, supposed we select a non-linear activation function $\phi$. The disadvantage clearly is that the BNN auto-encoder treats the bottleneck dimension $p$ as a hyper-parameter that needs to be selected before training the BNN. Changing this hyper-parameter requires to refit a new BNN architecture, i.e., in contrast to the PCA, we do not simultaneously get the results for all dimensions $1 \leq p \leq q$. Moreover, there is also no notion of singular values $\left(\lambda_{j}\right)_{j=1}^{q}$ that quantifies the significance of the principal components, but one has to evaluate the reconstruction errors for every bottleneck dimension $p$ to receive the suitable size of the bottleneck, i.e., an acceptable reconstruction error.

We close with remarks:

- Hinton-Salakhutdinov [97] have noticed that the gradient descent training of BNN architectures can be difficult, and it can likely result in poorly trained BNNs. Therefore, Hinton-Salakhutdinov [97] propose to use a BNN architecture that is symmetric in the bottleneck layer w.r.t. the number of neurons in all FNN layers. That is, select an architecture with $q_{m-k}=q_{m+k}$ for all $1 \leq k \leq m$ and $d=2 m$; Figure 9.3 gives such an example with $d=4$. Training of BNNs can then successively be done by recursively collapsing layers (keeping symmetric FNNs); we refer to Wüthrich-Merz [243, Section 7.5.5] for more details.
- If one chooses the linear activation function for $\phi$, the bottleneck will represent a linear space of dimension $p$ (supposed that all other FNN layers have more units),
![Page 174 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p174_img1.jpg)

## Page 175
and we receive a linear data compression. The result is basically the same as the one from the PCA, with the difference that the BNN auto-encoder does not give a representation in the orthonormal basis $\left(\boldsymbol{v}_{j}\right)_{j=1}^{p}$, but it gives the (same) results in the same linear subspace in a different parametrization (that is not explicitly specified). The reason for this is that the BNN auto-encoder does not have any notion of orthonormality, but this would need to be enforced by regularization during training.

# 9.2.5 Kernel principal component analysis 

The PCA is a linear dimension reduction technique, and one might look for a non-linear variant that is in the spirit of the PCA. To arrive at a non-linear PCA, the idea is to consider a feature map

$$
F: \mathbb{R}^{q} \rightarrow \mathbb{R}^{d}, \quad \boldsymbol{X} \mapsto F(\boldsymbol{X})
$$

where we typically are thinking of a higher dimensional feature embedding, $d>q$; in fact, typically, this higher dimensional space will be infinite-dimensional, but for the moment it is sufficient to think about a finite large $d$. We give an example that is related to support vector machines (SVMs).

Figure 9.4: Feature map $F: \mathbb{R} \rightarrow \mathbb{R}^{2}$ with $x \mapsto F(x)=\left(x, x^{2} / 4\right)^{\top}$.
Figure 9.4 (lhs) shows four real-valued instances $\left(X_{i}\right)_{i=1}^{4} \subset \mathbb{R}$. There are two of red type and two of blue type. On the real line $\mathbb{R}$, the red dots cannot be separated from the blue ones by one partition of $\mathbb{R}$. Figure 9.4 (rhs) shows the situation after applying the feature map $X_{i} \mapsto F\left(X_{i}\right)=\left(X_{i}, X_{i}^{2} / 4\right)^{\top} \in \mathbb{R}^{2}$. After this two-dimensional embedding we can separate the red from the blue dots by a single partition illustrated by the orange horizontal line. Such a feature map $F$ is the first part of the idea behind the non-linear kernel PCA, i.e., this higher dimensional embedding gives the necessary flexibility.

Main problem: How can we find a suitable feature map $F$ ?

Part of the answer to this question is:
![Page 175 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p175_img1.jpg)

## Page 176
It is not necessary to explicitly select the feature map $F$, but for our problem it suffices to know the (implied) kernel

$$
K: \mathcal{X} \times \mathcal{X} \rightarrow \mathbb{R}, \quad\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right) \mapsto K\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right)=\left\langle F(\boldsymbol{X}), F\left(\boldsymbol{X}^{\prime}\right)\right\rangle
$$

This is called the kernel trick, which means that for such types of problems, it is sufficient to know the kernel $K$. In many cases, it is simpler to directly select this kernel $K$, instead of trying to find a suitable feature map $F$.

We are going to explain why knowing the kernel $K$ is sufficient, but before that we start by assuming that the feature map $F: \mathbb{R}^{q} \rightarrow \mathbb{R}^{d}$ is known. This gives us the new (embedded) features $\left(F\left(\boldsymbol{X}_{i}\right)\right)_{i=1}^{n} \subset \mathbb{R}^{d}$, and we can construct the new design matrix in this bigger dimensional space

$$
\mathfrak{Z}=\left[F\left(\boldsymbol{X}_{1}\right), \ldots, F\left(\boldsymbol{X}_{n}\right)\right]^{\top} \in \mathbb{R}^{n \times d}
$$

Based on this embedding, we can perform a PCA on these embedded new features. Following the recipe of the PCA, see Section 9.2.3, we can find the principal components using a SVD of $\mathfrak{Z}$ providing us with the right-singular matrix with column vectors $\left(\boldsymbol{v}_{j}^{F}\right)_{j=1}^{d}$. This is then used to define the decoder $\Phi_{p}$, see (9.9), which gives us the PCA dimension reduction for $p \leq d$

$$
\boldsymbol{X} \mapsto F(\boldsymbol{X}) \mapsto \Phi_{p}(F(\boldsymbol{X}))=\left(\left\langle F(\boldsymbol{X}), \boldsymbol{v}_{1}^{F}\right\rangle, \ldots,\left\langle F(\boldsymbol{X}), \boldsymbol{v}_{p}^{F}\right\rangle\right)^{\top} \in \mathbb{R}^{p}
$$

Up to this stage, it seems that we need to know the feature map $F: \mathbb{R}^{q} \rightarrow \mathbb{R}^{d}$ to compute the individual principal components in (9.19). The crucial (next) step of the kernel trick is that the kernel $K$ is sufficient to compute $\left\langle F(\boldsymbol{X}), \boldsymbol{v}_{j}^{F}\right\rangle$, and the explicit knowledge of the feature map $F$ is not necessary. This precisely provides the (non-linear) kernel $P C A$ of Schölkopf et al. [200].
There are two crucial points that make the kernel trick work. These two points need some mathematical arguments which we are going to skip here, the interested reader is referred to Schölkopf et al. [200]. Before discussing these two points (a) and (b), we need to slightly generalize the feature map $F$ introduced in (9.17). Typically, this feature map $F: \mathbb{R}^{q} \rightarrow \mathcal{H}$ maps to an infinite-dimensional Hilbert space $\mathcal{H}$. This Hilbert space $\mathcal{H}$ allows for the kernel $K$ construction (9.18) because any Hilbert space is equipped with a scalar product. Of course, the finite-dimensional space $\mathbb{R}^{d}$, selected in (9.17), is one example of a Hilbert space $\mathcal{H}$. Now we are ready to discuss the two points (a) and (b) that make it possible to compute (9.19).
(a) First, there exist vectors $\boldsymbol{\alpha}_{j}=\left(\alpha_{j, 1}, \ldots, \alpha_{j, n}\right)^{\top} \in \mathbb{R}^{n}, j \geq 1$, that allow one to write the (eigen-)vectors $\left(\boldsymbol{v}_{j}^{F}\right)_{j \geq 1}$ as follows

$$
\boldsymbol{v}_{j}^{F}=\sum_{i=1}^{n} \alpha_{j, i} F\left(\boldsymbol{X}_{i}\right)
$$

i.e., the vectors $\left(\boldsymbol{v}_{j}^{F}\right)_{j \geq 1}$ are in the span of the new features $\left(F\left(\boldsymbol{X}_{i}\right)\right)_{i=1}^{n}$. Inserting this gives us for $j \geq 1$

$$
\left\langle F(\boldsymbol{X}), \boldsymbol{v}_{j}^{F}\right\rangle=\sum_{i=1}^{n} \alpha_{j, i} K\left(\boldsymbol{X}, \boldsymbol{X}_{i}\right)
$$

## Page 177
Note: this only requires the (implied) kernel $K$, but not the feature map $F$ itself.
(b) Second, we need to compute $\left(\boldsymbol{\alpha}_{j}\right)_{j \geq 1}$. Define the Gram matrix (kernel matrix)

$$
\mathbf{K}=\left[K\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right)\right]_{1 \leq i, i^{\prime} \leq n} \in \mathbb{R}^{n \times n}
$$

Solve the eigenvalue problem

$$
\mathbf{K} \boldsymbol{a}=\lambda^{K} \boldsymbol{a}
$$

and normalize the eigenvectors $\boldsymbol{a}_{j}$ of the non-zero eigenvalues $\lambda_{j}^{K}>0$ as follows

$$
\boldsymbol{\alpha}_{j}=\frac{1}{\sqrt{\lambda_{j}^{K} \boldsymbol{a}_{j}^{\top} \boldsymbol{a}_{j}}} \boldsymbol{a}_{j}
$$

These are precisely the vectors $\boldsymbol{\alpha}_{j} \in \mathbb{R}^{n}$ needed in (9.21).
In summary, we can compute (9.21)-(9.22) directly from the kernel $K$, without the explicit use of the feature map $F$. Thus, the kernel PCA dimension reduction (9.19) is fully determined by the kernel $K$, which also justifies the name kernel $P C A$.

Popular kernels in practice are polynomial kernels of order $k$ (with $b \in \mathbb{R}$ ) or radial Gaussian kernels (with $\gamma>0$ ) given by, respectively,

$$
\begin{aligned}
& K\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right)=\left(b+\left\langle\boldsymbol{X}, \boldsymbol{X}^{\prime}\right\rangle\right)^{k} \\
& K\left(\boldsymbol{X}, \boldsymbol{X}^{\prime}\right)=\exp \left\{-\gamma\left\|\boldsymbol{X}-\boldsymbol{X}^{\prime}\right\|_{2}^{2}\right\}
\end{aligned}
$$

For $k=1$ (and $b=0$ ) we have the linear kernel used in the standard PCA. Based on these kernel selections we can directly solve the kernel PCA by using (9.21)-(9.22), and we receive the kernel PCA dimension reduction (9.19) without an explicit choice of the feature map $F$.

Remark 9.4 (Mercer kernel). There is one question though. Namely, are the selected kernels in (9.23)-(9.24) "valid" kernels, i.e., are these (artificial) kernel choices implied by a feature map $F: \mathbb{R}^{q} \rightarrow \mathcal{H}$ according to (9.18)? If there does not exist such a feature map $F$ for a selected kernel $K$, then the presented theory may not hold for that kernel $K$. The Moore-Aronszajn [6] theorem gives sufficient conditions to solve this question. For this, we first need to introduce the Mercer kernel [154]. Assume $\mathcal{X}$ is a metric space. A mapping $K: \mathcal{X} \times \mathcal{X} \rightarrow \mathbb{R}$ is a Mercer kernel if it is continuous in both arguments, symmetric and positive semi-definite. ${ }^{2}$ The theorem of Moore-Aronszajn tells us that for every Mercer kernel there is a so-called reproducing kernel Hilbert space (RKHS) for which we can select a feature map $F$ that has this Mercer kernel $K$ as implied kernel. Thus, any Mercer kernel $K$ is a valid selection as it can be generated by a feature map $F$; see, e.g., Andrès et al. [3] for more details.

There are a couple of points that one should consider. The (kernel) PCA is usually performed on standardized matrices because this provides better results, i.e., essentially we should focus on the correlation/dependence structure, see Section 9.2.1. For the

[^0]
[^0]:    ${ }^{2}$ Positive semi-definite means that for all finite sequences of instances $\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$ and for all sequences $\boldsymbol{a} \in \mathbb{R}^{n}$ we have $\sum_{i, i^{\prime}=1}^{n} a_{i} a_{i^{\prime}} K\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right) \geq 0$.

## Page 178
kernelized version this means that one often replaces the Gram matrix $\mathbf{K}$ by a normalized version

$$
\widehat{\mathbf{K}}=\mathbf{K}-\mathbf{1}_{n} \mathbf{K}-\mathbf{K} \mathbf{1}_{n}+\mathbf{1}_{n} \mathbf{K} \mathbf{1}_{n}
$$

where the matrix $\mathbf{1}_{n} \in \mathbb{R}^{n \times n}$ has all elements equal to $1 / n$.
Compared to the classical PCA, there are two disadvantages of the kernel PCA. First, the kernel PCA is computationally very demanding for high sample sizes $n$, because it involves eigenvalue decompositions of matrices of size $n \times n$. Therefore, often the data is first compressed by a clustering algorithm, such as $K$-means clustering discussed in the next section. Second, since the feature map $F$ is not explicitly given, we cannot compute the eigenvectors (9.20), and, as a result, the reconstruction error is not easily tractable. Additionally, the eigenvalues are not directly helpful to determine the number of necessary principal components $p$ to have a small reconstruction error, because these eigenvalues are computed in a different space.

Example 9.5. We give an example of a kernel PCA. Assume that the covariates $\mathcal{L}=$ $\left(\boldsymbol{X}_{i}\right)_{i=1}^{n} \subset \mathbb{R}^{2}$ are two-dimensional, and they are related to three circles with different radii.

Figure 9.5: Learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$ in $\mathbb{R}^{2}$ with three circles of different radii.

Figure 9.5 shows the learning sample $\mathcal{L}$. This learning sample cannot be partitioned into the different colors by a simple splitting with hyperplanes (straight lines), and both coordinates are necessary to distinguish the differently colored dots. This implies that the first principal component of a (linear) PCA is not sufficient to describe the different instances. This is verified in Figure 9.6 (lhs).
Figure 9.6 (middle and rhs) show a polynomial kernel PCA, with $k=2$ and $b=1$, and a Gaussian kernel PCA, with $\gamma=1$, respectively. We now observe that the first principal component (on the $x$-axis) can separate the different colors fairly well, and in these two cases this first principal component (from the kernel PCA) might be sufficient to describe the data. This analysis does not use the standardized version of $\mathbf{K}$.
![Page 178 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p178_img1.jpg)

## Page 179
Figure 9.6: Kernel PCAs: (lhs) linear PCA, (middle) polynomial kernel PCA with $k=2$, (rhs) Gaussian kernel PCA.

# 9.3 Clustering methods 

Clustering methods aim at grouping similar covariates $\boldsymbol{X}$ into (homogeneous) clusters (also called groups, classes or bins), leading to a segmentation of the covariate space $\mathcal{X} \subset \mathbb{R}^{q}$; this is similar to a regression tree partition of the covariate space, we refer to Figure 6.2. Assume that we aim at partitioning the covariate space $\mathcal{X}$ into $K$ disjoint clusters. We introduce a classifier

$$
\mathcal{C}_{K}: \mathcal{X} \rightarrow \mathcal{K}:=\{1, \ldots, K\}, \quad \boldsymbol{X} \mapsto \mathcal{C}_{K}(\boldsymbol{X})
$$

This gives us a partition $\left(\mathcal{X}_{k}\right)_{k \in \mathcal{K}}$ of the covariate space $\mathcal{X}$ by defining for all $k \in \mathcal{K}$ the clusters

$$
\mathcal{X}_{k}=\left\{\boldsymbol{X} \in \mathcal{X} ; \mathcal{C}_{K}(\boldsymbol{X})=k\right\}
$$

for an illustration see Figure 9.7. This is rather equivalent to the regression tree partition (6.1), the main difference lies in its specific construction. For the regression tree construction in Chapter 6 we use the responses $Y$ to construct the partition, and in the clustering methods we use the covariates $\boldsymbol{X}$ themselves to define the clustering through a dissimilarity function. That is, we aim at choosing the classifier $\mathcal{C}_{K}$ such that the resulting dissimilarities within all clusters $\left(\mathcal{X}_{k}\right)_{k \in \mathcal{K}}$ are minimal. Sometimes this is also called quantization, meaning that all covariates $\boldsymbol{X}_{i} \in \mathcal{X}_{k}$ can be represented sufficiently accurately by a so-called model point $\boldsymbol{c}_{k} \in \mathcal{X}_{k}$, and actuarial modeling is then only performed on these model points $\left(\boldsymbol{c}_{k}\right)_{k \in \mathcal{K}}$. This is a quite common approach in life insurance portfolio valuation, that helps to simplify the complexity of valuation of large life insurance portfolios.

One distinguishes different types of clustering methods. There is (1) hierarchical clustering, (2) centroid-based clustering, (3) distribution-based clustering and (4) density-based clustering.
(1) Hierarchical clustering. Hierarchical clustering methods are based on recursive algorithms. The final number $K$ of clusters is not a-priori given as a hyper-parameter, but it is determined by a stopping rule. This hierarchical clustering is performed in
![Page 179 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p179_img1.jpg)

## Page 180
Figure 9.7: Illustration of $K$-means clustering for $\mathcal{C}_{K}: \mathbb{R}^{2} \rightarrow \mathcal{K}$ with $K=4$ : the black dots illustrate the cluster centers of step (1a) of the $K$-means clustering algorithm, and the orange dots show step (1b); this figure is taken from [183].
a tree construction-like manner, and there are two opposite ways of deriving such a segmentation: (i) divisive clustering and (ii) agglomerative clustering.
(i) Divisive clustering is a top-down approach of constructing clusters. Analogously to the recursive partitioning algorithm for regression trees, see Chapter 6, a divisive clustering method partitions non-homogeneous clusters into more homogeneous sub-groups w.r.t. the chosen dissimilarity measure, and a stopping rule decides on the resulting number $K$ of clusters. The most basic divisive clustering algorithm is called DIvisive ANAlysis (DIANA) clustering; see Kaufman-Rousseeuw [115, Chapter 6].
(ii) Agglomerative clustering is a bottom-up method that dynamically grows bigger clusters by merging sets that are similar until the algorithm is stopped. A basic agglomerative algorithm is called AGglomerative NESting (AGNES) clustering; see KaufmanRousseeuw [115, Chapter 5].

Typically, the resulting clusterings are illustrated in so-called dendrograms, which look the same as regression trees, see Figure 6.1. Both algorithms are usually exploit in a greedy manner, meaning that one tries to find the next optimal step in each loop of the recursive algorithm, i.e., the next optimal partition or fusion for the divisive and agglomerative algorithm, respectively. Usually, this results in time-consuming algorithms, and, if they converge, they likely converge to local optimums and not to the global one; the argument for this is similar to the one of the gradient descent algorithm; see Section 5.3. Note that if there are $n$ instances that we want to partition into two non-empty sets, there are $2^{n-1}-1$ possibilities. Therefore, it can be exhaustive to find the next best split, and this search is therefore often combined with other methods such as $K$-means clustering.
(2) Centroid-based clustering. For centroid-based clustering methods, one specifies a fixed number $K$ of clusters, and, depending on the method, different optimal cluster
![Page 180 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p180_img1.jpg)

## Page 181
centers are selected for these $K$ clusters. The partitioning is then obtained by allocating all instances to these cluster centers w.r.t. some distance or similarity measure. We will present $K$-means and $K$-medoids clustering, these methods mainly differ in how the cluster centers are selected.
(3) Distribution-based clustering. Centroid-based methods implicitly assume that the dissimilarity is a hard boundary decision. Distribution-based clusterings provide more flexibility in the sense that they allow for soft boundaries by adding some noise to the instances, accounting for the fact that some of the instances may, by coincidence, sit on the wrong side of the boundary. The most commonly used method is Gaussian mixture model (GMM) clustering, for which the $K$ cluster centers of the centroid-based methods are replaced by $K$ Gaussian distributions.
(4) Density-based clustering. Density-based clustering does not assume a fixed number $K$ of clusters, but similarly to agglomerative clustering, these clusters are determined dynamically. The idea behind density-based clustering is that every core of a cluster should be surrounded by a sufficiently dense set of instances to qualify to be a core of a cluster. The DBSCAN algorithm discussed below is of this type.

# 9.3.1 Hierarchical clustering 

We present the most basic divisive and agglomerative hierarchical clustering algorithms in this section.

## Divisive clustering algorithm

A divisive clustering algorithm is the DIANA algorithm which we briefly discuss in this section. Select a dissimilarity function $L: \mathcal{X} \times \mathcal{X} \rightarrow \mathbb{R}_{+}$on the covariate space $\mathcal{X} \subset \mathbb{R}^{q}$. We are going to recursively partition the learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n} \subset \mathcal{X}$.

A remark on the notation. The classifier (9.26) gives a partition $\left(\mathcal{X}_{k}\right)_{k \in \mathcal{K}}$ of the covariate space $\mathcal{X} \subset \mathbb{R}^{q}$, see (9.27). Naturally, we can only construct an exact partition on the (finite) learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n} \subset \mathcal{X}$. Thus, in fact, we will (only) construct the finite clusters

$$
\mathcal{X}_{k} \cap \mathcal{L}=\left\{\boldsymbol{X} \in \mathcal{L} ; \boldsymbol{X} \in \mathcal{X}_{k}\right\}
$$

To keep the notation simple in this outline, we will not distinguish the notation of the clusters $\mathcal{X}_{k}$, given in (9.27), and their finite sample counterparts $\mathcal{X}_{k} \cap \mathcal{L}$, given in (9.28). Moreover, we will also use the same notation for the indices of the instances in the clusters

$$
\mathcal{X}_{k}=\left\{i \in\{1, \ldots, n\} ; \boldsymbol{X}_{i} \in \mathcal{X}_{k}\right\}
$$

Thus, $\mathcal{X}_{k}$ has the three different meanings (9.27), (9.28) and (9.29), but from the context it will always be clear which version we use.

We now discuss the DIANA algorithm of Kaufman-Rousseeuw [115, Chapter 6].

## Page 182
Initialization. We initialize $\mathcal{X}_{1}=\mathcal{L}$. Similar to the regression tree this is the root cluster, and we initialize the index set $\mathcal{K}=\{1\}$, giving us one big cluster with $K=1$.

Recursive partitioning iteration. Assume we have the current partition (clusters) $\left(\mathcal{X}_{k}\right)_{k \in \mathcal{K}}$ of the learning sample $\mathcal{L}$. This partition has $K$ clusters, and in the next recursive step $K \rightarrow K+1$, we are going to expand by one cluster by partitioning one of the existing clusters. This recursive partitioning is going to be done in two steps: (i) find the cluster $k^{*} \in \mathcal{K}$ that is going to be partitioned, and (ii) construct the explicit partitioning of this cluster $\mathcal{X}_{k^{*}}$ (which is again done recursively). We explain these two steps.
(i) For the given dissimilarity function $L$, compute the diameters of all clusters, $k \in \mathcal{K}$,

$$
\delta_{k}=\max _{i, i^{\prime} \in \mathcal{X}_{k}} L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right)
$$

This diameter $\delta_{k} \geq 0$ gives the maximal dissimilarity between the instances within the same cluster $\mathcal{X}_{k}$. If $\max _{k \in \mathcal{K}} \delta_{k}=0$, we stop the algorithm because all clusters only contain completely similar instances. Otherwise, select the cluster with the biggest diameter

$$
k^{*}=\underset{k \in \mathcal{K}}{\arg \max } \delta_{k}
$$

with a deterministic rule if there is more than one argument that maximizes this problem. This provides us with the cluster $\mathcal{X}_{k^{*}}$ that we would like to split in the recursive step $K \rightarrow K+1$. Naturally, $\left|\mathcal{X}_{k^{*}}\right|>1$, because $\delta_{k}=0$ for all clusters that only contain one instance.
(ii) We construct the explicit partitioning of $\mathcal{X}_{k^{*}}$ by an inner recursive algorithm. Search for the instance $i \in \mathcal{X}_{k^{*}}$ that is the least similar one to all other instances in this cluster

$$
i^{*}=\underset{i \in \mathcal{X}_{k^{*}}}{\arg \max } \sum_{i^{\prime} \in \mathcal{X}_{k^{*}} \backslash\{i\}} L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right)
$$

with a deterministic rule if there is more than one such instance. This defines the initialization of the inner loop by setting up a new cluster $\mathcal{X}_{K+1}=\left\{\boldsymbol{X}_{i^{*}}\right\}$ and reducing the existing cluster by setting $\mathcal{X}_{k^{*}}^{\prime}=\mathcal{X}_{k^{*}} \backslash \mathcal{X}_{K+1}$.
If $\left|\mathcal{X}_{k^{*}}^{\prime}\right|>1$, we may migrate more instances from $\mathcal{X}_{k^{*}}^{\prime}$ to $\mathcal{X}_{K+1}$ by recursively computing for all instances $i \in \mathcal{X}_{k^{*}}^{\prime}$ the differences of the average dissimilarities on these two clusters $\mathcal{X}_{k^{*}}^{\prime}$ and $\mathcal{X}_{K+1}$, that is,

$$
\Delta(i)=\frac{1}{\left|\mathcal{X}_{k^{*}}^{\prime}\right|-1} \sum_{i^{\prime} \in \mathcal{X}_{k^{*}}^{\prime} \backslash\{i\}} L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right)-\frac{1}{\left|\mathcal{X}_{K+1}\right|} \sum_{i^{\prime} \in \mathcal{X}_{K+1}} L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right)
$$

If $\max _{i \in \mathcal{X}_{k^{*}}^{\prime}} \Delta(i) \leq 0$, we stop the inner migration loop because migrating does not decrease the average dissimilarity. Otherwise, we select

$$
i^{*}=\underset{i \in \mathcal{X}_{k^{*}}^{\prime}}{\arg \max } \Delta(i)
$$

with a deterministic rule if there is more than one maximizer. We migrate this instance $i^{*}$ to the new cluster by setting $\mathcal{X}_{K+1} \leftarrow \mathcal{X}_{K+1} \cup\left\{\boldsymbol{X}_{i^{*}}\right\}$ and we reduce the

## Page 183
existing cluster to $\mathcal{X}_{k^{*}}^{\prime}=\mathcal{X}_{k^{*}} \backslash \mathcal{X}_{K+1}$. This inner loop is iterated until the stopping rule is met or until $\left|\mathcal{X}_{k^{*}}^{\prime}\right|=1$. We then update the number of clusters $K \leftarrow K+1$, the reduced cluster $\mathcal{X}_{k^{*}} \leftarrow \mathcal{X}_{k^{*}}^{\prime}=\mathcal{X}_{k^{*}} \backslash \mathcal{X}_{K+1}$ and we add the new cluster $\mathcal{X}_{K+1}$, giving us the new partition $\left(\mathcal{X}_{k}\right)_{k=1}^{K+1}$ of $\mathcal{X}$.

These two steps (i)-(ii) are iterated until a stopping rule is met, or until there is no dissimilarity left on the existing clusters $\max _{k \in \mathcal{K}} \delta_{k}=0$. If we do not install a stopping rule, this algorithm will naturally terminate once all instances on all clusters are fully similar, and we can result in at most $K \leq n=|\mathcal{L}|$ clusters.

To define the diameter in (9.30), we consider the biggest dissimilarity between two instances in the same cluster. Of course, we could use many other definitions, e.g., we could consider the average dissimilarity as an alternative

$$
\delta_{k}=\frac{1}{\left|\mathcal{X}_{k}\right|^{2}} \sum_{i, i^{\prime} \in \mathcal{X}_{k}} L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right)
$$

# Agglomerative clustering algorithm 

We briefly describe the most basic agglomerative clustering algorithm, also known as AGNES; see Kaufman-Rousseeuw [115, Chapter 6]. Agglomerative means that we let the clusters grow starting from the individual instances.

Initialization. We initialize $\mathcal{X}_{i}=\left\{\boldsymbol{X}_{i}\right\}$ with index set $i \in \mathcal{K}=\{1, \ldots, n\}$, that is, each instance $1 \leq i \leq n$ forms its own cluster.

Recursive fusion iteration. We recursively fusion clusters that have the smallest mutual dissimilarity. Therefore, we define the average dissimilarity between two clusters $\mathcal{X}_{k}$ and $\mathcal{X}_{l}$, for $k, l \in \mathcal{K}$, as follows

$$
\delta_{k, l}=\frac{1}{\left|\mathcal{X}_{k}\right|\left|\mathcal{X}_{l}\right|} \sum_{i \in \mathcal{X}_{k}} \sum_{i^{\prime} \in \mathcal{X}_{l}} L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right)
$$

this is called the unweighted pair-group method with average mean (UPGMA). This UPGMA allows us to selected the two most similar clusters

$$
\left(k^{*}, l^{*}\right)=\underset{k, l \in \mathcal{K}}{\arg \min } \delta_{k, l}
$$

with a deterministic rule if there is more than one minimizer. We merge these two clusters $\mathcal{X}_{k^{*}} \leftarrow \mathcal{X}_{k^{*}} \cup \mathcal{X}_{l^{*}}$, reduce the index set $\mathcal{K} \leftarrow \mathcal{K} \backslash\left\{l^{*}\right\}$, and relabel the indices such that we obtain the new decreased index set $\mathcal{K}=\{1, \ldots, K\}$.
The UPGMA (9.31) is sometimes replaced by other dissimilarity measures. For example, the complete linkage considers

$$
\delta_{k, l}=\max _{i \in \mathcal{X}_{k}, i^{\prime} \in \mathcal{X}_{l}} L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right)
$$

or the single linkage considers

$$
\delta_{k, l}=\min _{i \in \mathcal{X}_{k}, i^{\prime} \in \mathcal{X}_{l}} L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right)
$$

The complete linkage considers the two most distinct instances, and the single linkage the two most similar instances in the two clusters.

## Page 184
# 9.3.2 K-means and $K$-medoids clusterings 

For $K$-means and $K$-medoids clustering, respectively, we first need to select the number $K$ of clusters that we want to have. This $K$ is a hyper-parameter selected by the modeler. We also remind of the three different definitions (9.27), (9.28) and (9.29) of $\mathcal{X}_{k}$; this is going to be used throughout this section.
The idea behind these two clustering methods is to achieve a minimal dissimilarity within the $K$ clusters

$$
\left(\mathcal{X}_{k}^{*}\right)_{k \in \mathcal{K}} \in \underset{\left(\mathcal{X}_{k}\right)_{k \in \mathcal{K}}}{\arg \min } \sum_{k=1}^{K} \sum_{i \in \mathcal{X}_{k}} L\left(\boldsymbol{c}_{k}, \boldsymbol{X}_{i}\right)
$$

where $\left(\boldsymbol{c}_{k}\right)_{k \in \mathcal{K}}$ are the corresponding cluster centers (also called cores); these cluster centers can be part of the minimization in (9.34); this is not indicated in the notation, but we briefly explain this next. $K$-means clustering and $K$-medoids clustering mainly (but not only) differ in how these cluster centers $\left(\boldsymbol{c}_{k}\right)_{k \in \mathcal{K}}$ are selected. For $K$-means clustering we select the empirical cluster means (thus, the selection of the cluster centers is not part of the minimization in (9.34)) by setting for $k \in \mathcal{K}$

$$
\boldsymbol{c}_{k}=\frac{1}{\left|\mathcal{X}_{k}\right|} \sum_{i \in \mathcal{X}_{k}} \boldsymbol{X}_{i} \in \mathbb{R}^{q}
$$

$K$-medoids considers a double minimization in (9.34), namely,

$$
\underset{\left(\mathcal{X}_{k}\right)_{k \in \mathcal{K}} ;\left.\boldsymbol{c}_{k} \in \mathcal{L} \text { for all } k \in \mathcal{K}\right\rvert\,}{\arg \min } \sum_{k=1}^{K} \sum_{i \in \mathcal{X}_{k}} L\left(\boldsymbol{c}_{k}, \boldsymbol{X}_{i}\right)
$$

That is, in $K$-medoids clustering, the cluster medoids $\boldsymbol{c}_{k} \in \mathcal{L}$ correspond to observed covariates $\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$, which puts an extra computational effort on the algorithm to find them compared to $K$-means clustering. The advantage is that $\boldsymbol{c}_{k} \in \mathcal{L}$ is always a valid observation.
On the other hand, $K$-means clustering is computationally much more attractive because the cluster centers (9.35) can be computed at a minimal effort; we are going to justify this selection below. A disadvantage of this approach is that if $\mathcal{X}$ is not convex (we refer to the continuous version (9.27)), it may happen that the empirical cluster mean $\boldsymbol{c}_{k}$ is not inside the area of valid instances $\mathcal{X}$, e.g., if this covariate space forms a circumference like in Figure 9.1, the center of the circle does not belong to this circumference and, thus, is not a valid covariate value.
Another disadvantage of $K$-means clustering is that it is specific to the squared Euclidean distance, we discuss this next, whereas the $K$-medoids clustering works for any dissimilarity function $L$.
A final introductory remark is that in (9.34) we do not scale with the cluster sizes, thus, we simultaneously balance the cluster size and the total within-cluster dissimilarity. Alternatively, we could scale with the cluster sizes $\left|\mathcal{X}_{k}\right|$.

## $K$-means clustering

For $K$-means clustering we select the squared Euclidean distance as dissimilarity function

$$
L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right)=\left\|\boldsymbol{X}_{i}-\boldsymbol{X}_{i^{\prime}}\right\|_{2}^{2}
$$

## Page 185
The consequence of this choice is that the empirical cluster means (9.35) minimize the within-cluster dissimilarities on the clusters $\mathcal{X}_{k}$. That is, we have for all $k \in \mathcal{K}$

$$
\boldsymbol{c}_{k}=\underset{\boldsymbol{c} \in \mathbb{R}^{q}}{\arg \min } \sum_{i \in \mathcal{X}_{k}}\left\|\boldsymbol{c}-\boldsymbol{X}_{i}\right\|_{2}^{2}=\frac{1}{\left|\mathcal{X}_{k}\right|} \sum_{i \in \mathcal{X}_{k}} \boldsymbol{X}_{i}
$$

Precisely this property is the reason for dropping the cluster center optimization in (9.34) for $K$-means clustering, and this motivates the name $K$-means clustering for this method. Thus, we aim at solving for the cluster centers (9.37)

$$
\left(\mathcal{X}_{k}^{*}\right)_{k \in \mathcal{K}}=\underset{\left(\mathcal{X}_{k}\right)_{k \in \mathcal{K}}}{\arg \min } \sum_{k=1}^{K} \sum_{i \in \mathcal{X}_{k}}\left\|\boldsymbol{c}_{k}-\boldsymbol{X}_{i}\right\|_{2}^{2}
$$

Initialization. We initialize the $K$-means algorithm by randomly allocating all instances $\left(\mathcal{X}_{i}\right)_{i=1}^{n}$ to the $K$ clusters (e.g., i.i.d. uniform). This defines the initial partition $\left(\mathcal{X}_{k}^{(0)}\right)_{k \in \mathcal{K}}$ as well as the initial cluster centers $\left(\boldsymbol{c}_{k}^{(0)}\right)_{k \in \mathcal{K}}$ by the corresponding empirical cluster means (9.37) on these initial clusters $\left(\mathcal{X}_{k}^{(0)}\right)_{k \in \mathcal{K}}$.

Recursive $K$-means iteration. We repeat for $t \geq 1$ until no more changes are observed:
(1a) Given the present empirical cluster means $\left(\boldsymbol{c}_{k}^{(t-1)}\right)_{k \in \mathcal{K}}$, we update the partition $\left(\mathcal{X}_{k}^{(t)}\right)_{k \in \mathcal{K}}$ by computing for each instance $1 \leq i \leq n$ the optimal allocation

$$
k_{t}^{*}(i)=\underset{k \in \mathcal{K}}{\arg \min }\left\|\boldsymbol{c}_{k}^{(t-1)}-\boldsymbol{X}_{i}\right\|_{2}^{2}
$$

with a deterministic rule if there is more than one minimizer. This gives us the new clusters at algorithmic time $t$

$$
\mathcal{X}_{k}^{(t)}=\{i \in\{1, \ldots, n\} ; k_{t}^{*}(i)=k\}
$$

(1b) Given the new clusters $\left(\mathcal{X}_{k}^{(t)}\right)_{k \in \mathcal{K}}$, we update the empirical cluster means $\left(\boldsymbol{s}_{k}^{(t)}\right)_{k \in \mathcal{K}}$ according to (9.37); these two steps (1a) and (1b) are illustrated in Figure 9.7.

Observe that at algorithmic step $t$ the total within-cluster dissimilarity is given by

$$
D(t)=\sum_{k=1}^{K} \sum_{i \in \mathcal{X}_{k}^{(t)}}\left\|\boldsymbol{c}_{k}^{(t)}-\boldsymbol{X}_{i}\right\|_{2}^{2} \geq 0
$$

The crucial point in the above algorithm is that both steps (1a) and (1b) are not increasing the total within-cluster dissimilarity $D(t)$ for increasing $t$. Having a lower bound zero and the fact that a finite sample can only be allocated in finitely many different ways to $K$ clusters implies that we have convergence

$$
\lim _{t \rightarrow \infty} D(t)=D\left(t^{*}\right) \in[0, \infty)
$$

in finitely many steps $t^{*} \in \mathbb{N}_{0}$.

## Page 186
Figure 9.8: Decrease of total within-cluster dissimilarity as a function of the number of clusters $K$; taken from [183].

The drawback is that $\left(\mathcal{X}_{k}^{\left(t^{*}\right)}\right)_{k \in \mathcal{K}}$ typically is a local minimum of the total within-cluster dissimilarity, and different initial configurations may converge to different (local) minimums.

An open question is the selection of the number of clusters $K$. This could be determined recursively as follows. Construct an optimal partition $\left(\mathcal{X}_{k}^{\left(t^{*}\right)}\right)_{k=1}^{K}$ for a given $K$. For the increased number of clusters $K+1$, initialize the $(K+1)$-means algorithm by the optimal clusters for parameter $K$, and randomly partition one of these clusters into two clusters. This implies that the total within-cluster dissimilarity decreases when going from $\left(\mathcal{X}_{k}^{\left(t^{*}\right)}\right)_{k=1}^{K}$ to $\left(\mathcal{X}_{k}^{(0)}\right)_{k=1}^{K+1}$. Then, run the algorithm in this increased setting with this initialization, and monotonicity implies that this new solution for $K+1$ clusters has a smaller total within-cluster dissimilarity. This results in a graph as in Figure 9.8 that is decreasing in $K$. An elbow criterion selects $K^{*}$ where this graph has a kink, in Figure 9.8 this might by for $K^{*}=4$.

# $K$-medoids clustering 

The $K$-means clustering algorithm requires that we consider the squared Euclidean distance as the dissimilarity function $L$. Of course, this is not always suitable, e.g., if we have a network where we need to travel from $\boldsymbol{X}_{i} \in \mathbb{R}^{2}$ to $\boldsymbol{X}_{i^{\prime}} \in \mathbb{R}^{2}$, the traveling costs are rather related to the Euclidean distance, but not to the squared Euclidean distance. However, $K$-means clustering cannot deal with this Euclidean distance problem. The $K$-medoids algorithm is more flexible and it can deal with any dissimilarity function $L$. This comes at the price of higher computational costs, because we cannot simply select the empirical cluster means as the cores $\left(\boldsymbol{c}_{k}\right)_{k \in \mathcal{K}}$. Instead, we need to compute the medoids $\left(\boldsymbol{c}_{k}\right)_{k \in \mathcal{K}}$ to receive a monotonically decreasing algorithm. The (optimal) medoids
![Page 186 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p186_img1.jpg)

## Page 187
are given by

$$
\left(\boldsymbol{c}_{k}\right)_{k \in \mathcal{K}}=\underset{\left(\boldsymbol{c}_{k}\right)_{k \in \mathcal{K}} \subset \mathcal{L}}{\arg \min } \sum_{k=1}^{K} \sum_{i \in \mathcal{X}_{k}} L\left(\boldsymbol{c}_{k}, \boldsymbol{X}_{i}\right)
$$

i.e., the medoids $\boldsymbol{c}_{k} \in \mathcal{L}=\left(\boldsymbol{x}_{i}\right)_{i=1}^{n}$ belong to the observed sample; again we install a deterministic rule if the argument in the minimum is not unique.

Similar to $K$-means clustering, the global minimum can generally not be found, therefore, we try to find a local minimum. Usually, the partitioning around medoids (PAM) algorithm of Kaufman-Rousseeuw [115] is exploited to solve the $K$-medoids clustering.

Initialization. Choose at random $K$ different initial medoids $\boldsymbol{c}_{1}, \ldots, \boldsymbol{c}_{K} \in \mathcal{X}$. Allocate each instance $\boldsymbol{X}_{i} \in \mathcal{L}$ to its closest medoid w.r.t. the selected dissimilarity measure $L$. This provides the initial total within-cluster dissimilarity

$$
D=\sum_{k=1}^{K} \sum_{i \in \mathcal{X}_{k}} L\left(\boldsymbol{c}_{k}, \boldsymbol{X}_{i}\right) \geq 0
$$

Recursive $K$-medoids iteration. We repeat until no more changes are observed:
(1a) Select a present medoid $\boldsymbol{c}_{k}$ and a non-medoid $\boldsymbol{X}_{i} \in \mathcal{L} \backslash\left(\boldsymbol{c}_{k}\right)_{k \in \mathcal{K}}$, swap the role of $\boldsymbol{c}_{k}$ and $\boldsymbol{X}_{i}$, and allocate each instance in $\mathcal{L}$ to the closest medoid in this new configuration;
(1b) compute the new total within-cluster dissimilarity (9.40) under this new configuration;
(1c) if the total within-cluster dissimilarity increases under this new configuration reject the swap, otherwise keep it.

Remark that there are many variants on how the swap in step (1a) can be selected (in a systematic way). Kaufman-Rousseeuw [115] provide one version which is also described in Algorithm 2 of Schubert-Rousseeuw [201], but there are many other possibilities that may provide computational improvements.

# 9.3.3 Clustering using Gaussian mixture models 

The $K$-means and $K$-medoids algorithms are based on the implicit assumption that the dissimilarity has a hard decision boundary. GMMs are distribution-based clustering methods that allow for soft decision boundaries accounting for some instances lying in the 'wrong' cluster. The basic assumption is that we have a mixture of $K$ multivariate Gaussian distributions that are assumed to have generated the instances $\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$. Thus, it is assumed that these instances were generated i.i.d. from a Gaussian mixture distribution having density

$$
f(\boldsymbol{x})=\sum_{k=1}^{K} p_{k} \frac{1}{\left(2 \pi\left|\Sigma_{k}\right|\right)^{q / 2}} \exp \left\{-\frac{1}{2}\left(\boldsymbol{x}-\boldsymbol{c}_{k}\right)^{\top} \Sigma_{k}^{-1}\left(\boldsymbol{x}-\boldsymbol{c}_{k}\right)\right\}
$$

## Page 188
with mean vectors $\left(\boldsymbol{c}_{k}\right)_{k \in \mathcal{K}} \subset \mathbb{R}^{q}$, positive definite covariance matrices $\Sigma_{k} \in \mathbb{R}^{q \times q}, 1 \leq$ $k \leq K$, and mixture probabilities $\left(p_{k}\right)_{k \in \mathcal{K}} \subset(0,1)$ aggregating to one, $\sum_{k=1}^{K} p_{k}=1$. This density gives a multivariate GMM with model parameter

$$
\vartheta=\left(\boldsymbol{\mu}_{k}, \Sigma_{k}, p_{k}\right)_{k \in \mathcal{K}}
$$

If we want to estimate this parameter with MLE, we need to consider the log-likelihood function for the given learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$

$$
\vartheta \mapsto \ell_{\mathcal{L}}(\vartheta)=\sum_{i=1}^{n} \log \left(\sum_{k=1}^{K} \frac{p_{k}}{\left(2 \pi\left|\Sigma_{k}\right|\right)^{q / 2}} \exp \left\{-\frac{1}{2}\left(\boldsymbol{X}_{i}-\boldsymbol{c}_{k}\right)^{\top} \Sigma_{k}^{-1}\left(\boldsymbol{X}_{i}-\boldsymbol{c}_{k}\right)\right\}\right)
$$

It is well-known that this MLE problem cannot be solved directly. In fact, it is not even clear whether a MLE for $\vartheta$ exists. There are many examples where this log-likelihood function is unbounded, henceforth, there is no MLE for $\vartheta$ in such cases.
For these reasons, one is less ambitious, and one just tries to find an estimator for $\vartheta$ that explains the learning sample reasonable well (is not a spurious solution in jargon). State-of-the-art uses variants of the expectation-maximization (EM) algorithm to find such solutions. We will not describe the EM algorithm here, but we refer to Dempster et al. [52], Wu [237] and McLachlan-Krishnan [152]. There are many different implementations of the EM algorithm, and for GMM clustering there are many variants relating to different choices of the covariance matrices $\Sigma_{k}$. E.g., if we decouple this covariance matrix according to $\Sigma_{k}=\lambda_{k} D_{k} A_{k} D_{k}^{\top}$ with a scalar $\lambda_{k}>0$, an orthogonal matrix $D_{k}$ containing the eigenvectors, and a diagonal matrix $A_{k}$ that is proportional to the eigenvalues of $\Sigma_{k}$, then one can fix some of these choices and exclude them from the MLE optimization. One choice is identical orientations $D_{k}=$ Id (identity matrices), equal volumes $\lambda_{k}=\lambda>0$, and $A_{k}$ can then provide different ellipsoids. Finally, the GMM clustering is obtained by allocating $\boldsymbol{X}_{i}$ to the estimated GMM component that provides the biggest log-likelihood.

# 9.3.4 Density-based clustering 

Density-based clustering focuses on constructing clusters that are sufficiently dense. We assume that the dissimilarity function $L$ is symmetric in its arguments. We select a neighborhood radius $\varepsilon>0$ and a critical density value $M \in \mathbb{N}$. This value $M$ is the minimal number of instances $\boldsymbol{X}_{i^{\prime}}$ in the $\varepsilon$-neighborhood of a considered instance $\boldsymbol{X}_{i}$, to declare this instance $\boldsymbol{X}_{i}$ to be a core instance. Thus, we need to count the number of instances in the $\varepsilon$-neighborhood of each instance $\boldsymbol{X}_{i}, 1 \leq i \leq n$,

$$
m_{i}=\sum_{i^{\prime} \neq i} \mathbb{1}_{\left\{L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right) \leq \varepsilon\right\}}
$$

This allows us to define the set of core instances

$$
\mathcal{C}=\left\{i \in\{1, \ldots, n\} ; m_{i} \geq M\right\}
$$

The DBSCAN method of Ester et al. [64] is obtained by constructing a graph of vertices and edges from these core instances $\mathcal{C}$ :

Version March 3, 2025, @AI Tools for Actuaries

## Page 189
(1) The vertices are given by all core instances $\boldsymbol{X}_{i} \in \mathcal{C}$, and we add an edge between two core instances $\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}} \in \mathcal{C}$ if they are in the $\varepsilon$-neighborhood of each other, i.e., if $L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right) \leq \varepsilon$. This gives a graph with vertices and edges, and we define the clusters to be the connected components of this graph.
(2) There are still the instances $\boldsymbol{X}_{l} \in \mathcal{L} \backslash \mathcal{C}$ that are not core instances. If such a non-core instance $\boldsymbol{X}_{l}$ is in the $\varepsilon$-neighborhood of at least one core instance $\boldsymbol{X}_{i}$, i.e., if $L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{l}\right) \leq \varepsilon$ for at least one core instance $\boldsymbol{X}_{i} \in \mathcal{C}$, then we assign it (at random) to one of these close core instances by adding an edge from $\boldsymbol{X}_{l}$ to $\boldsymbol{X}_{i}$. This increases the corresponding connected component of that core instance $\boldsymbol{X}_{i}$, but because the graph ends in $\boldsymbol{X}_{l}$ (there is no further edge in $\boldsymbol{X}_{l}$ ), this non-core instance is an isolated (satellite) point that is only connected to $\boldsymbol{X}_{i}$.
Finally, there are the so-called outliers $\boldsymbol{X}_{l}$ with $L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{l}\right)>\varepsilon$ for all core instances $\boldsymbol{X}_{i} \in \mathcal{C}$. These are treated as noise, and they are not assigned to any cluster.

Advantages of DBSCAN are that the number of clusters is flexible, and the resulting structures of the clusters can have any shape. Such a structure may be useful if one tries to describe how things spread (in a graph-like manner by nearest neighbor infections), but also for disaster modeling, e.g., one may use such graph to model the spread of a fire.

# 9.4 Low-dimensional visualization methods 

Visualization methods are more of a topological nature trying to preserve neighborhoods. Popular methods are the $t$-SNE method of van der Maaten-Hinton [223], UMAP of McInnes et al. [151] or SOM by Kohonen [122, 123, 124]. We only present the $t$-SNE method here and for the other methods we refer to the relevant literature.
These visualization methods are based on finding instances $\left(\boldsymbol{Z}_{i}\right)_{i=1}^{n}$ in a lower dimensional space, say, $\mathbb{R}^{2}$, such that there is (some) similarity in the distance functions generate by the learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n} \subset \mathbb{R}^{q}$ and this sequence $\left(\boldsymbol{Z}_{i}\right)_{i=1}^{n} \subset \mathbb{R}^{2}$. This motivates to solve minimization problems of the type

$$
\underset{\left(\boldsymbol{Z}_{i}\right)_{i=1}^{n} \subset \mathbb{R}^{2}}{\arg \min } \sum_{1 \leq i, i^{\prime} \leq n}\left(L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right)-\left\|\boldsymbol{Z}_{i}-\boldsymbol{Z}_{i^{\prime}}\right\|_{2}\right)^{2}
$$

In other words, we try to find a sample $\left(\boldsymbol{Z}_{i}\right)_{i=1}^{n}$ in the two-dimensional Euclidean space such that the original adjacency matrix

$$
\left(L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right)\right)_{1 \leq i, i^{\prime} \leq n} \in \mathbb{R}_{+}^{n \times n}
$$

is preserved as good as possible. This idea is similar to most visualization methods.
The $t$-SNE method of van der Maaten-Hinton [223] is considering an embedding that slightly modifies the above idea. Namely, we are going to map the dissimilarity $L\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}}\right)$ to a categorical distribution $\boldsymbol{q}=\left(q_{j}\right)_{j=1}^{J}$. Equivalently, we are going to find a $t$-distribution with instances $\left(\boldsymbol{Z}_{i}\right)_{i=1}^{n}$ whose dissimilarities can be mapped to a second categorical distribution $\boldsymbol{p}=\left(p_{j}\right)_{j=1}^{J}$. Instead of minimizing (9.43) we try to make the KL divergence from $\boldsymbol{p}$ to $\boldsymbol{q}$ small

$$
D_{\mathrm{KL}}(\boldsymbol{q} \| \boldsymbol{p})=\sum_{j=1}^{J} q_{j} \log \left(\frac{q_{j}}{p_{j}}\right)
$$

## Page 190
The KL divergence is zero if and only if $\boldsymbol{q}=\boldsymbol{p}$; this is proved by Jensen's inequality.

Original sample. For two instances $\boldsymbol{X}_{i}, \boldsymbol{X}_{i^{\prime}} \in \mathcal{L}$ one defines the conditional probability weight

$$
q_{i^{\prime} \mid i}=\frac{\exp \left\{-\frac{1}{2 \sigma_{i}^{2}}\left\|\boldsymbol{X}_{i^{\prime}}-\boldsymbol{X}_{i}\right\|_{2}^{2}\right\}}{\sum_{k \neq i} \exp \left\{-\frac{1}{2 \sigma_{i}^{2}}\left\|\boldsymbol{X}_{k}-\boldsymbol{X}_{i}\right\|_{2}^{2}\right\}} \in(0,1), \quad \text { for } i \neq i^{\prime}
$$

The choice of the bandwidth $\sigma_{i}>0$ is discussed below. The explanation of (9.45) is that $q_{i^{\prime} \mid i}$ gives the probability of selecting $\boldsymbol{X}_{i^{\prime}}$ as the neighbor of $\boldsymbol{X}_{i}$ from all instances, under a Gaussian kernel similarity measure, i.e., $\boldsymbol{X}_{i}$ is the center (core) of these conditional probabilities.
Since $q_{i^{\prime} \mid i}$ is non-symmetric, a symmetrized version is defined by

$$
q_{i, i^{\prime}}=\frac{1}{2 n}\left(q_{i^{\prime} \mid i}+q_{i \mid i^{\prime}}\right) \in(0,1), \quad \text { for } i \neq i^{\prime}
$$

Note, we exclude the diagonal from these definitions. Observe that $\sum_{i^{\prime} \neq i} q_{i^{\prime} \mid i}=1$ for all $1 \leq i \leq n$. This implies that $\sum_{i=1}^{n} \sum_{i^{\prime} \neq i} q_{i, i^{\prime}}=1$ and, henceforth, $\boldsymbol{q}=\left(q_{i, i^{\prime}}\right)_{i \neq i^{\prime}}$ is a categorical distribution with $J=n^{2}-n$ components.

Visualization sample. Select a fixed dimension $p<q$. The goal is to find a visualization sample $\left(\boldsymbol{Z}_{i}\right)_{i=1}^{n} \subset \mathbb{R}^{p}$ such that its Student- $t$ probabilities $\boldsymbol{p}=\left(p_{i, i^{\prime}}\right)_{i \neq i^{\prime}}$ (with one degree of freedom which is the Cauchy distribution), and defined by

$$
p_{i, i^{\prime}}=\frac{\left(1+\left\|\boldsymbol{Z}_{i}-\boldsymbol{Z}_{i^{\prime}}\right\|_{2}^{2}\right)^{-1}}{\sum_{k \neq l}\left(1+\left\|\boldsymbol{Z}_{k}-\boldsymbol{Z}_{l}\right\|_{2}^{2}\right)^{-1}} \in(0,1), \quad \text { for } i \neq i
$$

are close to the categorical distribution $\boldsymbol{q}=\left(q_{i, i^{\prime}}\right)_{i \neq i^{\prime}}$ of the original sample $\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$.
This motivates the following minimization problem

$$
\left(\boldsymbol{Z}_{i}^{*}\right)_{i=1}^{n} \in \underset{\left(\boldsymbol{Z}_{i}\right)_{i=1}^{n}}{\arg \min } D_{\mathrm{KL}}(\boldsymbol{q} \| \boldsymbol{p})=\underset{\left(\boldsymbol{Z}_{i}\right)_{i=1}^{n}}{\arg \min } \sum_{i \neq i^{\prime}} q_{i, i^{\prime}} \log \left(\frac{q_{i, i^{\prime}}}{p_{i, i^{\prime}}}\right)
$$

This optimization problem is usually solved with the gradient descent algorithm.
Remarks 9.6. - There is some discrepancy in the definition of $\boldsymbol{q}$ and $\boldsymbol{p}$. For the high-dimension case, we define $\boldsymbol{q}$ via the conditional probabilities (9.46). This approach has turned to be more robust towards outliers. In the low-dimensional case we can directly define $\boldsymbol{p}$ by (9.47).

- The Student- $t$ distribution is heavy-tailed (regularly varying), and for one degree of freedom (Cauchy case) we have a quadratic asymptotic decay $p_{i, i^{\prime}} \approx\left\|\boldsymbol{Z}_{i}-\boldsymbol{Z}_{i^{\prime}}\right\|_{2}^{-2}$ for $\left\|\boldsymbol{Z}_{i}-\boldsymbol{Z}_{i^{\prime}}\right\|_{2} \rightarrow \infty$.

## Page 191
- There remains the choice of the bandwidth $\sigma_{i}>0$. Typically, a smaller value for $\sigma_{i}>0$ gives a denser clustering. For $\boldsymbol{q}_{\bullet|i}=\left(q_{i^{\prime} \mid i}\right)_{i^{\prime} \neq i}$, one can define the perplexity

$$
\operatorname{Perp}\left(\boldsymbol{q}_{\bullet \mid i}\right)=\exp \left\{H\left(\boldsymbol{q}_{\bullet \mid i}\right)\right\}=\exp \left\{-\sum_{i^{\prime} \neq i} q_{i^{\prime} \mid i} \log _{2}\left(q_{i^{\prime} \mid i}\right)\right\}
$$

with $H\left(\boldsymbol{q}_{\bullet \mid i}\right)$ being the Shannon entropy. Following van der Maaten-Hinton [223], a good choice of the bandwidths $\sigma_{i}$ is received by a constant perplexity $\operatorname{Perp}\left(\boldsymbol{q}_{\bullet \mid i}\right)$ in $i$.

Figure 9.9: $t$-SNE visualizations from a five-dimensional sample $\left(\boldsymbol{X}_{i}\right)_{i=1}^{n} \subset \mathbb{R}^{5}$ to a twodimensional illustration $\left(\boldsymbol{Z}_{i}\right)_{i=1}^{n} \subset \mathbb{R}^{2}$ for different values of the perplexity parameter.

Figure 9.9 gives an example where we map a learning sample $\left(\boldsymbol{X}_{i}\right)_{i=1}^{n} \subset \mathbb{R}^{5}$ that is five-dimensional to a two-dimensional illustration $\left(\boldsymbol{Z}_{i}\right)_{i=1}^{n} \subset \mathbb{R}^{2}$. We use the R package tsne [58] which has a hyper-parameter called perplexity. Figure 9.9 shows the results for different values of this perplexity parameter. The colors are in all plots identical for the instances, and the specific meaning of the colors is related to a sports car evaluation with red color being a sports car; for details see Rentzmann-Wüthrich [183].
![Page 191 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p191_img1.jpg)

## Page 192
Version March 3, 2025, @AI Tools for Actuaries

## Page 193
# Chapter 10 

## Generative modeling

### 10.1 Introduction

Most of the applications considered in these notes follow the classical paradigm of supervised learning, introduced in Chapters 1 and 2, which is to infer the best approximation to an unknown regression function from a finite sample of data. Once this regression function has been learned, this function can be used to compute point estimates of interest, including, e.g., best estimates and estimates of quantiles of distributions. Within actuarial science, this paradigm of learning a regression function and a best estimate, respectively, encompasses a large proportion of tasks focused on prediction. Nonetheless, some tasks performed quite often by actuaries stand outside this paradigm, where, instead of producing point estimates, it is desired or necessary to produce a full predictive distribution. For example, in non-life reserving, besides a point estimate of reserves, it is usually important to produce a distribution of the outstanding loss liabilities, both to communicate the uncertainty of the point estimate (reserves) and to quantify the capital and margins needed to back the reserves. We briefly also mention capital modeling applications, whether parameterizing (simple) statistical distributions to model a full distribution of prospective insurance risks, or using dimensionality reduction tools, such as those introduced in the previous chapter, to reduce complex observations of market variables or mortality rates down to tractable quantities to enable modeling; a classical example here is interest rate modeling. These tasks can be characterized as generative modeling, which has as the goal to learn the underlying probability distribution $\boldsymbol{X} \sim \mathbb{P}$ of the instances itself, or a joint distribution of responses and covariates $(Y, \boldsymbol{X}) \sim \mathbb{P}$; we refer to Section 1.2.3. ${ }^{1}$

Once we have learned a good approximation to this distribution of the data, we can:
(1) Generate new samples: Draw new instances $\boldsymbol{X} \sim \mathbb{P}$ that resemble the data the model was trained on. This is useful for data augmentation, simulating scenarios, and creating synthetic data.
(2) Estimate probabilities: Evaluate the likelihood $p(\boldsymbol{X})$ of a given data point $\boldsymbol{X}$, which is useful, e.g., for anomaly detection.

[^0]
[^0]:    ${ }^{1}$ For simplicity, we drop the volume/weight in this chapter, by assuming $v \equiv 1$.

## Page 194
(3) Infer latent representations: Learn a compressed, lower-dimensional representation $\boldsymbol{Z}$ of the data $\boldsymbol{X}$ (similar to the auto-encoder examples in Section 9.2.2), which can reveal underlying structure, e.g., through visualizations of $\boldsymbol{Z}$.
(4) Perform conditional data generation: Generate new samples from a conditional distribution $\left.\boldsymbol{X}\right|_{Y} \sim \mathbb{P}(\cdot \mid Y)$, allowing for targeted data synthesis.

What distinguishes generative modeling from the unsupervised learning applications discussed in Section 9 - some of which also focus on producing latent factors $\boldsymbol{Z}$ - is exactly this goal of producing a learned probability distribution $\boldsymbol{X} \sim \mathbb{P}$ of the data $\boldsymbol{X}$.

Notation. We remark that in this field of literature, one typically uses the notation $p(\boldsymbol{X})$ for the density and the likelihood of $\boldsymbol{X} \sim \mathbb{P}$, we adopt this convention (which is in slight conflict with our previous notation).

Goal: Infer (or approximate) the true probability distribution $\boldsymbol{X} \sim \mathbb{P}$ (or density $p(\boldsymbol{X})$ ) from a finite sample $\mathcal{L}$ of (past) observations.

Major recent advances in generative modeling have been driven by the use of deep neural networks to learn probability distributions over complex, high-dimensional data; these so-called deep generative models (DGMs) have been extraordinarily successful in applications in natural language processing (NLP) and image generation. We parameterize this distribution with parameter $\vartheta$, writing $p_{\vartheta}(\boldsymbol{X})$, where $\vartheta \in \mathbb{R}^{r}$ represents the network parameter that needs to be learned from observed data. Various approaches have been proposed in the literature for the task of deep generative modeling; we refer to Tomczak [220] for an overview.

Here, we mainly discuss two of these approaches: the latent factor and implicit probability distribution approaches.
(1) The latent factor approach is to assume a parametric model

$$
p_{\vartheta}(\boldsymbol{X})=\int p_{\vartheta}(\boldsymbol{X} \mid \boldsymbol{z}) \pi(\boldsymbol{z}) \mathrm{d} \boldsymbol{z}
$$

where $\boldsymbol{z}$ denotes latent variables capturing unobserved factors that create variability in the data samples, and $\pi(\boldsymbol{z})$ is a prior distribution over these latent variables; this prior distribution can also be set as a very weak prior or as flat one in some cases.
The deep neural network components can parameterize both

- the conditional likelihood $p_{\vartheta}(\boldsymbol{X} \mid \boldsymbol{z})$, and
- the latent distribution $\pi(\boldsymbol{z})$ or, more commonly, the conditional distribution $\left.\boldsymbol{Z}\right|_{\boldsymbol{X}} \sim$ $q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{X})$ in variational inference frameworks, where $\vartheta$ contains both, the parameters of the conditional likelihood $p_{\vartheta}$ and the variational inference posterior $q_{\vartheta}$.

In practice, we choose flexible neural-network-based functions to map between $\boldsymbol{X}$ and $\boldsymbol{Z}$ (encoder) and from $\boldsymbol{Z}$ to (new) data $\boldsymbol{X}$ (decoder).

## Page 195
Variational auto-encoders (VAEs) are a typical example of this latent factor approach, where the encoder network approximates the posterior $q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{X})$, and the decoder network approximates the likelihood $p_{\vartheta}(\boldsymbol{X} \mid \boldsymbol{z})$; in what follows, we will extend the autoencoders introduced in Section 9.2.2 into this variational approach. We also briefly mention the Generative Adversarial Networks (GANs) of Goodfellow et al. [84], which work by sampling directly from an assumed latent factor distribution $\boldsymbol{Z} \sim \pi(\boldsymbol{z})$, and the denoising diffusion models due to Ho et al. [99], which are another way of acting on samples from a latent factor distribution $\pi$.
(2) The implicit probability distribution is a different approach that does not rely on explicit latent factors $\boldsymbol{Z}$. Instead, a neural network can directly learn a conditional probability distribution over $\boldsymbol{X}=\left(X_{1}, \ldots, X_{T}\right)=X_{1: T}$. Concretely, for sequential data $X_{1: T}$ (such as text or time-series data), this probability distribution is represented by factorizing the joint distribution into a product of conditional terms, i.e., as an autoregressive factorization that takes the form

$$
p_{\vartheta}\left(X_{1: T}\right)=\prod_{t=1}^{T} p_{\vartheta}\left(X_{t} \mid X_{1: t-1}\right)
$$

where each term $p_{\vartheta}\left(X_{t} \mid X_{1: t-1}\right)$ is modeled by a neural network that conditions on the preceding elements of the sequence $X_{1: t-1}$.
In many cases - especially when each $X_{t}$ is categorical (e.g., a word in a vocabulary $\mathcal{W}$ ) - this network outputs a probability distribution via a softmax function, which is the natural parameterization for multinomial outcomes, see (8.10). Specifically, if the possible values for $X_{t}$ belong to some discrete set $\mathcal{W} \subset \mathbb{R}$, then for each $w \in \mathcal{W}$, the network produces outputs

$$
\operatorname{logits}(w)=\operatorname{logits}_{\vartheta}\left(X_{1: t-1} ; w\right)
$$

which are mapped to probabilities by the softmax transformation

$$
p_{\vartheta}\left(X_{t}=w \mid X_{1: t-1}\right)=\frac{e^{\operatorname{logits}(w)}}{\sum_{u \in \mathcal{W}} e^{\operatorname{logits}(u)}}
$$

where $\operatorname{logits}(\cdot)$ refers to the unnormalized probabilities before transforming back to the probability scale. This implicit approach obviates the need for latent variables by directly specifying how the next outcome depends on the past. In language modeling, for example, the model learns $p_{\vartheta}\left(X_{t} \mid X_{1: t-1}\right)$ over a vocabulary of possible tokens (words or subwords); we have already introduced these concepts in Section 8.2. In time-series forecasting, the same principle applies, although the data may be continuous or mixed-type, in which case alternative output layers can be used. In all such scenarios, the core idea is to define the probabilities over $\mathcal{W}$ of the next outcome - completely determined by the network rather than decomposing the distribution through auxiliary latent factors.

In modern NLP, transformer-based models have emerged as a powerful way to implement these auto-regressive approaches. In Section 8.5, we have introduced encoder transformers, which process a known sequence of tokens to produce an output. For NLP and other generative modeling purposes, decoder transformers are used, where the next-token in an

## Page 196
observed sequence is predicted; this prediction is then appended to the sequence and the following token is predicted, and so on. We will discuss decoder transformers and large language models in more detail below.

# 10.2 Variational auto-encoders 

### 10.2.1 Introduction and motivation

Variational auto-encoders (VAEs), introduced by Kingma and Welling [119, 120] and Rezende et al. [184], combine ideas from variational inference and the auto-encoder framework (see Section 9.2.2) to provide a probabilistic approach for both learning latent representations and generating new samples from an unknown distribution. In contrast to a standard auto-encoder - which learns a deterministic mapping from inputs $\boldsymbol{X}$ to a compressed latent representation $\boldsymbol{Z}$ and back to a reconstruction $\boldsymbol{X}^{\prime}$ - a VAE incorporates stochasticity into both the encoding and decoding processes. This allows the model to approximate the full distribution $p(\boldsymbol{X})$ of the data, rather than merely learning a pointwise reconstruction. Moreover, the latent factor distribution $\boldsymbol{Z} \sim \pi(\boldsymbol{z})$ is usually assumed to follow a multivariate isotropic normal distribution; once the encoding network has been trained, samples from $\pi(\boldsymbol{z})$ can be drawn in a principled manner.

Remark 10.1. We briefly mention that, within actuarial modeling utilizing PCA, although a multivariate isotropic normal distribution is not imposed during the PCA fitting, nonetheless, it is often assumed that the (orthogonal) principal components follow this distribution and samples are drawn from $\pi(\boldsymbol{z})$ on this basis. Of course, the independence of the principal components by design means that at least part of this assumption is justified; orthogonal components are independent under a multivariate Gaussian assumption. A nice extension of this approach is to use a density estimation on the factors $\boldsymbol{Z}$; see Ghosh et al. [73].

### 10.2.2 Variational auto-encoder model architecture

At a high level, a VAE is rather similar to the bottleneck neural network (BNN) presented in Section 9.2.4; the main difference is that we introduce distributional assumptions into these networks, as we now explain. A VAE consists of two core components, each parameterized by usually distinct sets of neural network parameters, which we collect into $\vartheta \in \mathbb{R}^{r}$ (in a slight abuse of notation):
(1) Encoder (inference/recognition model): The encoder network takes an input data point $\boldsymbol{X}$ and outputs the parameters of a latent distribution, typically an isotropic multivariate Gaussian distribution

$$
q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{X}) \stackrel{(\mathrm{d})}{=} \mathcal{N}\left(\boldsymbol{\mu}_{\vartheta}(\boldsymbol{X}), \Sigma_{\vartheta}(\boldsymbol{X})\right)
$$

Here, $\boldsymbol{\mu}_{\vartheta}(\boldsymbol{X})$ and $\Sigma_{\vartheta}(\boldsymbol{X})$ are given by the encoder's outputs, with $\Sigma_{\vartheta}(\boldsymbol{X})$ often constrained to be diagonal for simplicity. The encoder is thus learning an approximate posterior distribution over latent variables $\boldsymbol{Z}$, conditioned on $\boldsymbol{X}$. We will explain how this assumption is enforced using a regularization term in the next section.

## Page 197
(2) Decoder (generative model): The decoder network takes a latent sample $\boldsymbol{Z}$ and outputs parameters of a distribution over the data space

$$
p_{\vartheta}(\boldsymbol{x} \mid \boldsymbol{Z}) \stackrel{(\mathrm{d})}{\cong} \mathcal{N}\left(\boldsymbol{m}_{\vartheta}(\boldsymbol{Z}), S_{\vartheta}(\boldsymbol{Z})\right)
$$

for an absolutely continuous $\boldsymbol{X}$. If $\boldsymbol{X}$ is binary or discrete, it estimates the parameters of a Bernoulli or a discrete distribution. In practice, $\boldsymbol{m}_{\vartheta}(\boldsymbol{Z})$ and $S_{\vartheta}(\boldsymbol{Z})$ are also outputs of a (separate) neural network.

In summary, the decoder is the generative component: once trained, it can take random samples $\boldsymbol{Z} \sim \pi(\boldsymbol{z})$ from the latent space and produce synthetic data points by generating new data $\boldsymbol{X}^{\prime} \sim p_{\vartheta}(\boldsymbol{x} \mid \boldsymbol{Z})$ that resembles the original dataset.

# 10.2.3 Variational objective: the evidence lower bound 

As we mentioned above, deep generative modeling often seeks to approximate the (intractable) marginal likelihood $p_{\vartheta}(\boldsymbol{x})$. For VAEs, we write

$$
p_{\vartheta}(\boldsymbol{x})=\int p_{\vartheta}(\boldsymbol{x} \mid \boldsymbol{z}) \pi(\boldsymbol{z}) \mathrm{d} \boldsymbol{z}
$$

where $\pi(\boldsymbol{z})$ is a prior over latent variables, typically chosen as a standard Gaussian $\mathcal{N}(\mathbf{0}, \mathbf{I})$. Directly optimizing $\log p_{\vartheta}(\boldsymbol{x})$ is generally intractable, but we can employ variational inference to maximize a lower bound, the evidence lower bound (ELBO), for a full derivation and explanation, see Odaibo [169],

$$
\begin{aligned}
\log p_{\vartheta}(\boldsymbol{x}) & =\log \int p_{\vartheta}(\boldsymbol{x} \mid \boldsymbol{z}) \pi(\boldsymbol{z}) \mathrm{d} \boldsymbol{z} \\
& =\log \int \frac{p_{\vartheta}(\boldsymbol{x} \mid \boldsymbol{z}) \pi(\boldsymbol{z})}{q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{x})} q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{x}) \mathrm{d} \boldsymbol{z} \\
& =\log \mathbb{E}_{q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{x})}\left[\frac{p_{\vartheta}(\boldsymbol{x} \mid \boldsymbol{Z}) \pi(\boldsymbol{Z})}{q_{\vartheta}(\boldsymbol{Z} \mid \boldsymbol{x})}\right] \\
& \geq \mathbb{E}_{q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log \left(\frac{p_{\vartheta}(\boldsymbol{x} \mid \boldsymbol{Z}) \pi(\boldsymbol{Z})}{q_{\vartheta}(\boldsymbol{Z} \mid \boldsymbol{x})}\right)\right] \\
& =\mathbb{E}_{q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log p_{\vartheta}(\boldsymbol{x} \mid \boldsymbol{Z})\right]-D_{\mathrm{KL}}\left(q_{\vartheta}(\cdot \mid \boldsymbol{x}) \| \pi\right)=: \mathcal{E}(\vartheta ; \boldsymbol{x})
\end{aligned}
$$

where $\mathbb{E}_{q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{x})}[\cdot]$ is the expectation operator of $\boldsymbol{Z} \sim q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{x})$ and $D_{\mathrm{KL}}\left(q_{\vartheta}(\cdot \mid \boldsymbol{x}) \| \pi\right)$ is the KL divergence from $\pi$ to $q_{\vartheta}(\cdot \mid \boldsymbol{x})$; for the finite discrete case, see (9.44).

The term $\mathcal{E}(\vartheta ; \boldsymbol{x})$ is the ELBO and consists of two terms

- Reconstruction term: $\mathbb{E}_{q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log p_{\vartheta}(\boldsymbol{x} \mid \boldsymbol{Z})\right]$, which encourages the decoder to reconstruct the original $\boldsymbol{x}$ from the latent code $\boldsymbol{Z}$.
- Regularization term: $-D_{\mathrm{KL}}\left(q_{\vartheta}(\cdot \mid \boldsymbol{x}) \| \pi\right)$, which aligns the encoder's approximate posterior with the prior $\pi(\boldsymbol{z})$. As we have mentioned already, typically $\pi(\boldsymbol{z}) \stackrel{(\mathrm{d})}{\equiv}$ $\mathcal{N}(\mathbf{0}, \mathbf{I})$.

## Page 198
Combining these two terms yields a balance between, on the one hand, a faithful reconstructions and, on the other, a latent space constrained to follow the prior assumptions. For a learning sample $\mathcal{L}=\left(\boldsymbol{X}_{i}\right)_{i=1}^{n}$, training maximizes the average ELBO over the learning sample

$$
\arg \max _{\vartheta} \frac{1}{n} \sum_{i=1}^{n} \mathcal{E}\left(\vartheta ; \boldsymbol{X}_{i}\right)
$$

# Intuitive understanding of the ELBO 

The ELBO may appear mathematically imposing, but it can be understood through an intuitive lens. Imagine you are trying to compress data (like an image) into a compact code that captures its essential features, and then reconstruct it from this code. The ELBO represents a balance between two competing objectives:
(1) Reconstruction quality: How accurately can we reconstruct the original data from our compressed representation? This corresponds to the first term in the ELBO, $\mathbb{E}_{q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log p_{\vartheta}(\boldsymbol{x} \mid \boldsymbol{Z})\right]$. Higher values mean better reconstruction.
(2) Compression regularity: How 'well-behaved' is our compression scheme? Does it distribute information evenly, avoid redundancy, and make an efficient use of the available space? This corresponds to the KL divergence term, $-D_{\mathrm{KL}}\left(q_{\vartheta}(\cdot \mid \boldsymbol{x}) \| \pi\right)$. Smaller divergence means the compression follows our desired prior distribution $\pi$.

The ELBO elegantly combines these objectives into a single value to be maximized. When maximizing the ELBO, we are finding the best trade-off between accurate reconstructions and well-structured compressions. This is why VAEs often learn meaningful, disentangled representations - they are simultaneously optimizing for fidelity (reconstruction) and simplicity (regularization).

### 10.2.4 Reparameterization trick and training

As we have mentioned in Section 5.3.3, neural network training relies on calculating gradients from outputs of the network to the parameters. In the case of VAEs, one cannot calculate a direct gradient of $\mathbb{E}_{q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{x})}[\cdot]$ w.r.t. $\vartheta$, because this expression is too complex as the unknown parameter $\vartheta$ enters the density for the expected value computatation. However, under a Gaussian assumption there is a nice way out, called the reparameterization trick. Assume a Gaussian encoder (10.1). This allows us to rewrite the Gaussian random variable $\boldsymbol{Z}$ as follows

$$
\boldsymbol{Z} \stackrel{(\mathrm{d})}{=} \boldsymbol{\mu}_{\vartheta}(\boldsymbol{x})+\Sigma_{\vartheta}^{1 / 2}(\boldsymbol{x}) \boldsymbol{\varepsilon}, \quad \boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})
$$

Here, $\boldsymbol{\varepsilon}$ is independent of $\vartheta$, so we can backpropagate through the neural network outputs $\boldsymbol{\mu}_{\vartheta}(\boldsymbol{x})$ and $\Sigma_{\vartheta}(\boldsymbol{x})$ without any issues. That is, we can rewrite

$$
\mathbb{E}_{q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{x})}\left[\log p_{\vartheta}(\boldsymbol{x} \mid \boldsymbol{Z})\right]=\mathbb{E}\left[\log p_{\vartheta}\left(\boldsymbol{x} \mid \boldsymbol{\mu}_{\vartheta}(\boldsymbol{x})+\Sigma_{\vartheta}^{1 / 2}(\boldsymbol{x}) \boldsymbol{\varepsilon}\right)\right]
$$

where the parameter $\vartheta$ is no longer part of the expectation operator $\mathbb{E}[\cdot]$. The process then employs a Monte Carlo version by, first, sampling $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ in the forward pass,

## Page 199
and second, during the backward pass, taking the gradients w.r.t. the mean and variance parameters. A single Monte Carlo sample often suffices to approximate the ELBO

$$
\mathcal{E}(\vartheta ; \boldsymbol{x}) \approx \widetilde{\mathcal{E}}(\vartheta ; \boldsymbol{x}):=\log p_{\vartheta}\left(\boldsymbol{x} \mid \boldsymbol{\mu}_{\vartheta}(\boldsymbol{x})+\Sigma_{\vartheta}^{1 / 2}(\boldsymbol{x}) \boldsymbol{\varepsilon}\right)-D_{\mathrm{KL}}\left(q_{\vartheta}(\cdot \mid \boldsymbol{x}) \| \pi\right)
$$

By performing this Monte Carlo sampling during the fitting procedure, VAEs learn both the inference (encoder) and generative (decoder) networks by maximizing this Monte Carlo ELBO instead of (10.2). Once trained, we can generate new data by sampling $\boldsymbol{Z} \sim \pi(\boldsymbol{z})$ and then drawing $\boldsymbol{X}^{\prime} \sim p_{\vartheta}(\boldsymbol{x} \mid \boldsymbol{Z})$.

# The reparameterization trick: a visual analogy 

The reparameterization trick can be understood through a simple analogy. Imagine you are running a factory that produces custom-sized widgets. There are two ways to adjust the production:
(1) Direct approach (without reparameterization). You might randomly select a size for each widget directly from your target distribution. But if you need to adjust this distribution (e.g., make widgets larger on average), you would have to change your entire random selection process. This is difficult to optimize.
(2) Indirect approach (with reparameterization). Instead, you could start with standard-sized blanks (from a fixed, standard distribution) and then apply a consistent transformation to each blank (scaling and shifting). Now, if you need to adjust your output distribution, you only need to modify the transformation parameters, not the random selection process.

The reparameterization trick follows this second approach.

### 10.2.5 Discussion

VAEs illustrate the latent factor approach described earlier: the hidden variables $\boldsymbol{Z}$ capture underlying structure, and the encoder-decoder networks map between $\boldsymbol{X}$ and $\boldsymbol{Z}$. This ensures that VAEs can both reconstruct existing data and sample novel data points, all while maintaining a tractable training objective (the ELBO). In practice, many variants of VAEs exist, e.g., $\beta$-VAEs or conditional VAEs, each modifying the objective or architecture to emphasize different aspects, such as disentangled latent representations or conditional generation.
Overall, VAEs remain one of the most popular DGMs due to their relative conceptual simplicity, stable training procedure, and ability to produce both probabilistic encodings and realistic sample generations.

### 10.3 Other approaches related to latent factor models

In addition to VAEs, several other approaches related - more or less - to latent factor approaches have been proposed for deep generative modeling. In this section, we highlight

## Page 200
two popular methods - generative adversarial networks (GANs) and giffusion models and then we briefly compare how these approaches relate to each other and to VAEs.

# 10.3.1 Generative adversarial networks 

## Introduction

GANs, introduced by Goodfellow et al. [84], represent a different strategy for generative modeling. Unlike VAEs, which explicitly approximate a conditional probability distribution over the latent variables $\boldsymbol{Z} \sim q_{\vartheta}(\boldsymbol{z} \mid \boldsymbol{X})$ via a latent variable formulation, GANs implicitly learn to generate data directly from random latent factors $\boldsymbol{Z}$ sampled from conventional distributions by pitting two neural networks against each other in an adversarial game. In other words, the encoder part is missing from GANs. These two networks, the generator and the discriminator, evolve through a competitive process that can yield remarkably realistic samples in many domains - especially images - but unfortunately suffers from training difficulties.

## The GAN framework

A GAN comprises two main components:

- Generator $(G)$ : A neural network generator, parameterized by $\vartheta_{1} \in \mathbb{R}^{r_{1}}$, takes as input a random noise vector $\boldsymbol{Z} \sim \pi(\boldsymbol{z})$ (commonly a standard multivariate Gaussian distribution) and outputs a synthetic sample

$$
\boldsymbol{X}^{\prime}=G\left(\boldsymbol{Z} ; \vartheta_{1}\right)
$$

The generator's objective is to produce data that is indistinguishable from real data by the discriminator.

- Discriminator (D): A neural network discriminator, parameterized by $\vartheta_{2} \in \mathbb{R}^{r_{2}}$, receives either a real sample $\boldsymbol{X}$ (from the true dataset) or a synthetic sample $\boldsymbol{X}^{\prime}$ (from the generator), and outputs a scalar $D\left(\boldsymbol{X} ; \vartheta_{2}\right) \in[0,1]$. This scalar is interpreted as the probability that input $\boldsymbol{X}$ is 'real'. The discriminator aims to correctly distinguish real data from generated data.

The generator is designed to take a random noise vector and transform it into a generated output by processing the noise through several neural network layers. This process allows the generator to learn how to create realistic images from random inputs. On the other hand, the discriminator receives a sample as input and then processes it through a series of layers. It outputs a probability via a sigmoid activation function that indicates whether the sample is real, i.e., sampled from the dataset used to train the GAN, or generated by the generator network.
As in the earlier sections, we use $\vartheta$ generically to denote the model parameters, though in practice one typically maintains separate sets of parameters for $G$ and $D$, i.e., $\vartheta=$ $\left(\vartheta_{1}, \vartheta_{2}\right)$. These networks are trained simultaneously in a mini-max game.

## Page 201
# The GAN objective function 

GANs frame training as a zero-sum game between the generator and the discriminator. The value function is given by

$$
\min _{G} \max _{D} V(D, G)=\mathbb{E}_{\boldsymbol{X} \sim p_{\text {data }}(\boldsymbol{x})}[\log D(\boldsymbol{X})]+\mathbb{E}_{\boldsymbol{Z} \sim \pi(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{Z})))]
$$

Here:

- $\boldsymbol{X} \sim p_{\text {data }}(\boldsymbol{x})$ denotes the true (unknown) data distribution, i.e., $\boldsymbol{X} \sim \mathbb{P}$.
- $\boldsymbol{Z} \sim \pi(\boldsymbol{z})$ is the prior for the noise vector (often a Gaussian or uniform distribution).

The discriminator maximizes $V(D, G)$ to try to distinguish real versus fake samples. The generator minimizes $V(D, G)$, trying to "fool" the discriminator $D$ so that generated samples are classified as real. In practice, optimization is performed via alternating gradient-based updates.
The discriminator is trained using the binary cross-entropy loss function, which is suitable for binary classification tasks (real vs. fake); in fact, the log-likelihood of the Bernoulli distribution is given by $Y \log p+(1-Y) \log (1-p)$ which is the structure of the above minimax game.
The discriminator's weights are frozen during the training of the generator, meaning to say that while the GAN is being trained to improve the generator, only the generator's parameters are updated. The purpose of freezing the discriminator in this step is to ensure that updates are made only to the generator network, allowing it to learn how to produce images that can optimally fool the discriminator. In other words, while optimizing the generator, the discriminator's weights remain fixed and serve only to provide a training signal (the discriminator's classification score) for the generator. This setup ensures that only the generator's parameters adjust, learning progressively how to create samples that can fool the current state of the discriminator.
Training GANs is known to be difficult and can suffer from issues such as mode collapse (where the generator learns to produce only a limited variety of samples) or vanishing gradients. Despite these challenges, with proper techniques (e.g., careful network design, hyperparameter tuning, and objective variants like Wasserstein GAN [4]), GANs can generate highly detailed and convincing samples.

### 10.3.2 Diffusion models

## Introduction and motivation

Diffusion models, also referred to as score-based generative models, see Song-Ermon [209], have recently gained significant attention as a state-of-the-art approach for image and audio generation, see Ho et al. [99]. Unlike VAEs and GANs, which rely on (possibly) low-dimensional latent factors or adversarial training objectives, diffusion models employ a forward noising process paired with a reverse denoising process. The forward process systematically corrupts data into noise, and the reverse process - learned by a neural network - seeks to recover clean data from noisy samples. Thus, at generation time, one simply starts from random noise and iteratively applies the learned reverse process

## Page 202
to obtain a final synthetic sample. Similar to GANs, there is no need for an encoder model within the diffusion modeling paradigm and, moreover, we do not approximate conditional latent factors, but we rather learn implicitly directly from random samples.

# Forward and reverse processes 

A typical forward noising process (following [208, 99]) is defined as a Markov chain of length $T$. Starting with a real data sample $\boldsymbol{X}_{0}$ (e.g., an image), we produce a sequence of increasingly noisy samples

$$
\boldsymbol{X}_{1}, \boldsymbol{X}_{2}, \ldots, \boldsymbol{X}_{T}
$$

where each step $\boldsymbol{X}_{t}$ is obtained by adding a small amount of Gaussian noise to $\boldsymbol{X}_{t-1}$. Concretely, one common choice is

$$
q\left(\boldsymbol{X}_{t} \mid \boldsymbol{X}_{t-1}\right) \stackrel{(\mathrm{d})}{=} \mathcal{N}\left(\sqrt{1-\beta_{t}} \boldsymbol{X}_{t-1}, \beta_{t} \mathbf{I}\right)
$$

with a variance schedule $\left\{\beta_{t}\right\}_{t=1}^{T} \in(0,1)$. After iterating this for sevaral steps, the sample is nearly indistinguishable from pure Gaussian noise (supposed that the variance schedule adds sufficient noise).

## Training objective

Training aims to learn the reverse distribution $p_{\vartheta}\left(\boldsymbol{X}_{t-1} \mid \boldsymbol{X}_{t}\right)$ so as to maximize the likelihood of clean samples under the implied marginal distribution. One way to view this is through a variational perspective, see Sohl-Dickstein et al. [208], which yields an ELBO on the negative log-likelihood of $\boldsymbol{X}_{0}$. However, Ho et al. [99] propose a simplified (yet empirically effective) noise-prediction objective, in which a neural network is trained to predict the noise $\varepsilon$ that was added at each forward step. Concretely:

- Let $\boldsymbol{X}_{0}$ be a real sample and $\varepsilon \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ be drawn independently.
- Define the noised version of $\boldsymbol{X}_{0}$ at step $t$ via

$$
\boldsymbol{X}_{t}=\sqrt{\alpha_{t}} \boldsymbol{X}_{0}+\sqrt{1-\alpha_{t}} \boldsymbol{\varepsilon}
$$

where $\alpha_{t}=\prod_{s=1}^{t}\left(1-\beta_{s}\right)$.

- The neural network $\boldsymbol{\epsilon}_{\vartheta}$ (often a U-Net, see Ronneberger et al. [195], which is a type of encoder-decoder CNN framework useful for working with images or similar architectures) is trained to predict $\boldsymbol{\varepsilon}$ from $\left(\boldsymbol{X}_{t}, t\right)$. The training loss commonly used is

$$
L_{\text {simple }}(\vartheta)=\mathbb{E}_{\boldsymbol{X}_{0}, \boldsymbol{\varepsilon}, t}\left[\left\|\boldsymbol{\varepsilon}-\boldsymbol{\epsilon}_{\vartheta}\left(\boldsymbol{X}_{t}, t\right)\right\|_{2}^{2}\right]
$$

By minimizing this loss, the model learns to "denoise" $\boldsymbol{x}_{t}$ at each time step, effectively approximating the score function (the gradient of the log-density w.r.t. the data) and providing a route to reverse the forward chain.

## Page 203
# Sampling and generation 

Once trained, sampling proceeds by starting with $\boldsymbol{X}_{T} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ and recursively applying

$$
\boldsymbol{X}_{t-1} \sim p_{\vartheta}\left(\boldsymbol{x}_{t-1} \mid \boldsymbol{X}_{t}\right), \quad t=T, \ldots, 1
$$

to obtain a final sample $\boldsymbol{X}_{0}$ that resembles the data distribution. In practice, the neural network predicts either the noise $\boldsymbol{\varepsilon}$ or the clean image $\boldsymbol{X}_{0}$ from $\left(\boldsymbol{X}_{t}, t\right)$, and one uses these predictions to sample from the approximate reverse Gaussian.

## Discussion

Diffusion models present a compelling alternative to VAEs and GANs for high-fidelity generation, particularly for large-scale image and audio data. In contrast to the singlestep generation of GANs (where latent noise is transformed into a final image in one forward pass), diffusion models gradually refine pure noise into structured data through a learned denoising sequence. Although this multi-step sampling can be slower, the gradual nature often leads to stable training dynamics and high-quality samples. Moreover, SongErmon [209] and subsequent works show that diffusion and score-based approaches can be unified through a differential equation perspective, with many interesting recent advances about the theoretical foundations of these models. Empirically, modern diffusion models have achieved state-of-the-art results on various generation tasks.

### 10.4 Decoder transformer models

### 10.4.1 Introduction and motivation

Decoder transformers extend the transformer framework (introduced in Section 8.5) to the task of auto-regressive generation. In contrast to an encoder-only transformer (as in Section 8.5), which processes an entire input sequence to extract a meaningful representation (recall from Section 8.5.3 that we captured this within the CLS token which is used for downstream modeling), decoder-only architectures focus on predicting each subsequent element of an output sequence given the elements generated so far. This makes them naturally suited to generative modeling, particularly of text, but also of other sequential modalities. Well-known examples of decoder-based transformer models include GPT, see Radford et al. [180] and Brown et al. [32], BART, see Lewis et al. [135], and T5 (in its decoder-only mode), see Raffel et al. [181].

### 10.4.2 Architecture overview

A decoder transformer follows a structure similar to a standard transformer but is specialized for sequence generation. Let

$$
X_{1: T}=\left(X_{1}, X_{2}, \ldots, X_{T}\right)
$$

denote a sequence of tokens (e.g., words, subwords, or characters). The model defines the joint distribution over all tokens via the factorization

$$
p_{\vartheta}\left(X_{1: T}\right)=\prod_{t=1}^{T} p_{\vartheta}\left(X_{t} \mid X_{1: t-1}\right)
$$

## Page 204
At each time step $t$, the decoder uses self-attention over the previously generated tokens $X_{1: t-1}$, together with positional embeddings, to form a representation from which to predict the next $X_{t}$. Notably, a causal mask is applied in the self-attention mechanism to ensure the model can only attend to past tokens, preserving the auto-regressive property and preventing future leakage; this is not the case in classical transformers as discussed in Section 8.5, because the queries and keys can freely interact in the attention mechanism (8.24).

Importantly, and in contrast to the encoding transformers presented earlier, the positional embeddings in decoding transformers are not usually learned, but are a static (previsible) function; we refer to Vaswani et al. [228] for the original approach using trigonometric functions of the position of each token and to Su et al. [211] for the highly successful rotary position embedding (ROPE) approach, which has been widely adopted by modern large language models.

# 10.4.3 Self-attention with causal masking 

Recall from (8.24) that the scaled dot-product attention mechanism computes, for a query $Q$, key $K$, and corresponding values $V$, the attention head

$$
H=\operatorname{softmax}\left(\frac{Q K^{\top}}{\sqrt{q}}\right) V
$$

where $q$ denotes the (embedding) dimension of the query $\boldsymbol{q}_{u}$, the key $\boldsymbol{k}_{u}$ and usually the value vectors $\boldsymbol{v}_{u}, 1 \leq u \leq t-1$, i.e., we have $Q, K, V \in \mathbb{R}^{(t-1) \times q}$, see (8.24).

In a decoder block, to preserve time-causality, each token's query vector $\boldsymbol{q}_{u}$ is restricted to only attend to keys from the previous positions, $\left(\boldsymbol{k}_{s}\right)_{s=1}^{u}$. This is implemented via a causal mask in the softmax step, setting the attention scores to zero whenever the key position exceeds the query position. More precisely, this is done by setting $\boldsymbol{q}_{u}^{\top} \boldsymbol{k}_{s}$ to $-\infty$ for $s>u$. Formally, for each token index $u$ and each position $s$, we set the mask

$$
\operatorname{mask}_{s, u}= \begin{cases}0, & \text { if } s \leq u \\ -\infty, & \text { if } s>u\end{cases}
$$

where the mask is applied in an additive manner to $\boldsymbol{q}_{u}^{\top} \boldsymbol{k}_{s}$. This results in an attention score 0 , whenever $s>u$, see (8.25). This implies that the model can only "see" previously generated tokens, enabling true auto-regressive generation and time-causality. Stacking multiple layers of masked self-attention and feed-forward transformations yields the typical decoder transformer.

## Page 205
# Analogy for causal masking in self-attention 

Causal masking in decoder transformers can be understood through the lens of an actuarial reserving exercise, where only past information is available for predicting future development. In a claims development triangle, we observe

$$
\left(\begin{array}{cccc}
C_{1,1} & C_{1,2} & \cdots & C_{1, n} \\
C_{2,1} & C_{2,2} & \cdots & ? \\
\vdots & \vdots & \ddots & \vdots \\
C_{n, 1} & ? & \cdots & ?
\end{array}\right)
$$

where the first index is the accident year and the second is the development year. When projecting future claims ( $C_{i, j}$, where $i+j>n+1$, i.e., beyond the current calendar year), we restrict ourselves to using only observed claims-entries in the upper-left triangle. This is directly analogous to causal masking, where for predicting token $X_{t}$, the model can only attend to previous tokens $X_{1: t-1}$.
Formally, in self-attention with causal masking, we use (10.3) to ensure that attention scores for future positions become invisible after the softmax application, preventing information leakage from tokens not yet generated - just as actuaries cannot use future claims development factors that have not occurred yet.
The sequential nature of both processes emphasizes the auto-regressive property: each new prediction builds upon previous predictions, compounding both capabilities and potential errors. Just as errors in early development factors propagate through the entire claims triangle, errors in early token predictions can influence all subsequent generations in a decoder transformer model.

### 10.4.4 Softmax outputs and probability calibration

At the final step of a decoder transformer layer, the hidden representation is typically projected onto the vocabulary space $\mathcal{W}$, yielding another set of so-called logits for each token, $\{\operatorname{logits}(w)\}_{w \in \mathcal{W}}$, and applying the softmax function gives the categorical distribution

$$
p_{\vartheta}\left(X_{t}=w \mid X_{1: t-1}\right)=\frac{\exp (\operatorname{logits}(w) / T)}{\sum_{u \in \mathcal{W}} \exp (\operatorname{logits}(u) / T)}
$$

where $T$ is often referred to as the temperature (see the next paragraph). In this way, the model's outputs define an implicit probability distribution over all possible next tokens. Therefore, conceptually, decoder-only transformers align with the implicit probability distribution approach discussed above: the next token is fully parameterized by the model, conditioned solely on the past. In practice, this allows for straightforward sampling token by token - and yields a model that scales gracefully as the dataset grows.
Importantly we must also note that large neural models are frequently miscalibrated, meaning their predicted probabilities may not align well with true outcome frequencies, see Guo et al. [89], in other words, the balance property of Section 4.1.2 is frequently not fulfilled with decoder transformers. Consequently, temperature scaling is commonly used to adjust the sharpness of the distribution: increasing $T>1$ flattens the distribution to reflect higher uncertainty, whereas decreasing $T<1$ sharpens the distribution to

## Page 206
make more confident predictions. Such post-hoc calibration not only affects sampling diversity when generating text (by controlling how quickly the distribution's mass is concentrated), but also helps ensure that probability estimates from the softmax layer align more faithfully with actual uncertainties.

# 10.4.5 Training and inference 

Training (teacher forcing). Decoder transformers are typically trained via teacher forcing, wherein the ground-truth token $X_{t}$ at time step $t$ is predicted from all preceding tokens $X_{1: t-1}$. Unlike standard machine learning loss functions that treat each sample independently, teacher forcing uses the ground-truth token $X_{t}$ at each time step to condition the prediction of the next token, thereby capturing the sequential dependencies inherent in language data. Moreover, this training scheme results in a very efficient use of sequence data. However, while this approach accelerates training by providing a clear context, it may introduce exposure bias during inference when the model must rely on its own generated tokens; for more discussion of this and a solution we refer to Bengio et al. [19]. Specifically, we minimize a negative log-likelihood objective:

$$
\ell(\vartheta)=-\frac{1}{T} \sum_{t=1}^{T} \log p_{\vartheta}\left(X_{t} \mid X_{1: t-1}\right)
$$

over a dataset of sequences. By training in this manner, the model learns to predict the next token based on the prior context. Although this training task of the next token prediction appears to be simple, nonetheless, it is sufficient for decoder transformer models to learn highly useful representations that can be adapted for various NLP tasks.

Inference (auto-regressive generation). Once trained, decoding proceeds token-by-token. We begin with a first token $X_{1}$, compute $p_{\vartheta}\left(X_{2} \mid X_{1}\right)$, sample or select the most probable token, append it to the partial sequence, and continue until we reach a predefined end-of-sequence token or a desired length. This iterative procedure naturally yields samples that reflect the learned distribution over sequences. Later, we will mention some more advanced sampling schemes.

Applications and variants. Decoder transformer models have been successfully deployed in a wide range of generative tasks, including:

- Language modeling and text generation: GPT models, see Radford et al. [180] and Brown et al. [32], achieve state-of-the-art results on various NLP benchmarks, generating coherent text and facilitating tasks such as summarization, translation, and open-domain dialogue.
- Conditional text generation: Using additional conditioning signals (e.g., prompts, context paragraphs), decoder transformers can produce targeted text in specific domains. BART of Lewis et al. [135] and T5 of Raffel et al. [181] exemplify encoderdecoder or decoder-focused architectures that excel at summarization, questionanswering, and more.

## Page 207
- Code generation: Extensions of the decoder transformer architecture have also found success in generating programming code, assisting software development workflows.

Ongoing research explores scaling up decoder transformers to billions (and even trillions) of parameters, yielding large language models capable of zero-shot or few-shot learning, robust transfer, and coherent long-range generation. Although computationally expensive, these models adapt to diverse downstream tasks with minimal additional training.

# 10.5 Conclusion on generative models 

Generative modeling now represents a cornerstone of modern machine learning, enabling us to capture intricate distributions over high-dimensional data and opening avenues for rich, creative applications. We have surveyed a variety of deep generative modeling approaches - from latent factor methods such as VAEs, GANs and diffusion models to implicit techniques such as auto-regressive decoder transformers. Each framework brings distinct strengths: VAEs offer tractable likelihood-based training and interpretable latent spaces, GANs facilitate visually compelling sample generation through adversarial training, and diffusion models provide stable multi-step data refinement. Meanwhile, auto-regressive transformers address sequential dependencies in language and beyond, forming the basis of cutting-edge large-scale language models. We summarize the discussion to this point in Table 10.1.
Despite these differences, the unifying goal is to learn $p_{\vartheta}\left(X_{1: T}\right)$ in a way that captures the underlying structure of the data, allowing us to sample, infer probabilities, or encode latent representations. Remarkably, the simple idea of modeling the distribution of observed data has led to new modeling capabilities which are ground-breaking for tasks such as image synthesis, text generation, uncertainty quantification, and other areas critical to science, finance, and technology. As model scale continues to grow, and as new training paradigms emerge (e.g., incorporating human feedback or advanced prompt engineering), generative models will likely expand their role even further.
The generative modeling approaches we have explored thus far - VAEs, GANs, diffusion models, and auto-regressive transformers - each represent important milestones in our ability to learn and sample from complex distributions. Yet, it is the decoder-based transformer architecture, specifically when scaled to massive parameters and trained on diverse textual corpora, that has yielded perhaps the most remarkable breakthrough in recent AI tools: the emergence of Large Language Models (LLMs).
LLMs can be viewed as the natural evolution of auto-regressive generative modeling, where the scaling of data, parameters, and computation, as well as the application of many new and novel techniques, has led to qualitatively different capabilities from previous types of generative models. Unlike specialized generative models designed for narrow domains (e.g., image generation with GANs or diffusion models), LLMs demonstrate a surprising degree of generality - they can generate not only coherent text across domains but also exhibit capabilities in reasoning, planning, and task adaptation that were not explicitly engineered.

## Page 208
Table 10.1: Comparison of key generative modeling approaches

| Model | Core principle | Strengths | Limitations | Typical applications |
| :--: | :--: | :--: | :--: | :--: |
| VAEs | Learn latent representations via variational inference | - Explicit probabilistic formulation <br> - Stable training dynamics <br> - Interpretable latent space | - Often yields blurry samples <br> - Limited sample diversity <br> - Complex reconstructionregularization balance | - Dimensionality reduction <br> - Anomaly detection <br> - Data augmentation |
| GANs | Adversarial training between generator and discriminator | - High-fidelity samples <br> - Sharp, realistic outputs <br> - Excels in visual domains | - Training instability <br> - Mode collapse <br> - No explicit density estimation | - Image synthesis <br> - Style transfer <br> - Data augmentation |
| Diffusion models | Gradual denoising process, reversing forward diffusion | - State-of-the-art quality <br> - Stable training <br> - Flexible conditioning | - Slow sequential sampling <br> - <br> Computationally intensive <br> - Complex implementation | - Image generation <br> - Audio synthesis <br> - 3D content creation |
| Auto- <br> regressive transformers | Factorize joint distribution into conditional predictions | - Scales to massive datasets <br> - Captures long dependencies <br> - Ideal for sequential data | - Exposure bias <br> - Limited context window <br> - Sequential generation | - Text generation <br> - Code synthesis <br> - Language modeling |

## Page 209
The connection between traditional generative models and LLMs is not merely architectural. The fundamental principles we have discussed, which are learning probability distributions, leveraging self-attention mechanisms, and employing auto-regressive factorization, remain at the core of LLM design. However, at the extreme scales of modern LLMs (with billions or trillions of parameters), these principles yield models that transcend simple next-token prediction to capture deeper patterns of language, knowledge, and problem-solving.
In the following sections, we will explore how LLMs have extended the generative paradigm from simple distribution learning to complex systems capable of contextual understanding, few-shot learning, and even rudimentary reasoning. This trajectory from specialized generative models to increasingly general AI systems reflects both the power of scale and the richness of the frameworks we have developed to this point for modeling complex distributions.

# 10.6 Large language models 

LLMs are perhaps the crowning achievement of the field of deep generative modeling to date, having shown dramatic success on a variety of machine learning tasks, capturing both public attention and massive capital investments. In this section, we will narrow our focus specifically to LLMs, which are massive pre-trained decoder-based transformers that have recently dominated the landscape of NLP and multimodal tasks. Building on the foundational ideas introduced in this chapter, we will examine how LLMs leverage in-context learning, alignment techniques, and prompt-based interfaces to deliver astonishing generative performance for real-world applications. We will then cover emerging topics like reasoning models and discuss methods for working with LLMs in a safe manner. It is important to emphasize to readers that, firstly, many of these areas are still emerging and are sometimes highly heuristic, and, secondly, due to the financial importance of LLMs, most research is now no longer published, so we need to rely on less formal sources to explain some of the concepts.

### 10.6.1 From auto-regressive transformers to LLMs

The conceptual roots of LLMs stem from the auto-regressive decoder transformer architectures that we have discussed in Section 10.4. As discussed there, an auto-regressive model, in essence, factorizes the probability of a token sequence $X_{1: T}=\left(X_{1}, \ldots, X_{T}\right)$ as

$$
p_{\vartheta}\left(X_{1: T}\right)=\prod_{t=1}^{T} p_{\vartheta}\left(X_{t} \mid X_{1: t-1}\right)
$$

By combining this factorization with the self-attention mechanism of transformers, Vaswani et al. [228], each token's prediction can condition on the entire preceding context in a computationally efficient manner. The resulting architecture naturally lends itself to large-scale training, which, in turn, uncovers extensive patterns in language data.
Early work on transformers, Brown et al. [32] and Kaplan et al. [113], revealed scaling laws indicating that larger models (in terms of parameters) trained on correspondingly larger datasets achieve systematically lower training and validation losses. This discovery

## Page 210
motivated the construction of models with billions (and later trillions) of parameters, coining the term Large Language Models (LLMs). As model capacity increases, LLMs often display emergent capabilities not present in smaller counterparts, such as better zero-shot generalization and few-shot in-context learning (described below).
Alongside model scaling, researchers recognized the importance of diverse, high-quality training corpora. Auto-regressive transformers trained on multi-domain data (web text, scientific articles, code, etc.) acquire flexible linguistic competence that can be harnessed for many downstream tasks, simply by changing the prompt or performing minimal finetuning. The development of the principles which underly modern LLMs can be traced through the advances contained in the Generative Pretrained Transformer (GPT) series of papers.

GPT-1. The first GPT, Radford et al. [180], demonstrated that a unidirectional (decoder) transformer trained on large unsupervised corpora could achieve strong performance on downstream tasks with minimal fine-tuning. This pretrain-then-finetune paradigm became a blueprint for subsequent GPT-style models.

GPT-2. Scaling up both model size (up to 1.5B parameters) and data quantity revealed that bigger models not only improved perplexity (in simple terms, the loss of the model) but could also generate impressively coherent texts, Radford et al. [181]. GPT-2 sparked discussions about responsible model release due to concerns over disinformation and misuse, thus, highlighting ethical and security considerations.

GPT-3 and in-context learning. GPT-3, Brown et al. [32], introduced a much larger model (up to 175B parameters) and ushered in the era of in-context learning. Surprisingly, GPT-3 could perform new tasks simply by reading a handful of examples within the prompt - few-shot prompting - without any gradient updates to model parameters. This phenomenon occurs because of the model's internal representation of language: it implicitly "learns" from the in-prompt examples and generalizes these patterns to predict the next tokens. This emergent capability defied earlier assumptions that explicit fine-tuning was always necessary.

GPT-3.5, GPT-4, and further refinements. Subsequent iterations like GPT-3.5 and GPT-4 refined the architecture, improved instruction-following, and integrated alignment techniques (see the discussion on RLHF in Section 10.6.4). These models further demonstrated emergent competencies in reasoning, math problem-solving, and creative writing, driven by the combination of massive parameter counts, diverse training data, and sophisticated alignment protocols.

A growing body of work attempts to explain how LLMs implement in-context learning from a theoretical standpoint:

- Meta-learning perspective: LLMs may store "internal optimizers" or representations that mirror gradient-based learning, thus, enabling them to adapt swiftly to new tasks within the forward pass alone; see Kirsch et al. [121].

## Page 211
- Implicit Bayesian inference: Some interpret in-context learning as performing approximate Bayesian updates over prompts, where examples shape the posterior distribution over the next-token predictions; see Xie et al. [245].
- Emergent structures: Empirical analyses suggest that deeper, wider transformers spontaneously encode schema-like knowledge, capturing linguistic phenomena (syntax, semantics) and domain rules (logic, mathematics); see our discussion on mechanistic interpretability later in Section 10.6.10.

While no single unifying theory fully accounts for in-context learning, these angles underscore its complexity and partially illuminate the remarkable "learning without parameter updates" phenomenon.

# Summary and outlook 

The journey from auto-regressive transformers to modern LLMs reflects a combination of:

- Model scaling in parameter count and data size.
- Emergent phenomena, such as in-context learning and few-shot prompting.
- Alignment methods, including human feedback and chain-of-thought prompting.

These elements, taken together, have propelled LLMs forward, creating significant capabilities in language understanding and generation. Research continues to expand context windows, refine architectural insights, and develop more robust theoretical frameworks. Given the significant achievements of LLMs, their theoretical underpinnings and practical implications will likely remain a central focus in research in generative modeling.

From a research perspective, a significant practical constraint of auto-regressive transformers is the context window, typically limited by computational considerations (e.g., a few thousand tokens). Research on extending this context to tens or hundreds of thousands of tokens (via efficient attention mechanisms or hierarchical memory) is ongoing; see Beltagy et al. [17] and Chowdhery et al. [43]. These longer context windows allow LLMs to handle extensive documents, multi-step narratives, or long code bases, further extending their utility.

## Page 212
# In-context learning: a credibility analogy without parameter updates 

Analogy overview. In-context learning enables large language models (LLMs) to adapt to new tasks simply by seeing examples in the prompt, without modifying their underlying weights. This mechanism has a meaningful parallel in credibility theory, where an actuary working in specialist lines of business refines a broad "base rate" with policyholder-specific information - again, without rebuilding the entire rating model.

1. Base rate model. An insurer's rate manual provides a baseline premium derived from population-level statistics. This is akin to the LLM's pretrained parameters, which capture general linguistic or domain knowledge.
2. Individual risk experience. When pricing a single policy, the insurer reviews the insured's personal claims history to tailor the final premium. In a LLM, analogous "in-context examples" in the prompt illustrate task-specific patterns for the immediate query.
3. Credibility-weighted output. Classical Bühlmann credibility [34] can be summarized as

$$
\text { Premium }=\omega \times(\text { Individual Experience })+(1-\omega) \times(\text { Class Rate })
$$

where omega $\in[0,1]$ is a credibility factor that determines how much to rely on individual risk data versus the global model.

- No retraining: The underlying rating tables remain intact, reflecting prior knowledge.
- Context-sensitive adjustment: The final estimate updates automatically based on recent experience.

Link to in-context learning. Similarly, a LLM conditions its output on both the query $Q$ and provided examples $\left(E_{1}, E_{2}, \ldots, E_{n}\right)$ :

$$
p\left(y \mid Q, E_{1}, \ldots, E_{n}\right)
$$

This process can be viewed as an implicit "credibility weighting" (or Bayes' update) for the new prompt examples - just as an actuary balances a policy's past claims with broader class results.

No parameter updates required. In both cases, the global model (the insurer's rating manual or the LLM's pretrained weights) remains unchanged. New, contextspecific outputs are produced without the computational overhead of a full retraining process or the risk of forgetting established knowledge.

## Page 213
# 10.6.2 Foundation models and pretraining 

Modern LLMs typically emerge from large-scale foundation models, see Bommasani et al. [24], which are neural networks (often transformers) trained on massive corpora encompassing various domains and modalities. These foundation models are learned via self-supervised or unsupervised objectives, such as masked language modeling or, more often, next-token prediction. The goal is to capture rich statistical patterns over text, enabling the model to generalize across tasks with limited or no additional fine-tuning. A typical pretraining process involves:

- Large-scale data: Billions of tokens from diverse sources, including web pages, books, and domain-specific datasets.
- Transformers at scale: Decoder architectures, see Section 10.4, or encoder-decoder transformers, often with billions of parameters, trained on large compute clusters.
- Unsupervised objectives: Masked language modeling (e.g., BERT-style) or autoregressive next-token prediction (e.g., GPT-style).

This pretraining yields a foundation that can be adapted to a variety of downstream tasks, simply by adjusting prompts or performing light fine-tuning.

### 10.6.3 Use cases of large language models

The proliferation of LLMs has yielded significant impact across diverse sectors:

- Customer support and chatbots: Companies employ LLM-driven assistants for query handling, knowledge base lookups, and interactive customer service.
- Content generation: Automated writing, summarization, and content ideation workflows leverage the generative capacity of LLMs.
- Coding assistance: Tools like GitHub Copilot, based on transformer architectures, suggest code completions, refactorings, and bug fixes.
- Scientific and legal research: LLMs facilitate initial drafts for technical documents, case analyses, or literature reviews, speeding up research processes.

While LLMs show promising capabilities, caution must be exercised regarding hallucinations, biases, and misinterpretations. Techniques like RLHF, see Section 10.6.4, and carefully designed prompts, see Section 10.6.6, can mitigate these issues to some extent.

### 10.6.4 Fine-tuning with reinforcement learning from human feedback

Although pretrained LLMs demonstrate impressive linguistic capabilities, they can generate outputs that are misleading, biased, or misaligned with human preferences. Reinforcement learning from human feedback (RLHF) aims to address this by incorporating human judgements into the fine-tuning process, see Christiano et al. [44] and Ouyang et al. $[172]$.

## Page 214
An RHLF procedure might be applied as follows:
(1) Initial supervised fine-tuning: Start from the pretrained model and fine-tune it on labeled examples to adapt it toward desired behaviors (e.g., polite conversation).
(2) Reward model (RM) training: Collect human preference data (e.g., given two model outputs, which is more helpful or correct?) and train a reward model to predict these preference scores.
(3) Reinforcement learning-based optimization: Using the reward model as a proxy for human preferences, update the LLM weights via reinforcement learning (e.g., proximal policy optimization, see Section 11.9.2, below). The model is thus guided to produce outputs favorably judged by humans.

RLHF has been instrumental in aligning LLMs' outputs with more human-like values, improving their helpfulness and reducing harmful or factually incorrect content.

## Page 215
# RLHF analogy: actuarial preferences for smoothness and monotonicity 

In RLHF, a LLM is adjusted to align with human preferences as judged by a reward model. One can draw a parallel with how actuaries incorporate business or regulatory shape constraints - e.g. requiring that premium rates be smooth in age or monotonically increasing in coverage - without redesigning the entire rating structure.

1. Initial model setup. When pricing using GLMs, actuaries will often begin with a baseline set of relativities, just as LLMs begin with pretrained weights. These starting points embed broad empirical domain knowledge.
2. Defining the "preference" or constraint. While RLHF uses human annotations to build a reward model that scores outputs, actuaries may impose formal constraints such as:

- Smoothness: Ensuring rates underlying premiums do not change abruptly between adjacent age bands.
- Monotonicity: For example, requiring that premium rates increase with coverage amounts or risk classifications.

This functions analogously to a "preference function" specifying which model behaviors are desired or penalized.
3. Credibility-like balancing act. Actuaries incorporate these shape constraints without discarding prior data or ignoring established rates; rather, they might credibility-weight the new constraints with the existing model (for example, by balancing penalties with an empirical loss function, such as a deviance loss). In RLHF terms, the constraints act as a reward/penalty that the model must learn to satisfy, while a KL divergence (or similar) prevents overly large deviations from the baseline model.
4. Controlled model updates. Just as the RLHF step fine-tunes a LLM to better match human preferences (while preserving core language skills), the actuarial process iteratively refines rates to respect shape constraints. The baseline structure stays in place - ensuring model continuity - while incremental updates push the model toward smooth or monotonic relationships in the variables of interest.

Outcome. The result is a stable, constraint-aware model that remains consistent with previous assumptions, much like a LLM that remains coherent to its pretraining but is shaped by new feedback. By introducing shape constraints akin to RLHF's preference signals, actuaries achieve alignment with business rules, regulatory standards, and risk theory without requiring a full model rebuild.

### 10.6.5 Parameter-efficient fine-tuning

In the LLM workflows, full fine-tuning of all model parameters can be prohibitively expensive in terms of computation and memory, especially for models with tens or hundreds

## Page 216
of billions of parameters. Consequently, researchers have proposed parameter-efficient adaptation methods that offer strong performance with only a small fraction of parameters being updated or introduced.

# Overview of fine-tuning methods 

Adapters [104]. Insert lightweight adapter layers within or between the existing transformer layers. During fine-tuning, only these adapter parameters are updated, while the original model weights remain fixed. Adapters can be trained for each downstream task, enabling modular reusability.

Prefix tuning [136]. Prepends a small set of learnable "prefix" tokens to each attention block. The main LLM parameters are frozen, and only the prefix embeddings are optimized to steer model behavior.

Low-rank adaptation (LoRA) [105]. Instead of storing full dense weight updates, LoRA factors the update matrix into low-rank components. During forward/backward passes, these low-rank matrices are injected into attention or FNN layers. This greatly reduces the memory overhead needed to adapt the model.

## Practical considerations

- Substantial memory savings: By freezing most layers, these approaches reduce GPU/TPU memory usage and speed up training iterations.
- Modularity: Adapters and prefix modules can be swapped in or out for different tasks, making it easier to maintain multiple domain-specific fine-tunings.
- Performance-trade-offs: While often competitive with full fine-tuning, performance might slightly lag if the downstream domain deviates significantly from the pretraining distribution.

Overall, parameter-efficient methods have become a standard practice for adapting large decoder transformers (e.g., GPT-3.5, Llama) to specialized tasks without incurring the enormous cost of training all parameters end to end.

### 10.6.6 Prompting

Prompting has emerged as a powerful way to harness decoding auto-regressive transformer models. In essence, prompting leverages the fact that a LLM generates tokens conditionally on previously observed (or generated) tokens. By carefully selecting an initial sequence of tokens (the prompt), users can steer the model to perform specific tasks or produce more detailed and context-aligned outputs. This framework of "prompt-and-generate" has dramatically extended the applicability of LLMs to tasks including question answering, summarization, and domain-specific reasoning; see Brown et al. [32]. Although we are going to attempt to provide a mathematical description here, it is important to note that prompting can be very heuristic in practice and that many ideas in prompting LLMs have been discovered in a totally empirical manner.

## Page 217
# Mathematical basis of prompting 

Let $X_{1: T}=\left(X_{1}, X_{2}, \ldots, X_{T}\right)$ denote a (partially) observed sequence of tokens, which we can split into a prompt portion

$$
\boldsymbol{p}=X_{1: k}=\left(X_{1}, \ldots, X_{k}\right)
$$

and a continuation portion

$$
\boldsymbol{c}=X_{k+1: T}=\left(X_{k+1}, \ldots, X_{T}\right)
$$

for some $1<k<T$. A LLM defines the probability distribution

$$
p_{\vartheta}\left(X_{1: T}\right)=\prod_{t=1}^{T} p_{\vartheta}\left(X_{t} \mid x_{1: t-1}\right)
$$

In the prompting paradigm, we treat $\boldsymbol{p}$ as given and seek for $t>k$

$$
p_{\vartheta}(\boldsymbol{c} \mid \boldsymbol{p})=\prod_{t=k+1}^{T} p_{\vartheta}\left(X_{t} \mid X_{1: k}, X_{k+1}, \ldots, X_{t-1}\right)
$$

Thus, the prompt $\boldsymbol{p}$ is a partial sequence or context that conditions the generation of the continuation $\boldsymbol{c}$. By altering the structure, style, or content of the prompt, we can influence the model's output distribution without modifying any model parameters! Of course, we need a very large model to be able to produce these highly conditional distributions over outputs, but with the large foundation models we have been discussing, the required conditions are in place for this to be successful.

## Prompting in practice

Instruction-based and zero/few-shot prompting. One strategy is to provide an instruction prompt describing the desired task (e.g., "Translate the following sentence to French:"). The model then generates a sequence that completes the task. In few-shot prompting, one appends one or more input-output examples (mini "demonstrations") to guide the model's behavior:

$$
\underbrace{\text { Example 1: [Input] } \rightarrow \text { [Output] }}_{\text {demonstration }} \quad \ldots \underbrace{\text { Example n: [Input] } \rightarrow \text { [Output] }}_{\text {demonstration }} \underbrace{\text { New Input:}}_{\text {query }}
$$

This sequence forms the prompt $\boldsymbol{p}$. The model then predicts the continuation $\boldsymbol{c}$, expected to mirror the pattern shown by the demonstrations.

Task-oriented prompts. Prompts can also be task-specific, containing relevant domain context (e.g., table schemas for SQL queries, or examples of correct predictions for classification tasks). Crucially, the model remains in its pretrained state - no additional fine-tuning is performed.
During evaluation, we compare the predicted continuation against ground truth references if available, or assess the model's response quality via metrics such as BLEU (for translation) or more qualitative judgements; see also the section on LLM as a judge below in Section 10.6.8 and a quantitative approach for assessing LLM outputs in Section 10.6.9.

## Page 218
# Chain-of-thought prompting 

A notable advancement in prompting is chain-of-thought prompting, see Wei et al. [234], where the prompt is carefully engineered to induce the model to explain or reason through intermediate steps before producing a final answer. Rather than prompting the model for a single final solution, we include a sequence of reasoning tokens - similar to showing one's "work" in a math problem. For instance:

## - Prompt:

"Q: If a car travels at $60 \mathrm{~km} / \mathrm{h}$ for 2 hours, how far does it go? Let's break it down step by step."

- Chain-of-thought (model's intermediate reasoning):
"We know speed $=$ distance / time. If speed is $60 \mathrm{~km} / \mathrm{h}$ and time is 2 hours, distance $=60 \cdot 2=120 \mathrm{~km}$."
- Final answer:
" 120 km ."

By exposing intermediate steps, chain-of-thought prompts often elicit more accurate and interpretable responses from the model, especially for multi-step reasoning tasks. This technique has been shown to improve performance on mathematical reasoning, logical deduction, and other complex question-answering domains.
Moreover, this approach underlies the next generation of LLMs, which are called reasoning models, see Section 10.6.7 below.

## Recent research on prompting

Prompting has become a rapidly expanding research area with efforts focusing on:

- Prompt engineering: Systematic methods for designing prompts, including prompt tuning and auto-prompting, where prompts (or prompt tokens) are learned or searched automatically rather than hand-crafted. A very nice approach and software package for this is DSPy, see Khattab et al. [117]; remarkably, optimal prompts can greatly increase the accuracy of LLM on certain tasks!
- Interpretability and reliability: Investigating how prompts can reveal model reasoning, help identify hallucinations, or mitigate undesired behaviors. Chain-of-thought prompting is one approach that aims to surface model reasoning steps.
- Large-scale benchmarks: Evaluations on broad sets of tasks (e.g., MMLU, BigBench) to measure how well prompting generalizes without further training.

Importantly, prompting interacts strongly with model size: large-scale LLMs often exhibit emergent few-shot and reasoning capabilities that smaller models lack. As a result, prompting-based methods have become the de facto approach for eliciting complex behaviors from LLMs with minimal overhead.

## Page 219
# 10.6.7 Building and refining reasoning models for LLMs 

Very recent advances in LLMs extend these models not only to perform generative modeling of text, but exploit the structure of decoder transformers to mimic the reasoning process that a person might follow when solving a highly complex problem. Among these models, the O1 and O3 series of models from OpenAI and the recent DeepSeek R1 model [48] have created a significant amount of interest publicly and within the machine learning community. In this section, we follow very closely the key ideas presented in a recent blog post by Raschka [182], who provides an excellent overview of methods and strategies for enhancing LLMs with reasoning capabilities. Unfortunately, not all of the research underlying reasoning models is in the public domain, so some "detective" work needs to be done to understand what methodologies have been applied to create these models. The main exception to this is the DeepSeek paper [48].

## Overview and motivation

Reasoning-centric LLMs are specialized models designed to handle complex, multi-step tasks - such as challenging math problems, puzzles, or coding scenarios - by explicitly incorporating intermediate thought processes into their responses. Although many standard LLMs can solve simple factual queries (e.g., "What is the capital of France?"), reasoning models aim to excel at questions like "A train travels at 60 mph for 3 hours; how far does it go?", where multiple steps (e.g., relating speed, time, and distance) are required. While existing large models are already somewhat capable in this domain, specialized reasoning models often include an intermediate chain-of-thought, enabling them to systematically break down and solve intricate problems. Whereas chain-of-thought of thought prompting was covered in Section 10.6.6, the main idea here is not to induce reasoning into LLMs through prompts, but rather to use reinforcement learning or other approaches to encourage LLMs automatically to produce intermediate chain-of-thought outputs.
Reasoning models are particularly useful for tasks requiring elaborate, multi-step logic or complex structure (e.g., advanced mathematics, riddles, or step-by-step code generation). In contrast, simpler tasks - like summarization, translation, or basic knowledge-based question answering - can often be performed by standard decoder transformer LLMs without additional "reasoning" overhead. Indeed, using a specialized reasoning model for every request can be inefficient and may introduce unnecessary verbosity or cost. The choice of model should therefore be guided by the complexity of the query at hand. An illustrative example of reasoning-focused LLM development is provided by the project DeepSeek R1 [48], which modifies the usual LLM training approach as follows:

- DeepSeek-R1-Zero: A base pre-trained model (DeepSeek-V3) is further trained with pure reinforcement learning (RL) on tasks requiring multi-step solutions. Surprisingly, the model spontaneously begins to produce chain-of-thought-like responses, showcasing that reasoning can emerge purely from reinforcement learning under the right reward design.
- DeepSeek-R1: Next, this "cold-start", the reinforcement learning model is refined using a combination of supervised fine-tuning (SFT) and reinforcement learning,

## Page 220
akin to RLHF approaches. Additional data is collected from the model itself, enabling multi-stage improvement (SFT $\rightarrow \mathrm{RL} \rightarrow$ more SFT $\rightarrow$ more RL). This yields a more robust reasoning LLM.

- DeepSeek-R1-Distill: Finally, the project employs a distillation-based approach to transfer reasoning capabilities into smaller models (e.g., Llama 8B or Qwen 30B). Though these distilled models do not match the full power of DeepSeek-R1, they exhibit surprisingly strong reasoning for their size.

This pipeline highlights a broader theme: many state-of-the-art reasoning LLMs rely on a combination of reinforcement learning, supervised instruction tuning (especially with chain-of-thought data), and occasional distillation to smaller architectures.

# Four main approaches to reasoning LLMs 

Four general strategies for building or improving reasoning models have emerged:
(1) Inference-time scaling. Inference-time scaling involves no additional training but expends more computational resources or tokens at inference to achieve better outputs. Examples include:

- Chain-of-thought (CoT) prompting: Encouraging step-by-step generation simply by appending instructions like "Think step by step." This can lead to more complete intermediate solutions for complex problems.
- Beam search, voting, or search-based methods: Generating multiple candidate solutions and then selecting the best via majority voting or a learned "judge." These methods often improve accuracy on difficult queries.

While effective, inference-time scaling can be costly if used indiscriminately.
(2) Pure Reinforcement Learning. DeepSeek-R1-Zero is a prime example of pure reinforcement learning producing emergent reasoning behavior. In that setup, the base model is optimized via accuracy and format rewards, with no intermediate supervised fine-tuning. The former reinforcement learning reward is used when the generated outputs can be verified empirically, for example, by testing code examples produced by the LLM by running these and assessing the outputs against known answers. The latter reward is derived using a LLM as a judge to ensure that the reasoning tokens are correctly formatted. Despite the lack of explicit chain-of-thought demonstrations, the model gradually learns to present multi-step reasoning in its answers, suggesting that certain reward signals can implicitly nudge the model toward generating structured, step-by-step solutions.
(3) SFT + RL (typical RLHF). Most top-performing reasoning LLMs (e.g., final DeepSeek-R1 or rumored pipelines for the O1 and O3 models from OpenAI) blend supervised fine-tuning (SFT) with reinforcement learning (RL):

## Page 221
- SFT stage: Collect chain-of-thought or instruction data from either humans or the model itself ("cold-start" generation). Train the LLM to follow these instructions or produce step-by-step solutions.
- RL stage: Further refine the model with preference-based or rule-based rewards (e.g., verified answers, consistent format).
- Iterate: Additional SFT data can be created using the latest model checkpoint, forming a virtuous cycle of improvement.

This approach generally outperforms pure reinforcement learning, especially for largescale deployments, and is favored in contemporary reasoning LLM research.
(4) Pure SFT and distillation. Finally, distillation from a larger reasoning model can be an easier method to produce smaller reasoning LLMs:

- SFT data generation: A larger teacher model (e.g., DeepSeek-R1) generates highquality chain-of-thought or instruction examples.
- Distillation: A smaller student model is fine-tuned on this curated dataset. The student often inherits some reasoning abilities from the teacher, though, typically at lower performance ceilings.

Distillation can drastically reduce inference costs and hardware requirements, making advanced reasoning accessible to researchers without multi-million-dollar budgets.

# Practical considerations and low-budget extensions 

Advanced reasoning LLMs like DeepSeek-R1 or OpenAI's "O1" models demand substantial compute resources. However, projects like TinyZero [174] and Sky-T1 [168] show that interesting progress is possible on smaller scales. For instance:

- TinyZero (3B params) attempts a pure reinforcement learning approach analogous to DeepSeek-R1-Zero, revealing emergent self-verification steps even at a modest parameter count.
- Sky-T1 (32B params) employs a low-budget distillation or SFT strategy, reportedly achieving performance near certain proprietary models at a fraction of the cost.

Such efforts underline the practicality of targeted or lower-scale fine-tuning for specialized tasks and domain constraints.

### 10.6.8 LLMs as a judge and self-consistency mechanisms

Beyond generating text, LLMs can be employed in a referee or judge capacity, evaluating their own outputs or the outputs of other models; see Bai et al. [10]. In this paradigm, the LLM critiques and scores a response - often employing chain-of-thoughtlike reasoning internally - to indicate correctness, clarity, or other quality measures. Such "self-evaluation" or "self-consistency" strategies may reduce error rates and help identify potential reasoning flaws.

## Page 222
# Mathematical formulation of self-consistency 

Consider a query (or prompt) $Q$. A single LLM can generate multiple candidate responses

$$
\mathcal{R}=\left\{R_{1}, R_{2}, \ldots, R_{K}\right\}
$$

At generation time, we obtain each $R_{k}$, for $1 \leq k \leq K$, auto-regressively from the model's next-token distribution:

$$
p_{\vartheta}\left(R_{k} \mid Q\right)=\prod_{t=1}^{T_{k}} p_{\vartheta}\left(r_{k, t} \mid Q, r_{k, 1}, \ldots, r_{k, t-1}\right)
$$

where $r_{k, t}$ denotes the $t$-th token in candidate $R_{k}$, and $T_{k}$ is the length of that candidate. Next, the judge component (which may be the same LLM configured in "critique" mode, or a separate model) provides a quality score or utility $J_{\phi}\left(R_{k}, Q\right)$ for each candidate, $1 \leq k \leq K$, reflecting the likelihood of correctness, alignment, or other criteria; in this case $\phi$ represents the parameters of the judge LLM, which can be the same as the parameter set $\vartheta$ if the same LLM is being used as the one used for generation. A simple self-consistency mechanism then selects the final response $\hat{R}$ as

$$
\hat{R}=\underset{R \in \mathcal{R}}{\arg \max } J_{\phi}(R, Q)
$$

This max-sampling approach chooses the highest scoring solution.

## Practical implementation and research directions

In practice, a single LLM instance might be used to:

- Propose multiple candidate responses $\mathcal{R}$.
- Judge or rank these responses based on correctness or alignment criteria, effectively instantiating $R \in \mathcal{R} \mapsto J_{\phi}(R, Q)$.
- Select the best response (or revise weaker ones).

This dual role (generator + judge) has inspired research on iterated refinement, selfconsistency decoding, and constitutional AI, whereby models use rules or guidelines to critique their outputs. For instance, a chain-of-thought can be included in the judging mechanism to facilitate more nuanced evaluations, e.g., verifying steps in a math proof. By iterating this process - sampling multiple answers, critiquing them, and selecting or refining the best - it is often possible to reduce error rates and highlight reasoning flaws that might otherwise go unnoticed in a single pass. This constitutes a "self-consistency" or "self-evaluation" loop, potentially improving the reliability of LLM-generated content without additional external supervision.
Overall, using LLMs in a judge capacity exemplifies how generative models can be extended beyond pure text generation to include meta-level reasoning about their own outputs. Such techniques dovetail with alignment strategies (Section 10.6.4) and advanced prompting methodologies (Section 10.6.6), contributing to a growing toolbox for building and refining LLMs. In Section 10.6.7 we discussed similar ideas that now underlie state of the art LLMs.

## Page 223
# 10.6.9 Responsible use of large language models 

Here we provide an overview of how LLMs can be used responsibly, basing this section mainly on van der Merwe-Richman [224]. The main idea is to use LLMs to output not only text data, but also quantitative metrics, for example, a LLM can evaluate how well a candidates curriculum vitae matches a job specification and output a score between 0 and 10. Once a quantitative output is available, then the usual actuarial and statistical processes used for model validation can be applied.

## Overview and governance

Working with LLMs requires a well-defined governance framework to ensure ethical, transparent, and compliant usage; see van der Merwe-Richman [224]. Such a framework typically includes:

- Accountability and ethics: Establishing clear responsibility for model outcomes and aligning generated content with relevant industry regulations or guidelines.
- Monitoring and controls: Continuously reviewing data pipelines and model performance, including adherence to data-privacy standards and detection of drift in model outputs.
- Escalation processes: Providing clear pathways for human intervention (human-in-the-loop) when unusual or high-stakes scenarios arise.

These governance pillars lay the foundation for subsequent steps in model selection, performance evaluation, and long-term monitoring.

## Model selection and quantitative scoring

When using a LLM for a task, where relevant, actuaries and data scientists should strongly consider requiring the LLM to output a numerical score for its predictions. Let $X \in \mathcal{X}$ be an input (such as a set of claims documents), and let the LLM's decision function

$$
f: \mathcal{X} \rightarrow \mathbb{R}
$$

produce a numerical output $f(X)$. Interpreting $f(X)$ as a probability, confidence level, or rating on a defined scale, we might write

$$
f(X)=\mathbb{P}(\text { claim is fraudulent } \mid X) \quad \text { or } \quad f(X)=\text { rating } \in[0,10]
$$

By capturing the LLM's beliefs in a single numeric measure, quantitative validations become directly applicable:

- Statistical analysis of scores: Means, variances, hypothesis testing, and time-series control charts can reveal shifts or unusual patterns.
- Machine learning metrics: Standard metrics like strictly consistent loss functions, e.g., mean squared error, or Gini or F1-scores enable direct benchmarking across different prompts or data conditions.

## Page 224
Moreover, assigning a numerical score at each step helps mitigate hallucinations: once the model is required to quantify its certainty, stakeholders can explicitly detect outlier predictions (e.g., extremely high scores for dubious responses) and investigate them using structured review or escalation processes. Having a set of quantitative scores and analysis for several different LLMs can aid in the process of selecting the most relevant model for a task.

# Performance metrics 

Once the model produces numeric scores, a variety of performance measures become straightforward to implement:

- NLP/LLM metrics: Evaluate textual quality via ROUGE or BLEU, while examining numeric agreement with human-labeled data (e.g., classification accuracy).
- Alignment measures: Compare the LLM's proposed chain-of-thought and final numeric scores against expert judgements or known standards.
- Stability and Sensitivity: Assess the model's outputs across varying prompt wordings or reordered inputs, checking for robustness in both text and numerical predictions.


## Robustness, bias and interpretability

Robustness. Testing the model under adversarial prompts or demographic shifts ensures its numeric output remains stable. For instance, if $f(X)$ changes dramatically under minor prompt modifications, further prompt engineering or data augmentation may be warranted.

Bias and fairness. Let

$$
G \in\left\{g_{1}, g_{2}, \ldots\right\}
$$

represent demographic group membership, and

$$
Y \in\{\text { True, False }\}
$$

be the label of interest. The model's estimated probability

$$
\widehat{p}(Y=1 \mid X)
$$

is tracked across these demographic subgroups to detect systematic disparities. Because $f(X)$ is explicitly numeric, standard fairness metrics (e.g., demographic parity, equal opportunity) can easily be computed.

Interpretability. Requiring the LLM to provide the chain-of-thought text alongside the numeric score can assist in diagnosing errors and identifying the sources of risk or ambiguity. Embeddings and dimensionality reduction can further reveal latent clusters in the data, creating a rich environment for deeper model explanations.

## Page 225
# Monitoring and ongoing controls 

After deployment, continuous monitoring should track:

- Data inputs: Ensuring that new data remain consistent with original training or fine-tuning assumptions.
- Performance metrics: Watching for significant shifts in numeric predictions or text outputs, indicative of concept drift.

Regular review of numeric scoring trends - particularly areas with unexpectedly high or low scores - can reveal potential hallucinations or systematic biases early, prompting timely interventions. Governance bodies can decide on revised thresholds, updated prompts, or further training if required.

## Conclusion

Imposing a numeric score on every LLM decision links the model's text generation to rigorous statistical validation, a hallmark of actuarial and data science practice. By integrating such quantitative outputs with robust governance, performance tracking, bias assessments, and human oversight, actuaries can more confidently deploy LLM-based solutions in high-stakes or regulated environments. These protocols do not merely enhance transparency - they offer a meaningful safeguard against hallucinations by flagging uncertain or outlier score values for deeper review.

### 10.6.10 Sparse auto-encoders and mechanistic interpretability

LLMs predominantly employ decoder transformer architectures (Section 10.4); however, these models are quite difficult to interpret, thus, it is hard to understand how the models have produced outputs - which may be used in sensitive downstream processes. Recently, there has been renewed interest in sparse auto-encoders and other dimensionalityreduction techniques for understanding or probing the internal representations learned by these massive networks. Building on the discussion of auto-encoders in Section 10.2.1, sparse variants of auto-encoders impose additional constraints to reveal interpretable, low-dimensional structures. In parallel, mechanistic interpretability research aims to reverse-engineer the computations of large models by inspecting how individual parameters, neurons, or attention heads contribute to emergent language capabilities.

## Sparse auto-encoders in the context of LLMs

Recall that an auto-encoder seeks to learn a bottleneck representation of input data, see Section 9.2.2. Sparse auto-encoders add a sparsity constraint on the hidden layer activations. Formally, if $\boldsymbol{Z}=\Phi(\boldsymbol{X})$ is an $m$-dimensional hidden representation of input $\boldsymbol{X}$, sparsity can be encouraged by adding a regularization term such as

$$
R(\boldsymbol{Z})=\eta \sum_{j=1}^{m} \phi\left(Z_{j}\right)
$$

## Page 226
where $\phi$ is a sparsity-inducing function, e.g., the $L^{1}$-norm or the KL divergence from a low target activation; see Section 2.4. By pushing many $Z_{j}$ values towards zero, the hidden layer tends to learn disentangled or factorized features.
In the context of LLM embeddings (e.g., word embeddings, hidden states of transformers), sparse auto-encoders can serve as a diagnostic or exploratory tool:

- Representation analysis: By fitting a sparse auto-encoder to hidden activations from a LLM, we may uncover latent components that correspond to semantic or syntactic features of language. This can shed light on how the network distributes information across its many dimensions. Often, the link between the learned sparse representations and the natural language concepts, these represent, might itself be made with LLMs; see Cunningham et al. [46].
- Dimensionality reduction for visualization: Sparse auto-encoders provide a controllable way to project high-dimensional LLM embeddings (often thousands of dimensions) down to a smaller but still interpretable sub-space, potentially aiding in model debugging or interpretability tasks.
- Model compression: In some cases, the sparse representation learned via autoencoding can hint at parameter-efficient strategies to prune or quantize model weights.

Although LLMs themselves typically rely on dense transformer layers, the application of sparse auto-encoders to LLM-generated activations or embeddings is increasingly explored in post-hoc interpretability settings, aiming to identify stable, low-dimensional factors that underlie the rich behaviors observed in large-scale generation.

# Mechanistic interpretability 

Mechanistic interpretability seeks to uncover how LLMs perform computations at a finegrained, algorithmic level. Rather than treating a LLM as a monolithic black box, researchers strive to identify and interpret the roles of individual components, such as attention heads, FNN layers and neurons, in linguistic processing; see Olah et al. [170]. This line of inquiry has gained momentum as models grow larger, prompting deeper examinations into how these intricate architectures handle tasks ranging from syntactic parsing to semantic understanding.
Recent advances in mechanistic interpretability have employed a variety of techniques. One approach, sometimes referred to as activation patching or ablation, involves systematically intervening in model activations while the network processes specific inputs; see Nanda et al. [163]. By replacing or removing particular activation vectors - often in selective layers - researchers can observe how these modifications alter the model's outputs. If performance on a certain task degrades significantly after a specific intervention, that suggests the intervened neurons or layers play a causal role. In parallel, tracing information flow across a transformer stack has illuminated how attention heads and FNN layers pass signals that reflect long-range context, anaphora resolution, and even forms of logical inference; see Olah et al. [171]. Another promising direction involves neurosymbolic probing, where tasks derived from symbolic or logic-based paradigms are used to

## Page 227
test whether sub-circuits within the network encode these structures internally; see Cao et al. [39]. For example, if a network reliably identifies symbolic patterns in its hidden representations, it indicates emergent, structured computations within the parameters.

# Synergies with sparse auto-encoders 

The synergy between mechanistic interpretability and sparse auto-encoders arises from their shared focus on identifying meaningful structure within high-dimensional representations. Sparse auto-encoders, by design, encourage models to compress data into a limited set of activation units, thereby shedding light on which dimensions are most critical for a given task; see Makhzani-Frey [147]. When examining LLM activations, if a sparse auto-encoder robustly encodes certain linguistic features in a small subset of neurons, this subset may correspond to functionally relevant circuits in the original model. Interventions such as ablation or activation patching can then be more narrowly targeted, allowing researchers to focus on the most influential dimensions within the network.
Enforcing sparsity is particularly helpful when trying to localize features to individual neurons or small neuron clusters. For instance, if a sparse auto-encoder bottleneck consistently highlights dimensions tied to tense or sentiment, these dimensions become natural entry points for deeper mechanistic analysis. Researchers can then ablate or patch only those critical neurons to measure how the LLM's behavior changes, shedding light on where and how key linguistic functions are implemented.

## Discussion and future directions

In summary, combining auto-encoder-based methods with mechanistic interpretability provides a powerful toolkit for unearthing how LLMs encode and transform information; Hinton-Salakhutdinov [97]. By extracting compact, interpretable representations of activations, sparse auto-encoders reveal hidden structures that might otherwise remain concealed in high-dimensional parameter spaces. Mechanistic interpretability goes a step further by attempting to reverse-engineer the computations behind these structures. Through selective analysis of sub-circuits, neurons, or attention heads, it becomes possible to illuminate how tasks such as coreference resolution, numeric reasoning, and code generation are managed internally.
Looking ahead, deeper integration of these research directions may inspire new architectural designs or training paradigms that prioritize intrinsic interpretability. For instance, networks could incorporate sparsity constraints during training, encouraging representational clarity from the outset. Circuit-level regularization might also become a standard practice, with the goal of engineering LLMs whose inner operations are more transparent and less prone to failure modes that are difficult to detect. As models scale toward trillions of parameters, understanding these internal processes will likely become increasingly critical for ensuring robustness, safety, and alignment with human values; Bender-Koller $[18]$.

## Page 228
# 10.6.11 Summary 

LLMs represent a paradigm shift in generative modeling, wherein a single pretrained neural network can address myriad tasks with minimal additional training. By incorporating human feedback mechanisms (RLHF), employing specialized prompts, or enabling self-consistency checks, LLMs can produce high-quality, context-aware, and interpretable outputs. Nonetheless, significant challenges remain, including controlling unwanted biases, ensuring factual accuracy, and addressing potential misuse. Ongoing research in foundation models, fine-tuning protocols, and advanced prompting strategies continues to shape the evolving landscape of LLMs.

### 10.7 Conclusion: From empirical scaling to broad AI

In this chapter, we have seen how LLMs - trained at unprecedented scales on diverse, high-dimensional data - build upon core ideas in empirical modeling that are intimately familiar to the actuarial profession, and that we have elucidated in these notes. The core principle of collecting data, specifying a flexible model architecture, and adjusting parameters to fit observations is the same principle that underlies many actuarial techniques, albeit that the actuarial techniques are typically applied at a (much) smaller scale.
Yet, as we increase the amount of data and computational resources, we find that LLMs, propelled by auto-regressive transformers and alignment protocols such as RLHF, can begin to exhibit emergent capabilities. No longer do these models merely perform specialized tasks like text classification or simple regressions; instead, they start to display a more generalized form of intelligence - able to write code, solve multi-step reasoning problems, and even critique or refine their own outputs. Powering these models to the next stage of usefulness are techniques to cause these models to "think" more and approximate some level of reasoning.
This scaling-up process, from small datasets to massive corpora, parallels the journey of actuarial science itself. In actuarial work, we often rely on large empirical datasets - claims histories, market data, demographic projections - and calibrate models to approximate real-world behavior. As data volumes and computational budgets have expanded, so too has the potential for sophisticated machine learning methods to deliver richer insights with less human-crafted structure.
Indeed, this evolution suggests that the classical actuarial approach - balancing rigorous statistical methods applied to empirical data with real-world pragmatism - that has now been adopted more widely in machine learning and artificial intelligence may serve as a foundation for creating even more advanced AI systems. Although true general artificial intelligence remains an open challenge, LLMs have brought us closer to models capable of multi-domain reasoning and adaptive problem-solving. Building on these advances and refining the models explored above on expanding datasets may lead, step by step, toward increasingly general and powerful AI capabilities.

## Page 229
# Chapter 11 

## Reinforcement learning

### 11.1 Introduction

Reinforcement learning is a fast evolving and exciting field on optimal decision making in a dynamic environment. In particular, reinforcement learning is one of the key techniques behind reasoning which is a crucial feature of modern generative AI models, e.g., used in solving mathematical problems.
To give full consideration to reinforcement learning, we would need to write an entire book. Our aim here is to give a short introduction to reinforcement learning and discuss what kind of problems can be studied by this technology. The reader should be aware of the fact that we only present the most simple problems and their solutions, but the latest technology is by far more developed; classical references on reinforcement learning are Sutton-Barto [212] and Murphy [162], the material presented in this section is largely taken from these two references. For an explicit actuarial example considering an optimal pricing problem, see Palmborg-Lindskog [173]. This paper presents a non-life insurance premium control problem that seeks for an optimal premium rule trying to maximize profits, complying with solvency regulation, and considering customers' price sensitivities. Such a multi-objective premium control problem can be solved dynamically by learning how specific actions contribute to a total reward with the aim of maximizing this total reward. This is the general philosophy in reinforcement learning.
Before starting, we would like to mention that the reinforcement learning community is somewhat disjoint from the classical machine learning community and also from the statistical community. We emphasize this because terminology can be quite different in these different communities, e.g., bootstrapping can mean rather different things depending on the specific community. We mention this to highlight that there may be some inconsistencies in this section compared to earlier chapters.
Generally speaking, in predictive modeling a decision maker tries to make accurate forecasts, and to evaluate the accuracy of her/his forecasts, the decision maker receives the correct answer at a later stage. As an example, we forecast an insurance claim at the beginning of the period, and by the end of the period we know the true claim incurred. In contrast, in reinforcement learning a decision maker takes actions which are rewarded. However, there is no right or wrong answer that can be revealed to the decision maker, she/he only gets a feedback in terms of a bigger or smaller reward, and at the same time,

## Page 230
she/he does not have the possibility to exploit all potential actions and their resulting rewards. For example, an insurer (decision maker) can either increase or lower the insurance premium, and by the end of the period the insurer gets a reward in terms of the total premium earned (based on the assumption that the customers will only sign new contracts up to their price tolerance levels), but there is no possibility for the insurer to simultaneously test different pricing strategies before exercising one of them. Using reinforcement learning, the insurer can continuously (online) learn to improve its decision making strategy by learning from the feedback received.

# 11.2 Multi-armed bandit problem 

The classical multi-armed bandit problem gives a fairly good introduction and overview of the field of reinforcement learning. That is why we start with this classical example (which is not directly related to insurance).
Assume that a gambler has the option to play on $k \geq 2$ different slot machines (one-armed bandits), where each of the slot machines has a different random payout. Naturally, the gambler's goal is to maximize her/his gain, and she/he selects the slot machine from which she/he believes that it will hit the jackpot in the next round.

In this game the gambler can exploit the slot machine that she/he believes has the biggest payout, but at the same time it may also be worth to explore the other $k-1$ slot machines because one of them could even be better.

We formalize this. We work in discrete time $t \in \mathbb{N}_{0}$. In each round $t \geq 0$ of the game, the gambler can select an action $A_{t} \in \mathcal{A}$ from the action space $\mathcal{A}$. In the multi-armed bandit problem the action space refers to the $k$ available slot machines, $\mathcal{A}=\{1, \ldots, k\}$. The taken action $A_{t}$ provides a real-valued (random) reward $R_{t+1}$ from which we aim at learning the optimal action, called control. The (true) action-value is defined by

$$
q(a)=\mathbb{E}\left[R_{t+1} \mid A_{t}=a\right]
$$

for $a \in \mathcal{A}$. This is called the true action-value because it uses the true reward mechanism; this is similar to the true regression function in (1.2).
If we knew the true action-value function $a \mapsto q(a)$, we would simply maximize this function over $a \in \mathcal{A}$, to obtain the maximal (expected) reward. Typically, the true actionvalue function is unknown to us because we do not know the precise reward mechanisms of the different slot machines. A general way to solve this problem is to try to learn this action-value function by exploring and exploiting the slot machines over several rounds of the game. This gives us estimates $\left(\widehat{q}_{t}(a)\right)_{a \in \mathcal{A}}$ in every round $t \geq 0$ for the true actionvalue function $q$. We use these estimates $\left(\widehat{q}_{t}(a)\right)_{a \in \mathcal{A}}$ for the next round of the game. They are then updated according to the received reward $R_{t+1}$ in this next round. Thus, the reward $R_{t+1}$ is a feedback on how our specific action $A_{t}$ has performed.

## Page 231
For given estimates $\left(\widehat{q}_{t}(a)\right)_{a \in \mathcal{A}}$ at time $t \geq 0$, the greedy action is the one with the (immediate) highest action-value estimate

$$
\underset{a \in \mathcal{A}}{\arg \max } \widehat{q}_{t}(a)
$$

If we select the greedy action, we exploit our current knowledge around the maximum of the estimated action-value function $a \mapsto \widehat{q}_{t}(a)$. But we can also select a non-greedy action by exploring whether we can improve our estimates $\left(\widehat{q}_{t}(a)\right)_{a \in \mathcal{A}}$ by selecting a different slot machine. Exploiting is the (estimated) optimal one-step ahead strategy but it is not necessarily optimal for multiple steps ahead (in the long run). This is precisely the tradeoff between exploiting and exploring which may have a sophisticated interrelationship.

To better understand this reinforcement learning mechanism, it is useful to give an explicit numerical example. We present the example of Sutton-Barto [212, Section 2.3].

Example 11.1. We choose $k=10$ one-armed bandits and we select their true actionvalues $(q(a))_{a=1}^{10}$ by simulating them from independent standard uniform Gaussian distributions. These true action-values $(q(a))_{a=1}^{10}$ are kept fixed, and they are unknown to the gambler. Figure 11.1 illustrates these true action-values, the most promising slot machine is number $a=4$, closely followed by slot machine number $a=8$.

Figure 11.1: $k$-armed bandit true action-values $(q(a))_{a=1}^{k}, k=10$.
The reward $R_{t+1}$ on slot machine $a \in \mathcal{A}$ in period $t \geq 0$ is determined by

$$
\left.R_{t+1}\right|_{A_{t}=a} \sim \mathcal{N}(q(a), 1)
$$

and we assume a Markov property, meaning that this reward $R_{t+1}$ only depends on the last selected action $A_{t}$, and not on any information prior to time period $t$.
The most natural and simple action-value estimate is given by computing the empirical average rewards on each slot machine $a \in \mathcal{A}$

$$
\widehat{q}_{t}(a)=\frac{1}{\sum_{s=0}^{t-1} \mathbb{1}_{\left\{A_{s}=a\right\}}} \sum_{s=0}^{t-1} R_{s+1} \mathbb{1}_{\left\{A_{s}=a\right\}}
$$

Version March 3, 2025, @AI Tools for Actuaries
![Page 231 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p231_img1.jpg)

## Page 232
and we set it to a default value for action-values, i.e., $a \in \mathcal{A}$, without any observations. The law of large numbers tells us that $\widehat{q}_{t}(a) \rightarrow q(a)$, a.s., for $t \rightarrow \infty$, and supposed $a$ is selected infinitely often in these trials. At time $t \geq 0$, the next greedy action is given by

$$
A_{t}=\underset{a \in \mathcal{A}}{\arg \max } \widehat{q}_{t}(a)
$$

with a deterministic rule if there is more than one solution to this maximization problem. This greedy step exploits the estimated optimal slot machine at time $t \geq 0$. To also explore the other slot machines, we insert random non-greedy steps, be using a so-called $\varepsilon$-greedy strategy. Select $\varepsilon \in(0,1)$ and sample i.i.d. Bernoulli random variables $B_{t}, t \geq 0$, being independent of everything else and taking the value one with probability $\varepsilon$.

The $\varepsilon$-greedy action at time $t \geq 0$ is given by

$$
A_{t}= \begin{cases}\arg \max _{a \in \mathcal{A}} \widehat{q}_{t}(a) & \text { if } B_{t}=0 \\ U_{t} & \text { if } B_{t}=1\end{cases}
$$

where $U_{t}$ is uniform on $\mathcal{A}$ and independent of everything else.
Thus, with probability $1-(\varepsilon-\varepsilon / k)$ we exploit and with probability $\varepsilon-\varepsilon / k$ we explore. Since this also implies that, a.s., every action $a \in \mathcal{A}$ is selected infinitely often as $t \rightarrow \infty$, we receive the law of large numbers for all actions $a \in \mathcal{A}$, saying that the estimated action-values $\widehat{q}_{t}(a)$ converge to the true ones $q(a)$, a.s., as $t \rightarrow \infty$.

Figure 11.2: (lhs) Development of average rewards $\bar{R}_{t}$, and (rhs) ratio of selection of the optimal slot machine for iterations $1 \leq t \leq 1000$.

We implement the $k$-armed bandit reinforcement learning algorithm (11.2) for different $\varepsilon$-greedy strategies with $\varepsilon \in(0.01,0.02,0.05)$. The results are shown in Figure 11.2. The left-hand side gives the average rewards, under the gambler's strategy (11.2), defined by

$$
\bar{R}_{t}=\frac{1}{t} \sum_{s=0}^{t-1} R_{s+1}
$$

The right-hand side of the figure shows the proportion of the selection of the optimal slot machine $a=4$, i.e., the slot machine $a \in \mathcal{A}$ that has the highest expected reward
![Page 232 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p232_img1.jpg)

## Page 233
$q(a)$; this optimal value is illustrated by the black horizontal line in Figure 11.2 (lhs). We observe that for all $\varepsilon$ choices the average rewards $\bar{R}_{t}$ approach this optimal value $q(a)$, $a=4$, and there seems to be little difference in their speeds of convergence. On the other hand, due to the $\varepsilon$-greedy strategy, the average reward will not converge to $q(a)$, but to a smaller value, because the $\varepsilon$-greedy sampling gives a fixed proportion of non-optimal slot machine selections. For convergence to $q(a)$ one also needs to temper the Bernoulli probability $\varepsilon_{t} \downarrow 0$ for $t \rightarrow \infty$.
Figure 11.2 (rhs) shows the proportions of the selection of the optimal slot machine $a=4$

$$
\frac{1}{t} \sum_{s=0}^{t-1} \mathbb{1}_{\left\{A_{t}=4\right\}}
$$

These quantities converge to $1-(\varepsilon-\varepsilon / k)$, illustrated by the horizontal lines in Figure 11.2 (rhs). In two cases, we have a rather smooth increase of these proportions to their limits, only the green graph looks a bit surprising. Remark that all these graphs depend on the initialization of the algorithm. We have randomly initialized $\left(\widehat{q}_{0}(a)\right)_{a=1}^{k}$, and different seeds provide different results. A random initialization avoids the difficulty of having multiple maximums in (11.2); if one sets $\left(\widehat{q}_{0}(a)\right)_{a=1}^{k}$ to very large values, this promotes exploring in the beginning of the algorithm, because every initial reward is likely going to be a disappointment moving on the the next slot machine. Let us try to understand the green graph of Figure 11.2 (rhs).

Figure 11.3: Explicit selections $A_{t} \in \mathcal{A}, t=0, \ldots, 1000$, of the different slot machines in the three examples of Figure 11.2 (rhs).

Figure 11.3 shows the selected slot machines $\left(A_{t}\right)_{t=0}^{1000}$ of the three examples of Figure 11.2 (rhs). We focus on the green graph on the right-hand side. The optimal slot machine is $a=4$, and we observe that in the green case, the algorithm is rather undecided about the two machines $a=4$ and $a=8$ in the first iterations of the algorithm. These two slot machines have quite close long-term rewards $q(a)$, see Figure 11.1. In this example, only after roughly $t=400$ iterations, we have found the best slot machine $a=4$. This explains the green curve in Figure 11.2 (rhs).

Conclusion. Example 11.1 gives the basic understanding of reinforcement learning. Subsequent extensions study more sophisticated dynamic decision making problems, e.g., having infinite (continuous) state spaces, having more sophisticated dynamic learning
![Page 233 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p233_img1.jpg)

## Page 234
problems, having side constraints and multiple targets, etc. This will require more sophisticated reinforcement learning algorithms, potentially based on approximations where some of the quantities cannot be computed explicitly, etc. In the remainder of this section we will discuss some of these extensions. The main purpose of this discussion is to make the reader familiar with some of the reinforcement learning concepts and intuition. Clearly, this discussion should be understood as an introduction, and for more advanced reinforcement learning technologies, the reader is referred to the specialized literature on reinforcement learning.

# 11.3 Incremental learning 

Example 11.1 has been implemented brute force, by simply increasing the information set at each period $t \geq 0$ by one unit. To keep the size of the memory constant, one should use a so-called incremental learning implementation, see Sutton-Barto [212, Section 2.4], meaning that one should update the action-value estimates recursively

$$
\begin{aligned}
\widehat{q}_{t+1}(a) & =\frac{1}{N_{t}(a)} \sum_{s=0}^{t} R_{s+1} \mathbb{1}_{\left\{A_{s}=a\right\}}=\frac{1}{N_{t}(a)}\left(R_{t+1} \mathbb{1}_{\left\{A_{t}=a\right\}}+N_{t-1}(a) \widehat{q}_{t}(a)\right) \\
& =\widehat{q}_{t}(a)+\frac{1}{N_{t}(a)}\left(R_{t+1}-\widehat{q}_{t}(a)\right) \mathbb{1}_{\left\{A_{t}=a\right\}}
\end{aligned}
$$

with the counts on each slot machine $a \in \mathcal{A}$

$$
N_{t}(a)=\sum_{s=0}^{t} \mathbb{1}_{\left\{A_{s}=a\right\}}
$$

These updates can be performed on a constant memory size and they essentially use the Markov property. Beyond that they have a rather interesting structure that is common to many reinforcement learning algorithms. We can interpret $1 / N_{t}(a)$ as a learning rate or a step size parameter.
For suitable learning rates $\varrho_{t}(a)>0$, we obtain updates

$$
\widehat{q}_{t+1}(a)=\widehat{q}_{t}(a)+\varrho_{t}(a)\left(R_{t+1}-\widehat{q}_{t}(a)\right) \mathbb{1}_{\left\{A_{t}=a\right\}}
$$

This looks very innocent, but actually this structure is the key to many reinforcement learning algorithms, namely, it proposes temporal difference learning by incrementally improving the estimate over time by the new experience
new estimate $\leftarrow$ old estimate $+\varrho$ (new experience - old estimate).
It can be interpreted as trying to predict the new experience $R_{t+1}$ by the old estimate $\widehat{q}_{t}(a)$, and (11.4) can then be seen as the corresponding updating step, trying to improve the prediction based on the new experience.

Summary. The key to reinforcement learning often has it grounds in a temporal difference learning structure of type (11.4). The multi-armed bandit problem of Example 11.1 has all these features. There are some extensions/changes that we are going to introduce, below, to make the framework more practical.

## Page 235
- We extend the actions $\left(A_{t}\right)_{t \geq 0}$ and the rewards $\left(R_{t}\right)_{t \geq 1}$ by a third sequence, the states $\left(S_{t}\right)_{t \geq 0}$. This will allow us to solve more interesting problems.
- We will not directly focus on the rewards $\left(R_{t}\right)_{t \geq 1}$, but rather on the future expected discounted rewards, called expected gains, for given (initial) state-action pairs $\left(S_{t}, A_{t}\right)$. Under an unknown reward mechanism, we need to estimate these expected gains along the way.


# 11.4 Tabular learning problems 

The above multi-armed bandit problem introduced the essentials of reinforcement learning. The following sections formalize this process w.r.t. the classical literature in reinforcement learning, in particular, we are going to extend the model by a state space; the following outline is taken from Sutton-Barto [212, Chapter 3].

A Markov decision process (MDP) considers three different sequences, states $\left(S_{t}\right)_{t \geq 0}$ living on a state space $\mathcal{S}$, actions $\left(A_{t}\right)_{t \geq 0}$ living on a action space $\mathcal{A}$, and rewards $\left(R_{t}\right)_{t \geq 0}$ living on a reward space $\mathcal{R} \subset \mathbb{R}$. We initialize $R_{0}=0$; this initial reward is usually not needed, see Example 11.1, but it allows us to study the triples $\left(R_{t}, S_{t}, A_{t}\right)$, for all $t \geq 0$. A MDP then describes the time-series of these triples

$$
R_{0}, S_{0}, A_{0} ; R_{1}, S_{1}, A_{1} ; R_{2}, S_{2}, A_{2} ; \ldots
$$

which will additionally obey a Markov property.

Figure 11.4: Environment-agent interaction process (11.5) for $t \geq 0$.

A finite $M D P$ has three finite spaces $\mathcal{S}, \mathcal{A}$ and $\mathcal{R}$. If the state space $\mathcal{S}$ and the action space $\mathcal{A}$ are finite, we speak about tabular learning because we can store all potential state-action pairs $(s, a) \in \mathcal{S} \times \mathcal{A}$ in a finite table. This outline mainly focuses on tabular learning, and possible extensions are only briefly considered in Section 11.8, below.

In this dynamic learning setting, one distinguishes two different cases, one can either have a continuing task where $\left(S_{t}\right)_{t \geq 0}$ randomly evolves over the state space $\mathcal{S}$ forever. In contrast, an episodic task is assumed to terminate, and we can restart it in a green field again. In that case, one adds a terminal (absorbing) state to the state space $\mathcal{S}^{\dagger}=\mathcal{S} \cup\{\dagger\}$, and the game is terminated when $S_{t+1}$ enters the terminal state $\dagger$ (for its first time). This motivates the definition of the stopping time

$$
T=\inf \left\{t \geq 0 ; S_{t+1} \in \mathcal{S}^{\dagger} \backslash \mathcal{S}\right\} \in[0, \infty]
$$
![Page 235 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p235_img1.jpg)

## Page 236
if there is no terminal state or if the state space process does not reach the terminal state, we set $T=\infty$.
Figure 11.4 shows that a MDP involves two different (Markovian) transitions: (a) there is the environment's dynamics $p: \mathcal{S} \times \mathcal{R} \times \mathcal{S} \times \mathcal{A} \rightarrow[0,1]$ in blue color, and (b) there is the agent's policy $\pi: \mathcal{A} \times \mathcal{S} \rightarrow[0,1]$ in orange color. Markovian means that these dynamics are fully determined by just considering the realization in the previous iteration. We discuss this.
(a) Environment's dynamics. The environment's dynamics is given by nature, and it is either known or unknown to the decision maker.
Specifically, in the finite spaces case, we assume the transition probabilities

$$
\begin{aligned}
p\left(s^{\prime}, r \mid s, a\right) & :=\mathbb{P}\left[S_{t+1}=s^{\prime}, R_{t+1}=r \mid S_{t}=s, A_{t}=a\right] \\
& =\mathbb{P}\left[S_{t+1}=s^{\prime}, R_{t+1}=r \mid S_{t}=s, A_{t}=a,\left(S_{u}\right)_{u=0}^{t-1},\left(A_{u}\right)_{u=0}^{t-1},\left(R_{u}\right)_{u=0}^{t}\right]
\end{aligned}
$$

for $t \geq 0$.
Thus, the pair $\left(S_{t+1}, R_{t+1}\right)$ only depends on the previous state-action pair $\left(S_{t}, A_{t}\right)$, this is the Markov property we use for the environment's dynamics. These transition probabilities $p$ fully determine the environment's dynamics of the MDP. We give some remarks:

- In the case of a terminal state $\dagger$ and state space $\mathcal{S}^{\dagger}$, one constrains (11.7) to remain in the terminal state with probability one (and all subsequent rewards and actions are discarded because the process is terminated).
- To run this dynamics we still need to define the agent's policy $\pi(a \mid s)$, and we need to specify the initial state $S_{0}$; we have set initial reward $R_{0}=0$.

Using the stopping time $T$ introduced in (11.6), one defines the total discounted reward, called gain, after time $t$ by

$$
G_{t}=\sum_{u=t}^{T} \gamma^{u-t} R_{u+1}
$$

for $\gamma \in(0,1]$, and where an empty sum is set equal to zero.
The gain $G_{t}$ is not generally finite for $\gamma=1$, i.e., there are models without a stopping $T=\infty$ or models with a slow (heavy tailed) stopping which may make the gain infinite on average for $\gamma=1$. For $\gamma<1$, this sum is always finite (also on average), because the rewards $\left(R_{t}\right)_{t \geq 1}$ are uniformly bounded on a finite reward space $\mathcal{R}$, providing a uniform upper bound (and a finite mean) from the corresponding geometric series.
(b) Agent's policy. There remains the agent's policy; note that the decision maker is commonly called agent.
The agent's policy is assumed to be of the form

$$
\begin{aligned}
\pi(a \mid s) & :=\mathbb{P}\left(A_{t}=a \mid S_{t}=s\right) \\
& =\mathbb{P}\left(A_{t}=a \mid S_{t}=s,\left(S_{u}\right)_{u=0}^{t-1},\left(A_{u}\right)_{u=0}^{t-1},\left(R_{u}\right)_{u=0}^{t}\right)
\end{aligned}
$$

for $t \geq 0$.

## Page 237
This policy $\pi$ describes the decision making of the agent, see Figure 11.4. This decision making can be deterministic, in which case the agent's policy $\pi(\cdot \mid s)$ is a single point measure in some action $a \in \mathcal{A}$, but it can also be random with $\pi(\cdot \mid s)$ describing a distribution over the action space $\mathcal{A}$. In case of a deterministic policy, it is more convenient to use the notation $\pi: \mathcal{S} \rightarrow \mathcal{A}, s \mapsto a=\pi(s) \in \mathcal{A}$.
We assume that the policy $\pi(\cdot \mid s)$ is not influenced by the rewards, see (11.9) and the dotted blue line in Figure 11.4. The goal is to select the optimal policy by maximizing the future expected discounted rewards, called value function, see next section.

The environment's transition probabilities $p$, given by (11.7), and the agent's policies $\pi$, given by (11.9), describe the finite MDP, as illustrated in Figure 11.4. The goal of this dynamic decision making problem is to find an optimal policy $\pi^{*}$ for a given environment's dynamics $p$ that maximizes the expected gain. This problem is solved by reinforcement learning, and there are two rather different situations: either the environment's dynamics $p$ is known to the agent or it is unknown to the agent. In the latter case, we can perform model-based reinforcement learning by trying to learn the model, or we can perform model-free reinforcement learning where the environment's dynamics is not needed to solve the task.

# 11.5 Known environment's dynamics 

We start by assuming a known environment's dynamics $p$; in most cases this is not realistic, but it helps us to shape the ideas. In this setting, there is no model uncertainty because the dynamics of the MDP is known and used to solve the task. This case is known as model-based reinforcement learning, which applies to an either known or an estimated environment's dynamics for solving the task.

We add the selected policy $\pi$ to the notation $\mathbb{P}_{\pi}$ and $\mathbb{E}_{\pi}$, respectively.
The value function (state-value function or expected gain) of a given policy $\pi$ is defined by

$$
v_{\pi}(s)=\mathbb{E}_{\pi}\left[G_{t} \mid S_{t}=s\right]=\mathbb{E}_{\pi}\left[\sum_{u=t}^{T} \gamma^{u-t} R_{u+1} \mid S_{t}=s\right]
$$

for states $s \in \mathcal{S}$.
Because of stationary we can drop the time index $t$ on the left-hand side of the previous identity. Under a known environment's dynamics $p$, the value function $v_{\pi}$ can be computed for every policy $\pi$, and the aim is to find the optimal policy $\pi^{*}$ that maximizes the value function. This then gives the optimal value

$$
v_{*}(s):=v_{\pi^{*}}(s)=\sup _{\pi} v_{\pi}(s), \quad \text { for } s \in \mathcal{S}
$$

In this setting, the main question is whether there exists an optimal policy $\pi^{*}$ that solves (11.10), and, if yes, how can it be found. In the finite MDP case and under deterministic policies, there exists an optimal policy $\pi^{*}$; see Puterman [178, Corollary 6.2.8]. Moreover, there are many other settings where such an existence result can be proved. In the finite

## Page 238
tabular case and under a known environment's dynamics $p$, the optimal policy problem is then solved by dynamic programming. There are two different versions that are useful: (A) policy iteration and (B) value iteration. We briefly describe these. Let $\mathcal{A}(s) \subset \mathcal{A}$ be the admissible actions $a$ in state $s \in \mathcal{S}$.

# 11.5.1 Policy iteration 

Assume a known environment's dynamics $p$. For policy iteration one alternates the following two steps: (a) policy evaluation and (b) policy improvement.
(a) Policy evaluation (also called prediction problem) aims at computing the value function $v_{\pi}$ for a fixed policy $\pi$. Deconvoluting the Markovian property by one step, gives us the Bellman equations

$$
v_{\pi}(s)=\sum_{a \in \mathcal{A}(s)} \pi(a \mid s) \sum_{s^{\prime} \in \mathcal{S}} \sum_{r \in \mathcal{R}} p\left(s^{\prime}, r \mid s, a\right)\left(r+\gamma v_{\pi}\left(s^{\prime}\right)\right)
$$

for $s \in \mathcal{S}$. These Bellman equations (11.11) have a unique solution if $\gamma<1$. Remark, for given $\pi,(11.11)$ gives us a system of $|\mathcal{S}|$ linear equations for $\left(v_{\pi}(s)\right)_{s \in \mathcal{S}}$. Thus, for known environment's dynamics $p$, this can fully be solved for the given policy $\pi$.
(b) Policy improvement aims at improving the policy for a given value function $\left(v_{\pi}(s)\right)_{s \in \mathcal{S}}$. The is done by a greedy step for deterministic policy improvements.

Algorithm 4 Policy iteration algorithm
(0) $k=0$ : select an initial deterministic policy $\pi_{k}: \mathcal{S} \rightarrow \mathcal{A}$. Fix $\gamma<1$.
(1) Iterate for $k \geq 0$ until the policy is stable:
(a) Apply policy evaluation to the deterministic policy $\pi_{k}$ to find the unique solution of the value function $\left(v_{\pi_{k}}(s)\right)_{s \in \mathcal{S}}$ to the linear system

$$
v_{\pi_{k}}(s)=\sum_{s^{\prime} \in \mathcal{S}} \sum_{r \in \mathcal{R}} p\left(s^{\prime}, r \mid s, \pi_{k}(s)\right)\left(r+\gamma v_{\pi_{k}}\left(s^{\prime}\right)\right)
$$

this inserts the deterministic policy $\pi_{k}$ into (11.11).
(b) Apply policy improvement by finding $\left(\pi_{k+1}(s)\right)_{s \in \mathcal{S}}$ in a greedy step

$$
\pi_{k+1}(s)=\underset{a \in \mathcal{A}(s)}{\arg \max } \sum_{s^{\prime} \in \mathcal{S}} \sum_{r \in \mathcal{R}} p\left(s^{\prime}, r \mid s, a\right)\left(r+\gamma v_{\pi_{k}}\left(s^{\prime}\right)\right)
$$

and increase $k \rightarrow k+1$.
(2) Return $\left(\pi_{k^{*}}(s)\right)_{s \in \mathcal{S}}$ and $\left(v_{\pi_{k^{*}}}(s)\right)_{s \in \mathcal{S}}$ for the stopping time $k^{*}$.

Algorithm 4 gives the resulting policy iteration algorithm. We comment on this algorithm. The greedy step (11.13) implies that each policy $\pi_{k+1}$ is uniformly better than the previous one $\pi_{k}$, and this algorithm will converge. As mentioned above, the system

## Page 239
(11.12) describes $|\mathcal{S}|$ linear equations that need to be solved. That is, for a suitable vector $\boldsymbol{b}_{\pi_{k}} \in \mathbb{R}^{|\mathcal{S}|}$ and matrix $B_{\pi_{k}} \in \mathbb{R}^{|\mathcal{S}| \times \mid \mathcal{S}|}$, (11.12) can be rewritten in vector notation

$$
\boldsymbol{v}_{\pi_{k}}=\boldsymbol{b}_{\pi_{k}}+B_{\pi_{k}} \boldsymbol{v}_{\pi_{k}}
$$

where we set $\boldsymbol{v}_{\pi_{k}}=\left(v_{\pi_{k}}(s)\right)_{s \in \mathcal{S}} \in \mathbb{R}^{|\mathcal{S}|}$. This can be solved by a matrix inversion, giving us the solution $\boldsymbol{v}_{\pi_{k}}=\left(\operatorname{Id}-B_{\pi_{k}}\right)^{-1} \boldsymbol{b}_{\pi_{k}}$ for the given policy $\pi_{k}$. In practice, this is solved differently. Namely, the value function can be seen as the fix point of the system (11.12) and (11.14), respectively. This fix point can be found by Banach's fix point iteration, under $\gamma \in(0,1)$. This observation is precisely the idea for the next algorithm, namely, it may not be necessary to run this fix point iteration until convergence, and one could alternate the fix point iteration step(s) and the policy evaluation more frequently.

# 11.5.2 Value iteration 

The difficulty with the policy iteration algorithm is that the policy evaluation may be quite prohibitive in finding the value function $\left(v_{\pi_{k}}(s)\right)_{s \in \mathcal{S}}$ in each step $k \geq 0$ of the algorithm. Value iteration is an alternative solution. For this we remark that the policy evaluation (11.12) can be solved by Banach's fix point iteration for $\gamma \in(0,1)$, thus, we iterate for $\ell \geq 0$

$$
v_{\ell+1}(s)=\sum_{s^{\prime} \in \mathcal{S}} \sum_{r \in \mathcal{R}} p\left(s^{\prime}, r \mid s, \pi_{k}(s)\right)\left(r+\gamma v_{\ell}\left(s^{\prime}\right)\right)
$$

to find $v_{\ell} \rightarrow v_{\pi_{k}}$ for $\ell \rightarrow \infty$ for a fixed policy $\pi_{k}$; this is called iterative policy evaluation. The idea for value iteration is to truncate this iterative policy evaluation after one step. This leads to the simpler Algorithm 5.

Algorithm 5 Value iteration algorithm
(0) For $k=0$, select an initial value function $\left(v_{k}(s)\right)_{s \in \mathcal{S}}$, and $\gamma \in(0,1)$.
(1) Iterate for $k \geq 0$ until stopping is exercised (resulting in stopping index $k^{*}$ )

$$
v_{k+1}(s)=\max _{a \in \mathcal{A}(s)} \sum_{s^{\prime} \in \mathcal{S}} \sum_{r \in \mathcal{R}} p\left(s^{\prime}, r \mid s, a\right)\left(r+\gamma v_{k}\left(s^{\prime}\right)\right), \quad \text { for } s \in \mathcal{S}
$$

(2) Return $\left(v_{k^{*}}(s)\right)_{s \in \mathcal{S}}$ and the resulting deterministic policy $\left(\pi_{k^{*}}(s)\right)_{s \in \mathcal{S}}$ obtained by

$$
\pi_{k^{*}}(s)=\underset{a \in \mathcal{A}(s)}{\arg \max } \sum_{s^{\prime} \in \mathcal{S}} \sum_{r \in \mathcal{R}} p\left(s^{\prime}, r \mid s, a\right)\left(r+\gamma v_{k^{*}}\left(s^{\prime}\right)\right)
$$

Algorithm 5 directly iterates the value optimization, i.e., it focuses on $v_{k}(s)$ instead of the value $v_{\pi_{k}}(s)$ of an actual policy $\pi_{k}$.

### 11.6 Unknown environment's dynamics: Monte Carlo

The policy iteration and the value iteration algorithms presented in the previous Section 11.5 both require the knowledge of the environment's dynamics $p$. In most cases this

## Page 240
knowledge is not available, see, e.g., the multi-armed bandit problem studied in Example 11.1, where the reward distribution is not available, but needs to be learned from experience. Thus, the typical case in practice is the one with unknown environment's dynamics $p$. This section mainly presents a preparation for the next Section 11.7 which explains how to deal with the case of unknown environment's dynamics $p$. The main technique used will be temporal difference learning, and in this section we prepare for this.
In the case of an unknown environment's dynamics $p$, one tries to either learn from actual experience or one tries to learn from simulated experience.

- Learning from actual experience does not require any knowledge about the environment's dynamics $p$. In fact, in a model-free manner, one directly tries to estimate the value function $v(s)$ from actual experience (this is also called prediction), from which one then derives the optimal policy.
- Learning from simulated experience requires a model to generate the (Markov) transitions. This can either be the true environment's dynamics $p$ (if known) or it can be an estimated one. This case refers to model-based reinforcement learning. Noteworthy, in many situations not the entire environment's dynamics $p$ is necessary, in contrast, to the dynamic programming solutions of policy or value iterations, see Algorithms 4 and 5. That is, dynamic programming requires the probability function $p$ in a sufficiently analytical way, whereas the methods presented below only require (explicit) transitions (i.e., samples) of next states $S_{t+1}$ and rewards $R_{t+1}$. Whenever, one works with explicit samples, the process is called Monte Carlo learning.

We expand the value function $\left(v_{\pi}(s)\right)_{s \in \mathcal{S}}$ to the action-value function (also called $Q$ function) which additionally accounts for the taken action

$$
q_{\pi}(s, a)=\mathbb{E}_{\pi}\left[G_{t} \mid S_{t}=s, A_{t}=a\right]=\mathbb{E}_{\pi}\left[\sum_{u=t}^{T} \gamma^{u-t} R_{u+1} \mid S_{t}=s, A_{t}=a\right]
$$

for $s \in \mathcal{S}$ and $a \in \mathcal{A}(s) \subset \mathcal{A}$, where $\mathcal{A}(s)$ are the admissible actions in state $s$.
This is similar to the multi-armed bandit example (11.1), but expanded by the state $S_{t}=s$ and accounting for all future (discounted) rewards under policy $\pi$. We have for any $t \geq 0$ the following two crucial relationships between the value and the action-value functions

$$
\begin{aligned}
v_{\pi}(s) & =\mathbb{E}_{\pi}\left[q_{\pi}\left(S_{t}, A_{t}\right) \mid S_{t}=s\right] \\
q_{\pi}(s, a) & =\mathbb{E}_{\pi}\left[R_{t+1}+\gamma v_{\pi}\left(S_{t+1}\right) \mid S_{t}=s, A_{t}=a\right]
\end{aligned}
$$

this uses the tower property for conditional expectations, and the latter particularly uses that the next action $A_{t}$ only depends on $S_{t}$, and not on the entire history, see (11.9), and on the stationarity of the MDP. The latter identity shows that the action-value function naturally enters the policy improvement (11.13) because we have

$$
\begin{aligned}
\pi_{k+1}(s) & =\underset{a \in \mathcal{A}(s)}{\arg \max } \sum_{s^{\prime} \in \mathcal{S}} \sum_{r \in \mathcal{R}} p\left(s^{\prime}, r \mid s, a\right)\left(r+\gamma v_{\pi_{k}}\left(s^{\prime}\right)\right) \\
& =\underset{a \in \mathcal{A}(s)}{\arg \max } q_{\pi_{k}}(s, a)
\end{aligned}
$$

## Page 241
Therefore, we could have introduced the action-value function $q_{\pi}(s, a)$ already at an earlier stage. A main difference to the previous policy and value iteration algorithms with known environment's dynamics $p$ is that we need to replace the policy improvement (11.13) by a tractable quantity not involving $p$, and for this we directly work with the action-value function $q_{\pi}(s, a)$ instead of the value function $v_{\pi}(s)$, see (11.15). Assume that for any given policy $\pi$, we can observe an episode following $\pi$, and given by the sequence

$$
R_{0}, S_{0}, A_{0} ; R_{1}, S_{1}, A_{1} ; R_{2}, S_{2}, A_{2} ; \ldots ; R_{T}, S_{T}, A_{T} ; R_{T+1}, S_{T+1}
$$

Denote by $T_{s, a}$ the first visit of the observed sequence (11.16) to the state-action pair $(s, a) \in \mathcal{S} \times \mathcal{A}$. This gives us an empirical estimate of the action-value $q_{\pi}(s, a)$ of policy $\pi$ in $(s, a)$

$$
\widehat{q}_{\pi}(s, a)=\sum_{u=T_{s, a}}^{T} \gamma^{u-T_{s, a}} R_{u+1}
$$

This is the simplest version of Monte Carlo estimation of the action-value function, and there are many similar variants; see Sutton-Barto [212, Section 5.1]. For the following algorithm, this estimation is performed for all state-action pairs $(s, a)$ independently, i.e., the estimates do not build on each other. Therefore, according to reinforcement learning terminology, this is not a bootstrapping estimate. ${ }^{1}$ Inserting the empirical estimate (11.17) into (11.15) motivates the following policy improvement step for $k \rightarrow k+1$

$$
\pi_{k+1}(s)=\underset{a \in \mathcal{A}(s)}{\arg \max } \widehat{q}_{\pi_{k}}(s, a)
$$

This leads us to the following algorithm; in the sequel it is more convenient to write the updates $\pi_{k} \rightarrow \pi_{k+1}$ as $\pi \leftarrow \pi$. I.e., instead of labeling the iterations by $k \geq 0$, we use a generic left-arrow ' $\leftarrow$ ' to indicate the updates in the loops of the following algorithms.

The resulting Monte Carlo exploring starts algorithm is presented in Algorithm 6. It considers the first visits $T_{s, a}$ to every state-action pair $(s, a)$ by recursively checking whether there is no earlier visit in the observed episode (11.16); this refers to the name 'exploring starts' of the algorithm. The resulting gain $G$ is then appended to the observed values Gains $(s, a)$ of that state-action pair $(s, a)$, and the current optimal policy estimate $\pi$ is re-evaluated/updated in the observed state $s=S_{t}$. However, this is not for a fixed policy, but rather over all past experienced policies because Gains $(s, a)$ collects the gains over all past episodes (11.16). This algorithm cannot converge to a suboptimal solution because of monotonicity. This is intuitively clear, however, as stated in Sutton-Barto [212, Section 5.3], there is no formal proof of this intuition. There is another difficulty in this algorithm, namely, there needs to be a way of observing an episode (11.16) for each policy $\pi$ under consideration. Typically, this requires simulated experience, but it will not easily be possible to generate actual experience for each policy $\pi$ of interest. E.g., in the multi-armed bandit problem this would require a huge investment to generate an episode for every policy $\pi$ of interest.

[^0]
[^0]:    ${ }^{1}$ Note that bootstrapping in reinforcement learning means that the parameter estimation depends recursively on previous estimates. This is different from the statistical bootstrap of Section 1.5.4.

## Page 242
# Algorithm 6 Monte Carlo exploring starts algorithm 

(0) Select an initial deterministic policy $\pi: \mathcal{S} \rightarrow \mathcal{A}$, an initial action-value function estimate $(\widehat{q}(s, a))_{s, a}$, and set Gains $(s, a)$ to the empty list for all state-action pairs $(s, a)$. Select $\gamma \in(0,1)$.
(1) Iterate until a stopping rule is exercised:

- Choose an initial state $S_{0} \in \mathcal{S}$ and an initial action $A_{0} \in \mathcal{A}\left(S_{0}\right)$ at random so that all potential state-action pairs have a positive probability.
- Observe an episode (11.16) for the present policy $\pi$ with finite termination time $T$, and initialize the gain $G=0$.
- Loop for $t=T, \ldots, 0$ :
* $G \leftarrow \gamma G+R_{t+1}$.
* If the state-action pair $\left(S_{t}, A_{t}\right)$ does not appear in $\left(S_{u}, A_{u}\right)_{u=0}^{t-1}$ :
$\triangleright$ Append the gain $G$ to Gains $\left(S_{t}, A_{t}\right)$;
$\triangleright$ Action-value update: $\widehat{q}\left(S_{t}, A_{t}\right) \leftarrow$ average $\left(\operatorname{Gains}\left(S_{t}, A_{t}\right)\right)$;
$\triangleright$ Policy update: $\pi\left(S_{t}\right) \leftarrow \underset{a \in \mathcal{A}\left(S_{t}\right)}{\arg \max } \widehat{q}\left(S_{t}, a\right)$.

The greedy update (11.18) exploits the optimal action in state $S_{t}$. In all algorithms below we insert $\varepsilon$-greedy updates for a given $\varepsilon \in(0,1)$ to also explore.
An $\varepsilon$-greedy strategy is obtained by replacing (11.18) by the following two steps

$$
a_{k+1}^{+}=\underset{a \in \mathcal{A}\left(S_{t}\right)}{\arg \max } \widehat{q}_{\pi_{k}}\left(S_{t}, a\right)
$$

and update for the new random policy

$$
\pi_{k+1}\left(a \mid S_{t}\right)= \begin{cases}1-\varepsilon\left(1-1 /\left|\mathcal{A}\left(S_{t}\right)\right|\right) & \text { for } a=a_{k+1}^{+}, \\ \varepsilon /\left|\mathcal{A}\left(S_{t}\right)\right| & \text { otherwise. }\end{cases}
$$

This $\varepsilon$-greedy strategy is equivalent to (11.2). It also mitigates the problem that there are state-action pairs that are not sufficiently often visited. In fact, it allows us to drop the inconvenient assumption in Algorithm 6 that each potential pair $(s, a)$ must appear as a starting point with a positive probability. This $\varepsilon$-greedy strategy is called on-policy method because it is used on the policy $\pi_{k}$ itself, whereas off-policy methods work on the transition probabilities to generate the episodes, e.g., by using a version of importance sampling.
There is one cool thing that we did not mention, namely, the above action-value updates can again be done by incremental learning (because we consider simple averages), see Section 11.3 and (11.4),

$$
\widehat{q}\left(S_{t}, A_{t}\right) \leftarrow \widehat{q}\left(S_{t}, A_{t}\right)+\varrho_{t}\left(G\left(S_{t}, A_{t}\right)-\widehat{q}\left(S_{t}, A_{t}\right)\right)
$$

where $G\left(S_{t}, A_{t}\right)$ is the gain appended to $\operatorname{Gain}\left(S_{t}, A_{t}\right)$ in the current iteration, and with

## Page 243
learning rates $\varrho_{t}=\varrho_{t}\left(S_{t}, A_{t}\right)>0$. This is the basis for all upcoming more practical proposals under unknown environment's dynamics $p$.

# 11.7 Temporal difference learning 

All previously considered algorithms are not practical because they either assume that the environment's dynamics $p$ is known or that we can generate an episode (11.16) for any selected policy $\pi$. The former does not work because we typically do not know the mechanism of the environment, see multi-armed bandit example. The latter may be too costly, as we may not be able to generate episodic experiences for any policy of interest, in the multi-armed bandit example this would require a huge investment of the gambler. The following temporal difference learning algorithms allow for actual experience learning, which can be interpreted as online learning as they are performed step-by-step as actual experience becomes available. We will present two different algorithms the SARSA onpolicy control and the $Q$-learning off-policy control.
We first explain the meaning of temporal difference learning. The previous example of Algorithm 6 was based on the incremental updating rule (11.21) stating

$$
\widehat{q}\left(S_{t}, A_{t}\right) \leftarrow \widehat{q}\left(S_{t}, A_{t}\right)+\varrho_{t}\left(G\left(S_{t}, A_{t}\right)-\widehat{q}\left(S_{t}, A_{t}\right)\right)
$$

and the gain generally satisfies the recursion

$$
G_{t}=\sum_{u=t}^{T} \gamma^{u-t} R_{u+1}=R_{t+1}+\gamma G_{t+1}
$$

Assume that the gain $G_{t}=G\left(S_{t}, A_{t}\right)$ belongs to the state-action pair $\left(S_{t}, A_{t}\right)$ at time $t$, and that it has been generated by an episode following policy $\pi$. Then, $G_{t}$ is an empirical estimate for $q_{\pi}\left(S_{t}, A_{t}\right)=\mathbb{E}_{\pi}\left[G_{t} \mid S_{t}, A_{t}\right]$, see (11.17). If we revert this consideration, we can also use the action-value $q_{\pi}\left(S_{t}, A_{t}\right)$ to predict the gain $G_{t}$, i.e., the gain is predicted by its expected value (which minimizes the mean squared error). If we perform this prediction at time $t+1$, i.e., if we use the next action-value $q_{\pi}\left(S_{t+1}, A_{t+1}\right)$ to predict the gain $G_{t+1}$, we receive the following approximation

$$
G_{t} \approx R_{t+1}+\gamma q_{\pi}\left(S_{t+1}, A_{t+1}\right)
$$

Inserting this approximation into the previous incremental update gives us with what is known as the one-step temporal difference $(\mathrm{TD}(0))$ update

$$
\widehat{q}\left(S_{t}, A_{t}\right) \leftarrow \widehat{q}\left(S_{t}, A_{t}\right)+\varrho_{t}\left(R_{t+1}+\gamma \widehat{q}\left(S_{t+1}, A_{t+1}\right)-\widehat{q}\left(S_{t}, A_{t}\right)\right)
$$

with learning rates $\varrho_{t}=\varrho_{t}\left(S_{t}, A_{t}\right)>0$.
This considers a temporal difference component in $t$ which tries to minimize the prediction error of the gain by the estimated action-value function, in fact (11.23) can be interpreted as a gradient descent step; for more technical rigour justifying (11.23) we refer to SuttonBarto [212, Sections 6.1-6.3]. The major difference to the Monte Carlo version of the previous section is that we do not need to compute the gains $G$ for the entire policy

## Page 244
$\pi$ under consideration, but only the next policy actions $\pi\left(A_{t} \mid S_{t}\right)$ matter for this step-by-step update. Therefore, it can be performed online on actual experience. Rewriting (11.23) gives us

$$
\widehat{q}\left(S_{t}, A_{t}\right) \leftarrow \varrho_{t}\left(R_{t+1}+\gamma \widehat{q}\left(S_{t+1}, A_{t+1}\right)\right)+\left(1-\varrho_{t}\right) \widehat{q}\left(S_{t}, A_{t}\right)
$$

Thus, we obtain an update in a recursive credibility manner. This method is therefore also called a bootstrapping method because it improves on the existing estimates; this meaning of bootstrapping is different from Section 1.5.4. Moreover, this estimate is also called a sample estimate because it anticipates the next state-action pair $\left(S_{t+1}, A_{t+1}\right)$ in its estimation. In many cases it can be proved that under some assumptions one obtains convergence to the true value under a given policy $\pi$.

# 11.7.1 SARSA on-policy control 

The first temporal difference method that we present is called SARSA on-policy control. It is called SARSA because from state $S_{t}$, we generate the action $A_{t}$ from the current policy $\pi$, this gives us the reward $R_{t+1}$ and the new state $S_{t+1}$, from which we can generate the next action $A_{t+1}$ to use the bootstrap update (11.23). This update is applied to every non-terminal state $S_{t}$. If $S_{t+1}=\dagger$ is terminal, we set $\widehat{q}\left(S_{t+1}, A_{t+1}\right)=0$.

Algorithm 7 SARSA temporal difference algorithm (for estimating the $Q$-function)
(0) Select an initial action-value function $(\widehat{q}(s, a))_{s, a}$ with $\widehat{q}(\dagger, a) \equiv 0$; and $\gamma \in(0,1)$, and small $\varepsilon>0$.
(1) Iterate until a stopping rule is exercised:

- Choose $S_{0} \in \mathcal{S}$ at random and sample action $A_{0}$ from an $\varepsilon$-greedy policy of structure (11.19)-(11.20).
- Loop for $t \geq 0$ until the terminal value $\dagger$ for $S_{t}$ :
* Given state-action pair $\left(S_{t}, A_{t}\right)$, observe reward $R_{t+1}$ and next state $S_{t+1}$.
* Given state $S_{t+1}$, sample action $A_{t+1}$ from an $\varepsilon$-greedy policy of structure (11.19)-(11.20).
* Update the action-value function with temporal difference (11.23) and use the state-action pair $\left(S_{t+1}, A_{t+1}\right)$ as input to the next step $t+1$.

Algorithm 7 gives the SARSA temporal difference algorithm for estimating the actionvalue function. SARSA on-policy learning is fully practical as we can online (real time) observe the next reward $R_{t+1}$ and the next state $S_{t+1}$, given the state-action pair $\left(S_{t}, A_{t}\right)$ on the selected policy. For an example, we refer to the multi-armed bandit problem that returns the next reward $R_{t+1}$ after we have taken the action $A_{t}$. That is, this can be performed with actual experience, and it does not require any (prior) knowledge about the environment's dynamics $p$. On-policy refers to the fact that we use the selected policy $\pi$ once more to anticipate the next action $A_{t+1}$, given state $S_{t+1}$. This is precisely the difference to the off-policy algorithm presented in the next subsection.

## Page 245
A variant of SARSA is expected SARSA temporal difference learning which considers the update

$$
\widehat{q}\left(S_{t}, A_{t}\right) \leftarrow \widehat{q}\left(S_{t}, A_{t}\right)+\varrho_{t}\left(R_{t+1}+\gamma \sum_{a \in \mathcal{A}\left(S_{t+1}\right)} \pi\left(a \mid S_{t+1}\right) \widehat{q}\left(S_{t+1}, a\right)-\widehat{q}\left(S_{t}, A_{t} \mid \mathrm{d}\right)\right)
$$

That is, we do not simulate the next action $A_{t+1}$ for the update, but we replace it by an expected value. The following off-policy algorithm is similar in that it replaces the expected value (reflected by the sum) by an off-policy maximum operation, see (11.25), below.

# 11.7.2 $Q$-learning off-policy control 

Watkins [232] and Watkins-Dayan [233] introduced a significant simplification which allowed for first rigorous proofs. Namely, they considered the temporal difference update

$$
\widehat{q}\left(S_{t}, A_{t}\right) \leftarrow \widehat{q}\left(S_{t}, A_{t}\right)+\varrho_{t}\left(R_{t+1}+\gamma \max _{a \in \mathcal{A}\left(S_{t+1}\right)} \widehat{q}\left(S_{t+1}, a\right)-\widehat{q}\left(S_{t}, A_{t}\right)\right)
$$

This is called off-policy learning because it does not anticipate the next action $A_{t+1}$ w.r.t. selected policy $\pi$, given state $S_{t+1}$.

Algorithm $8 Q$-Learning temporal difference algorithm
(0) Select an initial action-value function $(\widehat{q}(s, a))_{s, a}$ with $\widehat{q}(\dagger, a) \equiv 0$; and $\gamma \in(0,1)$ and small $\varepsilon>0$.
(1) Iterate until a stopping rule is exercised:

- Choose initial state $S_{0} \in \mathcal{S}$ at random.
- Loop for $t \geq 0$ until the terminal value $\dagger$ for $S_{t}$ :
* For state $S_{t}$, sample $A_{t}$ from an $\varepsilon$-greedy policy of structure (11.19)(11.20).
* Given state-action pair $\left(S_{t}, A_{t}\right)$, observe reward $R_{t+1}$ and next state $S_{t+1}$.
* Update the action-value function with temporal difference (11.25) and use the state $S_{t+1}$ as input to the next step $t+1$.

The maximizations in Algorithm 8 can be critical as they may lead to biases. To mitigate such biases there are more advanced methods like double- $Q$-learning; for details see Sutton-Barto [212, Section 6.7].

Example 11.2. For our illustration, we select a small scale example with finite spaces $\mathcal{R}=\mathcal{S}=\mathcal{A}=\{1, \ldots, 10\}$ for the reward space, the state space and the action space, respectively. We select a continuing task MDP by specifying an environment's dynamics $p: \mathcal{S} \times \mathcal{R} \times \mathcal{S} \times \mathcal{A} \rightarrow(0,1)$, see (11.7). This probability tensor $p$ has $10^{4}=10,000$ entries that we select at random such that $p(\cdot, \cdot \mid s, a)$ sums to one for all state-action pairs $(s, a) \in \mathcal{S} \times \mathcal{A}$, and such that it does not have any symmetries. For the gain computation,

## Page 246
we select a discount factor of $\gamma=1 / 2$. Our goal is to find the optimal policy $\pi^{*}$ that maximizes the values $v_{\pi}(s)$ for all initial states $s \in \mathcal{S}$.
There exists a unique solution to this optimal control problem and we try to find it with reinforcement learning. We present the four methods: (1) policy iteration presented in Algorithm 4, (2) value iteration presented in Algorithm 5, (3) SARSA temporal difference learning of Algorithm 7, and (4) $Q$-learning temporal difference of Algorithm 8. The first two methods (1)-(2) are based on the knowledge of the true probability tensor $p$, methods (3)-(4) do not use the knowledge of this probability tensor $p$, but only observed actual experience, thus, the latter two methods present realistic learning problems. The SARSA algorithm (3) performs on-policy learning, and $Q$-learning (4) off-policy learning.

Figure 11.5: Algorithm convergence analysis: (lhs) policy iteration Algorithm 4 and (rhs) value iteration Algorithm 5; the $x$-axis shows the iterations $k \geq 0$ of the algorithms.

Figure 11.5 shows the developments of the value functions $v_{\pi_{k}}(s), s \in \mathcal{S}$, in the policy iteration algorithm, and the value functions $v_{k}(s), s \in \mathcal{S}$, in the value iteration algorithm for iterations $k \geq 0$. The policy iteration Algorithm 4 converges in two iterations to the optimal policy $\pi^{*}$, and the value iteration Algorithm 5 converges in roughly 20 iterations, see Figure 11.5. For the policy iteration algorithm we solve the linear system (11.14) in every step $k \geq 0$ of the algorithm, which can easily be done here because $B_{\pi_{k}}$ is a small matrix of size $10 \times 10$. For the value iteration algorithm we instead use a (single) Banach's fix point step in each iteration $k \geq 0$. For this small scale example, this results in a less efficient algorithm because the matrix inversion is very efficient in this small example. Table 11.1 shows the resulting optimal policy $\pi^{*}$ which is the same in both algorithms.

| state $s$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| policy iteration | 7 | 5 | 10 | 6 | 4 | 3 | 6 | 3 | 3 | 7 |
| value iteration | 7 | 5 | 10 | 6 | 4 | 3 | 6 | 3 | 3 | 7 |

Table 11.1: Optimal policy $\pi^{*}(s) \in \mathcal{A}$ for states $s \in \mathcal{S}$.

Under a known environment's dynamics $p$, we can easily find the optimal policy $\pi^{*}$, as
![Page 246 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p246_img1.jpg)

## Page 247
illustrated in Table 11.1. We now turn our attention to the more realistic situation of not knowing the environment's dynamics $p$. We therefore implement SARSA and $Q$-learning temporal difference to determine an optimal policy. Recall, this is done as follows. Based on state $S_{t}$, we exercise action $A_{t}$ according to our actual policy $\pi$ in place. Nature then gives us the reward $R_{t+1}$ and the next state $S_{t+1}$, based on the current state-action pair $\left(S_{t}, A_{t}\right)$. This allows us to perform actual experience learning.
We implement SARSA temporal difference learning as follows. We select an $\varepsilon$-greedy policy with $\varepsilon=1 \%$, and we run the (continuing) task for 3000 iterations $t \in\{0, \ldots, 3000\}$, that is, on average 30 times we explore, instead of exploiting the currently estimated optimal policy. This seems a low value. We apply this procedure 2000 times, which determines the outer loop in Algorithm 7. Finally, the learning rate $\varrho_{t}=\varrho_{t}\left(S_{t}, A_{t}\right)$ is chosen inversely proportional to the number of occurrences of the state-action pair $\left(S_{t}, A_{t}\right)$ up to and including time $t$; this corresponds to (11.3) extended to the state observation.

Figure 11.6: Algorithm convergence analysis: (lhs) SARSA temporal difference Algorithm 7 and (rhs) $Q$-learning temporal difference Algorithm 8.

Figure 11.6 (lhs) shows the convergence behavior of the on-policy SARSA temporal difference algorithm. The $x$-axis shows the time scale $t \in\{0, \ldots, 3000\}$, and the $y$-axis the action-value functions $\tilde{q}(s, a)$ for selected state-action pairs $(s, a)$. Each graph is averaged over the 2000 runs of the outer loop of Algorithm 7. We observe not full convergence yet, which indicates that we should run the continuing task for more time steps $t$. Based on these action-value estimates $\tilde{q}(s, a)$, we determine the estimated optimal policy $\tilde{\pi}^{*}(s)$, $s \in \mathcal{S}$. The result is given in Table 11.2.
From Table 11.2, we observe that SARSA finds almost perfectly the true optimal policy $\pi^{*}$ only in state $s=9$, we estimate the optimal action to be $a=\tilde{\pi}^{*}(9)=10$, instead of the true optimal action $\pi^{*}(9)=3$.
For the off-policy learning with $Q$-learning temporal difference we apply the same strategy and the same parameters as for SARSA. The convergence behavior is shown in Figure 11.6 (rhs) and the estimated optimal policy $\tilde{\pi}^{*}$ is given on the last line of Table 11.2. There is one misspecification with $Q$-learning which concerns state $s=7$, where we
![Page 247 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p247_img1.jpg)

## Page 248
| state $s$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| policy iteration | 7 | 5 | 10 | 6 | 4 | 3 | 6 | 3 | 3 | 7 |
| value iteration | 7 | 5 | 10 | 6 | 4 | 3 | 6 | 3 | 3 | 7 |
| SARSA temporal difference | 7 | 5 | 10 | 6 | 4 | 3 | 6 | 3 | 10 | 7 |
| $Q$-learning temporal difference | 7 | 5 | 10 | 6 | 4 | 3 | 2 | 3 | 3 | 7 |

Table 11.2: Estimated optimal policies $\widehat{\pi}^{*}(s) \in \mathcal{A}$ for states $s \in \mathcal{S}$.
exercise an action $a=2$ instead of the action $a=6$. This closes this example.
Remarks 11.3. We close this tabular learning exposition by some further methods.

- There are many variants that aim at improving both accuracy and speed of convergence. E.g., the temporal difference step (11.23) considers a one-step ahead prediction which can easily be replaced by a $n$-step ahead prediction

$$
\begin{aligned}
G_{t} & =R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{n-1} R_{t+n}+\gamma^{n} G_{t+n} \\
& \approx \sum_{s=1}^{n} \gamma^{s-1} R_{t+s}+\gamma^{n} \widehat{q}_{t+n-1}\left(S_{t+n}, A_{t+n}\right)=: \widehat{G}_{t: t+n}
\end{aligned}
$$

if $\widehat{q}_{k}$ denotes the estimate of the action-value function at time $k$. This motivates the $n$-step temporal difference update

$$
\widehat{q}_{t+n}\left(S_{t}, A_{t}\right) \leftarrow \widehat{q}_{t+n-1}\left(S_{t}, A_{t}\right)+\varrho_{t}\left(\widehat{G}_{t: t+n}-\widehat{q}_{t+n-1}\left(S_{t}, A_{t}\right)\right)
$$

see Sutton-Barto [212, formula (7.5)]. Integrating this into the SARSA temporal difference algorithm gives the $n$-step SARSA which approaches Monte Carlo estimation for $n \rightarrow \infty$.

- A second modification is to average over different returns $\widehat{G}_{t: t+n}$. Selecting $\lambda \in$ $[0,1)$, we can also approximate the gain $G_{t}$ by

$$
\widehat{G}_{t}^{\lambda}=(1-\lambda) \sum_{n \geq 1} \lambda^{n-1} \widehat{G}_{t: t+n}
$$

note that the weights aggregate to one. This gives the general temporal difference methods called $\operatorname{TD}(\lambda)$; see Sutton-Barto [212, Chapter 12]. For $\lambda=1$, this again reduces to Monte Carlo estimation.

# 11.8 Beyond tabular learning 

The previous methods of reinforcement learning have been considering tabular problems meaning that both the state space $\mathcal{S}$ and the action space $\mathcal{A}$ were finite. This, allows one to store everything in a (finite) table. Going over to continuous state spaces $\mathcal{S}$ lets the problem become more complicated. In that case, tabular estimates can be approximated by networks. The method of deep $Q$-network (DQN), introduced by Mnih et al. [159, 160],

## Page 249
is considered to be a breakthrough in reinforcement learning, see Sutton-Barto [212, Chapter 16].

Assume a general state space $\mathcal{S}$ and a finite action space $\mathcal{A}=\left\{a_{1}, \ldots, a_{m}\right\}$ with $m$ possible actions $\left(a_{j}\right)_{j=1}^{m}$. First, approximate the action-value function $q_{\pi}(s, a)$ of a given policy $\pi$ with a multi-output network $\left(q_{\vartheta}\left(s, a_{j}\right)\right)_{j=1}^{m}$, having one input $s \in \mathcal{S}$ and $m$ outputs, and with $\vartheta$ denoting the network parameter. That is, select a multi-output network

$$
q_{\vartheta}: \mathcal{S} \mapsto \mathbb{R}^{m}, \quad s \mapsto\left(q_{\vartheta}\left(s, a_{1}\right), \ldots, q_{\vartheta}\left(s, a_{m}\right)\right)^{\top}
$$

First, if one only operated on this multi-output network $q_{\vartheta}$, one would result in an unstable situation because in the optimizations the unknown network parameter $\vartheta$ appears on both sides of the equation. To improve the stability of the algorithm, Mnih et al. $[159,160]$ duplicated the network $q_{\vartheta}$ by a second network $q_{\vartheta_{\tau}}$, called target network, that has the same architecture and only differs in the network parameter $\vartheta_{\tau}$. Both networks are initialized by the same network parameter $\vartheta=\vartheta_{\tau}$, but the network parameter of the first network will be updated more frequently, resulting in a second network $q_{\vartheta_{\tau}}$ that is more inert. This bigger inertia stabilizes the updates of the action-value estimates $q_{\vartheta}$ because otherwise the estimated action-value estimates would use themselves (in a self-circular way), see (11.25). Therefore, we need this bigger inertia second network to receive meaningful results and to prevent from over-fitting.
Second, to not waste any (costly) observations, every quadruple ( $S_{t}, A_{t}, R_{t+1}, S_{t+1}$ ) is stored in a memory denoted by $\mathcal{M}$; this idea was introduced by Lin [137]. For gradient descent learning, we will (re-)sample random (mini-)batches from this memory $\mathcal{M}$ to learn the network parameter $\vartheta$. As a side effect, such random mini-batches break the temporal correlation in the experience which is an advantage in gradient descent learning. Note that this makes the following Algorithm 9 an off-policy algorithm.

The first part of the deep $Q$-network algorithm is similar to the $Q$-learning temporal difference algorithm, see Algorithm 8, and the two algorithms start to differ in the step where we use the memory $\mathcal{M}$. Using this memory, we sample a mini-batch of size $K$, and each of this samples is used to construct an approximative gain $\widehat{G}_{k}$ based on the second inert network $q_{\vartheta_{\tau}}$, this is motivated by (11.22). The approximative gains are then used to improve the network parameter $\vartheta$ of the first network in the next step, by optimally predicting the approximative gains $\left(\widehat{G}_{k}\right)_{k=1}^{K}$ by this first network $q_{\vartheta}$. Note that the multioutput network $q_{\vartheta}\left(S_{k}, A_{k}\right)$ has input $S_{k}$, and we select the output channel that coincides with the value of $A_{k}$. For the loss function $L$ one can use any strictly consistent loss function for mean estimation, however, in reinforcement learning practice, also robust versions of loss functions have been chosen. Finally, every $\tau \gg 1$ iterations, the inert network $q_{\vartheta_{\tau}}$ is updated, with either a soft update $\alpha \in(0,1)$ or a hard update $\alpha=1$.
The above algorithm is again prone to provide a biased estimate by taking the maximum in the $\widehat{G}_{k}$ estimate. The deep double- $Q$-network proposed by Hasselt et al. [91] tries to compensate for this by considering an estimated gain instead

$$
\widehat{G}_{k}= \begin{cases}R_{k+1} & \text { if } S_{k+1} \text { is terminal } \\ R_{k+1}+\gamma q_{\vartheta_{\tau}}\left(S_{k+1}, \underset{a \in \mathcal{A}\left(S_{k+1}\right)}{\arg \max } q_{\vartheta}\left(S_{k+1}, a\right)\right) & \text { otherwise }\end{cases}
$$

Version March 3, 2025, @AI Tools for Actuaries

## Page 250
# Algorithm 9 Deep $Q$-network algorithm 

(0) Select a random initial network parameter $\vartheta$ and initialize $\vartheta_{\tau}=\vartheta$. Choose $\alpha \in(0,1]$ and small $\varepsilon>0$. Initialize the memory $\mathcal{M}$, set the (mini-)batch size $K \in \mathbb{N}$ and select the step size $\tau \in \mathbb{N}$.
(1) Iterate until a stopping rule is exercised:

- Choose $S_{0} \in \mathcal{S}$ at random.
- Loop for $t \geq 0$ until terminal value $\dagger$ for $S_{t}$ :
* For state $S_{t}$, sample $A_{t}$ from an $\varepsilon$-greedy policy of structure (11.19)(11.20) under the actual network parameter $\vartheta$ for $q_{\vartheta}$.
* Given state-action pair $\left(S_{t}, A_{t}\right)$, observe reward $R_{t+1}$ and next state $S_{t+1}$.
* Store $\left(S_{t}, A_{t}, R_{t+1}, S_{t+1}\right)$ to the memory $\mathcal{M}$.
* Sample a mini-batch of size $K$ from the memory $\mathcal{M}$.
* Set training labels, for $1 \leq k \leq K$,

$$
\widehat{G}_{k}= \begin{cases}R_{k+1} & \text { if } S_{k+1} \text { is terminal } \\ R_{k+1}+\gamma \max _{a \in \mathcal{A}\left(S_{k+1}\right)} q_{\vartheta_{\tau}}\left(S_{k+1}, a\right) & \text { otherwise }\end{cases}
$$

* Update the network parameter

$$
\vartheta \leftarrow \underset{\vartheta}{\arg \min } \sum_{k=1}^{K} L\left(\widehat{G}_{k}, q_{\vartheta}\left(S_{k}, A_{k}\right)\right)
$$

* Every $\tau$ steps, update the second network parameter

$$
\vartheta_{\tau} \leftarrow \alpha \vartheta+(1-\alpha) \vartheta_{\tau}
$$

* Use state $S_{t+1}$ for the next step $t+1$.

## Page 251
That is, we replace a maximum by an estimated expected value.

# 11.9 Actor-critic reinforcement learning algorithms 

State-of-the-art reinforcement learning uses so-called actor-critic reinforcement learning algorithms. These work a bit differently compared to the algorithms presented above: Essentially, the above algorithms estimate the action-value function $q_{\pi}(s, a)$ from which the optimal policy and action is directly selected by an $\varepsilon$-greedy step (11.19)-(11.20).
Actor-critic reinforcement learning tries to directly estimate an optimal policy $\pi_{\vartheta^{*}}(a \mid s)$ from a parametrized family of policies $\left\{\pi_{\vartheta}(a \mid s)\right\}_{\vartheta}$. In the case of a finite action space $\mathcal{A}$, we can select the parametrized family as categorical distributions $\pi_{\vartheta}(\cdot \mid s)$ on $\mathcal{A}$, for all states $s \in \mathcal{S}$. For example, we can select a multi-output FNN $\boldsymbol{z}_{\vartheta}: \mathcal{S} \rightarrow \mathbb{R}^{|\mathcal{A}|}$, and applying the softmax function, we receive the corresponding probabilities

$$
\pi_{\vartheta}(a \mid s)=\frac{\exp \left\{\boldsymbol{z}_{\vartheta}(s)_{a}\right\}}{\sum_{a^{\prime} \in \mathcal{A}} \exp \left\{\boldsymbol{z}_{\vartheta}(s)_{a^{\prime}}\right\}}
$$

if $\boldsymbol{z}_{\vartheta}(s)_{a^{\prime}}$ denotes the component of $\boldsymbol{z}_{\vartheta}$ that corresponds to action $a^{\prime} \in \mathcal{A}$.
An actor-critic algorithm has two different modules:

- Actor. The actor is responsible for learning an optimal policy $\pi_{\vartheta}(a \mid s)$ by improving the parameter $\vartheta$ based on the feedback signal the actor receives.
- Critic. The critic evaluates the taken action and gives a feedback signal to the actor. The evaluation is often done with a value or/and an action-value function estimate. This value function is estimated/improved by the critic analyzing the resulting rewards of the taken actions.


### 11.9.1 Policy gradient control

Before we can discuss actor-critic algorithms, we need to introduce the policy gradient, assuming that $\vartheta$ is a real-valued vector and that all following terms are differentiable in $\vartheta$. Following Sutton-Barto [212, Section 13.2], we focus for the moment on episodic tasks which allow us to set $\gamma=1$, and we assume finite action and state spaces (the following results can be generalized). Under these assumptions we define the so-called performance, which is going to be the objective function, given by

$$
J(\vartheta)=v_{\pi_{\vartheta}}\left(s_{0}\right)=\mathbb{E}_{\pi_{\vartheta}}\left[\sum_{u=0}^{T} R_{u+1} \mid S_{0}=s_{0}\right]
$$

for a given policy $\pi_{\vartheta}$ and starting in state $s_{0} \in \mathcal{S}$. Using some algebra, we can reformulate the gradient of the performance $J(\vartheta)$ w.r.t. $\vartheta$ as follows

$$
\begin{aligned}
\nabla_{\vartheta} J(\vartheta) & \propto \mathbb{E}_{\pi_{\vartheta}}\left[\sum_{a \in \mathcal{A}} q_{\pi_{\vartheta}}\left(S_{t}, a\right) \nabla_{\vartheta} \pi_{\vartheta}\left(a \mid S_{t}\right) \mid S_{0}=s_{0}\right] \\
& =\mathbb{E}_{\pi_{\vartheta}}\left[q_{\pi_{\vartheta}}\left(S_{t}, A_{t}\right) \nabla_{\vartheta} \log \pi_{\vartheta}\left(A_{t} \mid S_{t}\right) \mid S_{0}=s_{0}\right] \\
& =\mathbb{E}_{\pi_{\vartheta}}\left[G_{t} \nabla_{\vartheta} \log \pi_{\vartheta}\left(A_{t} \mid S_{t}\right) \mid S_{0}=s_{0}\right]
\end{aligned}
$$

Version March 3, 2025, @AI Tools for Actuaries

## Page 252
see Sutton-Barto [212, Section 13.3]. There is a subtle issue hidden in this identity (11.26), namely, the time index $t$ seems undefined. In fact, in this identity $t$ should be a random variable such that $S_{t}$ has the same distribution as the relative frequency of the visits of the state-space sequence to the states in $\mathcal{S}$ under policy $\pi_{\vartheta}$ and starting in $S_{0}=s_{0}$. Thus, $S_{t}$ should have the long-term equilibrium distribution of the relative numbers of visits to the states under $\mathbb{P}_{\pi_{\vartheta}}\left[\cdot \mid S_{0}=s_{0}\right]$.

Algorithm 10 Monte Carlo policy gradient control
(0) Initialize $\vartheta$, and select $\gamma \in(0,1]$ and step size $\varrho>0$.
(1) Iterate until a stopping rule is exercised:

- Choose an initial state $S_{0} \in \mathcal{S}$ at random and observe an episode (11.16) for the present policy $\pi_{\vartheta}$ with finite termination time $T$.
- Loop for $t=0, \ldots, T-1$ :

$$
\begin{aligned}
& * G_{t} \leftarrow \sum_{k=t+1}^{T} \gamma^{k-(t+1)} R_{k+1} \\
& * \text { Policy update: } \vartheta \leftarrow \vartheta+\varrho \gamma^{t} G_{t} \nabla_{\vartheta} \log \pi_{\vartheta}\left(A_{t} \mid S_{t}\right)
\end{aligned}
$$

The policy update in Algorithm 10 is also called reinforce; see Sutton-Barto [212, Section 13.3]. This reinforce uses the so-called eligibility vector

$$
\nabla_{\vartheta} \log \pi_{\vartheta}\left(A_{t} \mid S_{t}\right)=\frac{1}{\pi_{\vartheta}\left(A_{t} \mid S_{t}\right)} \nabla_{\vartheta} \pi_{\vartheta}\left(A_{t} \mid S_{t}\right)
$$

which shows that the gradient ascent steps are composed by the optimal policy increase being reweighted with the corresponding occurrence frequencies of the conditional actions $A_{t}$, in states $S_{t}$, to not favor more frequent actions. Having $\gamma<1$ also allows us to use Algorithm 10 for continuing tasks.
The policy update in Algorithm 10 can be generalized by including a state-dependent baseline $b\left(S_{t}\right)$, being independent of $A_{t}$. This baseline will cancel in the gradient computations, and it will provide the reinforce with baseline policy update, see Sutton-Barto [212, Section 13.4],

$$
\vartheta \leftarrow \vartheta+\varrho \gamma^{t}\left(G_{t}-b\left(S_{t}\right)\right) \nabla_{\vartheta} \log \pi_{\vartheta}\left(A_{t} \mid S_{t}\right)
$$

The advantage of this baseline, if chosen smartly, is that it can significantly reduce the variance in the reinforcement learning algorithm. A typical, good selection is an estimate of the value function $b\left(S_{t}\right)=\widehat{v}_{\pi_{\vartheta}}\left(S_{t}\right)$. Such a choice can significantly improve the speed of convergence of the reinforcement learning algorithm; see, e.g., Sutton-Barto [212, Figure 13.2].

# 11.9.2 Actor-critic reinforcement learning 

The reinforce with baseline policy update from above comes already quite close to an actor-critic algorithm. The missing point is that the critic is not yet involved. The critic will not only estimate the value function $v_{\pi_{\vartheta}}(\cdot)$, based on this it will also give a

## Page 253
feedback signal to the actor. This implies a dependence along the time line which allows to improve the quality of the estimates (by bootstrapping). For illustration, we consider the one-step actor-critic algorithm of Sutton-Barto [212, Section 13.5]. It is the analogue to the one-step temporal difference algorithms from above such as the SARSA Algorithm 7 .
First, we select a second parametrized function class $\left\{v_{w}(s)\right\}_{w}$ being based on a realvalued vector $w$, and we assume that all considered terms are differentiable in $w$. We then modify the reinforce with baseline policy update by a one-step temporal difference update using the gain approximation (11.22) based on its expected version (11.24), and the baseline $b\left(S_{t}\right)=v_{w}\left(S_{t}\right)$

$$
\vartheta \leftarrow \vartheta+\varrho \gamma^{t}\left(R_{t+1}+\gamma v_{w}\left(S_{t+1}\right)-v_{w}\left(S_{t}\right)\right) \nabla_{\vartheta} \log \pi_{\vartheta}\left(A_{t} \mid S_{t}\right)
$$

Since this is (only) a one-step incremental update it can be done online, in contrast to the Monte Carlo policy gradient control Algorithm 10.
Secondly, we also need to describe the value function update by temporal difference. This can be achieved by a second gradient assent step

$$
w \leftarrow w+\varrho^{\prime}\left(R_{t+1}+\gamma v_{w}\left(S_{t+1}\right)-v_{w}\left(S_{t}\right)\right) \nabla_{w} v_{w}\left(S_{t}\right)
$$

for a second learning rate $\varrho^{\prime}>0$.
Algorithm 11 One-step actor-critic temporal difference algorithm
(0) Initialize $\vartheta$ and $w$, and select $\gamma \in(0,1]$ and step sizes $\varrho>0$ and $\varrho^{\prime}>0$.
(1) Iterate until a stopping rule is exercised:

- Choose an initial state $S_{0} \in \mathcal{S}$ at random.
- Loop for $t \geq 0$ until terminal value $\dagger$ for $S_{t}$ :
* For state $S_{t}$, sample $A_{t}$ from $\pi_{\vartheta}\left(\cdot \mid S_{t}\right)$.
* Given state-action pair $\left(S_{t}, A_{t}\right)$, observe reward $R_{t+1}$ and next state $S_{t+1}$.
* Update the value function with temporal difference (11.28).
* Update the policy with temporal difference (11.27), and use state $S_{t+1}$ as input to the next step $t+1$.

In both of these two temporal difference steps (11.27) and (11.28), we consider a so-called advantage function, which can have different forms depending on the specific algorithms used. In our case it is

$$
\delta_{t}=R_{t+1}+\gamma v_{w}\left(S_{t+1}\right)-v_{w}\left(S_{t}\right)
$$

This compares the result of action $A_{t}$, given by $R_{t+1}+\gamma v_{w}\left(S_{t+1}\right)$, to the (average) value that we would expect, given by $v_{w}\left(S_{t}\right)$. Thus, the direction of the improvements is multiplied by a step-size that adjusts for the advantage achieved by the corresponding action.
There are many notable variants of the actor-critic Algorithm 11; we refer to the vastly growing literature in this field. We would like to close this section by the proximal policy

## Page 254
optimization (PPO) introduced by Schulman et al. [203]. For this we first discuss trust region policy optimization (TRPO) of Schulman et al. [202]. Many of the policy gradient methods lack sufficient robustness, and TRPO is a method that tries to improve on that point. Let us come back to the temporal difference step (11.27)

$$
\vartheta \leftarrow \vartheta+\varrho \gamma^{t} \delta_{t} \nabla_{\vartheta} \log \pi_{\vartheta}\left(A_{t} \mid S_{t}\right)
$$

with advantage function $\delta_{t}$. This gradient ascent step can stem from a maximization problem

$$
\underset{\vartheta}{\arg \max }\left(\gamma^{t} \delta_{t} \log \pi_{\vartheta}\left(A_{t} \mid S_{t}\right)\right)
$$

TRPO now argues that having an old estimate $\vartheta_{\text {old }}$, the updated estimate $\vartheta$ should not be too different from this previous estimate. This motivates regularization, see Section 2.4 , and as penalty function we select the KL divergence of the resulting categorical distributions (we have assumed a finite action space $\mathcal{A}$ ); for the KL divergence see (9.44). Moreover, we replace $\log \pi_{\vartheta}$ by a ratio of new and old policy, providing a different normalization in the gradient $\nabla_{\vartheta}$. This motivates the KL regularized optimization

$$
\underset{\vartheta}{\arg \max }\left(\gamma^{t} \delta_{t} \frac{\pi_{\vartheta}\left(A_{t} \mid S_{t}\right)}{\pi_{\vartheta_{\text {old }}}\left(A_{t} \mid S_{t}\right)}-\eta D_{\mathrm{KL}}\left(\pi_{\vartheta}\left(\cdot \mid S_{t}\right) \| \pi_{\vartheta_{\text {old }}}\left(\cdot \mid S_{t}\right)\right)\right)
$$

with regularization parameter $\eta>0$. Since this TRPO is comparably complex and it does not allow, e.g., for drop-outs during fitting PPO proposes a simpler method with a comparable performance, see Schulman et al. [203]. The objective that is solved is given by

$$
\underset{\vartheta}{\arg \max } \min \left\{\gamma^{t} \delta_{t} \frac{\pi_{\vartheta}\left(A_{t} \mid S_{t}\right)}{\pi_{\vartheta_{\text {old }}}\left(A_{t} \mid S_{t}\right)}, \gamma^{t} \delta_{t} \min \left(\max \left(\frac{\pi_{\vartheta}\left(A_{t} \mid S_{t}\right)}{\pi_{\vartheta_{\text {old }}}\left(A_{t} \mid S_{t}\right)}, 1-\varepsilon\right), 1+\varepsilon\right)\right\}
$$

for a clipping hyper-parameter $\varepsilon \in(0,1)$. Thus, the probability ratio is censored (clipped) at $1-\varepsilon$ and $1+\varepsilon$. This removes the incentive of moving the probability ratio out of the interval $[1-\varepsilon, 1+\varepsilon]$. This objective function is plotted in Figure 11.7 as a function of the probability ratio $r=r(\vartheta)=\pi_{\vartheta}\left(A_{t} \mid S_{t}\right) / \pi_{\vartheta_{\text {old }}}\left(A_{t} \mid S_{t}\right)>0$. The resulting function depends on the sign of the advantage function $\delta_{t} \in \mathbb{R}$.

## Page 255
Figure 11.7: Objective function of PPO for $\varepsilon=1 / 2$ and with the probability ratios $r=r(\vartheta)=\pi_{\vartheta}\left(A_{t} \mid S_{t}\right) / \pi_{\vartheta_{\text {obl }}}\left(A_{t} \mid S_{t}\right)>0$ on the $x$-axis.
![Page 255 Image 1](20250303_ai_tools_for_actuaries_assets/20250303_ai_tools_for_actuaries_p255_img1.jpg)

## Page 256
Version March 3, 2025, @AI Tools for Actuaries

## Page 257
# Chapter 12 

## Outlook

The present version of these notes covers a large part of the AI tools that actuaries should be familiar with, but the reader may also have noticed that still some topics are missing, e.g., methods on interpretability, data visualization, variable importance, or a discussion about fairness and discrimination. We are going to provide more chapters that will cover these topics, and for an overview of possible further topics, we also refer to:
https://actuary.eu/about-the-aae/continuous-professional-development/

## Page 258
Version March 3, 2025, @AI Tools for Actuaries

## Page 259
# Bibliography 

[1] Abbas, A., Sutter, D., Zoufal, C., Lucchi, A., Figalli, A., Woerner, S. (2021). The power of quantum neural networks. Nature Computational Science 1, June 2021, 403-409.
[2] Akaike, H. (1974). A new look at the statistical model identification. IEEE Transactions on Automatic Control 19/6, 716-723.
[3] Andrès, H., Boumezoued, A., Jourdain, B. (2024). Signature-based validation of real-world economic scenarios. ASTIN Bulletin - The Journal of the IAA 54/2, 410-440.
[4] Arjovsky, M., Chintala, S., Bottou, L. (2017). Wasserstein GAN. Proceedings of the 34th International Conference on Machine Learning (ICML), 214-223.
[5] Arnold, V.I. (1957). On functions of three variables. Doklady Akademii Nauk SSSR 114/4, 679-681.
[6] Aronszajn, N. (1950). Theory of reproducing kernels. Transactions of the American Mathematical Society 68/3, 337-404.
[7] Avanzi, B., Taylor, G., Wang, M., Wong, B. (2024). Machine learning with high-cardinality categorical features in actuarial applications. ASTIN Bulletin - The Journal of the IAA 54/2, 213-238.
[8] Ayer, M., Brunk, H.D., Ewing, G.M., Reid, W.T., Silverman, E. (1955). An empirical distribution function for sampling with incomplete information. Annals of Mathematical Statistics 26, 641-647.
[9] Ba, J.L., Kiros, J.R., Hinton, G.E. (2016). Layer normalization. arXiv:1607.06450.
[10] Bai, Y., Jones, A., Ndousse, K., Askell, A., Leike, J., Amodei, D. (2022). Constitutional AI: Harmlessness from AI feedback. arXiv:2212.08073.
[11] Bailey, R.A., Simon, L.J. (1960). Two studies on automobile insurance ratemaking. ASTIN Bulletin - The Journal of the IAA 1, 192-217.
[12] Bar-Lev, S. K., Enis, P. (1986). Reproducibility and natural exponential families with power variance functions. The Annals of Statistics 14, 1507-1522.
[13] Bar-Lev, S.K., Kokonendji, C.C. (2017). On the mean value parametrization of the natural exponential kamily - a revisited review. Mathematical Methods of Statistics 26/3, 159-175.
[14] Barlow, R.E., Bartholomew, D.J., Bremmer, J.M., Brunk, H.D. (1972). Statistical Inference under Order Restrictions. John Wiley \& Sons.
[15] Barlow, R.E., Brunk, H.D. (1972). The isotonic regression problem and its dual. Journal of the American Statistical Association 67/337, 140-147.
[16] Barndorff-Nielsen, O. (2014). Information and Exponential Families: In Statistical Theory. John Wiley \& Sons.
[17] Beltagy, I., Peters, M.E., Cohan, A. (2020). Longformer: The long-document transformer. arXiv:2004.05150.

## Page 260
[18] Bender, E.M., Koller, A. (2020). Climbing towards NLU: On meaning, form, and understanding in the age of data. Proceedings of the Annual Meeting of the ACL.
[19] Bengio, S., Vinyals, O., Jaitly, N., Shazeer, N. (2015). Scheduled sampling for sequence prediction with recurrent neural networks. Advances in Neural Information Processing Systems 28, 1171-1179.
[20] Bengio Y., Courville A., Vincent P. (2013). Representation learning: a review and new perspectives. IEEE Transactions on Pattern Analysis and Machine Learning Intelligence $35 / 8,1798-1828$.
[21] Bengio Y., Ducharme R., Vincent P., Jauvin C. (2003). A neural probabilistic language model. Journal of Machine Learning Research 3/Feb, 1137-1155.
[22] Bengio, Y., Schwenk, H., Senécal, J.-S., Morin, F., Gauvain, J.-L. (2006). Neural probabilistic language models. In: Innovations in Machine Learning. Holmes, D.E., Jain, L.C. (Eds.). Springer, Studies in Fuzziness and Soft Computing 194, 137-186.
[23] Blæsild, P., Jensen, J.L. (1985). Saddlepoint formulas for reproductive exponential models. Scandinavian Journal of Statistics 12/3, 193-202.
[24] Bommasani, R., Hudson, D.A., Adeli, E., et al. (2021). On the opportunities and risks of foundation models. arXiv:2108.07258.
[25] Boureau, Y.L., Ponce, J., LeCun, Y. (2010). A theoretical analysis of feature pooling in vision recognition. In: Proceedings of the International Conference on Machine Learning ICML 65.
[26] Brauer, A. (2024). Enhancing actuarial non-life pricing models via transformers. European Actuarial Journal 14/3, 991-1012.
[27] Brébisson, de A., Simon, É., Auvolat, A., Vincent, P., Bengio, Y. (2015). Artificial neural networks applied to taxi destination prediction. arXiv:1508.00021.
[28] Breiman, L. (1996), Out-of-bag estimation. https://www.stat.berkeley.edu/ breiman/ OOBestimation.pdf
[29] Breiman, L. (1996). Bagging predictors. Machine Learning 24/2, 123-140.
[30] Breiman, L. (2001). Random forests. Machine Learning 45/1, 5-32.
[31] Breiman, L., Friedman, J.H., Olshen, R.A., Stone, C.J. (1984). Classification and Regression Trees. Wadsworth Statistics/Probability Series.
[32] Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J.D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. (2020). Language models are few-shot learners. Advances in Neural Information Processing Systems 33, 1877-1901.
[33] Brunk, H.D., Ewing, G.M., Utz, W.R. (1957). Minimizing integrals in certain classes of monotone functions. Pacific Journal of Mathematics 7, 833-847.
[34] Bühlmann, H. (1967). Experience rating and credibility. ASTIN Bulletin - The Journal of the IAA 4/3, 199-207.
[35] Bühlmann, H., Gisler, A. (2005). A Course in Credibility Theory and its Applications. Springer Universitext.
[36] Bühlmann, H., Straub, E. (1970). Glaubwürdigkeit für Schadensätze. Mitteilungen der Schweizerischen Vereinigung der Versicherungsmathematiker 1970, 111-131.

## Page 261
[37] Bühlmann, P. (2002). Consistency for $L_{2}$ boosting and matching pursuit with trees and treetype basis functions. In: Research Report/Seminar für Statistik, Eidgenössische Technische Hochschule (ETH), Vol. 109. Seminar für Statistik, Eidgenössische Technische Hochschule (ETH).
[38] Burges, C.J.C. (1998). Tutorial on support vector machines for pattern recognition. Data Mining and Knowledge Discovery 2, 121-167.
[39] Cao, Q., Sutton, C., Liska, A., Titov, I. (2021). Neuro-symbolic probing in neural language models. Proceedings of the Annual Meeting of the ACL.
[40] Chaubard, F., Mundra, R., Socher, R. (2016). Deep Learning for Natural Language Processing. Lecture Notes, Stanford University.
[41] Chen, T., Guestrin, C. (2016). XGBoost: a scalable tree boosting system. In: KDD '16: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785-794.
[42] Cho, K., van Merrienboer, B., Gulcehre, C., Bahdanau, D., Bougares, F., Schwenk, H., Bengio, Y. (2014). Learning phrase representations using RNN encoder-decoder for statistical machine translation. arXiv:1406.1078.
[43] Chowdhery, A., Narang, A., Devlin, J., et al. (2022). PaLM: Scaling language modeling with pathways. arXiv:2204.02311,.
[44] Christiano, P.F., Leike, J., Brown, T.B., Martic, M., Legg, S., Amodei, D. (2017). Deep reinforcement learning from human preferences. Advances in Neural Information Processing Systems 30, 4299-4307.
[45] Cortes, C., Vapnik, V. (1995). Support-vector networks. Machine Learning 20/3, 273-297.
[46] Cunningham, H., Ewart, A., Riggs, L., Huben, R., Sharkey, L. (2023). Sparse autoencoders find highly interpretable features in language models. arXiv:2309.08600.
[47] Cybenko, G. (1989). Approximation by superpositions of a sigmoidal function. Mathematics of Control, Signals and Systems 2, 303-314.
[48] DeepSeek Research Team (2025). DeepSeek R1: A family of open-source reasoning LLMs. arXiv:2501.12948.
[49] Delong, Ł, Kozak, A. (2023). The use of autoencoders for training neural networks with mixed categorical and numerical features. ASTIN Bulletin - The Journal of the IAA 53/2, $213-232$.
[50] Delong, Ł., Lindholm, M. and Zakrisson, H., (2023). On cyclic gradient boosting machines. SSRN Manuscript ID 4352505.
[51] Delong, Ł, Wüthrich, M.V. (2024). Isotonic regression for variance estimation and its role in mean estimation and model validation. North American Actuarial Journal, in press.
[52] Dempster, A.P., Laird, N.M., Rubin, D.B. (1977). Maximum likelihood for incomplete data via the EM algorithm. Journal of the Royal Statistical Society, Series B 39/1, 1-22.
[53] Denuit, M., Charpentier, A., Trufin, J. (2021). Autocalibration and Tweedie-dominance for insurance pricing in machine learning. Insurance: Mathematics and Economics 101/B, $485-497$.
[54] Denuit, M., Trufin, J. (2021). Lorenz curve, Gini coefficient, and Tweedie dominance for autocalibrated predictors. LIDAM Discussion Paper ISBA 2021/36.

## Page 262
[55] Devlin, J., Chang, M.-W., Lee, K., Toutanova, K. (2018). BERT: Pre-training of deep bidirectional Transformers for language understanding. arXiv:1810.04805.
[56] Dietterich, T.G. (2000) An experimental comparison of three methods for constructing ensembles of decision trees: bagging, boosting, and randomization. Machine Learning 40, $139-157$.
[57] Dietterich, T.G. (2000). Ensemble methods in machine learning. In: Multiple Classifier Systems, Kittel, J., Roli, F. (eds.). Lecture Notes in Computer Science 1857. Springer, $1-15$.
[58] Donaldson, J. (2016). $t$-distributed stochastic neighbor embedding for R (t-SNE). R package tsne.
[59] Duan, T., Anand, A., Ding, D.Y., Thai, K.K., Basu, S., Ng, A., Schuler, A., (2020). NGBoost: Natural gradient boosting for probabilistic prediction. In; International Conference on Machine Learning, Proceedings of Machine Learning Research, 2690-2700.
[60] Dutang, C., Charpentier, A., Gallic, E. (2024). Insurance dataset. Recherche Data Gouv. https://doi.org/10.57745/POKHAG
[61] Efron, B. (1979). Bootstrap methods: another look at the jackknife. Annals of Statistics $7 / 1,1-26$.
[62] Efron, B., Tibshirani, R.J. (1993). An Introduction to the Bootstrap. Chapman \& Hall.
[63] Embrechts, P., Klüppelberg, C., Mikosch, T. (2003). Modelling Extremal Events for Insurance and Finance. 4th printing. Springer.
[64] Ester, M., Kriegel, J.P., Sander, J., Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. In: Proceedings of the Second International Conference on Knowledge Discovery and Data Mining (KDD-96). AAAI Press. 226-231.
[65] Fahrmeir, L., Tutz, G. (1994). Multivariate Statistical Modelling Based on Generalized Linear Models. Springer.
[66] Fan, J., Li, R. (2001). Variable selection via nonconcave penalized likelihood and its oracle properties. Journal of the American Statistical Association 96/456 1348-1360.
[67] Ferrario, A., Hämmerli, R. (2019). On boosting: theory and applications. SSRN Manuscript ID 3402687 .
[68] Fisher, R.A. (1934). Two new properties of mathematical likelihood. Proceeding of the Royal Society A 144/852, 285-307.
[69] Fissler, T., Lorentzen, C., Mayer, M. (2022). Model comparison and calibration assessment: user guide for consistent scoring functions in machine learning and actuarial practice. arXiv:2202.12780.
[70] Friedman, J., H. (2001). Greedy function approximation: a gradient boosting machine. Annals of Statistics 25/5, 1189-1232.
[71] Fritschi, S., Guenther, F., Wright, M.N., Suling, M., Mueller, S.M. (2019). Training of neural networks. R package neuralnet.
[72] Gao, G., Wang, H., Wüthrich, M.V. (2022). Boosting Poisson regression models with telematics car driving data. Machine Learning 111/1, 243-272.
[73] Ghosh, P., Sajjadi, M.S.M., Vergari, A., Black, M., Schölkopf, B., (2020). From variational to deterministic autoencoders. International Conference on Learning Representations (ICLR).

## Page 263
[74] Gini, C. (1912). Variabilità e Mutabilità. Contributo allo Studio delle Distribuzioni e delle Relazioni Statistiche. C. Cuppini, Bologna.
[75] Gini, C. (1936). On the measure of concentration with special reference to income and statistics. Colorado College Publication, General Series No. 208, 73-79.
[76] Glorot, X., Bengio, Y. (2010). Understanding the difficulty of training deep feedforward neural networks. In: Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics, Proceedings of Machine Learning Research 9, 249-256.
[77] Gneiting, T. (2011). Making and evaluating point forecasts. Journal of the American Statistical Association 106/494, 746-762.
[78] Gneiting, T., Raftery, A.E. (2007). Strictly proper scoring rules, prediction, and estimation. Journal of the American Statistical Association 102/477, 359-378.
[79] Gneiting, T., Ranjan, R. (2013). Combining predictive distributions. Electronic Journal of Statistics 7, 1747-1782.
[80] Gneiting, T., Resin, J. (2023). Regression diagnostics meets forecst evaluation: conditional calibration, reliability diagrams, and coefficient of determination. Electronic Journal of Statistics 17, 3226-3286.
[81] Goldburd, M., Khare, A., Tevet, D., Guller, D. (2020). Generalized Linear Models for Insurance Rating. 2nd edition. CAS Monograph Series, 5.
[82] Golub, G., Van Loan, C. (1983). Matrix Computations. John Hopkins University Press.
[83] Goodfellow, I., Bengio, Y., Courville, A. (2016). Deep Learning. MIT Press, http://www. deeplearningbook.org
[84] Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., Bengio, Y. (2014). Generative adversarial nets. Advances in Neural Information Processing Systems 27.
[85] Gorishniy, Y., Kotelnikov, A., Babenko, A. (2024). TabM: advancing tabular deep learning with parameter-efficient ensembling. arXiv:2410.24210.
[86] Gorishniy, Y., Rubachev, I., Khrulkov, V., Babenko, A. (2021). Revisiting deep learning models for tabular data. In: Beygelzimer, A., Dauphin, Y., Liang, P., Wortman Vaughan, J. (eds). Advances in Neural Information Processing Systems, 34. Curran Associates, Inc., New York, 18932-18943.
[87] Gourieroux, C., Montfort, A., Trognon, A. (1984). Pseudo maximum likelihood methods: theory. Econometrica 52/3, 681-700.
[88] Guo, C., Berkhahn, F. (2016). Entity embeddings of categorical variables. arXiv:1604.06737.
[89] Guo, C., Pleiss, G., Sun, Y., Weinberger, K.Q. On calibration of modern neural networks. Proceedings of the 34th International Conference on Machine Learning (ICML), 1321-1330.
[90] Hainaut, D., Trufin, J., Denuit, M. (2022). Response versus gradient boosting trees, GLMs and neural networks under Tweedie loss and log-link. Scandinavian Actuarial Journal 2022/10, 841-866.
[91] Hasselt, van H., Guez, A., Silver, D. (2015). Deep reinforcement learning with double $Q$ learning. arXiv:1509.06461.
[92] Hastie, T., Tibshirani, R. (1993). Varying-coefficient models. Journal of the Royal Statistical Society Series B: Statistical Methodology 55/4, 757-779.

## Page 264
[93] Hastie, T., Tibshirani, R., Friedman, J. (2009). The Elements of Statistical Learning: Data Mining, Inference, and Prediction. 2nd edition. Springer Series in Statistics.
[94] Hastie, T., Tibshirani, R., Wainwright, M. (2015). Statistical Learning with Sparsity: The Lasso and Generalizations. CRC Press.
[95] Havrylenko, Y., Heger, J. (2024) Detection of interacting variables for generalized linear models via neural networks. European Actuarial Journal 14/2, 551-580.
[96] He, K., Zhang, X., Ren, S., Sun, J. (2015). Deep residual learning for image recognition. arXiv:1512.03385.
[97] Hinton, G.E., Salakhutdinov, R.R. (2006). Reducing the dimensionality of data with neural networks. Science 313/5786, 504-507.
[98] Hinton, G., Srivastava, N., Swersky, K. (2012). Neural Networks for Machine Learning. Lecture Slides. University of Toronto.
[99] Ho, J., Jain, A., Abbeel, P. (2020). Denoising diffusion probabilistic models. Advances in Neural Information Processing Systems 33, 6840-6851.
[100] Hochreiter, S., Schmidhuber, J. (1997). Long short-term memory. Neural Computation 9/8, $1735-1780$.
[101] Hofner, B., Mayr, A., Robinzonov, N., Schmid, M. (2014). Model-based boosting in R: A hands-on tutorial using the R ackage mboost. Computational Statistics 29, 3-35.
[102] Hornik, K. (1991). Approximation capabilities of multilayer feedforward networks. Neural Networks 4/2, 251-257.
[103] Hornik, K., Stinchcombe, M., White, H. (1989). Multilayer feedforward networks are universal approximators. Neural Networks 2/5, 359-366.
[104] Houlsby, N., Giurgiu, A., Jastrzebski, S., Morrone, B., de Laroussilhe, Q., Gesmundo, A., Attariyan, M., Gelly, S. (2019). Parameter-efficient transfer learning for NLP. Proceedings of the 36th International Conference on Machine Learning (ICML), 2790-2799.
[105] Hu, E.J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., Chen, W. (2022). LoRA: Low-rank adaptation of large language models. International Conference on Learning Representations (ICLR).
[106] Huang, X., Khetan, A., Cvitkovic, M., Karnin, Z. (2020). TabTransformer: Tabular data modeling using contextual embeddings. arXiv:2012.06678.
[107] Ioffe, S., Szegedy, C. (2015). Batch normalization: Accelerating deep network training by reducing internal covariate shift. In: Proceedings of the 32nd International Conference on Machine Learning 37, 448-456.
[108] Isenbeck, M., Rüschendorf, L. (1992). Completeness in location families. Probability and Mathematical Statistics 13/2, 321-343.
[109] James, G., Witten, D., Hastie, T., Tibshirani, R. (2015). An Introduction to Statistical Learning. With Applications in $R$. Corrected 6th printing. Springer.
[110] Jørgensen, B. (1986). Some properties of exponential dispersion models. Scandinavian Journal of Statistics 13/3, 187-197.
[111] Jørgensen, B. (1987). Exponential dispersion models. Journal of the Royal Statistical Society, Series B 49/2, 127-145.
[112] Jørgensen, B. (1997). The Theory of Dispersion Models. Chapman \& Hall.

## Page 265
[113] Kaplan, J., McCandlish, S., Henighanm, T., et al. (2020). Scaling laws for neural language models. arXiv:2001.08361.
[114] Karush, W. (1939). Minima of Functions of Several Variables with Inequalities as Side Constraints. MSc Thesis. Department of Mathematics, University of Chicago.
[115] Kaufman, L., Rousseeuw, P.J. (1990). Finding Groups in Data: An Introduction to Cluster Analysis. John Wiley \& Sons.
[116] Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., Liu, T.-Y. (2017). LightGBM: a highly efficient gradient boosting decision tree. Advances in Neural Information Processing Systems 30, 3146-3154.
[117] Khattab, O., Singhvi, A., Maheshwari, P., et al. (2023). Dspy: Compiling declarative language model calls into self-improving pipelines. arXiv:2310.03714.
[118] Kingma, D., Ba, J. (2014). Adam: A method for stochastic optimization. arXiv:1412.6980.
[119] Kingma, D.P, Welling, M. (2013). Auto-encoding variational Bayes. arXiv:1312.6114.
[120] Kingma, D.P., Welling, M. (2019). An introduction to variational autoencoders. Foundations and Trends in Machine Learning 12/4, 307-392.
[121] Kirsch, L., Wang, Y., Zhao, Y., Pickett, M. (2022). Meta-learning in-context transformers. arXiv:2209.07680.
[122] Kohonen, T. (1982). Self-organized formation of topologically correct feature maps. Biological Cybernetics 43, 59-69.
[123] Kohonen, T. (2001). Self-Organizing Maps. 3rd edition. Springer.
[124] Kohonen, T. (2013). Essentials of the self-organizing map. Neural Networks 37, 52-65.
[125] Kolmogorov, A. (1957). On the representation of continuous functions of many variables by superposition of continuous functions of one variable and addition. Doklady Akademii Nauk SSSR 114/5, 953-956.
[126] Kramer, M.A. (1991). Nonlinear principal component analysis using autoassociative neural networks. AIChE Journal 37/2, 233-243.
[127] Krüger, F., Ziegel, J.F. (2021). Generic conditions for forecast dominance. Journal of Business and Economics Statistics 39/4, 972-983.
[128] Kruskal, J.B. (1964). Nonmetric multidimensional scaling. Psychometrica 29, 115-129.
[129] Kuhn, H.W., Tucker, A.W. (1951). Nonlinear programming. In: Proceedings of 2nd Berkeley Symposium. University of California Press, 481-492.
[130] LeCun, Y., Bengio, Y. (1995). Convolutional networks for images, speech, and time series. The Handbook of Brain Theory and Neural Networks 3361/10.
[131] LeCun, Y., Bottou, L., Bengio, Y., Haffner, P. (1998). Gradient-based learning applied to document recognition. Proceedings of the IEEE 86/11, 2278-2324.
[132] Lee, R.D., Carter, L.R. (1992). Modeling and forecasting U.S. mortality. Journal of the American Statistical Association 87/419, 659-671.
[133] Leeuw, de J., Hornik, K., Mair, P. (2009). Isotone optimization in R: pool-adjacent-violators algorithm (PAVA) and active set methods. Journal of Statistical Software 32/5, 1-24.
[134] Leshno, M., Lin, V.Y., Pinkus, A., Schocken, S. (1993). Multilayer feedforward networks with a nonpolynomial activation function can approximate any function. Neural Networks $6 / 6,861-867$.

## Page 266
[135] Lewis, M., Liu, Y., Goyal, N., Ghazvininejad, M., Mohamed, A., Levy, O., Stoyanov, V., Zettlemoyer, L. (2020). BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension. Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 7871-7880.
[136] Li, X., Liang, P. (2021). Prefix-tuning: Optimizing continuous prompts for generation. Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics, $4582-4597$.
[137] Lin, L.-J. (1992). Self-improving reactive agents based on reinforcement learning, planning and teaching. Machine Learning 8/3-4, 293-321.
[138] Lindholm, M., Lindskog, F., Palmquist, J. (2023). Local bias adjustment, duration-weighted probabilities, and automatic construction of tariff cells. Scandinavian Actuarial Journal 2023/10, 946-973.
[139] Lindholm, M., Palmborg, L. (2022). Efficient use of data for LSTM mortality forecasting. European Actuarial Journal 12/2, 749-778.
[140] Lindholm, M., Wüthrich, M.V. (2024). The balance property in insurance pricing. SSRN Manuscript ID 4925165.
[141] Liu, Z., Wang, Y., Vaidya, S., Ruehle, F., Halverson, J., Soljačić, M., Hou, T.Y., Tegmark, M. (2024). KAN: Kolmogorov-Arnold networks. arXiv:2404.19756.
[142] Loader, C. (1999). Local Regression and Likelihood. Springer.
[143] Lorentzen, C., Mayer, M., Wüthrich, M.V. (2022). Gini index and friends. SSRN Manuscript ID 4248143 .
[144] Lorenz, M.O. (1905). Methods of measuring the concentration of wealth. Publications of the American Statistical Association 9/70, 209-219.
[145] Loshchilov, I., Hutter, F. (2017). Decoupled weight decay regularization. International Conference on Learning Representations (ICLR).
[146] Mack, T. (1993). Distribution-free calculation of the standard error of chain ladder reserve estimates. ASTIN Bulletin - The Journal of the IAA 23/2, 213-225.
[147] Makhzani, A., Frey, B. (2014). K-sparse autoencoders. International Conference on Learning Representations (ICLR).
[148] Mallat, S., Zhang, Z. (1993). Matching pursuits with time frequency dictionaries. IEEE Transactions on Signal Processing 41, 3397-3415.
[149] Mayr, A., Fenske, N., Hofner, B., Kneib, T., Schmid, M., (2012). Generalized additive models for location, scale and shape for high dimensional data - a flexible approach based on boosting. Journal of the Royal Statistical Society Series C: Applied Statistics 61/3, $403-427$.
[150] McCullagh, P., Nelder, J.A. (1983). Generalized Linear Models. Chapman \& Hall.
[151] McInnes, L., Healy, J., Melville, J. (2018). UMAP: uniform manifold approximation and projection for dimension reduction. arXiv:1802.03426v2.
[152] McLachlan, G.J., Krishnan, T. (2008). The EM Algorithm and Extensions. 2nd edition. John Wiley \& Sons.
[153] Menon, A.K., Jiang, X., Vembu, S., Elkan, C., Ohno-Machado, L. (2012). Predicting accurate probabilities with ranking loss. ICML'12: Proceedings of the 29th International Conference on Machine Learning, 659-666.

## Page 267
[154] Mercer, J. (1909), Functions of positive and negative type and their connection with the theory of integral equations. Philosophical Transactions of the Royal Society A 209/441458, 415-446.
[155] Micci-Barreca, D. (2001). A preprocessing scheme for high-cardinality categorical attributes in classification and prediction problems. ACM SIGKDD Explorations Newsletter 3/1, 2732 .
[156] Mikolov, T., Chen, K., Corrado, G.S., Dean, J. (2013). Efficient estimation of word representations in vector space. arXiv:1301.3781.
[157] Mikolov, T., Sutskever, I., Chen, K., Corrado, G.S., Dean, J. (2013). Distributed representations of words and phrases and their compositionality. Advances in Neural Information Processing Systems 26, 3111-3119.
[158] Miles, R.E. (1959). The complete amalgamation into blocks, by weighted means, of a finite set of real numbers. Biometrika 46, 317-327.
[159] Minh, V., Kavukcuoglu, K., Silver, D., Graves, A., Antonoglou, I., Wierstra, D., Riedmiller, M. (2013). Playing Atari with deep reinforcement learning. arXiv:1312.5602.
[160] Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A.A., Veness, J., Bellemare, M.G., Graves, A., Riedmiller, M., Fidjeland, A.K., Ostrovski, G., Petersen, S., Beattie, C., Antonoglou, I., King, H., Kumaran, D., Wierstra, D., Legg, S., Hassabis, D. (2015). Human-level control through deep reinforcement learning. Nature 518/7540, 529-533.
[161] Murphy, A.H. (1973). A new vector partition of the probability score. Journal of Applied Meteorology 12/4, 595-600.
[162] Murphy, K.P. (2024). Reinforcement learning: an overview. arXiv:2412.05265.
[163] Nanda, N., Lindner, J., Belrose, C., Olsson, C. (2023). Activation patching for mechanistic interpretability. Proceedings of the Mechanistic Interpretability Workshop.
[164] Nelder, J.A., Wedderburn, R.W.M. (1972). Generalized linear models. Journal of the Royal Statistical Society, Series A 135/3, 370-384.
[165] Nesterov, Y. (2007). Gradient methods for minimizing composite objective function. Technical Report 76. Center for Operations Research and Econometrics (CORE), Catholic University of Louvain.
[166] Nesterov, Y. (2018). Lectures on Convex Optimization. Springer.
[167] Nigri, A., Levantesi, S., Marino, M., Scognamiglio, S., Perla, F. (2019). A deep learning integrated Lee-Carter model. Risks 7/1, 33.
[168] NovaSky Team (2025). Sky-T1: Train your own O1 preview model within $\$ 450$. https: //novasky-ai.github.io/posts/sky-t1, Accessed: 2025-01-09.
[169] Odaibo, S. (2019). Tutorial: deriving the standard variational autoencoder (VAE) loss function. arXiv:1907.08956.
[170] Olah, C., Mordvintsev, A., Schubert, L. (2018). Feature visualization Distill. https:// distill.pub/2017/feature-visualization
[171] Olah, C., Satyanarayan, A., Johnson, I., Carter, S., Schubert, L., Ye, K., Mordvintsev, A. (2020). An overview of early vision in InceptionV1. Distill. https://distill.pub/2020/ circuits/early-vision
[172] Ouyang, L., Wu, J., Jiang, X., Almeida, D., Christiano, P., Leike, J., Amodei, D. (2022). Training language models to follow instructions with human feedback. arXiv:2203.02155.

## Page 268
[173] Palmborg, L, Lindskog, F. (2023). Premium control with reinforcement learning. ASTIN Bulletin - The Journal of the IAA 53/2, 233-257.
[174] Pan, J., Zhang, J., Wang, X., Yuan, L., Peng, H., Suhr, A. (2025). TinyZero. https: //github.com/Jiayi-Pan/TinyZero, accessed: 2025-01-24.
[175] Pennington, J., Socher, R., Manning, C.D. (2014). GloVe: global vectors for word representation. Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), 1532-1543.
[176] Perla, F., Richman, R., Scognamiglio, S., Wüthrich, M.V. (2024). Accurate and explainable mortality forecasting with the LocalGLMnet. Scandinavian Actuarial Journal 2024/7, 123 .
[177] Pohle, M.-O. (2020). The Murphy decomposition and the calibration-resolution principle: A new perspective on forecast evaluation. arXiv:2005.01835.
[178] Puterman, M.L. (2005). Markov Decision Processes: Discrete Stochastic Dynamic Programming. John Wiley \& Sons.
[179] R Core Team (2021). R: A language and environment for statistical computing. R Foundation for Statistical Computing, Vienna, Austria. http://www.R-project.org/.
[180] Radford, A., Narasimhan, K., Salimans, T., Sutskever, I. (2018). Improving language understanding by generative pre-training. OpenAI Technical Report.
[181] Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou, Y., Li, W., Liu, P.J. (2020). Exploring the limits of transfer learning with a unified text-to-text transformer. Journal of Machine Learning Research 21/140, 1-67.
[182] Raschka, S. (2025). Understanding reasoning LLMs: Methods and strategies for building and refining reasoning models. Blog Post, February 5, 2025.
[183] Rentzmann, S., Wüthrich, M.V. (2019). Unsupervised learning: What is a sports car? SSRN Manuscript ID 3439358.
[184] Rezende, D.J., Mohamed, S., Wierstra, D. (2014). Stochastic backpropagation and approximate inference in deep generative models. Proceedings of the 31st International Conference on Machine Learning, 1278-1286.
[185] Ribeiro, M.T., Singh, S., Guestrin, C. (2016). "Why should I trust you?": explaining the predictions of any classifier. In: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, KDD '16. New York: Association for Computing Machinery, 1135-1144.
[186] Richman, R. (2021). AI in actuarial science - a review of recent advances - part 1. Annals of Actuarial Science 15/2, 207-229.
[187] Richman, R. (2021). AI in actuarial science - a review of recent advances - part 2. Annals of Actuarial Science 15/2, 230-258.
[188] Richman, R., Scognamiglio, S., and Wüthrich, M. V. (2025). The credibility transformer. European Actuarial Journal, in press.
[189] Richman, R., Wüthrich, M.V. (2020). Nagging predictors. Risks 8/3, article 83.
[190] Richman, R., Wüthrich, M.V. (2023). LocalGLMnet: interpretable deep learning for tabular data. Scandinavian Actuarial Journal 2023/1, 71-95.
[191] Richman, R., Wüthrich, M.V. (2023). LASSO regularization within the LocalGLMnet architecture. Advances in Data Analysis and Classification 17/4, 951-981.

## Page 269
[192] Richman, R., Wüthrich, M.V. (2024). High-cardinality categorical covariates in network regressions. Japanese Journal of Statistics and Data Science 7/2, 921-965.
[193] Richman, R., Wüthrich, M.V. (2024). Smoothness and monotonicity constraints for neural networks using ICEnet Annals of Actuarial Science 18/3, 712-739.
[194] Ridgeway, G. (2024). Generalized boosted models: a guide to the gbm package. https: //cran.r-project.org/web/packages/gbm/vignettes/gbm.pdf
[195] Ronneberger, O., Fischer, P., Brox, T. (2015). U-Net: Convolutional networks for biomedical image segmentation. Medical Image Computing and Computer-Assisted Intervention (MICCAI), 234-241.
[196] Rumelhart, D.E., Hinton, G.E., Williams, R.J. (1986). Learning representations by backpropagating errors. Nature 323/6088, 533-536.
[197] Saerens, M. (2000). Building cost functions minimizing to some summary statistics. IEEE Transactions on Neural Networks 11, 1263-1271.
[198] Savage, L.J. (1971). Elicitable of personal probabilities and expectations. Journal of the American Statistical Association 66/336, 783-810.
[199] Schervish, M.J. (1989). A general method of comparing probability assessors. The Annals of Statistics 17/4, 1856-1879.
[200] Schölkopf, B., Smola, A., Müller, K.R. (1998). Nonlinear component analysis as a kernel eigenvalue problem. Neural Computation 10/5, 1299-1319.
[201] Schubert, E., Rousseeuw, P.J. (2019). Faster $k$-medoids clustering: improving the PAM, CLARA, and CLARANS algorithms. arXiv:1810.05691v3.
[202] Schulman, J., Levine, S., Moritz, P., Jordan, M.I., Abbbeel, P. (2015). Trust region policy optimization. arXiv:1502.05477.
[203] Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O. (2017). Proximal policy optimization algorithms. arXiv:170706347.
[204] Schwarz, G.E. (1978). Estimating the dimension of a model. Annals of Statistics 6/2, 461464 .
[205] Scognamiglio, S. (2022). Calibrating the Lee-Carter and the Poisson Lee-Carter models via neural networks. ASTIN Bulletin - The Journal of the IAA 52/2, 519-561.
[206] Semenovich, D., Dolman, C. (2020). What makes a good forecast? Lessons from meteorology. 20/20 All-Actuaries Virtual Summit, The Institute of Actuaries, Australia.
[207] Shmueli, G. (2010). To explain or to predict? Statistical Science 25/3, 289-310.
[208] Sohl-Dickstein, J., Weiss, E., Maheswaranathan, N., Ganguli, S. (2015). Deep unsupervised learning using nonequilibrium thermodynamics. Proceedings of the 32nd International Conference on Machine Learning, 2256-2265.
[209] Song, Y., Ermon, S. (2019). Generative modeling by estimating gradients of the data distribution. Advances in Neural Information Processing Systems 32.
[210] Srivastava, N., Hinton, G., Krizhevsky, A. Sutskever, I., Salakhutdinov, R. (2014). Dropout: a simple way to prevent neural networks from overfitting. Journal of Machine Learning Research 15/56, 1929-1958.
[211] Su, J., Lu, R., Huang, G., Liang, Y., Xia, F. (2021). RoFormer: Enhanced transformer with rotary position embedding. arXiv2104.09864.

## Page 270
[212] Sutton, R.S., Barto, A.G. (2018). Reinforcement Learning: An Introduction. MIT Press.
[213] Tasche, D. (2006). Validation of internal rating systems and PD estimates. arXiv:0606071.
[214] Tasche, D. (2021). Calibrating sufficiently. Statistics: A Journal of Theoretical and Applied Statistics 55/6, 1356-1386.
[215] Therneau, T.M., Atkinson, E.J. (2015). An introduction to recursive partitioning using the RPART routines. R Vignettes, version of June 29, 2015. Mayo Foundation, Rochester.
[216] Thomson, W. (1979). Eliciting production possibilities from a well-informed manager. Journal of Economic Theory 20, 360-380.
[217] Tibshirani, R. (1996). Regression shrinkage and selection via the LASSO. Journal of the Royal Statistical Society, Series B 58/1, 267-288.
[218] Tibshirani, R., Saunders, M., Rosset, S., Knight, K. (2005). Sparsity and smoothness via the fused LASSO. Journal of the Royal Statistical Society, Series B 67/1, 91-108.
[219] Tikhonov, A.N. (1943). On the stability of inverse problems. Doklady Akademii Nauk SSSR 39/5, 195-198.
[220] Tomczak, J.M. (2024). Deep Generative Modeling. Springer.
[221] Tsyplakov, A. (2013). Evaluation of probabilistic forecasts: proper scoring rules and moments. SSRN Manuscript ID 2236605.
[222] Tweedie, M.C.K. (1984). An index which distinguishes between some important exponential families. In: Statistics: Applications and New Directions. Ghosh, J.K., Roy, J. (Eds.). Proceeding of the Indian Statistical Golden Jubilee International Conference, Indian Statistical Institute, Calcutta, 579-604.
[223] van der Maaten, L.J.P., Hinton, G.E. (2008). Visualizing data using t-SNE. Journal of Machine Learning Research 9, 2579-2605.
[224] van der Merwe, M., Richman, R. (2024). Responsible AI: The role of actuaries in bridging the trust deficit. Presented at the ASSA 2024 Convention in Cape Town.
[225] Vapnik, V.N. (1997). The support vector method. In: Artificial Neural Networks ICANN'97, Gerstner, W., Germond, A., Hasler, M., Nicoud, J.-D. (eds.). Lecture Notes in Computer Science. Vol. 1327. Springer.
[226] Vapnik, V.N., Chervonenkis, A.Y. (1964). On a class of perceptrons. Avtomatika i Telemekhanika 25/1.
[227] Vapnik, V.N., Chervonenkis, A.Y. (1964). On a class of algorithms of learning pattern recognition. Avtomatika i Telemekhanika 25/6.
[228] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł., Polosukhin, I. (2017). Attention is all you need. arXiv:1706.03762v5.
[229] Wager, S., Wang, S., Liang, P.S. (2013). Dropout training as adaptive regularization. In: Advances in Neural Information Processing Systems 26. Burges, C., Bottou, L., Welling, M., Ghahramani, Z., Weinberger, K. (Eds.). Curran Associates, 351-359.
[230] Wald, A. (1949). Note on the consistency of the maximum likelihood estimate. Annals of Mathematical Statistics 20/4, 595-601.
[231] Wang, C.W., Zhang, J., Zhu, W. (2021). Neighbouring prediction for mortality. ASTIN Bulletin: The Journal of the IAA 51/3, 689-718.

## Page 271
[232] Watkins, C.J.C.H. (1989). Learning from Delayed Rewards. PhD Thesis, University of Cambridge.
[233] Watkins, C.J.C.H., Dayan, P. (1992). Q-learning. Machine Learning 8/3-4, 279-292.
[234] Wei J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. arXiv:2201.11903.
[235] Werbos, P.J. (1988). Generalization of backpropagation with application to a recurrent gas market model. Neural Networks 1/4, 339-356.
[236] Williams, R.J., Zipser, D. (1989). A learning algorithm for continually running fully recurrent neural networks. Neural Computation 1/2, 270-280.
[237] Wu, C.F.J. (1983). On the convergence properties of the EM algorithm. The Annals of Statistics 11/1, 95-103.
[238] Wüthrich, M.V. (2020). Bias regularization in neural network models for general insurance pricing. European Actuarial Journal 10/1, 179-202.
[239] Wüthrich, M.V. (2023). Model selection with Gini indices under auto-calibration. European Actuarial Journal 13/1, 71-95.
[240] Wüthrich, M.V. (2025). Auto-calibration tests for discrete finite regression functions. European Actuarial Journal, in press.
[241] Wüthrich, M.V., Buser, C. (2016). Data Analytics for Non-Life Insurance Pricing. SSRN Manuscript ID 2870308, Version of June 19, 2023.
[242] Wüthrich, M.V., Merz, M. (2019). Editorial: Yes, we CANN! ASTIN Bulletin - The Journal of the IAA 49/1, 1-3.
[243] Wüthrich, M.V., Merz, M. (2023). Statistical Foundations of Actuarial Learning and its Applications. Springer Actuarial. https://link.springer.com/book/10.1007/ $978-3-031-12409-9$
[244] Wüthrich, M.V., Ziegel, J. (2024). Isotonic recalibration under a low signal-to-noise ratio. Scandinavian Actuarial Journal 2024/3, 279-299.
[245] Xie, S.M., Yala, L., Liu, Q. (2021). An explanation of in-context learning as implicit Bayesian inference. arXiv:2110.08387.
[246] Yuan, X.T., Lin, Y. (2007). Model selection and estimation in regression with grouped variables. Journal of the Royal Statistical Society, Series B 68/1, 49-67.
[247] Zakrisson, H., Lindholm, M. (2025). A tree-based varying coefficient model. Computational Statistics, in press.
[248] Zhang, T., Yu, B. (2005). Boosting with early stopping: Convergence and consistency The Annals of Statistics 33/4, 1538-1579.
[249] Zhou, Y., Hooker, G. (2022). Decision tree boosted varying coefficient models. Data Mining and Knowledge Discovery 36/6, 2237-2271.
[250] Zou, H., Hastie, T. (2005). Regularization and variable selection via the elastic net. Journal of the Royal Statistical Society, Series B 67/2, 301-320.