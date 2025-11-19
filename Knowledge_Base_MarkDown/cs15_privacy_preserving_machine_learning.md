_Note: Source document was split into 3 OCR chunks (pages 1-13, pages 14-25, pages 26-32) to stay within token limits._

# CS15 Privacy Preserving Machine Learning

## Page 1
# Privacy Preserving Machine Learning 

Daniel Meier* Juan Ramón Troncoso-Pastoriza ${ }^{\dagger}$<br>Prepared for:<br>Fachgruppe "Data Science"<br>Swiss Association of Actuaries SAV

Version of September 30, 2023


#### Abstract

This tutorial provides an introduction into the evolving topic of privacy preserving machine learning. It discusses how to run models on data from potentially multiple data providers without any data provider having to share any non-encrypted data with any other party. In particular, for use cases requiring large amounts of sensitive personal data, and in the context of strict regulations like GDPR in the European Union, this topic is highly relevant. We introduce the concept of (multiparty) homomorphic encryption and demonstrate the approach on two synthetic datasets of personal health information. Furthermore, this tutorial also provides an introduction into the most common (survival) models to predict health outcomes.


Keywords. Life \& health, sensitive personal data, cryptography, security, multiparty homomorphic encryption, logistic regression, Cox proportional hazards model, neural network, hazard ratio, relative risk, odds ratio, federated machine learning.

## 0 Introduction and overview

This data analytics tutorial has been written for the working group "Data Science" of the Swiss Association of Actuaries SAV, see
https://www.actuarialdatascience.org
In recent years, we have witnessed the advent of new regulatory frameworks such as the European General Data Protection Regulation (GDPR)[16] that impose stricter controls and protection guarantees on the processing of personal data. These are specially relevant to data controllers, who are bound to security obligations to prevent unauthorized disclosure by applying the principles of risk minimization, privacy-by-design and security-by-design. In terms of data collaborations, the fall of the privacy shield in July 2020 [1] greatly limited the scope under which most international data transfers involving personal data from European citizens with jurisdictions outside the EU/EEA can be carried out, requiring the implementation of "supplementary measures" to compensate for gaps in data protection, following the guidance of the European Data Protection Board (EDPB) [2].
In Switzerland, the new data protection regulation (nFADP - New Federal Act on Data Protection) ${ }^{1}$ is going to be implemented by September 1, 2023, and it introduces principles and obligations similar to those of the European GDPR.

[^0]
[^0]:    *Swiss Re Institute, Swiss Re Ltd, daniel_meier@swissre.com
    ${ }^{\dagger}$ Tune Insight SA, juan@tuneinsight.com
    ${ }^{\ddagger}$ https://www.edoeb.admin.ch/edoeb/en/home/datenschutz/grundlagen/ndsg.html

## Page 2
The technologies and cryptographic methods covered in this tutorial provide effective security measures that, when paired with appropriate organizational measures, can notably streamline compliance and also re-enable cross-border collaborations on personal data [10]. When there is a legal basis for processing personal data, a computation workflow can be authorized (e.g., computation of mortality statistics or training of (survival) models). The main ideas behind the proposed approaches are:

- Federated analytics / Federated machine learning: Keep personal data local (at the data controller infrastructure) and avoid transferring or exporting any raw personal data if it is not in itself the result of the workflow computation for which the treatment is approved/authorized. Leverage local computation to produce aggregate data before transferring it.
- Encrypted processing: Employ encryption in-use to protect data whenever it is out of the security perimeter of its data controller. Leverage the use of privacy enhancing techniques (PETs) such as homomorphic encryption and secure multiparty computation to avoid disclosure of intermediate results to any entity except the data controller.
- Protected release: Employ release protection mechanisms such as differential privacy to mitigate or minimize the risk of re-identification of the original personal records from any released (clear-text) results.

When all these mechanisms are in place, the risks of exposure during the treatment of personal data are minimized, and the produced results can be considered anonymous under a relative interpretation of the GDPR [47]. This is in line with recent decisions by the European General Court on considering encrypted (or coded) data as anonymous for attackers [22].
This tutorial focuses on a specific example application to survival models on health data (personal and special category data), showing how to optimize the process from a machine learning perspective and how to employ encrypted processing (second bullet point in the list above) to protect data while in use, hence laying the ground on how to securely process personal data to extract actionable insights useful in actuarial data science.

# 1 Working with sensitive (personal) data 

We create two synthetic datasets $\mathcal{D}_{1}$ and $\mathcal{D}_{2}$ with personal health information over time. Working with synthetic datasets has the advantage that we know the "true" model, and can thus compare against the known ground truth. Datasets $\mathcal{D}_{1}$ (and $\mathcal{D}_{2}$ ) comprise more than 600 k (1M) individual persons with more than 6 M (10M) person years in total. The following variables are used, $\mathcal{D}_{1}$ only uses the first 6 variables.

- id: an ID to uniquely identify a person,
- year: observation year of health information,
- age: age of the person at time year,
- gender: male (0)/female (1),
- bmi: body-mass-index (BMI), unit $\mathrm{kg} / \mathrm{m}^{2}$,
- sbp: systolic blood pressure (SBP), unit mmHg ,
- sd_sbp: standard deviation of systolic blood pressure measurements, unit mmHg ,
- tcl_hdl_ratio: total cholesterol level (TCL) divided by high-density lipoprotein level (HDL),
- num1, num2, num3: 3 generic numeric health risk factors without specifying their meaning explicitly, e.g., stepcounts, triglycerides, resting heartrate, etc.
- binary: a generic binary health risk factor, e.g., smokers, foreign born, etc.,
- event: binary target variable, e.g., developing a cardio-vascular disease or death.

## Page 3
For simplicity, we assume that we have 10 full years of observation periods for each individual person and there is no missing data in any of the individual health attributes. Both assumptions are not given in practice. While incomplete observation periods can be handled well by taking censored information (start and end date of the observation) into account, missing data - in particular data that is not "missing completely at random" (MCAR) - is a major challenge in practice.
As a starting point to create the synthetic dataset, we are using the QRISK3 calculator ${ }^{2}$, see [25]. Based on age, gender, BMI, SBP, standard deviation of SBP, TCL/HDL (and several other attributes we are ignoring in this tutorial) QRISK3 estimates the probability of developing a heart attack or stroke over the next 10 years. We will speak of cardio-vascular diseases (CVD) risk when referring to QRISK3. Moreover, we are using the following assumptions to simulate the first dataset $\mathcal{D}_{1}$ :

- set age $=35$ at the beginning of the 10 years observation period,
- set gender to male,
- $\binom{\text { sbp }}{\log (\text { bmi })} \sim \mathcal{N}\left(\left(\begin{array}{l}125 \\ 3.2\end{array}\right),\left(\begin{array}{cc}15^{2} & 15 \cdot 0.25 \rho \\ 15 \cdot 0.25 \rho & 0.25^{2}\end{array}\right)\right)$, with correlation coefficient $\rho=0.25$,
- remove persons with sbp $<110$ or sbp $>150$ or bmi $<18$ or bmi $>40$, see Figure 2,
- sample whether an event occurs according to QRISK3's probability $q$ and, if yes, draw time_of_event based on the main assumption that risk increases by around $10 \%$ each year, i.e., continuous-time CVD risk at time $t$ is proportional to around $\exp (0.095 t)$ (Gompertz-Makeham approximation)

$$
(\text { time_of_event } \mid \text { event }=1) \sim F(t):=q^{-1}\left(1-\exp \left(-\int_{\tau=0}^{t} \alpha \exp (0.095 \tau) d \tau\right)\right)
$$

where $\alpha$ is chosen such that the survival probability is

$$
\exp \left(-\int_{\tau=0}^{10} \alpha \exp (0.095 \tau) d \tau\right)=1-q
$$

- apart from age, event and time_to_event, all persons' variables remain constant over time, see Table 1.

Table 1: Example of dataset $\mathcal{D}_{1}$.

| id | year | age | gender | bmi | sbp | event | time_to_event |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 2010 | 35 | m | 24 | 120 | 0 | - |
| 1 | 2011 | 36 | m | 24 | 120 | 0 | - |
|  | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
| 1 | 2019 | 44 | m | 24 | 120 | 0 | - |
| 2 | 2010 | 35 | m | 33 | 145 | 0 | 7.5 |
| 2 | 2011 | 36 | m | 33 | 145 | 0 | 6.5 |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
| 2 | 2017 | 44 | m | 33 | 145 | 1 | 0.5 |
| 3 | 2010 | 35 | m | 26 | 125 | 0 | - |
| 3 | 2011 | 36 | m | 26 | 125 | 0 | - |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |

[^0]
[^0]:    ${ }^{2}$ QRISK3 itself is derived from a longitudinal health dataset. Interactions and the choice of functional forms, e.g., fractional polynomials, are mostly based on judgment.

## Page 4
When we are considering relative (CVD) risks (RR), i.e., 10-year CVD risk of a given individual divided by 10-year CVD risk of a reference person of the same age and gender, we set

$$
\begin{gathered}
\mathrm{bmi}=75 / 1.80^{2} \approx 23.1, \quad \mathrm{sbp}=120, \quad \text { sd_sbp }=10, \quad \text { tcl_hdl_ratio }=3.5 \\
\text { num } 1=\text { num } 2=\text { num } 3=0.5, \quad \text { binary }=0
\end{gathered}
$$

as a reference, see Figures 3 and 4. For the second dataset $\mathcal{D}_{2}$, we will be using the following additional (and overriding) assumptions:

- draw age uniformly from $[0,84]$,
- draw gender uniformly from \{male, female\},
- draw tcl_hdl_ratio uniformly from $[2.5,7]$,
- draw sd_sbp uniformly from $[5,15]$,
- draw the 3 generic numeric variables uniformly and independently from $[0,1]$,
- draw the generic binary variable uniformly from $\{0,1\}$,
- draw binary depending on num3 by rounding (num3 $+3 U$ )/4 for a $[0,1]$-uniformly distributed random variable $U$,
- apart from SBP and BMI, and binary and num3, there are no other dependencies modeled and we assume independence. ${ }^{3}$
Furthermore, we extend QRISK3 with the goal to model mortality instead of CVD risk as target variable. First, we derive 10-year mortality rates ${ }_{10} q_{x}$ for each $x=$ age, i.e., the risk of dying within 10 years, from one-year mortality rates $q_{x}$ of Swiss males in year 2019 provided by the Human Mortality Database [13]. Then we fit a degree 14 polynomial ${ }^{4} r$ (age) on the difference between $\log \left({ }_{10} q_{x}\right)$ and $\log ($ QRISK3) at age $x$ and individual attributes given by the reference person, see Figure 5.
The full extension from QRISK3 to mortality ${ }^{5}$ is then given by

$$
\begin{aligned}
\mu^{*}(\boldsymbol{x}) & =\exp \left(\log (\operatorname{QRISK} 3(\boldsymbol{x}))+r(\text { age })\right. \\
& \left.+16(\text { num } 1-0.5)^{4}+4(\text { num } 2-0.5)^{2} \text { num } 3+\text { num } 3+\text { binary }-1.65\right)
\end{aligned}
$$

The simulated mortality rates of $\mathcal{D}_{2}$ are shown in Figure 1. ${ }^{6}$
Datasets $\mathcal{D}_{1}$ and $\mathcal{D}_{2}$, as described above, are the common format for longitudinal health data in practice. In order to apply the models of Section 3 on a 10-year time horizon, the data is transformed into a slightly different format, where

- only the rows with year equal to the first observation year are kept,
- event is 1 if and only if an event occurred over the full 10 observation years,
- time_of_event $\in[0,10]$ is the time when the event happened, or, e.g., 11 or undefined otherwise.

We will use this format, where $\left|\mathcal{D}_{1}\right|$ and $\left|\mathcal{D}_{2}\right|$ denote the number of persons in each dataset, throughout the remainder of this tutorial.

[^0]
[^0]:    ${ }^{3}$ Note that there are plenty of dependencies across all variables in practice.
    ${ }^{4}$ We use such a high degree to sufficiently well capture increased mortality around age 20 due to accidents mainly.
    ${ }^{5}$ Note that $\mu^{*}(\boldsymbol{x})$ defines the assumed ground truth of 10 year mortality and not the force of mortality that usually is denoted by $\mu$ among Life actuaries.
    ${ }^{6}$ Note that $\mu^{*}(\boldsymbol{x})$ does not reproduce the average mortality rates of the Human Mortality Database in the sense of following a cohort of newborns. Also, the modelled evolution of the individual variables over time is very simplified (constant). We might consider these aspects in a future tutorial where the main focus is on models for longitudinal data.

## Page 5
Figure 1: Simulated 10-year log-mortality rates $\mathcal{D}_{2}$ (blue), and 10-year log-mortality rates of the reference person by age (red).

Figure 2: Simulating systolic blood pressure (SBP) and body-mass-index (BMI) within the usual ranges and with a small positive correlation. The red and green lines correspond to the red and green lines in Figure 4.

# 2 The most common cryptographic methods 

In this section, we provide a brief introduction into the most commonly used cryptographic methods, i.e., RSA, ElGamal, ECC, lattice-based cryptography, and we introduce some of their homomorphic properties that enable processing the encrypted data without having to decrypt it first.

### 2.1 RSA

The Rivest-Shamir-Adleman (RSA) public-key cryptosystem, see [43], is one of the oldest and most widely used methods for secure data transfers. We provide a brief introduction and a first simple example of homomorphic encryption based on RSA.
Consider a plain message (or any kind of data in general) encoded as a large integer $m$ that should be securely transferred from Alice to Bob.

1. Bob publicly shares his public key given by a large integer $n=p q>m$, the product of two large
![Page 5 Image 1](cs15_privacy_preserving_machine_learning_assets/cs15_privacy_preserving_machine_learning_p05_img1.jpg)
![Page 5 Image 2](cs15_privacy_preserving_machine_learning_assets/cs15_privacy_preserving_machine_learning_p05_img2.jpg)

