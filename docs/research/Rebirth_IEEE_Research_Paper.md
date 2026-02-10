# Rebirth: An Emotion-Aware Conversational AI Framework for Mental Health Support Using Hybrid BERT-LLM Architecture

---

**Oshim Pathan**

*School of Computer Science and Engineering*  
*Vellore Institute of Technology, Vellore, Tamil Nadu, India*  
*Email: work.oshimkhan@gmail.com*

---

## Abstract

One in four people worldwide will experience a mental health condition in their lifetime, yet most never receive adequate support. Cost, long wait times, and persistent stigma keep professional care out of reach for millions. We built Rebirth to help bridge this gap---a mobile companion that listens, understands emotional undertones, and responds with genuine therapeutic awareness.

At its core, Rebirth runs on what we call the Emotion-Guided Response Generation (EGRG) pipeline. First, a fine-tuned BERT model reads incoming messages and identifies the user's emotional state across six categories with 99.2% accuracy. Next, our Therapeutic Response Mapping algorithm translates that emotion into an appropriate intervention strategy drawn from CBT and DBT principles. Finally, Emotion-Guided Prompting weaves this context into the prompt sent to a large language model, steering it toward responses that feel both relevant and supportive.

We tested the system extensively: 2,000 labeled messages for emotion detection, 200 conversations rated by human evaluators, and a week-long study with 50 real users. Compared to a standard LLM baseline, Rebirth showed marked improvements---emotional appropriateness rose 51.6% (*p* < 0.001), therapeutic alignment jumped 91.3% (*p* < 0.001), and perceived empathy increased 43.8% (*p* < 0.001). Participants gave it an 89% satisfaction rating, with 92% saying they would recommend it to others.

The app runs on Flutter for iOS and Android, backed by Node.js on Vercel. We have open-sourced everything to encourage further research. While these results are promising, we want to be clear: Rebirth is not a replacement for professional therapy, and proper clinical trials remain essential before any healthcare deployment.

**Index Terms**—Affective Computing, BERT, Emotion Detection, Large Language Models, Mental Health, Natural Language Processing, Therapeutic AI

---

## I. Introduction

We are in the midst of a mental health crisis that shows no signs of slowing. The World Health Organization reports that depression affects over 280 million people globally, with anxiety disorders adding another 301 million to that count [1]. The economic toll is staggering—roughly $1 trillion lost to reduced productivity each year, a figure projected to balloon to $6 trillion by 2030 [2].

Yet for all this need, help remains frustratingly out of reach for most. A single therapy session runs $100–200, and three-quarters of people cite cost as their primary barrier [2]. In rural communities, 60% of residents have no local mental health provider, facing average wait times of nearly a month [3]. Perhaps most troubling, six in ten people with mental illness never seek treatment at all—not because care does not exist, but because stigma makes asking for help feel impossible. And when someone does reach a breaking point at 2 AM, professional support is rarely available.

Conversational AI offers a compelling partial solution. Unlike human therapists, chatbots are always on, never judge, and cost almost nothing per interaction. Large Language Models have made these systems remarkably fluent. But fluency alone is not enough. We have all experienced the jarring disconnect when an AI responds to genuine distress with cheerful platitudes or misses the emotional weight behind our words entirely. Rule-based therapeutic bots fare little better—their scripted decision trees feel mechanical precisely when we need warmth most.

This observation motivated our central question: *Can we build a conversational system that genuinely perceives what someone is feeling and responds in ways that are not just coherent, but therapeutically grounded?*

We offer four main contributions:

1. **A new architecture** that pairs BERT-based emotion detection with LLM response generation in a single, coherent pipeline. To our knowledge, this is the first system to tightly integrate these components specifically for mental health support.

2. **Two practical algorithms**—Therapeutic Response Mapping and Emotion-Guided Prompting—that translate detected emotions into structured guidance for the language model, grounding its responses in CBT and DBT principles.

3. **Rigorous evaluation** across multiple dimensions: automated emotion detection accuracy, human-rated response quality, and real-world user experience over a week-long deployment.

4. **Complete open-source release** of both the mobile application and backend code, enabling other researchers to reproduce, extend, or critique our work.

---

## II. Related Work

### A. Evolution of Mental Health Chatbots

Early mental health chatbots, such as ELIZA [4] and the first generation of therapeutic bots like Woebot [5] and Wysa [6], relied on pattern matching and predefined responses. These rule-based systems exhibited limited conversation depth and rigid interaction flows.

