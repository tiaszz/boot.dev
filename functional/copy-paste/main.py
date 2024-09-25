def new_clipboard(initial_clipboard):
    copy_clipboard = initial_clipboard.copy()
    def copy_to_clipboard(key, value):
        copy_clipboard[key] = value
        return copy_clipboard

    def paste_from_clipboard(key):
        if key not in copy_clipboard:
            return ""
        return copy_clipboard[key]

    return copy_to_clipboard, paste_from_clipboard

