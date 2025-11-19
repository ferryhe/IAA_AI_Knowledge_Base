_Note: Source document was split into 2 OCR chunks (pages 1-13, pages 14-24) to stay within token limits._

# CS9 Convolutional neural network case studies

## Page 1
# Convolutional neural network case studies: 

(1) anomalies in mortality rates
(2) image recognition

Daniel Meier* Mario V. Wüthrich ${ }^{\dagger}$

Prepared for:
Fachgruppe "Data Science"
Swiss Association of Actuaries SAV
Version of July 19, 2020


#### Abstract

We provide a general introduction to convolutional neural networks (CNNs) in this tutorial. CNNs are particularly well suited to find common spatial structure in images or time series. As an insurance related example for life \& health insurance we illustrate how to use a CNN to detect anomalies in mortality rates taken from the Human Mortality Database (HMD); the anomalies are caused by migration between countries and other errors. As a second example, we study a CNN to classify images of handwritten digits taken from one of the most widely used benchmark datasets, the Modified National Institute of Standards and Technology (MNIST) dataset. Our aim is to explore and discuss the building blocks and the properties of these CNNs, and we showcase their use.


Keywords. Convolutional neural network, CNN, regression, classification, mortality rates, image recognition.

## 0 Introduction and overview

This data analytics tutorial has been written for the working group "Data Science" of the Swiss Association of Actuaries SAV, see
https://www.actuarialdatascience.org
The main purpose of this tutorial is to provide a general introduction to convolutional neural network (CNN) architectures. We describe the building blocks used in the architectures of CNNs, we list problems for which CNNs are particularly well suited, and we showcase this more explicitly on two examples in this tutorial. The complete underlying code and data is available on GitHub. ${ }^{1}$

[^0]
[^0]:    *Swiss Re Institute, Swiss Re Ltd, daniel_meier@swissre.com
    ${ }^{\dagger}$ RiskLab, Department of Mathematics, ETH Zurich, mario.wuethrich@math.ethz.ch
    ${ }^{\ddagger}$ See https://github.com/JSchelldorfer/ActuarialDataScience

## Page 2
Despite the origins of CNNs dating back to as early as 1980, see [7], CNNs are one of the most important contributors - maybe even the most important one - for the tremendous success of deep learning over the recent years. Problems that have been considered to be not feasible two decades ago have essentially been solved with very high accuracy (or some other relevant metrics), often exceeding performance of humans where this criterion is applicable, see, e.g. [9]. The main area of problems where CNNs usually outperform other algorithms by far - boosted by massively increased availability of labeled data and computing power, including GPUs, see, e.g. [3] - is image recognition and classification. In Section 3 we try to partly demystify why CNNs are so successful in this area. However, the main justification for using CNNs for this kind of problems will remain the striking empirical evidence of success because there are only very few mathematical results that give analytical proofs to these empirical findings. Other areas where CNNs have been applied very successfully are:

- natural language processing (NLP), see, e.g. [11],
- time series modeling, see, e.g. $[1,8,16]$,
- anomaly detection, e.g. fraud, see, e.g. $[6,24]$,
- health predictions based on electronic health records, see, e.g. [2, 22],
- games like Go, see, e.g. [18].

There is a big library of pre-trained CNNs available for image classification, for example, AlexNet, GoogLeNet, ResNet, Inception, MobileNet, VGG, DenseNet, NASNet. These pretrained models can either be directly used and applied to classify images into the categories provided, e.g. AlexNet offers $1^{\prime} 000$ categories like "goldfish", "kite", "goose", etc., or these pre-trained CNNs can be used for transfer learning, e.g. by replacing the last $4^{\prime} 096 \times 1^{\prime} 000$ fully-connected layer of AlexNet by a $4^{\prime} 096 \times 10$ fully-connected layer for 10 (other) categories and only training the weights (parameters) of this last layer. By keeping the first pre-trained layers one can benefit from the fact that these layers have already been calibrated to find structures in images, for instance, sharp edges, and by only training the last layer we give the right interpretation to these sharp edges in our modeling context.
In this tutorial we follow the notation in [5] for feed-forward networks, using mappings

$$
\boldsymbol{z}^{(k)}: \mathbb{R}^{n^{(k-1)}} \rightarrow \mathbb{R}^{n^{(k)}}, \quad \boldsymbol{x} \mapsto \boldsymbol{z}^{(k)}(\boldsymbol{x})=\left(\begin{array}{c}
z_{1}^{(k)}(\boldsymbol{x}) \\
z_{2}^{(k)}(\boldsymbol{x}) \\
\vdots \\
z_{n^{(k)}}^{(k)}(\boldsymbol{x})
\end{array}\right)
$$

to define the $k$-th (hidden) layer of a feed-forward network. The input into the first hidden layer is denoted by $\boldsymbol{X} \in \mathbb{R}^{n^{(0)}}$, and the output of the last hidden layer $k_{\max }$ is denoted by $Y \in \mathbb{R}^{n^{(k_{\max })}}$. Additional subscripts as needed illustrate individual cases, e.g. of training samples. Most of the time in this tutorial we will work in higher dimensions, e.g. using $\mathbb{R}^{n_{1}^{(k)} \times n_{2}^{(k)}}$ instead of $\mathbb{R}^{n^{(k)}}$, but this is mainly to simplify notation and to better highlight the structure of the convolutional layer(s) of CNNs, because our CNNs act on two-dimensional arrays of size $n_{1}^{(k)} \times n_{2}^{(k)}$ in contrast to one-dimensional vectors of size $n^{(k)}$ of fully-connected feed-forward networks.

## Page 3
A feed-forward network based on layers (0.1) is then obtained by composing these layers, i.e.

$$
\boldsymbol{X} \in \mathbb{R}^{n^{(0)}} \mapsto Y=\left(\boldsymbol{z}^{\left(k_{\max }\right)} \circ \cdots \circ \boldsymbol{z}^{(1)}\right)(\boldsymbol{X}) \in \mathbb{R}^{n^{\left(k_{\max }\right)}}
$$

for the moment this assumes that there is no noise term involved. We will give a detailed description of CNN layers in Section 2.1, below.

Organization. This tutorial is organized as follows. In the next section we describe the datasets used. In Section 2 we introduce CNN architectures and we describe their features. Moreover, we explore these CNN architectures on our two datasets. In Section 3 we discuss main properties of CNNs, these help to better understand the functioning of CNNs. Finally, in Section 4 we conclude.

# 1 Datasets 

We start by introducing the two datasets we will be working on, defining the inputs $\boldsymbol{X}$ to the CNNs and the outputs (also called labels) $Y$.

### 1.1 Human Mortality Database

The Human Mortality Database (HMD), see https://www.mortality.org, is maintained by the University of California, Berkeley, and the Max Planck Institute for Demographic Research, Rostock. It offers mortality rates $q_{x, t, c, g}$ for ages $x$ in calendar years $t$ (see Figure 1) as well as the corresponding population numbers (exposures) $E_{x, t, c, g}$ (see Figure 2) for more than 40 countries $c$ split into males and females (denoted by gender $g$ ). It regularly collects updates from the national statistical offices, applying a uniform set of transformation procedures to the data. Despite the efforts made to ensure consistency across different countries we see various patterns emerging when analyzing anomalies due to migration and other errors. Such anomalies of mortality rates can result in substantial under- or overestimation in life insurance products. Two further data preparation steps are necessary on our side.

- In years of territorial changes the data on population numbers is given both before and after the change. We use the average of both values in such cases.
- Some mortality rates are missing. In case neighboring (in terms of ages $x$ and calendar years $t$ ) values are available we interpolate linearly, otherwise use the value of the nearest neighbor (both methods in the sense of the Python scipy package).

Inputs. For the inputs $\boldsymbol{X}$ into the CNN we will follow a Computer Vision approach, i.e. we take moving windows $W$ of mortality rates $q_{x, t, c, g}$ as input, and we aim at detecting whether (or how strong) anomalies due to migration and other errors are present in each window. In more detail, for a given country $c$ and $i=0,1,2, \ldots$ we define window $W_{i, c} \in \mathbb{R}^{10 \times 10 \times 3}$ by

$$
\begin{aligned}
& W_{i, c, \cdot, 1}:=\left(\text { logit }\left(q_{x, t, c, \text { males }}\right)\right)_{x_{i}<x \leq x_{i}+10, t_{i}<t \leq t_{i}+10} \\
& W_{i, c, \cdot, 2}:=\left(\text { logit }\left(q_{x, t, c, \text { females }}\right)\right)_{x_{i}<x \leq x_{i}+10, t_{i}<t \leq t_{i}+10} \\
& W_{i, c, \cdot, 3}:=W_{i, c, \cdot, 1}-W_{i, c, \cdot, 2}
\end{aligned}
$$

