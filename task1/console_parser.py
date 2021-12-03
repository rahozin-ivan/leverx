from argparse import ArgumentParser


class ConsoleParser(ArgumentParser):
    """Configure and read console arguments"""
    def __init__(self, formats: dict):
        super().__init__()
        self.add_argument("-students", "--s", type=str)
        self.add_argument("-rooms", "--r", type=str)
        self.add_argument("-format", "--f", type=str, choices=formats.keys())
        self.formats = formats
        self.args = None

    def read_console_args(self) -> None:
        """Read console arguments"""
        self.args = self.parse_args()
        try:
            self.args.serializer = self.formats[self.args.f]
        except KeyError:
            raise KeyError("No serializer for this format")
