from mysql.connector import connect

from queries import tables, queries
from serializers import XMLSerializer, JSONSerializer
from console_parser import ConsoleParser
from json_parser import JSONParser
from dbmanager import DBManager
from output import output


def main():
    formats = {"xml": XMLSerializer, "json": JSONSerializer}

    console_parser = ConsoleParser(formats)
    console_parser.read_console_args()

    room_list = JSONParser.parse_file(console_parser.args.rooms)
    student_list = JSONParser.parse_file(console_parser.args.students)
    dbmanager = DBManager(config=console_parser.args.db_config, tables=tables)

    with connect(**dbmanager.config) as db_connection:
        dbmanager.create_tables(db_connection)
        dbmanager.fill_table(db_connection, 'rooms', room_list)
        dbmanager.fill_table(db_connection, 'students', student_list)
        dbmanager.add_index(db_connection, 'birth', 'students', 'birthday')
        for k, v in queries.items():
            data = dbmanager.execute_query(db_connection, v)
            text = console_parser.args.serializer.serialize(data)
            output(text, k, console_parser.args.format)


if __name__ == '__main__':
    main()