## Page 4
Figure 1: Subset of mortality rates $q_{x, t, \mathrm{GBR}, \text { males }}$ by age $x$ and calendar year $t$ from the HMD.

Figure 2: Subset of population numbers (exposures) $E_{x, t, \mathrm{GBR}, \text { males }}$ by age $x$ and calendar year $t$ from the HMD.
![Page 4 Image 1](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p04_img1.jpg)
![Page 4 Image 2](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p04_img2.jpg)

## Page 5
where $x_{i}:=20+5(i \bmod 11)$ and $t_{i}:=1950+5\lfloor i / 11\rfloor$. Thus, starting with ages $x=21,22, \ldots, 30$ and years $t=1951,1952, \ldots, 1960$ we move in 5 -year age and time steps over the available mortality rates until age $x=80$ and year $t=2015$. See Figure 5 for a schematic overview. For some countries $c$ less years of observations are available and we generally exclude years before 1950 since for some countries population numbers (exposures) are given only for civilian population during war times, while mortality rates are always given for the whole population. Also note that the step width of 5 years is selected due to clear 5 -year patterns in the underlying data, e.g. from censuses in 5 -year intervals or groupings into 5 -year age buckets. The last dimension in windows $W_{i, c}$ is used for taking into account males, females, and their difference. The latter set of values $W_{i, c, \cdots, 3}$ is actually redundant and we mainly use it for the analogy to color images, i.e. each $W_{i, c}$ can be considered as a $10 \times 10$ color image with 3 channels. We apply two additional data preparation steps to conclude the definition of inputs.

- In some cases $q_{x, t, c, g}=0$ and, thus, $\operatorname{logit}\left(q_{x, t, c, g}\right)$ is not defined. In these cases we apply linear interpolation or using the nearest neighbor (in terms of ages $x$ and calendar years $t$ ) as already done above for missing $q_{x, t, c, g}$.
- Along each channel we normalize values into $[0,1]$ by subtracting minima and dividing by maxima less minima, i.e. we apply a MinMaxScaler.

After application of these two steps on each window $W_{i, c}$, we call the result $\boldsymbol{X}_{i, c} \in[0,1]^{10 \times 10 \times 3}$, which are the final inputs of the CNN; across all countries, these are about 4'000 input samples.

Outputs. For the outputs (labels) of the CNN - in contrast to the second dataset below, where labels are part of the dataset - we first need to go through a few preparation steps. The goal is to define an output value $Y_{i, c} \in[0,1]$ for each input $\boldsymbol{X}_{i, c}$ that measures the anomaly severity due to migration and other errors in the chosen window. We start with the following identity in case there is not any migration nor other error present

$$
E_{x, t, c, g}=E_{x-1, t-1, c, g}\left(1-q_{x-1, t-1, c, g}\right)
$$

i.e. the population number for age $x$ at time $t$ is equal to the population number for age $x-1$ at time $t-1$ times the observed survival rate $\left(1-q_{x-1, t-1, c, g}\right)$. We can measure how strong this identity is violated in case of errors by defining normalized residuals $r_{x, t, c, g}$ (see Figure 3) as

$$
r_{x, t, c, g}:=\frac{E_{x, t, c, g}-E_{x-1, t-1, c, g}\left(1-q_{x-1, t-1, c, g}\right)}{E_{x, t, c, g}}
$$

Values $r_{x, t, c, g}<0$ indicate emigration (or errors), and values $r_{x, t, c, g}>0$ indicate immigration (or errors). In order to define the outputs $Y_{i, c}$ we first apply the two preparation steps from above - linear interpolation/using neighboring values, and MinMax normalization into $[0,1]$ on $r_{x, t, c, g}$, call the result $\bar{r}_{x, t, c, g}$. Then, we define the outputs $Y_{i, c}$, the severity of anomalies, as

$$
Y_{i, c}:=\max _{\substack{x_{i}<x \leq x_{i}+10, \\ t_{i}<t \leq t_{i}+10}}\left|\frac{\bar{r}_{x, t, c, \text { males }}+\bar{r}_{x, t, c, \text { females }}}{2}\right| \in[0,1]
$$

The goal of our analysis is to see whether we can detect (predict) anomalies $Y_{i, c}$ based on observed mortality rates $\boldsymbol{X}_{i, c}$. Note that the latter inputs are only based on mortality rates $q_{x, t, c, g}$ that do not consider any exposures $E_{x, t, c, g}$, and we would like to understand whether we can find irregularities solely based on $\boldsymbol{X}_{i, c}$ using CNNs.

## Page 6
Figure 3: Normalized residuals $r_{x, t, c, g}$ for Norwegian, Russian and US males. Note the different structures along years (horizontal lines), cohorts (diagonal lines) and ages (vertical lines). Blue defines negative values (emigration/errors), red positive values (immigration/errors). The most intense colors are around $\pm 15 \%$.

# 1.2 MNIST dataset 

The Modified National Institute of Standards and Technology (MNIST) dataset contains 70'000 images of handwritten digits $0,1, \ldots, 9$ in the format of 28 times 28 grayscale pixels and is widely used as benchmark for various classification algorithms. Inputs and outputs are readily available.

Inputs. Grayscale images $\boldsymbol{X}_{i} \in[0,1]^{28 \times 28}$ after normalization via division by 255 , for $i=$ $1, \ldots, 70^{\prime} 000$.

Outputs. The actual digits $Y_{i} \in\{0,1\}^{10}$ represented by each image as one-hot encoding, i.e. component $j+1$ of $Y_{i}$ is equal to 1 if the $i$-th digit represents $j$, and 0 otherwise; for one-hot versus dummy coding we refer to $[5]$.

Figure 4: Some examples of the MNIST dataset containing 28 times 28 grayscale pixels images of handwritten digits.

## 2 Convolutional neural networks

In this section we introduce CNN architectures and we discuss their building blocks and features. Moreover, we apply these CNN architectures to the two datasets introduced above.
![Page 6 Image 1](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p06_img1.jpg)
![Page 6 Image 2](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p06_img2.jpg)

## Page 7
# 2.1 Typical layers in convolutional neural networks 

### 2.1.1 Convolutional layer

The main building block of a CNN is a convolutional layer. Strictly speaking the layer rather applies a moving dot-product instead of a convolution. But by applying zero-padding (or cropping) and reversing indices of filters, the moving dot-product is equivalent to a convolution and, thus, the name convolutional layer is justified.
In order to explain how a convolutional layer works, i.e. how inputs and outputs of the convolutional layer are connected, 2-dimensional inputs are typically used because they can nicely be illustrated. This is also the set-up we are going to present in the following. However, 1dimensional inputs (e.g. time-series, see for an example [8]) and higher dimensional inputs are also frequently considered in CNNs, and the definitions that we introduce below can easily be carried over. In fact, when working with several channels or filters, see below, we are already applying 3-dimensional inputs.
A convolution layer is a mapping

$$
\boldsymbol{z}^{(k)}: \mathbb{R}^{n_{1}^{(k-1)} \times n_{2}^{(k-1)}} \rightarrow \mathbb{R}^{n_{1}^{(k)} \times n_{2}^{(k)}}, \quad \boldsymbol{x} \mapsto\left(\begin{array}{ccc}
z_{1,1}^{(k)}(\boldsymbol{x}) & \cdots & z_{1, n_{2}^{(k)}}^{(k)}(\boldsymbol{x}) \\
\vdots & & \vdots \\
z_{n_{1}^{(k)}, 1}^{(k)}(\boldsymbol{x}) & \cdots & z_{n_{1}^{(k)}, n_{2}^{(k)}}^{(k)}(\boldsymbol{x})
\end{array}\right)
$$

with $n_{1}^{(k)} n_{2}^{(k)}$ hidden neurons in the $k$-th hidden layer. The special characteristics of a convolutional layer are given by the fact that each $\boldsymbol{x} \mapsto z_{i_{1}, i_{2}}^{(k)}(\boldsymbol{x})$ typically only considers a small subset of components of $\boldsymbol{x}$ and weights (learnable parameters) $\left(w_{j_{1}, j_{2}}^{(k)}\right)_{j_{1}, j_{2}}$ are shared by defining

$$
\boldsymbol{x} \mapsto z_{i_{1}, i_{2}}^{(k)}(\boldsymbol{x}):=w_{0,0}^{(k)}+\sum_{j_{1}=1}^{f_{1}^{(k)}} \sum_{j_{2}=1}^{f_{2}^{(k)}} w_{j_{1}, j_{2}}^{(k)} x_{i_{1}+j_{1}-1, i_{2}+j_{2}-1}
$$

