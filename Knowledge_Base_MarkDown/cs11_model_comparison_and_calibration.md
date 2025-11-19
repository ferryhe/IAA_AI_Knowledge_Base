_Note: Source document was split into 5 OCR chunks (pages 1-16, pages 17-32, pages 33-46, pages 47-59, pages 60-70) to stay within token limits._

# CS11 Model Comparison and Calibration

## Page 1
# Model Comparison and Calibration Assessment 

## User Guide for Consistent Scoring Functions in Machine Learning and Actuarial Practice

Tobias Fissler* Christian Lorentzen ${ }^{\dagger} \quad$ Michael Mayer ${ }^{\dagger}$<br>tobias.fissler@wu.ac.at christian.lorentzen@mobiliar.ch michael.mayer@mobiliar.ch

Prepared for:<br>Working Group "Data Science"<br>Swiss Association of Actuaries SAV<br>Version of July 27, 2023


#### Abstract

One of the main tasks of actuaries and data scientists is to build good predictive models for certain phenomena such as the claim size or the number of claims in insurance. These models ideally exploit given feature information to enhance the accuracy of prediction. This user guide revisits and clarifies statistical techniques to assess the calibration or adequacy of a model on the one hand, and to compare and rank different models on the other hand. In doing so, it emphasises the importance of specifying the prediction target functional at hand a priori (e.g. the mean or a quantile) and of choosing the scoring function in model comparison in line with this target functional. Guidance for the practical choice of the scoring function is provided. Striving to bridge the gap between science and daily practice in application, it focuses mainly on the pedagogical presentation of existing results and of best practice. The results are accompanied and illustrated by two real data case studies on workers' compensation and customer churn.


keywords: actuarial science, backtesting, calibration, classification, consistency, data science, identification functions, machine learning, model comparison, predictive performance, propriety, scoring functions, scoring rules, supervised learning

[^0]
[^0]:    * Institute for Statistics and Mathematics, Vienna University of Economics and Business (WU), Welthandelsplatz 1, 1020 Vienna, Austria
    1 la Mobilière, Bern, Switzerland

## Page 2
# Contents 

1. Introduction ..... 3
2. Supervised Learning ..... 6
2.1. Theory ..... 6
2.2. Example ..... 8
3. Statistical Learning Theory ..... 10
3.1. Theory ..... 10
3.2. Practicalities ..... 13
3.3. Example ..... 16
4. Calibration and Identification Functions ..... 18
4.1. Theory ..... 18
4.2. Practicalities ..... 22
4.3. Example ..... 23
5. Model Comparison and Selection with Consistent Scoring Functions ..... 30
5.1. Theory ..... 30
5.2. Practicalities ..... 38
5.3. Example ..... 40
6. Probabilistic Binary Classification ..... 45
6.1. Theory ..... 45
6.2. Practicalities ..... 47
6.3. Example ..... 50
7. Conclusion ..... 54
A. Exploratory Data Analysis ..... 61
A.1. Regression: Workers' Compensation Data Set ..... 61
A.2. Classification: Telco Customer Churn Data Set ..... 64
B. Tweedie Deviance and Homogeneous Bregman Functions ..... 66
C. Simulation study on efficiency ..... 67

## Page 3
# 1. Introduction 

This study has been carried out for the working group "Data Science" of the Swiss Association of Actuaries SAV, see
https://www.actuarialdatascience.org
The purpose of this user guide is to provide an overview of point forecast evaluation, theory and examples hand in hand. For better readability and distinction of theory and example sections, we mark them as follows:

## Theory 1 Practicalities Example

Nowadays, validating and comparing the predictive performance of statistical models has become ubiquitous by means like cross-validation, testing on a hold-out data set and machine learning (ML) competitions. In the light of these developments, this article strives to provide the methodology to answer two key questions:

1. Given a model, does it produce calibrated predictions?
2. Given two models, which model produces more accurate predictions?

In finance, these two tasks are customarily subsumed under the umbrella term backtesting. Intuitively, calibration means that the predictions produced by a model are in line with the observations of the response variable. It is a generalisation of unbiasedness, sometimes referred to as balance property in actuarial science. Calibration can be checked by means of identification functions, also known as moment functions. For the latter quest, predictive accuracy is commonly assessed in terms of loss or scoring functions, sometimes also called metrics. Roughly speaking, they measure the distance between a prediction and the observation of the quantity of interest. Crucially, for both tasks, the evaluation methodology should be "designed such that truth telling [...] is an optimal strategy in expectation" [29]. But what does truth amount to in this setting? In the most general and informative form, it is the true (conditional) probability distribution of the response (given the information contained in the features), called probabilistic prediction [27]. Alternatively, when the model outputs point predictions, it is a pre-specified summary measure, a property, or a functional of the true (conditional) probability distribution of the response, such as the (conditional) mean or a (conditional) quantile. For the situation of point predictions, the identification and scoring functions used must be chosen to fit to the target functional, i.e. they need to be strictly consistent. Interestingly, strictly consistent scoring functions then simultaneously assess calibration and discrimination ability of the model predictions.

In this user guide, we summarise the theoretical background and give illustrative examples. As a shortcut, just follow Figure 1 and Theory Short Form.

## Page 4
# Theory Short Form 

## Summary: Theory

- Mind your statistical assumption: Response $Y$ given feature information $\boldsymbol{X}$ is a random variable. Thus, $Y$ cannot be described as a deterministic function of $\boldsymbol{X}$.
- Decide if and how to summarise the uncertainty of $Y$ given $\boldsymbol{X}$, depending on your (business) goal.
- Not summarising leads to probabilistic predictions where the ideal prediction is the conditional distribution of $Y$ given $\boldsymbol{X}, F_{Y \mid \boldsymbol{X}}$.
- Summarising with a statistical functional $T$ leads to point predictions. The ideal prediction is given in terms of the conditional functional $T(Y \mid \boldsymbol{X})$, e.g., the conditional expectation $\mathbb{E}[Y \mid \boldsymbol{X}]$.
- Check whether $T$ is identifiable and elicitable.
- Use a strict identification function for $T$ to assess the calibration of a model.
- Choose a strictly consistent scoring function for $T$ in order to compare predictions of different models on a test data set that is independent of the training data.

Outline The present user guide starts with a short overview of supervised learning in Section 2 at the end of which a data set for a regression modelling example is introduced. Section 3 continues with the core of supervised learning: loss functions and the statistical risk. It introduces the concept of overfitting and the necessity of a train-test split for model comparison. In the example part, several models are trained, among them generalised linear models and gradient boosted trees. How to assess model calibration is then presented in Section 4. It defines identification functions and different notions of calibration which are then assessed and visualised in detail. The following Section 5 lays out the theory of scoring functions, which is an alternative name for loss functions. ${ }^{1}$ A central property of scoring functions is (strict) consistency, and general forms of consistent scoring functions for the most common target functionals are provided. Furthermore, it is shown that scoring functions simultaneously assess calibration and potential discriminative power of a given model. After practical considerations on how to choose a particular scoring function, the example part illustrates model comparison and concludes which model performs best on the given data set. Section 6 sheds light

[^0]
[^0]:    1 Conventions in the literature are different and sometimes loss functions are required to be nonnegative. We do not impose this condition. Our convention is to speak of loss functions in the context of learning and of scoring functions in the context of evaluation.

## Page 5
What is your ultimate (business) goal?

What is your response $Y$ ?

What input features / covariates $\boldsymbol{X}$ do you want to use?

What property (functional) of the distribution of $Y$ given $\boldsymbol{X}$ do you want to model?

Choose a strictly consistent scoring function and a strict identification function for this property.

Specify a class of suitable models.

Fit/Estimate models on a training set.

Check the calibration of your models with the identification function evaluated on an independent test set.

Compare your models with the scoring function evaluated on an independent test set.
Figure 1: Modeling decision graph

## Page 6
on the peculiarities of probabilistic binary classification and demonstrates them on a classification data set. Finally, the user guide concludes with Section 7.

Configuration All R code was run on the following system.

- Processor: Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz, 2112 Mhz, 4 Core(s)
- R version: 4.0.4

The complete R code can be found at https://github.com/JSchelldorfer/Actuari alDataScience. Note: Since version 3.6.0, R uses a different random number generator. Results are not reproducible under older versions.

# 2. Supervised Learning 

### 2.1. Theory

According to Wikipedia ${ }^{2}$ "supervised learning is the machine learning task of learning a function that maps an input to an output based on example input-output pairs." [67] Using standard notation, we call the input features, also called covariates, regressors or explanatory variables, $\boldsymbol{X}$, taking values in some possibly high dimensional feature space $\mathcal{X}$ such as $\mathbb{R}^{K}$, and the output $Y$, which is the response or target variable, and which takes values in some space $\mathcal{Y}$, which we assume to be a subset of $\mathbb{R}$. Observations of input-output pairs are denoted by $\left(\boldsymbol{x}_{i}, y_{i}\right), i=1, \ldots, n$. The presence of the observable outputs is the reason for the term supervised. In statistical learning theory, we consider both $\boldsymbol{X}$ and $Y$ to be random variables with joint probability distribution $F_{\boldsymbol{X}, Y}$. To ease the exposition, we dispense with a discussion of a time series framework and solely focus on cross-sectional data. That is, we assume that each sample of data is a random sample, meaning the data at hand $\left(\boldsymbol{x}_{i}, y_{i}\right), i=1, \ldots, n$, is independent and identically distributed (i.i.d.). ${ }^{3}$

The first key point we would like to stress is: It is in general illusive to hope that the input features $\boldsymbol{X}$ can fully explain the behaviour of $Y$ in that $Y$ is a deterministic function $g$ of the features, $Y=g(\boldsymbol{X})$. There is a remaining degree of uncertainty, which can be expressed in terms of the conditional distribution of $Y$, given $\boldsymbol{X}$, denoted by $F_{Y \mid \boldsymbol{X}}$. The most informative prediction approach is probabilistic, aiming at specifying the full conditional distribution $F_{Y \mid \boldsymbol{X}}$. Often, one is content with point predictions, ${ }^{4}$ modelling only a certain property or summary measure of the conditional distribution. Strictly speaking, such a summary measure is a statistical functional, mapping a distribution to a real number, such as the mean or a quantile. Then the ideal point prediction

[^0]
[^0]:    2 https://en.wikipedia.org/wiki/Supervised_learning as of 06.01.2021.
    3 It is also possible to allow for serial dependence and some non-stationarity in the data. However, this would dilute the main message of the paper and distract from our main goals.
    4 In this tutorial, we will use the terms "prediction" and "forecast" interchangeably, possibly ignoring the temporal connotation of the latter.

## Page 7
takes the form $T\left(F_{Y \mid \boldsymbol{X}}\right)$, which we will denote by $T(Y \mid \boldsymbol{X})$ for convenience. If $T$ is the mean functional, we obtain $T(Y \mid \boldsymbol{X})=\mathbb{E}[Y \mid \boldsymbol{X}]$, or if $T$ is the $\alpha$-quantile, we get $T(Y \mid \boldsymbol{X})=q_{\alpha}(Y \mid \boldsymbol{X})=\inf \left\{t \in \mathbb{R} \mid F_{Y \mid \boldsymbol{X}}(t) \geq \alpha\right\}$. It is also possible to combine different functionals to a vector, e.g., when interested in two quantiles at different levels or in the mean and variance of $Y$ given $X$. For the sake of simplicity, we will mostly stick to one dimensional functionals in this article, though.

The ideal goal of supervised learning is then to find a model $m: \mathcal{X} \rightarrow \mathbb{R}$ which approximates the actual underlying regression function $\mathcal{X} \ni \boldsymbol{x} \mapsto T(Y \mid \boldsymbol{X}=\boldsymbol{x})$. Since the search space of all (measurable) functions $\mathcal{X} \rightarrow \mathbb{R}$ is clearly not tractable, one needs to come up with a suitable model class $\mathcal{M}$ of such functions. For our purpose, we will require that $\mathcal{M}$ contains models of different complexity (also called model capacity) and always contains the trivial model, i.e. constant model (also called null model or intercept model). While the model complexity can theoretically be defined by the Vapnik-Chervonenkis dimension or the Rademacher complexity, cf. [70, 52, 3] and references therein, we give some vivid examples:

- Most classically, for the class of linear models, complexity can be measured by the number of estimable parameters, also known as degrees of freedom (df). This amounts to including and excluding features as well as adding interaction terms and quadratic and higher order polynomial terms such as splines.
- For penalised linear models (with fixed input features), such as ridge or lasso regression, the penalty parameter is a-reciprocal-measure of complexity.
- Non-parametric approaches often impose smoothness or shape constraints on the models, with the most prominent case of isotonic models. ${ }^{5}$ Then the degree of smoothness, for example, can be taken as a measure of complexity.
- For decision trees, it can be the number of leaves or the maximal tree depth.
- For ensemble models like gradient boosted trees, it can be a combination of the single tree complexity and the number of fitted trees.
- For neural nets, where the model class $\mathcal{M}$ is implicitly given by the architecture of the net, it can be the combination of the number of weights, early stopping and weight penalisation.

Using a training data sample $\left(\boldsymbol{x}_{i}, y_{i}\right), i=1, \ldots, n$, one then fits (or trains or estimates) a model $\widehat{m} \in \mathcal{M}$. The fitted model commonly has two purposes: On the one hand, it should be interpretable, describing the connection of $Y$ and $\boldsymbol{X}$ in terms of $T$ (which is often easier if $\mathcal{M}$ is small, e.g., for linear models). On the other hand, $\widehat{m}$ should produce predictions which should be as accurate as possible. That is, when using a new feature point $\boldsymbol{x}_{\text {new }}$ (not necessarily contained in the training sample), $\widehat{m}\left(\boldsymbol{x}_{\text {new }}\right)$ should be close to the ideal $T\left(Y \mid \boldsymbol{X}=\boldsymbol{x}_{\text {new }}\right)$.

[^0]
[^0]:    5 There is some (partial) order $\preceq$ on $\mathcal{X}$ and $x_{1} \preceq x_{2}$ implies that $m\left(x_{1}\right) \leq m\left(x_{2}\right)$.

## Page 8
# A 2.2. Example: Mean Regression for Workers' Compensation. 

Throughout this user guide, we illustrate the theoretical results on the Workers' Compensation data set, ${ }^{6}$ which consists of $n=100000$ rows, each representing a single insurance claim caused by injury or death from accidents or occupational disease while a worker is on the job. Due to possible data inconsistencies, we filter out all rows with WeeklyPay $<200$ and HoursWorkedPerWeek $<20$. This leaves us with $n=82017$ rows, see Listing 1.

Listing 1: Common data preprocessing for regression example

```
library(tidyverse)
library(lubridate)
library(OpenML)
df_origin <- getOMLDataSet(data.id = 42876L)
df <- tibble(df_origin$data)
df <- df %>%
    filter(WeeklyPay >= 200,
        HoursWorkedPerWeek >= 20) %>%
    mutate(
        DateTimeOfAccident = ymd_hms(DateTimeOfAccident),
        DateOfAccident = as_date(DateTimeOfAccident),
        DateReported = ymd(DateReported),
        LogDelay = loglp(as.numeric(DateReported - DateOfAccident)),
        HourOfAccident = hour(DateTimeOfAccident),
        WeekDayOfAccident = factor(wday(DateOfAccident, week_start = 1)),
        LogWeeklyPay = loglp(WeeklyPay),
        LogInitial = log(InitialCaseEstimate),
        DependentChildren = pmin(4, DependentChildren),
        HoursWorkedPerWeek = pmin(60, HoursWorkedPerWeek),) %>%
    mutate_at(c("Gender", "MaritalStatus", "PartTimeFullTime"), as.factor) %>%
    rename(HoursPerWeek = HoursWorkedPerWeek)
x_continuous <- c("Age", "LogWeeklyPay", "LogInitial", "HourOfAccident",
            "HoursPerWeek", "LogDelay")
x_discrete <- c("Gender", "MaritalStatus", "PartTimeFullTime",
            "DependentChildren",
            "DaysWorkedPerWeek", "WeekDayOfAccident")
x_vars <- c(x_continuous, x_discrete)
y_var <- "UltimateIncurredClaimCost"
```

The response variable is $Y=$ UltimateIncurredClaimCost with explanatory features $\boldsymbol{X}$ represented by the remaining columns listed in x_vars. As a summary measure $T$, we choose to model the conditional expectation of $Y$ given $\boldsymbol{X}$. It is the most common target functional in machine learning. In actuarial science, it informs about adequate pricing of policies. Moreover, the tower property of the conditional expectation ${ }^{7}$ facilitates to compute an estimate of the unconditional expectation of $Y$ as $\frac{1}{n} \sum_{i=1}^{n} m\left(\boldsymbol{X}_{i}\right)$ for claims (or policies) $i=1, \ldots, n$, i.e. the expected value for a whole portfolio of claims (or policies).

[^0]
[^0]:    6 https://www.openml.org/d/42876
    7 That is, $\mathbb{E}[\mathbb{E}[Y \mid X]]=\mathbb{E}[Y]$.

## Page 9
Figure 2: Histogram of response UltimateIncurredClaimCost on a logarithmic scale.

Listing 2 shows the first ten rows of the data.

Listing 2: Output of command print(df)

In Figure 2, the empirical, marginal distribution of $Y$ is visualised. As the large difference between mean and median indicates, the distribution seems to be very asymmetric, right-skewed, even heavy tailed. (Mind the logarithmic scale of the $x$-axis.) For further exploratory data analysis, we refer to Subsection A.1.
![Page 9 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p09_img1.jpg)
![Page 9 Image 2](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p09_img2.jpg)

## Page 10
# 3. Statistical Learning Theory 

### 3.1. Theory

To provide a complete picture, we shortly outline the basics of statistical learning theory. This will explain the difference between model estimation on the one hand and model validation and selection on the other hand. We start by introducing a loss function $L(z, y) \in \mathbb{R}, z, y \in \mathbb{R}$, that measures the accuracy of predictions $z=m(\boldsymbol{x})$ from a model $m \in \mathcal{M}$ for observations of the response $y$-with the convention the smaller the better. The leading example is the squared error, $L(z, y)=(z-y)^{2}$. The loss function should be chosen in line with the directive $T$ in that it should be (strictly) consistent for $T$; see Definition 4 in Section 5. For a model $m \in \mathcal{M}$ and a loss $L$, the statistical risk, also known as generalisation error, is defined as

$$
R(m)=\mathbb{E}[L(m(\boldsymbol{X}), Y)]
$$

where the expectation is taken with respect to the joint distribution of $Y$ and $\boldsymbol{X}$. The goal of statistical learning is to find the ideal model $m^{\star} \in \mathcal{M}$ minimising the corresponding statistical risk $R(m)$ (1). Supposed a solution exists, this amounts to the Bayes rule,

$$
m^{\star}=\underset{m \in \mathcal{M}}{\arg \min } R(m)
$$

The tower property of the conditional expectation yields the representation

$$
R(m)=\mathbb{E}[\mathbb{E}[L(m(\boldsymbol{X}), Y) \mid \boldsymbol{X}]]
$$

If there is some model $m_{0}$ minimising the conditional statistical risk

$$
R(m \mid \boldsymbol{x})=\mathbb{E}[L(m(\boldsymbol{x}), Y) \mid \boldsymbol{X}=\boldsymbol{x}]
$$

for almost all $\boldsymbol{x} \in \mathcal{X}, 8$ then $m_{0}$ clearly minimises the unconditional risk and $m^{\star}=m_{0}$.
In the absence of knowing the distribution of $(\boldsymbol{X}, Y)$ on the population level, we cannot calculate the statistical risk $R(m)$, and therefore generally also fail to determine the ideal model $m^{\star}$. We need to resort to an approximation of $R(m)$ on a sample level. Employing a random sample $D=\left\{\left(\boldsymbol{x}_{i}, y_{i}\right), i=1, \ldots, n\right\}$, we can easily compute the empirical risk

$$
\bar{R}(m ; D)=\frac{1}{n} \sum_{\left(\boldsymbol{x}_{i}, y_{i}\right) \in D} L\left(m\left(\boldsymbol{x}_{i}\right), y_{i}\right)
$$

The so called M-estimator ${ }^{9} \widehat{m}$ is defined as the empirical risk minimiser

$$
\widehat{m}=\widehat{m}\left(\cdot ; D_{\text {train }}\right)=\underset{m \in \mathcal{M}}{\arg \min } \bar{R}\left(m ; D_{\text {train }}\right)
$$

[^0]
[^0]:    8 That means it holds for all $\boldsymbol{x}$ in some subset $A \subseteq \mathcal{X}$ such that $\boldsymbol{X} \in A$ with probability one.
    9 Where the "M" is for minimisation and is due to Huber [41]; see also [42] for a good textbook.

