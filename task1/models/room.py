from dataclasses import dataclass, asdict

from .student import Student


@dataclass
class Room:
    """Model to store data of rooms"""
    id: int
    name: str
    students: list[Student]

    def __init__(self, data_dict: dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.students = []

    def add_student(self, student: Student) -> None:
        """Add student to the students field"""
        self.students.append(student)

    def to_dict(self) -> dict:
        """Convert instance to dict"""
        return asdict(self)