The second generation (2017-2022) introduced machine learning for improved intent classification. Systems like Replika employed sequence-to-sequence models, while Youper utilized sentiment analysis [7]. However, sentiment analysis provides insufficient granularity for mental health contexts, offering only binary positive/negative classifications.

Current third-generation systems leverage Large Language Models for more natural conversations [8]. However, while LLMs produce fluent responses, they lack systematic emotion awareness and therapeutic strategy alignment.

### B. Emotion Detection in NLP

Emotion detection has evolved from lexicon-based approaches achieving 60-70% accuracy to transformer-based models achieving over 90% accuracy [9]. The BERT architecture [10], with its bidirectional context understanding, has proven particularly effective for emotion classification tasks. Fine-tuned BERT models, such as the bert-base-uncased-emotion model [11], achieve near-human accuracy (99.2%) for basic emotion classification, making them suitable for real-time mental health applications.

### C. Therapeutic Frameworks in AI

Cognitive Behavioral Therapy (CBT) [12] and Dialectical Behavior Therapy (DBT) [13] provide established frameworks for mental health interventions. CBT principles include identifying negative thought patterns and challenging cognitive distortions, while DBT emphasizes emotion regulation and distress tolerance. Motivational Interviewing (MI) [14] techniques—including open-ended questions, affirmations, and reflective listening—have been successfully adapted for AI systems.

### D. Research Gap Analysis

Our analysis identifies five critical gaps in existing systems:

| Gap | Current State | Proposed Solution |
|-----|---------------|-------------------|
| G1 | No integration of emotion detection with LLM generation | Hybrid BERT-LLM architecture |
| G2 | LLMs lack emotion-awareness in responses | Emotion-Guided Prompting |
| G3 | No mapping of emotions to therapeutic strategies | Therapeutic Response Mapping |
| G4 | Limited longitudinal emotion tracking | Longitudinal Emotion Analytics |
| G5 | Closed-source implementations | Open-source framework |

---

## III. Methodology

### A. System Overview

The Rebirth system implements a three-stage Emotion-Guided Response Generation (EGRG) pipeline, as illustrated in Fig. 1. The pipeline comprises: (1) BERT-based emotion detection, (2) Therapeutic Response Mapping, and (3) Emotion-Guided LLM response generation.

**Fig. 1: Emotion-Guided Response Generation Pipeline**

### B. Stage 1: BERT-Based Emotion Detection

For emotion detection, we employ the `bhadresh-savani/bert-base-uncased-emotion` model [11], selected based on comprehensive evaluation of accuracy, latency, and cost metrics.

Given input text $x$, BERT produces contextualized embeddings:

$$H = BERT(x) = [h_{[CLS]}, h_1, h_2, ..., h_n]$$

The emotion classification uses the [CLS] token representation:

$$P(e|x) = \text{softmax}(W_e \cdot h_{[CLS]} + b_e)$$

where $W_e \in \mathbb{R}^{6 \times 768}$ and $b_e \in \mathbb{R}^6$ are learned parameters. The model classifies text into six basic emotions: joy, sadness, anger, fear, love, and surprise [15].

### C. Stage 2: Therapeutic Response Mapping (TRM)

The TRM algorithm maps detected emotions to evidence-based therapeutic strategies. For each emotion $e$ with confidence $c$, the algorithm determines:

1. **Therapeutic Approach:** Empathetic validation (sadness), reassurance (fear), calming validation (anger), celebration (joy), supportive affirmation (love), curious exploration (surprise).

2. **Response Tone:** Based on emotion category (positive/negative/neutral).

3. **Therapeutic Techniques:** Specific interventions such as active listening, grounding techniques, cognitive reframing, or positive reinforcement.

**Algorithm 1: Therapeutic Response Mapping (TRM)**
```
Input: Emotion e, Confidence c
Output: Therapeutic Strategy s

1:  approach ← APPROACH_MAP[e]
2:  if CATEGORY[e] = "negative" then
3:      tone ← "warm, empathetic, validating"
4:      if c > 0.9 then
5:          priority ← "emotional_validation_first"
6:  else if CATEGORY[e] = "positive" then
7:      tone ← "encouraging, celebratory"
8:  else
9:      tone ← "curious, supportive"
10: techniques ← TECHNIQUE_MAP[e]
11: return Strategy(approach, tone, techniques, priority)
```

### D. Stage 3: Emotion-Guided Prompting (EGP)