## Page 11
over a training sample $D_{\text {train }}$. Since estimating $\widehat{m}$ is based on the empirical risk, which is only an approximation of the statistical risk, it suffers from sampling uncertainty and is thus prone to estimation error. In particular, $\widehat{m}=\widehat{m}\left(\cdot ; D_{\text {train }}\right)$ inherently depends on the particular training sample $D_{\text {train }}$ at hand. If another training sample $D_{\text {train }}^{\prime}$ had been chosen, then generally $\widehat{m}\left(\cdot ; D_{\text {train }}\right) \neq \widehat{m}\left(\cdot ; D_{\text {train }}^{\prime}\right)$. This sampling variability leads us directly to the keyword of overfitting which we will formally introduce in Definition 1. A common practice to reduce this variability is to add an additional penalty term, $\lambda \Omega(m)$, such that (3) turns into

$$
\widehat{m}=\widehat{m}\left(\cdot ; D_{\text {train }}\right)=\underset{m \in \mathcal{M}}{\arg \min } \bar{R}\left(m ; D_{\text {train }}\right)+\lambda \Omega(m)
$$

Often, $\Omega: \mathcal{M} \rightarrow \mathbb{R}$ represents model complexity, see Theory 2.1. For example, it can be a norm of the underlying parameter vector $\theta$, employed in ridge or lasso regression. The penalisation strength $\lambda \geq 0$ is a tuning parameter, or hyperparameter. It should asymptotically vanish with increasing sample size, which is necessary to obtain a consistent estimate of the statistical risk and thus of the ideal model $m^{\star}$. Still, this is only an asymptotic result, and in finite samples, $\widehat{m} \neq m^{\star}$ is to be expected.

This fact necessitates a reliable evaluation of the predictive accuracy of $\widehat{m}\left(\cdot ; D_{\text {train }}\right)$, quantifying how well it generalises to unseen data points, $\left(\boldsymbol{x}_{\text {new }}, y_{\text {new }}\right)$. Furthermore, it calls for a meaningful comparison of different estimators of $m^{\star}$ which will be the main subject of Section 5. These estimators could stem from different samples or from different choices of the penalty term $\lambda \Omega(\cdot)$. The first possibility that comes to mind to estimate the statistical risk of $\widehat{m}\left(\cdot ; D_{\text {train }}\right)$ is to use the same $D_{\text {train }}$ again in the empirical risk, i.e. to use the in-sample performance, in-sample risk, or training loss, $\bar{R}\left(\widehat{m}\left(\cdot ; D_{\text {train }}\right) ; D_{\text {train }}\right)$. Having used the training sample twice, it is generally a biased performance measure. Since any estimator is tailored to fit the training sample involved in the estimation process, ${ }^{10}$ the in-sample risk is usually an overly optimistic performance measure that underestimates the statistical risk of $\widehat{m}\left(\cdot ; D_{\text {train }}\right) .{ }^{11}$ This is connected to the notion of overfitting.

Instead, the in-sample risk should be discarded in favour of an out-of-sample risk, i.e. the empirical risk evaluated on an independent test data set $D_{\text {test }}$ as $\bar{R}\left(\widehat{m}\left(\cdot ; D_{\text {train }}\right) ; D_{\text {test }}\right)$.

As the term overfitting is often used heuristically, we make it more precise by defining

[^0]
[^0]:    10 For instance, the OLS estimator is constructed as to minimise the in-sample squared error. It approximates the conditional mean $\mathbb{E}[Y \mid \boldsymbol{X}=\boldsymbol{x}]$ perfectly on the training sample in so far as the sum of residuals is 0 by construction.
    11 To be precise, the bias is caused by the dependence between the fitted model and the data used to estimate the risk. For squared error and zero-one loss, it can be shown that, in expectation, this bias stems indeed from $\operatorname{Cov}\left[\widehat{m}\left(\boldsymbol{X}_{i}\right), Y_{i}\right]$ and is called expected optimism, see Chapter 7.4 in [35] or Theorem 2.2 in [48]. Roughly speaking, the amount of "optimism" of the in-sample risk amounts to too high a sensitivity of the training of the model w.r.t. changes of the response values in the training sample.

## Page 12
Figure 3: Illustration of over- and underfitting in the classical regime. The estimation error corresponds to the last line in (4). Both regimes together show the typical double descent slope of the statistical risk.

overfitting in a relative sense, cf. [54]:

**Definition 1** *Model m ∈ M overfits (w.r.t. model complexity given by Ω) the training data D_train if there exists another model m′ ∈ M with Ω(m′) < Ω(m) such that R̄(m; D_train) ≤ R̄(m′; D_train), but R(m) > R(m′).*

Clearly, this definition of overfitting is only relevant on model classes M containing models of different complexity. The left side of Figure 3, denoted by "classical regime", provides an illustration of over- and underfitting with the typical U-shape of the statistical risk and a monotonically decreasing in-sample risk. Intuitively, overfitting appears as soon as a model starts to learn the training set by heart, indicated by point A. The behaviour of this regime is often explained by the bias-variance trade-off [26, 35]: At low complexity, the model is not able to capture the data structure, leading to a high bias. With larger complexity, the bias is reduced, but the variance, i.e. the estimation error, grows.

The interpolating regime on the right side of Figure 3 is an area of recent research, initiated by investigating the success of deep neural nets—models with an enormously huge amount of parameters—[59, 79]. The point where a model starts to interpolate the data, i.e. m(xi) = yi for all training data (xii, yi) ∈ D_train, has a very high statistical risk. 12 But as the model gets even more overparametrised, the statistical risk decreases again, while the in-sample risk remains constant (and minimal). Therefore, the terms interpolation and overparameterisation are more appropriate in this regime than the

<sup>12</sup> Here, we implicitly assume that the target functional T satisfies T(δy) = y for any y ∈ Y, where δy is a point mass in y.
![Page 12 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p12_img1.jpg)

## Page 13
notion of overfitting. The overall shape of the statistical risk has been called "double descent" and has been confirmed for several model classes [5]. Analytical results are available for linear models $[6,36,2]$. Whether there is a point in the interpolating regime with a smaller statistical risk than the local minimum in the classical regime denoted by $A$ depends on the model class as well as the distribution of the data, see [12] for a review.

Another possible way for dealing with the bias of the in-sample risk besides making use of an independent test data set is to use alternative in-sample measures like Akaike's information criterion (AIC) or the Bayesian information criterion (BIC), see [35] and references therein. They measure the in-sample risk including a penalty term accounting for model complexity.

The following decomposition of the statistical risk of a model $m \in \mathcal{M}^{13}$ illustrates the constituent parts of the learning procedure:

$$
\begin{aligned}
R(m) & =\inf _{g: \mathcal{X} \rightarrow \mathcal{Y}} R(g) & & \text { inherent unpredictability } \\
& +\inf _{f \in \mathcal{M}} R(f)-\inf _{g: \mathcal{X} \rightarrow \mathcal{Y}} R(g) & & \text { approximation error } \\
& +\inf _{f \in \mathcal{M}} \bar{R}(f ; D)-\inf _{f \in \mathcal{M}} R(f) & & \text { estimation error I } \\
& +\bar{R}(m ; D) \quad-\inf _{f \in \mathcal{M}} \bar{R}(f ; D) & & \text { optimisation error } \\
& +R(m) \quad-\bar{R}(m ; D) & & \text { estimation error II }
\end{aligned}
$$

Note that while the approximation and optimisation errors are always non-negative, the two estimation errors can have any sign. ${ }^{14}$ Equation (17) in Section 5 provides an alternative decomposition of statistical risk (there named expected score) with an emphasis on evaluation rather than learning.

# 3.2. Practicalities 

### 3.2.1. Train-Validation-Test split

In actuarial practice and machine learning, one often enjoys the situation of having a large amount of data, ${ }^{15}$ both for fitting and for model evaluation and comparison. Then, a crucial rule is to divide the data set into mutually exclusive subsets. Terminology and usage patterns for those data samples vary in the literature. We give the following definition, cf. [35, Chapter 7.2], [78, Chapter 7.2.3], [65]:

- Training set for model fitting, typically the largest set.

[^0]
[^0]:    13 Due to Daniel Hsu's slides https://www.cs.columbia.edu/ djhsu/tripodsbootcamp/overview. slides.pdf.
    14 Figure 7.2 in [35] illustrates a similar decomposition.
    15 Interestingly, the amount of data available to actuaries varies a lot depending on insurance sector and country, from (almost) no data for newly invented insurance coverages to usually very good amounts of data for motor insurance.

## Page 14
- Validation set for model comparison and model selection.

Typically, this set is used to tune a model of a given model class while building (fitting) models on the training set. Examples are variable selection and specification of terms for linear models, finding optimal architecture and early stopping for neural nets, hyperparameter tuning of boosted trees. This way, the validation set is heavily used and therefore does not provide an unbiased performance estimate anymore. The result is a "final" model for the given model class that is often refit on the joint training and validation sets.

- Test set for assessment and comparison of final models.

Once the model building phase is finished, this set is used to calculate an unbiased estimate of the statistical risk. It may be used to pick the best one of the (few) final models.

- Application set.

This is the data the model is used for in production. It consists of feature variables only. If the observations of the response become known after a certain time delay, it can serve to monitor the performance of the model.

In practise, the usage of the terms "validation set" and "test set" is often not clearly distinguished.

A golden rule is: Never ever look at the test set while still training models. Any data leakage from the test to the training set might invalidate the results, i.e. it will likely render evaluation results on the test set too optimistic. Also be aware that the more you use the test or validation data set, the less reliable your results become. ${ }^{16}$ For the validation set, this risk can be mitigated to some degree by methods like cross-validation, see below.

Data points $\left(\boldsymbol{x}_{i}, y_{i}\right) \in D_{\text {test }}$ of a hold-out set, i.e. validation and test set, should be independently drawn from the same distribution as the training set, ensuring that the evaluation is representative on the one hand and preventing overly optimistic results on the other hand. ${ }^{17}$ Below, we review and discuss some examples of data with dependencies.

A methodological sound train-validation-test split and usage pattern is essential for building good models and for an unbiased assessment of predictive performance.

[^0]
[^0]:    16 Assume 1000 random forests, each trained with a different random seed. Now, we evaluate on the validation set which one performs best and choose it as our final tuned model. We will pick the one that, by chance, optimised the validation set. If we finally look at the performance of the picked model on an independent test set, we might likely see a worse performance than on the validation set. This can be seen as an instance of the survivorship bias.
    17 Beware of distributions of response or feature variables that change over time. Take the trend to improved motorway safety in Switzerland as an example. A model for insurance claims frequency fitted in the year 2000 and evaluated on test data from 2015-2020 will show that it is not a good fit for today's situation, but might have been a good model at its time.

## Page 15
# 3.2.2. Data with dependencies 

Real life data sets often contain dependent rows. Taking the dependence structure into account is essential to create independent data sets, cf. [66].

- Data rows with the same policy number or customer ID are likely correlated. In this case, the same number or ID should only go in either training or test set, but not in both. This is called grouped sampling and is a form of a blocking strategy [66]. In practice, this can be a hidden dependency, e.g., if the ID is unknown.
- If the data at hand is a time series [43], the usual assumption is that the dependence decreases with larger time difference. Therefore, choosing a split time such that all training samples are older than the test set is a good strategy, called out-of-time [71] or forward-validation scheme [69]. The specific validation scheme depends on different aspects, for instance how the models are to be applied. For more details, we refer to the overview and references of [69].

Failing to account for important dependencies is information leakage between test and train set and will often lead to too optimistic results.

### 3.2.3. Data splitting ensuring identical distributions

The second aspect next to independence of the split data sets is to ensure that they are identically distributed. Differently distributed features or response variables will typically lead to different estimates of the statistical risk. This time, however, the direction is unclear: the result on the test set can be clearly better or worse than on the training set. Ensuring identically distributed sets makes results comparable.

- The data at hand might be ordered in some way. A simple random shuffled split then helps to create similarly distributed data sets. This procedure, however, does not mitigate possible dependence in the data.
- To ensure identically distributed response variables, one can employ stratified sampling. It can be combined with the previous point and is then called stratified random sampling. Stratification is often applied in classification problems, as do we in Example 3.3. Interestingly, stratification may induce some degree of dependence between the test and the training set, underpinning that there is no silver bullet in statistics.


### 3.2.4. Cross-Validation

A statistically more robust and less wasteful alternative to the above strategy of using a validation set to evaluate and compare models is $k$-fold cross-validation (CV) [35, 1]. There, the full data set available for training and validation is first split into $k$ partitions or folds, where $k$ is often a value between five and ten. For each fold, a model is trained on the remaining $k-1$ folds and a validation score is calculated from the hold-out fold. The $k$ validation scores are then summarised to an average CV score that can be

## Page 16
|  | Mean | Quantile |  |  |  |  |  |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| Set |  | $20 \%$ | $40 \%$ | $50 \%$ | $60 \%$ | $80 \%$ | $90 \%$ |
| train | 13001 | 204 | 461 | 693 | 1097 | 4596 | 18558 |
| test | 13025 | 202 | 460 | 700 | 1136 | 4715 | 20346 |

Table 1: Sample statistics of UltimateIncurredClaimCost on train and test set.
supplemented by its standard error or a confidence interval. ${ }^{18}$ After all decisions are made, the final model is retrained on all folds, i.e., on the full data set (besides a possible test data set). In practice, different variants to standard $k$-fold CV exist, e.g., repeated or nested CV, see references above.

# J 3.3. Example: Mean Regression for Workers' Compensation. 

Before we start modelling, we need to make a train-test split. It could be the case that the same person has several claims represented by different rows in the data. These rows would then likely be correlated. As we do not have that information in our data, we assume no ordering, and we use a random shuffled split which helps to create similarly distributed sets.

```
set.seed(1234321L)
.in <- sample(nrow(df), round(0.75 * nrow(df)), replace = FALSE)
train <- df[.in, ]
test <- df[ .in, ]
y_train <- train[[y_var]]
y_test <- test[[y_var]]
```

For inspection of this point, we list the mean as well as several quantiles of the response variable in Table 1. For large quantiles, we observe a certain discrepancy, but otherwise this looks acceptable.

Later on, we will evaluate and compare the models using the Gamma deviance, see Table 8. Therefore, we mainly focus on models that minimise this loss function. We train four different models:

- Trivial model: It will always predict the mean UltimateIncurredClaimCost of the training set, that is, $m_{\text {trivial }}(\boldsymbol{x})=13001.33$.
- Ordinary least squares (OLS) on $\log (y)$ : As the response is very skewed, but always positive, we fit an OLS model on the log transformed response.

```
form <- reformulate(x_vars, y_var)
fit_ols.log <- lm(update(form, log(UltimateIncurredClaimCost) ~ .),
    data = train)
```

18 Note, however, that CV in fact estimates the statistical risk for different models, each trained on a different fold permutation, meaning on different but dependent training sets. Thus, the averaged loss value over all folds may be seen as measuring the fit algorithm rather than as estimate of the statistical risk of a single-fitted-model, see [4].

## Page 17
Note that the backtransformation for predicting on the untransformed response, $\exp \left(m_{\mathrm{OLS}}(\boldsymbol{x})\right)$, introduces a bias. We mitigate this by a multiplicative correction factor corr_fact_ols $=6.644697$; see listing above.

- Gamma generalised linear model (GLM) with log link: Note that, while the log link gives us positive predictions, it is not the canonical link of the Gamma GLM, and therefore introduces a slight bias (see discussion around Equation (9) for this bias and the balance property). As for the OLS in log-space, we account for that with the multiplicative correction factor corr_fact_glm $=1.11445$, which is much smaller than the factor for the OLS.

```
library(glm2)
# glm2 is more stable.
fit_glm_gamma <- glm2(reformulate(x_vars, y_var), data = train,
    family = Gamma(link = "log"))
glm_gamma_predict <- function(X) {
    predict(fit_glm_gamma, X, type = "response")
}
corr_fact_glm <- mean(y_train) / mean(glm_gamma_predict(train))
glm_gamma_corr_predict <- function(X){
    corr_fact_glm * predict(fit_glm_gamma, X, type = "response")
}
```

- Poisson GLM: We keep the log link, but now use a Poisson distribution because this gives us a GLM with canonical link with good calibration properties. For instance, we do not need a correction factor.
- Gradient boosted trees via XGBoost [11] with Gamma deviance loss and log link: Parameters are tuned by five-fold cross-validation on the training data. As for the Gamma GLM, we apply a multiplicative correction factor corr_fact_xgb $=1.194863$ in order to be unbiased on the training data.

Instead of a multiplicative correction factor, we could have corrected the models by adding a constant. An additive constant, however, has the disadvantage that it could render some predictions negative. A multiplicative correction is better suited for models with a log link and models fit on the log transformed response as it is just an additive constant in link-space. For the Gamma GLM, it corresponds to adjusting the intercept term.

For this user guide the above five models are sufficient. Further models or improvements could consist in a separate large claim handling, e.g., shown in [22], more feature engineering with larger model pipelines, usage of other model types like neural nets, stacking of models, and many more.

## Page 18
# 4. Calibration and Identification Functions 

### 4.1. Theory

Once a certain model $m \in \mathcal{M}$ has been fitted, important questions arise: "Is the model fit for its purpose?" Or similarly: "Does the model produce predictions which are in line with the observations?" To answer these questions, the statistical notion of calibration is adequate, which was coined in [13] and further examined in [60].

### 4.1.1. Conditional calibration and auto-calibration

To introduce a formal definition of calibration, recall that exactly predicting $Y$ using a feature vector $\boldsymbol{X} \in \mathcal{X}$ is illusive. In almost all applications, $\boldsymbol{X}$ does not describe $Y$ entirely in the sense that $Y$ is a deterministic function of $\boldsymbol{X}$. That means $Y$ given $\boldsymbol{X}$ is stochastic, and we summerise this stochasticity in terms of a functional $T$. Our definitions of calibration follow $[60,49]$.

Definition 2 Given a feature-response pair $(\boldsymbol{X}, Y)$, the model $m(\boldsymbol{X})$ is conditionally calibrated for the functional $T$ if

$$
m(\boldsymbol{X})=T(Y \mid \boldsymbol{X}) \quad \text { almost surely. }
$$

The model $m(\boldsymbol{X})$ is auto-calibrated for $T$ if

$$
m(\boldsymbol{X})=T(Y \mid m(\boldsymbol{X})) \quad \text { almost surely. }
$$

In other words, a conditionally calibrated model uses the entire feature information ideally in the prediction task. It describes the oracle regression function $\mathcal{X} \ni \boldsymbol{x} \mapsto T(Y \mid \boldsymbol{X}=\boldsymbol{x})$. On the other hand, auto-calibration merely says that the information in the model $m(\boldsymbol{X})$ is used ideally to predict $Y$ in terms of $T$. Clearly, the one-dimensional $m(\boldsymbol{X}) \in \mathbb{R}$ is less informative than the feature $\boldsymbol{X} \in \mathcal{X}$ itself. In the extreme case when $m(\boldsymbol{X})$ is a constant model, it contains no information. Being auto-calibrated then simply means that the model equals the unconditional functional value $T(Y) .{ }^{19}$ For the rich class of identifiable functionals so called moment or identification functions are a tool to assess conditional calibration and auto-calibration.

Definition 3 Let $\mathcal{F}$ be a class of probability distributions where the functional $T$ is defined on. A strict $\mathcal{F}$-identification function for $T$ is a function $V(z, y)$ in a forecast $z$ and an observation $y$ such that

$$
\int V(z, y) \mathrm{d} F(y)=0 \quad \Longleftrightarrow \quad z=T(F) \quad \text { for all } z \in \mathbb{R}, F \in \mathcal{F}
$$

[^0]
[^0]:    19 In an insurance context, this would amount to assessing the risk of each client of a car insurance with the very same number, no matter what age, health conditions and experience they have, or if they have ever been involved in a car accident before.

## Page 19
| Functional | Strict Identification Function | Domain of $y, z$ |
| :-- | :-- | :-- |
| expectation $\mathbb{E}[Y]$ | $V(z, y)=z-y$ | $\mathbb{R}$ |
| $\alpha$-expectile | $V(z, y)=2|\mathbb{1}\{z \geq y\}-\alpha|(z-y)$ | $\mathbb{R}$ |
| median $F_{Y}^{-1}(0.5)$ | $V(z, y)=\mathbb{1}\{z \geq y\}-1 / 2$ | $\mathbb{R}$ |
| $\alpha$-quantile $F_{Y}^{-1}(\alpha)$ | $V(z, y)=\mathbb{1}\{z \geq y\}-\alpha$ | $\mathbb{R}$ |

Table 2: Table of canonical strict identification functions.

If only the implication $\Longleftarrow$ in (5) holds, then $V$ is just called an $\mathcal{F}$-identification function for $T$. If $T$ admits a strict $\mathcal{F}$-identification function, it is identifiable on $\mathcal{F}$.

Table 2 displays the most common strict identification functions for the mean and median as well as their generalisations, $\alpha$-quantiles for the latter and $\alpha$-expectiles for former. ${ }^{20}$ When $T$ is the mean functional, (conditional) calibration boils down to (conditional) unbiasedness. Not all functionals are identifiable. Most prominently, the variance, the expected shortfall (an important quantitative risk measure) and the mode (the point with highest density) fail to be identifiable [61, 27, 72, 38]. Strict identification functions are not unique: If $V(z, y)$ is a strict $\mathcal{F}$-identification function for $T$, so is $\widetilde{V}(z, y)=h(z) V(z, y)$, where $h(z) \neq 0$ for all $z .{ }^{21}$

