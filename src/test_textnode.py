import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.PLAIN, url = None)
        node2 = TextNode("This is a text node", TextType.PLAIN)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.IMAGE, url = "http://example.com/image.png")
        node2 = TextNode("This is a text node", TextType.IMAGE, url = "http://example.com/image.png")
        self.assertEqual(node, node2)

    def test_neq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_neq2(self):
        node = TextNode("This is a text node", TextType.IMAGE, url = "http://example.com/image.png")
        node2 = TextNode("This is a text node", TextType.IMAGE, url = "http://example.com/image2.png")
        self.assertNotEqual(node, node2)

    def test_neq3(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a italic text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()