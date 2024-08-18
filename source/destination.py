from dataclasses import dataclass
import inspect

@dataclass
class Destination:
    name: str = None
    description: str = None
    url: str = None
    price: str = None
    contact_info: list = None
