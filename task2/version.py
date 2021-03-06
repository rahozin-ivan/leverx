from functools import total_ordering

from replace_symbols import replace_symbols
from normalize_length import normalize_length


@total_ordering
class Version:
    must_be_replaced = {
        '-': '',
        'alpha': '.-3',
        'beta': '-2',
        'b': '.-2',
        'rc': '.-1',
    }
    normal_length = 5

    def __init__(self, version):
        self.version = self._configure_version(version)

    def _configure_version(self, version):
        version_list = replace_symbols(version, self.must_be_replaced).split('.')
        version = [int(i) for i in version_list]
        normalize_length(version, self.normal_length)
        return version

    def __gt__(self, other):
        return self.version > other.version

    def __eq__(self, other):
        return self.version == other.version


def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"


if __name__ == "__main__":
    main()