The connection between calibration and identification functions is as follows: Let $V$ be any strict $\mathcal{F}$-identification function for $T$ and suppose further that $\mathcal{F}$ contains the conditional distributions $F_{Y \mid \boldsymbol{X}=\boldsymbol{x}}$ for almost all $\boldsymbol{x} \in \mathcal{X}$. Then, an application of (5) to these conditional distributions yields that $m(\boldsymbol{x})=T(Y \mid \boldsymbol{X}=\boldsymbol{x})$ if and only if $\int V(m(\boldsymbol{x}), y) \mathrm{d} F_{Y \mid \boldsymbol{X}=\boldsymbol{x}}(y)=0$. This shows that $m$ is conditionally calibrated for $T$ if and only if

$$
\mathbb{E}[V(m(\boldsymbol{X}), Y) \mid \boldsymbol{X}]=0 \quad \text { almost surely. }
$$

Similarly, if the conditional distributions $F_{Y \mid m(\boldsymbol{X})=z}$ are in $\mathcal{F}$ for almost all $z \in \mathbb{R}$, then $m$ is auto-calibrated for $T$ if and only if

$$
\mathbb{E}[V(m(\boldsymbol{X}), Y) \mid m(\boldsymbol{X})]=0 \quad \text { almost surely. }
$$

Hence, for identifiable functionals with a sufficiently rich class $\mathcal{F}$, the tower property of the conditional expectation yields that a conditionally calibrated model is necessarily auto-calibrated. ${ }^{22}$ The reverse implication generally does not hold as can be seen, e.g.,

[^0]
[^0]:    20 We use the indicator function $\mathbb{1}\{A\}= \begin{cases}1, & \text { if } A \text { is true } \\ 0, & \text { else. }\end{cases}$
    21 It is actually also possible to show that all strict identification functions must be of this form, see Theorem S. 1 in [16].
    22 This implication does not necessarily hold for non-identifiable functionals. Consider the variance functional, let $Y$ be standard normal and consider the single feature $X=-Y$. Clearly, $X$ fully describes $Y$. Hence, $\operatorname{Var}[Y \mid X]=0$. The zero model $m(X)=0$ is conditionally calibrated. On the other hand, it provides no information about $Y$ at all. Consequently, conditioning on it has no effect. Since $\operatorname{Var}[Y]=1$, the zero model is not auto-calibrated.

## Page 20
| Notion | Definition | Check |
| :-- | :-- | :-- |
| conditional calibration | $m(\boldsymbol{X})=T(Y \mid \boldsymbol{X})$ | $\mathbb{E}[V(m(\boldsymbol{X}), Y) \mid \boldsymbol{X}]=0$ a.s. |
| auto-calibration | $m(\boldsymbol{X})=T(Y \mid m(\boldsymbol{X}))$ | $\mathbb{E}[V(m(\boldsymbol{X}), Y)] m(\boldsymbol{X})]=0$ a.s. |
| unconditional calibration | $\mathbb{E}[V(m(\boldsymbol{X}), Y)]=0$ | $\mathbb{E}[V(m(\boldsymbol{X}), Y)]=0$ |

Table 3: Types of calibration for an identifiable functional $T$ with strict identification function $V$.
with constant models.

# 4.1.2. Unconditional calibration 

Besides conditional calibration and auto-calibration, one can also find the notion of unconditional calibration in the literature on identifiable functionals. If $V$ is a strict identification function for $T$, then we say that $m(\boldsymbol{X})$ is unconditionally calibrated for $T$ relative to $V$ if $\mathbb{E}[V(m(\boldsymbol{X}), Y)]=0$. Unless $m(\boldsymbol{X})$ is constant, and in stark contrast to conditional calibration and auto-calibration, the notion of unconditional calibration depends on the choice of the identification function $V$ used. Moreover, there is no definition solely in terms of $T$ and $m(\boldsymbol{X})$ as in Definition 2, unless the model is constant such that the notions of unconditional calibration and auto-calibration coincide. As pointed out in [60], non-constant models that are not conditionally calibrated (or autocalibrated) can still be unconditionally calibrated. The different notions of calibration are summarised in Table 3. For a more detailed discussion, we refer to [63] and [31].

### 4.1.3. Assessment of calibration

On a sample $D=\left\{\left(\boldsymbol{x}_{i}, y_{i}\right), i=1, \ldots, n\right\}$, unconditional calibration can be empirically tested by checking whether $\bar{V}(m ; D)=\frac{1}{n} \sum_{\left(\boldsymbol{x}_{i}, y_{i}\right) \in D} V\left(m\left(\boldsymbol{x}_{i}\right), y_{i}\right)$ is close to 0 . This property justifies the term generalised residuals for the quantities $V\left(m\left(\boldsymbol{x}_{i}\right), y_{i}\right)$. Next to pure diagnostics, this can also be accompanied with a Wald test in an asymptotic regime. To check conditional calibration, one needs to assess (6) on a sample level. The presence of the conditional expectation in (6) complicates this check. Formally, (6) is equivalent to

$$
\mathbb{E}[\varphi(\boldsymbol{X}) V(m(\boldsymbol{X}), Y)]=0 \quad \text { for all (measurable) test functions } \varphi: \mathcal{X} \rightarrow \mathbb{R}
$$

Clearly, implementing (8) in practice is usually not feasible. ${ }^{23}$ One needs to choose a finite number of test functions $\varphi_{1}, \ldots, \varphi_{k}$ and check whether $\mathbb{E}\left[\varphi_{j}(\boldsymbol{X}) V(m(\boldsymbol{X}), Y)\right]=0$ for all $j=1, \ldots, k$, which can be done with a Wald test. On the other hand, (6) can be assessed visually with appropriate plots. or by checking suitable plots. The choice of the specific test functions and the overall number of test functions can greatly influence the power of the corresponding Wald test. On the population level, the more test functions,

[^0]
[^0]:    23 An important instance where this is possible is when the features are categorical only such that $\mathcal{X}=\left\{\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{k}\right\}$. Then (6) is equivalent to $\mathbb{E}\left[\mathbb{1}\left\{\boldsymbol{X}=\boldsymbol{x}_{j}\right\} V(m(\boldsymbol{X}), Y)\right]=0$ for all $\boldsymbol{x}_{j} \in \mathcal{X}$.

## Page 21
the higher the power of the test. But in the practically relevant situation of finite samples, increasing the number of test functions also increases the overall estimation error. Hence, one faces a trade-off. In many situations, one is left with practically testing a broader, i.e. less informative, null hypothesis than (6). So if the Wald test fails to reject the null $\mathbb{E}\left[\varphi_{j}(\boldsymbol{X}) V(m(\boldsymbol{X}), Y)\right]=0$ for all $j=1, \ldots, k$, one cannot be sure if (6) actually holds. ${ }^{24}$ It might thus be the case that a model is deemed conditionally calibrated even if it does not make ideal use of the information contained in $\boldsymbol{X}$.

The counterpart of (8) for testing auto-calibration is

$$
\mathbb{E}[\varphi(m(\boldsymbol{X})) V(m(\boldsymbol{X}), Y)]=0 \quad \text { for all (measurable) test functions } \varphi: \mathbb{R} \rightarrow \mathbb{R}
$$

This time $\varphi$ is a univariate function of $m(\boldsymbol{X})$ only, which greatly simplifies the practical implementation. The notion of auto-calibration and its assessment become important when the feature vector $\boldsymbol{X}$ is unknown in the evaluation process, but only the model (prediction) $m(\boldsymbol{X})$ along with the response $Y$ are reported, thus adhering to the weak prequential principle of [14].

Calibration gives us only a very limited possibility to actually compare two models. What if both of them are (auto-)calibrated, but one is more precise in that it incorporates strictly more information than the other one? What about two miscalibrated models? ${ }^{25}$ And how should we think of the situation where we have a calibrated, but uninformative model (e.g., making use of only one covariate) versus a very informative one, which is, however, slightly uncalibrated? On the one hand, such comparisons can be made by the expert at hand, say, the actuary, taking into regard the economic relevance of these differences. ${ }^{26}$ On the other hand, we shall introduce the notion of consistent scoring functions in Section 5. Assessing conditional calibration and resolution (a measure of the information content used in the model or its discrimination ability) simultaneously, they constitute an adequate tool to overall quantify prediction performance, and to ultimately compare and rank different models.

[^0]
[^0]:    24 On top of that, recall the general limitations in statistical tests that it is not possible to establish a null hypothesis by not rejecting it.
    25 This is particularly relevant under model-misspecification. That means that the model class $\mathcal{M}$ is too narrow such that there is no $m^{*}$ with $m^{*}(\boldsymbol{X})=T(Y \mid \boldsymbol{X})$. This can arise, e.g., when a monotone model is used to capture a relation with a clear saturation point. This can be observed, for instance, when $\boldsymbol{X}$ is a driver's age and $T(Y \mid \boldsymbol{X})=\mathbb{P}(Y=1 \mid \boldsymbol{X})$ is the probability of having a car accident $(Y=1)$, given that age. The effect of age on the accident probability is often bathtub-like: young drivers have more accidents, then become safer drivers over time until the risk of accident increases again.
    26 For example, is a more discriminative price policy (say, based on age, health, sex, race etc.) practically implementable, or legal at all? If not, then a less informative but well calibrated model might be more adequate.

## Page 22
# 4.2. Practicalities 

### 4.2.1. Best practice recommendations

- Check for calibration on the training as well as on the test set. On the training set, this yields insights on further modelling improvements, such as including an important omitted feature or excluding a less informative one. (One should, however, mind the overfitting trap when working on the training set.) Once training is finished, assessing calibration on the test set provides a more unbiased view of the calibration and indications whether there is severe bias in the model or whether the model is fit for predictive usage.
- Quantify calibration by making a choice for the test function $\varphi$ and report $\bar{V}_{\varphi}(m ; D)=\frac{1}{n} \sum_{i=1}^{n} \varphi\left(\boldsymbol{x}_{i}\right) V\left(m\left(\boldsymbol{x}_{i}\right), y_{i}\right)$. For practical and diagnostic purposes, we recommend to consider at least $\varphi(\boldsymbol{x})=1$ as well as all projections to single components of the feature vector $\boldsymbol{x}$ (supposed we do not have too many feature components) in addition with the (fitted) model $m(\boldsymbol{x})$, where the latter explicitly assesses auto-calibration. Moreover, the test functions $\varphi$ can be chosen to bin continuous feature variables; see [21] for more details. ${ }^{27}$
- Assess calibration visually: For a test function $\varphi$, plot the generalised residuals $V\left(m\left(\boldsymbol{x}_{i}\right), y_{i}\right)$ versus $\varphi\left(\boldsymbol{x}_{i}\right)$ for the above choices of test functions $\varphi$. Check whether the average of the generalised residuals is around 0 for all values of the test function. Another possibility is to plot the values of $\bar{V}_{\varphi}(m ; D)$ for different $\varphi$, for instance projections to single feature columns; see [21] for more details.
In addition, auto-calibration can be visually assessed by means of a reliability diagram: a graph of the mapping $m(\boldsymbol{x}) \rightarrow T(Y \mid m(\boldsymbol{x}))$, see [31]. For identifiable $T$, $T(Y \mid m(\boldsymbol{x}))$ can be estimated by isotonic regression of $y_{i}$ against $m\left(x_{i}\right)$ as shown in [45]. For an auto-calibrated model, the graph is the diagonal line. Note that due to the estimation error of $T(Y \mid m(\boldsymbol{x}))$ the graph usually shows some deviation from the diagonal even for an auto-calibrated model. In Figure 10, an example is given for binary classification where $T(Y \mid m(\boldsymbol{x}))=\mathbb{E}[Y \mid m(\boldsymbol{x})]$ is called conditional event probability.


### 4.2.2. GLMs with canonical link

By construction, a fitted GLM with canonical link fulfils the simplified score equations

$$
0=\sum_{i} x_{i j}\left(m\left(\boldsymbol{x}_{i}\right)-y_{i}\right) \quad \text { for all components } j \text { of the feature vector }
$$

[^0]
[^0]:    27 If, e.g., a numerical feature variable income is reported, we can bin it in, say, three categories low, middle, and high, defined through two thresholds, say $c_{\text {middle }}$ and $c_{\text {high }}$. Then we can consider the test functions $\varphi_{\text {low }}(\boldsymbol{x})=\mathbb{1}\left\{\right.$ income $\leq c_{\text {middle }}\}$, $\varphi_{\text {middle }}(\boldsymbol{x})=\mathbb{1}\left\{c_{\text {middle }}<\right.$ income $\leq c_{\text {high }}\}$, and $\varphi_{\text {high }}(\boldsymbol{x})=\mathbb{1}\left\{\right.$ income $\left.>c_{\text {high }}\right\}$.

## Page 23
|  | $\bar{V}(m ; D)$ |  | $p$-value of $t$-test |  |
| :-- | :--: | :--: | :--: | :--: |
| Model | $D=$ train | $D=$ test | $p$ train | $p$ test |
| Trivial | 0 | $\mathbf{- 2 4}$ | 1.0 | $9.5 \times 10^{-1}$ |
| OLS | -11045 | -11049 | 0 | $6.4 \times 10^{-188}$ |
| OLS corr | 0 | 109 | 1.0 | $7.6 \times 10^{-1}$ |
| GLM Gamma | -1335 | -1207 | $1.1 \times 10^{-9}$ | $8.8 \times 10^{-4}$ |
| GLM Gamma corr | 0 | 146 | 1.0 | $6.9 \times 10^{-1}$ |
| GLM Poisson | 0 | 125 | 1.0 | $7.3 \times 10^{-1}$ |
| XGBoost | -2120 | -2044 | $1.6 \times 10^{-22}$ | $1.4 \times 10^{-8}$ |
| XGBoost corr | 0 | 96 | 1.0 | $7.9 \times 10^{-1}$ |

Table 4: Assessment of unconditional calibration in terms of bias.
on the training set. ${ }^{28}$ This means that (8) is satisfied on the training set for all projections $\varphi$ to single features. By incorporating a constant feature to account for the intercept, (9) yields the so called balance property [78], $\bar{V}\left(m ; D_{\text {train }}\right)=\frac{1}{n_{\text {train }}} \sum_{\left(\boldsymbol{x}_{i}, y_{i}\right) \in D_{\text {train }}} m\left(\boldsymbol{x}_{i}\right)-y_{i}=$ 0 , which amounts to unconditional calibration on the training set. Moreover, dummy coding and (9) ensure that this balance property also holds on all labels of categorical features. Note that (8) is not necessarily fulfilled for other choices of $\varphi$ on the training set, nor is it clear that (8) holds on the test set in the presence of an estimation error.

# 4.3. Example: Mean Regression for Workers' Compensation. 

As we are modelling the expectation, we use the identification function $V(z, y)=z-y$, corresponding to the bias or negative residual. This immediately leads to the well-known analysis of residuals.

### 4.3.1. Unconditional calibration

Checking for unconditional calibration amounts to checking for the average bias $\bar{V}(m ; D)$ $=\frac{1}{n} \sum_{i \in D} m\left(\boldsymbol{x}_{i}\right)-y_{i}=\frac{1}{n} \sum_{i \in D}$ bias $_{i}$. Normalising with the sample size $n$ ensures that results on training and test set are directly comparable despite having different sizes. From the numbers in Table 4, we confirm that the correction factor eliminated the bias over the whole training set, while there is some bias on the test set. The bias on the test set might be due to estimation error on the training set on the one hand or to sampling error of the test set on the other hand. As expected, the Poisson GLM is unbiased on the training set out of the box as a consequence of the balance property for GLMs with canonical link. This, however, no longer holds on the test set, where the corrected XGBoost is the best one apart from the trivial model.

Table 4 additionally provides $p$-values for the two-sided $t$-tests with null hypotheses $\mathbb{E}[V(m(\boldsymbol{X}), Y)]=0$ for the respective models $m$. The advantage of $p$-values lies in a

[^0]
[^0]:    28 Often in the GLM context, $m\left(\boldsymbol{x}_{i}\right)$ is written as $\mu_{i}$.

## Page 24
|  | $\bar{V}_{\varphi}(m ; D)$ |  |
| :-- | :--: | :--: |
| Model | $D=$ train | $D=$ test |
| Trivial | 0 | $\mathbf{- 3 . 1 3 9 \times 1 0 ^ { 5 }}$ |
| OLS | $-6.201 \times 10^{7}$ | $-5.987 \times 10^{7}$ |
| OLS corr | $-2.266 \times 10^{6}$ | $3.110 \times 10^{7}$ |
| GLM Gamma | $-3.332 \times 10^{7}$ | $-9.977 \times 10^{6}$ |
| GLM Gamma corr | $1.162 \times 10^{7}$ | $3.996 \times 10^{7}$ |
| GLM Poisson | $3.525 \times 10^{7}$ | $7.485 \times 10^{7}$ |
| XGBoost | $-9.254 \times 10^{7}$ | $-6.777 \times 10^{7}$ |
| XGBoost corr | $-3.721 \times 10^{7}$ | $-6.723 \times 10^{6}$ |

Table 5: Assessment of auto-calibration with test function $\varphi(\boldsymbol{x})=m(\boldsymbol{x})$.
scale free representation of the statistic $\bar{V}$ within the range $[0,1]$ and the meaning: the larger the better calibrated.

# 4.3.2. Auto-Calibration 

We analyse auto-calibration by visualising bias versus predicted values. On the training set, this is a vertically flipped version of the well-known residual versus fitted plot. The smoothed lines in Figure 4 are an estimate of the average bias per prediction. We observe large differences in the range of predictions among the models. The three GLMs and the corrected OLS model show a wide range of predicted values with the Poisson GLM having the largest range with the largest predicted value, while the OLS has the smallest range and also the smallest predicted value-neglecting the trivial model. These peculiarities of the OLS are due to the backtransformation after modelling on the log-scale. By comparing the bias term with maximum absolute value, we get another valuable information. The OLS model has the bias term with largest absolute value, on the training set $\left(-3.131 \times 10^{6}\right)$ as well as on the test set $\left(-1.666 \times 10^{6}\right)$, the corrected Gamma GLM has the smallest such value on the training set $\left(-3.073 \times 10^{6}\right)$, the corrected XGBoost exhibits the smallest one on the test set $\left(-1.634 \times 10^{6}\right)$. For the three GLMs and the corrected OLS model, the bias tends to increase with increasing prediction. On the other hand, both XGBoost models show the opposite behaviour. Both phenomena might be due to the fact that there are only a few observations of features leading to large predictions such that the estimation error might be relatively high for such feature constellations. For a better view on the range with most exposure, we draw the smoothed lines only on the restricted range $m(\boldsymbol{x}) \leq 10^{5}$, but this time on the test set, see Figure 5. Here, it becomes visible that the corrected XGBoost model seems to have the best auto-calibration in that range.

The next step is to evaluate different test functions. We list the values of $\bar{V}_{\varphi}$ for the test function $\varphi(\boldsymbol{x})=m(\boldsymbol{x})$ in Table 5. The results are similar in quality to the ones concerning unconditional calibration. Among the non-trivial models, it is again the calibrated XGBoost model that is best in class on the test set.

## Page 25
Bias (negative residuals) vs predicted (training set)

Figure 4: Bias (negative residuals) vs predicted values with smoothed lines for the average bias. Note that the trivial model in the top left plot depicts a straight line, the distortion is due to the hexagon based visualisation.
![Page 25 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p25_img1.jpg)

## Page 26
Figure 5: Smoothed lines for average bias (negative residuals) vs predicted values, truncated at $10^{5}$.

### 4.3.3. Calibration conditional on Gender

We now have a look at the categorical variable Gender. Therefore, we evaluate $\bar{V}_{\varphi}(m ; D)$ for the two projection test functions $\varphi(\boldsymbol{x})=\mathbb{1}\{\text { Gender }="\mathrm{F}"\}$ and $\varphi(\boldsymbol{x})=\mathbb{1}\{\text { Gender }=$ "M" $\}$.

From the bare numbers in Table 6 as well as from the implied bar plot on the left-hand side of Figure 6, we observe again the perfect calibration of the Poisson GLM on the training set due to the balance property (9). This time, this carries over to the test set to a considerable degree. Interestingly, only the Poisson and the corrected Gamma GLM have a positive mean bias for Gender $=$ "F" on the test set. These two models seem to have the best out-of-sample calibration conditional on Gender.

A different perspective arises if, instead of evaluating $\bar{V}_{\varphi}(m ; D)$ on the whole training or test sample, we evaluate the mean bias $\bar{V}(m ; D)$ on the two projected subsamples $D$ with Gender $=$ "M" and Gender $=$ "F" separately. This corresponds to a different normalisation of the averaging step such that one obtains a mean bias per categorical level-a valuable information about possible discrimination. It can be seen from the right-hand side of Figure 6 that the bias for "F" is larger than for "M", in particular the opposite of the left plot.

