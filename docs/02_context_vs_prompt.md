# 📝 Context vs. Prompt: What's the Difference?

In everyday use, “prompt” and “context” are often used interchangeably — but in the world of LLMs, they have distinct meanings.

Understanding the difference helps you design better inputs and more reliable outputs.

---

## 🔑 Definitions

### Prompt

> The final input string sent to the model for completion.

A prompt may include instructions, examples, or formatting. It's the actual text that triggers the model’s next token prediction.

### Context

> Everything the model sees — including system messages, chat history, retrieved data, and the prompt.

Think of the prompt as a **subset** of the full context window.

---

## 🧱 Components of Context

Context is often composed of several layers:

```
[System Prompt / Defaults]
[Memory or App State]
[Retrieved Knowledge]
[User Prompt]
```

All of this is tokenized and forms the "context" the model uses to respond.

---

## 🔁 Prompt is Programmable — Context is Strategic

* **Prompt engineering** focuses on structure, tone, and phrasing
* **Context engineering** manages what goes in, what order, and how much

You can reuse and template prompts, but context must be **curated dynamically** in many real-world applications (e.g., RAG).

---

## ⚖️ When to Focus on Each

| If your goal is...                | Focus on...      |
| --------------------------------- | ---------------- |
| Formatting or style control       | Prompt design    |
| Knowledge injection or grounding  | Context design   |
| Multi-turn or conversational apps | Context handling |
| Short-form questions or API usage | Prompt phrasing  |

---

## Summary

> The prompt is what you write. The context is everything the model reads.

Next up: Learn how retrieval and compression can automate context assembly. ➡️
