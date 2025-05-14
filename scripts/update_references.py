import os
import re

# Directory containing your Markdown files
markdown_dir = r"c:\\Repos\\csu-devsquad\\multi-agent-reference-architecture"

# Regex to match Markdown links
link_regex = r'\[.*?\]\((https?://.*?)\)'

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
    print(f"Extracting links from: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return re.findall(link_regex, content)

def update_references():
    # Extract existing links from the References.md file
    existing_links = set()
    if os.path.exists(output_file):
        existing_links.update(extract_links_from_file(output_file))
        print (f"Existing links: {existing_links}")

    # Extract new links from all Markdown files
    new_links = set()
    for root, _, files in os.walk(markdown_dir):
        for file in files:
            if file.endswith('.md') and file.lower() not in ignored_files:
                print (f"Checking if {file} is not in ignored list")
                file_path = os.path.join(root, file)
                new_links.update(extract_links_from_file(file_path))
                print (f"New links: {new_links}")
    
    # Combine existing and new links
    all_links = existing_links.union(new_links)
    
    # Append new links to the References.md file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("# References\n\n")
        file.write("<!-- GENERATED FILE DO NOT CHANGE -->\n\n")
        file.write("## Microsoft\n\n")
        for link in sorted(all_links):
            if "microsoft" in link.lower() or "azure" in link.lower():
                file.write(f"- {link}\n")
        
        file.write("\n## Open AI\n\n")
        for link in sorted(all_links):
            if "openai" in link.lower():
                file.write(f"- {link}\n")
        
        file.write("\n## Other\n\n")
        for link in sorted(all_links):
            if "microsoft" not in link.lower() and "openai" not in link.lower():
                file.write(f"- {link}\n")
    
    print(f"References updated in {output_file}")

if __name__ == "__main__":
    update_references()