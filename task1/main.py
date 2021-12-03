from console_parser import ConsoleParser
from serializers import XMLSerializer, JSONSerializer
from json_parser import JSONParser
from models import Room, Student
from output import output


def main():
    formats = {"xml": XMLSerializer, "json": JSONSerializer}

    console_parser = ConsoleParser(formats)
    console_parser.read_console_args()

    room_list = JSONParser.parse_file(console_parser.args.r)
    student_list = JSONParser.parse_file(console_parser.args.s)

    rooms = []
    for room in room_list:
        rooms.append(Room(room))

    for student in student_list:
        rooms[student['room']].add_student(Student(student))

    rooms = [room.to_dict() for room in rooms]
    text = console_parser.args.serializer.serialize(rooms)

    output(text, console_parser.args.f)


if __name__ == '__main__':
    main()
