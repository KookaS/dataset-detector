"""decorators.singleton.py module"""
from functools import wraps


def singleton_class(_class):
    """
    Make a Singleton class (only one instance).
    Multiple reference will point to the same and unique class.
    Usage:
    @singleton_class
    def ClassA:
        pass
    """

    @wraps(_class)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = _class(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper

def singleton_instance(cache_key):
    """
    Make a Singleton isntance (only one instance).
    Multiple reference will point to the same and unique instance.
    Usage:
    @singleton_instance(function)
    def function(a):
        pass
    """
    def inner_function(_function):
        @wraps(_function)
        def wrapper(self, *args, **kwargs):
            instance = getattr(self, cache_key)
            if instance is not None:
                return instance

            instance = _function(self, *args, **kwargs)
            setattr(self, cache_key, instance)
            return instance
        return wrapper
    return inner_function
