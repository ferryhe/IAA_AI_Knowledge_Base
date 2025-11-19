# CAS_Monograph_03-Taylor-Errata

## Page 1
# Stochastic Loss Reserving Using Generalized Linear Models 

## Errata

Page 7, last line of second paragraph: should read " $Y_{k 1}\left(=X_{k 1}\right)$ ".
Page 7, last dot point: replace with the following:
Cape Cod forecast: $B_{k}=P_{k} \sum_{i=1}^{K} P_{i} \omega_{i}\left[\left(X_{i, K-i+1}+\hat{R}_{i}\right) / P_{i}\right] / \sum_{i=1}^{K} P_{i} \omega_{i}$ with $\omega_{i}=$ $1 / \hat{f}_{K-i+1} \ldots \hat{f}_{j-1}$.

Page 9, Table 2-1. In the "Inverse Gaussian" row, under the heading $b(\theta)$, the entry $-\left(-2 \theta\right)^{-1 / 2}$ should be $-\left(-2 \theta\right)^{1 / 2}$.

Page 9, sentence immediately following Table 2-1. Add "where $n$ and $v$ are additional parameters providing alternative representations of $\phi$ ".

Page 9, equation (2-5). The factor $\alpha(\phi)$ should be $a(\phi)$.
Page 10, equations (2-12) and (2-13). These are incorrect, and should be deleted. Equation (2-9) holds for $p \neq 1,2$, and (2-10) holds for $p \neq 1$. However, in these cases, the form of variance function implies the following:

For $p=1, b(\theta)=e^{\theta}, \mu=b^{\prime}(\theta)=e^{\theta}$.
For $p=2, b(\theta)=-\ln (-\theta), \mu=b^{\prime}(\theta)=-1 / \theta$.
Page 11, Table 2-2. In the "Gamma" row, under the heading $b(\theta)$, the entry $\ln (-\theta)$ should be $-\ln (-\theta)$.

Equation (2-15): Replace by $\exp c(y, \varphi)=\varphi^{-y / \varphi}[(y / \varphi)!]^{-1}$.
Equation (2-16): Replace by $\pi(y ; \mu, \phi)=\frac{(\mu / \phi)^{y / \phi} \exp (-\mu / \phi)}{(y / \phi)!}$.
Page 29, equation (3-12) require correction in sympathy with the correction to (2-16):
replace the term $\ln \left(f_{j-1}-1\right)$ by $\ln \left(\frac{f_{j-1}-1}{\phi_{j-1} / X_{k, j-1}}\right)$.
Page 30, 3 lines after equation (3-14): Definition of $\beta$ should be

$$
\beta=\left(f_{1}-1, f_{2}-1, \ldots, f_{9}-1\right)^{T}
$$

Page 49, equation (5-21): Replace by

$$
\varepsilon_{\text {proc }}^{*}=\hat{Y}_{\text {proc }}-\hat{Y}
$$