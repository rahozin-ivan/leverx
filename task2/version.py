from functools import total_ordering


@total_ordering
class Version:
    must_be_replaced = {
        '-': '',
        'alpha': '.-3',
        'beta': '-2',
        'b': '.-2',
        'rc': '.-1',
    }

    def __init__(self, version):
        version_list = Version.replace_symbols(version).split('.')
        self.version = [int(i) for i in version_list]

    def __lt__(self, other):
        if len(self.version) != len(other.version):
            version1, version2 = Version.normalize_length(self.version, other.version)
            return version1 < version2
        return self.version < other.version

    def __gt__(self, other):
        if len(self.version) != len(other.version):
            version1, version2 = Version.normalize_length(self.version, other.version)
            return version1 > version2
        return self.version > other.version

    def __ne__(self, other):
        if len(self.version) != len(other.version):
            version1, version2 = Version.normalize_length(self.version, other.version)
            return version1 != version2
        return self.version != other.version

    @staticmethod
    def replace_symbols(version: str) -> str:
        """Replace symbols which must be replaced"""
        for k, v in Version.must_be_replaced.items():
            if k in version:
                version = version.replace(k, v)
        return version

    @staticmethod
    def normalize_length(version1: list, version2: list):
        """Normalizing length of versions"""
        if len(version1) < len(version2):
            diff = len(version2) - len(version1)
            for i in range(diff):
                version1.append(0)
        else:
            diff = len(version1) - len(version2)
            for i in range(diff):
                version2.append(0)
        return version1, version2


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
