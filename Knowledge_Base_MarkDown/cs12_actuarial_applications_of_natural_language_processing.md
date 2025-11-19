_Note: Source document was split into 3 OCR chunks (pages 1-13, pages 14-29, pages 30-37) to stay within token limits._

# CS12 Actuarial applications of natural language processing

## Page 1
# Actuarial applications of natural language processing using transformers: Case studies for using text features in an actuarial context 

Andreas Troxler ${ }^{1}$ and Jürg Schelldorfer ${ }^{2}$<br>${ }^{1}$ AT Analytics Ltd, Forchwaldstrasse 57, 6318 Walchwil, Switzerland<br>${ }^{2}$ Swiss Re Management Ltd, Mythenquai 50/60, 8022 Zurich, Switzerland<br>Corresponding author: Andreas Troxler; Email: andreas.troxler@atanalytics.ch


#### Abstract

This paper demonstrates workflows to incorporate text data into actuarial classification and regression tasks. The main focus is on methods employing transformer-based models. A dataset of car accident descriptions with an average length of 400 words, available in English and German, and a dataset with short property insurance claims descriptions, are used to demonstrate these techniques. The case studies tackle challenges related to a multilingual setting and long input sequences. They also show ways to interpret model output and to assess and improve model performance, by fine-tuning the models to the domain of application or to a specific prediction task. Finally, the paper provides practical approaches to handle classification tasks in situations with no or only few labelled data. The results achieved by using the language-understanding skills of off-the-shelf natural language processing (NLP) models with only minimal pre-processing and fine-tuning clearly demonstrate the power of transfer learning for practical applications.


Keywords: Natural language processing; transformer; multilingual models; domain-specific fine-tuning; integrated gradients; extractive question answering; zero-shot classification; topic modelling

## 1. Introduction and Overview

The main purpose of this paper is to introduce natural language processing (NLP) in an actuarial context. We start with a brief overview of NLP and traditional approaches, and then provide an introduction to NLP using transformers. We provide an overview of different workflows to incorporate NLP into actuarial contexts. We apply the concepts to two datasets that are typical in actuarial applications. The first dataset contains verbal descriptions of car accidents in both English and German language, as well as some tabular data such as the number of vehicles involved and the presence of bodily injury. The second dataset contains short descriptions of property insurance claims. The case studies in this paper tackle challenges arising from a multilingual setting, long input sequences, and also cover interpretability, which is of paramount importance in machine learning, and, in particular, in an actuarial context, where decisions need to be transparent and explainable. Finally, the paper provides practical approaches to handle classification tasks in situations with no or only few labelled data. This article was originally written for the working party "Data Science" of the Swiss Association of Actuaries SAV, see https://www.actuarialdatascience.org/. It is accompanied by notebooks documenting the Python implementation. The datasets and the notebooks are available from Swiss Association of Actuaries (2023).

