
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from src.github_client import fetch_repos

app = FastAPI(
    title="MCP GitHub Demo",
    description="Expose GitHub API via MCP",
    version="1.0.0"
)

class UserQuery(BaseModel):
    username: str

@app.post("/repos")
async def get_repositories(query: UserQuery):
    """Fetch public repos for a given GitHub username"""
    repos = await fetch_repos(query.username)
    return [{"name": r["name"], "url": r["html_url"]} for r in repos]
