# 📚 RAG (Retrieval-Augmented Generation) Explained

Retrieval-Augmented Generation (RAG) is a technique that supplements language models with external data sources at runtime — allowing them to generate more accurate, grounded, and context-aware responses.

---

## 🤔 Why Use RAG?

LLMs have a limited context window and fixed knowledge (as of their training cut-off). RAG lets you inject **dynamic**, **custom**, and **updated** information into the model's context.

Example use cases:

* Private document QA
* Technical knowledge bases
* Legal, medical, or policy lookup

---

## 🧱 How RAG Works

Typical RAG pipeline:

```
[User Query] ─▶ [Embed & Search] ─▶ [Retrieve Chunks] ─▶ [Assemble Prompt] ─▶ [LLM Completion]
```

### 1. **Embedding**

Convert query and documents into vector representations using models like `sentence-transformers`.

### 2. **Similarity Search**

Find the most relevant document chunks using cosine similarity or vector databases (e.g., FAISS, Weaviate).

### 3. **Context Assembly**

Merge retrieved content with the user query in a way that fits within the token budget.

---

## ⚖️ Tradeoffs

| Benefit                     | Challenge                        |
| --------------------------- | -------------------------------- |
| Keeps LLM output up to date | Needs quality retrieval pipeline |
| Grounded in real documents  | Risk of irrelevant noise         |
| Scalable to large corpora   | Requires chunking & embeddings   |

---

## 📎 Tools in This Project

The app includes a **retrieval playground** that:

* Simulates document embeddings and chunk retrieval
* Shows how many tokens each chunk consumes
* Lets you test different assembly strategies

---

## Summary

> RAG bridges the gap between static models and dynamic data.

Used well, it can dramatically improve output quality — especially when facts matter.

➡️ Continue to the next doc to explore token budgeting and compression.
