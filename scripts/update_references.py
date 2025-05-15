import os
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Directory containing your Markdown files
markdown_dir = os.path.join(os.path.dirname(__file__), "..")

# Regex to match Markdown links
link_regex = r'\[.*?\]\((https?://[^\s)]+)\)'

# Ignore file list
ignored_files = [
    "readme.md",
    "references.md",
    "summary.md",
    "contributing.md",
    "code_of_conduct.md",
    "license",
    "security.md",
    "contributors.md",
    "support.md"
]

# File to store the updated reference list
output_file = os.path.join(markdown_dir, "docs", "References.md")

def extract_links_from_file(file_path):
    if not os.path.exists(file_path):
        logging.warning(f"File not found: {file_path}")
        return []
    
    logging.info(f"Extracting links from: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return re.findall(link_regex, content)

def update_references():
    # Extract existing links from the References.md file
    referenced_links = set()
    if os.path.exists(output_file):
        referenced_links.update(extract_links_from_file(output_file))
        logging.info(f"Referenced links: {referenced_links}")
    
    if not referenced_links:
        logging.warning("No referenced links found in the References.md file.")
        return


    # Extract new links from all Markdown files
    md_links = set()
    for root, _, files in os.walk(markdown_dir):
        for file in files:
            if file.endswith('.md') and file.lower() not in ignored_files:
                logging.info(f"Processing file: {file}")
                file_links = set()
                file_links = extract_links_from_file(os.path.join(root, file))
                logging.info(f"Links on file: {file_links}")
                md_links.update(file_links)
    logging.info(f"Total links identified: {md_links}")
    logging.info(f"Referenced links: {referenced_links}")
    logging.info(f"New links: {md_links - referenced_links}")
    return

    # extract only the new links
    new_links = md_links - referenced_links
    
    if new_links:
        logging.info(f"New links identified: {new_links}")
        # Append new links to the References.md file
        with open(output_file, 'a', encoding='utf-8') as file:
            file.write("# References\n\n")
            file.write("<!-- LINKS IDENTIFIED -->\n\n")
            file.write("## Microsoft\n\n")
            for link in sorted(new_links):
                if "microsoft" in link.lower() or "azure" in link.lower():
                    file.write(f"- {link}\n")
            
            file.write("\n## Open AI\n\n")
            for link in sorted(new_links):
                if "openai" in link.lower():
                    file.write(f"- {link}\n")
            
            file.write("\n## Other\n\n")
            for link in sorted(new_links):
                if "microsoft" not in link.lower() and "openai" not in link.lower():
                    file.write(f"- {link}\n")
        
        logging.info(f"References updated in {output_file}")
    else:
        logging.info("No new links identified. References are up-to-date.")

if __name__ == "__main__":
    update_references()