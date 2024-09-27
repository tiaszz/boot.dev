def configure_plugin_decorator(func):
    def wrapper(*args):
        dict_arg = {}
        for arg in args:
            dict_arg[arg[0]] = arg[1]
        
        return func(**dict_arg)
    return wrapper

