#!/usr/bin/env python

import doctest
import unittest

import frontmatter


class FrontmatterTest(unittest.TestCase):
    """
    Tests for parsing various kinds of content and metadata
    """

    def test_unicode_post(self):
        "Ensure unicode is parsed correctly"
        chinese = frontmatter.load('tests/chinese.txt')

        self.assertIsInstance(chinese.content, unicode)

        with self.assertRaises(UnicodeEncodeError):
            # this shouldn't work as ascii, because it's Hanzi
            chinese.content.encode('ascii')


if __name__ == "__main__":
    doctest.testfile('README.md')
    unittest.main()