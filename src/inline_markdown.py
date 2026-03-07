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