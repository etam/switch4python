from switch import switch

x = 5

with switch(x) as case:
    if case(4):
        assert False
    if case(5):
        assert True
        case.fallthrough()
    if case(5):
        assert True
    if case(5):
        assert False
    if case(6):
        assert False


with switch(3) as case:
    if case(lambda x: x > 5):
        assert False
    if case.default():
        assert True
