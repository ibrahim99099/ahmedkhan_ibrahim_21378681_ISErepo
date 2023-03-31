import maths_fun

def testfibonacciseq():
    with open("is_int.txt", mode = "w") as inputfile:
        inputfile.write("21\n31\n8\n4\n13\n41")
        assert "Fibonacci numbers: [8, 13]/nNon-Fibonacci numbers: [22, 31, 4, 41]" == maths_fun.fibonacciseq("is_int.txt")
        