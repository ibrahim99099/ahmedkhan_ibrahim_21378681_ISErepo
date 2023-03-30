import maths_fun

def testisint():
    try:
        actual = maths_fun.is_integer('2137')
        assert actual == True

    except ValueError:
        pass

    try:
        actual = maths_fun.is_integer('isnkn')
        assert actual == False

    except ValueError:
        pass

if __name__ == '__main__':
    testisint()
