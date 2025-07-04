# 🚀 Streamlit App Guide

The project includes a user-friendly [Streamlit](https://streamlit.io) interface for interactively exploring context engineering tools.

This guide walks you through its layout, usage, and development tips.

---

## 📂 Launching the App

To run the app locally:

```bash
streamlit run src/streamlit_app/Main.py
```

Or use Docker:

```bash
docker-compose up --build
```

Ensure your `requirements.txt` or environment has the proper dependencies.

---

## 🧭 App Sections

The Streamlit UI is organized into:

* **Overview**: Intro to context engineering and links to documentation
* **Prompt Tester**: Try out various prompts with LLM backends
* **Context Visualizer**: Token inspection, structure, and preview
* **Retrieval Playground**: Simulate RAG workflows with document chunks
* **Settings**: Adjust token budget, model, or app behavior

---

## 🛠 Developer Notes

* Streamlit reruns the script top-to-bottom on every interaction
* Use `st.session_state` to preserve values
* Modularize features under `src/streamlit_app/utils` for clarity
* You can extend the app by adding new pages using Streamlit’s `multipage` pattern

---

## 💡 Tips for Usage

* Try short vs. long prompts to see token effects
* Use the tokenizer view to debug overflow issues
* Experiment with context order to observe output changes

---

## 📌 Next Steps

> Explore context assembly in practice using the retrieval playground.

This app is designed to make the invisible visible — giving you control over how models interpret input.

➡️ Continue to the next doc for more advanced retrieval strategies.
