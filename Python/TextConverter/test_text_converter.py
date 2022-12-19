import unittest
from text_converter import UnicodeFileToHtmlTextConverter


class TestUnicodeFileToHtmlTextConverterTest:
    def test_foo(self):
        converter = UnicodeFileToHtmlTextConverter("foo")
        assert "foo" == converter.full_filename_with_path
