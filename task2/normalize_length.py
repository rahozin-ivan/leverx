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
