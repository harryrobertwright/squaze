import random
from dataclasses import asdict
from dataclasses import astuple
from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int

    def as_dict(self) -> dict[str, int]:
        return asdict(self)

    def as_tuple(self) -> tuple[int, int]:
        return astuple(self)

    @classmethod
    def random(cls) -> "Coordinates":
        return Coordinates(random.randrange(0, 1000, 5), random.randrange(0, 750, 5))
