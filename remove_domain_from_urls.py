import os
import re
from pathlib import Path

def remove_domain_from_urls(content):
    # Pattern to match image URLs with domain
    pattern = r'http://shevchenko4a\.brovary\.org(/wp-content/uploads/\d{4}/\d{2}/[^-\s]+(?:-\d+x\d+)?\.(?:jpg|jpeg|png|gif))'
    
    # Replace URLs with domain with relative URLs
    def replace_url(match):
        return match.group(1)
    
    return re.sub(pattern, replace_url, content)

def process_markdown_files(directory):
    for file_path in Path(directory).glob('*.md'):
        print(f"Processing {file_path}...")
        
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove domain from URLs
        new_content = remove_domain_from_urls(content)
        
        # Write back if changes were made
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_path}")

if __name__ == "__main__":
    # Process both _posts and _pages directories
    for directory in ["_posts", "_pages"]:
        print(f"\nProcessing {directory} directory...")
        process_markdown_files(directory) 