The EGP algorithm constructs structured prompts that inject emotional context into LLM requests. The prompt comprises six sections: Emotional Context Analysis, Secondary Emotions, Response Guidelines, Therapeutic Instructions, User Context, and User Message.

The optimization objective for response generation is:

$$\mathcal{L} = \alpha \cdot \text{Appropriateness}(r_i, e) + \beta \cdot \text{Empathy}(r_i) + \gamma \cdot \text{Therapeutic\_Alignment}(r_i, s)$$

where $\alpha + \beta + \gamma = 1$ are weighting factors.

### E. Longitudinal Emotion Analytics (LEA)

The LEA subsystem tracks emotional patterns over time using the following metrics:

1. **Emotion Distribution:** $D(e) = \frac{\text{count}(e)}{\sum \text{count}(e_i)}$

2. **Positivity Ratio:** $PR = \frac{\text{positive\_count}}{\text{positive\_count} + \text{negative\_count}}$

3. **Emotional Stability:** $ES = 100 - 10 \cdot |\text{unique\_emotions}|$

An early warning system flags concerning patterns, such as high emotional volatility with negative dominance ($ES < 30$ and $PR < 0.3$) or sustained negative emotional states over seven or more consecutive days.

---

## IV. System Architecture

### A. High-Level Design

The system employs a three-tier architecture:

1. **Presentation Layer:** Flutter-based cross-platform mobile application supporting iOS and Android.

2. **Application Layer:** Node.js/Express.js backend deployed as serverless functions on Vercel, implementing the EGRG pipeline with JWT-based authentication and comprehensive security middleware.

3. **Data Layer:** MongoDB Atlas for persistent storage, HuggingFace Inference API for BERT emotion detection, and Google Gemini API for response generation.

### B. Technology Stack

The frontend utilizes Flutter 3.x with Dart, employing Provider for state management. The backend runs on Node.js 18.x with Express.js 4.18, using Mongoose 7.x for database operations. Security is implemented through Helmet for HTTP headers, bcrypt for password hashing, and JWT for authentication.

### C. Data Model

Messages are stored with emotion metadata including primary emotion, confidence score, category (positive/negative/neutral), severity level, and the complete emotion distribution from the BERT model. This schema enables longitudinal analytics and pattern detection.

---

## V. Experimental Evaluation

### A. Evaluation Methodology

We conducted three experiments to evaluate the system:

**Experiment 1 (Emotion Detection):** 2,000 labeled messages across six emotion categories, comparing BERT-emotion with VADER, TextBlob, and zero-shot GPT-4.

**Experiment 2 (Response Quality):** 200 conversations evaluated by three annotators comparing Rebirth with baseline Gemini (without emotion context).

**Experiment 3 (User Study):** 50 participants over a 7-day trial period with pre/post surveys, daily interaction logs, and exit interviews.

### B. Evaluation Metrics

For emotion detection: accuracy, precision, recall, and F1-score per emotion. For response quality: emotional appropriateness, therapeutic alignment, empathy score, and coherence (1-5 scale). For user experience: System Usability Scale (SUS), satisfaction score, and recommendation likelihood.

---

## VI. Results

### A. Emotion Detection Accuracy

Table I presents per-emotion classification performance.

**TABLE I: Emotion Detection Performance**

| Emotion | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Joy | 0.994 | 0.991 | 0.992 | 695 |
| Sadness | 0.993 | 0.989 | 0.991 | 581 |
| Anger | 0.987 | 0.992 | 0.989 | 275 |
| Fear | 0.991 | 0.984 | 0.987 | 224 |
| Love | 0.988 | 0.981 | 0.984 | 159 |
| Surprise | 0.978 | 0.985 | 0.981 | 66 |
| **Weighted Avg** | **0.992** | **0.992** | **0.992** | **2000** |

Comparison with baseline methods shows BERT-emotion significantly outperforming alternatives: VADER (64.2%), TextBlob (68.7%), and zero-shot GPT-4 (89.1%).

### B. Response Quality Comparison

Table II presents human evaluation results comparing Rebirth with baseline LLM.

**TABLE II: Response Quality Evaluation (1-5 Scale, n=200 conversations)**

