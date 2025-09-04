
import httpx
import os

GITHUB_API = "https://api.github.com"

# Use a GitHub PAT (Personal Access Token) for higher rate limits
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

async def fetch_repos(username: str):
    url = f"{GITHUB_API}/users/{username}/repos"
    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers)
        r.raise_for_status()
        return r.json()
