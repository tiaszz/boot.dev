def args_logger(*args, **kwargs):
    for i in range(0, len(args)):
        print(f"{i}. {args[i]}")
    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")



