import os
import logging
from concurrent.futures import ThreadPoolExecutor

REPO_URL = "https://github.com/microsoft/multi-agent-reference-architecture"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "docs"))

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def format_title(filename: str) -> str:
    base = os.path.splitext(filename)[0]
    return base.replace("-", " ").replace("_", " ").title()


def add_or_update_github_discussions_button(
    file: str, abs_file_path: str, content: str
):
    rel_file_path = os.path.relpath(abs_file_path, os.path.dirname(DOCS_DIR)).replace(
        "\\", "/"
    )

    title = format_title(file)

    github_button_header = '\n\n---\n\n<a class="github-button"'
    new_snippet = (
        f'{github_button_header} '
        f'href="{REPO_URL}/discussions/new?category=q-a&body=Source: [{title}]({REPO_URL}/blob/main/{rel_file_path})" '
        f'data-icon="octicon-comment-discussion" target="_blank" data-size="large" '
        f'aria-label="Discuss buttons/github-buttons on GitHub">Discuss this page</a>\n\n'
        f'<script async defer src="https://buttons.github.io/buttons.js"></script>\n'
    ).strip()

    idx = content.rfind(github_button_header)

    if idx == -1:
        with open(abs_file_path, "a", encoding="utf-8") as f:
            _ = f.write("\n" + new_snippet + "\n")
        logging.info(f"🆕 Discussions button added to {rel_file_path}")
        return

    old_snippet = content[idx:].strip()

    if old_snippet == new_snippet:
        logging.info(
            f"✅ Discussions button already present and up to date in {rel_file_path}"
        )
        return

    new_content = content[:idx].rstrip() + "\n\n" + new_snippet

    with open(abs_file_path, "w", encoding="utf-8") as f:
        _ = f.write(new_content)

    logging.info(f"🔄 Discussions button replaced in {rel_file_path}")


def process_single_md_file(item: tuple[str, str]):
    directory, file = item
    abs_file_path = os.path.join(directory, file)

    with open(abs_file_path, encoding="utf-8") as f:
        content = f.read()

    add_or_update_github_discussions_button(
        file=file,
        abs_file_path=abs_file_path,
        content=content,
    )


def process_md_files(max_workers: int = 8):
    md_files: list[tuple[str, str]] = [
        (root, file)
        for root, _, files in os.walk(DOCS_DIR)
        for file in files
        if file.endswith(".md")
    ]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        _ = executor.map(process_single_md_file, md_files)


if __name__ == "__main__":
    process_md_files()
