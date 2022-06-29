"""decorators.timing.py module"""
import time
from functools import wraps


def timing(_function):
    """Decorator for timing functions
    Usage:
    @timing
    def function(a):
        pass
    """

    @wraps(_function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = _function(*args, **kwargs)
        end = time.time()
        print(f"function: {_function.__name__} took: {end - start} sec")
        return result

    return wrapper
