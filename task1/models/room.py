from dataclasses import dataclass, field

from .student import Student


@dataclass
class Room:
    """Model to store data of rooms"""
    id: int
    name: str
    students: list[Student] = field(default_factory=list)

    def add_student(self, student: Student) -> None:
        """Add student to the students field"""
        self.students.append(student)