where $f_{1}^{(k)}$ and $f_{2}^{(k)}$ define the filter size in the two directions considered in this two-dimensional case - a filter being defined as the matrix of weights (excluding the weight $w_{0,0}^{(k)}$ for bias/offset)

$$
\left(\begin{array}{ccc}
w_{1,1}^{(k)} & \cdots & w_{1, f_{2}^{(k)}}^{(k)} \\
\vdots & & \vdots \\
w_{f_{1}^{(k)}, 1}^{(k)} & \cdots & w_{f_{1}^{(k)}, f_{2}^{(k)}}^{(k)}
\end{array}\right) \in \mathbb{R}^{f_{1}^{(k)} \times f_{2}^{(k)}}
$$

Thus, a convolutional layer has $f_{1}^{(k)} f_{2}^{(k)}+1$ learnable parameters (weights) including the bias. Usually, this is substantially less compared to the $\left(n_{1}^{(k-1)} n_{2}^{(k-1)}+1\right) n_{1}^{(k)} n_{2}^{(k)}$ weights a fullyconnected layer would have, see [5]. This reduction is received because (1) common weights are shared across different places in the input array $\boldsymbol{x}$, and (2) the filter sizes $f_{1}^{(k)}$ and $f_{2}^{(k)}$ are usually taken not too big to identify common local structure at different locations in the inputs $\boldsymbol{x}$. Moreover, note that these choices imply that $n_{1}^{(k)}=n_{1}^{(k-1)}-f_{1}^{(k)}+1$ and $n_{2}^{(k)}=n_{2}^{(k-1)}-f_{2}^{(k)}+1$. The double sum in equation (2.2) can be considered as a moving dot-product of weights and inputs.
In a more general setup of convolutional layers three extensions of the above are often used.

## Page 8
1. Padding: Considering the input of the $k$-th layer $\boldsymbol{x} \in \mathbb{R}^{n_{1}^{(k-1)} \times n_{2}^{(k-1)}}$ as an image, padding with parameters $p_{1}^{(k)}, p_{2}^{(k)}$ means to horizontally and vertically add $p_{1}$ and $p_{2}$ pixels with value 0 (typically) on each side, increasing the input size to $\left(n_{1}^{(k-1)}+2 p_{1}^{(k)}\right) \times\left(n_{2}^{(k-1)}+2 p_{2}^{(k)}\right)$. We will use this later to show the connection to convolutions, while in practice padding can for example be useful to preserve image sizes, i.e. for uneven $f_{1}^{(k)}, f_{2}^{(k)}$ the use of $p_{1}^{(k)}=\left(f_{1}^{(k)}-1\right) / 2, p_{2}^{(k)}=\left(f_{2}^{(k)}-1\right) / 2$ leads to $n_{1}^{(k)}=n_{1}^{(k-1)}$ and $n_{2}^{(k)}=n_{2}^{(k-1)}$.
2. Strides: Parameters $s_{1}^{(k)}, s_{2}^{(k)}$ can be used to shift parts of the dot-product in equation (2.2) by using instead

$$
\sum_{j_{1}=1}^{f_{1}^{(k)}} \sum_{j_{2}=1}^{f_{2}^{(k)}} w_{j_{1}, j_{2}}^{(k)} F_{s_{1}^{(k)}\left(i_{1}-1\right)+j_{1}, s_{2}^{(k)}\left(i_{2}-1\right)+j_{2}}
$$

This reduces the output size from $\left(n_{1}^{(k-1)}-f_{1}^{(k)}+1\right) \times\left(n_{2}^{(k-1)}-f_{2}^{(k)}+1\right)$ to $\left(\left\lfloor\left(n_{1}^{(k-1)}-\right.\right.\right.$ $\left.\left.f_{1}^{(k)}\right) / s_{1}^{(k)}\right\rfloor+1) \times\left(\left\lfloor\left(n_{2}^{(k-1)}-f_{2}^{(k)}\right) / s_{2}^{(k)}\right\rfloor+1\right)$. The stride should be thought of as the step size with which the filter is moved across the input.
3. Dilation: Parameters $d_{1}^{(k)}, d_{2}^{(k)}$ can be used to shift parts of the dot-product in equation (2.2) by using instead

$$
\sum_{j_{1}=1}^{f_{1}^{(k)}} \sum_{j_{2}=1}^{f_{2}^{(k)}} w_{j_{1}, j_{2}}^{(k)} F_{i_{1}+d_{1}^{(k)}\left(j_{1}-1\right), i_{2}+d_{2}^{(k)}\left(j_{2}-1\right)}
$$

This reduces the output size from $\left(n_{1}^{(k-1)}-f_{1}^{(k)}+1\right) \times\left(n_{2}^{(k-1)}-f_{2}^{(k)}+1\right)$ to $\left(n_{1}^{(k-1)}-\right.$ $\left.d_{1}^{(k)}\left(f_{1}^{(k)}-1\right)\right) \times\left(n_{2}^{(k-1)}-d_{2}^{(k)}\left(f_{2}^{(k)}-1\right)\right)$ and can be useful for large inputs (e.g. high resolution images where neighboring pixels can be expected to have very similar values) as another way to reduce the number of parameters and, thus, increasing model calibration. Note that the filter size is enlarged by dilation by emptying some positions within the filter window to zero, e.g. for $d_{1}^{(k)}=2$ we only consider every second input component.

All three extensions can also be combined and applied together. The general output size is

$$
\left\lfloor\frac{n_{1}^{(k-1)}+2 p_{1}^{(k)}-d_{1}^{(k)}\left(f_{1}^{(k)}-1\right)+s_{1}^{(k)}-1}{s_{1}^{(k)}}\right\rfloor \times\left\lfloor\frac{n_{2}^{(k-1)}+2 p_{2}^{(k)}-d_{2}^{(k)}\left(f_{2}^{(k)}-1\right)+s_{2}^{(k)}-1}{s_{2}^{(k)}}\right\rfloor
$$

Applying (pre-defined) filters is also widely used in image processing for tasks like edge detection, blurring, sharpening, etc., we refer to transfer learning mentioned in Section 0, above. A major advantage of CNNs is that these filters get automatically estimated/optimized, which sometimes results in filters with an intuitive meaning like edge detection, but most often lack an easy explanation why these particular filters do a good job. Figure 15 illustrates results of applying the estimated filters of the digit recognition CNN.

Channels. The generic definition of a convolutional layer in (2.1) has considered 2-dimensional inputs $\boldsymbol{x} \in \mathbb{R}^{n_{1}^{(k-1)} \times n_{2}^{(k-1)}}$, i.e. in terms of images we are considering monochromatic images. Color images, however, have 3 channels for, e.g. red, green, blue (RGB) components of the

## Page 9
image ${ }^{2}$, i.e. $\boldsymbol{x} \in \mathbb{R}^{n_{1}^{(k-1)} \times n_{2}^{(k-1)} \times 3}$. For color images, or $c$ channels in general, the layer mapping becomes $\boldsymbol{z}^{(k)}: \mathbb{R}^{n_{1}^{(k-1)} \times n_{2}^{(k-1)} \times c} \rightarrow \mathbb{R}^{n_{1}^{(k)} \times n_{2}^{(k)}}$ with weights $\left(w_{j_{1}, j_{2}, c_{1}}^{(k)}\right)_{j_{1}, j_{2}, c_{1}}$ and a single bias/offset weight $w_{0,0}^{(k)}$ that is shared. Note that channels typically only refer to the inputs of a layer.

Number of filters. One hyperparameter we still need to introduce is the number of filters $m^{(k)}$. So far we have only been considering a single filter, i.e. a single set of weights $\left(w_{j_{1}, j_{2}}^{(k)}\right)_{j_{1}, j_{2}}$, see (2.3), while typically $m^{(k)}>1$ many filters are used in parallel, such that the general layer mapping becomes

$$
\boldsymbol{z}^{(k)}: \mathbb{R}^{n_{1}^{(k-1)} \times n_{2}^{(k-1)} \times m^{(k-1)}} \rightarrow \mathbb{R}^{n_{1}^{(k)} \times n_{2}^{(k)} \times m^{(k)}}
$$

with $m^{(k)}\left(f_{1}^{(k)} f_{2}^{(k)}+1\right)$ weights/parameters being used. Note that from a structural point of view filters in the input layer $m^{(0)}$ are equivalent to channels, i.e. in the input layer we call multiple dimensions $m^{(k-1)}$ (input) channels, whereas in the output we call multiple dimensions $m^{(k)}$ (output) filters. Table 1 provides an overview of all hyperparameters involved.

