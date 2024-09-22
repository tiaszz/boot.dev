def doc_format_checker_and_converter(conversion_function, valid_formats):
    def validation(filename, content):
        format = filename.split(".")
        if format[1] in valid_formats:
            return conversion_function(content)
        raise ValueError("Invalid file format")
    return validation

# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]

