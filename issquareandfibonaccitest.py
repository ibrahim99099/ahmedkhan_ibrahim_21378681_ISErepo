import maths_fun
import io
import sys

def testisquare_and_fibonacci():
    sys.stdin = io.StringIO("5\n")
    assert ('5 is not a square number') == maths_fun.issquare_and_fibonacci()

if __name__ == '__main__':
    testisquare_and_fibonacci()