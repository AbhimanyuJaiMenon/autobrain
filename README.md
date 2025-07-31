
# 🧠 Autonomous AI Brainstorming System

Simulate a team of autonomous AI agents—Product Manager, Developer, Designer, and Marketer—collaborating on your startup or product idea. Each agent brings unique insights and domain expertise to expand, validate, and evolve your concepts in real time.

---

## 🚀 Features

- 🧑‍💼 Product Manager agent for feature scoping and use-case design
- 👨‍💻 Developer agent suggesting implementation plans and tools
- 🎨 Designer agent proposing UI/UX ideas
- 📈 Marketer agent crafting GTM (Go-To-Market) strategies
- 💾 Session-based memory retention for agent context consistency
- 📄 Export brainstorm results as `.pdf`, `.md`, or `.txt`
- 🔁 Modular & extendable agent design using LangChain

---

## 🛠️ Tech Stack

- **LangChain**
- **Ollama** (running LLaMA3 or other local LLMs)
- **ChromaDB** (for memory)
- **nomic-embed-text** (for embeddings)
- **Streamlit** (interactive UI)
- **FPDF** (for PDF export)

---

## 💡 How It Works

1. Input your product or startup idea.
2. The Product Manager interprets the idea and forms a base strategy.
3. Each specialized agent reacts to the PM’s output in sequence.
4. The system stores outputs in session memory for contextual responses.
5. Export your brainstorming session for documentation or collaboration.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/autonomous-ai-brainstormer.git
cd autonomous-ai-brainstormer
python -m venv venv
venv\Scripts\activate      # or source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Run the App

Ensure Ollama is running a supported model (e.g., `llama3`) before launching:

```bash
streamlit run ui/app.py
```

---

## 📤 Export Formats

- ✅ Markdown (`.md`)
- ✅ Plaintext (`.txt`)
- ✅ PDF (`.pdf` via in-browser button)

---

## 🧠 Example Use Case

> 💡 **Idea**: A voice journaling app that summarizes your day and tracks mood patterns  
> The AI agents will brainstorm features, architecture, UI concepts, and marketing strategy.

---

## 🧰 Future Improvements

- Agent feedback loops
- Roleplay conversations between agents
- Long-term memory (optional persistent ChromaDB)
- Voice-based inputs via Whisper or faster-whisper

---

## 📃 License

MIT License

---

## 🙋‍♂️ Author

Abhimanyu Jai Menon  
[LinkedIn](https://www.linkedin.com/in/abhimanyujaimenon/) | [GitHub](https://github.com/AbhimanyuJaiMenon)
=======
# autobrain
A multi-agent autonomous brainstorming system powered by LLaMA3 and LangChain.
