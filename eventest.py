import maths_fun

def testsumeven():
    try:
        actual = maths_fun.sumeven([1, 2, 3, 4, 5, 6, 9, 10])
        assert actual == 22

    except ValueError:
        pass

    try:
        actual = maths_fun.sumeven([1, 'bb', 3, '4', 5, 6, 9, 10])
        assert actual == "Error: Input must be a list of integers."

    except ValueError:
        pass

if __name__ == '__main__':
    testsumeven()