## Page 6
Figure 3: 10 year relative risk of developing a cardio-vascular disease (CVD) according to QRISK3 of the 35 year old reference person.

Figure 4: 10 year relative risk of developing a cardio-vascular disease (CVD), with SBP $=125$ (red line), when varying SBP according to $\mathrm{SBP}=3.75(\log (\mathrm{BMI})-3.2)+125$ (green line), and the expected relative risk conditioned on BMI.
strong primes $p \neq q$, and another large integer $e$.
2. Alice encrypts the message $m$ by calculating $c=m^{e} \bmod n$ and sends ciphertext $c$ to Bob.
3. Bob decrypts the message with his private key $d$, the inverse of $e$ in the multiplicative group $\bmod n$, by using the identity $c^{d}=m^{e d}=m \bmod n$.

The exponent $e$ of the public key is an integer $2<e<\varphi(n)=(p-1)(q-1)$, where $\varphi(n)$ is Euler's totient function, see Equation (2.1), and $e$ and $\varphi(n)$ are co-prime, i.e., the greatest common divisor $\operatorname{gcd}(e, \varphi(n))=1$. Euler's totient function is defined as the number of elements in the multiplicative group of $\mathbb{Z} / n \mathbb{Z}$ (integers modulo $n$ ). Recall that $\varphi(p)=p-1$ since the multiplicative group of the finite field $\mathbb{Z} / p \mathbb{Z}$ is given by $\{1,2, \ldots, p-1\}$ for any prime $p$. In general, the multiplicative inverse of any element $a$ in the multiplicative group of $\mathbb{Z} / n \mathbb{Z}$ of size $\varphi(n)$ can be calculated efficiently in $\mathcal{O}(\log \varphi(n))$ time via the extended Euclidean algorithm providing $x$ and $y$ that fulfill
![Page 6 Image 1](cs15_privacy_preserving_machine_learning_assets/cs15_privacy_preserving_machine_learning_p06_img1.jpg)
![Page 6 Image 2](cs15_privacy_preserving_machine_learning_assets/cs15_privacy_preserving_machine_learning_p06_img2.jpg)

## Page 7
Figure 5: Extending QRISK3 (given for ages 25 to 84) by adding a degree 14 polynomial to log QRISK3 to approximate mortality of Swiss males in 2019.

$$
x a+y \varphi(n)=\operatorname{gcd}(a, \varphi(n))=1
$$

such that $x a=1 \bmod \varphi(n)$.

# Euler's totient function 

$$
\varphi(n)=n \prod_{\substack{p \text { prime } \\ p \mid n}}\left(1-\frac{1}{p}\right)=\left(p_{1}-1\right) p_{1}^{c_{1}-1} \cdots\left(p_{k}-1\right) p_{k}^{c_{k}-1}, \text { where } n=p_{1}^{c_{1}} \cdots p_{k}^{c_{k}}
$$

The private key $d$ is the multiplicative inverse of $e \bmod \varphi(n)$ and by knowing $p$ and $q$ (thus knowing $\varphi(n))$ it can be calculated efficiently. The security of RSA is based on the difficulty of

1. factoring $n=p q$,
2. calculating $\varphi(n)$,
3. calculating $d$ from $e$ and $n$, or more generally, calculating the discrete logarithm $\bmod n$.

These 3 tasks are equally difficult, see, e.g., [34] for a precise definition of "equally difficult". We sketch the simple relations:

- 1. knowing factors $p, q$ of $n \Rightarrow 2$. calculate $\varphi(n)=(p-1)(q-1)$.
- 2. knowing $\varphi(n) \Rightarrow 3$. calculate $d$ via extended Euclidean algorithm $e d+y \varphi(n)=\operatorname{gcd}(d, \varphi(n))=1$.
- 2. knowing $\varphi(n) \Rightarrow 1$. calculate $p+q$ from $\varphi(n)=-(p+q)+1 \bmod n$, then solve $x^{2}-(p+q) x+n=0$ to obtain its roots $p$ and $q$.

Also note that there are several combinations of $n$ and $e$ that are vulnerable, see, e.g., [49]. Also, if $n$ is not sufficiently large, integer factoring algorithms like the quadratic sieve [40] and the asymptotically slightly faster number field sieve [29] will provide the factors of $n$ in subexponential expected running time with respect to the number of digits of $n$. Finally, Shor's algorithm [48] demonstrates how quantum
![Page 7 Image 1](cs15_privacy_preserving_machine_learning_assets/cs15_privacy_preserving_machine_learning_p07_img1.jpg)

## Page 8
computers are able to very efficiently factor integers (and also efficiently calculate discrete logarithms) to completely undermine the security of RSA. See, for example, $[11,18]$ for an overview of the current state of the art on quantum computing.

Homomorphic properties. RSA also provides a simple example to introduce the concept of homomorphic encryption. In general, consider an encryption function enc, i.e., a function that is simple to evaluate but assumed to be difficult to invert (without knowing the private key)

$$
\operatorname{enc}: \mathcal{M} \longrightarrow \mathcal{C}
$$

where $m \in \mathcal{M}$ denotes a plaintext, unencrypted datapoint, e.g., $m \in \mathbb{Z} / n \mathbb{Z}$. Let dec: $\mathcal{C} \longrightarrow \mathcal{M}$ denote the decryption function. Furthermore, let op ${ }_{\mathcal{M}}$ denote an operator on $\mathcal{M} \times \mathcal{M}$, e.g., multiplication in $\mathbb{Z} / n \mathbb{Z}$ or any other operation needed for modelling purposes, such as addition, exponentiation, etc. The encryption being homomorphic means that there exists an operator op ${ }_{\mathcal{C}}$ on $\mathcal{C} \times \mathcal{C}$ such that

$$
\operatorname{dec}\left(\operatorname{op}_{\mathcal{C}}\left(\operatorname{enc}\left(m_{1}\right), \operatorname{enc}\left(m_{2}\right)\right)\right)=\operatorname{op}_{\mathcal{M}}\left(m_{1}, m_{2}\right)
$$

For RSA, with $\mathcal{M}=\mathcal{C}=\mathbb{Z} / n \mathbb{Z}$ and $\operatorname{op}_{\mathcal{M}}=\operatorname{op}_{\mathcal{C}}=$ multiplication $\bmod n, \operatorname{enc}(m)=m^{c} \bmod n$, and $\operatorname{dec}(c)=c^{d} \bmod n$, Equation (2.2) becomes

$$
\operatorname{dec}\left(\operatorname{enc}\left(m_{1}\right) \cdot \operatorname{enc}\left(m_{2}\right)\right)=\operatorname{dec}\left(m_{1}^{c} \cdot m_{2}^{c} \bmod n\right)=\left(m_{1} \cdot m_{2}\right)^{c d} \bmod n=m_{1} \cdot m_{2} \bmod n
$$

Hence, RSA is multiplicatively homomorphic, but it cannot be securely used as a homomorphic cryptosystem, as will be shown in the next sections.

# 2.2 ElGamal 

We briefly introduce the ElGamal cryptosystem [15], in the simplest case operating on the multiplicative group of $\mathbb{Z} / p \mathbb{Z}$, where $p$ is a large strong prime. Let $\alpha \in G$ be one of the $\varphi(p-1)$ many generators of $\mathbb{Z} / p \mathbb{Z}$, i.e., $\mathbb{Z} / p \mathbb{Z}=\left\{\alpha^{k} \mid k \in \mathbb{Z}\right\}$, e.g. $\alpha \in\{2,3,10,13,14,15\}$ for $p=19$. Bob chooses a private key $1<d<p-1$ and defines his public key as the tuple $(p, \alpha, z)$, where $z:=\alpha^{d}$. To encrypt a message $m \in \mathbb{Z} / p \mathbb{Z}$, Alice

1. draws a random $r \in\{1, \ldots, p-1\}$, calculates the shared secret $s:=z^{r}=\left(\alpha^{d}\right)^{r} \bmod p$, and
2. sends the tuple $\left(\alpha^{r}, m s\right) \bmod p$ to Bob.

To decrypt the tuple $\left(\alpha^{r}, m s\right) \bmod p$, Bob

1. calculates the shared secret $s=\left(\alpha^{r}\right)^{d} \bmod p$ and its inverse $s^{-1} \bmod p$ via the extended Euclidean algorithm ( $s$ and $p$ are co-prime), and
2. retrieves the message from $m=(m s) s^{-1} \bmod n$.

The security of ElGamal thus depends on the difficulty of calculating discrete logarithms $d=\log _{\alpha} z$ $\bmod p$. It is worth noting that with the given definition, ElGamal also presents a multiplicative homomorphism, as RSA.

### 2.3 ECC

The elliptic curve cryptosystem, ECC, [35] uses the same approach as ElGamal, but replaces the group $\mathbb{Z} / p \mathbb{Z}$ by groups on elliptic curves over finite fields, i.e., the solutions of equations of the form

$$
y^{2}=x^{3}+a x+b
$$

## Page 9
where $4 a^{3}+27 b^{2} \neq 0$. A group operation can be defined both algebraically and geometrically and the security is again based on the difficulty to calculate discrete logarithms. We omit the details and close with remarking that ECC today is the preferred method for secure web browsing, as first handshake to exchange keys for symmetric encryption methods like AES, and many other applications.

# 2.4 Homomorphic Encryption 

The previously presented RSA and ElGamal cryptosystems provide multiplicative homomorphisms, but their homomorphic properties are rarely used, whereas most of the currently used homomorphic cryptosystems are based on lattice cryptography. A homomorphic cryptosystem must fulfill Equation 2.2 for at least one operation. This enables the definition of an extended cryptosytem, that besides the regular key generation, encryption and decryption functions, comprises an additional evaluation function, which carries out the homomorphic versions of plaintext operations on ciphertext inputs to obtain encrypted results. This was originally introduced by Rivest, Adleman and Dertouzos back in 1978 [42], who coined the term "privacy homomorphism". In the case of RSA and ElGamal, this evaluation function is limited to products of ciphertexts, which is equivalent to products of plaintexts.
Besides Equation 2.2, homomorphic cryptosystems must also fulfill the following properties [4]:

- Semantic security (also known as IND-CPA security): Semantic security is achieved if no polynomialtime adversary has an advantage in guessing (better than random) whether a given ciphertext is an encryption of one of two different messages. This property was introduced by Goldwasser and Micali [24] in 1982, together with the first IND-CPA secure homomorphic cryptosystem. Semantic security can only be achieved by probabilistic encryption schemes, where two encryptions of the same plaintext are different (with overwhelming probability). RSA as defined above is deterministic: the encryption of the same message under the same key always results in the same ciphertext, so it is possible for an adversary to distinguish whether a ciphertext is an encryption of a given plaintext or not (just by encrypting the plaintext with the same public key and checking for equality). Hence, an adversary could use the homomorphic computation to build a dictionary of known plaintext-ciphertext maps (e.g., of common or more likely plaintext values), and use the homomorphic multiplication to find whether a new encryption contains a factor or a multiple of the dictionary points. Hence, RSA is not semantically secure and cannot be safely used as a homomorphic cryptosystem.
- Compactness: A homomorphic encryption is compact if homomorphic operations on the ciphertexts do not expand their length. That is, an arbitrary list of calls to the evaluation function produces a ciphertext in the ciphertext space, whose size or dimension does not depend on the complexity of the evaluated functions.
- Efficient decryption: The decryption runtime does not depend on the function evaluated on the ciphertexts.

The first property is an essential security property of homomorphic cryptosystems, whereas the other two properties relate to efficiency and scalability to avoid uncontrolled complexity growth for handling encryptions when homomorphic operations are used.

Fully Homomorphic Encryption. For many years since the introduction of the privacy homomorphism concept, multiple cryptosystems with homomorphic properties were introduced. Their evaluate function was capable of executing either binary additions or products in $\mathbb{Z} / 2 \mathbb{Z}$, or ring additions or products in $\mathbb{Z} / n \mathbb{Z}$ for $n>2$; some cryptosystems, such as Boneh-Goh-Nissim [6] were able to homomorphically compute degree-2 polynomials (2-DNF), but there was always a limit on the depth of the circuits, i.e., the set of subsequent operations on inputs, that could be run homomorphically before incurring decryption errors or "exhausting the homomorphic capacity" of the evaluate function.

## Page 10
The open question was whether it could be possible to break the limits on this homomorphic capacity and enable the homomorphic evaluation of arbitrary-depth circuits. Craig Gentry answered that question in his thesis in 2009 [23] by introducing the concept of cryptographic bootstrapping, conceptually equivalent to homomorphically running the decryption circuit to obtain a "fresh" encryption, so that it is possible to keep on homomorphically computing an arbitrary depth circuit by running a bootstrapping before the homomorphic capacity of the encryption is exhausted.

Paillier cryptosystem. Paillier's [38] is one of the most widely known additively-homomorphic cryptosystems, extensively used in secure protocols before the popularization of lattice-based cryptosystems after Gentry's breakthrough in 2009 [23]. We briefly introduce it here as an example of an additive homomorphism meeting all the aforementioned required properties. Its security is based on the hardness of integer factoring (just like RSA) and on the decisional composite residuosity assumption, i.e., given a composite $n$ and an integer $x$, it is hard to decide whether $x$ is an $n$ th-residue modulo $n^{2}$, i.e., whether there exists a $y \in \mathbb{Z} / n^{2} \mathbb{Z}$ such that $x=y^{n} \bmod n^{2}$.

- Key generation: Let $n=p q$ and $\lambda=\operatorname{lcm}(p-1, q-1)$, where $p$ and $q$ are two large strong primes such that $\operatorname{gcd}(p q,(p-1)(q-1))=1$; select a random $g \in \mathbb{Z} / n^{2} \mathbb{Z}$ such that $n$ divides the order of $g$, i.e., the smallest $k>0$ with $g^{k}=1 \bmod n^{2}$. The public key is $(n, g)$ and the private key is $\lambda$.
- Encryption of a plaintext $m \in \mathbb{Z} / n \mathbb{Z}$ :

