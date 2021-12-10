def move_students_to_rooms(rooms: list, students: list) -> None:
    for student in students:
        rooms[student.room].add_student(student)
