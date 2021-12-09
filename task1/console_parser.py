from argparse import ArgumentParser


class ConsoleParser(ArgumentParser):
    """Configure and read console arguments"""
    def __init__(self, formats: dict):
        super().__init__()
        self.add_argument("-students", "--s", dest="students", type=str)
        self.add_argument("-rooms", "--r", dest="rooms", type=str)
        self.add_argument("-format", "--f", dest="format", type=str, choices=formats.keys())
        self.formats = formats
        self.args = None

    def read_console_args(self) -> None:
        """Read console arguments"""
        self.args = self.parse_args()
        self.args.serializer = self.formats[self.args.format]
