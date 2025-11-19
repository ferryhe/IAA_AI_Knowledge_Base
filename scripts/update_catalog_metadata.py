import json
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

ROOT = Path("Knowledge_Base_MarkDown")
README = Path("README.md")
ENV_PATH = Path("AI_Agent/.env")

load_dotenv(ENV_PATH)
API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    raise SystemExit("OPENAI_API_KEY missing from AI_Agent/.env")

client = OpenAI(api_key=API_KEY)


def extract_title(text: str, path: Path) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return path.stem


def build_prompt(text_sample: str) -> str:
    return (
        "You are an assistant that extracts metadata from Markdown documents. "
        "Reply with a JSON object containing two keys:\n"
        "- \"publish_date\": a short publish date if you can infer one (e.g., \"March 2022\" or \"2022-03-15\") or \"unknown\" if uncertain.\n"
        "- \"summary\": 1-2 sentences summarizing the document.\n\n"
        "Document content:\n```\n"
        f"{text_sample}\n```\n"
    )


def normalize_metadata(publish: str, summary: str) -> tuple[str, str]:
    summary_clean = summary.strip()
    if summary_clean.startswith("{") and summary_clean.endswith("}"):
        try:
            nested = json.loads(summary_clean)
        except json.JSONDecodeError:
            nested = {}
        else:
            publish = nested.get("publish_date", publish)
            summary_clean = nested.get("summary", summary_clean)
    return publish, summary_clean


def strip_code_block(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = stripped[3:]
        if stripped.startswith("json"):
            stripped = stripped[4:]
        if stripped.startswith("\n"):
            stripped = stripped[1:]
        if stripped.endswith("```"):
            stripped = stripped[: -3]
    return stripped.strip()


def query_metadata(text: str) -> dict[str, str]:
    prompt = build_prompt(text)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a metadata extractor."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,
    )
    content = response.choices[0].message.content.strip()
    content = strip_code_block(content)
    try:
        data = json.loads(content)
        publish = data.get("publish_date", "unknown")
        summary = data.get("summary", content)
    except json.JSONDecodeError:
        publish = "unknown"
        summary = content
    publish, summary = normalize_metadata(publish, summary)
    return {"publish_date": publish, "summary": summary}


def format_entry(path: Path, metadata: dict[str, str]) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    title = extract_title(text, path)
    upload = time.strftime("%Y-%m-%d", time.localtime(path.stat().st_mtime))
    lines = [
        f"- **[Title]** [{title}]({path.as_posix()})",
        f"  - **[Upload Date]** {upload}",
        f"  - **[Publish Date]** {metadata['publish_date']}",
        f"  - **[Summary]** {metadata['summary']}",
    ]
    return "\n".join(lines)


def rebuild_readme(entries: list[str]) -> None:
    text = README.read_text(encoding="utf-8")
    start = text.index("## Catalog")
    end = text.find("\n\n---", start)
    if end == -1:
        end = len(text)
        suffix = ""
    else:
        suffix = text[end:]
    prefix = text[:start]
    catalog_block = "## Catalog\n\n" + "\n\n".join(entries) + "\n\n"
    README.write_text(prefix + catalog_block + suffix, encoding="utf-8")


def main():
    entries = []
    docs = sorted(ROOT.rglob("*.md"))
    total = len(docs)
    for idx, md in enumerate(docs, start=1):
        print(f"[{idx}/{total}] processing {md.name} ...")
        raw = md.read_text(encoding="utf-8", errors="ignore")
        snippet = raw[:4000]
        metadata = query_metadata(snippet)
        entries.append(format_entry(md, metadata))
        time.sleep(0.8)
    rebuild_readme(entries)
    print("README catalog updated with OpenAI metadata.")


if __name__ == "__main__":
    main()
