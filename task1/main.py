from console_parser import ConsoleParser
from serializers import XMLSerializer, JSONSerializer
from json_parser import JSONParser
from models import Room, Student
from output import output
from merge_data import move_students_to_rooms
from extract_data import extract_data


def main():
    formats = {"xml": XMLSerializer, "json": JSONSerializer}

    console_parser = ConsoleParser(formats)
    console_parser.read_console_args()

    room_list = JSONParser.parse_file(console_parser.args.rooms)
    student_list = JSONParser.parse_file(console_parser.args.students)

    rooms = extract_data(room_list, Room)
    students = extract_data(student_list, Student)

    move_students_to_rooms(rooms, students)

    text = console_parser.args.serializer.serialize(rooms)

    output(text, console_parser.args.format)


if __name__ == '__main__':
    main()
