__all__ = ['switch']


from contextlib import contextmanager


class Switch:
    def __init__(self, value):
        self.value    = value
        self.finished = False

    def case(self, cond):
        if self.finished:
            return False

        match = False

        if hasattr(cond, '__call__'):
            if cond(self.value):
                match = True
        elif cond == self.value:
            match = True

        if match:
            self.finished = True

        return match

    def fallthrough(self):
        self.finished = False

    def default(self):
        return not self.finished

@contextmanager
def switch(value):
    the_switch = Switch(value)
    yield the_switch
