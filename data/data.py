from dataclasses import dataclass


@dataclass
class Contact:
    first_name: str = None
    last_name: str = None
    title: str = None
    email: str = None
    note: str = None
