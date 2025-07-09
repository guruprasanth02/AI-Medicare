# 🧠 AI Medicare – A Multi-Agent AI Governance System

AI Medicare is an AI-powered web application built for the GenAI Hackathon. It leverages LLMs and moderation pipelines to provide medically guided responses while enforcing responsible AI governance. The system includes user-role based access control, moderation filters, and audit logging.

---

## 🔧 Features

- 🌐 Web-based interface using Flask
- 🧑‍⚕️ Role-based access: Admin, Analyst, User
- 🧠 LLM integration via Together AI (LLaMA 3 - 8B Chat)
- 🛡️ Toxicity detection using `unitary/toxic-bert`
- 📊 Dataset preview for authorized users (Admin only)
- 🗂️ Logging and feedback collection
- ✅ Keyword-based guardrails and policy enforcement
- 🔍 Analyst dashboard with pagination and insights
