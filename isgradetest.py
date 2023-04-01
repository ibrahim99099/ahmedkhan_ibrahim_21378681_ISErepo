import sys
import io
import maths_fun

def testgrade():
    sys.stdin = io.StringIO("-2137\n")
    assert "Invalid score" == maths_fun.grading()

    sys.stdin = io.StringIO("15\n")
    assert "You can do better" == maths_fun.grading()

    sys.stdin = io.StringIO("35\n")
    assert "Good" == maths_fun.grading()

    sys.stdin = io.StringIO("60\n")
    assert "Great" == maths_fun.grading()

    sys.stdin = io.StringIO("82\n")
    assert "Excellent" == maths_fun.grading()

    sys.stdin = io.StringIO("98\n")
    assert "Brilliant" == maths_fun.grading()

if __name__ == '__main__':
    testgrade()