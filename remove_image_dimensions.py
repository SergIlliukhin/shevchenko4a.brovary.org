import os
import re
from pathlib import Path

def remove_dimensions_from_urls(content):
    # Pattern to match image URLs with dimensions
    pattern = r'(http://shevchenko4a\.brovary\.org/wp-content/uploads/\d{4}/\d{2}/[^-\s]+)-\d+x\d+\.(jpg|jpeg|png|gif)'
    
    # Replace URLs with dimensions with clean URLs
    def replace_url(match):
        base_url = match.group(1)
        extension = match.group(2)
        return f"{base_url}.{extension}"
    
    return re.sub(pattern, replace_url, content)

def process_markdown_files(directory):
    for file_path in Path(directory).glob('*.md'):
        print(f"Processing {file_path}...")
        
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove dimensions from URLs
        new_content = remove_dimensions_from_urls(content)
        
        # Write back if changes were made
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_path}")

if __name__ == "__main__":
    posts_dir = "_posts"
    process_markdown_files(posts_dir) 