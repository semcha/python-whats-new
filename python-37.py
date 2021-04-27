from dataclasses import dataclass


# PEP 557 -- Data Classes
## https://realpython.com/python-data-classes/
@dataclass
class Position:
    name: str
    lon: float
    lat: float = 0.0


pos = Position("Oslo", 10.8, 59.9)
print(pos)
print(f"{pos.name} is at {pos.lat}°N, {pos.lon}°E")


@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""

    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


new_item = InventoryItem("Red Hammer", 4.59, 10)
total_cost = new_item.total_cost()
print(new_item)
print(total_cost)
