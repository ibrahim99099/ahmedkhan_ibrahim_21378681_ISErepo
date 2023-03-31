import maths_fun

def testfibonacciseq():
    with open("is_int.txt", mode = "w") as file:
        file.write("20\n-27\n9\n3\n13\n41")
    fib_numbers,non_fib_numbers = maths_fun.fibonacciseq("is_int.txt")
    assert ([3,13],[20,-27,9,41]) == (fib_numbers,non_fib_numbers)


    with open("emptyfile.txt",mode = "w") as file:
        file.write("")
    fib_numbers,non_fib_numbers = maths_fun.fibonacciseq("emptyfile.txt")
    assert ([],[]) == (fib_numbers,non_fib_numbers)

if __name__ == '__main__':
    testfibonacciseq()