[^0]
[^0]:    (c) The Author(s), 2024. Published by Cambridge University Press on behalf of Institute and Faculty of Actuaries. This is an Open Access article, distributed under the terms of the Creative Commons Attribution licence (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted re-use, distribution, and reproduction in any medium, provided the original work is properly cited.

## Page 2
# 2. What is NLP and Why Is It Interesting and Challenging? 

An abundant amount of information is available in the form of text. However, language data is generally unstructured, and single words or phrases taken out of a context can be highly ambiguous. This makes it complex to exploit the data within algorithms, because computers are best suited to processing structured data.

In an insurance context, text data is used in a vast number of applications and areas, such as:

- Customer interaction: supporting the customers in their journey to purchase the right insurance product or to submit a claim.
- Underwriting: processing of medical reports, risk survey reports, etc.
- Claims handling: processing of first notices of loss reports to direct the information to the appropriate department or to control fully automated processing of simple and small claims; processing of loss adjuster's or expert's reports to support the setting of case reserves; detection of claims with recovery or litigation potential.
- Anonymisation of documents with personal information before further processing in compliance with relevant data protection regulation.

Natural language processing (NLP) seeks to convert speech and text data into a structured data format to enable machines to

- understand the information conveyed, and use this information to support decision making (natural language understanding, NLU).
- formulate relevant, contextual responses (natural language generation, NLG).

Typical NLU tasks for written text data are:

- Sequence classification: classify a sequence according to a given number of classes (e.g. classify a text document as being a medical report).
- Extractive question answering: extract an answer to a question from a given text. The term "extractive" means that the answer is an extract of the text, as opposed to a generated new text.
- Masked language modelling: learn word associations from a large text corpus - an unstructured collection of possibly domain-specific text. A random fraction of words in the input text is masked, and the model is prompted to fill in the space with an appropriate word.
- Causal language modelling: fit a language model to a text corpus, by predicting the token following a sequence of tokens (also known as next-word or next-sentence prediction).
- Named entity recognition: classify tokens according to a class, for example, identifying a token as a person, an organisation or a location.
- Summarisation: summarise a document or an article into a shorter text.
- Machine translation.

We apply some of the above-mentioned tasks to enable the use of text data as features (or to augment other available features) for classification and regression tasks.

Practical applications, in particular, in an insurance context, often come with a number of challenges:
a. The text corpus may be highly domain-specific, i.e. it may use specialised terminology.
b. Multiple languages might be present simultaneously.
c. Text sequences might be short and ambiguous, or they might be so long that it is hard to identify the parts relevant to the task.

## Page 3
d. The amount of training data may be relatively small. In particular, gathering large amounts of labelled data (i.e. text sequences augmented with a target label) might be expensive.
e. It is important to understand why a model arrives at a particular prediction or classification.

This paper illustrates techniques to address these challenges. We use two data sets:

- Verbal descriptions of around 7,000 car accidents available in English (and translated into German), as well as some tabular data (number of vehicles involved, indicator of presence of bodily injury etc.) which can be used as response variables to train predictive models. The length of the texts averages around 400 words and sometimes exceeds 1,000 words.
- A dataset of circa 6,000 property insurance claims records that include a claim amount, a very short English claim description and a hazard type with 9 different levels.

Appendix A provides more detail on the data used.

# 3. A Brief Overview of NLP Approaches 

The field of NLP has made significant progress over the past decades. An excellent introduction is provided in Ferrario \& Nägelin (2020), which distinguishes three broad approaches to text classification:

1. Classical NLP pipelines based on bag-of-words and bag-of-part-of-speech methods to generate a numerical representation of text documents, used as input to a classifier.
2. Modern approaches using word embeddings (and some aggregation of word embeddings into sentence embeddings by a sentence encoder) to numerically represent text documents, again used as input to a classifier.
3. Contemporary approaches that apply a minimum degree of pre-processing and train recurrent neural networks directly on text documents.

For the sake of context, the following subsections briefly explain the key concepts of these approaches. For more details we refer to Ferrario \& Nägelin (2020). The remainder of this paper will focus on transformer models, introduced in the next section.

### 3.1. Classical NLP Pipelines

This section describes the typical elements of a classical machine learning pipeline for text classification. The key steps involve:

1. Text pre-processing.
2. Computing a numerical representation of the text.
3. Using the numerical representation as input feature for a classifier.

The following sections explain and discuss each of these steps.

### 3.1.1. Text pre-processing

The goal of text pre-processing is to transform the text to make it suitable for predictive modelling. Essentially, the text is broken down into tokens, i.e. elements of a vocabulary. This allows encoding of the text by integers - the identifiers of the vocabulary elements. The required functionality is provided by libraries such as spaCy (Honnibal \& Montani, 2017) and nltk (Bird et al., 2009).

Figure 1 shows a fictional example.

## Page 4
Figure 1. Fictional example of text pre-processing. The text is converted to lowercase, stemmed ("occurred" becomes "occur"; "intersection" becomes "intersect") and split into tokens. Stopwords such as "the," "at" and "an" are removed. The misspelled word "crach" is not in the dictionary and is represented by a special token. In this example, punctuation is suppressed. The emphasis on the word "intersection" is lost, because formatting is suppressed, and all words are converted to lowercase.

The following paragraphs briefly explain typical pre-processing steps and some of the issues that may arise. Depending on the application, not all steps are necessarily required.

Import of the raw text and formatting. There is no such thing as clean data. Issues may arise around encoding, formatting, removal of HTML tags from web documents, etc.

Conversion to lowercase. This is a common procedure in NLP text processing, as it generates a harmonised string out of uppercase and lowercase variants of the same word. However, for some languages, the case can convey meaning (e.g. names of named entities, German nouns etc.), so this step could result in loss of information.

Tokenisation. This step splits the text into items of a vocabulary. The vocabulary is either generated based on rules from the present text data, or it is pre-defined from a large corpus of texts. In the latter case, if the present text contains words that are not present in the vocabulary, they can be mapped to a special token. This might result in a significant loss of information, for example when the present text contains domain-specific words that are significant for the NLP task.

The following broad approaches are available:

- Word-based tokenisation splits text based on spaces or punctuation. Since each token represents an entire word, the information content per token is high. Limitations include similar and closely related words (e.g. "cat" and "cats") being represented by different tokens, vocabulary being very large and words missing in the vocabulary being mapped to a special token causing a loss of information.
- Character-based tokenisation splits text into individual characters. Compared to word-based tokenisation, this leads to a smaller vocabulary, and out-of-vocabulary tokens will be less frequent. On the other hand, the information content per token is much smaller (unless for ideogram-based languages), and the token sequences to be processed by the model are much longer, thus limiting the maximum allowable text length.
- Subword-based tokenisation combines the advantages of the previous approaches by retaining frequent words and splitting rarer words into subwords (e.g. "cats" into "cat" +"s", prefixes and suffixes). Compared to word-based tokenisation, the vocabulary size is much smaller, as information is shared across different words. Many algorithms are available, such as WordPiece, Unigram and Byte-Pair Encoding.

Tokenisation rules differ in many aspects, for example in how they treat punctuation (e.g. suppression of punctuation, punctuation as separate tokens, etc.), how they treat prefixes and suffixes, or whether they apply a minimum token length. The importance of these choices depends on the language. For instance, interpunctuation rules differ between French ("n'est-ce pas") and English ("we don't"), etc.

Removal of stopwords. Stopwords are frequent words with little semantic meaning. Examples might be "the" and "to" in English. Removing these words reduces the dimensionality of the
![Page 4 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p04_img1.jpg)

## Page 5
vocabulary and might improve the predictive power of the NLP model. Stopwords are based on a corpus of text in a given language.

Part-of-speech-tagging. Another step is tagging each token with part-of-speech (POS) attributes, such as noun, verb, adjective, etc. Models to achieve this are pre-trained on text corpora. As such, they are language specific.

Stemming or lemmatisation. Stemming and lemmatisation are two procedures that reduce inflectional forms to their stem by truncating pre- and suffixes, conjugations and declinations. The goal of this step is to reduce vocabulary size. It is language specific. Stemming algorithms strip affixes off words to reduce them to their root forms, which need not be words in the given language. For example, the English word "moving" would be reduced to "mov." Lemmatisation is a more complex approach to the problem of determining the stem of a word. This process involves first determining the part-of-speech of a word and applying different normalisation rules for each part-of-speech. Often one uses a pre-trained library for this.

# 3.1.2. Computing numerical representations of the text: bag-of-word models 

The previous steps have transformed a raw text into a sequence of tokens. Since the text corpus contains a defined vocabulary of unique tokens, this delivers the encoding of the raw text into a sequence of integers (representing the identifier of each token), see Figure 1.

The next step involves defining a real-valued representation of this sequence, which can be used as input feature to a classifier. One approach is the so-called "bag-of-words" model.

Bag-of-words model. The bag-of word model maps each token sequence into a vector $x \in \mathbb{N}_{0}^{V}$, where $V$ is the vocabulary size, and the $i$-th element of $x$ is the number of occurrences of token $i$ in the sequence.

A drawback of this approach is that the ordering of words gets lost; this issue will be discussed later. Further, each word is treated as being equally important. However, certain words are much more frequent in the corpus than others (e.g. "the," "a," "is" in English), but carry very little meaningful information about the actual contents of the text. If we were to feed the direct count data directly to a classifier those very frequent terms would shadow the frequencies of rarer yet more interesting terms. This drawback can be mitigated by normalisation.

Normalisation. Normalisation applies weights to the token counts with diminishing importance for tokens that occur in the majority of documents. This produces a floating-point vector $\tilde{x} \in \mathbb{R}^{V}$. A common approach is the so-called "TF-IDF" transform. It multiplies the term frequency (TF) $x$ obtained from the bag-of-words by the "inverse document-frequency" (IDF), which is a function of the inverse of the proportion of documents which contain the term, with some additional normalisation. For more details we refer to Baeza-Yates \& Ribeiro-Neto (2011) and Manning et al. (2008).

### 3.1.3. Using the bag-of-words model for text classification

Finally, the vector $\tilde{x} \in \mathbb{R}^{V}$ is used as input feature for a classifier, such as naïve Bayes, tree-based methods, support vector machines, neural networks, etc.

### 3.1.4. Discussion and variants

The bag-of-words method is simple to construct - all it takes is a vocabulary and a simple count. One disadvantage is the large feature space for the classification task. Also, the bag-of-words mapping is not injective as the order of occurrence of the word gets lost. Therefore, the bag-ofwords model cannot capture phrases and multi-word expressions, effectively disregarding any word order dependence.

## Page 6
Depending on the application, this loss of information may be detrimental to understanding the meaning of the text. For instance, consider the two sentences: "The driver of the minivan ignored the red traffic light and crashed into pickup truck" and "The driver of the pickup truck overlooked the red minivan and crashed into the traffic light." They have a very different meaning, but they will be mapped to the identical feature vector. If the classification task is about predicting which driver is at fault, this leads to problems. On the other hand, if the classification task is about distinguishing car accident reports from fire claim descriptions, bag-of-words might work well.

The problem of word ordering can be mitigated by considering n-grams instead of single words (unigrams). An n-gram is a sequence of $n$ words. Instead of building a simple collection of unigrams $(n=1)$, one might prefer a collection of bigrams $(n=2)$, where occurrences of pairs of consecutive words are counted. Of course, this comes at the cost of much higher dimensionality.

# 3.2. Modern Approaches based on Word Embeddings 

### 3.2.1. Motivation and concept

As discussed in Section 3.1.4, one drawback of the bag-of-words model is the high dimensionality of the feature space, which is equal to the size of the vocabulary, $V$.

The technique of word embeddings, introduced by Bengio et al. (2003), overcomes this by mapping each token in the vocabulary to a much lower-dimensional Euclidean space $\mathbb{R}^{E}, E \ll V$. This mapping is constructed in such a way that tokens with similar meaning are close in $\mathbb{R}^{E}$. Mathematically, the embedding can be described by a matrix $W \in \mathbb{R}^{V \times E}$; the embedding of token $i$ is simply row $i$ of $W$.

Various algorithms are available to produce embeddings. Some of the most important methods are the following:

- Word to vector algorithm (word2vec): Mikolov et al. (2013a) and Mikolov et al. (2013b) developed two algorithms based on the key idea that the similarity of words can be learned from the context in which the words are used, i.e. the surrounding words, in a given text corpus. One algorithm is based on predicting the centre word from its context ("continuous-bag-of-words," "CBOW"), and the other one is based on predicting the context from the centre word ("skip-gram").
- Global vector algorithm (GloVe): The global vector algorithm is an unsupervised word embedding methodology developed by Pennington et al. (2014). It is trained on the matrix of word co-occurrence counts of the entire text corpus (as opposed to one context window at a time).

For details, we refer to Ferrario \& Nägelin (2020) and. Note that the approaches described in the following sections also use word embeddings.

### 3.2.2. Using word embeddings for text classification

The starting point is a tokenised text, obtained from a pre-processing process as explained in Section 3.1.1. The word embedding is applied to these tokens.

In practical applications, the volume of available text data may not be sufficiently large to train embeddings from scratch. In this case, pre-trained embeddings can be used, which are available in packages such as Pennington et al. (2014) and Bird et al. (2009), trained on Wikipedia and other large text corpuses. The use of pre-trained embeddings speeds up the process significantly. However, it can be problematic if the text data uses a domain-specific vocabulary (or common words with a very specific meaning) which is not covered adequately by the corpus that has been used to train the embedding. Also, words with multiple meanings may be problematic, such as the English words "fire" (verb or noun); "well" (adjective, adverb, noun, verb); "will" (verb, noun); etc.

## Page 7
There are different ways to use word embedding in text classification applications:

- Mean pooling: apply word embedding to all tokens of the input sequence and take the average of the embedding. This produces a vector in $\mathbb{R}^{E}$, which is used as input feature to a classifier. With this approach, the order of the token sequence gets lost.
- Feed all the word embeddings of the text sequence into a dense neural network with an activation function suitable for classification. To ensure that all inputs have the same length, long sentences are truncated and short sequences are padded. If pre-trained embeddings are used, the embedding layer can either be kept constant, or it can be included in the training of the neural network, in order to adapt to domain-specific meanings of words. The dimension of the input feature into the neural network is $E \times T$, where $T$ is the sequence length and $E$ the dimension of the embedding.


# 3.3. Contemporary Approaches using Recurrent Neural Networks 

The approaches described have the drawback that they either lose information about the order of words, or they produce high-dimensional input features for the classifier.

An alternative approach is given by recurrent neural networks (RNN), which feed the input tokens sequentially through a neural network, and also feed hidden states from one step to the next, thus keeping information on the previous steps in memory. The hidden state produced by the last step is then used as input feature to the classifier. The basic architecture is shown in Figure 2. In practice, often only one or a few layers are used.

The elements of the architecture are as follows:

1. The starting point is the pre-processed text, as obtained from the workflow described in Section 3.1.1.
2. The texts are truncated to a maximum length of $T$ tokens. Shorter texts are padded with a special token.
3. For each step $t \in\{1,2, \ldots, T\}$ in the sequence, the token is passed through an embedding layer, resulting in a vector $x_{t} \in \mathbb{R}^{E}$.
4. This input is fed into one or more layers of the RNN.
a. The first layer is fed by $x_{t} \in \mathbb{R}^{E}$ and $z_{t-1}^{(1)} \in \mathbb{R}^{H_{1}}$, the hidden state of the first layer from the previous step, where $H_{1}$ denotes the size of the first hidden layer, and with the initial value $z_{0}^{(1)}=0$.
b. The subsequent layers $l \in\{2, \ldots, L\}$ are fed by $z_{t}^{(l-1)} \in \mathbb{R}^{H_{l-1}}$ and $z_{t-1}^{(l)} \in \mathbb{R}^{H_{l}}$.
5. The hidden state of the last layer of the final step, $z_{T}^{L} \in \mathbb{R}^{H_{1}}$ is used as input to the classifier, a dense layer with a suitable activation function for the classification task.

Note that the embedding layer and the RNN layer in items 3 and 4 are identical for all steps, i.e. they share the weights. Different architectures are available for the RNN layers:

- Plain-vanilla dense layers: if these networks are trained with backward propagation trough time (BPTT), the necessary computation of gradients is recursive and often leads to either exploding or vanishing gradients with respect to time (Bengio et al., 1994). This leads to numerical instability or inability to learn long-distant associations (Pascanu et al., 2013).
- Long-short-memory (LSTM) units (Hochreiter \& Schmidhuber, 1997), which use in addition to the hidden state a cell state for long-term memory storage (not shown in Figure 2).
- Gated recurrent units (GRU) (Cho et al., 2014), a similar but less complex architecture.

## Page 8
Figure 2. Basic architecture of a recurrent neural network.

We refer to section 8 of Wüthrich & Merz (2023) and section 5 of Ferrario & Nägelin (2020) for more details, and we recommend the paper Richman & Wüthrich (2019). For the embedding layer, different options are available:

- Train the embedding layer from scratch: this is computationally expensive and requires a large amount of data.
- Use pre-trained embeddings and keep them fixed during the training of the RNN classifier: this reduces computation time and complexity significantly, but it can be problematic if the text data uses a domain-specific vocabulary.
- Use pre-trained embeddings and update the weights of the embedding layer during the training process.

The basic architecture has been extended in different ways. For instance, bidirectional recurrent neural networks (BRNN) connect two hidden layers of opposite directions to the same output. Further, one-dimensional convolutions can be used to compress the input layer.

As can be seen from Figure 2, RNNs use sequential processing of the text: to produce the hidden state of the second token in the sequence, hidden states of the first token need to be calculated first. This inhibits parallel processing within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across samples. This lack of parallelisation leads to a performance bottleneck.

Further, the basic architecture described here follows the Markov property: each state is assumed to be dependent only on the previously seen state. This can lead to problems processing sequences with long-range dependencies and is the reason why LSTMs and GRUs are useful.

## 4. NLP using Transformers

The drawbacks of RNNs are mitigated by the transformer architecture proposed by Vaswani et al. (2017). Since their introduction, transformer-based architectures have quickly become dominant
![Page 8 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p08_img1.jpg)

## Page 9
**Figure 3.** Basic architecture of the transformer encoder. The architecture of a transformer encoder layer is shown in the right part of the graph.

for achieving state-of-the-art results on many NLP tasks. This is the reason why the remainder of this paper focuses exclusively on transformer-based approaches.

The transformer reads the entire sequence of words at once ("bidirectional)," as opposed to directional models, which read the text input sequentially (left-to-right or right-to-left). A language model which is bidirectionally trained can have a deeper sense of language context and flow than single-direction language models, because a word may relate to other words earlier or later in the same sentence.

We recommend Alammar (2018) for an easy-to-follow introduction to the transformer architecture. Tunstall et al. (2022) use a hands-on approach to teach how transformers work and how to integrate them in applications.

Figure 3 shows a high-level representation of the transformer architecture:

Comparing Figure 3 to Figure 2, we notice that there are no horizontal connectors and the transformer encoder layer receives the full embedded sequence at once. This reflects the non-sequential nature of the architecture. Both architectures start with an embedding layer producing the embedding *x<sub>t</sub>* ∈ ℝ<sup>E</sup> for each token. In order to inject some information on the position of each token in the input sequence, the transformer architecture uses a "positional encoding" – a vector of the same dimension *E* as the encoding, following a fixed pattern of sine and cosine waves, which is summed to the input embedding.

The transformer encoder layer consists of a self-attention layer and a feed-forward neural network.

The motivation for using attention is to be able to model dependencies regardless of the distance in the sequence. The attention concept has been introduced by Bahdanau et al. (2014), also referred to as "additive attention." The transformer uses the so-called dot product attention mechanism.

The self-attention layer helps the encoder to look at other words in the input sequence as it encodes a specific word. For a sequence of length *T*, it computes a matrix *A* ∈ [0, 1]<sup>*T*</sup> × <sup>*T*</sup> (attention matrix) with pairwise attention scores. The element *A<sub>i,j</sub>* determines how strongly the encoding of
![Page 9 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p09_img1.jpg)

## Page 10
the token at position $i$ should pay attention to the token at position $j$. The rows are normalised to have unit sum. The attention matrix $A$ is calculated from the input sequence itself (hence the term self-attention). This basically gives weights according to the importance of certain words in the entire sentence.

The transformer architecture uses a multi-headed attention which runs through an attention mechanism several times in parallel. The independent attention outputs are then concatenated and linearly transformed into the dimension $\mathbb{R}^{T \times E}$. In what follows, we denote by $X \in \mathbb{R}^{T \times E}$ the layer input. For the first encoder layer, this is the embedded input sequence; for the other layers, it is the output of the previous encoder layers. The transformer encoder layer works as follows:

1. Apply the multi-head attention, with the subscript $h=1, \ldots, H$ denoting the head:
a. Apply three linear transformations to the input $X \in \mathbb{R}^{T \times E}$ to obtain three matrices $V_{h}, Q_{h}, K_{h} \in \mathbb{R}^{T \times d_{K}}$ (called "value," "query," "key"), where the linear transformations are represented by weight matrices $W_{h}^{V}, W_{h}^{Q} W_{h}^{K} \in \mathbb{R}^{E \times d_{K}}$, which are learned during the training process. The dimension $d_{K}$ is a hyperparameter.
b. The attention matrix is calculated from the key and value matrices: $A_{h}=\operatorname{softmax}\left(\frac{Q_{h} K_{h}^{T}}{V_{h}^{T}}\right)$. The softmax function normalises each row to unit sum, as desired. The denominator ensures well-behaved magnitude of the gradients when $d_{K}$ is large.
c. The output of the self-attention is given by $Y_{h}=A_{h} V_{h}$ (dot product attention).
d. Finally, the outputs $Y_{h}$ are concatenated and linearly transformed into $Y^{(1)}=\sum_{h} Y_{h} W_{h}^{O} \in \mathbb{R}^{T \times E}$, where is $W_{h}^{O} \in \mathbb{R}^{H . d_{k} \times E}$ another weight matrix learned during the training process.
2. To speed up convergence of the training process, apply residual connection (also known as skip connection) (He et al., 2016) and layer normalisation (Ba et al., 2016):

$$
Y^{(2)}=\operatorname{LayerNorm}\left(X+Y^{(1)}\right) \in \mathbb{R}^{T \times E}
$$

3. The fully connected feed-forward neural network uses two linear transformations and a ReLU activation in between, to produce $Y^{(3)} \in \mathbb{R}^{T \times E}$. The exact same feed-forward network is independently applied to each position of the sequence.
4. Apply again residual connection and layer normalisation to produce the output $Z \in \mathbb{R}^{T \times E}$.

An interpretation of the attention mechanism is as follows:

- The attention matrices $A_{h}$ are weights that can be understood as importance weights.
- $Y_{h}$ is then a new representation of the values $V_{h}$, where the values are weighted according to their importance.

There are many different variants of the transformer architecture. In this paper, we use mainly models derived from the BERT model. BERT (Bidirectional Encoder Representations from Transformers) was introduced by Devlin et al. (2019) and developed to state-of-the-art on a large number of NLP tasks. The BERT model has over 100 million parameters, which are pre-trained on two tasks, Masked Language Modelling (MLM) and Next-Sentence Prediction (NSP). This pretraining is performed on a large corpus of text data. The language mix of this text corpus determines the language(s) understood by the model.

In MLM, a random fraction of tokens of the input sequence is masked (i.e. replaced by the MASK token). The model then attempts to predict the original value of the masked tokens, based on the context provided by the other, non-masked tokens in the sequence. This procedure can be performed in a fully unsupervised fashion. It is different to next-word prediction, which is inherently directional, thus limiting context learning.

## Page 11
In NSP, the model receives pairs of sentences as input and learns to predict whether the second sentence in the pair is the subsequent sentence in the original document. To help the model distinguish between the two sentences in training, the CLS token is inserted at the beginning of the first sentence and a SEP token is inserted at the end of each sentence. In addition, a sentence embedding indicating Sentence A or Sentence B is added to each token. The model output corresponding to the CLS token is used for the prediction. As such, this output can be seen as a representation of the full input sentence. This property will be used in Section 6.1.

The fact that the pre-training of transformer models can be performed in an unsupervised fashion on a large text corpus is very important. It enables transfer learning, i.e. transferring the language-understanding skill acquired during pre-training to an applied task with a much smaller data volume. As will be shown in Section 7.1, the transformer model can be fine-tuned on the application-specific text corpus if required, at significantly reduced effort.

# 5. NLP Workflows 

Before moving to the applications, we describe in this section general approaches to augment tabular data for classification and regression problems with text data.
A. Use NLP techniques to extract additional features from text data (each with a specific meaning understandable by humans). Add these additional columns to the tabular data already available and apply a supervised learning technique to the augmented tabular data. This approach is illustrated in Figure 4.
B. Use NLP techniques to encode the text sequences into a finite set of additional columns, and proceed as in Approach A. The difference versus Approach A is that the meaning of the columns representing the text sequence is not defined by humans, but by the NLP encoder. This approach is illustrated in Figure 5.
C. The transformer models used in this paper are neural networks that encode a text sequence into a tensor. If the prediction model for the tabular data is also a neural network, the outputs of the last hidden layers of the two networks can be concatenated and the networks can be trained at the same time. This approach is illustrated in Figure 6. A variant of this approach would leave (parts of the) transformer encoder frozen during the training process.

In this paper, we will demonstrate Approach B in Section 6.2 and Approach C in Section 7.2. In both cases, we will not use additional tabular data. These examples can be seen as a demonstration of how to build the NLP classifier of Approach A.

Whilst all applications in this paper are classification tasks, regression tasks are handled in an analogous fashion.

## 6. Using Transformers to Extract Features for Supervised Learning Tasks

This section shows how transformer models can be used to extract features from text data to feed into regression or classification tasks. This demonstrates Approach B discussed Figure 5. Special emphasis is put on multilingual situations. In this section, the transformer model is used in its off-the-shelf format. Fine-tuning will be discussed in Section 7.

### 6.1. Basic Approach

The idea is simple: the transformer encoder is used to encode the text data into a numerical representation, which is then used as an input feature to a regression or classification model. This is an example of transfer learning: the NLP model learns language-understanding skills from a

## Page 12
Figure 4. NLP techniques are used to extract additional features, which are used to augment the available tabular features.

Figure 5. An NLP encoder used to encode the text data into additional features, which are used to augment the available tabular features.

Figure 6. The transformer encoder and the neural network to process the tabular data are connected and trained together. Parts of the transformer encoder could be frozen during the training process.
very large corpus of text data, using large-scale computing power. Both elements allow for a powerful (but relatively complex) model. This model can then be applied to situations where the availability of data or computing power would not allow for such complex models. Throughout this paper, we use the transformers library (Wolf et al., 2019), provided by HuggingFace.

In the following case study, we use the distilbert-base-multilingual-cased model, a multilingual BERT model, which was trained on the concatenation of Wikipedia in 104 different languages. DistilBERT, introduced by Sanh et al. (2019), is a simplification of a BERT model with fewer parameters and a faster execution time, but similar language-understanding
![Page 12 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p12_img1.jpg)
![Page 12 Image 2](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p12_img2.jpg)
![Page 12 Image 3](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p12_img3.jpg)

## Page 13
capabilities to BERT. "cased" in the name of the model refers to the fact that the model differentiates words by case. The sequence length of this model is limited to a maximum of $T=512$ tokens.

As explained in Section 4, the dimension of the transformer encoder output is $\mathbb{R}^{T \times E}$, where $T$ is the sequence length and $E$ is the output dimension of the last layer ( 768 for our model). We wish to represent the entire encoded sequence in one vector in $\mathbb{R}^{E}$, regardless of the sequence length. The following approaches are available and used in practice:
(a) Using the first element of the encoder output, corresponding to the CLS token. As explained in Section 4, the motivation behind this approach is that pre-training of BERT on next-sentence prediction tasks uses the encoder output corresponding to the CLS token as input to the prediction.
(b) Mean pooling, i.e. averaging over the encodings of all sequence items (except those items which are used to pad the sequence to a minimum length).

Note that the transformer encoder and its self-attention mechanism do have a sense of word ordering. As such, mean pooling on its output does not lose information on word ordering, in contrast to mean pooling applied directly on input embeddings, mentioned in Section 3.2.2.

In Case Study 1 we explore both approaches. We use a simple multinomial logistic regression classifier (see for instance section 4.4. of Hastie et al. (2008)) from the scikit-learn library (Pedregosa et al., 2011), with L2-regularisation to avoid overfitting.

# 6.2. Case Study 1: Use English Accident Reports to Predict the Number of Vehicles Involved 

In the case study presented in this section, we use accident reports from the dataset described in Appendix A. 1 to predict the number of vehicles involved. In contrast to Figure 5, we do not use any other (tabular) data for this task. The column NUMTOTV available in the dataset is used as labels to train a classifier in a supervised learning setting.

Figure A1 in Appendix A shows the distribution of the number of vehicles. Most cases involve two vehicles, and only very few cases involve more than three vehicles. No cases involve zero vehicles. We could formulate the prediction problem as regression problem, with a suitable distributional assumption. Because of the zero mass at 0 vehicles and a relatively low mass at high vehicle counts, the (zero-truncated) Poisson distribution does not appear to be a good representation of the data. Therefore, we formulate the prediction problem as multiclass classification. To avoid a heavily unbalanced classification problem we aggregate all cases of three or more vehicles into one group. The three resulting levels are denoted as 1,2 and $3+$.

We proceed as follows:

1. Train-test split: $80 \%$ of the records are used as the training set and the remainder as the test set.
2. Tokenise both sets using the standard tokeniser that ships with distilbert-base-multilingual-cased. This is a WordPiece tokeniser (see Section 3.1.1).
3. Apply the model to obtain the outputs of the final layer - the encoded sequence.
4. Condense the encoded sequence into a single vector using one of the approaches described in Section 5.
5. Use this vector as input feature for a multinomial logistic regression classifier with L2regularisation (GLM), and train the classifier to predict NUMTOTV.

Note that only step 5 is task-specific. For the first steps, we use the transformer model without any further training. Regularisation in step 5 is crucial to mitigate the risk of overfitting. In this

## Page 14
Table 1. Scores of the Different Approaches, Evaluated on the Test Set

|  Model | Log Loss | Brier Loss | Accuracy Score  |
| --- | --- | --- | --- |
|  Dummy classifier | 0.961 | 0.574 | $57.2 \%$  |
|  Logistic regression classifier, (a) using first element of encoded sequence | 0.275 | 0.146 | $90.9 \%$  |
|  Logistic regression classifier, (b) using mean pooling of encoded sequence | 0.127 | 0.063 | $96.0 \%$  |


Figure 7. Confusion matrices, evaluated on the test set. The dummy classifier always predicts the most frequent class. setting, we have 768 features (the fixed output dimension of the NLP model) and only between 5,000 and 6,000 training samples.

Table 1 and Figure 7 show the results, evaluated on the test set. As a baseline, we also show results for a dummy classifier, which always predicts the most frequent class. For a discussion and explanation of different scoring metrics see Fissler et al. (2022).

In this case, mean pooling outperforms the use of the encoding corresponding to the first token. For this reason, we use mean pooling subsequently.

To conclude, the quite impressive accuracy of $96 \%$ clearly demonstrates the power of transfer learning. We have used the language-understanding skills of the NLP model off-the-shelf, without any fine-tuning. We have only trained a simple classifier on its output.

# 6.3. Case Study 2: Cross-Lingual Transfer and Multilingual Training

In practice, text data might be present in different languages. This is usual in Switzerland, where the primary insurers deal with four official languages and English. As an example, claims descriptions exist in these five languages.

One option is to translate the data to a single language, for example using DeepL or any other machine translation software, as a pre-processing step before applying the NLP model. A possible drawback of this approach is that machine translation might not be available in the desired quality for the languages (or, domain-specific vocabulary) present in the data set.

An alternative approach, adopted here, is to use a multilingual NLP model, such as distilbert-base-multilingual-cased.

Our dataset provides the accident reports in both English and German, so we can assess performance if we train the classifier on the encoding of the German reports instead of the English reports. As Table 2 shows, similar scores are reached as with the English encodings.

The next question is whether we can train the classifier on the encoded texts in one language and apply it (with no further training) to the other language. Unfortunately, this transferability is not guaranteed, and the results in Table 2 and Figure 8 show poor performance. Given the positive results of the previous experiments, we suspect that this is not caused by the NLP encoder but by
![Page 14 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p14_img1.jpg)

## Page 15
Table 2. Scores in a Multilingual Setting, Using Distilbert-Base-Multilingual-Cased, Evaluated on the Test Set

| Classifier Trained On | Test Data | Log Loss | Brier Loss | Accuracy Score |
| :-- | :-- | :--: | :--: | :--: |
| English | English | 0.127 | 0.063 | $96.0 \%$ |
| English | German | 1.083 | 0.527 | $66.0 \%$ |
| German | English | 8.052 | 1.361 | $24.3 \%$ |
| German | German | 0.120 | 0.062 | $96.0 \%$ |
| 80\% English, 20\% German | English | 0.136 | 0.068 | $95.7 \%$ |
| 80\% English, 20\% German | German | 0.160 | 0.080 | $95.2 \%$ |

Logistic regression (b), train EN, test EN train GE, test EN
train EN/GE, test EN
train EN, test GE
train GE, test GE
train EN/GE, test GE
train EN/GE, test GE
train EN/GE, test GE

Figure 8. Confusion matrices in a multilingual setting, using distilbert-base-multilingual-cased, evaluated on the test set.
the classifier, which might predominantly use features of the encoded sequence that are specific to the training language.

A possible solution is to train the classifier with a training set consisting of encoded samples from both languages. In practice, this could be achieved by translating a fraction of the data and then training the model on encodings of the mixed-language data. To simulate a situation where one language is underrepresented (as might be the case in Switzerland), we create a mixed-language dataset with $80 \%$ English and $20 \%$ German samples and train the classifier on the encoded output. This improves all scores and brings them much closer to the monolingual case.

To conclude, a multilingual situation can be handled by a multilingual transformer model. For the best performance, the classifier should be trained on the encoded sequences from all languages.
![Page 15 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p15_img1.jpg)
![Page 15 Image 2](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p15_img2.jpg)
![Page 15 Image 3](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p15_img3.jpg)
![Page 15 Image 4](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p15_img4.jpg)

## Page 16
# 7. Improving the Model 

In the case studies of the previous section the NLP model was used without any adaptation to the text data at hand. For the task at hand, the results are already very good. However, in certain situations it might be required to further improve model performance.

In this section we explore two approaches to how to fine-tune a transformer model:

- Domain-specific fine-tuning involves updating the parameters of the transformer model using text data that is relevant to the domain where the model will be applied. However, the model is not necessarily tuned for a specific downstream task of interest.
- Task-specific fine-tuning uses domain-specific text data and tunes the parameters of the transformer model while training it for a given downstream task of interest.

One advantage of the first approach is that it can be performed in an unsupervised fashion, i.e. it does not require labelled data. Also, the fine-tuned model can be used on different downstream tasks in the same domain. On the other hand, task-specific fine-tuning is expected to produce better performance on the particular task the model was tuned to, so it might be the method of choice if there is a single downstream task and if sufficient labelled data is available. These two fine-tuning approaches are explored in turn.

### 7.1. Domain-Specific Fine-Tuning

Domain-specific fine-tuning can be achieved by applying the model to a "masked language modelling" task. This involves taking a sentence, randomly masking a certain percentage of the words in the input, and then running the entire masked sentence through the model, which has to predict the masked words. This self-supervised approach is an automated process to generate inputs and labels from the texts and does not require any human labelling. Figure 9 illustrates this approach.

Figure 9. Domain-specific pre-training by masked language modelling.
Fortunately, this process does not require much coding, as can be seen in the accompanying notebook. However, it requires significant computing resources, in particular for longer text sequences, albeit much less than training a model of comparable quality from scratch.

We apply two epochs of fine-tuning (i.e. we run the masked language modelling process twice through the mixed-language training set) and repeat the experiments of Section 6.3. The results are shown in Table 3 and Figure 10, evaluated on the test set.

In conclusion, by comparing to Table 2, we observe that the domain-specific fine-tuning on the mixed-language training set has improved the scores, but not to a satisfactory level for the crosslanguage transfer cases. Note that since the fine-tuning was not in any way specific to the task of predicting the number of vehicles, the fine-tuned NLP model can be applied to other tasks based on this dataset (or another dataset in the same domain). We perform this in Section 8.1.

### 7.2. Task-Specific Fine-Tuning

An alternative to domain-specific fine-tuning is task-specific fine-tuning.
![Page 16 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p16_img1.jpg)

## Page 17
|  Classifier Trained On | Test Data | Log Loss | Brier Loss | Accuracy Score  |
| --- | --- | --- | --- | --- |
|  English | English | 0.093 | 0.044 | 97.1%  |
|  English | German | 0.352 | 0.207 | 85.4%  |
|  German | English | 2.028 | 0.631 | 65.3%  |
|  German | German | 0.107 | 0.053 | 96.3%  |
|  80% English, 20% German | English | 0.098 | 0.047 | 97.1%  |
|  80% English, 20% German | German | 0.134 | 0.063 | 96.2%  |

**Table 3.** Scores, Evaluated on the Test Set, in a Multilingual Setting, Using `Distilbert-Base-Multilingual-Cased` with 2 Epochs of Masked Language Modelling on the Mixed-Language Training Set


**Figure 10.** Confusion matrices, evaluated on the test set, in a multilingual setting with 2 epochs of masked language modelling on the mixed-language training set.

The idea is to train a transformer model directly on the task at hand, in our case a sequence classification task. This means that we don't use the encoder outputs directly, but we add a classification layer to the NLP model, so that the resulting model is a neural network classifier.

This is an example of Approach C discussed in Section 5 (illustrated in Figure 6), but with no additional tabular data. Fortunately, this process does not require more coding than domain-specific pre-training, as can be seen in the accompanying notebook. However, it requires significant computing resources.

We apply 2 epochs of task-specific pre-training on the original `distilbert-base-multilingual-cased` model using the English training set. The results are shown in Table 4.

We did not repeat all the experiments, as the results indicate that 2 epochs of task-specific pre-training on the English training set improved all scores significantly, both on the English test set and the German test set (despite the model being trained on English data only).
![Page 17 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p17_img1.jpg)

## Page 18
Table 4. Scores, Evaluated on the Test Set, in a Multilingual Setting, using Distilbert-Base-Multilingual-Cased Without Fine-Tuning, with 2 Epochs of Task-Specific Pre-Training

| Classifier Trained On | Test Data | Log Loss | Brier Loss | Accuracy Score |
| :-- | :-- | :--: | :--: | :--: |
| English | English | 0.028 | 0.009 | $99.6 \%$ |
| English | German | 0.072 | 0.030 | $98.3 \%$ |

For this case, cross-lingual transfer seems to work well. Looking at the sample in Figure A3 in Appendix A, this might be due to the fact that the German translation of vehicle designations is quite close to English. For example, "V1" and "V2" are the same in both languages. In general, we would advise performing the task-specific fine-tuning on a multilingual training set.

# 7.3. Further Improvements 

One challenge that might appear in practical applications is that the length of the texts exceeds the maximum length of input sequences allowed by the model. For instance, the model used in the previous case study can handle at most 512 tokens. Only the first 512 tokens are processed, and the remainder are discarded. If the relevant part of the input is discarded this will lead to false predictions. To address this issue we need a way to process longer input sequences. Several approaches are available:
(a) Applying the limited-length model to chunks of the text sequences.
(b) Using a model which can handle more than 512 tokens. Transformer-based models are inefficient at processing long sequences due to their self-attention operation, which scales quadratically with the sequence length. To address this limitation, Beltagy et al. (2020) introduced the so-called Longformer, with an attention mechanism that scales linearly with sequence length, making it easy to process documents of thousands of tokens or longer.
(c) Using methods to extract the part of the input sequence that is relevant to the task. An example is provided in Section 9.1.

In more general terms, the performance could be further improved by:

- applying hyperparameter tuning on the training parameters (such as the learning rate).
- using alternative transformer models (such as XLM or XLM-RoBERTa in the multilingual case).
- using ensemble models (i.e. using the outputs of different NLP models and/or classifiers) to arrive at the final prediction.

Finally, dimensionality reduction techniques could be used to reduce the length of the encodings. In this case, UMAP (Uniform Manifold Approximation and Projection for Dimension Reduction, (McInnes \& Healy, 2018) is currently the method of choice, as it preserves both the local and global structure of embeddings quite well. Section 9.4 presents an application of UMAP.

## 8. Interpretability and Error Analysis

As seen in Section 7, predicting the number of vehicles from the case descriptions is a relatively easy task for the transformer model, even in a multilingual situation. Therefore, we turn to a more challenging problem, presented in Case Study 3.

## Page 19
Table 5. Scores of the Different Approaches, Evaluated on the Test Set

|  Model | Log Loss | Brier Loss | Accuracy Score  |
| --- | --- | --- | --- |
|  Dummy classifier | 0.679 | 0.486 | $58.7 \%$  |
|  Logistic regression classifier on mean-pooled output of DistilBERT | 0.400 | 0.259 | $80.1 \%$  |
|  Logistic regression classifier on mean-pooled output of pre-trained model | 0.362 | 0.228 | $83.4 \%$  |
|  Task-specific fine-tuning of DistilBERT classifier | 0.279 | 0.155 | $90.4 \%$  |


Figure 11. Confusion matrices evaluated on the test set. The result from task-specific fine-tuning is shown in Figure 12.

# 8.1. Case Study 3: Use English Accident Reports to Identify Bodily Injury

In this case study, we use accident reports from the dataset described in Appendix A (Section A.1) to identify cases which lead to bodily injuries. The original dataset contains a tabular feature (INJSEVA) which indicates the most serious sustained injury in the accident. One could hope to use this as the label to train a text classification model. However, this information, taken from police accident reports and supplementary to the case description, does not necessarily align well with the case description, as shown in Table A2 in Appendix A. Therefore, we use a binary bodily injury indicator (INJSEVB) as target label.

We fit the following models:

1. Dummy classifier, which always predicts the most frequent class.
2. Using the approach described in Section 6.2, we fit a logistic regression classifier to the mean-pooled outputs of a distilbert-base-multilingual-cased encoder.
3. We repeat the same, with domain-specific fine-tuning as described in Section 7.1.
4. We perform task-specific fine-tuning, as described in Section 7.2.

Table 5 and Figure 11 show the results. The relative performance of the approaches aligns with the experience from the previous case studies, with task-specific fine-tuning leading to the best results. From the confusion matrix of the neural network classifier used for task-specific fine-tuning, we observe that the false negative rate (i.e. false negatives to positives, or 1 - recall) is rather high. The question arises as to how this could be improved. To answer this, we need to understand the source of the errors. This is addressed in Section 8.2.

### 8.2. Error Analysis

The first step of the error analysis is to inspect the samples producing false negative and false positive predictions. Reading every single text would be very tedious, therefore it is worthwhile
![Page 19 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p19_img1.jpg)

## Page 20
Table 6. Scores of the Different Approaches, Evaluated on the Test Set. Since We Have not Implemented a Logic to Combine the Predicted Probabilities of the Different Chunks, the Log Loss and Brier Loss Cannot be Evaluated in This Case

| Model | Log Loss | Brier Loss | Accuracy Score |
| :-- | :--: | :--: | :--: |
| Task-specific fine-tuning of DistilBERT classifier | 0.279 | 0.155 | $90.4 \%$ |
| Task-specific fine-tuning; splitting the input sequences into chunks | $\mathrm{n} / \mathrm{a}$ | $\mathrm{n} / \mathrm{a}$ | $92.8 \%$ |

DistilBERT classifier - 2 epochs task-specific DistilBERT classifier - split inputs

Figure 12. Confusion matrices, evaluated on the test set.
focusing on those examples where the probability assigned to the false prediction was high, i.e. cases where the model was confident but wrong.

First, we look at the text lengths. For the false negative predictions, we observe that the average length of the texts exceeds 500 words. We are using a model with word-piece tokenisation, so the tokenised input sequence will be even longer on average. The transformer encoder is limited to a sequence length of maximum 512 tokens. Only the first 512 tokens will be processed, and the remainder are discarded. If only the discarded part of the text indicates the presence of a bodily injury, this will give rise to a false negative classification.

To address this issue, we adopt approach (a) described in Section 7.3, as follows:

1. For the training phase, we continue using the truncated input sequences.
2. For the predictions on the test set, we split each input sequence into slightly overlapping chunks of length 512, run the prediction on each chunk, and combine the predictions by logical OR.

Fortunately, the coding effort is quite small. The results are shown in Table 6 and Figure 12.
Indeed, splitting the input sequences has significantly reduced the number of false negatives. In turn, the number of false positives has increased slightly, due to false positives from previously discarded parts of the input texts. To gain a better understanding of the false positives and false negatives, we would like to know why the model has arrived at a certain prediction. The next paragraph presents one way to achieve this.

# 8.3. Interpretability 

Transformer models are quite complex, and therefore interpreting model output can be difficult. In this paper we briefly introduce the library Captum from Kokhlikyan et al. (2020)
![Page 20 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p20_img1.jpg)

## Page 21
("comprehension" in Latin). This is an open source, extensible library for model interpretability built on PyTorch. It provides different interpretability methods, grouped into:

- Primary Attribution: evaluates contribution of each input feature to the output of a model.
- Layer Attribution: evaluates contribution of each neuron in a given layer to the output of the model.
- Neuron Attribution: evaluates contribution of each input feature on the activation of a particular hidden neuron.

Here, as we primarily wish to understand which part of the text leads to a particular classification, we are going to use one of the primary attribution methods provided by Captum, namely integrated gradients. The method of integrated gradients was introduced by Sundararajan et al. (2017). It represents the integral of gradients with respect to inputs along the path from a given baseline to input. Formally, it can be described as follows:

$$
I G_{i}(x):=\left(x_{i}-x_{i}^{\prime}\right) \cdot \int_{0}^{1} \frac{\partial F\left(x^{\prime}+\alpha \cdot\left(x-x^{\prime}\right)\right)}{\partial x_{i}} d \alpha
$$

where $F$ denotes the prediction function, $x$ the input vector of the example under consideration, $x^{\prime}$ some baseline input vector, and the subscript $i$ denotes dimension $i$ of the respective vector. The integral can be approximated numerically. The baseline vector is a vector consisting only of padding tokens. We use the library transformers-interpret from Pierse (2023) which provides a convenient interface to Captum, requiring only minimal coding (a few lines).

Figures A4, A5 and A6 in Section A. 1 in Appendix A show examples of word importance visualisations based on integrated gradients. We systematically evaluated these visualisations for all false positive and false negative cases to also check that the target labels are correct. Based on such visualisations, it is possible to determine which parts of the input sequence are most important for the model to arrive at a particular prediction. This helps with finding issues with the text data (e.g. ambiguous statements), erroneous labels, or shortcomings of the model.

# 9. Using Transformers for Unsupervised Applications 

The previous sections have described supervised learning approaches. This relies on the availability of sufficient labelled data. However, this is not always provided in practice. Transformer-based NLP models are also useful in unsupervised settings. We introduce three unsupervised applications: extractive question answering, zero-shot classification and topic clustering.

### 9.1. Case Study 4: Extractive Question Answering

As the name implies, the goal of extractive question answering is to extract an answer to a question from a given text. The term "extractive" means that the answer is an extract of the text, as opposed to a generated new text.

For extractive question answering, the transformer model is presented with two text sequences: the so-called context (from which the answer should be extracted), and the question. The model tries to predict the most likely start and end positions of the candidate answer(s) within the context, or the question might be unanswerable.

The question answering is able to handle long input sequences because it automatically splits long input sequences into chunks. Therefore, this approach is a way to extract the part of the input sequence relevant to the task, at the risk of losing some information. Any NLP model of choice can be applied to further process the extracted texts. Figure 13 illustrates the approach.

## Page 22
Figure 13. Using extractive question answering to extract shorter text sequences from the raw text.

Extractive question answering can be applied without task-specific pre-training, in a fully unsupervised fashion, thus transferring the language-understanding skills from a model that was pre-trained on a large corpus of text data. Here, we use the deutsche-telekom/bert-multi-english-german-squad2 model provided by HuggingFace. The starting point to train this model was "The Stanford Question Answering Dataset" (SQUAD2.0, Rajpurkar, 2023) consisting of 100 k answerable and 50 k unanswerable questions. These questions and answers were auto-translated into German, proofread and corrected. The bert-base-multilingualcased model was fine-tuned on this question answering task.

In the following application example, we continue the case study of Section 8.1: we apply extractive question answering to the accident reports to identify cases with bodily injury. We visit each accident report in turn (the context) and ask the model the two questions "Was someone injured?" and "Was someone transported?" Since the accident report might provide information on multiple persons, we allow a maximum of four candidate answers for each question, which we concatenate into a single (much shorter) new text. For instance, the example shown in Figure A5 produces the concatenated answers shown in Figure 14:

She was not injured. She was not injured. She was not injured in the crash. He slammed on his brakes. her Jeep was driven from the scene. he drove off the right side of $t$ he roadway. She was transported to the hospital. the unknown vehicle passed him on the left side.

Figure 14. Extracted answers to the questions "Was someone injured?" and "Was someone transported?" from the example shown in Figure A5 (SCASEID $=2007043731967$ ). The first four sentences are the candidate answers to the first question. The last four sentences are the candidate answers to the second question. The person who was not injured is the driver of V1; the person transported to hospital is the driver of V2.

To assess the quality of the extracted texts, we use the approach described in Section 7.2 to train a distilbert-base-multilingual-cased model for the classification task. Since the text extracts are much shorter than the original texts, this training process is significantly faster. Table 7 show the results, in comparison to those shown in Tables 5 and 6.

Table 7. Scores Obtained of the Different Approaches, Evaluated on the Test Set

|  Model | Log Loss | Brier Loss | Accuracy Score  |
| --- | --- | --- | --- |
|  Dummy classifier | 0.679 | 0.486 | $58.7 \%$  |
|  Logistic regression classifier on mean-pooled output of DistilBERT | 0.400 | 0.259 | $80.1 \%$  |
|  Logistic regression classifier on mean-pooled output of pre-trained model | 0.362 | 0.228 | $83.4 \%$  |
|  Task-specific fine-tuning; inputs sequences truncated to 512 tokens | 0.279 | 0.155 | $90.4 \%$  |
|  Task-specific fine-tuning; splitting the input sequences into chunks | $\mathrm{n} / \mathrm{a}$ | $\mathrm{n} / \mathrm{a}$ | $92.8 \%$  |
|  Task-specific fine-tuning; based on extractive question answering | 0.420 | 0.241 | $84.7 \%$  |
![Page 22 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p22_img1.jpg)

## Page 23
**Figure 15.** Confusion matrices corresponding to the second last items of Table 7.

From Figure 15 we see that there is a larger number of false negatives than obtained by task-specific training and evaluation on the full-length sequence. This indicates that in some cases the extractive question answering has missed out or suppressed certain relevant parts. For instance, if the original text reads "The driver was injured," the extract "The driver" is a correct answer to the question "Was someone injured?"; however, it is too short to detect the presence of an injury from the extract.

### 9.2. Case Study 5: Zero-Shot Classification

There are situations with no or only few labelled data. For a hands-on guide we refer to Chapter 9 of Tunstall et al. (2022). Here, we briefly demonstrate an approach that is suited for such situations.

Zero-shot classification involves classifying text sequences in an unsupervised way (without having training data in advance and building a model), as studied by Yin et al. (2019). The model is presented with a text sequence and a list of expressions and assigns a probability to each expression. Figure 16 illustrates the approach.


**Figure 16.** Using zero-shot classification to assign probabilities to pre-defined expressions.

We demonstrate the approach using the LGPIF dataset described in Appendix A (Section A.2). This dataset relates to property insurance claims and consists of 6,030 records (4,991 in the training set, 1,039 in the test set). For each record, there is a short claims description in English, and a categorical variable encoding the hazard type, with nine different levels: Fire, Lightning, Hail, Wind, WaterW (weather-related water claims), WaterNW (other weather claims), Vehicle, Vandalism and Misc (any other). Table 8 defines the expressions and mapping to hazard types.

We use the facebook/bart-large-mnli model for zero-shot classification. The claim descriptions are the only input feature for zero-shot classification. We apply zero-shot classification directly on the test set, because no task-specific training is required. The resulting confusion matrix is shown in the left part of Figure 17, and the scores are shown in Table 9.

The classifier struggles to correctly identify the "WaterW" cases based on the expression "Weather." Also, it seems that the expression "Misc" may not be the optimal choice, as it produces many false positives. To address this, we introduce the following heuristic: if the probability
![Page 23 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p23_img1.jpg)
![Page 23 Image 2](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p23_img2.jpg)

## Page 24
Table 8. Expressions and Mapping to Hazard Types. Note that we Have Mapped Two Different Expressions for the Hazard Type "Vandalism"

| Expression |  | Hazard Type |
| :-- | :-- | :-- |
| Vandalism | 0 | Vandalism |
| Theft | 0 | Vandalism |
| Fire | 1 | Fire |
| Lightning | 2 | Lightning |
| Wind | 3 | Wind |
| Hail | 4 | Hail |
| Vehicle | 5 | Vehicle |
| Water | 6 | WaterNW |
| Weather | 7 | WaterW |
| Misc | 8 | Misc |

Table 9. Scores of the Different Approaches, Evaluated on the Test Set. For the Zero-Shot Model with Adjusted Threshold, Predicted Probabilities are Not Available; Therefore, the Log Loss and Brier Loss are Not Shown. The Sentence Similarity Approach will be Discussed in the Next Section

| Model | Log Loss | Brier Loss | Accuracy Score |
| :-- | :--: | :--: | :--: |
| Dummy classifier | 1.977 | 0.835 | $29.8 \%$ |
| Zero-shot classification | 1.043 | 0.463 | $65.5 \%$ |
| Zero-shot classification, with adjusted threshold for Misc | $\mathrm{n} / \mathrm{a}$ | $\mathrm{n} / \mathrm{a}$ | $69.7 \%$ |
| Sentence similarity | $\mathrm{n} / \mathrm{a}$ | $\mathrm{n} / \mathrm{a}$ | $74.5 \%$ |
| Sentence similarity, refined | 1.172 | 0.403 | $76.6 \%$ |
| Logistic regression classifier on mean-pooled output of DistilBERT | 0.531 | 0.243 | $83.9 \%$ |
| Task-specific fine-tuning of DistilBERT classifier | 0.554 | 0.233 | $84.7 \%$ |

Zero-shot-classification

|  | Vandalism |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Zero-shot classification, refined |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Page 25
Logistic Regression classifier

Transformer-based classifier

Figure 18. Confusion matrices, evaluated on the test set.
assigned to the expression "Misc" is highest but with a margin of less than 50 percentage points to the second-most likely expression, we select the latter. This increases the accuracy score from $65.5 \%$ to $69.7 \%$ and produces the confusion matrix shown in the right part of Figure 17. Compared to the $29.8 \%$ accuracy score of the dummy classifier, and considering that we have performed no training specific to the data set, this result is quite remarkable.

Looking at false predictions in the training set, we observe the following:
(a) True label "Vandalism," predicted label "Vehicle" or "Misc": quite a few descriptions contain the word "glass." For these claims, "Vandalism" appears to be a natural classification.
(b) True label "Vehicle," predicted label "Vandalism": this group contains many descriptions like "light pole damaged" or "fence damaged." Apparently, the zero-shot classifier does not realise that, for these items, damage caused by a vehicle is more likely than damage caused by vandalism.
(c) True label "WaterW," predicted label "WaterNW": some of the descriptions like "frozen pipe caused water damage to indoor pool," "gutter pulled from roof ice dam," "water damage and mould growth from storms" suggest that the candidate word "Weather" is not optimal to attract all weather-related water claims.

Based on these and similar observations, one could refine the approach by adding more candidate expressions, e.g. adding "glass" to hazard type 0 ("Vandalism"), "light pole" and "fence" to hazard type 5 ("Vehicle"), "storm" and "ice" to hazard type 7 ("WaterW"), etc. However, we refrain from doing so because the computational effort scales with the number of samples times the number of candidate expressions. We will look at an alternative approach in Section 9.3.

If the true labels are available (which is the case here), the supervised NLP methods described can learn these associations automatically. To check this, we apply the methods described in Sections 6.1 and 7.2, using the distilbert-base-uncased model. The results are shown in Figure 18 and Table 9.
![Page 25 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p25_img1.jpg)
![Page 25 Image 2](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p25_img2.jpg)

## Page 26
Table 10. Expressions and Mapping to Hazard Types

| Expression |  | Hazard Type |
| :-- | :-- | :-- |
| "Vandalism" | 0 | Vandalism |
| "Glass" | 0 | Vandalism |
| "Theft" | 0 | Vandalism |
| "Fire damage" | 1 | Fire |
| "Lightning damage" | 2 | Lightning |
| "Wind damage" | 3 | Wind |
| "Hail damage" | 4 | Hail |
| "Damage caused by a vehicle" | 5 | Vehicle |
| "Water damage" | 6 | WaterNW |
| "Weather damage" | 7 | WaterW |
| "Ice" | 7 | WaterW |
| "Electricity" | 8 | Misc |
| "Power surge" | 8 | Misc |

As per usual in machine learning, it is important to evaluate the performance on test data, which has not been used in the training process. For this reason, our results are not comparable to those reported in Wüthrich \& Merz (2023), because these were obtained by using the full data set for both training and evaluation. The importance of this can be demonstrated by a simple example. For instance, the training might have a claim description "water damage to library," classified as "WaterNW." Then, the NLP classifier might learn that the association of the expressions "water" and "library" is indicative of "WaterNW" claims. However, this association has no predictive power, because water damage to a library could also be caused by a weatherrelated event, which needs to be classified as "WaterW."

# 9.3. Case Study 6: Sentence Similarity 

In the previous section, we have seen that the computational effort of zero-shot classification scales with the number of samples times the number of candidate expressions, as the transformer model is applied to each pair. In this section, we explain an alternative approach with a computational effort proportional to the number of samples plus the number of candidate expressions. This encourages experimenting with various candidate expressions.

The idea is to encode each sample and each candidate expression separately into an embedding vector. Then, for each pair, similarity is determined by the cosine similarity score, which is the dot product of the respective embedding vectors, each normalised to unit length. For each sample, the expression with the highest similarity score is selected. Figure 19 illustrates the approach.

We apply this approach to the test set of the LGPIF data described in Appendix A (Section A.2), we have already used. We define the following expressions and mapping to hazard types in Table 10:

As you can see, we have applied some of the lessons learned from the previous experiments with the zero-shot classifier.

We use the model sentence-transformers/all-MiniLM-L12-v2, which is a BERT model that produces a sequence of real-valued vectors of length 384 . During pre-training on

## Page 27
Figure 19. Using sentence similarity to perform unsupervised classification.


Figure 20. Confusion matrices, evaluated on the test set.
sentence similarity tasks, mean pooling is applied to encode each the sequence into a single vector. For details, we refer to Reimers \& Gurevych (2019).

We apply the approach directly to the test set, because no task-specific training is required. The resulting confusion matrix is shown in the left part of Figure 20, and the scores are shown in Table 9.

As a refinement, we train a sentence classifier (as in Section 7.2) on the training set, using the labels obtained by the sentence similarity approach. Although this is a supervised learning step, we are not using the original labels, therefore the overall approach is still unsupervised. The resulting confusion matrix, evaluated on the test set, is shown in the right part of Figure 20.

Compared to the zero-shot classifier, the confusion between "Vandalism" and "Vehicle" has significantly reduced, and the scores have improved. This comparison is not entirely fair, because we have not used the same candidate expressions in both cases. The model still struggles to distinguish weather-related from non-weather-related water claims, and to identify the hazard type Misc; both difficulties are inherent in the data.

# 9.4. Case Study 7: Topic Clustering 

In the previous sections we have seen that no prior training of the language model is required to produce a classification of reasonable quality. However, providing suitable candidate expressions is non-trivial. Ideally, we would wish for a method to extract these directly from the data.
![Page 27 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p27_img1.jpg)
![Page 27 Image 2](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p27_img2.jpg)

## Page 28
Figure 21. Using topic clustering to generate document labels in an unsupervised setting.

This section describes an approach to unsupervised labelling. The idea is to encode the text samples, create clusters of "similar" documents and extract meaningful verbal representations of the clusters. Figure 21 illustrates the approach.

Several packages are available to perform this task, e.g. BERTopic, Top2Vec (Angelov, 2020) and chat-intents (Borelli, 2023). These packages use similar concepts but provide different APIs, hyper-parameters, diagnostics tools, etc. Here, we use BERTopic (Grootendorst, 2022).

The algorithm consists of the following steps:

1. Embed documents:
a. Encode each text sample (document) into a vector - the embedding. This can be based on a BERT model or any other document embedding technique. By default, BERTopic uses all-MiniLM-L6-v2, which is trained in English. In the multilingual case it uses paraphrase-multilingual-MiniLM-L12-v2.
2. Cluster documents:
a. Reduce the dimensionality of the embeddings. This is required because the document embeddings are high-dimensional, and, typically, clustering algorithms have difficulty clustering data in high-dimensional space. By default, BERTopic uses UMAP (Uniform Manifold Approximation and Projection for Dimension Reduction, (McInnes \& Healy, 2018) as it preserves both the local and global structure of embeddings quite well.
b. Create clusters of semantically similar documents. By default, BERTopic uses HDBSCAN (McInnes et al., 2017) as it allows to identify outliers.
3. Create topic representation:
a. Extract and reduce topics with c-TF-IDF. This is a modification of TF-IDF (explained in Section 3.1.2), which applies TF-IDF to the concatenation of all documents within each document cluster, to obtain importance scores for the words within the cluster.
b. Improve coherence and diversity of words with Maximal Marginal Relevance, to find the most coherent words without having too much overlap between the words themselves. This results in the removal of words that do not contribute to a topic.

We apply this algorithm to the training set the LGPIF data described in Appendix A.2, which we already used in the previous section. The claim descriptions are the only input feature, the labels are not used. Unfortunately, reproducibility across runs is not guaranteed; therefore, we obtain different results each time.

This produces roughly 50 clusters. For each cluster, we know the samples allocated to the cluster, and we have the topic representation, as illustrated in the Figure 22.

Based on the word scores, it is straightforward to map the topics to the labels. This is typically a manual step, but performing this mapping on circa 50 topics is much less burdensome than manually mapping thousands of samples.

In our case, we have the true labels available. We use this information to produce the mapping automatically: we map each topic cluster to the most frequent label in that cluster. A similar approach can also be used if only few labels are available. Figure 23 shows the relative label frequency distribution by topic.
![Page 28 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p28_img1.jpg)

## Page 29
**Figure 22.** Topic word scores for the first four identified topics. The topics appear in descending order of number of allocated samples. The first and third topic are mapped to "Vandalism," Topic 1 is mapped to "Fire" and Topic 3 to "Wind".


**Figure 23.** The matrix shows one column per topic. The shading indicates the frequency distribution of labels within a given topic. The presence of a single dark patch indicates that almost all of the samples of the topic are associated with a single label.

We observe that for most topics, one label is dominant, with the following exceptions:

- The classes 6 ("WaterNW") and 7 ("WaterW") are difficult to tell apart from the clusters. This finding aligns with the observations made in the previous section. All topics affected by this issue will be mapped to the more frequent class "WaterW." This results in no topic being mapped to "WaterNW."
- The first topic (-1) contains all samples which were not allocated to any of the clusters. These outliers cannot be clearly allocated to one specific label, but they will be mapped to the most frequent class 2 ("Vandalism"). This affects roughly 14% of the samples.

For all the other topics, the automatic mapping based on the true label matches the manually produced mapping.

Next, we apply the clustering and mapping to the test set. By comparing to the true labels, we obtain an accuracy score of ca. 70%. By looking at the confusion matrix in the left part of Figure 24, we observe that the class 2 ("Lightning") has many false positives. This is caused by the mapping applied to the outliers. To mitigate this issue, we train a transformer encoder classifier on the training set using the labels obtained from the unsupervised topic modeling but excluding the outliers. This improves the accuracy score to ca. 80%. To conclude, unsupervised topic modeling provides an easy approach in the absence of sufficient labelled text data.

### 10. Conclusions

In this paper we have provided an overview of common approaches to NLP, with a focus on transformer-based models. We have shown typical workflows to incorporate text data into classification and regression tasks, which often arise in an actuarial context.
![Page 29 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p29_img1.jpg)
![Page 29 Image 2](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p29_img2.jpg)

## Page 30
Figure 24. Confusion matrices, comparing labels obtained from topic clustering with the true labels, evaluated on the test set.

In one of these workflows, the NLP model is used to encode the text into real-valued vectors which are then used as (additional) input features of a classifier or regressor, with no training of the NLP model whatsoever. This is an example of transfer learning: the language-understanding skill of the NLP model, learned from a very large volume of text data, is transferred to an application with only limited text data available. This approach was demonstrated by predicting the number of involved vehicles and the presence of bodily injury from a real dataset of car accident reports, available in English and German. Our case study found that in a multilingual setting, training samples should represent all languages, albeit a heavy under-representation of one language did not lead to issues.

In our case studies, model performance was improved by domain-specific pre-training, which is a process to refine the NLP model using the available text data in an unsupervised way. We further significantly improved the model by task-specific fine-tuning and by adjusting the model to handle long input texts for prediction.

We have demonstrated how the integrated gradients method helps in identifying those parts of the input text that led to a particular classification; and in finding issues with the text data, erroneous labels, or shortcomings of the model.

Finally, we have demonstrated unsupervised techniques. Extractive question answering was used to shorten long input sequences by filtering the relevant parts. Zero-shot classification, sentence similarity and topic clustering were applied for a classification task in a situation with no labels available.

Overall, the results obtained in the case studies clearly demonstrate that transformer models provide a powerful tool to make text features usable for actuarial applications, with only minimal pre-processing and fine-tuning.

The results presented in this paper were obtained from an implementation in Python, available as a Jupyter notebook from Swiss Association of Actuaries (2023).

Acknowledgements. The authors are very grateful to Mario Wüthrich, Christian Lorentzen and Michael Mayer for their comprehensive reviews and their innumerable inputs which led to substantial improvements of this work.
![Page 30 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p30_img1.jpg)

## Page 31
# References 

Alammar, J. (2018). The illustrated transformer. GitHub, available at https://jalammar.github.io/illustrated-transformer/
Angelov, D. (2020). Top2Vec: distributed representations of topics. arXiv:2008.09470.
Ba, J. L., Kiros, J. R., \& Hinton, G. E. (2016). Layer normalization. arXiv:1607.06450v1.
Baeza-Yates, R., \& Ribeiro-Neto, B. (2011). Modern Information Retrieval. Addison Wesley, 68-74.
Bahdanau, D., Cho, K., \& Bengio, Y. (2014). Neural machine translation by jointly learning to align and translate. arXiv:1409.0473v7.
Beltagy, I., Peters, M. E., \& Cohan, A. (2020). Longformer: the long-document transformer. arXiv:2004.05150v2.
Bengio, Y., Simard, P., \& Frasconi, P. (1994). Learning long-term dependencies with gradient descent is difficult. IEEE Transactions on Neural Networks, 5(2), 157-166.
Bengio Y., Ducharme R., Vincent P., \& Jauvin C. (2003). A neural probabilistic language model. Journal of Machine Learning Research, 3(Feb), 1137-1155.
Bird, S., Klein, E., \& Loper, E. (2009). Natural Language Processing with Python: Analyzing Text with the Natural Language Toolkit. O'Reilly Media, Inc.
Borelli, D. (2023). Clustering sentence embeddings to extract message intent. GitHub, available at https://github.com/ dborrelli/chat-intents
Cho, K., van Merriënboer, B., Gulcehre, C., Bahdanau, D., Bougares, F., Schwenk, H., \& Bengio, Y. (2014). Learning phrase representations using RNN encoder-decoder for statistical machine translation. arXiv:1406.1078v3.
Devlin, J., Chang, M.-W., Lee, K., \& Toutanova, K. (2019). BERT: pre-training of deep bidirectional transformers for language understanding. arXiv:1810.04805v2.
Ferrario, A., \& Nägelin, M. (2020). The art of natural language processing: classical, modern and contemporary approaches to text document classification. SSRN ID 3547887. Version March 1, 2020.
Fissler, T., Lorentzen, C., \& Mayer, M. (2022). Model comparison and calibration assessment: user guide for consistent scoring functions in machine learning and actuarial practice. arXiv:2202.12780v2.
Frees, E.W. (2020). Loss data analytics. An open text authored by the Actuarial Community. GitHub, available at https:// openacttexts.github.io/
Grootendorst, M. (2022). BERTopic: neural topic modeling with a class-based TF-IDF procedure. arXiv:2203.05794v1.
Hastie, T., Tibshirani, R., \& Friedman, J. (2008). The Elements of Statistical Learning (2 ${ }^{\text {nd }}$ ed.). Springer.
He, K., Zhang, X., Ren, S., \& Sun, J. (2016). Deep residual learning for image recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 770-778.
Hochreiter, S., \& Schmidhuber, J. (1997). Long short-term memory. Neural Computation, 9(8), 1735-1780.
Honnibal, M., \& Montani, I. (2017). spaCy 2: Natural language understanding with Bloom embeddings, convolutional neural networks and incremental parsing, available at https://spacy.io/
Kokhlikyan, N., Miglani, V., Martin, M., Wang, E., Alsallakh, B., Reynolds, J., Melnikov, A., Kliushkina, N., Araya, C., Yan, S., \& Reblitz-Richardson, O. (2020). Captum: A unified and generic model interpretability library for PyTorch. arXiv:2009.07896.
McInnes, L., Healy, J., \& Astels, S. (2017). Hdbscan: hierarchical density based clustering. Journal of Open Source Software, 2(11), 205.
McInnes, L., Healy, J. (2018). UMAP: uniform manifold approximation and projection for dimension reduction, arXiv:1802.03426v3.
Mikolov, T., Chen, K., Corrado, G., Dean, J. (2013a). Efficient estimation of word representations in vector space. arXiv:1301.3781v3.
Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., \& Dean, J. (2013b). Distributed representations of words and phrases and their compositionality. Advances in Neural Information Processing Systems 26, 3111-3119.
Manning C. D., Raghavan, P., \& Schütze, H. (2008). Introduction to Information Retrieval. Cambridge University Press, $118-120$.
Pascanu, R., Mikolov, T., \& Bengio, Y. (2013). On the difficulty of training recurrent neural networks. In Proceedings of the 30th International Conference on Machine Learning (ICML '13), Atlanta, GA, USA, 1310-1318.
Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., \& Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825-2830.
Pennington, J., Socher, R., \& Manning, C. D. (2014). GloVe: global vectors for word representation. In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), 1532-1543.
Pierse, C. (2023). Model explainability that works seamlessly with HuggingFace transformers. GitHub, available at https:// github.com/cdpierse/transformers-interpret
Rajpurkar, P. (2023). Stanford Question Answering Dataset (SQuAD) 2.0. GitHub, available at https://rajpurkar.github.io/ SQuAD-explorer/

## Page 32
Reimers, N., \& Gurevych, I. (2019). Sentence-BERT: sentence Embeddings using Siamese BERT-Networks. arXiv: 1908.10084v1.

Richman, R., \& Wüthrich, M. V. (2019). Lee and Carter go machine learning: recurrent neural networks. SSRN ID 3441030. Version August 22, 2019.
Sanh, V., Debut, L., Chaumond, J., \& Wolf, T. (2019). DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter. arXiv:1910.01108v4.
Sundararajan, M., Taly, A., \& Yan, Q. (2017). Axiomatic attribution for deep networks. arXiv:1703.01365v2.
Swiss Association of Actuaries (2023). Code for the SAV actuarial data science tutorials. GitHub, available at https://github. com/actuarial-data-science/.
Tunstall, L., von Werra, L., \& Wolf, T. (2022). Natural Language Processing with Transformers. O'Reilly Media, Inc.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł., \& Polosukhin, I. (2017). Attention is all you need. arXiv:1706.03762v5.
Wolf, T., Debut, L., Sanh, V., Chaumond, J., Delangue, C., Moi, A., Cistac, P., Rault, T., Louf, R., Funtowicz, M., Davison, J., Shleifer, S., von Platen, P., Ma, C., Jernite, Y., Plu, J., Xu, C., Le Scao, T., Gugger, S., Drame, M., Lhoest, Q., \& Rush, A.M. (2019). HuggingFace's transformers: State-of-the-art natural language processing. arXiv:1910.03771.

Wüthrich, M. V., \& Merz, M. (2023). Statistical foundations of actuarial learning and its applications. SSRN ID 3822407. Version Nov 3, 2021.
Yin, W., Hay, J., \& Roth, D. (2019). Benchmarking zero-shot text classification: datasets, evaluation and entailment approach. arXiv:1909.00161v1.

## Page 33
# Appendix A – Data Sets

## A.1. NHTSA Accident Data

In the United States, the National Highway Traffic Safety Administration (NHTSA) is authorised by Congress to collect information on motor vehicle crashes to aid in the development, implementation, and evaluation of motor vehicle and highway safety countermeasures. From 2005 to 2007, the NHTSA conducted the National Motor Vehicle Crash Causation Study (NMVCCS). This study covers a total of 6,949 cases. For each case, a text document is available, which describes the accident situation, road and weather conditions, vehicles, drivers and passengers involved, preconditions, health status, injuries of persons involved, etc. The level of detail and length of these texts varies and averages about 400 words. In addition, tabular data is available, which encodes some of the information described, as well as additional information.

The NMVCCS database consists of several tables that are linked by the case identifier (and vehicle or passenger identifier, respectively, where relevant). For simplicity, we have extracted parts of the information contained in the NMVCCS database into a single data frame. Moreover, in order to simulate a multilingual environment, we have translated the accident descriptions to German using the DeepL Python API, without any postprocessing. Table A1 lists the columns.

### Table A1. Summary of Dataset Columns

|  Column Name | Type | Meaning  |
| --- | --- | --- |
|  SCASEID | Integer | Unique case identifier  |
|  NUMTOTV | Integer | Number of vehicles involved  |
|  WHEATHER1 ... WHEATHER8 | Integer | Indicators of certain weather conditions  |
|  INJSEVA | Integer | Classification of most severe injury sustained  |
|  INJSEVB | Integer | Indicator of bodily injury  |
|  SUMMARY_EN | Character string | Original case description in English  |
|  SUMMARY_DE | Character string | German translation of case description  |

This combination of text data and tabular data is ideal for our work, because it allows us to use supervised learning techniques.

Figure A1 shows the histogram of NUMTOTV. All cases involve at least one vehicle. Most cases involve two vehicles, and only very few accidents involve more than three vehicles.


**Figure A1.** Distribution of NUMTOTV, the number of vehicles involved.
![Page 33 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p33_img1.jpg)

## Page 34
**Figure A2.** Box plot of the length of the English case descriptions (counting words split by empty space) by number of vehicles involved. The minimum/average/maximum length is 60/419/1248 words, respectively.

|  INJSEVA | Description | INJSEVB = 0 | INJSEVB = 1 | Total  |
| --- | --- | --- | --- | --- |
|  0 | O – No injury | 1,458 | 96 | 1,554  |
|  1 | C – Possible injury | 1,112 | 1,298 | 2,410  |
|  2 | B – Non-incapacitating injury | 729 | 945 | 1,674  |
|  3 | A – Incapacitating injury | 304 | 373 | 677  |
|  4 | K – Killed | 5 | 114 | 119  |
|  5 | U – Injury, severity unknown | 44 | 122 | 166  |
|  6 | Died prior to crash | 0 | 0 | 0  |
|  9 | Unknown if injured | 51 | 16 | 67  |
|  10 | No person in crash | 1 | 0 | 1  |
|  11 | No PAR (police accident report) obtained | 231 | 50 | 281  |
|  Total |  | 3,935 | 3,014 | 6,949  |

**Table A2.** Distribution of INJSEVA and INJSEVB

INJSEVA indicates the most serious sustained injury in the accident. For instance, if one person was not injured, and another person suffered a non-incapacitating injury, injury class 2 was assigned to the case. This information has been extracted by the NHTSA from police accident reports, if available. Unfortunately, this information does not necessarily align with the case description. There are many cases for which the case description indicates the presence of an injury, but INJSEVA does not, and vice versa. For this reason, we created manually an additional column INJSEVB based on the case description, to indicate the presence of a (possible) bodily injury. Table A2 shows the distribution of number of cases by the two variables.

The length of the case descriptions correlates with the number of vehicles involved, see Figure A2.

Figure A3 shows a sample text, and Figures A4, A5 and A6 show word importance visualisations obtained using the approach described in Section 8.3.
![Page 34 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p34_img1.jpg)

## Page 35
V1, a 2000 Pontiac Montana minivan, made a left turn from a private driveway onto a northbound 5-lane twoway, dry asphalt roadway on a downhill grade. The posted speed limit on this roadway was 80 kmph ( 50 MPH ). V1 entered the roadway by crossing over the two southbound lanes and then entering the third northbound lane, which was a left turn-only lane at a 4-way intersection. The driver of V1 intended to travel straight through the intersection, and so he began to change lanes to the right. He did not see V2, a 1994 Pontiac Grand Am, that was traveling in the second northbound lane. The northbound roadway had curved to the right prior to the private driveway that V1 had exited. As V1 began to change lanes to the right, the front of V1 contacted the left rear of V2 before coming to final rest on the roadway. The driver of V1 was a 60-year old male who reported that he had been traveling between 2-17 kmph (1-10 mph) prior to the crash. He had no health-related problems, and had taken no medication prior to the crash. He was rested and traveling back home. He was wearing his prescribed lenses that corrected a myopic (nearsighted) condition. He did not sustain any injuries from the crash and refused treatment. The Critical Precrash Event for the driver of V1 was when he began to travel over the lane line on the right side of the travel lane. The Critical Reason for the Critical Precrash Event was inadequate surveillance (failed to look, looked but did not see). Associated factors coded to the driver of V1 include an illegal use of a left turn lane (cited by police) and an unfamiliarity with the roadway. As per the driver of V1, this was the first time he had driven on this roadway. The driver of V2 was a 28-year old woman who reported that she had been traveling between 66-80 kmph (41-50 mph) prior to the crash. She had no health-related problems, and had taken no medication prior to the crash. She was rested and on her way home. She does not wear corrective lenses. She sustained minor injuries and was transported to a local trauma facility. The Critical Precrash Event for the driver of V2 was when the other vehicle encroached into her lane, from an adjacent lane (same direction) over the left lane line. The Critical Reason for the Critical Precrash Event was not coded to the driver of V2 and no associated factors were coded to her.
$====$
V1, ein Minivan der Marke Pontiac Montana aus dem Jahr 2000, bog von einer privaten Einfahrt nach links auf eine zweispurige, trockene Asphaltstraße mit 5 Fahrspuren in nördlicher Richtung und einem Gefälle ab. Die zulässige Höchstgeschwindigkeit auf dieser Fahrbahn betrug $80 \mathrm{~km} / \mathrm{h}$ ( 50 MPH ). V1 fuhr auf die Fahrbahn, indem er die beiden Fahrspuren in Richtung Süden überquerte und dann auf die dritte Fahrspur in Richtung Norden einfuhr, die an einer Kreuzung mit vier Fahrspuren nur für Linksabbieger vorgesehen war. Der Fahrer von V1 beabsichtigte, geradeaus über die Kreuzung zu fahren, und begann daher, die Spur nach rechts zu wechseln. Dabei übersah er V2, einen Pontiac Grand Am von 1994, der auf der zweiten Fahrspur in Richtung Norden unterwegs war. Die Fahrbahn in nördlicher Richtung war vor der privaten Einfahrt, aus der V1 herausgefahren war, nach rechts gebogen. Als V1 begann, die Spur nach rechts zu wechseln, berührte die Front von V1 das linke Heck von V2, bevor er auf der Fahrbahn zum Stehen kam. Der Fahrer von V1 war ein 60-jähriger Mann, der angab, vor dem Unfall mit einer Geschwindigkeit von 2 bis $17 \mathrm{~km} / \mathrm{h}$ unterwegs gewesen zu sein. Er hatte keine gesundheitlichen Probleme und hatte vor dem Unfall keine Medikamente eingenommen. Er war ausgeruht und auf dem Weg nach Hause. Er trug die ihm verschriebenen Kontaktlinsen, die eine Kurzsichtigkeit korrigieren. Er zog sich bei dem Unfall keine Verletzungen zu und lehnte eine Behandlung ab. Das kritische Ereignis vor dem Unfall war für den Fahrer von V1, als er begann, die Fahrspurlinie auf der rechten Seite der Fahrbahn zu überfahren. Der kritische Grund für das kritische Ereignis vor dem Unfall war unzureichende Überwachung (nicht hingesehen, hingesehen, aber nicht gesehen). Zu den assoziierten Faktoren, die dem Fahrer von V1 zugeschrieben werden, gehören das illegale Benutzen einer Linksabbiegerspur (von der Polizei verwarnt) und die Unkenntnis der Fahrbahn. Für den Fahrer von V1 war es das erste Mal, dass er diese Fahrbahn befuhr. Bei der Fahrerin von V2 handelte es sich um eine 28-jährige Frau, die angab, vor dem Unfall mit einer Geschwindigkeit von 66-80 km/h unterwegs gewesen zu sein. Sie hatte keine gesundheitlichen Probleme und hatte vor dem Unfall keine Medikamente eingenommen. Sie war ausgeruht und befand sich auf dem Heimweg. Sie trägt keine Korrekturgläser. Sie erlitt leichte Verletzungen und wurde in eine örtliche Unfallklinik gebracht. Das kritische Ereignis vor dem Unfall war für die Fahrerin von V2, als das andere Fahrzeug von einer benachbarten Fahrspur (gleiche Richtung) über die linke Fahrspurlinie in ihre Spur eindrang. Der kritische Grund für das kritische Vorunfallereignis wurde der Fahrerin von V2 nicht zugeordnet, und es wurden ihr keine zugehörigen Faktoren zugeordnet.

Figure A3. Sample of SUMMARY_EN and SUMMARY_DE (SCASEID $=200501269400$ ).

## Page 36
**Figure A4.** Word importance visualisation for a true positive example (SCASEID = 2006008500862). Apparently, the most important word is "injuries." The original text is padded to a length of 512 tokens (not all shown in the exhibit).

|  Legend: ☐ Negative ☐ Neutral ☐ Positive |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
![Page 36 Image 1](cs12_actuarial_applications_of_natural_language_processing_assets/cs12_actuarial_applications_of_natural_language_processing_p36_img1.jpg)

## Page 37
# A.2. Wisconsin Local Government Property Insurance Fund 

This dataset concerns property insurance claims of the Wisconsin Local Government Property Insurance Fund (LGPIF), made available by Frees (2020). The Wisconsin LGPIF is an insurance pool managed by the Wisconsin Office of the Insurance Commissioner. This fund provides insurance protection to local governmental institutions such as counties, schools, libraries, airports, etc. It insures property claims at buildings and motor vehicles, and it excludes certain natural and manmade perils like flood, earthquakes or nuclear accidents.

The data consists of 6,030 records ( 4,991 in the training set, 1,039 in the test set) which include a claim amount, a short English claim description and a hazard type with 9 different levels: Fire, Lightning, Hail, Wind, WaterW (weather-related water claims), WaterNW (other weather claims), Vehicle, Vandalism and Misc (any other). The following exhibit shows an example.

Table A3. Sample of the LPGIF Data Set

| Row | Vandalism | Fire | Lightning | Wind | Hail | Vehicle | WaterNW | WaterW | Misc | Loss | Description |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 6,838.87 | Lightning damage |
| 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2,085 | Lightning damage at Comm. Center |
| 6 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8,775 | Surveillance equipment stolen |
| 7 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 34,610.27 | Wind blew stack off and damaged roof |
| 9 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 9,711.28 | Forklift hit building damaging wall and door frame |
| 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1,942.67 | Water damage at courthouse |
| 30 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 3,469.79 | Light pole damaged |

For the examples shown, the peril classification is plausible, given the text description. The exception is row 11, which could be attributed to WaterNW as well.

[^0]
[^0]:    Cite this article: Troxler A and Schelldorfer J. (2024). Actuarial applications of natural language processing using transformers: Case studies for using text features in an actuarial context. British Actuarial Journal. https://doi.org/10.1017/ S1357321724000023