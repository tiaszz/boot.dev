def create_markdown_image(alt_text):
    markdown_image = f"![{alt_text}]"

    def inner_function(url):
        escaped_url = url.replace("(", "%28").replace(")", "%29")
        markdown_image_url = f"{markdown_image}({escaped_url})"

        def innermost_function(title=None):
            if title:
                return f'{markdown_image_url[:-1]} "{title}")'
            return markdown_image_url

        return innermost_function

    return inner_function
