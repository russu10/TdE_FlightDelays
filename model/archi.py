from dataclasses import dataclass

from model.airport import Airport


@dataclass
class Arco:
    a1 : int
    a2 : int
    peso : int