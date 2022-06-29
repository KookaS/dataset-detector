"""decorators.shutdown_cloud.py module"""
import os
from functools import wraps, partial

from numpy import uint


def run_command(cmd):
    """
    Run a bash command.
    """
    return os.system(cmd)


def shutdown_cloud(_function=None, *, seconds: uint = 0):
    """
    Decorator for shutding down cloud instance when it's done.
    Shutdown system after seconds given. Useful for shutting EC2 to save costs.
    Usage:
    @shutdown_cloud
    def function(a):
        pass

    or

    @shutdown_cloud(seconds= 3)
    def function(a):
        pass
    """
    if _function is None:
        return partial(shutdown_cloud, seconds=seconds)

    @wraps(_function)
    def wrapper(*args, **kwargs):
        result = _function(*args, **kwargs)
        if os == "linux":
            run_command(f"sudo shutdown -h -t sec {seconds}")
        elif os == "windows":
            run_command(f"shutdown -s -t {seconds}")
        return result

    return wrapper
