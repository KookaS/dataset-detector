"""decorators.count_calls.py module"""
import functools


class CountCalls:
    """
    Decorator for printing each time a function is called.
    Usage:
    @CountCalls
    def function(a):
        pass
    """

    def __init__(self, _function):
        """
        Constructor for the CountCalls decorator
        """
        functools.update_wrapper(self, _function)
        self._function = _function
        self.num_of_calls = 0

    def __call__(self, *args, **kwargs):
        """
        Each time the function is called, it calls CountCalls.__call__
        """
        self.num_of_calls += 1
        print(f"{self._function.__name__} called {self.num_of_calls} times")
        return self._function(*args, **kwargs)
