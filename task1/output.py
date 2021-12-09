def output(text: str, output_format: str) -> None:
    """Create or rewrite file with provided text"""
    file_name = f'output.{output_format}'
    with open(file_name, 'w') as file:
        file.write(text)