$$
\operatorname{enc}(m)=g^{m} \cdot r^{n} \bmod n^{2}
$$

where $r \in \mathbb{Z} / n^{2} \mathbb{Z}$ with $\operatorname{gcd}\left(r, n^{2}\right)=1$ is drawn at random.

- Decryption:

$$
\operatorname{dec}(c)=\mathrm{L}\left(c^{\lambda} \bmod n^{2}\right) \cdot \mathrm{L}\left(g^{\lambda} \bmod n^{2}\right)^{-1} \bmod n
$$

where $\mathrm{L}(\cdot)=(\cdot-1) / n$ in $\mathbb{Z}$ and $(\cdot)^{-1}$ is the inverse in $\mathbb{Z} / n \mathbb{Z}$.

- Homomorphic addition:

$$
\begin{aligned}
\operatorname{dec}\left(\operatorname{enc}\left(m_{1}\right) \cdot \operatorname{enc}\left(m_{2}\right)\right) & =\operatorname{dec}\left(g^{m_{1}} \cdot r_{1}^{n} g^{m_{2}} \cdot r_{2}^{n} \bmod n^{2}\right) \\
& =\operatorname{dec}\left(g^{m_{1}+m_{2}} \cdot\left(r_{1} r_{2}\right)^{n} \bmod n^{2}\right) \\
& =m_{1}+m_{2} \bmod n
\end{aligned}
$$

- Homomorphic ciphertext-plaintext product:

$$
\operatorname{dec}\left(\operatorname{enc}\left(m_{1}\right)^{m_{2}}\right)=\operatorname{dec}\left(\left(g^{m_{1}} \cdot r_{1}^{n} \bmod n^{2}\right)^{m_{2}}\right)=\operatorname{dec}\left(g^{m_{1} m_{2}} \cdot r_{1}^{n} \bmod n^{2}\right)=m_{1} m_{2} \bmod n
$$

# 2.5 Lattice-based homomorphic cryptosystems 

Lattice-based cryptography can be defined as "the use of conjectured hard problems on point lattices in $\mathbb{R}^{n}$ as the foundation for secure cryptographic systems" [39]. It presents many benefits with respect to the previously introduced cryptosystems based on the hardness of number theoretic problems such as integer factoring and discrete logarithms. In particular:

- The currently used lattice-based cryptosystems have also been conjectured to be resistant to quantum attacks, which already yields a net advantage with respect to most number-theoretic cryptography, including the public-key cryptosystems presented in the previous sections, which can be broken by efficient quantum algorithms.
- Lattice cryptography also introduces a high asymptotic efficiency and high parallelization factor, hence, efficiently scaling in input size and in the use of higher computing resources.

## Page 11
- Lattice schemes base their security on worst-case intractability assumptions instead of average-case intractability [3]. This means that it is possible to build cryptographically secure systems based on lattice problems for which there exist some hard instances, even if the problem is not hard to solve on average.

Lattice-based constructions have been used for multiple cryptographic applications, including signature schemes, identity based encryption, attribute-based encryption, among others. We refer the interested reader to [39] for further details. Here we will only focus on encryption schemes with homomorphic properties.

Hard problems in lattice-based homomorphic cryptosystems. In terms of encryption functions based on lattices, the first main hard problem, introduced by Regev [41] is Learning with Errors (LWE). The decision-LWE problem can be defined as follows.

# Decision-LWE 

Let $n, q$ be positive integers, and let $\chi$ be an error distribution over $\mathbb{Z}_{q}=\mathbb{Z} / q \mathbb{Z}$ (typically, a discrete Gaussian). Given a (not public) secret $s$ randomly chosen from a given distribution, e.g., uniformly at random in $\mathbb{Z}_{q}^{n}$ or from a short or norm-bounded distribution such as the error distribution $\chi$, and independent samples $\left(\boldsymbol{a}_{i}, c_{i}\right) \in \mathbb{Z}_{q}^{n} \times \mathbb{Z}_{q}$, where every sample is distributed according to either

- LWE distribution, i.e., $\boldsymbol{a}_{i} \in \mathbb{Z}_{q}^{n}$ is drawn uniformly at random in $\mathbb{Z}_{q}^{n}$, and $c_{i}$ is chosen as $c_{i}=\left\langle\boldsymbol{a}_{i}, \boldsymbol{s}\right\rangle+e_{i} \bmod q$, where $\langle\cdot, \cdot\rangle$ is the standard inner product and $e_{i}$ is drawn from the error distribution $\chi$, or
- uniform distribution, i.e., $\left(\boldsymbol{a}_{i}, c_{i}\right)$ is drawn uniformly at random in $\mathbb{Z}_{q}^{n} \times \mathbb{Z}_{q}$,
decide which samples were drawn from which distribution.
The security of LWE thus depends on the difficulty of calculating $s$ from arbitrarily many pairs $\left(\boldsymbol{a}_{i}, c_{i}\right)$. The presence of the error term drawn from $\chi$ is the source of the hardness of this problem, which makes learning the secret $s$ difficult. If we omitted it (i.e., we set $e_{i}=0$ ), the problem is easy to solve, and equivalent to checking whether the corresponding system of $m$ linear equations defined by $\left\langle\boldsymbol{a}_{i}, \boldsymbol{s}\right\rangle=c_{i}$ is compatible or incompatible, and $s$ could be found if the system has full rank (at least $n$ samples needed); this is linked to the analogous search version of the decisional-LWE problem. This problem can be informally posed as learning the secret $s$ is hard if there are small errors introduced in the system of linear equations. Therefore the name "learning with errors".
As the reader will have noticed, the definition of LWE does not directly involve lattices, but cryptosystems based on LWE (and on the subsequent problems presented in the next sections) are considered lattice cryptosystems, as there is a quantum reduction [41] from LWE to lattice hard problems such as the shortest vector problem (SVP) or the shortest independent vectors problem (SIVP). SVP can be informally defined as finding the shortest (minimum norm) vector, and the shortest basis for SIVP in a lattice of a given dimension $n$. An important property of LWE compared to many other cryptosystems is its average case hardness, i.e., all secrets $s$ are equally hard to break, see [41].

LWE Example. We provide a simple example for encryption and decryption with LWE, only considering addition as a homomorphic operation, while multiplication - and several successive operations requires more sophisticated noise and scaling management, see following paragraphs. Let $q=100$, and we encode a binary number with $k$ digits as $m \in \mathbb{Z}_{q}^{k}$ by defining $m_{i}=0$ if the $i$-th digit is 0 , and $m_{i}=50$ if the $i$-th digit is 1 . Let $\chi_{e}$ be a uniform distribution on $[-12,12] \subset Z_{q}$. For $1 \leq i \leq k$ define

## Page 12
$$
\begin{aligned}
\operatorname{enc}\left(m_{i}\right) & =\left(\boldsymbol{a}_{i},-\left\langle\boldsymbol{a}_{i}, \boldsymbol{s}\right\rangle+e_{i}\right)=\left(\boldsymbol{a}_{i}, c_{i}\right) \in \mathbb{Z}_{q}^{n} \times \mathbb{Z}_{q}, \text { and } \\
\operatorname{dec}\left(\left(\boldsymbol{a}_{i}, c_{i}\right)\right) & = \begin{cases}0, & \text { if }\left(c_{i}+\left\langle\boldsymbol{a}_{i}, \boldsymbol{s}\right\rangle\right) \in[-25,24] \bmod q \\
50, & \text { if }\left(c_{i}+\left\langle\boldsymbol{a}_{i}, \boldsymbol{s}\right\rangle\right) \in[25,74] \bmod q\end{cases}
\end{aligned}
$$

The decryption function thus implicitly rounds the results from $\mathbb{Z}_{100}$ to $\mathbb{Z}_{2}$ (see later use of [4]). Note that for a single addition we thus have an exact equivalence

$$
\operatorname{dec}\left(\operatorname{enc}\left(m_{i}\right)+\operatorname{enc}\left(m_{i}^{\prime}\right)\right)=m_{i}+m_{i}^{\prime} \bmod q
$$

Cryptosystems based on LWE typically present a large expansion, i.e., ciphertexts are much larger than their plaintext counterpart. This impacts their practicality and scalability, and it was the main reason for the search of additional structure that could improve efficiency and preserve compactness, that led to the formulation of a ring version of the problem, denoted Ring-Learning with Errors (RLWE), for which here we provide the definition of the decisional problem [31, 32]:

# Decision-RLWE 

Let $\chi$ be an error distribution (typically, a discrete Gaussian) over a ring $R$. Given a secret $s$ randomly chosen from a given distribution (e.g., uniformly at random in $R$ or from a short or normbounded distribution such as the error distribution $\chi$ ), and $m$ independent samples $\left(a_{i}, b_{i}\right) \in R \times R$, where every sample is distributed according to either

- RLWE distribution, i.e., $a_{i}$ is drawn uniformly at random in $R, e_{i}$ is drawn from the error distribution $\chi$, and $b_{i}$ is chosen as $b_{i}=s \cdot q+e_{i}$
- uniform distribution, i.e., $\left(a_{i}, b_{i}\right)$ is drawn uniformly random in $R \times R$,
decide which samples were drawn from which distribution.
The RLWE problem also has a reduction to SIVP. The ring $R$ is usually chosen as a cyclotomic ring and, for performance reasons, this cyclotomic ring is chosen as a polynomial ring $R=\mathbb{Z}[x] /(f(x))$ where the modulo polynomial $f(x)$ is a power of 2 . Indeed, cyclotomic polynomials of power-of-2 degree are of the form $f(x)=x^{n}+1$, with $n$ a power of 2 , which greatly simplifies the computation of modular reduction operations in the ring, using $x^{n}=-1 \bmod f(x)$.
As evidenced by the definition of LWE and RLWE, noise terms are an essential component for the indistinguishability assumptions to hold, and the cryptographic constructions based on these problems have to implement mechanisms to properly manage these noise terms.

RLWE cryptosystems. Three main RLWE-based cryptosystems with an algebraic homomorphism (both additive and multiplicative) have been popularized since 2011, namely BFV (Brakerski/FanVercauteren) [17], BGV (Brakerski-Gentry-Vaikuntanathan) [8] and CKKS (Cheon-Kim-Kim-Song) [9]. All of them follow a similar basic construction and they share the same core decryption function; they mainly differ on the relation between the noise and the message, and in how noise propagation is managed when running homomorphic operations; for this purpose, they introduce a relinearization operation and the concept of "levels", which is related to the plaintext scale (in BGV and CKKS) or constant (in BFV, termed scale-invariant). For the sake of conciseness, we will present CKKS with power-of-2 cyclotomics as an exemplifying cryptosystem, as this can be considered the best-suited RLWE-based homomorphic cryptosystem for closed-loop iterative ML training workflows and it is the only one that features an approximate decryption. In the next paragraphs, we explain step by step each of the operations in the CKKS cryptoscheme. For the sake of notational simplicity, we will omit some of the common function inputs (e.g., keys, scale factors, levels).

## Page 13
- Setup: Let $n=2^{k}$ be a power of 2 and $\Phi(x)=x^{n}+1$. Let $\left(q_{0}, \ldots, q_{L}\right)$ be a sequence of integer values, $q_{i} \in \mathbb{Z}^{+}$, with $Q_{i}=\prod_{j=0}^{i} q_{j}$. This moduli chain will be used to enable proper noise management. Typically, the plaintext coefficients are smaller than the last modulus $q_{0}$, hence $q_{0}$ must be large enough to offer the required precision to represent the input plaintext coefficients. Let $R_{Q_{i}}$ be the quotient ring of polynomials with integer coefficients $R_{Q_{i}}=\mathbb{Z}_{Q_{i}}[x] / \Phi(x)$, and let $\chi_{s}$ (typically polynomials with ternary $\{0, \pm 1\}$ coefficients) and $\chi_{e}$ (typically polynomials with coefficients from a truncated Gaussian distribution) be two short error distributions in $R_{Q_{i}}$ (polynomials with small coefficients).
- Key generation: The secret key $s \in R_{Q_{L}}$ is drawn from a distribution $\chi_{s}$. Let $a$ be drawn uniformly at random from $R_{Q_{L}}$, and $e$ be drawn from the error distribution $\chi_{e}$. The public key is $p k=$ $(-a \cdot s+e, a) \in R_{Q_{L}}^{2}$.
- Encryption: A complex plaintext vector $\boldsymbol{m} \in \mathbb{C}^{n / 2}$ is first mapped to a real vector (encoded) using a canonical ring homomorphism

$$
\psi: \mathbb{C}^{n / 2} \rightarrow \mathbb{R}^{n}
$$

before being discretized into an element of $R_{Q_{L}} m=\lfloor\Delta \cdot \psi(\boldsymbol{m})\rfloor$, where $\lfloor\cdot\rceil$ denotes rounding to a close element in $R_{Q_{L}}$, and the scaling factor $\Delta$ guarantees a sufficient precision after the discretization/rounding. We omit the details on how the ring homomorphism $\psi$ is constructed, see [9], but emphasize that component-wise addition and multiplication in $\mathbb{C}^{n / 2}$ correspond to addition and multiplication in $R_{Q_{L}}$. Let $r$ be randomly drawn from $\chi_{s}$, and $e_{0}, e_{1}$ randomly drawn from $\chi_{e}$.

$$
\boldsymbol{c}=\operatorname{enc}(\boldsymbol{m})=r \cdot p k+\left(m+e_{0}, e_{1}\right) \in R_{Q_{L}}^{2}
$$

The ciphertext can be regarded as vector in $\boldsymbol{c}=\left(c_{0}, c_{1}\right) \in R_{Q_{L}}^{2}$, or as a degree-1 polynomial in $s$, i.e., $c(s)=c_{0}+c_{1} \cdot s \in R_{Q_{L}}[s]$. In the following, we will use both representations interchangeably.

