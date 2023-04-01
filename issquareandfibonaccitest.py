import maths_fun
import io
import sys

def testisquare_and_fibonacci():

    sys.stdin = io.StringIO("5\n")
    assert ('5 is not a square number') == maths_fun.issquare_and_fibonacci()

    sys.stdin = io.StringIO("81\n")
    assert ('81 is a square number but not in the Fibonacci sequence') == maths_fun.issquare_and_fibonacci()

    sys.stdin = io.StringIO("144\n")
    assert ('144 is a square number and in the Fibonacci sequence') == maths_fun.issquare_and_fibonacci()

    sys.stdin = io.StringIO("-213\n")
    assert ('-213 is not a valid input') == maths_fun.issquare_and_fibonacci()

if __name__ == '__main__':
    testisquare_and_fibonacci()