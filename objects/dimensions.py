import random
from dataclasses import astuple
from dataclasses import dataclass


@dataclass
class Dimensions:
    width: int
    height: int

    def as_tuple(self) -> tuple[int, int]:
        return astuple(self)

    @classmethod
    def random(cls) -> "Dimensions":
        return cls(random.randrange(25, 100, 5), random.randrange(25, 100, 5))
