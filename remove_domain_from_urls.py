import os
import re
from pathlib import Path

def remove_domain_from_urls(content):
    # First handle Markdown image syntax with dimensions
    markdown_pattern = r'\[!\[\]\((http://shevchenko4a\.brovary\.org/wp-content/uploads/\d{4}/\d{2}/[^)\s]+?)-\d+x\d+(\.[^)]+)\)\]\((http://shevchenko4a\.brovary\.org/wp-content/uploads/\d{4}/\d{2}/[^)\s]+?)(?:-\d+x\d+)?(\.[^)]+)\)'
    
    def replace_markdown(match):
        path = match.group(1) + match.group(2)
        path = path.replace('http://shevchenko4a.brovary.org', '')
        return f'[![]({path})]({path})'
    
    content = re.sub(markdown_pattern, replace_markdown, content)
    
    # Then handle direct URLs
    url_pattern = r'http://shevchenko4a\.brovary\.org(/wp-content/uploads/\d{4}/\d{2}/[^"\s]+?)-\d+x\d+(\.[^"\s]+)'
    
    def replace_url(match):
        return match.group(1) + match.group(2)
    
    content = re.sub(url_pattern, replace_url, content)
    
    # Finally handle any remaining domain references
    domain_pattern = r'http://shevchenko4a\.brovary\.org(/wp-content/uploads/[^"\s]+)'
    
    def replace_domain(match):
        return match.group(1)
    
    return re.sub(domain_pattern, replace_domain, content)

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