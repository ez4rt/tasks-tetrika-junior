def strict(func):
    def wrapper(*args, **kwargs):
        values = list(args) if args else list(kwargs.values())
        for value in values:
            if type(value) != int:
                raise TypeError
        return func(*values)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b



