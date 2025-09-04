# mcp-github-demo

# 🚀 MCP GitHub Demo

This project shows how to build a **Model Context Protocol (MCP) server** using FastAPI that connects to the **GitHub API**. It also includes a **Streamlit client** for testing.

---

## 📌 What is MCP?
- **MCP (Model Context Protocol)** is a standard for connecting AI assistants to external tools and APIs.
- Instead of manually wiring each tool, MCP uses an **OpenAPI spec** to describe endpoints.
- Clients like **Claude, VS Code, Cursor** auto-discover these tools and call them directly.

---

## ⚙️ Features
- MCP-compatible FastAPI server
- GitHub API wrapper (list repositories)
- Streamlit client for quick testing
- Pytest integration

---

## 🛠️ Setup

```bash
git clone https://gitlab.com/<your-namespace>/mcp-github-demo.git
cd mcp-github-demo
pip install -r requirements.txt