Remarkably, it turns out that the models with correction factor are not only better unconditionally calibrated than the uncorrected ones, but they are also better conditionally calibrated on Gender, in-sample as well as out-of-sample. If we were to place great importance on calibration, we could exclude the three model variants without correction factor, OLS, Gamma GLM and XGBoost, from further analysis as they persistently show worse calibration than their counterparts with calibration factor.

We could go on and investigate interactions with other features, for instance, use
![Page 26 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p26_img1.jpg)

## Page 27
|  | $\bar{V}_{\varphi}(m ; D)$ |  |  |  |
| :-- | :--: | :--: | :--: | --: |
| Model | train |  | test |  |
|  | bias F | bias M | bias F | bias M |
| Trivial | -969 | 969 | -934 | 910 |
| OLS | -3269 | -7776 | -3250 | -7799 |
| OLS corr | -246 | 246 | -152 | 261 |
| GLM Gamma | -274 | -1061 | -178 | -1029 |
| GLM Gamma corr | 130 | -130 | 237 | -91 |
| GLM Poisson | 0 | 0 | $\mathbf{1 0 5}$ | $\mathbf{2 0}$ |
| XGBoost | -858 | -1262 | -779 | -1265 |
| XGBoost corr | -284 | 284 | -191 | 286 |

Table 6: Assessment of calibration conditional on Gender with test functions $\varphi(\boldsymbol{x})=$ $\mathbb{1}\{$ Gender $=$ "F" $\}$ and $\varphi(\boldsymbol{x})=\mathbb{1}\{$ Gender $=$ "M" $\}$.

Figure 6: Plot of mean bias on the test set. Left: $\bar{V}_{\varphi}(m ; D)$ for the two test functions $\varphi(\boldsymbol{x})=\mathbb{1}\{$ Gender $=\mathrm{F}\}$ and $\varphi(\boldsymbol{x})=\mathbb{1}\{$ Gender $=\mathrm{M}\}$. Right: $\bar{V}$ evaluated on the subsamples with Gender $=$ "F" and Gender $=$ "M", respectively.
![Page 27 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p27_img1.jpg)

## Page 28
|  | $\bar{V}_{\varphi}(m ; D)$ |  |
| :-- | --: | --: |
| Model | $D=$ train | $D=$ test |
| Trivial | -3730 | -3502 |
| OLS | -69362 | -69102 |
| OLS corr | 125 | 1158 |
| GLM Gamma | -8107 | -6985 |
| GLM Gamma corr | 313 | 1549 |
| GLM Poisson | 0 | 1118 |
| XGBoost | -13569 | -12788 |
| XGBoost corr | -298 | $\mathbf{6 1 1}$ |

Table 7: Assessment of conditional calibration with respect to LogWeeklyPay, using test function $\varphi(\boldsymbol{x})=$ LogWeeklyPay.
$\varphi(\boldsymbol{x})=$ LogWeeklyPay $\cdot \mathbb{1}\{$ Gender $=$ "M" $\}$.

# 4.3.4. Calibration conditional on LogWeeklyPay 

In order to assess the calibration conditional on the continuous variable LogWeeklyPay, we bin it on the whole data set into intervals of 11 evenly distributed quantiles $(0,10 \%$, $20 \%, \ldots, 100 \%)$. Since the lowest value WeeklyPay $=200$ occurs in over $22 \%$ of the data rows, we end up with only 8 unique bins. Then we compute

- $\bar{V}_{\varphi}(m ; D)$ for the projection test functions $\varphi_{k}(\boldsymbol{x})=\mathbb{1}\{$ LogWeeklyPay $\in$ bin $k\}$ for all bins $k=1, \ldots, 8$; and
- the average bias $\bar{V}\left(m ; D_{\text {bin }}\right)$ per bin.

To plot the bins on the $x$-axis, we choose the midpoint of each bin. While it is the logarithm of WeeklyPay that enters the models, we display the results in Figure 7 on the original scale. It is obvious that the OLS model without correction is very biased as a consequence of the backtransformation after modelling on the log scale of $y$. We rate the corrected XGBoost model as the most unbiased one, conditional on LogWeeklyPay.

Similar to what we have done for assessing auto-calibration, we also check with the test function $\varphi(\boldsymbol{x})=$ LogWeeklyPay. This leads to computing $\bar{V}_{\varphi}(m ; D)=\frac{1}{n}$ $\sum_{\left(\boldsymbol{x}_{i}, y_{i}\right) \in D} \operatorname{LogWeeklyPay}_{i}\left(m\left(\boldsymbol{x}_{i}\right)-y_{i}\right)$, see Table 7. We see that the Poisson GLM passes this check perfectly on the training set which is a result of the score equation Eq. (9). On the test set, the corrected XGBoost has again the smallest value, which confirms our earlier findings: overall, the corrected XGBoost seems to be the best calibrated model.

## Page 29
Figure 7: Mean bias (negative residual) conditional on binned (quantile based) LogWeeklyPay. Top: $\bar{V}_{\varphi}(m ; D)$ for the test functions $\varphi$ projecting on each bin. Bottom: $\bar{V}\left(m ; D_{\text {bin }}\right)$ for the subsample of each bin.
![Page 29 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p29_img1.jpg)

## Page 30
| Functional | Scoring Function | Formula $S(z, y)$ | Domain |
| :-- | :-- | :-- | :-- |
| expectation $\mathbb{E}[Y]$ | squared error | $(y-z)^{2}$ | $y, z \in \mathbb{R}$ |
|  | Poisson deviance | $2(y \log \frac{y}{z}+z-y)$ | $y \geq 0, z>0$ |
|  | Gamma deviance | $2\left(\log \frac{z}{y}+\frac{y}{z}-1\right)$ | $y, z>0$ |
|  | Tweedie deviance | $2\left(\frac{y^{2-p}}{(1-p)(2-p)}\right.$ | $y, z>0$ |
|  | $p \in \mathbb{R} \backslash\{1,2\}$ | $\left.-\frac{y \cdot z^{1-p}}{1-p}+\frac{z^{2-p}}{2-p}\right)$ | $y \geq 0$ for $p<2$ |
|  | homogeneous score | $\left\lvert\,|y|^{a}-|z|^{a}\right.$ | $y, z \in \mathbb{R}$ |
|  | $a>1$ | $-a \operatorname{sign}(z)|z|^{a-1}(y-z)$ |  |
|  | $\log$ loss | $-y \log z-(1-y) \log (1-z)$ | $0 \leq y \leq 1$ |
|  |  | $+y \log y+(1-y) \log (1-y)$ | $0<z<1$ |
| $\alpha$-expectile | APQSF | $\mid \mathbb{1}\{z \geq y\}-\alpha \mid(z-y)^{2}$ | $\mathbb{R}$ |
| median $F_{Y}^{-1}(0.5)$ | absolute error | $\mid y-z \mid$ | $\mathbb{R}$ |
| $\alpha$-quantile $F_{Y}^{-1}(\alpha)$ | pinball loss | $(\mathbb{1}\{z \geq y\}-\alpha)(z-y)$ | $\mathbb{R}$ |

Table 8: Examples of strictly consistent scoring functions.
For more details about the Tweedie deviance, see Appendix B. The homogeneous score arises from Eq. (13) with $\phi(x)=|x|^{a}$. Note that homogeneous score and Tweedie deviance coincide on the common domains, up to a multiplicative constant. The terms in the second line of the log loss render it non-negative for all $0 \leq y \leq 1$, but are zero for $y \in\{0,1\}$, see Section 6. APQSF stands for asymmetric piecewise quadratic scoring function. The pinball loss is also known as asymmetric piecewise linear scoring function.

# 5. Model Comparison and Selection with Consistent Scoring Functions 

### 5.1. Theory

Suppose we have two models $m_{A}, m_{B}: \mathcal{X} \rightarrow \mathbb{R}$ and we would like to compare and rank their accuracy or predictive performance. Here, we are agnostic about how one has come up with these models. They might be the result of a statistically sound parametric estimation procedure, the yield of fitting the same model with different loss functions, the output of black box algorithms (which is often the case in Machine Learning), or they might be based on expert opinion (or an aggregate of different opinions), underlying physical models or pure gut guess. Since we ignore how the models have been produced, particularly if and what training sample might have been used, we only care about out-of-sample performance.

## Page 31
# 5.1.1. Model comparison 

So suppose we have a random test sample $D=D_{\text {test }}=\left\{\left(\boldsymbol{x}_{i}, y_{i}\right), i=1, \ldots, n\right\}$. The standard tool to assess prediction accuracy are scoring functions $S(z, y)$, which is an alternative name for loss functions frequently used in the forecasting literature; see Footnote 1 for further comments. Just like identification functions, they are functions of the prediction $z=m(\boldsymbol{x})$ and the observed response $y$. In a sense, they measure the distance between a forecast $z$ and the observation $y$, with the standard examples being the squared and the absolute prediction error, $S(z, y)=(z-y)^{2}$ and $S(z, y)=|z-y|$, such that smaller scores are preferable. We estimate the expected score $\mathbb{E}[S(m(\boldsymbol{X}), Y)]$, earlier called statistical risk, as

$$
\bar{S}(m ; D)=\frac{1}{n} \sum_{\left(\boldsymbol{x}_{i}, y_{i}\right) \in D} S\left(m\left(\boldsymbol{x}_{i}\right), y_{i}\right)
$$

which we called empirical risk before. Model $m_{A}$ is deemed to have an inferior predictive performance than model $m_{B}$ in terms of the score $S$ (and on the sample $D$ ) if

$$
\bar{S}\left(m_{A} ; D\right)-\bar{S}\left(m_{B} ; D\right)=\frac{1}{n} \sum_{\left(\boldsymbol{x}_{i}, y_{i}\right) \in D} S\left(m_{A}\left(\boldsymbol{x}_{i}\right), y_{i}\right)-S\left(m_{B}\left(\boldsymbol{x}_{i}\right), y_{i}\right)>0
$$

This pure assessment can be accompanied by a testing procedure to take into account the estimation error of the empirical risk. Hence, we can test for superiority of $m_{A}$ by formally testing (and rejecting) the null hypothesis $\mathbb{E}\left[S\left(m_{A}(\boldsymbol{X}), Y\right)-S\left(m_{B}(\boldsymbol{X}), Y\right)\right] \geq 0$. Similarly, one can also test the composite null that $\mathbb{E}\left[S\left(m_{A}(\boldsymbol{X}), Y\right)-S\left(m_{B}(\boldsymbol{X}), Y\right)\right] \leq 0$, or test the null hypothesis of equal predictive performance via the two-sided null $\mathbb{E}\left[S\left(m_{A}(\boldsymbol{X}), Y\right)-\right.$ $\left.S\left(m_{B}(\boldsymbol{X}), Y\right)\right]=0$. In a cross-sectional framework, these null hypotheses can all be addressed with a $t$-test which provides asymptotically valid results. In the context of predictive performance comparisons, such $t$-tests are also known as Diebold-Mariano tests, $[15] .{ }^{29}$

### 5.1.2. Consistency and elicitability

An important question in this model ranking procedure is the choice of the scoring function $S$. At first glance, there is a multitude of scores to choose from. To get some guidance, let us first ignore the presence of features and consider only constant models. Then, the constant model $m(\boldsymbol{x})=c$ is correctly specified if $c=T(Y)$. To ensure that the correctly specified model outperforms any misspecified model on average if evaluated according to (11), one needs to impose the following consistency criterion on the score $S$, which was coined in [55] and is discussed in detail in [27].

[^0]
[^0]:    29 For more details about hypothesis testing with scoring functions, we refer to Chapter 3 of [29]. Serial correlation as in time-series needs to be accounted for in the estimation of the variance of the score difference. For correction in a cross-validation setting, see [58, 7]. Finally, we hint at recent developments for e-values, see [39].

## Page 32
Definition 4 Let $\mathcal{F}$ be a class of probability distributions where the functional $T$ is defined on. A scoring function $S(z, y)$ is a function in a forecast $z$ and an observation $y$. It is $\mathcal{F}$-consistent for $T$ if

$$
\int S(T(F), y) \mathrm{d} F(y) \leq \int S(z, y) \mathrm{d} F(y) \quad \text { for all } z \in \mathbb{R}, F \in \mathcal{F}
$$

The score is strictly $\mathcal{F}$-consistent for $T$ if it is $\mathcal{F}$-consistent for $T$ and if equality in (12) implies that $z=T(F)$. If $T$ admits a strictly $\mathcal{F}$-consistent scoring function, it is elicitable on $\mathcal{F}$.

If the functional of interest is possibly set-valued (e.g. in the case of quantiles), the usual modification of (12) is that any value in the correctly specified functional $T(F)$ should outperform a forecast $z \notin T(F)$ in expectation. Roughly speaking, strict consistency acts as a "truth serum", encouraging to report correct forecasts.

As can be seen in Table 8, quantiles and expectiles (and therefore the median and mean) are not only identifiable, but also elicitable, subject to mild conditions. Indeed, it can be shown that under some richness assumptions on the class $\mathcal{F}$ and continuity assumptions on $T$, identifiability and elicitability are equivalent for one-dimensional functionals, see [72]. In line with this, variance and expected shortfall fail to be elicitable $[61,27]$. An important exception from this rule is the mode. If $\mathcal{Y}$ is categorical, then the mode is elicitable with the zero-one loss, but no strict identification function is known. For continuous response variables, the mode generally fails to be elicitable or identifiable $[38]$.

# 5.1.3. Characterisation results 

(Strictly) consistent scoring functions for a functional are generally not unique. One obvious fact is that if $S(z, y)$ is (strictly) consistent for $T$, then $\widetilde{S}(z, y)=\lambda S(z, y)+a(y)$ is also (strictly) consistent for $T$ if $\lambda>0$. But the flexibility is usually much higher: For example, under richness conditions on $\mathcal{F}$ and smoothness assumptions on the score, any (strictly) $\mathcal{F}$-consistent score for the mean takes the form of a Bregman function

$$
S(z, y)=\phi(y)-\phi(z)+\phi^{\prime}(z)(z-y)+a(y)
$$

where $\phi$ is (strictly) convex and $a$ is some function only depending on the observation $y$. For $a=0$ and $\phi(z)=z^{2}$, this nests the usual squared error; see Table 8 for some examples. Note also that deviances of the exponential dispersion family are Bregman functions, see [68] and Eq. (2.2.7) of [78]. An example of this fact is given in Appendix B for the Tweedie familiy. For the $\alpha$-quantile, under similar conditions, any (strictly) $\mathcal{F}$-consistent score takes the form

$$
S(z, y)=(\mathbb{1}\{y \leq z\}-\alpha)(g(z)-g(y))+a(y)
$$

called generalised piecewise linear, where $g$ is (strictly) increasing [27]. The standard choice arises when $g(z)=z$ is the identity. Then (14) is often called piecewise linear loss,

## Page 33
tick loss, or pinball loss.
There is an intimate link between strictly consistent scoring functions and strict identification functions, called Osband's principle [61, 27, 24]. For any strictly $\mathcal{F}$ consistent score $S(z, y)$ and strict $\mathcal{F}$-identification function $V(z, y)$ there exists a function $h(z)$ such that

$$
\frac{\partial}{\partial z} \mathbb{E}[S(z, Y)]=h(z) \mathbb{E}[V(z, Y)] \quad \text { for all } z \in \mathbb{R}, \text { for all } Y \sim F \in \mathcal{F}
$$

Using the standard identification functions for the mean and the quantile, Osband's principle (15) applied to (13) yields that $h(z)=\phi^{\prime \prime}(z)$, and applied to (14) it yields $h(z)=g^{\prime}(z)$; see Table 8 for some specific examples. Again, the mode functional constitutes an important exception. Here, for categorical $Y$, any strictly consistent score is of the form

$$
S(z, y)=\lambda \mathbb{1}\{z \neq y\}+a(y), \quad \lambda>0
$$

see $[28]$.

# 5.1.4. Score decompositions 

So far, we have motivated consistency in the setup without any feature information. In the presence of feature information, however, [40] showed that a conditionally calibrated model $m_{A}(\boldsymbol{X})$ outperforms a conditionally calibrated model $m_{B}\left(\boldsymbol{X}^{\prime}\right)$, where the latter one is based only on a subvector $\boldsymbol{X}^{\prime}$ of $\boldsymbol{X}$. This led to the observation that consistent scoring functions assess the information contained in a model and how accurately it is used simultaneously. It can be formalised in the following two versions of the calibrationresolution decomposition due to [63]:

$$
\begin{aligned}
\mathbb{E}[S(m(\boldsymbol{X}), Y)] & =\{\underbrace{\mathbb{E}[S(m(\boldsymbol{X}), Y)]-\mathbb{E}[S(T(Y \mid \boldsymbol{X}), Y)]}_{\text {conditional miscalibration }}\} \\
& -\{\underbrace{\mathbb{E}[S(T(Y), Y)]-\mathbb{E}[S(T(Y \mid \boldsymbol{X}), Y)]}_{\text {conditional resolution } / \text { conditional discrimination }}\}+\underbrace{\mathbb{E}[S(T(Y), Y)]}_{\text {uncertainty / entropy }} \\
& =\{\underbrace{\mathbb{E}[S(m(\boldsymbol{X}), Y)]-\mathbb{E}[S(T(Y \mid m(\boldsymbol{X})), Y)]}_{\text {auto-miscalibration }}\} \\
& -\{\underbrace{\mathbb{E}[S(T(Y), Y)]-\mathbb{E}[S(T(Y \mid m(\boldsymbol{X})), Y)]}_{\text {auto-resolution } / \text { auto-discrimination }}\}+\underbrace{\mathbb{E}[S(T(Y), Y)]}_{\text {uncertainty / entropy }}
\end{aligned}
$$

The term $\mathbb{E}[S(m(\boldsymbol{X}), Y)]-\mathbb{E}[S(T(Y \mid \boldsymbol{X}), Y)]$ expresses the degree of conditional miscalibration of $m(\boldsymbol{X})$ with respect to the information contained in the full feature vector $\boldsymbol{X}$. If the score is $\mathcal{F}$-consistent and assuming that the conditional distribution $F_{Y \mid \boldsymbol{X}}$ is in $\mathcal{F}$ almost surely, this term is non-negative. Under strict $\mathcal{F}$-consistency, it is 0 if and only if

## Page 34
$m(\boldsymbol{X})=T(Y \mid \boldsymbol{X})$ almost surely. ${ }^{30}$ The second term, $\mathbb{E}[S(T(Y), Y)]-\mathbb{E}[S(T(Y \mid \boldsymbol{X}), Y)]$, called conditional resolution or conditional discrimination, expresses the potential of a calibrated and informed prediction $T(Y \mid \boldsymbol{X})$ with respect to a calibrated, but uninformative prediction $T(Y)$. Using the tower property of the conditional expectation and consistency, it is non-negative (see also [40]). Under strict consistency, it is 0 if and only if $T(Y \mid \boldsymbol{X})=T(Y)$ almost surely. Finally, $\mathbb{E}[S(T(Y), Y)]$ quantifies the inherent uncertainty of $Y$ when predicting $Y$ in terms of $T$. It is also called entropy or Bayes risk in the literature [30]. The second identity in (17) constitutes a similar score decomposition, but now with respect to the auto-calibration. Here, one is more modest in terms of the information set which is used. It is generated by the model $m(\boldsymbol{X})$ itself (hence the term "auto"). This contains generally less information than $\boldsymbol{X}$ itself. ${ }^{31}$ Therefore, the first term $\mathbb{E}[S(m(\boldsymbol{X}), Y)]-\mathbb{E}[S(T(Y \mid m(\boldsymbol{X})), Y)]$, called automiscalibration, assesses the deviation from perfect auto-calibration, while the second term $\mathbb{E}[S(T(Y), Y)]-\mathbb{E}[S(T(Y \mid m(\boldsymbol{X})), Y)]$, called auto-resolution or auto-discrimination, is still a resolution term, quantifying the potential improvement in reducing uncertainty if the information in the model $m(\boldsymbol{X})$ had been used ideally. This second decomposition reflects the general trade-off a modeller faces when deciding whether to incorporate an additional feature into the model in terms of out-of-sample performance. On the one hand, including additional feature information increases the auto-resolution, but on the other hand, correctly fitting the model will become more difficult making it prone to a potential increase in auto-miscalibration. The two decompositions (17) inform that minimising the expected score in the model $m(\boldsymbol{X})$ amounts to simultaneously improving calibration and maximising resolution [63].

To make the calibration-resolution decomposition (17) tangible, we provide it for the squared error:

$$
\mathbb{E}\left[(m(\boldsymbol{X})-Y)^{2}\right]=\underbrace{\mathbb{E}\left[(m(\boldsymbol{X})-\mathbb{E}[Y \mid \boldsymbol{X}])^{2}\right]}_{\text {conditional miscalibration }}-\underbrace{\operatorname{Var}[\mathbb{E}[Y \mid \boldsymbol{X}]]}_{\text {conditional resolution }}+\underbrace{\operatorname{Var}[Y]}_{\text {uncertainty }}
$$

