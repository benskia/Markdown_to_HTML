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
    markdown_to_html_node,
)
from htmlnode import LeafNode, ParentNode


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

    def test_markdown_to_html_node(self):
        input = """
## Heading

A paragraph with **bolded** text, and
a second line with *italic* text.

A one liner with `code` in it.

* An
* Unordered
* List

1. An
2. Ordered
3. List

> And finally
> A blockquote
            """
        h2 = "<h2>Heading</h2>"
        p_multi = "<p>A paragraph with <b>bolded</b> text, and\na second line with <i>italic</i> text.</p>"
        p_single = "<p>A one liner with <code>code</code> in it.</p>"
        ulist = "<ul><li>An</li><li>Unordered</li><li>List</li></ul>"
        olist = "<ol><li>An</li><li>Ordered</li><li>List</li></ol>"
        quote = "<blockquote>And finally\nA blockquote</blockquote>"
        output = f"<div>{h2}{p_multi}{p_single}{ulist}{olist}{quote}</div>"
        self.assertEqual(markdown_to_html_node(input).to_html(), output)
