import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.TEXT, url = None)
        node2 = TextNode("This is a text node", TextType.TEXT, url = None)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.IMAGE, url = "http://example.com/image.png")
        node2 = TextNode("This is a text node", TextType.IMAGE, url = "http://example.com/image.png")
        self.assertEqual(node, node2)

    def test_neq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_neq2(self):
        node = TextNode("This is a text node", TextType.IMAGE, url = "http://example.com/image.png")
        node2 = TextNode("This is a text node", TextType.IMAGE, url = "http://example.com/image2.png")
        self.assertNotEqual(node, node2)

    def test_neq3(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a italic text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        node = TextNode("Image description", TextType.IMAGE, url = "http://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "http://example.com/image.png", "alt": "Image description"})

if __name__ == "__main__":
    unittest.main()