from json import load


class JSONParser:
    """Parser of json files"""
    @staticmethod
    def parse_file(file_name: str) -> list:
        """Parse file and store data"""
        with open(file_name) as file:
            data = load(file)
        return data