- Decryption: For a ciphertext $\boldsymbol{c}$, decryption comprises a scalar product between the ciphertext vector of polynomials and the secret key in the form $(1, s) \in R_{Q_{L}}^{2}$. This can be seen as the evaluation of the ciphertext $c(s)$ as a polynomial. Then, the obtained polynomial in $R_{Q_{L}}$ is decoded by applying $\psi^{-1}$ and the scaling factor, to obtain a complex vector $\boldsymbol{m}^{\prime}$ :

$$
\begin{gathered}
m^{\prime}=\operatorname{dec}(\boldsymbol{c})=\langle\boldsymbol{c},(1, s)\rangle \bmod Q_{L} \\
\boldsymbol{m}^{\prime}=\psi^{-1}\left(\Delta^{-1} \cdot m^{\prime}\right) \in \mathbb{C}^{n / 2}
\end{gathered}
$$

- Homomorphic addition: Let $\boldsymbol{c}_{1}, \boldsymbol{c}_{2}$ be two ciphertexts respectively encrypting plaintexts $\boldsymbol{m}_{1}, \boldsymbol{m}_{2}$ with the same scaling factor $\Delta$. Then,

$$
\begin{aligned}
\boldsymbol{c}_{\mathrm{add}} & =\boldsymbol{c}_{1}+\boldsymbol{c}_{2} \in R_{Q_{L}}^{2} \\
\operatorname{dec}\left(\boldsymbol{c}_{\mathrm{add}}\right) & \approx \boldsymbol{m}_{1}+\boldsymbol{m}_{2}
\end{aligned}
$$

Note that the level of approximation can be steered to match the requirements of the actual use case, including an exact equivalence if needed.

- Homomorphic multiplication: The product of two ciphertexts $\boldsymbol{c}_{1}=\left(c_{10}, c_{11}\right), \boldsymbol{c}_{2}=\left(c_{20}, c_{21}\right) \in R_{Q_{L}}^{2}$ can be seen as the product of their corresponding polynomial representations:

$$
\begin{aligned}
\boldsymbol{c}_{\mathrm{mul}} & =c_{1}(s) \cdot c_{2}(s)=c_{10} c_{20}+\left(c_{10} c_{21}+c_{11} c_{20}\right) s+c_{11} c_{21} s^{2} \\
& =\left(c_{10} c_{20}, c_{10} c_{21}+c_{11} c_{20}, c_{11} c_{21}\right) \in R_{Q_{L}}^{3}
\end{aligned}
$$

Even if the resulting extended ciphertext is a three-component vector in $R_{Q_{L}}$, decryption can still be seen as the evaluation of its polynomial form in $s$, which is equivalent to its scalar product with the secret key in the form $\left(1, s, s^{2}\right) \in R_{Q_{L}}^{3}$. Also, it must be noted that the scale of the plaintext in $\boldsymbol{c}_{\mathrm{mul}}$ is the product of the scales of the multiplied ciphertexts; i.e., $\Delta_{\mathrm{mul}}=\Delta_{1} \cdot \Delta_{2}$.

## Page 14
The decryption of the resulting ciphertext is equivalent to a component-wise product of the plaintext complex vectors in $\mathbb{C}^{n / 2}$, up to a noise factor: $\operatorname{dec}\left(\boldsymbol{c}_{\text {mul }}\right) \approx \boldsymbol{m}_{1} \cdot \boldsymbol{m}_{2}$.

- Relinearization: In order to preserve the cryptosystem's compactness, the output of a product should be in $R_{Q_{L}}^{2}$, so the result of a homomorphic multiplication (ciphertext polynomial of degree-2 in $s$ ) has to be brought back to a degree-1 polynomial on the key $s$, linear on the key, hence the name relinearization. This relinearization operation on a degree- 2 ciphertext $\boldsymbol{c}_{\text {mul }}=\left(c_{\text {mul } 0}, c_{\text {mul } 1}, c_{\text {mul } 2}\right)$ can be expressed as

$$
\boldsymbol{c}_{\mathrm{mul}}^{\prime}=\left(c_{\mathrm{mul} 0}, c_{\mathrm{mul} 1}\right)+\left\lfloor\frac{c_{\mathrm{mul} 2} \cdot \mathrm{evk}}{P}\right\rceil
$$

where $P$ is a large integer and $\mathbf{e v k} \in R_{P Q_{L}}^{2}$ is a public evaluation key, which can be defined as

$$
\text { evk }=\left(-a^{\prime} \cdot s+e^{\prime}+P \cdot s^{2}, a^{\prime}\right) \in R_{P Q_{L}}^{2}
$$

$a^{\prime}$ is drawn uniformly at random from $R_{Q_{L}}$ and $e^{\prime}$ is drawn from the error distribution $\chi_{e}$. The relinearization key evk can be seen as an encryption of $s^{2}$, which is used to homomorphically remove the quadratic factor $s^{2}$ of the extended ciphertext $\boldsymbol{c}_{\text {mul }}$ during the relinearization operation.

- Rescaling: The plaintext message is scaled by a factor $\Delta$ before encryption, when it is always coupled with a (smaller) noise factor $e$ drawn from $\chi_{e}$. After every homomorphic addition or multiplication, both message and noise get added or multiplied, and the scale factor also gets multiplied after a product. Hence, the noise power (and the plaintext scale) would grow exponentially with the depth of the homomorphically executed circuit. In order to avoid this, RLWE-based cryptosystems must implement a noise management operation, which takes the form of a rescaling operation (also known as modulus-switching) in CKKS. Let $\boldsymbol{c} \in R_{Q_{L}}^{2}$ be a ciphertext. Typically, rescaling involves switching from modulus $Q_{L}$ to modulus $Q_{L-1}$ :

$$
\boldsymbol{c}^{\prime}=\left\lfloor\frac{\boldsymbol{c}}{q_{L}}\right\rceil \in R_{Q_{L-1}}^{2}
$$

The plaintext is preserved after a rescaling, but both the noise and the corresponding plaintext scale are divided by $q_{L}$, i.e., $\Delta^{\prime}=\frac{\Delta}{q_{L}}$. This operation effectively brings the encryption down one level, from $L$ to $L-1$.

Noise management, levels, and approximate decryption. The message encrypted with a RLWEbased cryptosystem is always coupled with a small additive noise factor $e$ drawn from $\chi_{e}$, in order to preserve the hardness of the RLWE problem. The available schemes differ on how this noise relates to the message $m$ (coded as a polynomial). ${ }^{7}$ BGV multiplies the noise factor by a factor $t$ (i.e., the encryption function contains a term in the form $m+t \cdot e$ ); in this case, the noise is coded in the upper-part of the polynomial coefficients, and the message is coded in the lower-part. CKKS and BFV apply the factor to the message instead (i.e., the encryption function contains a term in the form $\Delta m+e$ ), so that the noise is coded in the lower-part and the message is coded in the upper-part of the polynomial coefficients.
Whenever the ciphertext is subjected to homomorphic operations, the messages are added or multiplied, but the corresponding additive noise factors also get added or multiplied. Taking CKKS as an example:

$$
(\Delta m+e)\left(\Delta m^{\prime}+e^{\prime}\right)=\underbrace{\Delta^{2}}_{\text {new scale }} \cdot \underbrace{m m^{\prime}}_{\text {new message }}+\underbrace{\Delta\left(m e^{\prime}+m^{\prime} e\right)+e e^{\prime}}_{\text {new noise term }}
$$

In the case of BGV and BFV, after a given number of operations, the noise level can overflow its available range and be combined with the message, effectively producing a wrong decryption, which can be seen as exhausting the homomorphic capacity of the ciphertext. Therefore, the noise growth has to be controlled

[^0]
[^0]:    ${ }^{7}$ Note also that using power-of-2 cyclotomic polynomials has implications in terms of the error distributions and error behavior, which enable simpler implementations and security reductions [44].

## Page 15
in order to maximize the depth of the circuit that can be run before a decryption error. BGV is defined as a leveled cryptosystem to enable a modulus-switch or rescale operation that limits this noise and makes it linear instead of quadratic with the depth of the circuit. By going down one (or multiple) level(s), the ciphertext modulus is reduced, making the ciphertext coefficients, and thus the noise, smaller as levels are traversed. BFV, conversely, is a scale-invariant cryptosystem, where there is only one constant level/modulus $Q$, and no explicit rescaling operation. It instead has a different multiplication procedure that reduces the noise growth from quadratic to linear.
CKKS is also defined as a leveled cryptosystem, but its peculiarity and its main difference with respect to BFV and BGV in terms of noise management is that it does not distinguish between the message and the noise. Both are kept in the same domain which allows them to be mixed together. Thus, in CKKS the rescaling is not used to reduce the noise level (since it is considered to be part of the message) but to control the magnitude of the message and prevent it from overflowing the modulus Q. By default, the decryption therefore outputs a complex vector instead of an integer vector (BGV/BFV work with integer vectors), where the final precision will depends on the ratio between the message scale and the noise level. That is the reason why CKKS's decryption is called approximate. This is what makes CKKS ideal for closed-loop iterative machine learning operations, as the cryptographic noise has the same effect as a small-norm regularizer and it is automatically corrected by the learning iterations, with negligible impact on the final operational precision.

Packing, plaintext domains, and vector/polynomial arithmetic. One clear difference between RLWE-based encryptions and classical encryptions such as RSA and ElGamal is that the plaintext space is either a polynomial ring or a vector space, instead of a ring of integers. This means that a RLWE ciphertext (such as a CKKS ciphertext) encrypts a vector of $n$ integers (or $n / 2$ complex numbers) instead of a single integer. Homomorphic operations are also vector or polynomial operations. In CKKS, additions always represent vector additions, or component-wise additions of the vector coefficients.
As for homomorphic products, they can be used in two ways, to represent the desired product operations on the plaintext space. If the input plaintexts are encoded using the ring homomorphism in Equation (2.3), then a homomorphic product represents a component-wise product of the plaintext vectors. In this case, it is said that the input is represented in the slot domain. Conversely, if the input plaintext vector $\boldsymbol{m}$ is directly encoded as a polynomial, it is said that the message is encoded in the coefficient domain, and homomorphic products represent polynomial products (e.g., nega-cyclic convolutions when the modulo polynomial is of the form $f(x)=x^{n}+1$ ) between the plaintexts. It is possible to transition between both domains by means of the ring homomorphism $\psi$, which can be represented as a linear transformation. This linear transformation can also be applied homomorphically, to change domains once the message is already encrypted, without having to decrypt it; these are known as SlotsToCoeffs and CoeffsToSlots homomorphic operations.
It must be noted that due to this vector/polynomial nature of the plaintext space, it is not efficient to encrypt a single integer in one RLWE ciphertext. In order to fully utilize RLWE-based encryptions, multiple input scalar numbers must be packed in vectors or polynomials, and homomorphic operations have to be thought of as vector or SIMD (Single-Input-Multiple-Data) operations, that add or multiply all the packed inputs in parallel with a single encrypted operation. It is also possible to manipulate the individual slots, by homomorphically applying rotations and masks.

Advanced operations: key switching, slot manipulation, and bootstrapping. The relinearization operation that is applied after each homomorphic product is in fact a particular case of a more generic key switching operation that can enable the proxy-reencryption of a ciphertext under a key $\boldsymbol{s}_{a}$ to a different key $\boldsymbol{s}_{b}$; in a relinearization, these two keys are represented by $\left(1, s, s^{2}\right)$ and $(1, s)$. The appropriate key-switching keys enable to change the decryption key, and also enable transformations on the slots. For example, a slot rotation, when applied directly to a ciphertext, will rotate both the plaintext and the key, so it requires a key switching from the rotated key to the original key to be performed after the rotation,

## Page 16
in order to keep the ciphertext decryptable under the same key. The necessary (public) key-switching and rotation keys can be generated in advance to make it possible that a third party without access to the secret key can apply these slot manipulations homomorphically.
The progressive noise growth when several homomorphic products are chained in a deep circuit determines the homomorphic capacity of the cryptosystem, and this is what characterizes somewhat homomorphic schemes, as opposed to fully homomorphic schemes, which are able to execute an arbitrary number of operations without incurring decryption errors. The procedure that transforms a somewhat homomorphic encryption to a fully homomorphic one is called bootstrapping, see [23]. In a nutshell, a bootstrapping is a homomorphic execution of a squashed version of the decryption circuit, that results in a fresh encryption of the same plaintext, with a lower noise level. We will not go into the details of the bootstrapping procedure here, and we refer the interested reader to Gentry's work for further details [23].
In leveled schemes such as CKKS and BGV, the bootstrapping operation takes a ciphertext at a low level (e.g., at level 0 ) and brings it back to a high level ( $L-k$, where $k$ is the depth of the bootstrapping circuit), so that it can further support the homomorphic execution of circuits while leveraging the noise management through modulus-switching/rescaling, until level 0 is reached again. As indicated in the description of the CKKS setup, the modulus $q_{0}$ of the last level must be large enough to represent the inputs at the full required precision; if this is not the case, the plaintext coefficients can expand several moduli (e.g., $Q_{1}=q_{0} q_{1}$ ), and in this case, level 0 cannot be reached and a bootstrapping is required when the minimum level to correctly represent the input precision is reached.
It is worth highlighting, though, that the so-called CKKS bootstrapping is not meant to reduce noise; indeed, it increases the noise level by a controllable fixed amount. Instead, it enables further execution of deep circuits, and, as mentioned above, the use of noise in CKKS, due to its approximate decryption and its application to ML iterative feedback loops, differs from the use of noise in other RLWE-cryptosystems.

# 3 Models to predict health outcomes 

In this section, we provide a light and high-level introduction into 3 models to predict probabilities of health outcomes, i.e., CVD risk for dataset $\mathcal{D}_{1}$ and mortality for dataset $\mathcal{D}_{2}$ : logistic regression, Cox regression, and a simple feed-forward neural network. While this section introduces the models and compares their performance on plain, unencrypted data, Section 4 will exemplify one of the models running on encrypted data.

