def new_resizer(max_width, max_height):
    def min_resizer(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def image_size(width, height):
            adjusted_width = max(min(width, max_width), min_width)
            adjusted_height = max(min(height, max_height), min_height)
            return adjusted_width, adjusted_height

        return image_size

    return min_resizer

