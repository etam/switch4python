A switch "statement" for Python.

    x = 5

    with switch(x) as case:
        if case(4):
            assert False
        if case(5):
            assert True
            case.fallthrough()
        if case(lambda x: x > 3):
            assert True
        if case(6):
            assert False
        if case.default():
            assert False

Tests and usage in test.py.
