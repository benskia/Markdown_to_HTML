import unittest

from block_markdown import (
    block_to_block_type,
    markdown_to_blocks,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_ulist,
    block_type_olist,
)


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

    def test_block_type_heading(self):
        input = "### wowee"
        self.assertEqual(block_to_block_type(input), block_type_heading)

    def test_invalid_heading(self):
        input = "####### wowee"
        self.assertEqual(block_to_block_type(input), block_type_paragraph)

    def test_block_type_code(self):
        input = "```this is code```"
        self.assertEqual(block_to_block_type(input), block_type_code)

    def test_invalid_code(self):
        input = "``but is this code``"
        self.assertEqual(block_to_block_type(input), block_type_paragraph)

    def test_block_type_quote(self):
        input = "> this is a quote\n> on multiple lines\n> this is a quote"
        self.assertEqual(block_to_block_type(input), block_type_quote)

    def test_invalid_quote(self):
        input = "> the first line is valid\nbut the second line is not\n> and the third one is"
        self.assertEqual(block_to_block_type(input), block_type_paragraph)

    def test_block_type_ulist(self):
        input = "* one\n- two\n* three\n- four"
        self.assertEqual(block_to_block_type(input), block_type_ulist)

    def test_invalid_ulist(self):
        input = "* one\n- two\noops\n- four"
        self.assertEqual(block_to_block_type(input), block_type_paragraph)

    def test_block_type_olist(self):
        input = "1. one\n2. two\n3. three\n4. four"
        self.assertEqual(block_to_block_type(input), block_type_olist)

    def test_invalid_olist(self):
        input = "1. one\n5. five?\n3. three\n4. four"
        self.assertEqual(block_to_block_type(input), block_type_paragraph)
