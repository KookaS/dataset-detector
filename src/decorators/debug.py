"""decorators.debug.py module"""
from functools import wraps


def debug(_function):
    """
    Print the function signature and return value
    Usage:
    @debug
    def function(a):
        pass
    """

    @wraps(_function)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        print(f"Calling {_function.__name__}({signature})")
        result = _function(*args, **kwargs)
        print(f"{_function.__name__!r} returned {result!r}")  # 4
        return result

    return wrapper
