import os
import re
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Directory containing your Markdown files
markdown_dir = os.path.join(os.path.dirname(__file__), "..")

# Regex to match Markdown links and extract description and URL
link_regex = r"\[(.*?)\]\((https?://[^\s)]+)\)"

# Ignore file list
ignored_files = [
    "references.md",
    "summary.md",
    "contributing.md",
    "code_of_conduct.md",
    "license",
    "security.md",
    "contributors.md",
    "support.md",
]

ignored_links = [
    "https://buttons.github.io/buttons.js",
    "https://img.shields.io/github/stars/microsoft/multi-agent-reference-architecture?style=social"
]

# File to store the updated reference list
output_file = os.path.join(markdown_dir, "docs", "References.md")


def extract_links_from_file(file_path):
    """Extract links and their descriptions from a Markdown file."""
    if not os.path.exists(file_path):
        logging.warning(f"File not found: {file_path}")
        return {}

    logging.info(f"Extracting links from: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

        for ignored_link in ignored_links:
            if ignored_link in content:
                return {}

        matches = re.findall(link_regex, content)
        return {url: description for description, url in matches}


def update_references():
    """Update the References.md file with new links and descriptions."""
    # Extract existing links from the References.md file
    existing_links = {}
    if os.path.exists(output_file):
        existing_links.update(extract_links_from_file(output_file))
        logging.info(f"Found {len(existing_links)} new links:")
        for url, description in existing_links.items():
            logging.info(f"- {description}: {url}")

    # Extract new links from all Markdown files
    new_links = {}
    for root, _, files in os.walk(markdown_dir):
        for file in files:
            if file.endswith(".md") and file.lower() not in ignored_files:
                file_path = os.path.join(root, file)
                file_links = extract_links_from_file(file_path)
                for url, description in file_links.items():
                    if url not in existing_links:
                        new_links[url] = description

    if len(new_links) == 0:
        logging.info("No new links identified. References are up-to-date.")
        return

    logging.info(f"Found {len(new_links)} new links:")
    for url, description in new_links.items():
        logging.info(f"- {description}: {url}")

    # Write the updated links to the References.md file
    with open(output_file, "a", encoding="utf-8") as file:

        def write_section(file, title, links):
            file.write(f"\n## {title}\n\n")
            for url, description in sorted(links.items()):
                file.write(f"- [{description}]({url})\n")

        write_section(file, "New Links identified", new_links)

    logging.info(f"References updated in {output_file}")


if __name__ == "__main__":
    update_references()
