import math


def log_scale(data, base):
    new_data = []
    for num in data:
        new_data.append(math.log(num, base))
    return new_data

