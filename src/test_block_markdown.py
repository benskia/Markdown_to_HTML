import unittest

from block_markdown import markdown_to_blocks


class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        input = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        output = [
            """This is **bolded** paragraph""",
            """This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line""",
            """* This is a list
* with items""",
        ]
        self.assertListEqual(markdown_to_blocks(input), output)

    def test_markdown_to_blocks_many_newlines(self):
        input = """This is **bolded** paragraph



This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line



* This is a list
* with items"""
        output = [
            """This is **bolded** paragraph""",
            """This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line""",
            """* This is a list
* with items""",
        ]
        self.assertListEqual(markdown_to_blocks(input), output)
