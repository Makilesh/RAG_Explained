# RAG from Scratch

Ever wondered how ChatGPT could answer questions about *your* documents? That's [RAG](what_is_RAG.md). This tutorial breaks it down into simple, runnable code that actually works.



## The Files

- [`what_is_RAG.md`](what_is_RAG.md) - Start here if RAG is new to you
- [`How_does_RAG_work.ipynb`](How_does_RAG_work.ipynb) - Interactive notebook (run each cell)
- [`Complete_RAG_implementation.py`](Complete_RAG_implementation.py) - The full system (ready to run)
- [`knowledge.txt`](knowledge.txt) - Your test data
- [`RAG_knowledge.md`](RAG_knowledge.md) - Advanced stuff and FAQs

**Quick access:**
- 📖 [What is RAG?](what_is_RAG.md) - Start here for concepts
- 📓 [Step-by-step Notebook](How_does_RAG_work.ipynb) - Interactive learning
- 🚀 [Complete Implementation](Complete_RAG_implementation.py) - Production code
- 📚 [Advanced Guide](RAG_knowledge.md) - Deep dive & FAQs
- 📄 [Sample Data](knowledge.txt) - Test knowledge base

## Get Running

**Step 1:** Grab the code
```bash
git clone https://github.com/Makilesh/RAG_Explained.git
cd RAG_Explained
```

**Step 2:** Install stuff
```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Mac/Linux
pip install -r requirements.txt
```

**Step 3:** (Optional) Get a free Gemini API key
- Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
- Copy `.env.example` to `.env` and paste your key
- Skip this if you want to run locally

**Step 4:** Run it
```bash
python Complete_RAG_implementation.py
```
Ask it: *"What do elephants use their trunks for?"*

## How to Use This Repo

**Never touched RAG before?**  
Read [`what_is_RAG.md`](what_is_RAG.md) → Open [`How_does_RAG_work.ipynb`](How_does_RAG_work.ipynb) → Run each cell and watch what happens

**Just want to see it work?**  
Run [`Complete_RAG_implementation.py`](Complete_RAG_implementation.py) right now. It works out of the box.

**Building something real?**  
Check [`RAG_knowledge.md`](RAG_knowledge.md) for production tips, common pitfalls, and how to scale.

## What Makes This Different

No fluff. No 500-line enterprise boilerplate. Just:
- **Real code** that runs in 5 minutes
- **Actual explanations** of why each line exists
- **Works offline** (uses local models if you skip the API)
- **Your choice:** Gemini API for quality, or free local model

Built with: LangChain, FAISS, Sentence Transformers, Google Gemini

## The 5-Step Breakdown

This is what RAG actually does:

1. **Ingest** → Load your documents (PDFs, text files, whatever)
2. **Embed** → Turn text into numbers (so computers can compare them)
3. **Retrieve** → Find the most relevant chunks for your question
4. **Augment** → Combine your question with the retrieved info
5. **Generate** → Let an LLM write a proper answer

Each step has its own section in the notebook with runnable code.

## Try These Questions

Once you're running, ask:
- "What do elephants use their trunks for?"
- "Tell me about honey"
- Or add your own docs to [`knowledge.txt`](knowledge.txt) and ask about those

## What is RAG, Really?

> 💡 **[Full explanation in what_is_RAG.md →](what_is_RAG.md)**

You know how ChatGPT sometimes makes stuff up? RAG fixes that by letting it "look up" answers in your documents before responding.

**Without RAG:** LLM guesses based on training data  
**With RAG:** LLM reads your actual documents, then answers

It's like giving someone an open-book exam instead of making them memorize everything.

## Issues? Questions?

Open an issue. I actually read them.

Or fork it and make it better. That works too.

If this helped you build something, drop a star ⭐ 

**Resources that helped build this:**
- [LangChain Docs](https://python.langchain.com/)
- [FAISS on GitHub](https://github.com/facebookresearch/faiss)
- [Gemini API](https://ai.google.dev/)
- [Sentence Transformers](https://www.sbert.net/)