Table 1: Overview of typical hyperparameters of a convolutional layer.

| Input size | $n_{1}^{(k-1)} \times n_{2}^{(k-1)}$ |
| :-- | :--: |
| Number of channels | $m^{(k-1)}$ |
| Padding | $p_{1}^{(k)}, p_{2}^{(k)}$ |
| Strides | $s_{1}^{(k)}, s_{2}^{(k)}$ |
| Dilation | $d_{1}^{(k)}, d_{2}^{(k)}$ |
| Output size | $n_{1}^{(k)} \times n_{2}^{(k)}$ |
| Number of filters | $m^{(k)}$ |

Connection to convolutions. Ignoring bias/offset weight $w_{0,0}^{(k)}$ or setting $w_{0,0}^{(k)}:=0$, the remaining moving dot-product in equation (2.2) is given by

$$
\sum_{j_{1}=1}^{f_{1}^{(k)}} \sum_{j_{2}=1}^{f_{2}^{(k)}} w_{j_{1}, j_{2}}^{(k)} x_{i_{1}+j_{1}-1, i_{2}+j_{2}-1}
$$

which very much resembles a (discrete) convolution

$$
(\boldsymbol{w} * \boldsymbol{x})_{i_{1}, i_{2}}:=\sum_{j_{1}} \sum_{j_{2}} w_{j_{1}, j_{2}}^{(k)} x_{i_{1}-j_{1}, i_{2}-j_{2}}
$$

where $j_{1}, j_{2}$ run over those indices such that weights $\boldsymbol{w}$ and inputs $\boldsymbol{x}$ are defined. Using weights with reversed indices, i.e.

$$
w_{j_{1}, j_{2}}^{*}(k):=w_{f_{1}^{(k)}-j_{1}+1, f_{2}^{(k)}-j_{2}+1}^{(k)}
$$

[^0]
[^0]:    ${ }^{2}$ For humans, the linear combination of 3 channels is sufficient to cover the full range of perceivable colors from 3 different types of receptor cells in the human eye. For some animals, e.g. pigeons and some butterflies, actually up to 5 channels are needed.

## Page 10
for the moving dot-product of equation (2.5), and either using zero-padding parameters $p_{1}(k)=$ $f_{1}(k)-1, p_{2}(k)=f_{2}(k)-1$ on $\boldsymbol{x}$ in equation (2.5) or cropping, i.e. padding with negative parameters $p_{1}(k)=1-f_{1}(k), p_{2}(k)=1-f_{2}(k)$ on $\boldsymbol{w} * \boldsymbol{x}$ in equation (2.6), shows the equivalence of both approaches and, thus, justifies the name convolutional layer.

Fast Fourier transform (FFT). Having established the connection to convolutions in the previous paragraph, an immediate thought is whether the FFT could be used for the evaluation of the moving dot-product, which requires in total $f_{1}^{(k)} f_{2}^{(k)} n_{1}^{(k)} n_{2}^{(k)}$ multiplications. The general answer is yes. The necessary steps are:

- zero-padding weights $\boldsymbol{w}$ such that inputs $\boldsymbol{x}$ and weights $\boldsymbol{w}$ have the same size,
- reversing indices of weights, see (2.7),
- FFT of $\boldsymbol{w}^{*}$ and $\boldsymbol{x}$,
- element-wise product (Hadamard product) of $\operatorname{FFT}\left(\boldsymbol{w}^{*}\right)$ and $\operatorname{FFT}(\boldsymbol{x})$,
- inverse FFT and cropping results.

The number of multiplications required in this set of operations is in $\mathcal{O}\left(n_{1}^{(k)} n_{2}^{(k)} \log \left(n_{1}^{(k)} n_{2}^{(k)}\right)\right)$, which corresponds to a speed-up for large filter sizes $f_{1}^{(k)} f_{2}^{(k)}>\log \left(n_{1}^{(k)} n_{2}^{(k)}\right)$. But since filter sizes, in practice, typically are small, the use of the FFT does not improve computation times.

# 2.1.2 Pooling layer 

A max-pooling layer is defined by

