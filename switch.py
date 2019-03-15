__all__ = ['switch']


from contextlib import contextmanager
from typing import (
    cast,
    Callable,
    Generator,
    Generic,
    TypeVar,
    Union,
)


T = TypeVar('T')
GuardT = Callable[[T], bool]


class Case(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.finished = False

    def __call__(self, cond: Union[T, GuardT]) -> bool:
        if (self.finished
                or (hasattr(cond, '__call__')
                    and not cast(GuardT, cond)(self.value))
                or cond != self.value):
            return False

        self.finished = True
        return True

    def fallthrough(self) -> None:
        self.finished = False

    def default(self) -> bool:
        return not self.finished


@contextmanager
def switch(value: T) -> Generator[Case[T], None, None]:
    yield Case(value)
