class DBManager:
    def __init__(self, config: dict, tables: dict):
        self.config = config
        self.tables = tables

    def create_tables(self, db_connection):
        with db_connection.cursor() as cur:
            for table in self.tables.values():
                cur.execute(table)

    def fill_table(self, db_connection, table_name: str, data: list):
        """Fill table with provided data"""
        if table_name not in self.tables.keys():
            raise AttributeError('No table found')

        columns = len(data[0]) - 1
        insert = f'INSERT INTO {table_name} VALUES(%s' + ', %s' * columns + ')'
        with db_connection.cursor() as cur:
            cur.executemany(insert, map(lambda x: x.values(), data))
            db_connection.commit()

    def execute_query(self, db_connection, query: str) -> list[dict]:
        """Execute query and return data dict"""
        with db_connection.cursor() as cur:
            cur.execute(query)
            result = cur.fetchall()
            columns = cur.column_names
        result = self._convert_data(columns, result)
        return result

    @staticmethod
    def _convert_data(keys: list, data: list) -> list[dict]:
        """Convert query result to dict"""
        result = []
        for value in data:
            data_dict = {}
            for i in range(len(keys)):
                data_dict[keys[i]] = value[i]
            result.append(data_dict)
        return result

    @staticmethod
    def add_index(db_connection, index_name: str, table_name: str, field_name):
        if type(field_name) == list:
            field_name = ', '.join(field_name)
        with db_connection.cursor() as cur:
            cur.execute(f'create index {index_name} on {table_name}({field_name})')