The intuitive link between the conditional miscalibration term or the auto-miscalibration term on the one hand and the characterisation of conditional calibration (6) or auto-calibration (7) on the other hand can be made as follows: Invoking the close connection between scoring functions and identification functions via Osband's principle (15), the respective miscalibration terms can be regarded as the antiderivative of the expected identification function $\mathbb{E}[V(m(\boldsymbol{X}), Y)]$ in $m(\boldsymbol{X})$, with an additive term such that this antiderivative is non-negative and 0 if and only if the corresponding calibration property holds. (Of course, formally this reasoning only holds for the case of constant models and for auto-calibration / unconditional calibration.)

Practical estimation of $T(Y \mid m(\boldsymbol{X}))$ and therefore of the auto variant of the decomposition can often be performed, see [31] or Figure 10, while the estimation of the ultimate

[^0]
[^0]:    30 This follows from an application of the definition of (strict) consistency (12) using the conditional distribution $F=F_{Y \mid \boldsymbol{X}}$. Then, the expected score amounts to the conditional risk defined in (2).
    31 As an example, consider a linear model where $\boldsymbol{X}$ is high dimensional, but the model $m(\boldsymbol{X})$ is only one-dimensional.

## Page 35
goal $T(Y \mid \boldsymbol{X})$ can be harder. Hence, estimation of the miscalibration and resolution terms in the decompositions (17) are challenging. In any case, the score decompositions yield beneficial conceptional insights. For practical checks of calibration, one should usually resort to the methods pointed out in Section 4. However, since the unconditional functional $T(Y)$ and hence the uncertainty are relatively easy to estimate, a simplified decomposition consisting of miscalibration minus resolution / discrimination on the one hand and uncertainty on the other hand is feasible to estimate. Therefore, [31] have promoted the ratio of these two constituents of the simplified score decomposition as a universal coefficient of determination (tacitly assuming that the scores are non-negative). As an in-sample version, it generalises the classical coefficient of determination, $\mathrm{R}^{2}$, from OLS estimation. The out-of-sample version of this universal coefficient of determination is often referred to as skill score. ${ }^{32}$

We close the discussion by commenting on the differences of the calibration-resolution decomposition (17) from the decomposition of the statistical risk in (4). Upon identifying the loss function $L$ with the score $S$, the terms which are decomposed are the same: $R(m)=\mathbb{E}[S(m(\boldsymbol{X}), Y)]$. The two main differences are, however, that first the decomposition (4) is concerned with estimation of the risk on a sample level while the decomposition (17) stays on a population level. Second, the baseline in (17) is the entropy $\mathbb{E}[S(T(Y), Y)]$, which corresponds to the smallest risk in the class of trivial models $\{1\} \rightarrow \mathcal{Y}$. In contrast, the baseline in (4) is $\inf _{g: \mathcal{X} \rightarrow \mathcal{Y}} R(g)$, which corresponds to the term $\mathbb{E}[S(T(Y \mid \boldsymbol{X}), Y)]$ in (17).

# 5.1.5. Further topics 

The following five topics also have potential relevance in applications:

- When aiming at estimating the expectation functional, often the root mean squared error $\operatorname{RMSE}(m ; D)=\bar{S}(m ; D)^{\frac{1}{2}}$ is reported and used for comparisons instead of the mean squared error (MSE) $\bar{S}(m ; D)=\frac{1}{n} \sum_{\left(\boldsymbol{x}_{i}, y_{i}\right) \in D}\left(m\left(\boldsymbol{x}_{i}\right)-y\right)^{2}$ in order to have a score on the same unit as the response variable. Since taking the square root is a monotone transformation, RMSE and MSE induce the same model ranking.
- Absolute percentage error (APE) $S(z, y)=\left|\frac{z-y}{y}\right|$ and relative error (RE) $S(z, y)=$ $\left|\frac{z-y}{z}\right|, z, y>0$, are two frequently used scores, in particular because they have no unit and can be reported as percentages. According to [27], Theorem 5 (Theorem 2.7 in arxiv version), they both are strictly consistent scoring functions for the $\beta$-median with $\beta=-1$ for the APE and $\beta=1$ for the RE. The $\beta$-median of a distribution $F$ with density $f$ is defined as the median of the re-weighted distribution $F_{\beta}$ with density proportional to $y^{\beta} f(y)$.

[^0]
[^0]:    32 More generally, the skill score for model $m$ and scoring function $S$ is defined as relative improvement over a reference model $m_{\text {ref }}$ as $\operatorname{score}_{\text {skill }}(m ; D)=\frac{\bar{S}(m ; D)-\bar{S}\left(m_{\text {ref }} ; D\right)}{\bar{S}\left(m^{*} ; D\right)-\bar{S}\left(m_{\text {ref }} ; D\right)} \leq 1$ where $\bar{S}\left(m^{*} ; D\right)=0$ for a suitable choice of the constant $a(y)$, see [30]. It has therefore a reversed orientation, meaning larger values are better, and the optimal model achieves $\operatorname{score}_{\text {skill }}\left(m^{*} ; D\right)=1$.

## Page 36
- One could be interested in a whole vector of different point predictions, resulting in a vector of functionals $\left(T_{1}, \ldots, T_{k}\right)$. Scoring functions for such pairs have been studied, e.g., in [24]. Even though variance and expected shortfall fail to be elicitable, the pair of expected shortfall and the quantile at the same probability level admit strictly consistent scores, see [24] for details. Similarly, the pair (mean, variance) is elicitable. Scores of this pair are provided in [25] Eq. (4.13). One particular example derived from the squared loss and the Poisson deviance is

$$
S(\mu, \sigma, y)=(\mu-y)^{2}+y^{2} \log \frac{y^{2}}{\mu^{2}+\sigma^{2}}+\mu^{2}+\sigma^{2}-y^{2}
$$

with predicted mean $\mu$ and predicted standard deviation $\sigma$. Note that this is a homogeneous function of degree two, see (20), and $S(\mu, \sigma, y) \geq S(y, 0, y)=0$.
It might also be interesting to consider pairs of functionals which are elicitable on their own. Two quantiles at different levels $\alpha<\beta$ induce a prediction interval with nominal coverage of $\beta-\alpha$. Scores for two quantiles can easily be obtained as the sum of two generalised linear losses (14). For the case of a central $(1-\alpha)$-prediction interval, i.e. when predicting two quantiles at levels $\frac{\alpha}{2}$ and $1-\frac{\alpha}{2}$, denoted $l$ (lower) and $u$ (upper), a standard interval score [30] arises as

$$
S(l, u, y)=\frac{\alpha}{2}(u-l)+(l-y) \mathbb{1}\{y<l\}+(y-u) \mathbb{1}\{y>u\}
$$

The first term penalises large intervals (corresponding to bad discrimination), the other terms penalise samples outside the predicted interval (corresponding to miscalibration). For more details on evaluating prediction intervals, we refer to [8, 23].

- If the goal is a probabilistic prediction, i.e. to predict the whole conditional distribution $F_{Y \mid \boldsymbol{X}}$, then one uses scoring rules to evaluate the predictions, see [30, 29]. They are maps of the predictive distribution or density and the observation. Here, (strict) consistency is often termed (strict) propriety. It arises in (12) upon considering the identity functional, $T(F)=F$. Standard examples are the logarithmic scoring rule and the continuously ranked probability score.
- The notion of consistency in Definition 4 has its justification in a large sample situation, relying on a Law of Large Numbers argument to approximate expected scores. In a small sample setting it depends on how scores are used. If modellers are rewarded for their prediction accuracy according to the average score their models achieve, consistency still has its justification in a repeated setting. If, on the other hand, the average score is only a tool to establish a ranking of different models, such that there is a winner-takes-it-all reward, one should care about the probability of achieving a smaller score than competitor models, $\mathbb{P}\left(\bar{S}\left(m_{A} ; D\right)<\bar{S}\left(m_{B} ; D\right)\right)$. This probability is not directly linked to the expected score and such schemes do generally not incentivise truthful forecasting [77]. Hence, it provides an example where a criterion other than consistency is justified. While this field is still subject

## Page 37
to ongoing research, the following Subsubsection 5.1.6 provides some links between winner-takes-it-all rewards and efficiency considerations in Diebold-Mariano tests.

# 5.1.6. Role of data generating process for efficiency 

As discussed in Subsubsection 5.1.1, Diebold-Mariano tests for superior predictive performance of model $m_{B}$ over model $m_{A}$ formally test the null hypothesis $\mathbb{E}\left[S\left(m_{A}(\boldsymbol{X}), Y\right)-\right.$ $\left.S\left(m_{B}(\boldsymbol{X}), Y\right)\right] \leq 0$ for a scoring function $S$. Without any further distributional assumptions on $(\boldsymbol{X}, Y)$, one needs to invoke asymptotic normality of the average score differences and uses a $t$ - or a $z$-test. With this normal approximation, the power of such a test, i.e. the probability for rejecting under the alternative, is the higher the smaller the ratio

$$
\frac{\operatorname{Var}\left[S\left(m_{A}(\boldsymbol{X}), Y\right)-S\left(m_{B}(\boldsymbol{X}), Y\right)\right]}{\mathbb{E}\left[S\left(m_{A}(\boldsymbol{X}), Y\right)-S\left(m_{B}(\boldsymbol{X}), Y\right)\right]^{2}}
$$

is. This ratio clearly depends on the true joint distribution of $(\boldsymbol{X}, Y)$ and on the choice of $S$. While we are unaware of any clear theoretical results which $S$ maximises this efficiency, the simulation study in Appendix C and the following arguments provide evidence that scores derived from the negative log-likelihood of the underlying distribution behave advantageously. The rationale is deeply inspired by the exposition of Section 3.3 in [50] highlighting the role of the classical Neyman-Person Lemma.

To facilitate the presentation, we omit the presence of features for a moment such that we only need to care about the distribution of $Y$. Hence, the null simplifies to $H_{0}: \mathbb{E}\left[S\left(z_{A}, Y\right)-S\left(z_{B}, Y\right)\right] \leq 0$ for two reals $z_{A}, z_{B}$. Suppose $Y$ follows some parametric distribution $F_{\theta}$ with density $f_{\theta}, \theta \in \mathbb{R}$. Moreover, assume that on this family, the parameter corresponds to the target functional $T$, i.e. $T\left(F_{\theta}\right)=\theta$ for all $\theta \in \mathbb{R}$. For example, $f_{\theta}$ could be the family of normal densities with mean $\theta$ and variance 1 . Then one could also consider the simple test of the null $H_{0}^{\prime}: Y_{i} \sim f_{z_{A}}$ against the simple alternative $H_{1}^{\prime}: Y_{i} \sim f_{z_{B}}$. The Neyman-Pearson Lemma then asserts that - under independence - the most powerful test at level $\alpha$ is based on the likelihood ratio $\prod_{i=1}^{n} f_{z_{B}}\left(y_{i}\right) / \prod_{i=1}^{n} f_{z_{A}}\left(y_{i}\right)$ and it rejects if this ratio exceeds some critical level $c_{\alpha}$, which is determined such that the probability of false rejection is exactly $\alpha$ under $H_{0}^{\prime}$.

Suppose there exists a strictly consistent scoring function $S$ for $T$ such that for some function $a$ it holds that for all $\theta \in \mathbb{R}, y \in \mathcal{Y}$,

$$
f_{\theta}(y)=\exp (-S(\theta, y)+a(y))
$$

For the above example for normally distributed densities, $S$ could be half of the squared error. Hence, the likelihood ratio exceeds $c_{\alpha}$ if and only if the log of the likelihood ratio, which corresponds to

$$
\log \left(\frac{\prod_{i=1}^{n} f_{z_{B}}\left(y_{i}\right)}{\prod_{i=1}^{n} f_{z_{A}}\left(y_{i}\right)}\right)=\sum_{i=1}^{n} \log \left(f_{z_{B}}\left(y_{i}\right)\right)-\log \left(f_{z_{A}}\left(y_{i}\right)\right)=\sum_{i=1}^{n} S\left(z_{A}, y_{i}\right)-S\left(z_{B}, y_{i}\right)
$$

exceeds $\log \left(c_{\alpha}\right)$. As a matter of fact, the decision based on the likelihood ratio is equivalent

## Page 38
to a decision based on the empirical score difference, or equivalently on the average thereof.

Advantageously, this is not an asymptotic argument, but holds for any finite sample size $n$. On the other hand, the Neyman-Pearson Lemma is only applicable if the level of the test is exactly achieved under the null. The correct critical value $c_{\alpha}$ can, however, only be calculated when exactly knowing $H_{0}^{\prime}$ and $H_{1}^{\prime}$. And it is not clear per se if the test has the correct size under the broader null $H_{0}$.

# 5.2. Practicalities 

### 5.2.1. Which scoring function to choose?

In the presence of a clear purpose for a model, be it business, scientific or anything else, accompanied by an intrinsically meaningful loss function to assess the accuracy of this model, one should just use this very loss function for model ranking and selection. ${ }^{33}$ In the absence of knowing such a specific cost function, but still knowing the modelling target $T$, one should clearly use a strictly consistent scoring function for the functional $T$.

But out of the (usually) infinitely many consistent scoring functions, which one to choose? We see four different directions which might help in selecting a single one:

- Different scoring functions have different domains for forecasts $z$ and observations $y$. For instance, the Poisson deviance can only be used for non-negative $y$ and positive $z$. This might at least exclude some of the choices.
- Scoring functions can exhibit beneficial invariance or equivariance properties. One of the most relevant ones is positive homogeneity. This describes the scaling behaviour of a function if all its arguments are multiplied by the same positive number. The degree of homogeneity of the score $S$ is defined as the number $h$ that fulfils

$$
S(t z, t y)=t^{h} S(z, y) \quad \text { for all } t>0 \text { and for all } z, y
$$

Up to a multiplicative constant, the Tweedie deviances, see Table 8 and Appendix B, are essentially the only homogeneous scoring functions that are strictly consistent for the expectation functional. The Tweedie deviance with power parameter $p$ has degree $h=2-p$, the Gaussian deviance (corresponding to the squared error) has $h=2$, the Poisson deviance $h=1$, the Gamma deviance $h=0$ and the inverse Gaussian deviance $h=-1$. This reflects the well-known fact that the squared error penalises large deviations of its arguments quadratically more than small ones. On the other hand, the Poisson deviance scales linearly with its arguments and preserves the unit. For instance, if $z$ and $y$ are amounts in some currency like CHF, the unit of Poisson deviance is CHF, too. The scale-invariant Gamma

[^0]
[^0]:    33 E.g. the owner of a windmill might be interested in predictions for windspeed. Windspeed is directly linked to the production capability of electricity for the windmill. The owner uses this capability to enter a short-term contract on the electricity marked with explicit costs for over- or undersupply, resulting in an explicit economic loss for inaccurate forecasts.

## Page 39
deviance only measures relative differences and has no notion of scales or units. As a 0 -homogeneous score it can downgrade the (conditional) heteroskedasticity in the data (volatility clusters etc.). Lastly, larger values of the Tweedie power correspond to heavier-tailed distributions (still, all moments are finite). The larger the Tweedie power, the smaller the degree of homogeneity of the corresponding deviance, which puts less and less emphasis on the deviation of large values and more and more weight on deviations of small values. ${ }^{34}$

- Another aspect in the choice of the scoring function is the efficiency in test decisions for predictive dominance, see Subsubsection 5.1.6. Scoring functions based on the negative log-likelihood of the conditional distribution of $Y$ given $\mathcal{X}$ appear to be beneficial. E.g. if this distribution is a certain Tweedie distribution, the corresponding Tweedie deviance given in Table 8 is appropriate. See Appendix C for a corresponding simulation study.
- In order to assess the ranking of two models with respect to all consistent scoring functions, one can exploit the mixture representations of consistent scores established for quantiles and expectiles in [18] and visually assess the dominance in terms of Murphy diagrams, see Figure 9.


# 5.2.2. Sample weights and scoring functions 

For model fitting, a priori known sample weights $w_{i}>0$, also known as case weights andin the actuarial literature-exposure or volume, are a way to account for heteroskedasticity and to improve the speed of convergence of the estimation. A simple example is given by the weighted least squares estimation in comparison to OLS estimation. More generally, estimating the conditional expectation via maximum likelihood with a member of the exponential dispersion family amounts to minimising the weighted score

$$
\frac{1}{\sum_{i} w_{i}} \sum_{i} w_{i} S\left(m\left(\boldsymbol{x}_{i}\right), y_{i}\right)
$$

for scoring functions $S$ of the Bregman form, see (13) and comments thereafter.
For fitting as well as for model validation, it is noteworthy that using weights often changes the response variable. Take as an example the actuarial task of modelling the average claim size, called severity. Let $w_{i}$ denote the number of claims of a policy $i$ with features $\boldsymbol{X}_{i}$, where $w_{i}$ is given in the feature vector, which happened in a certain amount of time, and $C_{i}$ denotes the corresponding sum of claim amounts. We define the severity as $Y_{i}=\frac{C_{i}}{w_{i}}$. Then, the response modelled and predicted by $m\left(\boldsymbol{X}_{i}\right)$ is $Y_{i}$ and not $C_{i}$, with the important assumption that $\operatorname{Var}\left[Y_{i} \mid \boldsymbol{X}_{i}\right] \propto \frac{1}{w_{i}} .{ }^{35}$

[^0]
[^0]:    34 Consider the inverse Gaussian deviance with $p=3$ and degree of homogeneity $h=-1, S(z, y)=$ $\frac{(z-y)^{2}}{z^{2} y}$. The score $S(2,1)=\frac{1}{4}$ is ten times larger than the score $S(20,10)=\frac{1}{40}$.
    35 This can be seen as follows. We use the $\alpha$ - $\beta$-parametrisation of the Gamma distribution, such that $Z \sim \mathrm{Ga}(\alpha, \beta)$ has $\mathrm{E}[Z]=\frac{\alpha}{\beta}=\mu$ and $\operatorname{Var}[Z]=\frac{\alpha}{\beta^{2}}=\phi \mu^{2}$ upon setting $\phi=\frac{1}{\alpha}$. A typical assumption is that $C_{i}$ is a sum of $w_{i}$ independent $\mathrm{Ga}\left(\alpha, \beta_{i}\right)$-distributed claim amounts each with mean $\mu_{i}$

## Page 40
Back to our main purpose of estimating the expected score $\mathbb{E}[S(m(\boldsymbol{X}), Y)]$ based on an i.i.d. test sample $\left(\boldsymbol{X}_{i}, Y_{i}\right)_{i=1, \ldots, n}$. We assume that $\mathbb{E}[S(m(\boldsymbol{X}), Y) \mid \boldsymbol{X}]=\mu$ for some constant $\mu$ and heteroskedasticity in the form of a conditional variance $\operatorname{Var}[S(m(\boldsymbol{X}), Y) \mid \boldsymbol{X}]=$ $\sigma^{2} h(\boldsymbol{X})$ for some $\sigma^{2}>0$ and some positive and measurable function $h: \mathcal{X} \rightarrow(0, \infty)$. Again, consider the weighted score average

$$
\bar{S}_{n}=\frac{1}{\sum_{i} w_{i}} \sum_{i=1}^{n} w_{i} S\left(m\left(\boldsymbol{X}_{i}\right), Y_{i}\right)
$$

Here, each weight $w_{i}$ is a function of the feature $\boldsymbol{X}_{i}$. For the case that all weights are the same, one simply retrieves the average score $\bar{S}_{n}$. Just like $\bar{S}_{n}$, the weighted average $\bar{S}_{n}$ is an unbiased estimate of the expected score. (This is achieved by the normalisation. Simply consider $\mathbb{E}\left[\bar{S}_{n} \mid \boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{n}\right]=\mu$.) Thanks to the total variance formula, ${ }^{36}$ we can calculate the variance of $\bar{S}_{n}$ as

$$
\operatorname{Var}\left[\bar{S}_{n}\right]=\operatorname{Var}\left[\bar{S}_{n} \mid \boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{n}\right]=\left(\sum_{i=1}^{n} w_{i}\right)^{-2} \sigma^{2} \sum_{i=1}^{n} w_{i}^{2} h\left(\boldsymbol{X}_{i}\right)
$$

Minimising (21) with respect to the weights yields that any solution can be written as $w_{i}=\lambda / h\left(\boldsymbol{X}_{i}\right)$ for some constant $\lambda>0 .{ }^{37}$

The major drawback with this re-weighting approach in practice is that the conditional variance of the scores is usually unknown. Even if the conditional variance of the response variable is known or assumed, as in maximum likelihood estimation, the authors are not aware of a general link to the level of the score. Whether weighted averages with weights accounting for heteroskedasticity of the response provide more efficient estimates for the expected score seems to be an open question. That being said, weighted averages of scores are nonetheless unbiased.

# 5.3. Example: Mean Regression for Workers' Compensation. 

### 5.3.1. Model comparison with Gamma deviance

As stated in the Example 3.3, we evaluate our models with the Gamma deviance, see Table 8 and Equation (10). The reasons for this choice follow the discussion of Subsubsection 5.2.1:

- The target functional is the expectation and the Gamma deviance is strictly consistent for it.