### 3.1 Logistic regression

In the case of logistic regression $\mu_{1}(\boldsymbol{x})$, for both datasets $\mathcal{D}_{1}$ and $\mathcal{D}_{2}$ we omit the variable time_to_event and only consider the binary $y=$ event as target variable. We have a functional form of

$$
\begin{aligned}
\mu_{1}(\boldsymbol{x}) & =\frac{1}{1+\exp \left(-\beta_{0}-\beta_{1} x_{1}-\cdots-\beta_{k} x_{k}\right)}, \text { or equivalently } \\
\operatorname{logit}\left(\mu_{1}(\boldsymbol{x})\right) & =\beta_{0}+\beta_{1} x_{1}+\cdots+\beta_{k} x_{k}
\end{aligned}
$$

where $\operatorname{logit}(x):=\log (x /(1-x))$. Note how the coefficients $\beta_{1}, \ldots, \beta_{k}$ are connected to odds ratios (OR) as follows. First, under the model assumption of logistic regression, the odds of an event happening $(y=1)$ are

$$
\begin{aligned}
\operatorname{odds}(y=1 \mid \boldsymbol{x}) & :=\frac{P(y=1 \mid \boldsymbol{x})}{P(y=0 \mid \boldsymbol{x})}=\frac{P(y=1 \mid \boldsymbol{x})}{1-P(y=1 \mid \boldsymbol{x})} \text { and } \\
\log (\operatorname{odds}(y=1 \mid \boldsymbol{x})) & =\beta_{0}+\beta_{1} x_{1}+\cdots+\beta_{k} x_{k}
\end{aligned}
$$

Furthermore, this also provides a simple interpretation of the model coefficients $\beta_{j}$ in terms of odds ratios

## Page 17
$$
\begin{aligned}
\frac{\operatorname{odds}\left(y=1 \mid\left(x_{1}, \ldots, x_{j}+1, \ldots, x_{k}\right)\right)}{\operatorname{odds}(y=1 \mid \boldsymbol{x})} & =\frac{\exp \left(\beta_{0}+\beta_{1} x_{1}+\cdots+\beta_{j}\left(x_{j}+1\right)+\cdots+\beta_{k} x_{k}\right)}{\exp \left(\beta_{0}+\beta_{1} x_{1}+\cdots+\beta_{k} x_{k}\right)} \\
& =\exp \left(\beta_{j}\right)
\end{aligned}
$$

Thus, the odds ratio of increasing component $x_{j}$ by one unit over $\boldsymbol{x}$ is $\exp \left(\beta_{j}\right)$. In the code notebook we are using the Python package statsmodels:

```
import statsmodels.formula.epi as sm
log_reg = sm.logit(formula="E^SBP+BMI+I(BMI**2)", data=time_to_event_train).fit()
pred = log_reg.predict(time_to_event_test)
```


# 3.2 Cox regression 

We provide a brief introduction into Cox regression or the Cox proportional hazards model, a model from the family of survival models that also comprises the Weibull Accelerated Failure model (AFT) and Aalen's Additive model. For a more comprehensive overview see, e.g., [12, 7, 14]. An advantage of using Cox regression over the logistic regression is that the additional information provided by $t=$ time_to_event can be used to often provide better predictions, see also Section 3.4. Furthermore, note that our assumption to observe all persons throughout the full 10-year observation period is usually not given in practice, but the data is censored, where persons might enter the observation period late or stop being observed without having experienced an event. It is another key strength of Cox regression to allow taking censoring information into account.
Cox regression considers instantaneous, continuous-time hazard rates $h(t \mid \boldsymbol{x})$ at time $t$ given $\boldsymbol{x}=$ $\left(x_{1}, \ldots, x_{k}\right)$, defined by

$$
h(t \mid \boldsymbol{x}):=\lim _{\tau \rightarrow 0} \frac{P(t \leq T<t+\tau)}{\tau P(T \geq t)}
$$

The functional form to model the hazard rate is then assumed to be

$$
h(t \mid \boldsymbol{x})=h_{0}(t) \exp \left(\beta_{1} x_{1}+\cdots+\beta_{k} x_{k}\right)
$$

where $h_{0}(t)$ is called the baseline hazard, which can be considered as a time varying intercept. Note that as a consequence the parameters $\beta_{1}, \ldots, \beta_{k}$ are lacking an intercept $\beta_{0}$. Cox regression is called semi-parametric due to its non-parametric part $h_{0}(t)$ and the remaining parametric part.
An interpretation of the model coefficients $\beta_{j}$ can be given in terms of hazard ratios (HR)

$$
\frac{h_{0}(t) \exp \left(\beta_{1} x_{1}+\cdots+\beta_{j}\left(x_{j}+1\right)+\cdots+\beta_{k} x_{k}\right)}{h_{0}(t) \exp \left(\beta_{1} x_{1}+\cdots+\beta_{k} x_{k}\right)}=\exp \left(\beta_{j}\right)
$$

Thus, the hazard ratio of increasing $x_{j}$ by one unit over $\boldsymbol{x}$ is $\exp \left(\beta_{j}\right)$. Note that this ratio is independent of time $t$, the proportion remains constant, which is the reason for calling Cox regression a proportional hazards model. AFT does not have this property.
In order to model whether an event happens over a 10-year time horizon - just like for logistic regression $\mu_{1}(\boldsymbol{x})$ in Section 3.1 - we define

$$
\mu_{2}(\boldsymbol{x}):=1-\exp \left(-\int_{0}^{10} h(t \mid \boldsymbol{x}) d t\right)
$$

In the code notebook we are using the Python package lifelines:

```
import lifelines as 11
cph = 11.CoxPRFitter()
cph.fit(time_to_event, "T", event_col="E", formula="SBP+BMI+I(BMI**2)")
pred = (1 - np.array(cph.predict_survival_function(time_to_event_test))[10,:])
```

## Page 18
In absence of covariates or in case of only very few categorical covariates, the Kaplan-Meier estimator is often used as a complement or an alternative to Cox regression. Either for the full dataset or separately for parts of the dataset based on some categorical covariates (e.g., males and females). The Kaplan-Meier estimator derives the empirical survival curve, i.e., the probability of the event not happening until time $t$, see Figure 6 on dataset $\mathcal{D}_{1}$.

Figure 6: Kaplan-Meier estimator for dataset $\mathcal{D}_{1}$, i.e., the empirical probability of a CVD event not happening until time $t$, and $95 \%$ confidence intervals.

# 3.3 Neural networks 

Although it is controversial to define neural networks as non-parametric, the journey from logistic regression via Cox regression to neural networks can be considered a path from parametric to semi-parametric to non-parametric models, in the sense that usually there are so many parameters in a neural network such that it seems more appropriate to speak of a non-parametric model. We are using a simple feed-forward neural network with 3 hidden layers, see Table 2 for an overview of layers and number of parameters. Analogously to logistic regression, we omit the variable time_to_event and only consider the binary $y=$ event as target variable. Figure 7 shows how the binary cross entropy (loss) is decreasing both for the training and validation subset of $\mathcal{D}_{2}$. After around 50 epochs the validation loss reaches a minimum. In the code notebook we are using the tensorflow/keras package:

```
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense, Activation
model = Sequential({
    Input(shape=(10,)),
    Dense(256),
    Activation(tf.keras.activations.relu),
    Dense(128),
    Activation(tf.keras.activations.relu),
    Dense(64),
    Activation(tf.keras.activations.relu),
    Dense(1, activation = "sigmoid")
    })
model.compile(optimizer = opt, loss = 'binary_crossentropy')
model.fit(X_train, y_train, batch_size = 64, epochs = 100, shuffle = True, validation_split = 0.20)
pred = model.predict(X_test).flatten()
```

The functional form of the neural network with 3 hidden layers on dataset $\mathcal{D}_{2}$ with 10 input variables is given by
![Page 18 Image 1](cs15_privacy_preserving_machine_learning_assets/cs15_privacy_preserving_machine_learning_p18_img1.jpg)

## Page 19
Table 2: Structure of the feed-forward neural network to predict mortality rates on dataset $\mathcal{D}_{2}$, with $44^{\prime} 033$ learnable parameters.

| Layer | input size | output size | \#parameters | input from layer $\kappa$ |
| :-- | :--: | :--: | :--: | :--: |
| Fully-conn. | 10 | 256 | $2^{\prime} 816$ | 0 |
| ReLU $\phi$ | 256 | 256 | 0 | 1 |
| Fully-conn. | 256 | 128 | $32^{\prime} 896$ | 1 |
| ReLU $\phi$ | 128 | 128 | 0 | 2 |
| Fully-conn. | 128 | 64 | $8^{\prime} 256$ | 2 |
| ReLU $\phi$ | 64 | 64 | 0 | 3 |
| Fully-conn. | 64 | 1 | 65 | 3 |
| Sigmoid output | 1 | 1 | 0 | 4 |

