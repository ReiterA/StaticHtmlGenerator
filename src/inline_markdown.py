import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split_texts = node.text.split(delimiter)
            if len(split_texts) % 2 == 0:
                raise Exception(f"A closing delimiter '{delimiter}' is missing")
            for i, split_text in enumerate(split_texts):
                if split_text == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_text, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_text, text_type))
                
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            matches = extract_markdown_images(node.text)
            if len(matches) > 0:
                split_texts = re.split(pattern, node.text)
                for i, split_text in enumerate(split_texts):
                    if i % 3 == 1:
                        alt_text = split_text
                    if split_text == "":
                        continue
                    if i % 3 == 0:
                        new_nodes.append(TextNode(split_text, TextType.TEXT))
                    if i % 3 == 2:
                        new_nodes.append(TextNode(alt_text, TextType.IMAGE, url=split_text))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            matches = extract_markdown_links(node.text)
            if len(matches) > 0:
                split_texts = re.split(pattern, node.text)
                for i, split_text in enumerate(split_texts):
                    if i % 3 == 1:
                        alt_text = split_text
                    if split_text == "":
                        continue
                    if i % 3 == 0:
                        new_nodes.append(TextNode(split_text, TextType.TEXT))
                    if i % 3 == 2:
                        new_nodes.append(TextNode(alt_text, TextType.LINK, url=split_text))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
                