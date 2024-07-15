from dataclasses import dataclass

@dataclass
class Stato():
    id: str
    Name: str
    Capital: str
    Lat: float
    Lng: float
    Area: int
    Population: int
    Neighbors: str

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return self.Name