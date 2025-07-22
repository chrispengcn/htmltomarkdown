import argparse
import frontmatter
import markdownify
from pathlib import Path
import shutil
from bs4 import BeautifulSoup  # For fixing HTML syntax errors

def fix_html_syntax(html_content):
    """Fix syntax errors in HTML content"""
    # Use BeautifulSoup's repair capabilities; lxml parser has good fault tolerance
    # For serious errors, BeautifulSoup will try to repair and preserve usable content
    soup = BeautifulSoup(html_content, 'lxml')
    # Return the fixed HTML
    return str(soup)

def convert_html_to_markdown(content):
    """Convert HTML in content to Markdown, first fixing syntax errors"""
    # First fix HTML syntax errors
    fixed_html = fix_html_syntax(content)
    # Then convert to Markdown
    return markdownify.markdownify(fixed_html, heading_style="ATX")

def process_file(source_path, target_path):
    """Process a single file: preserve front-matter, convert HTML in content"""
    # Read the file
    post = frontmatter.load(source_path)
    
    # Convert HTML in content
    if post.content:
        post.content = convert_html_to_markdown(post.content)
    
    # Ensure target directory exists
    target_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the converted file
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))

def process_directory(source_dir, target_dir):
    """Process all files in the directory"""
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    # Ensure source directory exists
    if not source_path.exists():
        print(f"Error: Source directory does not exist - {source_dir}")
        return
    
    # Create target directory if it doesn't exist
    target_path.mkdir(parents=True, exist_ok=True)
    
    # Traverse all files and subdirectories in the source directory
    for item in source_path.rglob('*'):
        # Calculate relative path
        relative_path = item.relative_to(source_path)
        target_item = target_path / relative_path
        
        if item.is_dir():
            # Create corresponding directory
            target_item.mkdir(parents=True, exist_ok=True)
        elif item.is_file() and item.suffix.lower() == '.md':
            # Process Markdown files
            print(f"Processing file: {item}")
            process_file(item, target_item)
        else:
            # Copy non-Markdown files
            shutil.copy2(item, target_item)
            print(f"Copying file: {item}")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Convert HTML code in Markdown files to Markdown format with automatic HTML syntax error repair')
    parser.add_argument('--sourcedir', required=True, help='Source file directory')
    parser.add_argument('--targetdir', required=True, help='Target file directory')
    
    args = parser.parse_args()
    
    # Process directory
    process_directory(args.sourcedir, args.targetdir)
    print("Conversion completed!")

if __name__ == "__main__":
    main()
    
