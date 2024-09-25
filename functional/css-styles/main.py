def css_styles(initial_styles):
    styles_copy = initial_styles.copy()
    def add_styles(selector, property, value):
        if selector not in styles_copy:
            styles_copy[selector] = {}

        styles_copy[selector][property] = value
        return styles_copy
    return add_styles