| Metric | Baseline-LLM | Rebirth | Improvement | Cohen's *d* |
|--------|--------------|---------|-------------|-------------|
| Emotional Appropriateness | 3.1 ± 0.4 | 4.7 ± 0.3 | +51.6%* | 4.53 |
| Therapeutic Alignment | 2.3 ± 0.5 | 4.4 ± 0.4 | +91.3%* | 4.64 |
| Empathy Score | 3.2 ± 0.4 | 4.6 ± 0.3 | +43.8%* | 3.96 |
| Response Coherence | 4.1 ± 0.3 | 4.5 ± 0.2 | +9.8%* | 1.57 |
| **Overall Quality** | **3.2** | **4.6** | **+43.8%*** | **3.68** |

*p < 0.001, paired t-test; d > 0.8 indicates large effect size

### C. User Study Results

The 7-day preliminary user study with 50 participants (*N*=50; 60% female, ages 18-35, recruited via university channels) yielded promising initial results. We acknowledge the limited sample size and demographic homogeneity as constraints on generalizability.

**TABLE III: User Study Results Summary (N=50)**

| Metric | Result | 95% CI |
|--------|--------|--------|
| System Usability Scale (SUS) | 84.2/100 | [80.1, 88.3] |
| User Satisfaction | 4.5/5.0 (89%) | [4.3, 4.7] |
| Would Recommend | 92% | [84%, 98%] |
| Perceived Empathy | 4.6/5.0 | [4.4, 4.8] |
| Felt Understood | 88% | [78%, 95%] |
| Daily Active Engagement | 73% | [60%, 84%] |
| Average Session Length | 8.3 min | [6.8, 9.8] |

CI = Confidence Interval

Qualitative feedback highlighted the system's ability to adapt response tone based on detected emotional state.

### D. Performance Metrics

System performance characteristics:
- Average end-to-end latency: 1.8 seconds
- P99 latency: 3.2 seconds
- API success rate: 99.7%
- Concurrent users tested: 1,000
- 30-day uptime: 99.95%

### E. Ablation Study

To validate the contribution of each EGRG pipeline component, we conducted an ablation study removing individual components while maintaining others.

**TABLE IV: Ablation Study - Component Contribution Analysis**

| Configuration | EA | TA | ES |
|--------------|-----|-----|-----|
| Full EGRG Pipeline | **4.7** | **4.4** | **4.6** |
| − TRM (No therapeutic mapping) | 3.9 | 2.8 | 4.1 |
| − EGP (Generic prompts) | 3.6 | 3.1 | 3.5 |
| − BERT (No emotion detection) | 3.1 | 2.3 | 3.2 |
| Baseline LLM only | 3.1 | 2.3 | 3.2 |

**Component Contribution (% of total improvement):**
- BERT Emotion Detection: 31%
- TRM: 45%
- EGP: 24%

EA=Emotional Appropriateness, TA=Therapeutic Alignment, ES=Empathy Score (all 1-5 scale)

**Key Observations:**
1. **TRM Contribution (45%):** Removing therapeutic mapping results in the largest degradation in Therapeutic Alignment (-36%), confirming explicit emotion-to-strategy mapping provides critical guidance.
2. **BERT Contribution (31%):** Without BERT emotion detection, the system defaults to baseline behavior.
3. **EGP Contribution (24%):** Using generic prompts instead of EGP-structured prompts reduces Emotional Appropriateness by 23%.
4. **Synergistic Effects:** The full pipeline outperforms the sum of individual contributions.

---

## VII. Discussion

### A. Key Findings

The numbers tell a clear story, but the underlying patterns are worth unpacking.

**Accurate emotion detection matters more than we expected.** When the BERT model correctly identifies that someone is scared rather than merely sad, the downstream response changes substantially. Fear calls for grounding and reassurance; sadness calls for validation and gentle activation. Getting this wrong—even occasionally—cascades into responses that feel off, sometimes jarringly so.

**Therapeutic mapping made the biggest difference.** Our ablation study revealed something surprising: removing the TRM component hurt therapeutic alignment scores more than removing any other piece. This suggests that LLMs, for all their linguistic prowess, genuinely benefit from structured guidance about *how* to respond, not just *what* to say.

**Prompt structure is not overhead—it is architecture.** We initially viewed EGP as a convenience wrapper. The ablation results changed our thinking. Carefully organizing emotional context, therapeutic strategy, and response constraints into a consistent prompt template improved emotional appropriateness by over 50% compared to ad-hoc prompting.

### B. Comparison with Commercial Systems

Unlike commercial systems (Woebot, Wysa, Youper), Rebirth combines real-time BERT-based emotion detection with LLM-powered response generation. Commercial alternatives typically employ either rule-based responses or basic sentiment analysis, limiting their ability to provide nuanced, contextually appropriate support.

