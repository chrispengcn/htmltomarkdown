# HTML to Markdown Converter

A Python tool that converts HTML code within Markdown files to proper Markdown format while preserving front-matter sections. The tool automatically fixes HTML syntax errors before conversion.

## Features

- Converts HTML tags in Markdown content to equivalent Markdown formatting
- Preserves front-matter sections unchanged
- Automatically fixes HTML syntax errors (unclosed tags, incorrect nesting, etc.)
- Processes entire directory structures recursively
- Copies non-Markdown files unchanged to target directory
- Maintains original directory structure in output

## Dependencies

- python-frontmatter: For handling front-matter sections
- markdownify: For converting HTML to Markdown
- beautifulsoup4: For fixing HTML syntax errors
- lxml: Parser for BeautifulSoup

## Installation

Install required dependencies using pip:
pip install python-frontmatter markdownify beautifulsoup4 lxml
## Usage

Run the script from the command line, specifying source and target directories:
python3 html2markdown.py --sourcedir /path/to/source --targetdir /path/to/target
- `--sourcedir`: Path to the directory containing your original Markdown files
- `--targetdir`: Path to the directory where converted files will be saved

## How It Works

1. The program reads each Markdown file in the source directory
2. It separates and preserves any front-matter section
3. For the main content:
   - First fixes any HTML syntax errors using BeautifulSoup
   - Converts the cleaned HTML to proper Markdown format
4. Saves the processed file to the target directory, maintaining the original directory structure
5. Copies non-Markdown files directly to the target directory

## Notes

- The conversion quality depends on the complexity of the HTML and markdownify's ability to convert it
- Most common HTML tags (headings, lists, links, images, etc.) convert well
- The program will overwrite existing files in the target directory with the same name
- Directory structures from the source are replicated in the target directory

## License

This project is released under the MIT License.
    
