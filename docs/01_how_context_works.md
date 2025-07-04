# 🧠 How Context Works in LLMs

Context in LLMs refers to the entire prompt or input the model receives before generating a response. It includes user instructions, data retrieved from knowledge sources, system-level messages, and any conversational history.

---

## Context = Memory Window

LLMs like GPT-4 don't have long-term memory. They generate output solely based on the context window — a sliding buffer of the most recent tokens (e.g., 8K, 32K, or more).

Everything the model "knows" in that moment is encoded in the tokens it sees.

---

## Key Principles

### 1. Tokenization

LLMs don’t read words — they read **tokens**, which may be entire words, subwords, or characters.

Use a tokenizer (like `tiktoken`) to preview how many tokens your input uses.

### 2. Position Matters

The model pays close attention to where things are placed. Instructions near the end might be ignored in favor of earlier context, or vice versa, depending on model architecture.

### 3. Relevance vs. Length

More context isn’t always better. You want the **most relevant**, well-structured info — not the most data. Cluttered prompts can confuse the model.

### 4. Hidden Influence

Even system prompts, example completions, or format hints (like colons or line breaks) can shape how the model behaves.

---

## Visualization Example

Imagine your context as a stack:

```
[System Prompt]
[Retrieved Snippets]
[User Instruction]
[Chat History]
```

This entire stack is tokenized and fed into the model at once. The order and phrasing of each piece affect prediction.

---

## TL;DR

> The model sees what you give it. It knows nothing else.

Context engineering is about mastering this one fact — and learning to make every token count.

➡️ Continue to the next doc to learn about effective prompt strategies.
