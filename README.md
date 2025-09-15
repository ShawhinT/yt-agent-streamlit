---
title: YT Agent Streamlit
emoji: 🤖
colorFrom: yellow
colorTo: blue
sdk: docker
pinned: false
license: apache-2.0
short_description: Example Space for running YT agent Streamlit app.
---
# yt-agent-streamlit
Example code for creating a YouTube agent with Streamlit and hosting via Hugging Face Spaces.

## QuickStart

## Hosting on HF Space
1. Create new Space
2. Add multiple remotes

```
# In your yt-agent-streamlit directory
git remote add gh https://github.com/{your_gh_username}/yt-agent-streamlit.git
git remote add hf https://huggingface.co/spaces/{your_hr_username}/yt-agent-streamlit.git

# Push to both
git push gh
git push --force hf
```