[^0]
[^0]:    and variance $\phi \mu_{i}^{2}$, such that $C_{i} \mid \boldsymbol{X}_{i} \sim \mathrm{Ga}\left(w_{i} \alpha_{i} \beta_{i}\right)$. Then, the severity is also Gamma distributed, $Y_{i} \mid \boldsymbol{X}_{i} \sim \mathrm{G}\left(w_{i} \alpha_{i} w_{i} \beta_{i}\right)$, with mean $\mathbb{E}\left[Y_{i} \mid \boldsymbol{X}_{i}\right]=\frac{\alpha}{\beta_{i}}=\mu_{i}$ and variance $\operatorname{Var}\left[Y_{i} \mid \boldsymbol{X}_{i}\right]=\frac{1}{w_{i}} \phi \mu_{i}^{2}$.
    36 It asserts that $\operatorname{Var}[Z]=\mathbb{E}[\operatorname{Var}[Z \mid \boldsymbol{X}]]+\operatorname{Var}[\mathbb{E}[Z \mid \boldsymbol{X}]]$.
    37 This can be easiest derived by a constraint optimisation with the Lagrange method, where (21) is minimised subject to $\sum_{i=1}^{n} w_{i}=c$ for some constant $c>0$.)

## Page 41
- Observations and predictions are positive, thus falling within the domain of the Gamma deviance.
- The 0-homogeneity of the Gamma deviance implies that the induced model ranking is independent of the unit of the response (currency in our case).
- The response is right-skewed. The Gamma distribution is a good candidate distribution for such data within the class of Tweedie distributions. In addition, only Tweedie deviances provide homogeneous scores.

In analogy to the coefficient of determination, $\mathrm{R}^{2}$, we additionally report the (relative) Gamma deviance reduction $\mathrm{R}^{\star}=1-\frac{\bar{S}(m ; D)}{\bar{S}\left(m_{\text {trivial }} ; D\right)}$, which is closely related to McFadden's pseudo $\mathrm{R}^{2}$ and which corresponds to the universal coefficient of determination coined in [31]. It holds that $\mathrm{R}^{\star} \leq 1$, where a larger value indicates a better fit. Table 9 displays the scores on the training as well as on the test set. Figure 8 visualises these numbers. The best out-of-sample performance is achieved by the corrected XGBoost with a test $\mathrm{R}^{\star}$ of 0.308 . We could use a $t$-test to check whether it is significantly better than the second best model, but refrain here to do so. We also observe for all models that the in-sample $\mathrm{R}^{\star}$ is better (higher) than the out-of-sample $\mathrm{R}^{\star}$, reflecting the general difficulty to generalise to new data. According to our definition of overfitting in Definition 1, the uncorrected XGBoost model overfits the training data. Indeed, the corrected XGBoost model exhibits a smaller complexity (the correction acts as additional constraint and reduces the degrees of freedom in fitting by one) and it holds that $\bar{S}\left(m_{\text {xgb }} ; D_{\text {train }}\right)<\bar{S}\left(m_{\text {xgb_corr }} ; D_{\text {train }}\right)$, while $\bar{S}\left(m_{\text {xgb }} ; D_{\text {test }}\right)>\bar{S}\left(m_{\text {xgb_corr }} ; D_{\text {test }}\right)$. Another observation is that both Gamma GLMs perform better in terms of Gamma deviance than the Poisson GLM. This is to be expected as the Gamma GLMs minimise the Gamma deviance on the training set, while the training objective for the Poisson GLM is the Poisson deviance. Similar to our finding for calibration, the bare OLS shows very poor performance, even negative $\mathrm{R}^{\star}$, indicating worse predictive performance than the trivial model. Again, this is the consequence of modelling on the log transformed response variable and then backtransforming for prediction. On the other hand, the corrected OLS performs even better than the Poisson GLM. Regarding the correction term for the Gamma GLM and the XGBoost model, it slightly reduces the performance on the training set. On the test set, however, there is hardly a penalty left. On the contrary, the XGBoost out-of-sample performance is even improved by it.

For a more detailled inspection, we add the score decomposition of the Gamma deviance according to the auto-variant of (17) in Table 10. We observe that the uncertainty term is by far the largest component. The model ranking is then dominated by the autoresolution term (larger is better). Clearly, the XGBoost models make most use of the information contained in themselves. The only exception is again the OLS model, whose auto-miscalibration component is even larger than the uncertainty term. Interestingly, auto-miscalibration is the decisive component for the ranking within the different GLMs, with the Gamma GLMs being better auto-calibrated than the Poisson GLM. To the largest part, these findings are in line with Table 5.

## Page 42
Figure 8: Performance on training and validation data in terms of mean Gamma deviance (smaller is better) and its relative reduction $\mathrm{R}^{*}$ (larger is better).

| Model | $\mathrm{R}^{*}$ train | $\mathrm{R}^{*}$ test | Mean deviance train | Mean deviance test |
| :-- | --: | --: | --: | --: |
| Trivial | 0 | 0 | 5.08 | 5.04 |
| OLS | -1.24 | -1.33 | 11.4 | 11.8 |
| OLS corr | 0.251 | 0.240 | 3.80 | 3.83 |
| GLM Gamma | 0.279 | 0.271 | 3.66 | 3.68 |
| GLM Gamma corr | 0.277 | 0.270 | 3.67 | 3.68 |
| GLM Poisson | 0.225 | 0.216 | 3.94 | 3.95 |
| XGB | 0.362 | 0.299 | 3.24 | 3.54 |
| XGB corr | 0.358 | $\mathbf{0 . 3 0 6}$ | 3.26 | $\mathbf{3 . 5 0}$ |

Table 9: Performance on training and validation data in terms of mean Gamma deviance (smaller is better) and its relative reduction $\mathrm{R}^{*}$ (larger is better).

| Model | Mean deviance | Auto-miscalibration | Auto-resolution | Uncertainty |
| :-- | --: | --: | --: | --: |
| Trivial | 5.04 | 0 | 0 | 5.04 |
| OLS | 11.8 | 8.25 | 1.52 | 5.04 |
| OLS corr | 3.83 | 0.314 | 1.52 | 5.04 |
| GLM Gamma | 3.68 | 0.190 | 1.56 | 5.04 |
| GLM Gamma corr | 3.68 | 0.197 | 1.56 | 5.04 |
| GLM Poisson | 3.95 | 0.482 | 1.57 | 5.04 |
| XGB | 3.54 | 0.124 | 1.63 | 5.04 |
| XGB corr | $\mathbf{3 . 5 0}$ | $\mathbf{0 . 0 8 8}$ | $\mathbf{1 . 6 3}$ | 5.04 |

Table 10: Decomposition of the Gamma deviance on the test set into auto-miscalibration (smaller is better), auto-resolution (larger is better) and uncertainty.
![Page 42 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p42_img1.jpg)

## Page 43
To summarise the results for our models: Overall, the corrected XGBoost model seems to be the best calibrated one and has the best out-of-sample performance. We are confident to have mitigated the risk of overly optimistic scores with the evaluation on an independent test set. The corrected Gamma GLM shows better performance than the Poisson GLM, at the cost of a slightly worse calibration conditional on Gender, cf. Table 6, and on LogWeeklyPay, cf. Table 7.

# 5.3.2. Murphy diagram 

How sensitive are our results with respect to the choice of the scoring function? We show Murphy diagrams [18], which depict different scores along a parameter. The standard way is to use the elementary scoring function, for the expectation given by $S_{\theta}(z, y)=\frac{1}{2}|\theta-y| \mathbb{1}\{\min (z, y) \leq \theta<\max (z, y)\}$, and to vary its parameter $\theta$, see Figure 9a. As we have worked with and emphasised the Tweedie deviances, we show the same type of diagram with varying Tweedie power parameter $p$ in Figure 9b. We have left out the trivial model and the OLS for better readability of the charts. One sees that the corrected XGBoost model performs best on a large range of scores, indicating that this model dominates its competitors. This is in contrast to other models like the Poisson GLM which has good scores for Tweedie powers $p$ close to 1 , corresponding to the Poisson deviance, but gets worse for larger $p$.

## Page 44
(a) Murphy diagram with elementary scores for $\theta$ from $1 \times 10^{4}$ to $1.7 \times 10^{5}$ (instead of $\min (y)$ to $\max (y)$, for better readability). The black vertical line indicates the average response on the training data set.
(b) Murphy-like diagram with Tweedie deviances across range of Tweedie powers. For better readability, the $y$-axis shows a rescaled version of the Tweedie deviance: $d_{p} \cdot \bar{y}^{p-2}$ with the mean response value $\bar{y}$.

Figure 9: Murphy diagrams
![Page 44 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p44_img1.jpg)
![Page 44 Image 2](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p44_img2.jpg)

## Page 45
# 6. Probabilistic Binary Classification 

Binary classification might be the most common task in ML, be it in theory, in ML challenges or in real world applications. While all the above theory parts fully apply here as well, we still want to highlight some special features and to present an example on probabilistic binary classification.

The term classification usually means predicting one discrete class out of a fixed set of $k$ classes, which can be identified with $\mathcal{Y}=\{0, \ldots, k-1\}$ upon renaming the class labels. Examples for such classes are client states like "healthy", "ill", "dead" or "lapsed" and "renewed". Here, we use the term probabilistic classification to underpin that we mean predicting probabilities per class. Thus, probabilistic classification amounts to probabilistic prediction for discrete response values.

In the sequel, we focus on the most relevant situation of $k=2$ classes, called binary classification.

## Summary: Binary Classification

- The response $Y$ takes only the values 0 and 1 .
- The probability for class 1 is the expectation $\mathbb{P}(Y=1 \mid \boldsymbol{X})=\mathbb{E}[Y \mid \boldsymbol{X}]$.
- Probabilistic classification models $z=m(\boldsymbol{X})$ predicting the class probability are models for the conditional expectation with canonical identification function $V(z, y)=z-y$, cf. Table 2. Strictly consistent scoring functions are Bregman functions (22).
- Deterministic classification, i.e. predicting one class only, is decision making. Ideally, decisions ought be made based on the full information of $\mathbb{P}(Y=1 \mid \boldsymbol{X})$, or, at least, on a good prediction thereof.


### 6.1. Theory

In probabilistic binary classification, the outcome space $\mathcal{Y}$ consists of dichotomous events, leading to $\mathcal{Y}=\{0,1\}$. If we assign $p=\mathbb{P}(Y=1 \mid \boldsymbol{X})$ and $1-p=\mathbb{P}(Y=0 \mid \boldsymbol{X})$, we immediately obtain $p=\mathbb{E}[Y \mid \boldsymbol{X}] \in[0,1]$. This shows the well-known fact that the entire (conditional) distribution of $Y$ is solely parametrised by the expectation of $Y$, which is a number in the interval $[0,1]$. Hence, probabilistic modelling and prediction amounts to modelling the (conditional) mean of $Y$. This is in sharp contrast to continuous responses where probabilistic predictions are much harder than point predictions. It also means that the notions of scoring functions (for the expectation) and scoring rules (for the probability distribution) coincide, cf. [30, 29, 9].

## Page 46
# 6.1.1. Probabilistic classification models 

Probabilistic models make probabilistic predictions $m(\boldsymbol{x}) \in[0,1]$. The ideal model is

$$
m^{*}(\boldsymbol{x})=\mathbb{P}(Y=1 \mid \boldsymbol{X}=\boldsymbol{x})=\mathbb{E}[Y \mid \boldsymbol{X}=\boldsymbol{x}]
$$

Since this conditional probability actually corresponds to a conditional expectation, any strictly consistent scoring function takes the form (13), which is

$$
S(z, y)=\phi(y)-\phi(z)+\phi^{\prime}(z)(z-y)+a(y), \quad z \in[0,1], y \in\{0,1\}
$$

where $\phi$ is some strictly convex function on $[0,1]$.
In this context, the squared error, arising from $\phi(z)=z^{2}$ and $a=0$, is called Brier score. Its auto-resolution-miscalibration decomposition is referred to as Brier score decomposition [57] and given in (18) upon replacing the conditioning on $\boldsymbol{X}$ by conditioning on $m(\boldsymbol{X})$. The most prominent strictly consistent score for binary classification is the $\log$ loss

$$
S_{\log }(z, y)=-y \log (z)-(1-y) \log (1-z)
$$

see Table $8 .{ }^{38}$ In contrast to the Brier score, the log loss penalises false certainty, i.e. $z=0$ while $y=1$ or $z=1$ while $y=0$, with an infinite score.

### 6.1.2. Deterministic classification: decision rule

The alternative to probabilistic models are models that make discrete predictions $m(\boldsymbol{x}) \in$ $\{0,1\}$, called decision rule or simply zero-one prediction. Hence, the target functional needs to attain values in $\{0,1\}$ only, with the most important case being a quantile. In a business context, this can easily be motivated as follows. For a decision maker, the cost $c_{0}$ of false positives (predicting $m(\boldsymbol{X})=1$ while $Y=0$ materialises) and the cost $c_{1}$ for false negatives (predicting $m(\boldsymbol{X})=0$ while $Y=1$ materialises) can be very different and very much context dependent, cf. $[74,19,33] .{ }^{39}$ With cost ratio $c=\frac{c_{0}}{c_{0}+c_{1}} \in[0,1]$, this leads to the cost-weighted misclassification error: ${ }^{40}$

$$
S_{c}(z, y)=(1-c) y(1-z)+c(1-y) z=(\mathbb{1}\{z \geq y\}-(1-c))(z-y), \quad z, y \in\{0,1\}
$$

[^0]
[^0]:    38 The $\log$ loss is known under many different names: logarithmic score, log loss, logistic loss, Bernoulli or Binomial deviance, Bernoulli log-likelihood. It gives rise to the Kullback-Leibler divergence, the Shannon entropy, and the binary cross-entropy.
    It arises from (22) upon using the strictly convex function $\phi(z)=z \log (z)+(1-z) \log (1-z)$, $z \in(0,1)$, with its continuous extension to $[0,1]$ such that $\phi(0)=\phi(1)=0$, and $a(y)=-\phi(y)$.
    39 An example is fraud detection for insurance claims. Typically, the cost of missing a fraud case (false negatives) is much higher than the cost for wrongly predicting fraud (false positives).
    40 In this context of decision theory, such loss or cost functions are called utility.

## Page 47
It turns out that this is the pinball loss of Table 8 for the $\alpha$-quantile with $\alpha=1-c$ and optimal predictions are the $\alpha$-quantiles of $\mathbb{P}(Y=1 \mid \boldsymbol{X})$ given by

$$
m^{*}(x)= \begin{cases}0, & \mathbb{P}(Y=1 \mid \boldsymbol{X}=\boldsymbol{x})<c \\ 1, & \mathbb{P}(Y=1 \mid \boldsymbol{X}=\boldsymbol{x})>c \\ 0 \text { or } 1, & \mathbb{P}(Y=1 \mid \boldsymbol{X}=\boldsymbol{x})=c\end{cases}
$$

where the threshold $c$ is identical to the cost ratio. This representation reveals that deterministic classification is only concerned about the (proximity of the) decision boundary $\mathbb{P}(Y=1 \mid \boldsymbol{X})=c$ in contrast to probabilistic classification.

In light of (24), the cost-weighted misclassification error is often written in terms of probabilistic predictions $z \in[0,1]$ where the thresholding is made explicit

$$
S_{c}(z, y)=y(1-c) \cdot \mathbb{1}\{z \leq c\}+(1-y) c \cdot \mathbb{1}\{z>c\}, \quad y \in\{0,1\}, z \in[0,1]
$$

In the case of threshold $c=\frac{1}{2}$, i.e. equal cost for false positives and false negatives, the ideal model is the median of the distribution of $Y$, conditional on $\boldsymbol{X}$. For a dichotomous response variable $Y$, the conditional median equals the conditional mode. Then, the only strictly consistent scoring function for the mode-up to equivalence-is given by

$$
S(z, y)=2 S_{\frac{1}{2}}(z, y)=\mathbb{1}\{z \neq y\}=|z-y|, \quad z, y \in\{0,1\}
$$

which is the zero-one loss of (16), [28], also known as $1-$ accuracy.

# 6.2. Practicalities 

As already outlined in the introduction "[i]deally, forecasts ought to be probabilistic, taking the form of predictive distributions over future quantities and events." [27] For binary responses, probabilistic forecasts translate to predicting $\mathbb{P}(Y=1 \mid \boldsymbol{X})=\mathbb{E}[Y \mid \boldsymbol{X}]$ with the help of which an informed decision can be made. In contrast to continuous responses, probabilistic forecasts for binary events are much simpler as they are just point forecasts for the conditional expectation. Disadvantages of deterministic classifiers that directly predict a discrete class are that they lose a lot of information and prematurely make the decision in choosing a threshold $c$ in (24) or a loss function like the zero-one loss. Further arguments in favour of probabilistic classification can be found in Chapter 1.3 of [34]. To conclude this point: "[D]eterministic forecasts suffer from two serious deficiencies. First, a forecaster or forecast system is seldom, if ever, certain which event will occur. Second, categorical forecasts do not provide users of the forecast with the information that they need to make rational decisions in uncertain situations." [56] Therefore, without use case specific reasons to do otherwise, we generally recommend the use of calibrated probabilistic classifiers, in particular for actuarial applications.

## Page 48
# 6.2.1. Miscellaneous scores 

- Accuracy: $S(z, y)=\mathbb{1}\{z=y\}$ for $z \in\{0,1\}$ or $z \in[0,1]$.

As stated above, the accuracy, is $1-$ zero-one loss. Hence, upon reversing the orientation of strict consistency (meaning that larger values are preferable), it is strictly consistent for the median / mode. As such, it fails to be a strictly proper scoring rule, even if $z$ attains values in $[0,1]$. One advantage of accuracy is the ease of communication and the direct interpretability of the average accuracy of a model, attaining values in $[0,1]$. However, we would like to caution such a use. Scoring functions are primarily tailored to forecast comparison. The calibration-resolution decomposition (17) underpins the dependence of the expected or average score on the unconditional distribution of $Y$ via the uncertainty term. For binary responses, the more imbalanced the unconditional distribution is, the smaller the uncertainty. That means it is "easier" to make accurate predictions without making use of the information contained in the features at all. If, e.g., $\mathbb{P}(Y=1)=0.95$, a calibrated trivial model maximising accuracy always predicts 1 such that an accuracy of 0.95 is achieved by this trivial model. This highlights the importance of reporting skill scores / universal coefficients of determination.

- Absolute loss $S(z, y)=|z-y|$ for $z \in\{0,1\}$ or $z \in[0,1]$.

Since the absolute loss is strictly consistent for the median and, for binary responses, the median equals the mode, the same comments as for accuracy apply here. (However, with the usual sign convention that smaller scores reflect a better predictive performance.)

- Hinge loss $S(z, y)=\max (0,1-\tilde{y} z)$ with $\tilde{y}=2 y-1 \in\{-1,+1\}$ for $z \in[-1,1]$ or $z \in \mathbb{R}$.
The hinge loss is commonly used to fit support vector machines and deterministic classification models. It is minimised by

$$
m^{\star}(x)= \begin{cases}\leq-1, & \mathbb{P}(Y=1 \mid \boldsymbol{X}=\boldsymbol{x})<1 / 2 \\ \geq 1, & \mathbb{P}(Y=1 \mid \boldsymbol{X}=\boldsymbol{x})>1 / 2 \\ \leq-1 \text { or } \geq 1, & \mathbb{P}(Y=1 \mid \boldsymbol{X}=\boldsymbol{x})=\frac{1}{2}\end{cases}
$$

We see that the additional flexibility issuing predictions on the whole real line is not really essential. The best action is actually one-to-one with (24) for $c=1 / 2$. The best model aims at modelling the conditional mode.

- Confusion matrix related scores for deterministic classification.

There is a wealth of scores derived from the confusion matrix, also known as binary contingency table, see $[64,73]$ and $[76$, Section 2]. Next to accuracy-and again being flexible about the orientation of the scores-established ones are the hit rate $(\mathrm{HR})^{41}$ (number of observations correctly predicted as positive, $z=y=1$,

[^0]
[^0]:    41 HR is also know as sensitivity, recall and true positive rate.

## Page 49
over number of positive outcomes, $y=1$ ) and false alarm rate (FAR) ${ }^{42}$ (number of observations falsely predicted as positive, $z=1$ while $y=0$, over number of negative outcomes, $y=0$ ). On a population level, the hit rate describes the conditional probability $\mathbb{P}(m(\boldsymbol{X})=1 \mid Y=1)$ and the false alarm rate describes $\mathbb{P}(m(\boldsymbol{X})=1 \mid Y=0)$.
A straightforward application of [27, Theorem 5] yields that HR is optimised by the constant model $m^{\star}(\boldsymbol{x})=1$, and equally FAR is optimised by $m^{\star}(\boldsymbol{x})=0$. Therefore, they are strictly consistent scoring functions for trivial (and uninteresting) functionals, not taking into account the distribution of the response variable. Hence, while HR, FAR and further variations (e.g., precision, $F_{1}$-score, etc.) have their place in diagnostics, reporting and decision making, they are unfit for model comparison.

- Area under the curve (AUC) for probabilistic forecasts $z \in \mathbb{R}$.

