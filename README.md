# yt-agent-streamlit
Example code for creating a YouTube agent with Streamlit and hosting via Hugging Face Spaces.

## How to Run This Example

1. Clone this repo

    ```
    git clone https://github.com/ShawhinT/yt-agent-streamlit.git
    ```
2. Open repo directory

    ```
    cd yt-agent-streamlit
    ```
3. Install dependencies

    ```
    uv sync
    ```
4. Run Streamlit app

    ```
    uv run streamlit run main.py
    ```

## Hosting on HF Space

1. [Create new](https://huggingface.co/new-space) Hugging Face Space

    ```
    Name: yt-agent-streamlit
    Description: Example Space for running YT agent Streamlit app.
    Space SDK: Docker
    Docker Template: Blank
    Space Hardware: CPU
    ```
2. Add multiple remotes to git repo

    ```
    # In your yt-agent-streamlit directory
    git remote add hf https://huggingface.co/spaces/{your_hr_username}/yt-agent-streamlit.git
    git remote add gh https://github.com/{your_gh_username}/yt-agent-streamlit.git
    ```
3. Push code to HF spaces (force only needed on first push)

    ```
    git push --force hf
    ```
4. Push code to github

    ```
    git push gh
    ```

---
title: YT Agent Streamlit
emoji: 🤖
colorFrom: yellow
colorTo: blue
sdk: docker
app_port: 8501
tags:
  - streamlit
pinned: false
license: apache-2.0
short_description: Example Space for running YT agent Streamlit app.
---