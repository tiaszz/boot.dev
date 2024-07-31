def zipmap(keys, values):
    if len(keys) == 0 and len(values) == 0:
        return {}
    return {keys[0]: values[0]} or zipmap(keys[1:], values[1:])

