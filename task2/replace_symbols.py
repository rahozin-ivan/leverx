def replace_symbols(version: str, must_be_replaced: dict) -> str:
    """Replace symbols which must be replaced"""
    for k, v in must_be_replaced.items():
        if k in version:
            version = version.replace(k, v)
    return version
