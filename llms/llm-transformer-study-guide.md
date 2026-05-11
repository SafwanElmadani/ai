# LLM Transformer Study Guide

A 6-phase path from zero to building and understanding modern LLMs. Estimated 6 to 10 weeks at ~10 hrs/week, but go at your own pace.

---

## Phase 0: Prerequisites (skip if comfortable)

**Goal:** Be fluent enough in Python and math to follow along.

- [ ] Python: classes, list comprehensions, NumPy basics
- [ ] Linear algebra: vectors, matrix multiplication, dot products
  - [ ] 3Blue1Brown, "Essence of Linear Algebra" (~3 hrs)
- [ ] Calculus: derivatives, chain rule, partial derivatives (intuition is enough)
  - [ ] 3Blue1Brown, "Essence of Calculus" (~3 hrs)
- [ ] PyTorch basics: tensors, autograd, `nn.Module`
  - [ ] PyTorch official "60 Minute Blitz" tutorial

**Checkpoint:** You can read `y = x @ W + b` and explain what shape everything is.

---

## Phase 1: Deep Learning Foundations

**Goal:** Understand backprop, gradient descent, and basic neural nets by building them.

- [ ] Karpathy, "The spelled-out intro to neural networks and backpropagation: building micrograd" (~2.5 hrs)
- [ ] Karpathy, "makemore" part 1: bigrams
- [ ] Karpathy, "makemore" part 2: MLPs
- [ ] Karpathy, "makemore" part 3: activations, gradients, BatchNorm
- [ ] Read: chapters 1 to 3 of d2l.ai (free, online)

**Build:**
- [ ] micrograd from scratch
- [ ] Character-level MLP language model

**Checkpoint:** You can explain what a gradient is, why we use cross-entropy loss, and what dropout does.

---

## Phase 2: Visual Intuition for Transformers

**Goal:** Get the picture before the math.

- [ ] 3Blue1Brown, "Neural Networks" chapter 5 (transformers)
- [ ] 3Blue1Brown, "Neural Networks" chapter 6 (attention)
- [ ] 3Blue1Brown, "Neural Networks" chapter 7 (how LLMs store facts)
- [ ] Jay Alammar, "The Illustrated Transformer"
- [ ] Jay Alammar, "The Illustrated GPT-2"

**Checkpoint:** You can sketch the transformer block on paper and explain Q, K, V in one paragraph.

---

## Phase 3: The Foundational Paper

**Goal:** Read the original work and connect it to code.

- [ ] Vaswani et al., "Attention Is All You Need" (2017)
- [ ] Harvard NLP, "The Annotated Transformer" (paper walkthrough with PyTorch)
- [ ] Optional: Lilian Weng, "The Transformer Family"

**Checkpoint:** You understand multi-head attention, positional encodings, and why transformers replaced RNNs.

---

## Phase 4: Build a GPT From Scratch

**Goal:** Implement a working transformer end-to-end.

- [ ] Karpathy, "Let's build GPT: from scratch, in code, spelled out" (~2 hrs)
- [ ] Karpathy, "Let's build the GPT Tokenizer" (~2 hrs)
- [ ] Karpathy, "Let's reproduce GPT-2 (124M)" (~4 hrs)

**Build:**
- [ ] nanoGPT trained on Tiny Shakespeare
- [ ] Your own BPE tokenizer
- [ ] A small GPT-2 reproduction (Colab or local GPU)

**Checkpoint:** You can write a transformer block in PyTorch from memory.

---

## Phase 5: Modern LLM Architecture

**Goal:** Understand what changed between 2017 GPT and today's models.

Architecture papers (skim, don't memorize):
- [ ] RoPE: "RoFormer: Enhanced Transformer with Rotary Position Embedding"
- [ ] RMSNorm and SwiGLU (referenced in the LLaMA paper)
- [ ] "LLaMA: Open and Efficient Foundation Language Models" (Meta, 2023)
- [ ] "Mistral 7B" (sliding window attention, GQA)
- [ ] "Mixtral of Experts" (MoE)
- [ ] "FlashAttention" (Dao et al.)

Scaling and training:
- [ ] "Scaling Laws for Neural Language Models" (Kaplan et al.)
- [ ] "Training Compute-Optimal Large Language Models" (Chinchilla)

**Checkpoint:** You can explain GQA, RoPE, and why MoE saves compute.

---

## Phase 6: Specialize (pick one or more)

**Goal:** Go deep in a direction that matches your interest.

### Track A: Mechanistic Interpretability
- [ ] Anthropic, "A Mathematical Framework for Transformer Circuits"
- [ ] Neel Nanda, "Concrete Steps to Get Started in Transformer Mechanistic Interpretability"
- [ ] ARENA curriculum (free, hands-on)

### Track B: Post-training and Alignment
- [ ] "Training language models to follow instructions" (InstructGPT)
- [ ] "Direct Preference Optimization" (DPO)
- [ ] "Constitutional AI" (Anthropic)

### Track C: Inference and Systems
- [ ] "Efficient Memory Management for Large Language Model Serving" (vLLM / PagedAttention)
- [ ] Speculative decoding papers
- [ ] Quantization: GPTQ, AWQ, GGUF

### Track D: Building Apps
- [ ] Anthropic Claude API docs and cookbook
- [ ] Prompt engineering guides
- [ ] Tool use, agents, retrieval-augmented generation

---

## Tools and Habits

- Keep a notebook (literal or Obsidian) of unfamiliar terms, with one-line definitions
- Re-implement, don't just read. If you can't code it, you don't fully understand it
- Use Colab or Lightning Studio if you don't have a GPU; nanoGPT runs fine on free tiers
- Join r/LocalLLaMA and follow a few researchers on X for ambient learning

---

## Single-Sentence Summary

Watch 3Blue1Brown for intuition, do Karpathy's Zero-to-Hero to build it yourself, read the original paper alongside the Annotated Transformer, then read modern papers (LLaMA, Mistral) to see what changed.
