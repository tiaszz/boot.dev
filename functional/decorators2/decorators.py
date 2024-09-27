def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        mapped_args = list(map(convert_md_to_txt, args))
        mapped_kwargs = {k: convert_md_to_txt(v) for k, v in kwargs.items()}
        return func(*mapped_args, **mapped_kwargs)

    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)

