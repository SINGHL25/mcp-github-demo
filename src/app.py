
import streamlit as st
import httpx

st.title("🔍 MCP GitHub Demo - Streamlit Client")

BASE_URL = "http://127.0.0.1:8000"  # your FastAPI server

username = st.text_input("Enter GitHub username", "torvalds")

if st.button("Fetch Repos"):
    try:
        with httpx.Client() as client:
            r = client.post(f"{BASE_URL}/repos", json={"username": username})
            r.raise_for_status()
            repos = r.json()
            st.success(f"Found {len(repos)} repos for {username}")
            for repo in repos:
                st.write(f"- [{repo['name']}]({repo['url']})")
    except Exception as e:
        st.error(str(e))