$$
\boldsymbol{z}^{(k)}: \mathbb{R}^{n_{1}^{(k-1)} \times n_{2}^{(k-1)}} \rightarrow \mathbb{R}^{n_{1}^{(k)} \times n_{2}^{(k)}}, \quad \boldsymbol{x} \mapsto z_{i_{1}, i_{2}}^{(k)}(\boldsymbol{x})=\max _{\substack{1 \leq j_{1} \leq f_{1}^{(k)} \\ 1 \leq j_{2} \leq f_{2}^{(k)}} x_{i_{1}+j_{1}-1, i_{2}+j_{2}-1}
$$

i.e. it takes maxima over areas (windows) of size $f_{1}^{(k)} \times f_{2}^{(k)}$. A max-pooling layer is mainly used for reducing size of data. Replacing maxima by averages is commonly used as well and known as average-pooling. The same extensions (padding, strides, dilation) as above are also applied in pooling layers, and the strides are typically set to $s_{1}^{(k)}=f_{1}^{(k)}, s_{2}^{(k)}=f_{2}^{(k)}$ to prevent from overlapping windows. No weights/parameters are estimated in a pooling layer, it is purely a fixed mapping. Note that pooling layers can also be interpreted as convolutional layers, where the convolution operation is replaced by extracting the maximum (max-pooling) or the average (average-pooling) out of a window of the same size as the filter.

### 2.1.3 Fully-connected layer

Fully-connected layers are discussed in detail in [5]. Just like for neural networks in general, one or more fully-connected layers are frequently used in CNNs, typically as last layers to reduce the output sizes to e.g. the number of categories for classification problems. For layers closer to the inputs of the CNN a fully-connected layer would require too many weights/parameters because it connects every neuron of the input $\boldsymbol{x} \in \mathbb{R}^{n_{1}^{(k-1)} \times n_{2}^{(k-1)}}$ to every neuron of the output $\mathbb{R}^{n_{1}^{(k)} \times n_{2}^{(k)}}$. For example, using a fully-connected layer for the first layer of the digit recognition

## Page 11
CNN would require $28^{2} \cdot 26^{2}+26^{2}=530^{\prime} 660$ weights/parameters, while a convolutional layer with 10 filters of size $3 \times 3$ only uses $9 \cdot 10+10=100$ weights/parameters due to its sparse connections and weights sharing. We are going to use fully-connected layers as last layer to bring the CNN processed input $\boldsymbol{X}$ into the right structural form to predict the output $Y$, see e.g. line 12 in Table 2 .

# 2.1.4 Batch normalization layer 

A batch normalization layer acts quite differently than other layers. First, during training, it normalizes (subtracting empirical mean and dividing by empirical standard deviation) the inputs of each filter of a mini-batch. Thus, this introduces dependencies between the input samples of a mini-batch and it is therefore important that mini-batches use randomized samples, e.g. by randomizing the order of inputs $\boldsymbol{X}$. Then, for each filter the outputs are shifted and scaled by two learnable parameters (the same across all mini-batches). For predictions, the input is first shifted and scaled via the average of parameters during training across mini-batches (these are considered as non-learnable parameters), and then shifted and scaled by the latter two (learnable) parameters, learned during training. This results in $4 m^{(k)}$ parameters of which half of them are learnable in the sense that they are optimized in the overall loss minimization, while the other half are simple averages calculated during training.
We use batch normalization layers for the purpose of addressing the problem of vanishing or exploding gradients and because of their empirical evidence to improve our results. Getting insights into other consequences of using batch normalization layers and expressing this in simple rules of thumb is surprisingly challenging, see, e.g. [20].

### 2.1.5 Flatten layer

The flatten layer performs a simple transformation by rearranging dimensions and preserving all values, e.g. it flattens an array $\mathbb{R}^{n_{1}^{(k-1)} \times n_{2}^{(k-1)}}$ to a vector $\mathbb{R}^{n^{(k)}}$ with $n^{(k)}=n_{1}^{(k-1)} n_{2}^{(k-1)}$. This is mainly used if we compose a CNN layer with a fully-connected layer, the former having, e.g. 2-dimensional outputs and the latter using 1-dimensional vectors as inputs.

### 2.1.6 Softmax and sigmoid output layers

Just like for neural networks for classification in general, we are using a softmax layer to turn the final output vector $Y$ into a categorical probability distribution, this is equivalent to multinomial logistic regression. The softmax layer is defined by

$$
\boldsymbol{z}^{(k)}: \mathbb{R}^{n^{(k-1)}} \rightarrow[0,1]^{n^{(k)}}, \quad \boldsymbol{x} \mapsto \boldsymbol{z}^{(k)}(\boldsymbol{x})=\frac{1}{\sum_{i=1}^{n^{(k-1)}} \exp \left(x_{i}\right)}\left(\begin{array}{c}
\exp \left(x_{1}\right) \\
\exp \left(x_{2}\right) \\
\vdots \\
\exp \left(x_{n^{(k-1)}}\right)
\end{array}\right)
$$

and, thus, $n^{(k)}=n^{(k-1)}$. If we have only two classes, i.e. if we have a Bernoulli prediction problem, then we only need to model one output $\boldsymbol{x} \mapsto p^{(k)}(\boldsymbol{x})=\boldsymbol{z}^{(k)}(\boldsymbol{x}) \in[0,1]$ because the probability of the other class can simply be obtained by $1-p^{(k)}(\boldsymbol{x}) \in[0,1]$. In this Bernoulli

## Page 12
case one usually uses the sigmoid/logistic function, that is, assume $n^{(k)}=n^{(k-1)}=1$ and set

$$
\boldsymbol{x} \in \mathbb{R} \mapsto p^{(k)}(\boldsymbol{x})=\frac{1}{1+e^{-\boldsymbol{x}}}
$$

The softmax and sigmoid output layers address classification problems. In case we consider regression problems we may select any reasonable link function to connect the output with the last hidden layer. For instance, if we predict claim counts, we typically choose the log-link which results in the exponential output function

$$
\boldsymbol{x} \in \mathbb{R} \mapsto \boldsymbol{z}^{(k)}(\boldsymbol{x})=\exp (\boldsymbol{x})>0
$$

# 2.1.7 Activation layer 

We emphasize that in the network layers discussed above (convolutional layer and fully-connected layer) all operations have been linear, but the full power of network modeling only comes into play by using non-linear activations of these linear operations. Instead of including the nonlinear activations into the convolutional and the fully-connected layer, respectively, we treat the activation as a separate layer

$$
\boldsymbol{z}^{(k)}: \mathbb{R}^{n^{(k-1)}} \rightarrow \mathbb{R}^{n^{(k)}}, \quad \boldsymbol{x} \mapsto \phi(\boldsymbol{x})
$$

where typically the activation function $\phi$ is non-linear (e.g. ReLU, sigmoid, tanh, etc.) and it is applied element-wise, thus $n^{(k)}=n^{(k-1)}$. This separation of the activation is required because of using batch normalization between convolution and activation layers, see Table 2.
We remark that these non-linear activations are crucial for receiving the so-called universality theorems, e.g. in [15] it is proved that multi-layer fully-connected feed-forward networks with non-polynomial activation can approximate big classes of functions arbitrarily well (in some norm) supposed that these networks have sufficiently many neurons.

### 2.2 Two example CNN architectures

After introducing the typical layers of CNNs in the previous section we provide a full overview of all layers of the two examples considered in this tutorial in Tables 2 and 3. The first one is a regression problem with a single output, and the second one is a classification problem with 10 labels.
We describe in detail the first network architecture given in Table 2. We start by applying a batch normalization step on line 1 to ensure that all input components live on a comparable scale. Then, we stack three convolutional layers (lines 2, 5, 8), also see Figure 5, each of these convolutional layers is followed by a batch normalization layer (lines $3,6,9$ ), and then it is non-linearly activated using the ReLU activation (lines $4,7,10$ ). This processes the $m^{(0)}=3$ channels of the $10 \times 10$ input to $m^{(8)}=64$ filters of $4 \times 4$ outputs. These outputs are flattened to a $4 \times 4 \times 64=1^{\prime} 024$ dimensional vector which serves as input to a (last) fully-connected layer on line 12 having a 1-dimensional output. Finally, we apply the sigmoid function to this output to ensure that the final network output is in $[0,1]$, which is exactly the domain of our (continuous) responses $Y$. Remark that the original input is already quite low-dimensional, for this reason we do not use max-pooling layers in this example.

## Page 13
Table 2: Structure of a CNN to detect anomalies in mortality rates, with $24^{\prime} 839$ learnable weights/parameters and 230 non-learnable parameters (given in brackets).

|  Layer | input size | output size | $f_{1}^{(k)}, f_{2}^{(k)}$ | $s_{1}^{(k)}, s_{2}^{(k)}$ | $m^{(k)}$ | #parameters  |
| --- | --- | --- | --- | --- | --- | --- |
|  1. Batch norm. | $10 \times 10 \times 3$ | $10 \times 10 \times 3$ | - | - | - | $6(+6)$  |
|  2. Conv. | $10 \times 10 \times 3$ | $8 \times 8 \times 16$ | 3,3 | 1,1 | 16 | $16 \cdot 3 \cdot 3^{2}+16$  |
|  3. Batch norm. | $8 \times 8 \times 16$ | $8 \times 8 \times 16$ | - | - | - | $32(+32)$  |
|  4. ReLU $\phi$ | $8 \times 8 \times 16$ | $8 \times 8 \times 16$ | - | - | - | 0  |
|  5. Conv. | $8 \times 8 \times 16$ | $6 \times 6 \times 32$ | 3,3 | 1,1 | 32 | $32 \cdot 16 \cdot 3^{2}+32$  |
|  6. Batch norm. | $6 \times 6 \times 32$ | $6 \times 6 \times 32$ | - | - | - | $64(+64)$  |
|  7. ReLU $\phi$ | $6 \times 6 \times 32$ | $6 \times 6 \times 32$ | - | - | - | 0  |
|  8. Conv. | $6 \times 6 \times 32$ | $4 \times 4 \times 64$ | 3,3 | 1,1 | 64 | $64 \cdot 32 \cdot 3^{2}+64$  |
|  9. Batch norm. | $4 \times 4 \times 64$ | $4 \times 4 \times 64$ | - | - | - | $128(+128)$  |
|  10. ReLU $\phi$ | $4 \times 4 \times 64$ | $4 \times 4 \times 64$ | - | - | - | 0  |
|  11. Flatten | $4 \times 4 \times 64$ | $1^{\prime} 024 \times 1$ | - | - | - | 0  |
|  12. Fully-conn. | $1^{\prime} 024 \times 1$ | $1 \times 1$ | - | - | - | $1^{\prime} 024+1$  |
|  13. Sigmoid output | $1 \times 1$ | $1 \times 1$ | - | - | - | 0  |

Table 3: Structure of a CNN for digit recognition of the MNIST dataset, with $15^{\prime} 710$ learnable weights/parameters and 140 non-learnable parameters (given in brackets).

|  Layer | input size | output size | $f_{1}^{(k)}, f_{2}^{(k)}$ | $s_{1}^{(k)}, s_{2}^{(k)}$ | $m^{(k)}$ | #parameters  |
| --- | --- | --- | --- | --- | --- | --- |
|  1. Conv. | $28 \times 28$ | $26 \times 26 \times 10$ | 3,3 | 1,1 | 10 | $10 \cdot 3^{2}+10$  |
|  2. Batch norm. | $26 \times 26 \times 10$ | $26 \times 26 \times 10$ | - | - | - | $20(+20)$  |
|  3. ReLU $\phi$ | $26 \times 26 \times 10$ | $26 \times 26 \times 10$ | - | - | - | 0  |
|  4. Max-pooling | $26 \times 26 \times 10$ | $13 \times 13 \times 10$ | 2,2 | 2,2 | - | 0  |
|  5. Conv. | $13 \times 13 \times 10$ | $11 \times 11 \times 20$ | 3,3 | 1,1 | 20 | $20 \cdot 10 \cdot 3^{2}+20$  |
|  6. Batch norm. | $11 \times 11 \times 20$ | $11 \times 11 \times 20$ | - | - | - | $40(+40)$  |
|  7. ReLU $\phi$ | $11 \times 11 \times 20$ | $11 \times 11 \times 20$ | - | - | - | 0  |
|  8. Max-pooling | $11 \times 11 \times 20$ | $10 \times 10 \times 20$ | 2,2 | 1,1 | - | 0  |
|  9. Conv. | $10 \times 10 \times 20$ | $8 \times 8 \times 40$ | 3,3 | 1,1 | 40 | $40 \cdot 20 \cdot 3^{2}+40$  |
|  10. Batch norm. | $8 \times 8 \times 40$ | $8 \times 8 \times 40$ | - | - | - | $80(+80)$  |
|  11. ReLU $\phi$ | $8 \times 8 \times 40$ | $8 \times 8 \times 40$ | - | - | - | 0  |
|  12. Max-pooling | $8 \times 8 \times 40$ | $4 \times 4 \times 40$ | 2,2 | 2,2 | - | 0  |
|  13. Flatten | $4 \times 4 \times 40$ | $640 \times 1$ | - | - | - | 0  |
|  14. Fully-conn. | $640 \times 1$ | $10 \times 1$ | - | - | - | $640 \cdot 10+10$  |
|  15. Softmax output | $10 \times 1$ | $10 \times 1$ | - | - | - | 0  |

# 2.3 Loss functions

### 2.3.1 Loss function for CNN on mortality rates

By $\mathcal{I}^{*}$ we denote all indexes $(i, c)$ in the training/test/validation data. As loss function for the CNN on mortality rates - without any further considerations or assumptions on (normal)

## Page 14
Figure 5: CNN on mortality rates: Schematic overview of moving windows $W_{i, c}$ over mortality rates $q_{x, t, c, g}$ (red, only one channel), where each square $\square$ represents a $5 \times 5$ block of mortality rates. The following moving dot product/convolution (blue, only one channel) similarly moves over values of $\boldsymbol{x}$.
distributions of the errors - we use mean squared errors, i.e.

$$
\mathcal{L}\left(Y, \widehat{\mu}(\boldsymbol{X}) ; \mathcal{I}^{*}\right):=\frac{1}{\left|\mathcal{I}^{*}\right|} \sum_{(i, c) \in \mathcal{I}^{*}}\left(Y_{i, c}-\widehat{\mu}\left(\boldsymbol{X}_{i, c}\right)\right)^{2}
$$

where $\widehat{\mu}\left(\boldsymbol{X}_{i, c}\right)$ denotes the prediction of the $i$-th window in country $c$, and where $Y_{i, c} \in[0,1]$ is the corresponding (continuous) response, see (1.1). The minimization is performed by Keras'/ TensorFlow's stochastic gradient descent (SGD) method, see Figure 6 for losses on training and validation set during model training.

Figure 6: Mean squared error during training phase of the CNN on mortality rates: the plot shows training and validation losses, the latter being used to track over-fitting.
![Page 14 Image 1](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p14_img1.jpg)
![Page 14 Image 2](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p14_img2.jpg)

## Page 15
# 2.3.2 Loss function for CNN of digit recognition 

For the digit recognition CNN we choose the categorical cross-entropy/multinomial logistic (deviance) loss as loss function, i.e.

$$
\mathcal{L}\left(Y, \widehat{\mu}(\boldsymbol{X}) ; \mathcal{I}^{*}\right):=-\sum_{i \in \mathcal{I}^{*}} \sum_{j=1}^{10}\left(Y_{i}\right)_{j} \log \left(\widehat{\mu}\left(\boldsymbol{X}_{i}\right)_{j}\right)
$$

Recall that $Y_{i} \in\{0,1\}^{10}$ is a one-hot encoded vector that represents the actual digit of the image. As minimization algorithm we select the AdaDelta algorithm, a variant of SGD with specific adaptive learning rates, see Figure 7. For a detailed description of different SGD algorithms we refer to $[10]$.

Figure 7: Categorical cross-entropy during training phase of the digit recognition CNN.

### 2.4 Metrics

Apart from the losses above, we consider some other metrics for measuring model performance (which are not necessarily metrics in a mathematical sense). Unlike losses these metrics are not minimized or maximized by the model, but are very useful to assess the overall model performance and quality.

### 2.4.1 Metrics for CNN on mortality rates

First, the CNN on mortality rates, which has been setup as a (continuous) regression problem, can a posteriori also be considered as a (binary) classification model by defining a binary variable

$$
b_{i, c}:= \begin{cases}1, & Y_{i, c} \geq q_{0.95}(Y) \\ 0, & \text { otherwise }\end{cases}
$$
![Page 15 Image 1](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p15_img1.jpg)

## Page 16
where $q_{0.95}(Y)$ defines the empirical $95 \%$-quantile of the set of all observations $Y_{i, c}$. We define that an anomaly is present in window $W_{i, c}$ iff $b_{i, c}=1$, i.e. if $Y_{i, c}$ belongs to the $5 \%$ most extreme observations. Remark that a value of $Y_{i, c}$ close to 1 , means that $\bar{r}_{x, t, c, \text { males }}$ and $\bar{r}_{x, t, c, \text { females }}$ are close to 1 , thus, this reflects large migration/errors. By applying the same approach to predictions $\widehat{\mu}\left(\boldsymbol{X}_{i, c}\right)$, sweeping over all quantiles, we can derive the receiver operating characteristic curve (ROC) by plotting true positive rates vs. false positive rates. A metric frequently used for such (binary) classification problems is the area under the curve (AUC), see Figure 8.
Note that due to the different migration/error structures across countries, see Figure 3, we are using AUC also to pre-select countries for the final CNN by applying the following steps.

- For each country $c$, train a (simpler and thus faster) CNN only on input from $c$ and define the square matrix $A$ by setting $A_{c, c^{*}}$ equal to the AUC of the prediction for country $c^{*}$.
- Partition the countries into 4 clusters by methods also discussed in our tutorial [17] and in [4], i.e.
- normalize $A$ by defining $\bar{A}:=R^{-1 / 2} A C^{-1 / 2}$, where $R$ and $C$ are diagonal matrices with diagonals equal to $\sum_{c^{*}} A_{c, c^{*}}$ and $\sum_{c} A_{c, c^{*}}$,
- apply a singular value decomposition (SVD) $\bar{A}=U \Sigma V^{\prime}$, where singular values in $\Sigma$ are sorted non-increasingly,
- apply the $K$-means algorithm on the resulting 2 vectors $\binom{R^{-1 / 2} U_{\cdot j}}{C^{-1 / 2} V_{\cdot j}}$ for $j=2,3$ to obtain 4 clusters of countries.

The final CNN on mortality rates is then only applied on the largest cluster, where migration/ error structures are more homogeneous. ${ }^{3}$

# 2.4.2 Metrics for CNN of digit recognition 

As metric for the digit recognition CNN we use accuracy, i.e. the ratio of correctly classified images, which is $99.65 \%$ on the training set, $99.04 \%$ on validation, and $99.01 \%$ on test data in our example. In Figure 9 we provide the full confusion matrix on the test data.

### 2.5 Results

In this section we summarize and discuss the main results of the two example CNNs, the first one a priori being a regression model, the second one being a classification model.

### 2.5.1 CNN on mortality rates

The primary goal of the CNN on mortality rates is to predict the severity of anomalies (in the sense of equation (1.1)) in a given window of mortality rates. Note that population numbers (exposures) are not used for the prediction, only mortality rates are considered as input. Actual severities $Y_{i, c}$ versus predictions $P_{i, c}:=\widehat{\mu}\left(\boldsymbol{X}_{i, c}\right)$ are shown in Figure 10 for Switzerland (based

[^0]
[^0]:    ${ }^{3}$ The largest cluster consists of the 22 countries Australia, Belarus, Bulgaria, Canada, Czech Republic, Estonia, Finland, Greece, Hong Kong, Iceland, Italy, Japan, Lithuania, New Zealand, Poland, Portugal, Russia, Slovakia, Spain, Taiwan, UK, and Ukraine.

## Page 17
Figure 8: Receiver operating characteristic curve (ROC) of the classification problem on mortality anomalies on test data. Area under the curve (AUC) is $93 \%$.

Figure 9: Confusion matrix of the digit recognition CNN on test data. Overall accuracy is $99.01 \%$.
on the simpler CNN used for clustering) and for all populations of the largest cluster. In an ideal model all samples would lie on the diagonal given by the identity $P=Y$. We observe that, in particular, for the largest cluster of population predictions for larger anomalies (red dots denote the top $5 \%$ ) are better than for smaller anomalies, which could be explained by the fact that only larger anomalies result in a sufficiently large footprint in mortality rates exceeding usual random fluctuations. However, if we focus on Switzerland in Figure 10 we observe a fairly
![Page 17 Image 1](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p17_img1.jpg)
![Page 17 Image 2](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p17_img2.jpg)

## Page 18
strong diagonal picture, which illustrates that this prediction task is done quite successfully on country-specific data. Figure 11 shows outputs and predictions arranged by age and year buckets.
As a secondary goal, we use the CNN on mortality rates to detect anomalies as defined in equation (2.14). This turns the original regression problem into a (binary) classification problem. The preferred way to tackle this problem would be to introduce a new CNN and train this on binary data. However, since we treat detection only as a secondary goal, we directly use the predictions of the original CNN as described above to obtain an already quite strong AUC of $93 \%$.
From Figure 3 we observe for example that for Russian males, the window $t=1961, \ldots, 1970$, $x=71, \ldots, 80$ contains quite some anomalies, in particular locally for $x=80$, which are most probably due to errors. These could be driven by errors in population numbers (exposures) or in mortality rates. In this case, the major driver are mortality rates, where $q_{79,1968, \text { RUS,males }}=$ $8.98 \%$ is a local single outlier being surrounded by values above $10 \%$ along time, age, and cohort directions.

Figure 10: Actual output $Y$ (severity of anomalies) versus prediction $P$ of the CNN on mortality rates for Switzerland (left) and the test set of all population of the largest cluster. Red dots denote the $5 \%$ largest values of $Y$.

# 2.5.2 Digit recognition CNN 

The website where the MNIST dataset can be obtained ${ }^{4}$ provides an overview of several methods (linear classifiers, $K$-nearest neighbors, support vector machines (SVMs), etc.) and their performance in terms of error rates (i.e. 1 less accuracy) on the test dataset. We observe that the simple CNN in this tutorial already achieves quite a remarkably low error rate of $0.99 \%$, which means that out of the $10^{\prime} 000$ images of the test dataset, only 99 are not correctly classified, see off-diagonal values of the confusion matrix in Figure 9. The overview also clearly shows how well CNNs perform on this kind of classification problems and that CNNs outperform most other methods.

[^0]
[^0]:    ${ }^{4}$ http://yann.lecun.com/exdb/mnist/
![Page 18 Image 1](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p18_img1.jpg)

## Page 19
Figure 11: Actual output $Y$ (left) versus prediction $P$ (right) of the CNN on mortality rates for Switzerland (left) arranged by age and year buckets.

# 3 Insights into convolutional neural networks 

In this section we try to demystify how CNNs work by providing insights from several angles. This is more tangible on the digit recognition CNN which we will use throughout this section. We start with some (desired) properties.

### 3.1 Shift invariance

Convolutions are shift invariant, i.e. for a Dirac matrix $\delta_{i_{1}, i_{2}}$ (which means a shift by $\left(i_{1}, i_{2}\right)$ when convoluted)

$$
\delta_{i_{1}, i_{2}} *(\boldsymbol{w} * \boldsymbol{x})=\left(\delta_{i_{1}, i_{2}} * \boldsymbol{w}\right) * \boldsymbol{x}=\boldsymbol{w} *\left(\delta_{i_{1}, i_{2}} * \boldsymbol{x}\right)
$$

This might suggest that CNNs are also shift invariant in the sense that $\widehat{\mu}\left(\delta_{i_{1}, i_{2}} * \boldsymbol{x}\right)$ for some small $i_{1}, i_{2}$ would deliver similar predictions or predictions that are "shifted" in some sense. For some special cases this is indeed true, e.g. assume a single convolutional layer with zeropadding $p_{1}^{(1)}=p_{2}^{(1)}=5$ (and strides and dilation $(1,1)$ ) followed by a global max-pooling layer $f_{1}^{(1)}=n_{1}^{(0)}, f_{2}^{(1)}=n_{2}^{(0)}$. Furthermore, assume that all inputs $\boldsymbol{x}$ have a 5 -pixel border of 0 -valued pixels, such that non-zero pixels "remain" in the image for all $\delta_{i_{1}, i_{2}} * \boldsymbol{x}$ with $-5 \leq\left(i_{1}, i_{2}\right) \leq 5$. Then, clearly $\widehat{\mu}\left(\delta_{i_{1}, i_{2}} * \boldsymbol{x}\right)=$ constant for all $-5 \leq\left(i_{1}, i_{2}\right) \leq 5$.
In general, however, CNNs are not shift invariant, as can also be seen in Figure 12, where we shift the first 20 images of the MNIST dataset given in Figure 4 by values $-5 \leq\left(i_{1}, i_{2}\right) \leq 5$ and plot the component of the correct digit of the output of the softmax layer, black equals 1, white equals 0 . Still, in particular for Computer Vision, shift invariance is a desired property and Figure 12 also reveals that this property holds at least to a certain extent. Improvements can be made for example by data augmentation, i.e. extending the training dataset by shifted variants of the original training images, or also by antialiasing (see, e.g. [23]), e.g. replacing maxpooling layers with non-overlapping areas by overlapping max-pooling and a non-overlapping convolutional layer. Another approach is to increase the depth of the network, see, e.g. [21], where this is proven in a more general framework of scattering networks and wavelet transforms
![Page 19 Image 1](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p19_img1.jpg)

## Page 20
on images considered as Lebesgue-measurable functions $L^{2}\left(\mathbb{R}^{2}\right)$.

Figure 12: Shifting the first 20 images of the MNIST dataset by all values $-5 \leq\left(i_{1}, i_{2}\right) \leq 5$. In the images of the lower two rows green equals 1 (correct prediction) and red equals 0 for each $\left(i_{1}, i_{2}\right)$. The shifted images of the upper two rows correspond to the upper left corners, i.e. $(-5,-5)$.

# 3.2 Rotation invariance 

Rotation invariance might be desired in some cases, e.g. detecting floods in satellite images, but is not desired in other cases like for example digit recognition where a 6 and a 9 should be treated as different numbers. In Figure 13 we provide (some of) the outputs of the softmax layer of the digit recognition CNN under various rotation angles. Clearly, rotation invariance is not given.

Figure 13: Outputs of the softmax layer when rotating the digit 6, the lower graph shows the softmax probabilities for digits $6,9,8$ and 5 in blue, red, yellow and green colors.

### 3.3 Scale invariance

In Figure 14, we provide the outputs of the softmax layer (of the correct digit) when scaling the first 20 images of the MNIST dataset by values ranging from $(0.5,0.5)$ (upper left corner) to
![Page 20 Image 1](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p20_img1.jpg)
![Page 20 Image 2](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p20_img2.jpg)

## Page 21
$(1.5,1.5)$ (lower right corner). Although scale invariance in general is not given by a CNN, digits are still very well recognized in our example across a wide range as can be seen from Figure 14.

Figure 14: Scaling the first 20 images of the MNIST dataset by values ranging from $(0.5,0.5)$ (upper left corner) to $(1.5,1.5)$ (lower right corner), green equals 1 (correct prediction), red equals 0 . The scaled images of the upper two rows correspond to the lower left corners, i.e. scaling by $(1.5,0.5)$.

# 3.4 Layer visualizations 

One way to obtain further insights into CNNs is by visualizing the outputs of each layer, see Figure 15. While the first layer still can be analyzed whether the applied filters are similar to commonly used filters like edge detection or blurring, the later layers do not seem to provide further insights in an easily understandable manner. In particular, the structure of the 10 dot-products represented by the fully-connected layer remains very intransparent.

Figure 15: Visualization of the outputs of the 3 convolutional layers (on rows) with 10, 20 (displayed as $2 \times 10$ ), and 40 (displayed as $4 \times 10$ ) filters.
![Page 21 Image 1](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p21_img1.jpg)
![Page 21 Image 2](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p21_img2.jpg)

## Page 22
# 3.5 Trying to invert CNNs 

Another way to obtain insights into (classification) CNNs is by trying to invert them, i.e. considering the CNN as a mapping from inputs to categories and then finding the pre-image of each category. We present three approaches to formalize this idea.

1. Backtracking along maximum weights. We briefly sketch the algorithm behind this idea. Starting with a given category from the fully-connected layer, there are 640 weights (excluding the bias/offset) connecting this category to the previous layer. Pick the, say, $1 \%$ largest weights and follow them to the previous layer, where this corresponds to a subset $S$ of the $4 \times 4 \times 40$ input of the flatten layer. Let the elements of $\boldsymbol{x} \in \mathbb{R}^{4 \times 4 \times 40}$ be equal to the corresponding weight if in $S$, and be zero otherwise. Continuing this approach by duplicating values (or picking a single value) for max-pooling layers and multiplying with the, say, $1 \%$ largest weights starting from each non-zero value of convolutional layers (averaging across overlaps), we eventually get to the first layer to obtain a $28 \times 28$ image for the category we started from, see, e.g. [14] where essentially this approach is applied.
2. Activation maximization. The idea behind this approach - also known as deep dream - is to maximize the CNN output $\widehat{\mu}(\cdot)_{j}$ for each category $j$, i.e. find

$$
\boldsymbol{x}^{(j)}:=\underset{0 \leq \boldsymbol{x} \in B_{1}}{\arg \max }\left(\widehat{\mu}(\boldsymbol{x})_{j}\right)
$$

where $B_{1}$ is a unit-ball with respect to a suitable norm, e.g. maximum norm on $\mathbb{R}^{n_{1}^{(0)} \times n_{2}^{(0)}}$. The maximum is not necessarily unique but performing a simple gradient ascent algorithm will provide a single $\boldsymbol{x}^{(j)}$ for each category $j$. Often, additional regularization is applied to derive more "meaningful" images, see e.g. [19] as one of the first papers to apply this approach.
3. Decoder network. Another approach is to design an inverse network, i.e. considering the original CNN as an encoder from images to one-hot vectors of digits, and design a decoder network that maps digits to images. Both networks together can be considered an autoencoder, however, of course, with the restriction that the encoding should be one-hot vectors of the digits. In Table 4, we provide the structure of a decoder network, where two additional types of layers are used - a reshape layer to change the input dimensions, analogous to a flatten layer, and an upsample layer to reverse max-pooling - and Figure 16 shows the predictions of all 10 digits.

Figure 16: Predictions of the decoder network for all 10 digits.
![Page 22 Image 1](cs9_convolutional_neural_network_case_studies_assets/cs9_convolutional_neural_network_case_studies_p22_img1.jpg)

## Page 23
Table 4: Decoder network that tries to invert the CNN given in Table 3 with $2^{\prime} 590$ learnable parameters.

| Layer | input size | output size | $f_{1}^{(k)}, f_{2}^{(k)}$ | $p_{1}^{(k)}, p_{2}^{(k)}$ | $m^{(k)}$ | \#parameters |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| 1. Fully conn. | $10 \times 1$ | $49 \times 1$ | - | - | - | $49 \cdot 10+49$ |
| 2. ReLU $\phi$ | $49 \times 1$ | $49 \times 1$ | - | - | - | 0 |
| 3. Reshape | $49 \times 1$ | $7 \times 7$ | - | - | - | 0 |
| 4. Conv. | $7 \times 7$ | $7 \times 7 \times 20$ | 3,3 | 1,1 | 20 | $20 \cdot 3^{2}+20$ |
| 5. ReLU $\phi$ | $7 \times 7 \times 20$ | $7 \times 7 \times 20$ | - | - | - | 0 |
| 6. Upsample | $7 \times 7 \times 20$ | $14 \times 14 \times 20$ | 2,2 | 1,1 | - | 0 |
| 7. Conv. | $14 \times 14 \times 20$ | $14 \times 14 \times 10$ | 3,3 | 1,1 | 10 | $10 \cdot 20 \cdot 3^{2}+10$ |
| 8. ReLU $\phi$ | $14 \times 14 \times 10$ | $14 \times 14 \times 10$ | - | - | - | 0 |
| 9. Upsample | $14 \times 14 \times 10$ | $28 \times 28 \times 10$ | 2,2 | 1,1 | - | 0 |
| 10. Conv. | $28 \times 28 \times 10$ | $28 \times 28$ | 2,2 | 1,1 | 1 | $10 \cdot 2^{2}+1$ |

# 4 Summary 

In this tutorial we have provided a general introduction to convolutional neural networks (CNNs), i.e. feed-forward networks with specific structures and properties given by convolutional layers. For image recognition and similar problems to detect patterns in (typically) multi-dimensional data, CNNs perform extremely well, and they can be considered as one of the major contributors for the success and popularity of deep learning over the past years.
We used two example CNNs, a regression model on mortality rates and a classification model on images of hand-written digits to demonstrate the strengths and properties of CNNs. We provided a list of commonly used pre-trained CNNs that can also be used for transfer learning, and we tried to demystify how CNNs work by analyzing properties like shift, rotation and scale invariance. The presented approaches to visualize a trained CNN provide further useful insights. Despite these insights we conclude with the remark that there remains a substantial gap to theoretically explain and grasp the reasons for the striking empirical success of CNNs.

## References

[1] S. Bai, J. Z. Kolter, and V. Koltun. "An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling." arXiv:1803.01271, 2018
[2] Y. Cheng, F. Wang, P. Zhang, and J. Hu. "Risk Prediction with Electronic Health Records: A Deep Learning Approach." Proceedings of the 2016 SIAM International Conference on Data Mining, 2016
[3] D. C. Ciresan, U. Meier, L. M. Gambardella, and J. Schmidhuber. "Deep Big Simple Neural Nets Excel on Handwritten Digit Recognition." arXiv:1003.0358, 2010
[4] I. S. Dhillon. "Co-Clustering Documents and Words using Bipartite Spectral Graph Partitioning." Proceedings of the Seventh ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 269-274, 2001
[5] A. Ferrario, A. Noll, and M. V. Wüthrich. "Insights from Inside Neural Networks." Available at SSRN: https://ssrn.com/abstract=3226852, 2018
[6] K. Fu, D. Cheng, Y. Tu, and L. Zhang. "Credit Card Fraud Detection Using Convolutional Neural Networks." ICONIP 2016: Neural Information Processing, pp. 483-490, 2016

## Page 24
[7] K. Fukushima. "Neocognitron: A Self-organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position." Biological Cybernetics, 36 (4), pp. 193-202, 1980
[8] G. Gao, and M. V. Wüthrich. "Convolutional Neural Network Classification of Telematics Car Driving Data." Risks, 7 (1), 6, 2019
[9] R. Geirhos, D. H. J. Janssen, H. H. Schütt, J. Rauber, M. Bethge, and F. A. Wichmann. "Comparing Deep Neural Networks Against Humans: Object Recognition When the Signal Gets Weaker." arXiv:1706.06969, 2017
[10] I. Goodfellow, Y. Bengio, and A. Courville. "Deep Learning." MIT Press, 2016
[11] E. Grefenstette, P. Blunsom, N. de Freitas, and K. M. Hermann. "A Deep Architecture for Semantic Parsing." arXiv:1404.7296, 2014
[12] Y. LeCun, B. Boser, J. S. Denker, D. Henderson, R. E. Howard, W. Hubbard, and L. D. Jackel. "Handwritten Digit Recognition with a Back-Propagation Network." In Advances in Neural Information Processing Systems, 1990
[13] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. "Gradient-Based Learning Applied to Document Recognition." Proceedings of the IEEE, Vol 86, pp. 2278-2324, 1998
[14] H. Lee, R. Grosse, R. Ranganath, and A. Y. Ng. "Convolutional Deep Belief Networks for Scalable Unsupervised Learning of Hierarchical Representations." ICML '09: Proceedings of the 26th Annual International Conference on Machine Learning, pp. 609-616, 2009
[15] M. Leshno, V. Y. Lin, A. Pinkus, A., and S. Schocken. "Multilayer Feedforward Networks with a Nonpolynomial Activation Function Can Approximate Any Function." Neural Networks. 6 (6), pp. $861-867,1993$
[16] F. Perla, R. Richman, S. Scognamiglio, and M. V. Wüthrich. "Time-Series Forecasting of Mortality Rates using Deep Learning." Available at SSRN: https://ssrn.com/abstract=3595426, 2020
[17] S. Rentzmann, and M. V. Wüthrich. "Unsupervised Learning: What is a Sports Car?" Available at SSRN: https://ssrn.com/abstract=3439358, 2019
[18] D. Silver, A. Huang, C. Maddison et al. "Mastering the Game of Go with Deep Neural Networks and Tree Search." Nature 529, pp. 484-489, 2016
[19] K. Simonyan, A. Vedaldi, and A. Zisserman. "Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps." arXiv:1312.6034, 2013
[20] S. Ioffe, C. Szegedy. "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift." arXiv:1502.03167, 2015
[21] T. Wiatowski, and H. Bölcskei. "A Mathematical Theory of Deep Convolutional Neural Networks for Feature Extraction." IEEE Transactions on Information Theory, Vol 64 (3), pp. 1845-1866, 2018
[22] C. Xiao, E. Choi, and J. Sun. "Opportunities and Challenges in Developing Deep Learning Models using Electronic Health Records Data: a Systematic Review." Journal of the American Medical Informatics Association, Vol 25, Issue 10, pp. 1419-1428, 2018
[23] R. Zhang. "Making Convolutional Networks Shift-Invariant Again." arXiv:1904.11486, 2019
[24] S. Zhou, W. Shen, D. Zeng, M. Fang, Y. Wei, and Z. Zhang. "Spatial-Temporal Convolutional Neural Networks for Anomaly Detection and Localization in Crowded Scenes." Signal Processing: Image Communication, Vol 47, pp. 358-368, 2016