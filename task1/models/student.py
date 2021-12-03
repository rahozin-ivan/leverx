from dataclasses import dataclass


@dataclass
class Student:
    """Model to store data of students"""
    id: int
    name: str

    def __init__(self, data_dict: dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
