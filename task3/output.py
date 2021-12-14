def output(text: str, file_name: str, output_format: str) -> None:
    """Create or rewrite file with provided text"""
    full_file_name = f'output/{file_name}.{output_format}'
    with open(full_file_name, 'w') as file:
        file.write(text)
