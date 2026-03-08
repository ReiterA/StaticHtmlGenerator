import unittest

from block_markdown import *


class TestBlockMarkdown(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        # Test heading
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

        # Test unordered list
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)

        # Test ordered list
        self.assertEqual(block_to_block_type("1. Item 1\n2. Item 2"), BlockType.ORDERED_LIST)

        # Test quote
        self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)

        # Test code
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.CODE)

        # Test paragraph
        self.assertEqual(block_to_block_type("Paragraph"), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()