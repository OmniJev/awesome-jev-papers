<div align="center">

<img src="assets/cover.png" alt="Awesome JEV Papers: research papers on Jev and System One decision models" width="100%">

# Awesome JEV Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Research papers on Jev, TypeSafe's System One model, and the open models built in its shape.

[![Gallery](https://img.shields.io/badge/gallery-omnijev.github.io-2F80ED?style=flat-square&logo=githubpages&logoColor=white)](https://omnijev.github.io/awesome-jev-gallery/)

![Papers](https://img.shields.io/badge/papers-51-B31B1B?style=flat-square&logo=arxiv&logoColor=white)
![Jev papers](https://img.shields.io/badge/Jev%20papers-29-2F80ED?style=flat-square&logo=bookstack&logoColor=white)
![Foundations](https://img.shields.io/badge/foundations-22-8A2BE2?style=flat-square&logo=academia&logoColor=white)
![With code](https://img.shields.io/badge/with%20code-27-181717?style=flat-square&logo=github&logoColor=white)
![Daily Papers](https://img.shields.io/badge/%F0%9F%A4%97%20daily%20papers-30-FFD21E?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2026--09--28-10B981?style=flat-square&logo=calendar&logoColor=white)
[![License](https://img.shields.io/badge/license-CC%20BY%204.0-10B981?style=flat-square&logo=creativecommons&logoColor=white)](LICENSE)

🧭 Survey · 🔓 Open models · 📊 Judges · 🛡️ Robustness · 🤖 Agents · 🌍 Applications · 🧬 Foundations

</div>

---

## Contents

- [🔥 News](#-news)
- [🧭 Survey & Ecosystem](#-survey--ecosystem) (1)
- [🔓 Open Decision Models](#-open-decision-models) (6)
- [📊 Jev as Judge & Classifier](#-jev-as-judge--classifier) (6)
- [🛡️ Robustness & Attacks](#-robustness--attacks) (4)
- [🤖 Agents & Systems](#-agents--systems) (7)
- [🌍 Applications](#-applications) (5)
- [🧬 Foundations](#-foundations) (22)
- [🔗 Related Lists](#-related-lists)

---

## 🔥 News

🚀 **2026-09-28 · Launch.** 51 papers: 29 papers on Jev from the first two weeks after its release on 15 September, and 22 earlier papers the System One idea builds on. Every entry is checked against its arXiv page.

💡 **Ongoing · PRs welcome.** A new Jev paper on arXiv? Open a pull request with the arXiv link.

---

## 🧭 Survey & Ecosystem

Studies of how Jev is used across public projects.

- [Jev in the Wild](https://arxiv.org/abs/2609.30216), "Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem". ![arXiv](https://img.shields.io/badge/arXiv-2609.30216-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/godxue1/Jev_in_the_wild?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/godxue1/Jev_in_the_wild) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2609.30216&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2609.30216)

---

## 🔓 Open Decision Models

Open models and decoding methods that rebuild the System One shape: declared options in, one probability per option out.

- [LAVOIR](https://arxiv.org/abs/2609.30706), "LAVOIR: Teaching a Single-Pass Decision Encoder When and What to Ask with Amortized Value of Information". ![arXiv](https://img.shields.io/badge/arXiv-2609.30706-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/moganai/lavoir?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/moganai/lavoir) [![Model](https://img.shields.io/badge/%F0%9F%A4%97%20Model-8B5CF6?style=flat-square)](https://huggingface.co/moganai/lavoir) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2609.30706&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2609.30706)
- [PixelJev](https://arxiv.org/abs/2609.29283), "From Text Decisions to Pixels: An Study of Jev-Style Visual Choice Model". ![arXiv](https://img.shields.io/badge/arXiv-2609.29283-B31B1B?style=flat-square)
- [NumericJev](https://arxiv.org/abs/2609.28587), "NumericJev: Jev-like LLM Numerical Decoding with Multiway Decision Trees". ![arXiv](https://img.shields.io/badge/arXiv-2609.28587-B31B1B?style=flat-square)
- [Visual Jev](https://arxiv.org/abs/2609.25845), "Visual Jev: Accurate and Efficient Decisions from Shared Visual Context". ![arXiv](https://img.shields.io/badge/arXiv-2609.25845-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/guanxuyu-sv/Visual-Jev?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/guanxuyu-sv/Visual-Jev) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2609.25845&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2609.25845)
- [JevLite](https://arxiv.org/abs/2609.23959), "Open-Jev Judgments on CallScreenBench: Calibrated One-Pass Scam Screening with a Small Language Model". ![arXiv](https://img.shields.io/badge/arXiv-2609.23959-B31B1B?style=flat-square)
- [this-that-model-1.0](https://arxiv.org/abs/2609.23886), "this-that-model-1.0: A typed decision model that decides in 30 ms, for a millionth of a cent". ![arXiv](https://img.shields.io/badge/arXiv-2609.23886-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/FLock-io/this-that-model?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/FLock-io/this-that-model) [![Model](https://img.shields.io/badge/%F0%9F%A4%97%20Model-8B5CF6?style=flat-square)](https://huggingface.co/flock-io/this-that-model-1.0) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2609.23886&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2609.23886)

---

## 📊 Jev as Judge & Classifier

Jev measured against LLM judges, classifiers and human labels.

- [Jev vs. LLM Rubric Judges](https://arxiv.org/abs/2609.29769), "JEV vs. LLMs as Rubric Judges: Cheaper, Faster, and Wrong in the Same Places". ![arXiv](https://img.shields.io/badge/arXiv-2609.29769-B31B1B?style=flat-square)
- [Just Ask Jev](https://arxiv.org/abs/2609.29429), "Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot Detector of AI Alignment Failures". ![arXiv](https://img.shields.io/badge/arXiv-2609.29429-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/sumleo/RLCDAlignBench?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/sumleo/RLCDAlignBench) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2609.29429&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2609.29429)
- [Same Scores, Different Decisions](https://arxiv.org/abs/2609.27678), "Same Scores, Different Decisions: Evaluating JEV and Language Models for Legal Document Understanding". ![arXiv](https://img.shields.io/badge/arXiv-2609.27678-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/ZF-Utokyo/Jev-Benchmark?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/ZF-Utokyo/Jev-Benchmark)
- [Jev for Radiology Reports](https://arxiv.org/abs/2609.27607), "Can Jev Judge Radiology Reports? Evaluating a System One Model for Clinical Factuality". ![arXiv](https://img.shields.io/badge/arXiv-2609.27607-B31B1B?style=flat-square)
- [JEV-as-a-Judge](https://arxiv.org/abs/2609.26550), "JEV-as-a-Judge: Accept When Confident, Escalate When Unsure". ![arXiv](https://img.shields.io/badge/arXiv-2609.26550-B31B1B?style=flat-square) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2609.26550&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2609.26550)
- [Jev for Scientific Decisions](https://arxiv.org/abs/2609.24965), "Jev for Scientific Decisions: Evaluating Semantic Choices and Their Consequences". ![arXiv](https://img.shields.io/badge/arXiv-2609.24965-B31B1B?style=flat-square)

---

## 🛡️ Robustness & Attacks

How typed decisions move under context changes, option renaming, prompt injection and adversarial search.

- [JevAdvBench](https://arxiv.org/abs/2609.31142), "JevAdvBench: A Benchmark and Black-Box Attacks for Reinforcement Learning for Calibrated Decisions Models". ![arXiv](https://img.shields.io/badge/arXiv-2609.31142-B31B1B?style=flat-square) [![Website](https://img.shields.io/badge/Website-2EA44F?style=flat-square&logo=googlechrome&logoColor=white)](https://JevAdvBench.github.io/JevAdvBench/)
- [JevOut](https://arxiv.org/abs/2609.30243), "JevOut: Natural Context Can Flip Decision Models". ![arXiv](https://img.shields.io/badge/arXiv-2609.30243-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/xzx34/JevOut?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/xzx34/JevOut) [![Website](https://img.shields.io/badge/Website-2EA44F?style=flat-square&logo=googlechrome&logoColor=white)](https://xzx34.github.io/jevout/)
- [Decision Hijacking](https://arxiv.org/abs/2609.28613), "Decision Hijacking: Prompt Injection Attacks on Jev's Typed Probabilistic Decisions". ![arXiv](https://img.shields.io/badge/arXiv-2609.28613-B31B1B?style=flat-square) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2609.28613&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2609.28613)
- [Type-Safe Is Not Error-Free](https://arxiv.org/abs/2609.26758), "Type-Safe Is Not Error-Free: A Constrained Decision Head Follows the Option Name, Not the Rubric Bound to It". ![arXiv](https://img.shields.io/badge/arXiv-2609.26758-B31B1B?style=flat-square) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2609.26758&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2609.26758)

---

## 🤖 Agents & Systems

Jev as the fast decision layer inside agents, routers and harnesses.

- [JevSoup](https://arxiv.org/abs/2609.30922), "JevSoup: System-One Routing for Training-Free LoRA Composition". ![arXiv](https://img.shields.io/badge/arXiv-2609.30922-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/Leowang980/JevSoup?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/Leowang980/JevSoup)
- [Jev-Mobile](https://arxiv.org/abs/2609.30186), "Jev-Mobile: Jev as an Executor for Mobile GUI Agents". ![arXiv](https://img.shields.io/badge/arXiv-2609.30186-B31B1B?style=flat-square)
- [Pentest Decision Layers](https://arxiv.org/abs/2609.28940), "Calibrated Decision Models for Autonomous Penetration-Testing Harnesses: JEV and Laya as System One Decision Layers for LLM-Driven Pentest Agents". ![arXiv](https://img.shields.io/badge/arXiv-2609.28940-B31B1B?style=flat-square)
- [Coding-Agent Router](https://arxiv.org/abs/2609.28919), "Control the Harness, Control the Cost: Routing and Governing AI Coding Agents in the Enterprise". ![arXiv](https://img.shields.io/badge/arXiv-2609.28919-B31B1B?style=flat-square)
- [JEV-Star](https://arxiv.org/abs/2609.27331), "JEV-Star: Fast, Low-Cost StarCraft II Control with Language-Model Planning". ![arXiv](https://img.shields.io/badge/arXiv-2609.27331-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/sc2musa/Jev_Star?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/sc2musa/Jev_Star) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2609.27331&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2609.27331)
- [REFLEX](https://arxiv.org/abs/2609.26532), "REFLEX with Jev for Efficient Selective Control in LLM Agents". ![arXiv](https://img.shields.io/badge/arXiv-2609.26532-B31B1B?style=flat-square) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2609.26532&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2609.26532)
- [Jev-Mem](https://arxiv.org/abs/2609.23986), "Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents". ![arXiv](https://img.shields.io/badge/arXiv-2609.23986-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/libingzheren/Jev-Mem?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/libingzheren/Jev-Mem) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2609.23986&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2609.23986)

---

## 🌍 Applications

Jev applied to a domain problem.

- [KITE](https://arxiv.org/abs/2609.27535), "KITE: Scaling Jev Population Experiments with Sparse Flagship Calibration". ![arXiv](https://img.shields.io/badge/arXiv-2609.27535-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/HengyuLi-Ozaki-lab/kite_population_simulator?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/HengyuLi-Ozaki-lab/kite_population_simulator)
- [JEVQA](https://arxiv.org/abs/2609.24395), "JEVQA - Video Quality from Metadata, Bitstream, and Pixel Features with a General-Purpose Decision Model". ![arXiv](https://img.shields.io/badge/arXiv-2609.24395-B31B1B?style=flat-square)
- [Crash Narratives](https://arxiv.org/abs/2609.24052), "Calibrated Decisions at Scale: Converting Police Crash Narratives into Probabilistic Crash Variables with a System One Model (Jev)". ![arXiv](https://img.shields.io/badge/arXiv-2609.24052-B31B1B?style=flat-square)
- [6G Intent Orchestration](https://arxiv.org/abs/2609.23136), "Fast Intent-Driven Service Orchestration with Jev for 6G Edge Networks". ![arXiv](https://img.shields.io/badge/arXiv-2609.23136-B31B1B?style=flat-square)
- [Edge Service Orchestration](https://arxiv.org/abs/2609.22753), "Replacing Large Language Models with Jev Decision Models for Low-Latency Edge Service Orchestration". ![arXiv](https://img.shields.io/badge/arXiv-2609.22753-B31B1B?style=flat-square)

---

## 🧬 Foundations

Papers from before Jev that it builds on or is measured against.

### The Shape Before Jev

Encoders, calibrated rewards, diffusion decoders and serving work that the System One idea draws on.

- [Calibration-Aware RL for Decision-Making LLMs](https://arxiv.org/abs/2601.13284), "Balancing Classification and Calibration Performance in Decision-Making LLMs via Calibration Aware Reinforcement Learning". ![arXiv](https://img.shields.io/badge/arXiv-2601.13284-B31B1B?style=flat-square)
- [GLiClass](https://arxiv.org/abs/2508.07662), "GLiClass: Generalist Lightweight Model for Sequence Classification Tasks". ![arXiv](https://img.shields.io/badge/arXiv-2508.07662-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/Knowledgator/GLiClass?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/Knowledgator/GLiClass) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2508.07662&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2508.07662)
- [RLCR](https://arxiv.org/abs/2507.16806), "Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty". ![arXiv](https://img.shields.io/badge/arXiv-2507.16806-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/damanimehul/RLCR?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/damanimehul/RLCR) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2507.16806&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2507.16806)
- [Mercury](https://arxiv.org/abs/2506.17298), "Mercury: Ultra-Fast Language Models Based on Diffusion". ![arXiv](https://img.shields.io/badge/arXiv-2506.17298-B31B1B?style=flat-square) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2506.17298&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2506.17298)
- [Generative or Discriminative?](https://arxiv.org/abs/2506.12181), "Generative or Discriminative? Revisiting Text Classification in the Era of Transformers". ![arXiv](https://img.shields.io/badge/arXiv-2506.12181-B31B1B?style=flat-square)
- [Rewarding Doubt](https://arxiv.org/abs/2503.02623), "Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of Large Language Models". ![arXiv](https://img.shields.io/badge/arXiv-2503.02623-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/pasta99/RewardingDoubt?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/pasta99/RewardingDoubt)
- [LLaDA](https://arxiv.org/abs/2502.09992), "Large Language Diffusion Models". ![arXiv](https://img.shields.io/badge/arXiv-2502.09992-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/ML-GSAI/LLaDA?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/ML-GSAI/LLaDA) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2502.09992&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2502.09992)
- [Llama Guard](https://arxiv.org/abs/2312.06674), "Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations". ![arXiv](https://img.shields.io/badge/arXiv-2312.06674-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/meta-llama/PurpleLlama?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/meta-llama/PurpleLlama) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2312.06674&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2312.06674)
- [GLiNER](https://arxiv.org/abs/2311.08526), "GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer". ![arXiv](https://img.shields.io/badge/arXiv-2311.08526-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/urchade/GLiNER?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/urchade/GLiNER) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2311.08526&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2311.08526)
- [vLLM](https://arxiv.org/abs/2309.06180), "Efficient Memory Management for Large Language Model Serving with PagedAttention". ![arXiv](https://img.shields.io/badge/arXiv-2309.06180-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/vllm-project/vllm?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/vllm-project/vllm) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2309.06180&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2309.06180)
- [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774), "GPT-4 Technical Report". ![arXiv](https://img.shields.io/badge/arXiv-2303.08774-B31B1B?style=flat-square) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2303.08774&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2303.08774)
- [InstructGPT reward model](https://arxiv.org/abs/2203.02155), "Training language models to follow instructions with human feedback". ![arXiv](https://img.shields.io/badge/arXiv-2203.02155-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/openai/following-instructions-human-feedback?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/openai/following-instructions-human-feedback) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2203.02155&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2203.02155)
- [Zero-shot Classification as Entailment](https://arxiv.org/abs/1909.00161), "Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach". ![arXiv](https://img.shields.io/badge/arXiv-1909.00161-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/yinwenpeng/BenchmarkingZeroShot?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/yinwenpeng/BenchmarkingZeroShot) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F1909.00161&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/1909.00161)
- [monoBERT](https://arxiv.org/abs/1901.04085), "Passage Re-ranking with BERT". ![arXiv](https://img.shields.io/badge/arXiv-1901.04085-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/nyu-dl/dl4marco-bert?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/nyu-dl/dl4marco-bert) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F1901.04085&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/1901.04085)

### What Jev Is Sold Against

Structured generation, routing and LLM judges, the approaches Jev replaces for bounded decisions.

- [Constitutional Classifiers](https://arxiv.org/abs/2501.18837), "Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming". ![arXiv](https://img.shields.io/badge/arXiv-2501.18837-B31B1B?style=flat-square) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2501.18837&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2501.18837)
- [JSONSchemaBench](https://arxiv.org/abs/2501.10868), "JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models". ![arXiv](https://img.shields.io/badge/arXiv-2501.10868-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/guidance-ai/jsonschemabench?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/guidance-ai/jsonschemabench) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2501.10868&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2501.10868)
- [Let Me Speak Freely?](https://arxiv.org/abs/2408.02442), "Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models". ![arXiv](https://img.shields.io/badge/arXiv-2408.02442-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/appier-research/structure-gen?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/appier-research/structure-gen) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2408.02442&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2408.02442)
- [RouteLLM](https://arxiv.org/abs/2406.18665), "RouteLLM: Learning to Route LLMs with Preference Data". ![arXiv](https://img.shields.io/badge/arXiv-2406.18665-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/lm-sys/RouteLLM?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/lm-sys/RouteLLM) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2406.18665&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2406.18665)
- [DSPy](https://arxiv.org/abs/2310.03714), "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines". ![arXiv](https://img.shields.io/badge/arXiv-2310.03714-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/stanfordnlp/dspy?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/stanfordnlp/dspy) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2310.03714&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2310.03714)
- [Outlines](https://arxiv.org/abs/2307.09702), "Efficient Guided Generation for Large Language Models". ![arXiv](https://img.shields.io/badge/arXiv-2307.09702-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/dottxt-ai/outlines?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/dottxt-ai/outlines) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2307.09702&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2307.09702)
- [MT-Bench](https://arxiv.org/abs/2306.05685), "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena". ![arXiv](https://img.shields.io/badge/arXiv-2306.05685-B31B1B?style=flat-square) [![Code](https://img.shields.io/github/stars/lm-sys/FastChat?style=flat-square&logo=github&label=Code&color=181717)](https://github.com/lm-sys/FastChat) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2306.05685&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2306.05685)

### Where the Name Comes From

Dual-process thinking in AI.

- [Thinking Fast and Slow in AI](https://arxiv.org/abs/2010.06002), "Thinking Fast and Slow in AI". ![arXiv](https://img.shields.io/badge/arXiv-2010.06002-B31B1B?style=flat-square) [![Daily Papers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fpapers%2F2010.06002&query=%24.upvotes&label=%F0%9F%A4%97%20Daily&color=FFD21E&style=flat-square)](https://huggingface.co/papers/2010.06002)

---

## 🔗 Related Lists

- [Awesome JEV](https://github.com/OmniJev/awesome-jev-gallery), Papers, open models, projects and evaluations around Jev, with a picture gallery. ![List](https://img.shields.io/github/stars/OmniJev/awesome-jev-gallery?style=flat-square&logo=github&label=List&color=181717)

---

## Contributing

This list holds papers only: arXiv preprints, conference and journal papers, and technical reports. Read [CONTRIBUTING.md](CONTRIBUTING.md) first.

A paper belongs here when Jev, or a model with Jev's shape (declared options in, one calibrated probability per option out), is the subject, the method, or a measured system.

---

## Footnotes

```bibtex
@misc{awesome_jev_papers,
  title        = {Awesome JEV Papers},
  year         = {2026},
  howpublished = {\url{https://github.com/OmniJev/awesome-jev-papers}},
  note         = {A curated list of research papers on Jev and System One decision models}
}
```