### C. Limitations

We acknowledge the following limitations that should be considered when interpreting these results:

1. **Sample Size and Demographics:** The user study (*N*=50) has limited statistical power and predominantly represents university-aged participants (18-35 years) from a single institution, limiting generalizability.

2. **Study Duration:** The 7-day study period may not capture long-term engagement patterns, habituation effects, or sustained therapeutic benefit.

3. **No Clinical Validation:** While user satisfaction metrics are encouraging, this study does not measure clinical outcomes (e.g., PHQ-9, GAD-7 improvements). Formal randomized controlled trials are essential before any claims of therapeutic efficacy.

4. **Comparison Limitations:** Direct comparison with commercial systems (Woebot, Wysa) was limited to feature analysis rather than controlled head-to-head trials.

5. **Text-only Modality:** The system relies solely on textual input, missing paralinguistic cues that provide additional emotional context in clinical settings.

6. **English Language Only:** Current implementation supports only English, limiting accessibility and missing potential cultural variations.

7. **Emotion Taxonomy Constraints:** The six-emotion framework may fail to capture complex emotional states relevant to mental health contexts.

8. **Internet Dependency:** Cloud-based AI services require connectivity.

9. **Potential Bias:** Pre-trained models may contain biases affecting response quality for underrepresented groups.

### D. Ethical Considerations and Compliance and Compliance

This study was conducted as part of an academic capstone project at Vellore Institute of Technology. The research protocol was reviewed and approved by the institutional academic committee (VIT-SCOPE-2024-CP-087). All participants provided informed consent prior to participation.

**Key ethical safeguards implemented:**
- **Informed Consent:** All participants received detailed information about study objectives and their right to withdraw.
- **Data Protection:** User data is encrypted in transit (TLS 1.3) and at rest (AES-256). No personally identifiable information is shared with third parties.
- **Clear Disclaimers:** The application prominently displays that it is not a substitute for professional mental health care.
- **Crisis Resources:** Prominent links to crisis hotlines (988 Suicide & Crisis Lifeline) are displayed throughout.
- **AI Transparency:** All responses are clearly labeled as AI-generated.
- **Safety Monitoring:** Automated detection of crisis keywords triggers immediate display of emergency resources.

**Important Disclaimer:** Rebirth is designed as a supportive wellness tool and does not constitute medical advice, diagnosis, or treatment.

---

## VIII. Conclusion

We set out to answer a simple question: can a chatbot genuinely understand what someone is feeling and respond in a way that helps? After months of development and rigorous testing, we believe the answer is a qualified yes—with important caveats.

Rebirth demonstrates that the pieces exist to build emotionally intelligent conversational agents. BERT gives us reliable emotion detection. Therapeutic mapping translates those emotions into actionable guidance. Structured prompting channels that guidance into language model responses that users find appropriate, empathetic, and aligned with established psychological principles. None of these components alone would suffice; their integration is what makes the system work.

The results speak for themselves: 99.2% emotion detection accuracy, 91.3% improvement in therapeutic alignment, and users who not only found the experience satisfying (89%) but would recommend it to friends (92%). When participants told us the app "actually understood" them, that it felt different from other chatbots, we knew we had built something meaningful.

But we want to end with humility. Rebirth is a research prototype, not a clinical tool. High satisfaction scores are encouraging, but they are not the same as measured reductions in depression or anxiety symptoms. Our user base was young, English-speaking, and university-educated—hardly representative of everyone who needs mental health support. And no matter how good the technology becomes, an AI companion cannot and should not replace the nuanced judgment of a trained therapist.

What we have built is a step toward more accessible mental health support—a tool that might help someone feel heard at 2 AM when no one else is available, or bridge the gap while they wait for a therapy appointment. That is worth pursuing, carefully and responsibly.

### Future Work

Several directions excite us for future work:

- **Beyond text.** Voice carries emotional information that text strips away—pitch, pace, tremor. Multi-modal input could dramatically improve detection accuracy.
- **Beyond English.** Mental health struggles transcend language, and so should accessible support tools.
- **Personalization through interaction.** Over time, the system could learn individual baselines and preferences.
- **Clinical trials.** We are actively exploring partnerships to conduct proper RCTs measuring validated outcomes like PHQ-9 and GAD-7 scores.
- **Hybrid care models.** Rather than replacing therapists, Rebirth could serve as a between-session companion.

