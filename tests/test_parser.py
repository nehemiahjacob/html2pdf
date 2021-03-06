import unittest
from xhtml2pdf.parser import pisaParser
from xhtml2pdf.context import PisaContext

_data = b"""
<!doctype html>
<html>
<title>TITLE</title>
<body>
BODY
</body>
</html>
"""


class TestCase(unittest.TestCase):

    def testParser(self):
        c = PisaContext(".")
        r = pisaParser(_data, c)
        self.assertEqual(c, r)

    def test_getFile(self):
        c = PisaContext(".")
        r = pisaParser(_data, c)
        self.assertEqual(c.get_file(None), None)

    def test_height_as_list(self):
        """Asserts attributes like 'height: 10px !important" are parsed"""
        c = PisaContext(".")
        data = b"<p style='height: 10px !important;width: 10px !important'>test</p>"
        r = pisaParser(data, c)
        self.assertEqual(c, r)


def buildTestSuite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)


def main():
    buildTestSuite()
    unittest.main()

if __name__ == "__main__":
    main()
