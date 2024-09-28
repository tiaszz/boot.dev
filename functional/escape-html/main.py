def replacer(old, new):
    def replace(func):
        def wrapper(text):
            replaced_text = text.replace(old, new)
            return func(replaced_text)

        return wrapper
        
    return replace

@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"

