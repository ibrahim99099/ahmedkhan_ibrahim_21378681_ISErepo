import sys
import io
import maths_fun

def testissquare():
    sys.stdin = io.StringIO("25\n")
    assert True == maths_fun.issquare()

    sys.stdin = io.StringIO("80\n")
    assert False == maths_fun.issquare()


if __name__ == '__main__':
    testissquare()