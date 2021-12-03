def output(text: str, output_format: str) -> None:
    """Create or rewrite file with provided text"""
    file_name = 'output.xml' if output_format == 'xml' else 'output.json'
    with open(file_name, 'w') as file:
        file.write(text)
