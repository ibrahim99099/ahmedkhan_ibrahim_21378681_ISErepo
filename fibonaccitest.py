import sys
import io
import maths_fun

def setUp():
    capOut = io.StringIO()
    sys.stdout = capOut
    return capOut

def testfibonacci1():
    capOut = setUp()
    maths_fun.fibonacci(5)
    assert ("5 is in the Fibonacci sequence") == capOut.getvalue().strip()
    tearDown()

def testfibonacci2():
    capOut = setUp()
    maths_fun.fibonacci(7)
    assert ("7 is not in the Fibonacci sequence") == capOut.getvalue().strip()
    tearDown()

def testfibonacci3():
    capOut = setUp()
    maths_fun.fibonacci(0)
    assert ("0 is in the Fibonacci sequence") == capOut.getvalue().strip()
    tearDown()

def testfibonacci4():
    capOut = setUp()
    maths_fun.fibonacci(-3)
    assert ("-3 is not in the Fibonacci sequence (negative numbers are not in the sequence)") == capOut.getvalue().strip()
    tearDown()

def tearDown():
    sys.stdout = sys.__stdout__

if __name__ == "__main__":
    setUp()
    testfibonacci1()
    tearDown()
    setUp()
    testfibonacci2()
    tearDown()
    setUp()
    testfibonacci3()
    tearDown()
    setUp()
    testfibonacci4()
    tearDown()