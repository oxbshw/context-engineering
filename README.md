# 🧠 Context Engineering

**Context Engineering** is an open-source toolkit that helps you understand, visualize, and optimize how large language models (LLMs) process their context windows.

It’s built for AI researchers, developers, and prompt engineers who want deeper control and insight into how tokenized input is interpreted.

---

## 🚀 Quick Start

### 🔧 Option 1: Local Run

```bash
pip install -r requirements.txt
streamlit run src/streamlit_app/Main.py
```

### 🐳 Option 2: Docker

```bash
docker-compose up
```

---

## 🖥 Features

* ✍️ **Prompt Playground**: Write and analyze prompts
* 🔍 **Token Visualizer**: View how prompts are tokenized
* 📦 **RAG Context Simulator**: Inject and inspect retrieved documents
* 📊 **Context Budget Tool**: Monitor token usage
* 🧪 **Modular Design**: Easy to extend with your own components

---

## 📚 Documentation

Check the `docs/` folder for:

* `00_overview.md` – What is Context Engineering?
* `01_how_context_works.md` – How LLMs interpret input
* `02_context_vs_prompt.md` – Prompting vs context construction
* `03_streamlit_guide.md` – Using the web app
* `04_rag_explained.md` – Retrieval-Augmented Generation (RAG)
* `05_neural_fields.md` – Embeddings, position encodings, and more

---

## 🤝 Contributing

We welcome PRs and issues! To contribute:

1. Fork the repo
2. Make your changes in a branch
3. Submit a PR with a clear explanation

Run tests with:

```bash
pytest
```

Lint your code with:

```bash
flake8 src tests
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

Built using tools from OpenAI, Hugging Face, and the open-source community.

See [CITATIONS.md](CITATIONS.md) for key research references.

---

## 🌐 Live Demo

> Coming soon — stay tuned!
