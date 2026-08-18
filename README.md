# ML & AI Launchpad

Thirteen weeks plus Demo Day, in a real sequence. Each week names the outcome and the artifact you walk away with.

## Curriculum

| # | Week | Outcome | Stack |
|---|------|---------|-------|
| 01 | [See It Work, Then Hit the Wall](week01-see-it-work) | Build a working AI agent with zero code, then hit its limits and start writing Python to get past them. | n8n · Google Sheets · Telegram · Python |
| 02 | [Python's Data Toolkit](week02-python-data-toolkit) | Load, clean, and visualize a real dataset — and spot the pattern you'll model in Week 3. | NumPy · pandas · Matplotlib · Seaborn |
| 03 | [Machine Learning, Regression](week03-regression) | Train, evaluate, and explain your first model end to end. | scikit-learn · pandas |
| 04 | [Classification & Deployment](week04-classification-and-deployment) | Two models packaged into one deployed app. Deployment is a repeatable process, not a property of the model. | scikit-learn · MLflow · Streamlit · Flask · Docker |
| 05 | [Deep Learning & the Bridge to LLMs](week05-deep-learning-and-llms) | Run an object detection demo and make your first LLM API call. | PyTorch · YOLO · Ollama |
| 06 | [Multi-Model UIs & RAG Concepts](week06-multi-model-uis-and-rag-concepts) | Ship a real chat UI with tool calling, and understand what RAG is and why it works. | Gradio · LangChain · ChromaDB |
| 07 | [Build & Evaluate RAG](week07-build-and-evaluate-rag) | Ship a RAG app over your own documents and learn how and why RAG breaks. | LangChain · ChromaDB |
| 08 | [Fine-Tuning](week08-fine-tuning) | Fine-tune an open-source model and compare it head-to-head against a frontier model. | Hugging Face · LoRA · QLoRA · Google Colab |
| 09 | [Agent Foundations & OpenAI Agents SDK](week09-agent-foundations) | Hand-build an agent loop from scratch and deploy your own digital twin. | Python · OpenAI Agents SDK · Gradio |
| 10 | [Deep Research Agent](week10-deep-research-agent) | Build and deploy a multi-agent research system that's usable outside the classroom. | OpenAI Agents SDK |
| 11 | [CrewAI](week11-crewai) | Ship a multi-agent project where a crew of agents with different roles collaborates on real work. | CrewAI |
| 12 | [MCP & the MVP](week12-mcp-and-mvp) | Understand MCP and start your capstone MVP. | MCP · Power BI |
| 13 | [Ship It](week13-ship-it) | Capstone deployed, documented, and ready to show. | Your capstone stack |
| — | [Demo Day](demo-day) | Present your capstone to the cohort. | Your capstone stack |

Every week is 4 hours and contains the course material plus a `community_contributions/` folder holding work shared by cohort members.

## Getting started

```bash
git clone https://github.com/Wahab901278/ml-and-ai-launchpad.git
cd ml-and-ai-launchpad
```

Set up a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
```

Copy `.env.example` to `.env` and fill in your own API keys. **Never commit `.env`.**

## Contributing your work

Cohort members are encouraged to share projects. You contribute by **forking this repo and opening a pull request** that adds files to a single folder:

```
<week-folder>/community_contributions/<your-github-handle>/
```

PRs that touch anything else are rejected automatically by CI. Full instructions: [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) for the code. Course material is the author's.
