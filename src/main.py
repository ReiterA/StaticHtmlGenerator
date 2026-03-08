import os

from copystatic import copy_content
from textnode import TextNode, TextType
from block_markdown import markdown_to_html_node
from inline_markdown import extract_title

def main():
    copy_content("static", "public")
    generate_pages_recursive("content", "template.html", "public")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown_string = f.read()
    with open(template_path, "r") as f:
        template_string = f.read()

    html_string = markdown_to_html_node(markdown_string).to_html()
    title = extract_title(markdown_string)
    final_string = template_string.replace("{{ Content }}", html_string).replace("{{ Title }}", title if title else "Untitled Page")
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(final_string)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        if filename.endswith(".md"):
            from_path = os.path.join(dir_path_content, filename)
            dest_path = os.path.join(dest_dir_path, filename.replace(".md", ".html"))
            generate_page(from_path, template_path, dest_path)
        if os.path.isdir(os.path.join(dir_path_content, filename)):
            generate_pages_recursive(os.path.join(dir_path_content, filename), template_path, os.path.join(dest_dir_path, filename))

if __name__ == "__main__":
    main()