AUC is defined as the area under the ROC curve, see further below and cf. [20, 10, 32]. It has a value between 0 and 1 with the orientation the higher the better. Note, however, that a random guessing classifier has $\mathrm{AUC}=0.5$ such that sensible classifiers should have $\mathrm{AUC}>0.5$. While the AUC can be appealing when it comes to diagnostics, its deficiency is that it ignores calibration of the forecast, basically only assessing its resolution or discrimination, [76, Section 4.7]. In particular, equation (3.4) in [10] illustrates that the AUC ignores the marginal distribution of $Y$. Hence, it cannot be a proper scoring rule for a binary response. This coincides with the findings of [10], who also formulated partial exceptions where propriety holds.

# 6.2.2. Graphical tools 

- Reliability diagrams

A good diagnostic tool for assessing auto-calibration of binary responses are reliability diagrams [17] which draw observed outcomes vs predicted values. "In a nutshell, [...] [a probabilistic] classifier is calibrated or reliable if, when looking back at a series of extant forecasts, the conditional event frequencies match the predictive probabilities." [17]

- Receiver operating characteristic (ROC)

The ROC is a graphical tool illustrating the trade-off when choosing different cost ratios or thresholds $c$, see [20].
Let $m(\boldsymbol{X}) \in[0,1]$ be a probabilistic model. Following [32], the ROC curve is a plot of the hit rate against the false alarm rate. To that end, one first turns the probabilistic forecast $m(\boldsymbol{X})$ into a deterministic classification, using a threshold $c \in[0,1]$. So the classification will be 1 if $m(\boldsymbol{X})>c$. Then we can define the hit rate at level $c, \operatorname{HR}(c)$, and the false alarm rate at level $c, \operatorname{FAR}(c)$, as

$$
\operatorname{HR}(c)=\mathbb{P}(m(\boldsymbol{X})>c \mid Y=1), \quad \operatorname{FAR}(c)=\mathbb{P}(m(\boldsymbol{X})>c \mid Y=0)
$$

[^0]
[^0]:    42 FAR is also known as probability of false detection, fall-out and false positive rate. It equals minus specificity, selectivity, or true negative rate

## Page 50
The ROC curve is then formally defined as the graph

$$
\{(\operatorname{FAR}(c), \operatorname{HR}(c)): c \in[0,1]\} \subset[0,1]^{2}
$$

This definition on the population level has a clear counterpart on the sample level.

# 6.2.3. Imbalanced classes 

There is a large strand of literature about the so-called imbalanced learning problem [37]. For binary classification, this means that one class significantly outnumbers the other one. Typically, main interest is in the rare class $Y=1$, called minority class, with $\mathbb{P}(Y=1) \ll \mathbb{P}(Y=0)$, e.g., with a ratio of $1: 10,1: 1000$ or even more unbalanced. ${ }^{43}$

Poor models in this setting are often a result of - any combination of-fitting deterministic classifiers, using re-sampling or re-weighting methods to balance class frequencies in the training data and evaluating the model with a score such as accuracy. As mentioned above, accuracy is a poor score for model comparison, especially so for imbalanced classes where the cost-ratio $c$, if known, is likely far away from $1 / 2$. The frequently encountered practice of over-sampling the minority class or under-sampling the majority class might help to get better (accuracy) scores, but it does not help with the underlying problem: If the minority class is very rare in absolute terms, no matter the size of the training set, one has effectively a small sample problem. No re-sampling technique will magically generate more information out of the few cases with the rare class. ${ }^{44}$ Finally, we generally recommend probabilistic classifiers based on consistent scoring rules over deterministic classifiers. For instance, a well specified logistic regression model with logit link and intercept fulfils (9) and therefore, at least on the training set, is guaranteed to predict the class probabilities according to their observed frequencies. We refer to [47] for more information about logistic regression with rare events, e.g., data collection, finite sample corrections and correcting estimates.

### 6.3. Example: Binary Classification of Customer Churn

As an example for binary classification, we take the Telco Customer Churn data set ${ }^{45}$. Each of the $n=7043$ rows represents a customer of a telecommunication company and the response variable $Y=($ Churn $=$ "Yes") indicates if the customer left within the last month. For the sake of brevity, we refrain from repeating the detailed steps of the regression example and instead focus on the new aspects of this classification task.

Listing 3 shows the short preprocessing and the features used for modelling.

[^0]
[^0]:    43 An example are Covid-19 cases. Main interest is in the minority group of infected persons, luckily outnumbering the group of not infected people by a large margin.
    44 Let us play coin toss with a probability $p$ for $Y=1=$ "head". Every toss generates a data point adding the Shannon entropy $H=-p \log _{2} p-(1-p) \log _{2}(1-p) . H$ is maximised for $p=1 / 2$ giving $H=1$ bit of information and minimised by $p \in\{0,1\}$ giving $H=0$ bits. Data points for imbalanced classes therefore have little information content.
    45 https://www.openml.org/d/42178

## Page 51
```
library(tidyverse)
library(OpenML)
df_origin <- getOMLDataSet(data.id = 42178L)
df <- tibble(df_origin$data)
df[df == "No_internet_service" | df == "No_phone_service"] <- "No"
df <- df %>%
    mutate(
        LogTotalCharges = log(as.numeric(TotalCharges)),
        Churn = (Churn == "Yes") + 0,
    ) %>%
    replace.na(list(LogTotalCharges = median(.$LogTotalCharges, na.rm = TRUE))) %>%
    mutate_if(is.character, as.factor)
y_var <- "Churn"
x_continuous <- c("tenure", "MonthlyCharges", "LogTotalCharges")
x_discrete <- setdiff(colnames(select_if(df, is.factor)),
                                    c("customerID", y_var, "TotalCharges"))
x_vars <- c(x_continuous, x_discrete)
```

For a short exploratory data analysis, we refer to Subsection A.2.
We use a stratified train-test split:

```
library(splitTools)
set.seed(34621L)
inds <- partition(df$Churn, p = c(train = 0.75, test = 0.25))
train <- df[inds$train, ]
test <- df[inds$test, ]
y_train <- train[[y_var]]
y_test <- test[[y_var]]
```

This guarantees the same average churn frequency on both sets. We obtain $\bar{y}=0.265$ on the training and $\bar{y}=0.266$ on the test set. This helps to better compare results across both sets. ${ }^{46}$

We train four different models:

- Trivial model with $m_{\text {trivial }}(\boldsymbol{x})=0.2652907$;
- Logistic regression (LogReg), i.e. a GLM with binomial family and logistic link function;
form <- reformulate(x_vars, y_var)
fit_glm <- glm(form, data = train, family = binomial())
- Random forest (RF) with R package ranger;

```
fit_rf <- ranger(
    form,
    data = train,
    probability = TRUE,
```

[^0]
[^0]:    46 If those numbers deviated too much, the i.i.d. assumption would clearly be violated.

## Page 52
|  | $\bar{V}(m ; D)$ |  |
| model | $D=$ train | $D=$ test |
| --- | --- | --- |
| Trivial | 0 | $\mathbf{- 0 . 0 0 0 3 1 7}$ |
| LogReg | 0 | -0.00533 |
| RF | 0.00117 | -0.00329 |
| XGBoost | 0.000483 | -0.00523 |

Table 11: Assessment of classifiers' unconditional calibration in terms of bias.

```
seed = 774,
min.node.size = 30,
oob.error = TRUE
}
```

- XGBoost model with log loss as objective function, logit link function and optimised hyperparameters via cross-validation similar to the regression case.

The unconditional calibration with $V(z, y)=z-y$ is summarised in Table 11. The GLM with canonical link, i.e. the logistic regression, once more shows the balance property on the training set. On the test set, the trivial model has quite a good calibration and, among the feature using models, the random forest is the best unconditionally calibrated one.

As graphical tool to check auto-calibration, we show reliability diagrams on the test set with the CORP approach of [17] in Figure 10. The CORP approach essentially

Figure 10: Reliability diagrams. The $x$-axis shows predictions/forecast values, the $y$ axis conditional event probabilities (CEP). At the bottom of each plot, the histogram of forecast values is drawn. The values in the boxes are the decomposition of the $\log$ loss (23) into miscalibration (MCB), discrimination (DSC) and uncertainty (UNC), such that $\bar{S}_{\log }=\mathrm{MCB}-\mathrm{DSC}+\mathrm{UNC}$; see also (17).
![Page 52 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p52_img1.jpg)

## Page 53
Figure 11: Performance on training and validation data in terms of mean log loss (smaller is better), its relative reduction R* (larger is better).

performs the binning in an optimal way such that the conditional event probabilities (CEP), which are binned observed frequencies, are isotonic. The random forest seems to be the best auto-calibrated one. This is confirmed by the score decomposition of the log loss (23) according to the auto-calibration variant of (17) given in Figure 10. The lowest miscalibration (MCB) is obtained by the random forest. On the other hand, the logistic regression has the highest discriminative power (DSC).

Finally, we assess the predictive performance with the log loss and the relative reduction in log loss w.r.t. the trivial model, R*, see Table 12 and Figure 11. The random forest

|  | mean log loss |  | R* |  | AUC |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Model | train | test | train | test | train | test |
| Trivial | 0.579 | 0.579 | 0 | 0 | 0.500 | 0.500 |
| LogReg | 0.415 | $\mathbf{0 . 3 8 2}$ | 0.282 | $\mathbf{0 . 3 4 0}$ | 0.845 | $\mathbf{0 . 8 7 5}$ |
| RF | 0.318 | 0.390 | 0.450 | 0.325 | 0.935 | 0.868 |
| XGB | 0.401 | 0.390 | 0.306 | 0.327 | 0.859 | 0.871 |

Table 12: Performance on training and validation data in terms of mean log loss (smaller is better), its relative reduction R* and AUC (for both larger is better).
clearly shows overfitting as it has the lowest mean log loss on the training set but also the second highest one behind the trivial model on the test set. This is not surprising as random forests are typically built of very deep trees. The XGBoost model performs a touch better than the random forest on the test set. Note, however, that this time no correction factor was required. Despite the fact that we did not put much effort in the logistic regression, e.g., we did not include any interaction terms nor splines
![Page 53 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p53_img1.jpg)

## Page 54
Figure 12: Murphy diagram with elementary scores for $\theta$ from 0 to 1. The black vertical line indicates the average response on the training data set.
or polynomials of degree two or higher, it ranks on top of all other models regarding predictive performance. A possible explanation for this ranking is the modest size of the data set.

We also show the AUC. As the models show different calibration, their ranking in terms of AUC could be very different from the ranking based on log loss. Coincidentally, AUC shows the same out-of-sample ranking as log loss. This can be explained by the score decomposition of the log loss in Figure 10. The discrimination components DSC are an order of magnitude larger than the miscalibration components MCB and give the same ranking as according to the log loss. Despite the appeal of AUC, we generally prefer to evaluate the models with a strictly consistent scoring function, i.e. log loss in our case.

We conclude this example with the Murphy diagram in Figure 12. We observe the small values of the random forest on the training set for a large range of scores. From the right-hand side of the figure, we are visually inclined to award the logistic regression with the best out-of-sample performance. However, the differences out-of-sample seem to be relatively small such that we refrain from a definite answer as to what model exhibits the best predictive accuracy measured by a wide range of consistent scoring functions.

# 7. Conclusion 

In this user guide, we have elaborated on best statistical practice in model assessment and model comparison, important tasks in Machine Learning and actuarial science. We have argued that for both tasks, specifying the modelling target in the form of a statistical functional is crucial. The tools for calibration assessment and model comparisonidentification functions and scoring functions - need to be chosen in line with the modelling target at hand. Calibration assessment via strict identification functions checks whether
![Page 54 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p54_img1.jpg)

## Page 55
there are any systematic errors in the predictive model. On the other hand, strictly consistent scoring functions simultaneously encourage good calibration and discrimination ability, honouring the information content of a model. The methodology has been illustrated with running examples in regression and in binary classification, based on two (almost) real world data sets. Making a clear distinction between learning (model building) and model evaluation, we have stressed the importance of thorough train-test split of the data.

Clearly, it was not possible to elaborate on all practically relevant aspects in this field. For instance, we have entirely omitted the situation of missing or incomplete data. Examples from insurance are IBNR (incurred but not yet reported) for frequency models or RBNS (reported but not settled) for claims severity. Moreover, we have mainly focused on cross-sectional data, only providing some comments on data with serial dependence.

While the majority of the used guide at hand is devoted to a definition of what predictive performance is and how it can be assessed, we would like to close it by remarking that there are sometimes other important (and sometimes conflicting) goals in modelling such as calibration, explainability [51], impartiality [44], or robustness of predictions [53].

# Acknowledgements 

The authors are very grateful to Jürg Schelldorfer and Mario Wüthrich as well as to Timo Dimitriadis, Daniel Meier and Marc-Oliver Pohle for their comprehensive reviews and their innumerable inputs which led to substantial improvements of this work. Christian Lorentzen and Michael Mayer like to thank their company la Mobilière for its support.

## References

[1] S. Arlot and A. Celisse. "A survey of cross-validation procedures for model selection". In: Statistics Surveys 4 (2010), pp. 40 -79. DOI: 10.1214/09-ss054. arXiv: 0907 . 4728 [math.ST].
[2] P. L. Bartlett, P. M. Long, G. Lugosi, and A. Tsigler. "Benign overfitting in linear regression". In: Proceedings of the National Academy of Sciences 117.48 (2020), pp. 30063-30070. DOI: 10.1073/pnas. 1907378117.
[3] P. L. Bartlett and S. Mendelson. "Rademacher and Gaussian Complexities: Risk Bounds and Structural Results". In: Computational Learning Theory. Ed. by D. Helmbold and B. Williamson. Berlin, Heidelberg: Springer Berlin Heidelberg, 2001, pp. 224-240. DOI: 10.1007/3-540-44581-1_15. URL: http://www.jmlr.org/p apers/volume3/bartlett02a/bartlett02a.pdf.
[4] S. Bates, T. Hastie, and R. Tibshirani. "Cross-validation: what does it estimate and how well does it do it?" In: (2021). arXiv: 2104.00673 [stat.ME].

## Page 56
[5] M. Belkin, D. Hsu, S. Ma, and S. Mandal. "Reconciling modern machine-learning practice and the classical bias-variance trade-off". In: Proceedings of the National Academy of Sciences 116.32 (2019), pp. 15849-15854. DOI: 10.1073/pnas. 190307 0116 .
[6] M. Belkin, D. Hsu, and J. Xu. "Two Models of Double Descent for Weak Features". In: SIAM Journal on Mathematics of Data Science 2.4 (2020), pp. 1167-1180. ISSN: 2577-0187. DOI: 10.1137/20m1336072. arXiv: 1903.07571 [math.ST].
[7] R. R. Bouckaert and E. Frank. "Evaluating the Replicability of Significance Tests for Comparing Learning Algorithms". In: Advances in Knowledge Discovery and Data Mining. Springer Berlin Heidelberg, 2004, pp. 3-12. DOI: 10.1007/978-3-5 40-24775-3_3. URL: http://www.cs.waikato.ac.nz/ ml/publications/2004 /bouckaert-frank.pdf.
[8] J. R. Brehmer and T. Gneiting. "Scoring interval forecasts: Equal-tailed, shortest, and modal interval". In: Bernoulli 27.3 (2021), pp. 1993-2010. DOI: 10.3150/20BEJ1298. arXiv: 2007.05709 [math.ST].
[9] A. Buja, W. Stuetzle, and Y. Shen. Loss Functions for Binary Class Probability Estimation and Classification: Structure and Applications. Tech. rep. University of Pennsylvania, 2005. URL: http://www-stat.wharton.upenn.edu/ buja /PAPERS/paper-proper-scoring.pdf.
[10] S. Byrne. "A note on the use of empirical AUC for evaluating probabilistic forecasts". In: Electronic Journal of Statistics 10.1 (2016), pp. 380-393. DOI: 10.1214/16EJS1109.
[11] T. Chen and C. Guestrin. "XGBoost: A Scalable Tree Boosting System". In: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. KDD '16. San Francisco, California, USA: Association for Computing Machinery, 2016, pp. 785-794. DOI: 10.1145/2939672.2939785. URL: http://doi.acm.org/10.1145/2939672.2939785.
[12] Y. Dar, V. Muthukumar, and R. G. Baraniuk. "A Farewell to the Bias-Variance Tradeoff? An Overview of the Theory of Overparameterized Machine Learning". In: (2021). arXiv: 2109.02355 [stat.ML].
[13] M. H. A. Davis. "Verification of internal risk measure estimates". In: Statistics $\mathcal{G}$ Risk Modeling 33.3-4 (2016), pp. 67-93. DOI: 10.1515/strm-2015-0007.
[14] A. P. Dawid and V. G. Vovk. "Prequential probability: principles and properties". In: Bernoulli 5.1 (1999), pp. 125-162. DOI: bj/1173707098.
[15] F. X. Diebold and R. S. Mariano. "Comparing Predictive Accuracy". In: Journal of Business $\mathcal{G}$ Economic Statistics 13.1 (1995), pp. 253-265. DOI: 10.2307/1392185. URL: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.454.4 490\&rep=rep1\&type=pdf.
[16] T. Dimitriadis, T. Fissler, and J. F. Ziegel. "The Efficiency Gap". In: arXiv (2020). arXiv: 2010.14146 [math.ST].

## Page 57
[17] T. Dimitriadis, T. Gneiting, and A. I. Jordan. "Stable reliability diagrams for probabilistic classifiers". In: Proceedings of the National Academy of Sciences 118.8 (2021), e2016191118. DOI: 10.1073/pnas. 2016191118.
[18] W. Ehm, T. Gneiting, A. I. Jordan, and F. Krüger. "Of quantiles and expectiles: consistent scoring functions, Choquet representations and forecast rankings". In: Journal of the Royal Statistical Society: Series B (Statistical Methodology) 78.3 (2016), pp. 505-562. DOI: 10.1111/rssb.12154. arXiv: 1503.08195 [math.ST].
[19] C. Elkan. "The Foundations of Cost-Sensitive Learning". In: Proceedings of the 17th International Joint Conference on Artificial Intelligence. IJCAI'01. San Francisco, CA, USA: Morgan Kaufmann Publishers Inc., 2001, pp. 973-978. ISBN: 978-1-55860-812-2. URL: https://citeseerx.ist.psu.edu/viewdoc/download?doi=1 0.1.1.29.514\&rep=rep1\&type=pdf.
[20] T. Fawcett. "An introduction to ROC analysis". In: Pattern Recognition Letters 27.8 (2006), pp. 861-874. DOI: 10.1016/j.patrec.2005.10.010.
[21] T. Fissler, F. Krüger, and M.-O. Pohle. "Regression Diagnostics via Generalized Residuals". Mimeo. 2022.
[22] T. Fissler, M. Merz, and M. V. Wüthrich. "Deep Quantile and Deep Composite Model Regression". In: arXiv (2021). arXiv: 2112.03075 [stat.ME].
[23] T. Fissler, R.Frongillo, J. Hlavinová, and B. Rudloff. "Forecast evaluation of quantiles, prediction intervals, and other set-valued functionals". In: Electronic Journal of Statistics 15.1 (2021), pp. 1034-1084. DOI: 10.1214/21-EJS1808.
[24] T. Fissler and J. F. Ziegel. "Higher order elicitability and Osband's principle". In: The Annals of Statistics 44.4 (2016), pp. 1680-1707. DOI: 10.1214/16-AOS1439.
[25] T. Fissler and J. F. Ziegel. "Order-sensitivity and equivariance of scoring functions". In: Electronic Journal of Statistics 13.1 (2019), pp. 1166-1211. DOI: 10.1214/19EJS1552.
[26] S. Geman, E. Bienenstock, and R. Doursat. "Neural Networks and the Bias/Variance Dilemma". In: Neural Computation 4.1 (Jan. 1992), pp. 1-58. DOI: 10.1162/neco .1992.4.1.1.
[27] T. Gneiting. "Making and Evaluating Point Forecasts". In: Journal of the American Statistical Association 106.494 (2011), pp. 746-762. DOI: 10.1198/jasa.2011.r1 0138. arXiv: 0912.0902 [math].
[28] T. Gneiting. "When is the mode functional the Bayes classifier?" In: Stat 6.1 (2017), pp. 204-206. DOI: 10.1002/sta4.148. arXiv: 1704.08979 [math.ST].
[29] T. Gneiting and M. Katzfuss. "Probabilistic Forecasting". In: Annual Review of Statistics and Its Application 1.1 (2014), pp. 125-151. DOI: 10.1146/annurev-st atistics-062713-085831.

