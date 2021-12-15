def normalize_length(version: list, normal_length: int):
    """Normalizing length of version"""
    if len(version) < normal_length:
        diff = normal_length - len(version)
        for i in range(diff):
            version.append(0)
