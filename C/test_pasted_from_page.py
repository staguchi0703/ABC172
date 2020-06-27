from resolve import resolve 
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 4 240
60 90 120
80 150 80 150"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4 730
60 90 120
80 150 80 150"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 4 1
1000000000 1000000000 1000000000 1000000000 1000000000
1000000000 1000000000 1000000000 1000000000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