## Page 58
[30] T. Gneiting and A. E. Raftery. "Strictly Proper Scoring Rules, Prediction, and Estimation". In: Journal of the American Statistical Association 102 (2007), pp. 359378. DOI: 10.1198/016214506000001437. URL: http://www.stat.washington .edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf.
[31] T. Gneiting and J. Resin. "Regression Diagnostics meets Forecast Evaluation: Conditional Calibration, Reliability Diagrams, and Coefficient of Determination". In: arXiv (2021). arXiv: 2108.03210 [stat.ME].
[32] T. Gneiting and P. Vogel. "Receiver operating characteristic (ROC) curves: equivalences, beta model, and minimum distance estimation". In: arXiv (2021). DOI: 10.1007/s10994-021-06115-2. arXiv: 1809.04808 [stat.ME].
[33] C. W. J. Granger and M. Hashem Pesaran. "Economic and Statistical Measures of Forecast Accuracy". In: Journal of Forecasting 19 (1999), pp. 537-560. DOI: 10.1002/1099-131X(200012)19:7<537::AID-FOR769>3.0.CO;2-G. URL: https://www.repository.cam.ac.uk/bitstream/1810/421/1/gp1999.pdf.
[34] F. E. Harrell. Regression Modeling Strategies. 2nd ed. Springer Series in Statistics. Springer International Publishing Switzerland 2015, 2015. ISBN: 978-3-319-19424-0. DOI: 10.1007/978-3-319-19425-7.
[35] T. Hastie, R. Tibshirani, and J. Friedman. The Elements of Statistical Learning. Springer Series in Statistics. New York, NY, USA: Springer New York Inc., 2001. URL: https://web.stanford.edu/ hastie/ElemStatLearn/.
[36] Trevor Hastie, Andrea Montanari, Saharon Rosset, and Ryan J. Tibshirani. "Surprises in High-Dimensional Ridgeless Least Squares Interpolation". In: (2020). arXiv: 1903.08560 [math.ST].
[37] H. He and Y. Ma, eds. Imbalanced Learning: Foundations, Algorithms, and Applications. John Wiley \& Sons, Inc., 2013. ISBN: 978-1-118-07462-6. DOI: 10.1002/9 781118646106.
[38] C. Heinrich-Mertsching and T. Fissler. "Is the mode elicitable relative to unimodal distributions?" In: Biometrika (forthcoming) (2021). DOI: 10.1093/biomet/asab 065. arXiv: 2109.00464.
[39] A. Henzi and J. F. Ziegel. "Valid sequential inference on probability forecast performance". In: arXiv (2021). arXiv: 2103.08402 [stat.ME].
[40] H. Holzmann and M. Eulert. "The role of the information set for forecasting - with applications to risk management". In: The Annals of Applied Statistics 8 (2014), pp. 79-83. DOI: 10.1214/13-AOAS709.
[41] P. J. Huber. "Robust Estimation of a Location Parameter". In: The Annals of Mathematical Statistics 35.1 (Mar. 1964), pp. 73-101. DOI: 10.1214/aoms/11777 03732 .
[42] P. J. Huber and E. M. Ronchetti. Robust Statistics. Second. Hoboken, New Jersey: John Wiley \& Sons, Inc., 2009.

## Page 59
[43] R. J. Hyndman and G. Athanasopoulos. "Forecasting: principles and practice". In: OTexts: Melbourne, Australia, 2021. URL: https://otexts.com/fpp3.
[44] K. D. Johnson, D. P. Foster, and R. A. Stine. "Impartial Predictive Modeling and the Use of Proxy Variables". In: (2016). arXiv: 1608.00528 [stat.ME].
[45] Alexander I. Jordan, Anja Mühlemann, and Johanna F. Ziegel. "Characterizing the optimal solutions to the isotonic regression problem for identifiable functionals". In: Annals of the Institute of Statistical Mathematics 74.3 (2022), pp. 489-514. DOI: 10.1007/s10463-021-00808-0.
[46] B. Jørgensen. The Theory of Dispersion Models. London: Chapman and Hall/CRC, 1997. ISBN: 978-0-412-99711-2.
[47] G. King and L. Zeng. "Logistic Regression in Rare Events Data". In: Political Analysis 9.2 (2001), pp. 137-163. DOI: 10.1093/oxfordjournals.pan.a004868.
[48] D. P. Kroese, Z. I. Botev, T. Taimre, and R. Vaisman. Data Science and Machine Learning: Mathematical and Statistical Methods. Chapman \& Hall/CRC machine learning \& pattern recognition. Boca Raton: CRC Press, 2019. ISBN: 978-1-138-49253-0. URL: https://people.smp.uq.edu.au/DirkKroese/DSML/.
[49] Fabian Krüger and Johanna F. Ziegel. "Generic Conditions for Forecast Dominance". In: Journal of Business 6 Economic Statistics 39.4 (2021), pp. 972-983. DOI: 10.1 080/07350015.2020.1741376. URL: https://doi.org/10.7892/boris.141834.
[50] Sebastian Lerch, Thordis L. Thorarinsdottir, Francesco Ravazzolo, and Tilmann Gneiting. "Forecaster's Dilemma: Extreme Events and Forecast Evaluation". In: Statist. Sci. 32.1 (2017), pp. 106-127. DOI: 10.1214/16-STS588. URL: https: //projecteuclid.org:443/euclid.ss/1491465630.
[51] C. Lorentzen and M. Mayer. "Peeking into the Black Box: An Actuarial Case Study for Interpretable Machine Learning". In: SSRN Manuscript ID 3595944 (2020). DOI: $10.2139 /$ ssrn. 3595944.
[52] U. von Luxburg and B. Schoelkopf. "Statistical Learning Theory: Models, Concepts, and Results". In: (2008). arXiv: 0810.4752 [stat.ML].
[53] M. Mayer, S. C. Bourassa, M. Hoesli, and D. Scognamiglio. "Estimation and Updating Methods for Hedonic Valuation". English. In: Journal of European Real Estate Research 12.1 (2019), pp. 134-150. DOI: 10.1108/JERER-08-2018-0035. URL: https://ssrn.com/abstract=3300193.
[54] T. M. Mitchell. Machine Learning. 1st ed. USA: McGraw-Hill, Inc., 1997. ISBN: 978-0-07-042807-2.
[55] A. H. Murphy and H. Daan. "Forecast Evaluation". In: Probability, Statistics and Decision Making in the Atmospheric Sciences. Ed. by A. H. Murphy and R. W. Katz. Westview Press, Boulder, Colorado, 1985, pp. 379-437.
[56] A. H. Murphy and R. L. Winkler. "Probability Forecasting in Meterology". In: Journal of the American Statistical Association 79.387 (1984), pp. 489-500. ISSN: 01621459. DOI: 10.2307/2288395.

## Page 60
[57] Allan H. Murphy. "A New Vector Partition of the Probability Score". In: Journal of Applied Meteorology and Climatology 12.4 (1973), pp. 595-600. DOI: 10.1175/1 520-0450(1973)012<0595:ANVPOT>2.0.CO;2.
[58] C. Nadeau and Y. Bengio. "Inference for the Generalization Error". In: Machine Learning 52.3 (2003), pp. 239-281. DOI: 10.1023/a:1024068626366.
[59] B. Neyshabur, R. Tomioka, and N. Srebro. "In Search of the Real Inductive Bias: On the Role of Implicit Regularization in Deep Learning". In: (2015). arXiv: 1412.6614 [cs.LG].
[60] N. Nolde and J. F. Ziegel. "Elicitability and backtesting: Perspectives for banking regulation". In: The Annals of Applied Statistics 11.4 (2017), pp. 1833-1874. DOI: 10.1214/17-AOAS1041.
[61] K. H. Osband. "Providing Incentives for Better Cost Forecasting". PhD thesis. University of California, Berkeley, 1985. DOI: 10.5281/zenodo. 4355667.
[62] A. J. Patton. "Volatility forecast comparison using imperfect volatility proxies". In: Journal of Econometrics 160.1 (2011), pp. 246-256. DOI: 10.1016/j.jeconom. 20 10.03.034. URL: http://public.econ.duke.edu/ ap172/Patton_vol_proxie s_JoE_2011.pdf.
[63] M.-O. Pohle. "The Murphy Decomposition and the Calibration-Resolution Principle: A New Perspective on Forecast Evaluation". In: arXiv (2020). arXiv: 2005.01835 [stat.ME].
[64] D. M. W. Powers. Evaluation: From Precision, Recall and F-Factor to ROC, Informedness, Markedness $\mathcal{E}$ Correlation. Tech. rep. SIE-07-001. School of Informatics and Engineering Flinders University, Adelaide, 2007. arXiv: 2010.16061 [cs.LG].
[65] S. Raschka. "Model Evaluation, Model Selection, and Algorithm Selection in Machine Learning". In: arXiv (2018). arXiv: 1811.12808 [cs.LG].
[66] D. R. Roberts, V. Bahn, S. Ciuti, M. S. Boyce, J. Elith, G. Guillera-Arroita, S. Hauenstein, J. J. Lahoz-Monfort, B. Schröder, W. Thuiller, D. I. Warton, B. A. Wintle, F. Hartig, and C. F. Dormann. "Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure". In: Ecography 40.8 (2017), pp. 913-929. DOI: 10.1111/ecog. 02881.
[67] S. J. Russell and P. Norvig. Artificial Intelligence: A Modern Approach. Third. Prentice Hall, 2009. ISBN: 978-0-13-604259-4.
[68] M. Saerens. "Building cost functions minimizing to some summary statistics". In: IEEE Transactions on Neural Networks 11.6 (2000), pp. 1263-1271. DOI: $10.1109 / 72.883416$.
[69] M. Schnaubelt. A comparison of machine learning model validation schemes for non-stationary time series data. eng. FAU Discussion Papers in Economics 11/2019. Nürnberg, 2019. URL: http://hdl.handle.net/10419/209136.

## Page 61
[70] S. Shalev-Shwartz and S. Ben-David. Understanding Machine Learning. Cambridge University Press, 2014. DOI: 10.1017/cbo9781107298019. URL: https://www.c se.huji.ac.il/ shais/UnderstandingMachineLearning.
[71] R. M. Stein. "Benchmarking default prediction models: pitfalls and remedies in model validation". In: The Journal of Risk Model Validation 1.1 (2007), pp. 77-113. DOI: 10.21314/JRMV.2007.002. URL: http://www.rogermstein.com/wp-conte nt/uploads/BenchmarkingDefaultPredictionModels_TR030124.pdf.
[72] I. Steinwart, C. Pasin, R. Williamson, and S. Zhang. "Elicitation and Identification of Properties". In: JMLR Workshop Conf. Proc. 35 (2014), pp. 1-45. URL: http: //proceedings.mlr.press/v35/steinwart14.html.
[73] A. Tharwat. "Classification assessment methods". In: New England Journal of Entrepreneurship 17.1 (2020), pp. 168-192. DOI: 10.1016/j.aci.2018.08.003.
[74] J. C. Thompson and G. W. Brier. "The Economic Utility of Weather Forecasts". In: Monthly Weather Review 83.11 (1955), pp. 249 -253. DOI: 10.1175/1520-049 3(1955)083<0249:TEUOWF>2.0.CO;2.
[75] M. C. K. Tweedie. "An index which distinguishes between some important exponential families". In: vol. Proceedings of the Indian Statistical InstituteGolden Jubilee International Conference. Statistics: Applications and New Directions. 1984, pp. 579-604.
[76] D. S. Wilks. "Forecast Verification". In: Statistical Methods in the Atmospheric Sciences. 3rd ed. International Geophysics Series. Elsevier, 2011. Chap. 8, pp. 301394. ISBN: 978-0-12-385022-5. DOI: 10.1016/B978-0-12-385022-5.00008-7.
[77] J. Witkowski, R. Freeman, J. Wortman Vaughan, D. M. Pennock, and A. Krause. "Incentive-Compatible Forecasting Competitions". In: arXiv (2021). arXiv: 2101.0 1816 [cs.GT].
[78] M. V. Wüthrich and M. Merz. "Statistical Foundations of Actuarial Learning and its Applications". In: SSRN Manuscript ID 3822407 (Nov. 2021). DOI: 10.2139/s srn. 3822407.
[79] C. Zhang, S. Bengio, M. Hardt, B. Recht, and O. Vinyals. "Understanding deep learning requires rethinking generalization". In: (2017). arXiv: 1611.03530 [cs.LG].

# A. Exploratory Data Analysis 

## A.1. Regression: Workers' Compensation Data Set

See Figures 13, 14, 15 and 16.

## Page 62
Figure 13: Histograms of categorical features of Workers' Compensation data set.


Figure 14: Histograms of numerical features of Workers' Compensation data set.
![Page 62 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p62_img1.jpg)
![Page 62 Image 2](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p62_img2.jpg)

## Page 63
Figure 15: Boxplots of response UltimateIncurredClaimCost conditional on categorical features of Workers' Compensation data set.

Figure 16: Density plots of response UltimateIncurredClaimCost conditional on numerical features Workers' Compensation data set.
![Page 63 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p63_img1.jpg)
![Page 63 Image 2](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p63_img2.jpg)

## Page 64
# A.2. Classification: Telco Customer Churn Data Set 

See Figures 17, 18, 19 and 20.

Figure 17: Histograms of categorical features of Telco Customer Churn data set.
![Page 64 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p64_img1.jpg)

## Page 65
Figure 18: Histograms of numerical features of Telco Customer Churn data set.

Figure 19: Mean response Churn conditional on categorical features of Telco Customer Churn data set.
![Page 65 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p65_img1.jpg)
![Page 65 Image 2](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p65_img2.jpg)

## Page 66
Figure 20: Density plots of response Churn conditional on numerical features of Telco Customer Churn data set.

# B. Tweedie Deviance and Homogeneous Bregman Functions 

In Eq. (20) of [27], originally in [62], a rich family of homogeneous Bregman functions with parameter $b \in \mathbb{R}$ is introduced for the positive real line $z, y \in \mathbb{R}_{+}$as

$$
S_{b}(z, y)= \begin{cases}\frac{1}{b(b-1)}\left(y^{b}-z^{b}\right)-\frac{1}{b-1} z^{b-1}(y-z) & b \in \mathbb{R} \backslash\{0,1\} \\ y \log \frac{y}{z}-y+z & b=1 \\ \frac{y}{z}-\log \frac{y}{z}-1 & b=0\end{cases}
$$

Up to a multiplicative constant, this coincides with the homogeneous scores in Table 8 for $b=a>1$.

The Tweedie distributions $T w_{p}(\mu, \varphi)$ [75] are a subfamily of the exponential dispersion family (EDF), see [46, 78], and are characterised by their mean-variance relation $\operatorname{Var}[Y]=$ $\varphi \cdot \mu^{p}$ with mean $\mu=\mathbb{E}[Y]$, dispersion parameter $\varphi>0$ and power $p$. Their deviance is given by

$$
d_{p}(y, \mu)=2 \cdot \begin{cases}\frac{\max \left(0, y^{2-p}\right)}{(1-p) \cdot(2-p)}-\frac{y \cdot \mu^{1-p}}{1-p}+\frac{\mu^{2-p}}{2-p} & p \in \mathbb{R} \backslash(0,1] \cup\{2\} \\ y \log \frac{y}{\mu}-y+\mu & p=1 \\ \frac{y}{\mu}-\log \frac{y}{\mu}-1 & p=2\end{cases}
$$

with valid domains:
![Page 66 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p66_img1.jpg)

## Page 67
| response $y$ | mean $\mu$ | power $p$ |
| :-- | :-- | :-- |
| $y \in \mathbb{R}$ | $\mu \in \mathbb{R}_{+}$ | $p<0$ |
| $y \in \mathbb{R}$ | $\mu \in \mathbb{R}$ | $p=0$ |
| $y \in \mathbb{R}_{+} \cup\{0\}$ | $\mu \in \mathbb{R}_{+}$ | $1 \leq p<2$ |
| $y \in \mathbb{R}_{+}$ | $\mu \in \mathbb{R}_{+}$ | $p \geq 2$ |

Well-known members are the Normal distribution $(p=0)$, the Poisson distribution $(p=1)$, the Gamma distribution $(p=2)$, and the inverse Gaussian distribution $(p=3)$. Remarkably, for $p \in(0,1)$, no Tweedie distribution exists while the Bregman function $S_{b}$ is defined for all $b \in \mathbb{R}$.

On the common domains of $y$ and $z$, it holds that

$$
d_{p}(y, x)=2 \cdot S_{2-p}(x, y)
$$

This indicates that Tweedie deviances for $p \in(0,1)$ may be used as consistent scoring function for the expectation, although no distribution exists for this parameter range. On the other hand, the domain of $z$ for a Bregman function can be extended to allow for $z=0$ for $0<b \leq 1$.

Furthermore, Tweedie distributions are the only distributions within the EDF that are closed under scale transformations [46]: If $Y \sim T w_{p}(\mu, \varphi)$ then $t Y \sim T w_{p}\left(t \mu, t^{2-p} \varphi\right)$ for any $t>0$. We recover the degree of homogeneity of Tweedie deviances, $h=2-p$, as the law of transformation of the dispersion parameter of Tweedie random variables under scale transformations.

# C. Simulation study on efficiency 

As outlined in Subsubsection 5.1.6, the coefficient of variation $\operatorname{CV}(Z)=\left(\operatorname{Var}[Z] / \mathbb{E}[Z]^{2}\right)^{1 / 2}$, where $Z$ is the score difference, determines the asymptotic power of a Diebold-Mariano test. To be more precise and to take into account the sample size $n$ of the test data set, the power is inversely linked to the coefficient of variation of the average score difference

$$
\bar{Z}_{n}=\frac{1}{n} \sum_{i=1}^{n} S\left(m_{A}\left(\boldsymbol{X}_{i}\right), Y_{i}\right)-S\left(m_{B}\left(\boldsymbol{X}_{i}\right), Y_{i}\right)
$$

As an empirical illustration of the convergence speed, we simulate a Gamma distributed response, conditionally on two features $\boldsymbol{X}=\left(X_{1}, X_{2}\right)$, one categorical and one numerical feature, $Y \mid \boldsymbol{X} \sim$ Gamma.

```
generate_data <- function(n_samples, seed = NA) {
    if (!is.na(seed) && seed%%1==0) {
        set.seed(seed)
    }
    df <- tibble(
        color = sample(c("red", "blue"), n_samples, replace = TRUE, prob = c(0.2, 0.8)),
        length = runif(n_samples, min = -2, max = 2)) %>%
    mutate(color = as.factor(color))
```

## Page 68
Figure 21: Speed of convergence with increasing test sample size of several scoring functions in terms of $\operatorname{CV}\left(\bar{Z}_{n}\right)$ evaluated over 100 simulations. Horizontal lines in the right figure indicate the value of $\operatorname{CV}(Z)$ based on $10^{8}$ data points.

```
true_mean <- exp(model.matrix(~ color + length, data = df) %*% c(4, -2, 1))
dispersion <- 2 # results are highly sensitive to this parameter
# E[Y] = shape * scale = mu
# Var[Y] = shape * scale**2 = dispersion * mu**2
# shape = 1 / dispersion
# scale = mu * dispersion
df$y <- rgamma(n_samples, shape = 1 / dispersion, scale = true_mean * dispersion)
df
}
```

We fit a trivial model as $m_{A}$ as well as a (correctly specified) Gamma GLM with log link as $m_{B}$ on a training sample of size $=1000$. We evaluate different scoring functions-squared error (corresponding to Gaussian deviance), Poisson deviance, Gamma deviance and inverse Gaussian deviance, which are Tweedie deviances with power $p=0,1,2,3$-on a sequence of nested test sets with increasing size $n=1, \ldots, 10^{6}$.

Take the following results with a grain of salt as they are very sensitive to slight changes of the distribution of the data. The relative deviation of the score difference $Z$ on different test sets can be seen in Figure 22. We repeat this simulation 100 times with different random seeds and calculate the coefficient of variation for each test size $n$. Figure 21 visualises $\operatorname{CV}\left(\bar{Z}_{n}\right)$ as well as $\sqrt{n} \operatorname{CV}\left(\bar{Z}_{n}\right)$, taking into account the convergence rate of $n^{-1 / 2}$ of $\operatorname{CV}\left(\bar{Z}_{n}\right)$. It further exhibits the theoretical quantity of $\sqrt{n} \operatorname{CV}(Z)$ (based on a Monte Carlo simulation with size $10^{8}$ ). It is well visible that the Gamma deviance converges fastest with inverse Gaussian and Poisson deviance close together as second. The squared error seems to suffer from some data points on which it produces outliers. ${ }^{47}$ This simulation study suggests that scores derived from a quasi maximum likelihood

[^0]
[^0]:    47 We even observed erratic behaviour of the inverse Gaussian deviance for values of $y$ very close to zero when experimenting with different parameters of data distributions.
![Page 68 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p68_img1.jpg)

## Page 69
Figure 22: Speed of convergence with increasing test sample size of several scoring functions for 9 different simulations of test sets. Values on $y$-axis are the relative deviation of score differences with respect to their respective values at $n=10^{6}$.
![Page 69 Image 1](cs11_model_comparison_and_calibration_assets/cs11_model_comparison_and_calibration_p69_img1.jpg)

## Page 70
approach of the underlying data distribution exhibit a fast convergence. This underpins the theoretical intuition provided in Subsubsection 5.1.6. We emphasise that this intuition ignored the presence of features. This could be the reason for the sensitivity of the results with respect to small changes in the distribution of the data. We encourage further research which takes the presence of feature information into account.