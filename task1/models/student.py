from dataclasses import dataclass


@dataclass
class Student:
    """Model to store data of students"""
    id: int
    name: str
    room: int
