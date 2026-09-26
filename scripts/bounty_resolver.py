import os
import re

def update_readme_status_meter(readme_path="README.md"):
    """
    Injects a dynamic status meter/counter into the README.md file.
    Uses Shields.io badge formatting for a professional look and high visibility.
    """
    badge_url = "https://img.shields.io/badge/status-active-brightgreen.svg"
    counter_url = "https://img.shields.io/badge/bounties_claimed-0-blue.svg"
    
    # Target insertion point (after the first header)
    insertion_text = f"\n![Status]({badge_url}) ![Claims]({counter_url})\n"
    
    try:
        with open(readme_path, 'r+', encoding='utf-8') as f:
            content = f.read()
            
            # Prevent duplicate injection
            if "img.shields.io" in content:
                print("Status meter already exists.")
                return

            # Find the first header (line starting with #) to place badge after
            match = re.search(r'^#\s.*$', content, re.MULTILINE)
            if match:
                pos = match.end()
                new_content = content[:pos] + insertion_text + content[pos:]
                f.seek(0)
                f.write(new_content)
                f.truncate()
                print("Successfully injected status meter into README.md")
            else:
                print("Could not locate main header in README.md")
                
    except FileNotFoundError:
        print(f"Error: {readme_path} not found.")

if __name__ == "__main__":
    update_readme_status_meter()