import os
from pathlib import Path

import streamlit as st
from openai import OpenAI

from scripts.ask import INDEX_PATH, META_PATH, MODEL, SYSTEM_PROMPT, retrieve

REPO_URL = "https://github.com/ferryhe/IAA_AI_Knowledge_Base"
DOCS_DIR = Path(__file__).resolve().parent.parent / "Knowledge_Base_MarkDown"
PREVIEW_CHAR_LIMIT = 4000


st.set_page_config(page_title="IAA Knowledge Base Q&A", layout="wide")
st.title("IAA Knowledge Base Q&A")

st.caption("Grounded Q&A over the Markdown corpus published in the public repository.")

has_api_key = bool(os.getenv("OPENAI_API_KEY"))
artifacts_ready = INDEX_PATH.exists() and META_PATH.exists()

if not has_api_key:
    st.warning("Set `OPENAI_API_KEY` in `AI_Agent/.env` before issuing queries.")
if not artifacts_ready:
    st.warning("Vector index not found. Run `make index` (or `python scripts/build_index.py`) first.")


def load_markdown_catalog():
    if not DOCS_DIR.exists():
        return []
    return sorted(DOCS_DIR.rglob("*.md"))


def read_preview_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if len(text) <= PREVIEW_CHAR_LIMIT:
        return text
    return f"{text[:PREVIEW_CHAR_LIMIT]}\n...\n(Preview truncated to {PREVIEW_CHAR_LIMIT:,} characters.)"


md_files = load_markdown_catalog()
relative_paths = [str(path.relative_to(DOCS_DIR)) for path in md_files]

with st.sidebar:
    st.header("Markdown Library")
    st.caption(f"Source: [{REPO_URL}]({REPO_URL})")
    st.text(f"{len(md_files)} files indexed")
    filter_term = st.text_input("Filter files", placeholder="Type keywords", label_visibility="collapsed")

    filtered_options = relative_paths
    if filter_term:
        lowered = filter_term.lower()
        filtered_options = [path for path in relative_paths if lowered in path.lower()]

    if not filtered_options:
        st.info("No files match the current filter.")
        selected_file = None
    else:
        selected_label = st.selectbox(
            "Select a Markdown file", filtered_options, label_visibility="collapsed"
        )
        selected_file = md_files[relative_paths.index(selected_label)]
        github_blob = f"{REPO_URL}/blob/main/Knowledge_Base_MarkDown/{selected_label.replace(os.sep, '/')}"
        st.markdown(f"[Open in GitHub]({github_blob})")
        with st.expander("Preview", expanded=False):
            st.code(read_preview_text(selected_file), language="markdown")

st.subheader("How to use this agent")
st.markdown(
    """
1. Browse the Markdown files in the sidebar to understand available context.
2. Ask focused questions about the repository content using the form below.
3. Review answers with citations and inspect retrieved snippets for verification.
"""
)
st.divider()

st.subheader("Ask the Knowledge Base")
st.caption(
    f"All responses are grounded in `Knowledge_Base_MarkDown/` from [{REPO_URL}]({REPO_URL})."
)

with st.form("ask_form", clear_on_submit=True):
    question = st.text_area(
        "Question",
        placeholder="e.g., Summarize the July 2025 AI governance consultation draft",
    )
    ask_button = st.form_submit_button(
        "Ask", use_container_width=True, disabled=not (has_api_key and artifacts_ready)
    )

if "history" not in st.session_state:
    st.session_state.history = []

if ask_button:
    if not question.strip():
        st.warning("Please enter a question before submitting.")
    else:
        try:
            with st.spinner("Retrieving and generating answer..."):
                client = OpenAI()
                hits = retrieve(client, question)
                context = "\n\n".join(f"[{i+1}] {hit['path']}\n{hit['text']}" for i, hit in enumerate(hits))
                messages = [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": f"Retrieved snippets:\n{context}\n\nQuestion: {question}",
                    },
                ]
                response = client.chat.completions.create(model=MODEL, messages=messages, temperature=0.2)
                answer = response.choices[0].message.content
                st.session_state.history.insert(0, {"question": question, "answer": answer, "hits": hits})
        except FileNotFoundError as err:
            st.error(f"{err}")
        except Exception as err:  # noqa: BLE001 - surface user-friendly error
            st.error(f"Unable to generate an answer: {err}")

st.divider()
st.subheader("Conversation history")

if not st.session_state.history:
    st.info("No questions yet. Submit one to start building the conversation timeline.")
else:
    for entry in st.session_state.history:
        st.markdown(f"### Q: {entry['question']}")
        st.markdown(entry["answer"])
        with st.expander("Retrieved snippets"):
            for i, hit in enumerate(entry["hits"], start=1):
                st.markdown(f"**[{i}] {hit['path']}**")
                st.code(hit["text"], language="markdown")
