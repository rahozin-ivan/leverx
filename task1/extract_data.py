def extract_data(data: list[dict], data_model) -> list:
    result = []
    for item in data:
        result.append(data_model(**item))
    return result