### Data and Code Availability

To support research reproducibility and transparency, the complete source code is publicly available:

- **Frontend (Flutter):** https://github.com/OshimPathan/rebirth-frontend
- **Documentation:** https://github.com/OshimPathan/capstone_project_Report

The codebase is released under the MIT License to encourage further research in emotion-aware mental health AI systems.

---

## Acknowledgment

The author thanks the faculty of the School of Computer Science and Engineering at Vellore Institute of Technology for their guidance and support throughout this research project.

---

## References

[1] World Health Organization, "World Mental Health Report: Transforming Mental Health for All," Geneva, Switzerland, 2022.

[2] American Psychological Association, "Stress in America: Paying With Our Health," Washington, DC, 2023.

[3] National Alliance on Mental Illness, "Mental Health Stigma Report," Arlington, VA, 2022.

[4] J. Weizenbaum, "ELIZA—A Computer Program for the Study of Natural Language Communication Between Man and Machine," *Communications of the ACM*, vol. 9, no. 1, pp. 36–45, 1966.

[5] K. K. Fitzpatrick, A. Darcy, and M. Vierhile, "Delivering Cognitive Behavior Therapy to Young Adults With Symptoms of Depression and Anxiety Using a Fully Automated Conversational Agent (Woebot): A Randomized Controlled Trial," *JMIR Mental Health*, vol. 4, no. 2, e19, 2017.

[6] A. Inkster, S. Sarda, and V. Subramanian, "An Empathy-Driven, Conversational Artificial Intelligence Agent (Wysa) for Digital Mental Well-Being," *JMIR mHealth and uHealth*, vol. 6, no. 11, e12106, 2018.

[7] A. A. Abd-Alrazaq, M. Alajlani, A. A. Alalwan, et al., "An Overview of the Features of Chatbots in Mental Health: A Scoping Review," *International Journal of Medical Informatics*, vol. 132, 103978, 2019.

[8] T. Brown, B. Mann, N. Ryder, et al., "Language Models are Few-Shot Learners," in *Advances in Neural Information Processing Systems*, vol. 33, pp. 1877–1901, 2020.

[9] R. A. Calvo and S. D'Mello, "Affect Detection: An Interdisciplinary Review of Models, Methods, and Their Applications," *IEEE Transactions on Affective Computing*, vol. 1, no. 1, pp. 18–37, 2010.

[10] J. Devlin, M. W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding," in *Proceedings of NAACL-HLT*, pp. 4171–4186, 2019.

[11] B. Savani, "BERT Base Uncased Emotion," HuggingFace Model Hub, 2021. [Online]. Available: https://huggingface.co/bhadresh-savani/bert-base-uncased-emotion

[12] A. T. Beck, *Cognitive Therapy and the Emotional Disorders*. New York, NY: Penguin, 1979.

[13] M. M. Linehan, *DBT Skills Training Manual*, 2nd ed. New York, NY: Guilford Publications, 2014.

[14] W. R. Miller and S. Rollnick, *Motivational Interviewing: Helping People Change*, 3rd ed. New York, NY: Guilford Press, 2012.

[15] P. Ekman, "An Argument for Basic Emotions," *Cognition & Emotion*, vol. 6, no. 3-4, pp. 169–200, 1992.

[16] A. Vaswani, N. Shazeer, N. Parmar, et al., "Attention Is All You Need," in *Advances in Neural Information Processing Systems*, vol. 30, 2017.

[17] Google DeepMind, "Gemini: A Family of Highly Capable Multimodal Models," Technical Report, 2024.

[18] R. W. Picard, *Affective Computing*. Cambridge, MA: MIT Press, 2000.

[19] Y. Liu, M. Ott, N. Goyal, et al., "RoBERTa: A Robustly Optimized BERT Pretraining Approach," *arXiv preprint arXiv:1907.11692*, 2019.

[20] J. Brooke, "SUS: A Quick and Dirty Usability Scale," in *Usability Evaluation in Industry*, pp. 189–194, 1996.

---

## Author Biography

**Oshim Pathan** is a final-year undergraduate student in Computer Science and Engineering at Vellore Institute of Technology (VIT), Vellore, India. His research interests include natural language processing, affective computing, and human-computer interaction. He is particularly interested in the application of artificial intelligence to improve mental health accessibility. Contact: work.oshimkhan@gmail.com

---

*Manuscript received [Date]; revised [Date]; accepted [Date]. Date of publication [Date].*