$$
\begin{aligned}
\mu_{3}(\boldsymbol{x}) & =\boldsymbol{z}^{(4)} \circ \boldsymbol{z}^{(3)} \circ \boldsymbol{z}^{(2)} \circ \boldsymbol{z}^{(1)}(\boldsymbol{x}), \text { where } \\
z_{j}^{(\kappa)}(\boldsymbol{z}) & =\phi^{(\kappa)}\left(\beta_{0, j}^{(\kappa)}+\sum_{\ell=1}^{6 \sim 1} \beta_{\ell, j}^{(\kappa)} z_{\ell}\right), \text { for } 1 \leq j \leq q_{\kappa} \\
\phi^{(\kappa)}(x) & =\left\{\begin{array}{l}
1 /(1+\exp (-x)) \\
x \mathbb{1}_{\{x \geq 0\}}
\end{array}, \kappa=4\right. \\
\left(q_{4}, \ldots, q_{0}\right) & =(1,64,128,256,10)
\end{aligned}
$$

Note that if we would remove the 3 hidden layers $\boldsymbol{z}^{(1)}, \boldsymbol{z}^{(2)}, \boldsymbol{z}^{(3)}$, the neural network is equivalent to logistic regression $\mu_{1}(\boldsymbol{x})$, minimizing the same deviance (loss) function given in Equation (3.2).

Figure 7: Binary cross entropy during each epoch on a training and validation subset of $\mathcal{D}_{2}$.

# 3.4 Model performance comparison 

As performance metrics, we consider for all 3 models $\mu_{i}(\boldsymbol{x})$ and both datasets $\mathcal{D}_{1}$ and $\mathcal{D}_{2}$, in increasing order of relevance

- Area under the receiver operating characteristic curve (ROC AUC),
![Page 19 Image 1](cs15_privacy_preserving_machine_learning_assets/cs15_privacy_preserving_machine_learning_p19_img1.jpg)

## Page 20
- Mean squared error (MSE) with respect to the log ground truth $\log \left(\mu^{*}(\boldsymbol{x})\right)$

$$
\frac{1}{|\mathcal{D}|} \sum_{j=1}^{|\mathcal{D}|}\left(\log \left(\mu_{i}\left(\boldsymbol{x}_{j}\right)\right)-\log \left(\mu^{*}\left(\boldsymbol{x}_{j}\right)\right)\right)^{2}
$$

- logistic deviance, binary cross entropy

$$
-2 \sum_{j=1}^{|\mathcal{D}|} y_{j} \operatorname{logit}\left(\mu_{i}\left(\boldsymbol{x}_{j}\right)\right)+\log \left(1-\mu_{i}\left(\boldsymbol{x}_{j}\right)\right)=-2 \sum_{j=1}^{|\mathcal{D}|} y_{j} \log \left(\mu_{i}\left(\boldsymbol{x}_{j}\right)\right)+\left(1-y_{j}\right) \log \left(1-\mu_{i}\left(\boldsymbol{x}_{j}\right)\right)
$$

- Kullback-Leibler divergence

$$
\sum_{j=1}^{|\mathcal{D}|} y_{j} \log \left(y_{j} / \mu_{i}\left(\boldsymbol{x}_{j}\right)\right)
$$

More complex performance metrics might be useful in practice, considering aspects like cashflow evaluations, propensity to buy conditional on premiums, etc.
As visual performance metrics we consider calibration plots, partial dependence plots, and individual conditional expectations.
We start assessing the performance of the 3 models $\mu_{i}(\boldsymbol{x})$ on dataset $\mathcal{D}_{1}$ and conclude from Table 3 and Figure 8 that logistic regression and Cox regression provide similar performance results, while the non-parametric neural network shows worse results. Despite more than 600 thousand individuals and a reasonably long observation period of 10 years, there are only around 5 thousand events. The dataset $\mathcal{D}_{1}$ is not sufficiently large to make the neural network outperform the (semi-)parametric models, where the chosen functional form matches the ground truth rather well.
The ordering of the models in terms of performance changes as expected on the richer dataset $\mathcal{D}_{2}$ where the neural network outperforms the other two models because of

- a larger sample size of more than 300 thousand events,
- more covariates,
- non-(logit/log)-linear marginals, e.g., age, num1,
- non-additive interactions, e.g., num2 and num3.

Note that the rank based ROC AUC is high mainly because age and gender alone are already very good predictors. The ROC AUC of simply sorting all individuals of $\mathcal{D}_{2}$ by age $-6 \cdot$ gender already provides an ROC AUC of $87.82 \%$.

Table 3: Performance metrics on the test data subset of $\mathcal{D}_{1}$.

| Performance metric | logistic regression $\mu_{1}(\boldsymbol{x})$ | Cox regression $\mu_{2}(\boldsymbol{x})$ | neural net $\mu_{3}(\boldsymbol{x})$ |
| :-- | :--: | :--: | :--: |
| ROC AUC | $56.17 \%$ | $56.17 \%$ | $56.04 \%$ |
| MSE wrt $\log \left(\mu^{*}(\boldsymbol{x})\right)$ | 0.0016 | 0.0016 | 0.0057 |
| Logistic deviance | 9223.88 | 9223.88 | 9227.72 |
| Kullback-Leibler | 3807.96 | 3807.97 | 3839.38 |

## Page 21
Figure 8: Calibration plots of logistic regression, Cox regression, and the neural network on the test data subset of $\mathcal{D}_{1}$.

Table 4: Performance metrics on the test data subset of $\mathcal{D}_{2}$.

| Performance metric | logistic regression $\mu_{1}(\boldsymbol{x})$ | Cox regression $\mu_{2}(\boldsymbol{x})$ | neural net $\mu_{3}(\boldsymbol{x})$ |
| :-- | :--: | :--: | :--: |
| ROC AUC | $90.54 \%$ | $90.55 \%$ | $92.05 \%$ |
| MSE wrt $\log \left(\mu^{*}(\boldsymbol{x})\right)$ | 1.74 | 1.75 | 0.11 |
| Logistic deviance | 85383 | 83994 | 75732 |
| Kullback-Leibler | 27648 | 26475 | 24622 |


Figure 9: Calibration plots of logistic regression, Cox regression, and the neural network on the test data subset of $\mathcal{D}_{2}$.

# 3.5 Discrimination-free insurance pricing 

Before we introduce in Section 4 how to run the models on encrypted data without having to access the (plain) individual data records, we mention another closely related data access challenge in practice. Often, for a given dataset many individual (non-protected) attributes are accessible, while some attributes are considered as protected and thus made not accessible. One of the main points investigated in [30] is to show that the unawareness of the protected attributes, i.e., not having access to these attributes, still leads to discrimination when there are dependencies between protected and non-protected attributes. We can also demonstrate this on dataset $\mathcal{D}_{2}$ assuming that binary is a protected attribute and all other attributes are accessible. Let $n_{0}$ and $n_{1}$ be the number of individuals with binary equal to 0 and 1 . Let group $A$ be those individuals with num3 $<0.5$ and group $B$ be those individuals with num3 $\geq 0.5$. We obtain the following best-estimate $\mu(\boldsymbol{x} \mid$ group, binary), unawareness $\mu(\boldsymbol{x} \mid$ group $)$, and discriminationfree prices $\mu(\boldsymbol{x} \mid$ group, 0$) n_{0} /\left(n_{0}+n_{1}\right)+\mu(\boldsymbol{x} \mid$ group, 1$) n_{1} /\left(n_{0}+n_{1}\right)$, see Table 5 , where $\mu$ denotes the empirical mortality rates of the test dataset of $\mathcal{D}_{2}$, and with the notation of [30] we used $\mathbb{P}^{*}(\boldsymbol{d})=\mathbb{P}(\boldsymbol{d})$ for discrimination-free prices without any further adjustments. Note the difference in prices between group $A$ and $B$ of the unawareness prices vs discrimination-free prices. The higher unawareness price of group $B$ is considered discriminatory. Privacy preserving methods thus can also help to mitigate this type of discrimination from unawareness.
![Page 21 Image 1](cs15_privacy_preserving_machine_learning_assets/cs15_privacy_preserving_machine_learning_p21_img1.jpg)
![Page 21 Image 2](cs15_privacy_preserving_machine_learning_assets/cs15_privacy_preserving_machine_learning_p21_img2.jpg)

## Page 22
Table 5: Best-estimate vs. unawareness vs. discrimination-free pricing.

|  | group $A$ | group $B$ |
| :--: | :--: | :--: |
|  | Number of individuals |  |
| binary $=0$ | 60371 | 42947 |
| binary $=1$ | 42760 | 60382 |
|  | Best-estimate prices |  |
| binary $=0$ | 0.039 | 0.108 |
| binary $=1$ | 0.081 | 0.185 |
|  | Unawareness prices |  |
| binary $\in\{0,1\}$ | 0.068 | 0.142 |
|  | Discrimination-free prices |  |
| binary $\in\{0,1\}$ | 0.074 | 0.133 |

# 4 Running models on encrypted data 

In this section, we will exemplify the use of a RLWE-based cryptosystem (CKKS, see Section 2.5) to run a logistic regression on encrypted data [28]. Logistic regression with $k$ variables and coefficients $\beta_{0}, \ldots, \beta_{k}$ on an input vector $\boldsymbol{x} \in \mathbb{R}^{k}$ involves evaluating Equation (3.1),

$$
\mu(\boldsymbol{x})=\frac{1}{1+\exp \left(-\beta_{0}-\beta_{1} x_{1}-\cdots-\beta_{k} x_{k}\right)}
$$

### 4.1 Simple example: evaluating a generalized linear model on encrypted data

The evaluation of a generalized linear model, or the computation of the output for each of the neurons of a multi-layer neural network is analogous, just potentially changing the activation function $1 /(1+\exp (-\cdot))$. Therefore, in this section, we will be using Equation (4.1) as running example. The four main points that have to be accounted for when working with homomorphic encryption are:

- choosing the cryptosystem parameters,
- input packing,
- function approximation,
- noise management for deep circuits.

Choosing the cryptosystem parameters. There are two factors that have to be considered when choosing the parameters of the used cryptosystem: correctness and security. Both are closely related, and one cannot be set without overlooking the other. In terms of correctness, parameters such as the moduli chain $\left\{q_{0}, \ldots, q_{L}\right\}$ and the input scale factor $\Delta$ have to be set so that the full dynamic range of the inputs, intermediate values and results can be contained within the plaintext space without overflowing the modulus $Q$ (which leads to decryption errors) or underflowing (which leads to loss of precision, with the message flooded by noise). The moduli chain also determines the number of levels that can be traversed when executing a circuit made of successive products, and whether the cryptosystem will operate as somewhat homomorphic (for shallow circuits or with interactions) or fully homomorphic (using bootstrapping, for deep circuits without interactions).
Conversely, the polynomial degree $n$ and the noise power (the variance of the noise distribution $\chi_{e}$ and the weight of the key distribution $\chi_{s}$ ) are chosen according to the Homomorphic Encryption standard [4] or by using the lattice estimator [5], in order to reach a desired security level in terms of bits of security; typically, the requirements are set for either 128-bits classical security or 128-bits post-quantum security,

## Page 23
depending on the assumptions and the required long-term protection. For a fixed bit security, $n$ depends on the chosen $Q_{L}$; i.e., the bigger $Q_{L}$, the larger $n$ has to be set in order to preserve the same security level. Larger parameters imply larger encryptions and therefore more bandwidth use and slower operations, so it is important to choose a tight parameterization to avoid an unnecessary overhead.
In the notebook examples, the used parameterization is the following

$$
\begin{aligned}
\log _{2}(n) & =14 \\
\left(\left\lceil\log _{2}\left(q_{0}\right)\right\rceil, \ldots,\left\lceil\log _{2}\left(q_{6}\right)\right\rceil\right) & =(50,45,45,45,45,45,45,45) \\
\left\lceil\log _{2}(P)\right\rceil & =50 \\
\left\lfloor\log _{2}(\Delta)\right\rfloor & =45
\end{aligned}
$$

This means that the polynomial degree is $n=2^{14}=16384$, and $\left\lceil\log _{2}\left(P Q_{L}\right)\right\rceil=415$, which, according to the Homomorphic Encryption security standard [4] guarantees a post-quantum security level of 128 bits $^{8}$; this can also be checked by using the lattice estimator [5]. Each moduli is of the same size of the input scale $\Delta$, except for the last modulus ( $q_{0}, 60$ bits), which is larger in order to cope with the growth of the input parameters after applying a computation chain. With a chain of 8 moduli we can enable circuits of depth 7 with controlled noise (e.g., homomorphically evaluating a polynomial of degree up to $2^{7}-1=127$, or a product chain of 7 levels), running a rescale operation after each level.

Input packing. Let $A^{\prime}$ be an input matrix of size $\ell \times k$, representing $\ell$ data records with $k$ variables each. Let $A=\left[1 A^{\prime}\right]$ represent the block matrix that concatenates a column of ones (regression intercept) and $A^{\prime}$. One single CKKS encryption can hold up to $n / 2$ complex scalar values. Therefore, there are at least two ways in which we can pack the inputs to take advantage of the SIMD operations offered by the cryptosystem:

- Horizontal packing. If $(k+1) \leq n$, each data record (row) in $A$ can be packed into one encryption using $k+1$ consecutive values ( $k$ input values plus the intercept), as can the $k+1$ regression coefficients $\beta_{i}$ (in reverse order). In this case, the input vector can be directly coded in the polynomial coefficients; i.e., the input plaintext messages for data record $i$ and for the regression coefficients are

$$
\begin{aligned}
\boldsymbol{m}_{j} & =\sum_{i=0}^{k} a_{j, i} x^{i} \rightarrow \boldsymbol{c}_{\boldsymbol{m}_{j}}=\operatorname{enc}\left(\boldsymbol{m}_{j}\right) \\
\boldsymbol{\beta} & =\sum_{i=0}^{k} \beta_{k-i} x^{i} \rightarrow \boldsymbol{c}_{\boldsymbol{\beta}}=\operatorname{enc}(\boldsymbol{\beta})
\end{aligned}
$$

The homomorphic product between the two encryptions encodes the polynomial product between the input and the regression coefficients

$$
\begin{aligned}
\operatorname{dec}\left(\boldsymbol{c}_{m_{j}} \cdot \boldsymbol{c}_{\beta}\right) & \approx\left(\sum_{i=0}^{k} a_{j, i} x^{i}\right) \cdot\left(\sum_{i=0}^{k} \beta_{k-i} x^{i}\right)=\sum_{i=0}^{k} \sum_{u=0}^{k} a_{j, i} \beta_{k-u} x^{i+u} \\
& =\left(\sum_{i=0}^{k} a_{j, i} \beta_{i}\right) x^{k}+\sum_{i=0}^{k} \sum_{u=0, u \neq k-i}^{k} a_{j, i} \beta_{k-u} x^{i+u}
\end{aligned}
$$

It can be seen that the plaintext coefficient in $x^{k}$ holds the result of the scalar product between the $j$-th row of $A$ and $\boldsymbol{\beta}$. Under encryption, it can be extracted and masked by a transformation of the message to the slot domain, so that it can be used for the next steps of the process (the activation

[^0]
[^0]:    ${ }^{8}$ There are further considerations to account for in order to determine the security level, which relate to the key distribution and weight; these are out of scope for this tutorial, and we refer the reader to [5].

## Page 24
function). The rest of the coefficients are discarded (masked to 0 before decryption), which means that the resulting ciphertext only holds one scalar value. If $k \leq\lfloor n / r\rfloor$ for an integer $r$, then it is possible to pack $r$ input records in a single encryption (e.g., $m_{\text {pack0 }}=\sum_{j=0}^{r-1} x^{2 k j} m_{j}$ ), and extract $r$ scalar product results from each ciphertext product. See Figure 10 for a visual representation of this product with horizontal packing and coefficient encoding.

Figure 10: Horizontal packing: Each color within the same data block represents one ciphertext, and each square represents a scalar plaintext coefficient in that ciphertext. Ciphertexts of the same color are operands or results of the same operation. Lighter squares represent empty or discarded coefficients. Input encoding is on the coefficient domain, so the product of ciphertexts represents the polynomial product of the inputs. Each row of $A$ is encoded in one ciphertext and homomorphically multiplied by the encryption of $\boldsymbol{\beta}$.

- Vertical packing. If the number of records is $\ell \geq(k+1)$, it is more efficient to pack each regression variable in one ciphertext. In this case, it is preferable to encode the message in the slot domain, as a vector, so the homomorphic operations are component-wise additions and products, and the resulting scalar product is already in the correct domain for the activation. Therefore, if $\ell \leq n / 2$, each column of the matrix $A$ is encoded in a single plaintext, whereas regression coefficients $\beta_{i}$ are encoded using a repetition code, each one in a separate plaintext

$$
\begin{aligned}
\boldsymbol{m}_{j} & =\left(a_{0, j}, \ldots, a_{\ell-1, j}, 0, \ldots, 0\right) \rightarrow \boldsymbol{c}_{\boldsymbol{m}_{j}}=\operatorname{enc}\left(\boldsymbol{m}_{j}\right) \\
\boldsymbol{\beta}_{j} & =\left(\beta_{j}, \ldots, \beta_{j}\right) \rightarrow \boldsymbol{c}_{\boldsymbol{\beta}_{j}}=\operatorname{enc}\left(\boldsymbol{\beta}_{j}\right)
\end{aligned}
$$

Then, the scalar product can be computed in parallel across all the packed records:

$$
\operatorname{dec}\left(\boldsymbol{c}_{\boldsymbol{\beta}_{0}}+\sum_{j=1}^{k} \boldsymbol{c}_{\boldsymbol{m}_{j}} \cdot \boldsymbol{c}_{\boldsymbol{\beta}_{j}}\right) \approx\left(\beta_{0}+\sum_{j=1}^{k} a_{i, j} \beta_{j}\right)_{i=0}^{\ell-1}
$$

The result is a vector that holds in each slot the scalar product between the corresponding input record and the regression coefficients. If $\ell=r n / 2$, with $r$ integer, each column of the input matrix $A$ is packed and encrypted across $r$ ciphertexts, for which the full packing capacity is used, and no slots are discarded. The space required to encode/encrypt the regression coefficients is larger compared to the horizontal packing ( $k$ ciphertexts versus 1 single ciphertext), but there is no need to encode/encrypt the vector of 1 used for the intercept, the encoding for the input data is much more efficient, and there is no need to change domain for the output vector of scalar products, which is already encoded in the slot domain, ready to be used as input for the evaluation of the activation function. See Figure 11 for a visual representation of this product with vertical packing and slot encoding.
Each of the two packing strategies presents advantages and disadvantages, and they have to be chosen depending on the geometry of the input matrix and the subsequent processing that has to be applied to the outputs of the scalar product.
![Page 24 Image 1](cs15_privacy_preserving_machine_learning_assets/cs15_privacy_preserving_machine_learning_p24_img1.jpg)

## Page 25
Figure 11: Vertical packing: Each color within the same data block represents one ciphertext, and each square represents a scalar plaintext slot in that ciphertext. Ciphertexts of the same color are operands or results of the same computation. Input encoding is on the slot domain, so the product of ciphertexts represents the component-wise product of the inputs. Each column of $A$ is encoded in one ciphertext and multiplied by the corresponding element of $\boldsymbol{\beta}$, which is repetition-coded in all slots of a single ciphertext. All the resulting ciphertexts are added together to obtain the final result, encoded in the slots of a single ciphertext. No slots are discarded.

Function approximation. The arithmetic supported by the homomorphism comprises ring operations (additions and products), and therefore, polynomial functions can be natively run under encryption. In order to compute a non-polynomial function, it has to be either (a) approximated by a polynomial or (b) run on universal gates (nand and xor) with binary arithmetic in $\mathbb{Z}_{2}$, mimicking the binary representation of the inputs and of the mathematical operations inside the arithmetic-logic unit in current computer processors. CKKS is more suited to polynomial arithmetic, so we will focus on the first approach. For completeness, we highlight three typically used polynomial approximations for a function $f(x): \mathbb{R} \rightarrow \mathbb{R}$ within an interval $[a, b] \in \mathbb{R}$ :

- Taylor approximation. Let $f(X)$ be $d+1$-differentiable within the interval $[a, b]$, and let $c$ be a point in this interval. The degree- $d$ Taylor polynomial of $f(x)$ around $c$ can be defined as $p_{T}(x)=$ $f(c)+f^{(1)}(c)(x-c)+\cdots+\frac{1}{d!} f^{(d)}(c)(x-c)^{d}$, where $f^{(i)}(c)$ is the $i$-th derivative of $f(x)$. The approximation error can be bounded by $\left|p_{T}(x)-f(x)\right|<\max _{y \in(c, x)}\left|\frac{1}{(d+1)!} f^{(d+1)}(y)(x-c)^{d+1}\right|$. Therefore, the error is not uniform in the interval $[a, b]$, and it is more tightly bounded for points closer to $c$. A Taylor approximation is preferred when the distribution of the input to the to-be-approximated function is denser around $c$ than on the extremes of the interval; e.g., for a Gaussian-distributed input.
- Least-squares approximation. The degree- $d$ least squares polynomial $p_{L}(x)=\sum_{j=0}^{d} p_{j} x^{j}$ of $f(x)$ in a set of $k$ different points $\left\{x_{i}\right\}_{i=0}^{k-1}$, with $x_{i} \in[a, b]$, is computed as the polynomial that minimizes the squared error $\sum_{i=0}^{k-1}\left|f\left(x_{i}\right)-p_{L}\left(x_{i}\right)\right|^{2}$. As all inputs to a homomorphic circuit have to be quantized to be encoded into plaintexts, the points $x_{i}$ are chosen as the centroids of the used quantizer that fall within the interval $[a, b]$, as defined by the scale factor $\Delta$ used in the plaintext encoding. If the interval $[a, b]$ spans a large number of centroids, the least squares polynomial can also be approximated by minimizing the integral of the squared error over the continuous interval $[a, b]$. The least squares approximation is preferred when the inputs are uniformly distributed and the homomorphic capacity is large enough to absorb large individual approximation errors without producing an overflow. In this case, only the average error is relevant to determine the quality of the approximation.
- Chebyshev approximation. The degree- $d$ Chebyshev approximation of $f^{*}(x)$ in $(-1,1)^{9}$ can be de-

[^0]
[^0]:    ${ }^{9} f^{*}(x)$ is defined by the affine transformation on the inputs to $f(x)$ to bring the interval $(a, b)$ to $(-1,1)$
![Page 25 Image 1](cs15_privacy_preserving_machine_learning_assets/cs15_privacy_preserving_machine_learning_p25_img1.jpg)

## Page 26
fined as $p_{C}(x)=\sum_{k=0}^{d} c_{k} T_{k}(x)-\frac{1}{2} c_{0}$, where $T_{k}(x)$ is the $k$-th Chebyshev polynomial of the first kind, and $c_{j}=\frac{2}{d+1} \sum_{k=1}^{d+1} f^{*}\left(x_{k}\right) T_{j}\left(x_{k}\right)$, with $\left\{x_{k}\right\}$ the Chebyshev nodes in $(-1,1)$. The Chebyshev approximation polynomial has a bounded maximum error, and it converges with $d$ to the minimax polynomial that minimizes this maximum approximation error in the considered interval. This is especially useful when the used cryptosystem is parameterized with a very tight homomorphic capacity, so error outliers could produce an overflow even when the average error is bounded (e.g., using least-squares polynomial approximations). The use of Chebyshev approximations can therefore help to reduce the probability of an overflow in chained homomorphic computations.

With the packing strategy to compute the scalar product, and the activation function represented as an approximation polynomial of degree $d$, we have all the required building blocks to evaluate a logistic regression model on the input matrices of data $A$, as a homomorphic circuit of depth $\left\lceil\log _{2}(d+1)\right\rceil+1$. The following code snippet shows how to run the encrypted regression loop end to end with vertical packing and slot encoding, using Tune Insight's ${ }^{10}$ Python cryptolib, which wraps the cryptographic functions of the Lattigo homomorphic encryption library [27]:

```
from tuneinsight.cryptolib.hefloat import hefloat
import numpy as np
import numpy.polynomial.chebyshev as chebyshev
# Parameterization: scale/precision and circuit depth
log_scale = 45 # Fixed-point arithmetic floating point scaling factor in bits (log2(Delta))
levels = 7 # Circuit depth
log_qi = [log_scale+5] + levels*[log_scale] # 5 additional bits for the lowest level,
                                    # to account for plaintext growth
log_pi = [log_scale+5] # Auxiliary module used for relinearization
                                    # (usually, at least of the same size as the lowest level q0)
# In order to generate an instance of the cryptosystem, the RLVE ring degree is automatically chosen
# to ensure at least 128-bit of security
# A context stores the scheme cryptographic parameters and a key generator
context = hefloat.new_context(log_qi = log_qi, log_default_scale= log_scale, log_pi = log_pi)
# Generate a fresh secret key
sk = context.new_secret_key()
# Instantiate an evaluator with a relinearization key. This is a public-evaluation key required
# to ensure ciphertext x ciphertext compactness
# The resulting evaluator object contains only public information and can be freely shared
evaluator = context.new_evaluator(context.new_relinearization_key(sk))
```

The data and regression coefficients (randomly generated for the purpose of exemplifying the workflow) are encrypted in the slot domain:

```
# Generate random data for 8192 records and 200 regression variables
# Number of samples to process in parallel (available plaintext slots that one encryption can hold)
batch_size = context.slots()
# Number of features (k=200)
features = 200
# Generate random data in [-0.5, 0.5]. This is the matrix A'
data = np.random.rand(batch_size, features)-0.5
# Generate random regression weights in [0, 1]. These represent beta_i, i=1,...,k
weights = np.random.rand(features, 1)
# Generate random bias (intercept coefficient) in [0, 1]. This represents beta_0
bias = np.random.rand(1)
# Batched (slot) packing
batched = True
# The encrypt function can receive a two-dimensional matrix as input, in which case
# it encrypts each row of the input matrix in one ciphertext.
# The function returns an object that stores a vector of ciphertexts.
encrypted_data = context.encrypt(data.transpose().copy(), sk, batched)
```

${ }^{10}$ https://tuneinsight.com

## Page 27
```
# We encrypt each of the weights replicated in all slots of the corresponding ciphertext.
encrypted_weights = context.encrypt(np.tile(weights, (1, batch_size))* 2/(b-a), sk, batched)
# The intercept coefficient or bias is also encrypted in its sum ciphertext,
# with the same repetition coding as all the other regression coefficients
encrypted_bias = context.encrypt(np.tile(bias, (1, batch_size))* 2/(b-a) + (-a-b)/(b-a), sk, batched)
```

The server can then perform the scalar product and evaluate the activation function, which is represented with a Chebyshev approximation polynomial of degree 32:

```
# Expected interval of the encrypted values after the scalar product
a = -12
b = 12
# Interpolates the Sigmoid in the interval [-12, 12] and returns the coefficients
# for the Chebyshev approximation polynomial in the Chebyshev basis
coeffs = chebyshev.chebinterpolate(lambda x: 1/(1+np.exp(-((b-a)/2 * x + (b+a)/2))), 63)
# Encrypted evaluation of data @ weights:
# np.sum(data.transpose() * np.tile(bias, (1, batch_size)), axis=0)
encrypted_scalar_product = evaluator.scalar_product(encrypted_data, encrypted_weights)
# Encrypted evaluation of data @ weights + bias
encrypted_scalar_product_plus_bias = evaluator.add(encrypted_bias, encrypted_scalar_product)
# Encrypted evaluation of sigmoid(data @ weights + bias)
encrypted_prediction = evaluator.polynomial(encrypted_scalar_product_plus_bias, coeffs=coeffs, basis="Chebyshev")
```

Finally, the client can decrypt the results, which are given as a vector of estimations for all the input records:
prediction = context.decrypt(encrypted_prediction, sk)[:, batch_size]

Noise/level management for deep circuits. The moduli chain for the cryptosystem can be configured to support the depth of the whole circuit, so the described process can be implemented without requiring any bootstrapping operation as long as this evaluation is the final result of the encrypted computation.
If this evaluation is part of a deeper circuit or an iterative training loop, such as a gradient descent loop for adjusting the regression coefficients, then a bootstrapping operation will be needed in order to enable running an arbitrary number of iterations. In this case, the moduli chain has to be configured to at least support the execution of the bootstrapping circuit and the evaluation of the scalar product and the activation function; then, one bootstrapping would be needed after every regression evaluation [20]. If the trained model is a multi-layer neural network, this configuration would require one bootstrapping after the evaluation of each layer. The bootstrapping is the costliest basic homomorphic operation, so minimizing the number of required bootstrappings is fundamental to optimize the execution overhead. For this purpose, it is possible to configure a longer moduli chain to support more than one layer between two bootstrapping operations; in order to keep the same required security level after increasing $Q_{L}$, a higher degree $n$ would be needed; as a consequence, this change will imply larger ciphertexts with larger packing capacity, but also costlier base operations (additions and products). Hence, there is a point where there are no efficiency gains by further increasing the ciphertext size, and this is the optimal parameterization where the cost of the bootstrapping is compensated by the higher efficiency of the operations with smaller ciphertexts [46]. We refer the interested reader to $[20,46]$ for further details on how to run an encrypted iterative gradient descent loop for generalized linear models and an encrypted backpropagation loop with multi-layer perceptrons, respectively.

# 4.2 Practical applications to partitioned data and federated problems. 

So far we have focused on outsourcing problems, where there is a need to compute on personal or confidential data in an untrustworthy environment (such as a cloud). Therefore, the workflow can be

## Page 28
Table 6: ROC AUC results when running a centralized regression vs federated vs encrypted federated regression on dataset $\mathcal{D}_{2}$, in the same conditions as Table 4.

|  | Logistic regression | Cox regression |
| :-- | :--: | :--: |
| Local | 0.9056 | 0.9163 |
| Federated | 0.9045 | 0.9165 |
| Secure Federated | 0.9045 | 0.9006 |

represented as (1) client encryption of the input data, (2) transmission of the encrypted data to the server, (3) server homomorphic computation, (4) transmission of the encrypted results to the client, (5) client decryption of the results.
This setting is relevant when all the data is owned or hosted by a single party (a single company or a single site), but this is typically not the case in machine learning scenarios, where (a) data from a single organization is insufficient to train a representative and generalizable model, or (b) data cannot be transferred to a geography subject to a different data protection regulatory framework (e.g., data transfers between United States and Europe), or (c) it cannot be transferred between different sectors (e.g., clinical data from hospitals and claims data from insurers). In these cases, data has to remain at the local controller, and the process needs to be federated in order to avoid the transfer of the raw data. The vanilla variants of federated learning and federated analytics do not provide any guarantee in terms of prevention of reidentification or membership inference attacks, because they incur in an inherent leakage, that has been highlighted and exploited in many recent publications [26, 50, 51, 33, 37]. In order to mitigate or avoid this leakage, it is possible to use the homomorphic encryption techniques introduced above in a federated setting, where there are multiple parties (data owners) contributing their data to the collective training process. Moreover, the local data does not have to be encrypted during the local process, because it happens within the security boundaries of its own data controller; instead, encryption is used to protect the aggregates (e.g., the local models) exported from each site, to support the collective aggregation of all local contributions and produce the encrypted global result, hence avoiding the disclosure of any partial results or local contributions. In this case, the secret key or the capacity of decrypting encrypted results can also be federated, by using a threshold cryptosystem [36]. Threshold cryptosystems require the participation of multiple parties in order to complete a decryption of a ciphertext, in such a way that no single party is able to decrypt any ciphertext by itself.
Besides the trust distribution that the use of threshold or distributed cryptosystems entails for the whole process, federated encrypted approaches are much more cost-effective than encrypting all the data from the different sites and sending it to a central processor, with significant gains in terms of both bandwidth use and computational overhead, and the same security and confidentiality guarantees for the data owners. We refer the interested reader to $[36,20,46]$ for further details, and to $[21,45,19]$ to find practical applications of these techniques in medical settings, including the secure federated computation of survival analyses, single cell analyses, and genomic analyses.
The companion notebook include a code sample using Tune Insight's full Python SDK, that represent a full secure federated learning pipeline for a Cox regression across three different data providers. In general, this training paradigm with encrypted aggregation can accept any model. The pre-trained models can also be encrypted and used for secure predictions. Besides the simple logistic regression example shown in the code snippets above, the SDK also enables the use of a more general Pytorch-defined model for running secure predictions. In particular, we have partitioned the dataset $\mathcal{D}_{2}$ in three independent subsets, simulating a scenario with three different hospitals or data sources. The results obtained in terms of ROC AUC are reported in Table 6, showing the comparison between a fully centralized and clear-text scenario (the same as in Section 3), a federated scenario (with no protection mechanisms applied to the data or models), and a federated encrypted training using both homomorphic encryption, which protects the data from the processor, and release protection mechanisms (i.e., differential privacy), which protects

## Page 29
the released decrypted results from the recipient, It can be seen that the performance of the obtained model is not materially impacted by the encrypted federated process, and there is a minimal impact from the use of differential privacy noise, which can be modulated depending on the privacy requirements of the target application. More in-depth details about the whole workflow and its evaluation can be found in the companion notebook.

# 5 Conclusion 

The ability to run models on sensitive (personal) data without the need to access unencrypted individual data records is beneficial in many practical applications and can unlock notable value. Homomorphic encryption is a key enabler for these scenarios, as it can protect data while in use, hence making it possible to securely process personal records to extract actionable insights without revealing to the processor or to any other party the contents of those personal records.
When data cannot be centralized or transferred, homomorphic encryption is not sufficient. The extension of homomorphic encryption called "multiparty" homomorphic encryption stems from the combination with other approaches such as federated analytics, data release protection (e.g., differential privacy), and secure multiparty computation. Together, they provide effective security measures that, when paired with appropriate organizational measures, can notably streamline compliance and also re-enable crossborder collaborations on personal data [10]. When there is a legal basis for processing personal data, a computation workflow can be authorized (e.g., computation of mortality statistics or training of (survival) models), even when this computation spans siloed or isolated data sources. This leads to larger datasets that become available for (actuarial) analyses where ML methods outperform classical methods as highlighted in Section 3.

## Acknowledgements

We would like to thank Theresa Blümlein, Andreas Troxler, and Mario Wüthrich for their comprehensive reviews and feedback that led to significant improvements of this tutorial. Furthermore, we would like to thank the Data Science Working Group of the SAV for supporting this work.

## References

[1] Case C-311/2018 Judgment of the court (grand chamber) of 16 July 2020. Data Protection Commissioner v Facebook Ireland Limited and Maximillian Schrems.
[2] Recommendations 01/2020 on measures that supplement transfer tools to ensure compliance with the EU level of protection of personal data.
[3] M. Ajtai. Generating hard instances of lattice problems (extended abstract). In Proceedings of the Twenty-Eighth Annual ACM Symposium on Theory of Computing, STOC '96, page 99-108, New York, NY, USA, 1996. Association for Computing Machinery.
[4] Martin Albrecht, Melissa Chase, Hao Chen, Jintai Ding, Shafi Goldwasser, Sergey Gorbunov, Shai Halevi, Jeffrey Hoffstein, Kim Laine, Kristin Lauter, Satya Lokam, Daniele Micciancio, Dustin Moody, Travis Morrison, Amit Sahai, and Vinod Vaikuntanathan. Homomorphic encryption security standard. Technical report, HomomorphicEncryption.org, Toronto, Canada, November 2018.
[5] Martin R. Albrecht, Rachel Player, and Sam Scott. On the concrete hardness of learning with errors. Journal of Mathematical Cryptology, 9(3):169-203, 2015.
[6] D. Boneh, E. Goh, and K. Nissim. Evaluating 2-DNF Formulas on Ciphertexts. In Proceedings of Theory of Cryptography (TCC) '05, LNCS 3378, pages 325-341, 2005.

## Page 30
[7] M J Bradburn, T G Clark, S B Love, and D G Altman. Survival analysis part ii: Multivariate data analysis - an introduction to concepts and methods. British Journal of Cancer, 89(3):431-436, Aug 2003 .
[8] Zvika Brakerski, Craig Gentry, and Vinod Vaikuntanathan. (leveled) fully homomorphic encryption without bootstrapping. In Proceedings of the 3rd Innovations in Theoretical Computer Science Conference, ITCS '12, page 309-325, New York, NY, USA, 2012. Association for Computing Machinery.
[9] Jung Hee Cheon, Andrey Kim, Miran Kim, and Yongsoo Song. Homomorphic encryption for arithmetic of approximate numbers. In Tsuyoshi Takagi and Thomas Peyrin, editors, Advances in Cryptology - ASIACRYPT 2017, pages 409-437, Cham, 2017. Springer International Publishing.
[10] Marcelo Corrales Compagnucci, Mark Fenwick, Mateo Aboy, and Timo Minssen. Supplementary Measures and Appropriate Safeguards for International Transfers of Personal Data after Schrems II. SSRN, 2022.
[11] McKinsey \& Company. Quantum Technology Monitor. https://www.mckinsey.com/ /media/mckinsey/business_functions_mckinsey\%20digital/our\%20insights/quantum\% 20computing\%20funding\%20remains\%20strong\%20but\%20talent\%20gap\%20raises\%20concern/ quantum-technology-monitor.pdf, 2022.
[12] D. R. Cox. Regression models and life-tables. Journal of the Royal Statistical Society: Series B (Methodological), 34(2):187-202, 1972.
[13] Human Mortality Database. Max Planck Institute for Demographic Research (Germany), University of California, Berkeley (USA), and French Institute for Demographic Studies (France). Available at www.mortality.org. Downloaded in December 2022.
[14] Cameron Davidson-Pilon. lifelines: survival analysis in python. Journal of Open Source Software, $4(40): 1317,2019$.
[15] T. ElGamal. A public key cryptosystem and a signature scheme based on discrete logarithms. IEEE Transactions on Information Theory, 31(4):469-472, 1985.
[16] European Parliament and Council of the European Union. Regulation (EU) 2016/679 of the European Parliament and of the Council.
[17] Junfeng Fan and Frederik Vercauteren. Somewhat practical fully homomorphic encryption. Cryptology ePrint Archive, Paper 2012/144, 2012. https://eprint.iacr.org/2012/144.
[18] World Economic Forum. State of Quantum Computing: Building a Quantum Economy. https: //www3.weforum.org/docs/WEF_State_of_Quantum_Computing_2022.pdf, 2022.
[19] D. Froelicher, H. Cho, M. Edupalli, J. Sa Sousa, J. Bossuat, A. Pyrgelis, J. R. Troncoso-Pastoriza, B. Berger, and J. Hubaux. Scalable and privacy-preserving federated principal component analysis. In 2023 IEEE Symposium on Security and Privacy (SP), pages 1908-1925, Los Alamitos, CA, USA, may 2023. IEEE Computer Society.
[20] David Froelicher, Juan R. Troncoso-Pastoriza, Apostolos Pyrgelis, Sinem Sav, Joao Sa Sousa, JeanPhilippe Bossuat, and Jean-Pierre Hubaux. Scalable Privacy-Preserving Distributed Learning. Proceedings on Privacy Enhancing Technologies Symposium, 2021.
[21] David Froelicher, Juan R Troncoso-Pastoriza, Jean Louis Raisaro, Michel A Cuendet, Joao Sa Sousa, Hyunghoon Cho, Bonnie Berger, Jacques Fellay, and Jean-Pierre Hubaux. Truly privacy-preserving federated analytics for precision medicine with multiparty homomorphic encryption. Nature communications, 12(1):1-10, 2021.

## Page 31
[22] Extended Composition) General Court (Eighth Chamber. Case t-557/20 single resolution board v european data protection supervisor. protection of personal data - procedure for granting compensation to shareholders and creditors following the resolution of a bank - decision of the edps in which it found that the srb failed to fulfil its obligations concerning the processing of personal data - article 15(1)(d) of regulation (eu) 2018/1725 - concept of personal data - article 3(1) of regulation 2018/1725 - right of access to the file.
[23] Craig Gentry. A fully homomorphic encryption scheme. PhD thesis, Stanford University, 2009. Short version: Fully homomorphic encryption using ideal lattices, at Symposium on the Theory of Computing (STOC), 2009, pp. 169-178.
[24] S. Goldwasser and S. Micali. Probabilistic encryption and how to play mental poker keeping secret all partial information. In STOC '82 Proceedings of the 14th annual ACM Symposium on Theory of Computing, pages 365-377, 1982.
[25] Julia Hippisley-Cox, Carol Coupland, and Peter Brindle. Development and validation of QRISK3 risk prediction algorithms to estimate future risk of cardiovascular disease: prospective cohort study. $B M J, 357,2017$.
[26] Briland Hitaj, Giuseppe Ateniese, and Fernando Perez-Cruz. Deep models under the GAN: information leakage from collaborative deep learning. In ACM CCS, 2017.
[27] Tune Insight and EPFL LDS. Lattigo: A Library For Lattice-Based Homomorphic Encryption in Go. https://github.com/tuneinsight/lattigo, (accessed: August 2023).
[28] Miran Kim, Yongsoo Song, Shuang Wang, Xia Yuhou, and Xiaoqian Jiang. Secure logistic regression based on homomorphic encryption: Design and evaluation. JMIR Medical Informatics, 6, 082017.
[29] Arjen K Lenstra, Hendrik W Lenstra Jr, Mark S Manasse, and John M Pollard. The number field sieve. In Proceedings of the twenty-second annual ACM symposium on Theory of computing, pages $564-572,1990$.
[30] M. Lindholm, R. Richman, A. Tsanakas, and M.V. Wüthrich. Discrimination-free insurance pricing. ASTIN Bulletin: The Journal of the IAA, 52(1):55-89, 2022.
[31] Vadim Lyubashevsky, Chris Peikert, and Oded Regev. On ideal lattices and learning with errors over rings. In Henri Gilbert, editor, Advances in Cryptology - EUROCRYPT 2010, pages 1-23, Berlin, Heidelberg, 2010. Springer Berlin Heidelberg.
[32] Vadim Lyubashevsky, Chris Peikert, and Oded Regev. On ideal lattices and learning with errors over rings. J. ACM, 60(6), nov 2013.
[33] L. Melis, C. Song, E. De Cristofaro, and V. Shmatikov. Exploiting unintended feature leakage in collaborative learning. In IEEE S\&P, 2019.
[34] Gary L. Miller. Riemann's hypothesis and tests for primality. Journal of Computer and System Sciences, 13(3):300-317, 1976.
[35] Victor S. Miller. Use of elliptic curves in cryptography. In Hugh C. Williams, editor, Advances in Cryptology - CRYPTO '85 Proceedings, pages 417-426, Berlin, Heidelberg, 1986. Springer Berlin Heidelberg.
[36] Christian Mouchet, Juan R. Troncoso-pastoriza, Jean-Philippe Bossuat, and Jean Pierre Hubaux. Multiparty homomorphic encryption from ring-learning-with-errors. In Proceedings on Privacy Enhancing Technologies Symposium, 2021.

## Page 32
[37] M. Nasr, R. Shokri, and A. Houmansadr. Comprehensive privacy analysis of deep learning: Passive and active white-box inference attacks against centralized and federated learning. In IEEE S\&P, 2019 .
[38] Pascal Paillier. Public-key cryptosystems based on composite degree residuosity classes. In Jacques Stern, editor, Advances in Cryptology - EUROCRYPT '99, pages 223-238, Berlin, Heidelberg, 1999. Springer Berlin Heidelberg.
[39] Chris Peikert. A decade of lattice cryptography. Found. Trends Theor. Comput. Sci., 10(4):283-424, mar 2016 .
[40] C. Pomerance. Analysis and comparison of some integer factoring algorithms. In H. W. Lenstra, Jr. and R. Tijdeman, editors, Computational Methods in Number Theory, pages 89-139. Math. Centrum Tract 154, Amsterdam, 1982.
[41] Oded Regev. On lattices, learning with errors, random linear codes, and cryptography. In Proceedings of the Thirty-Seventh Annual ACM Symposium on Theory of Computing, STOC '05, page 84-93, New York, NY, USA, 2005. Association for Computing Machinery.
[42] R L Rivest, L Adleman, and M L Dertouzos. On data banks and privacy homomorphisms. Foundations of Secure Computation, Academia Press, pages 169-179, 1978.
[43] Ronald L. Rivest, Adi Shamir, and Leonard M. Adleman. A method for obtaining digital signatures and public-key cryptosystems. Commun. ACM, 21:120-126, 1978.
[44] Miruna Rosca, Damien Stehlé, and Alexandre Wallet. On the ring-lwe and polynomial-lwe problems. In Jesper Buus Nielsen and Vincent Rijmen, editors, Advances in Cryptology - EUROCRYPT 2018, pages 146-173, Cham, 2018. Springer International Publishing.
[45] Sinem Sav, Jean-Philippe Bossuat, Juan R Troncoso-Pastoriza, Manfred Claassen, and Jean-Pierre Hubaux. Privacy-preserving federated neural network learning for disease-associated cell classification. Patterns, 3(5):100487, 2022.
[46] Sinem Sav, Apostolos Pyrgelis, Juan R Troncoso-Pastoriza, David Froelicher, Jean-Philippe Bossuat, Joao Sa Sousa, and Jean-Pierre Hubaux. POSEIDON: Privacy-Preserving Federated Neural Network Learning. NDSS, 2021.
[47] J Scheibner, J Raisaro, JR Troncoso-Pastoriza, M Ienca, J Fellay, E Vayena, and Hubaux JP. Revolutionizing Medical Data Sharing Using Advanced Privacy-Enhancing Technologies: Technical, Legal, and Ethical Synthesis. J Med Internet Res, 23, 2021.
[48] Peter W. Shor. Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer. SIAM Journal on Computing, 26(5):1484-1509, oct 1997.
[49] Eric R. Verheul and Henk C. A. van Tilborg. Cryptanalysis of 'Less Short' RSA Secret Exponents. Applicable Algebra in Engineering, Communication and Computing, 8:425-435, 1997.
[50] Z. Wang, M. Song, Z. Zhang, Y. Song, Q. Wang, and H. Qi. Beyond inferring class representatives: User-level privacy leakage from federated learning. In IEEE INFOCOM, 2019.
[51] Ligeng Zhu, Zhijian Liu, and Song Han. Deep leakage from gradients. In NIPS. 2019.