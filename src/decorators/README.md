# dressme-ml decorators

## decorators

Use case:

    from decorators import <DECORATOR>
    @<DECORATOR>
    def function(a):
        pass

### performance

#### cache

For iterative functions for example:
The maxsize parameter specifies how many recent calls are cached. The default value is 128, but you can specify maxsize=None to cache all function calls. However, be aware that this can cause memory problems if you are caching many large objects.
You can use the .cache_info() method to see how the cache performs, and you can tune it if needed. 

    import functools
    @functools.lru_cache(maxsize=4)

#### jit

https://numba.pydata.org/numba-doc/latest/user/jit.html

    from numba import jit
    @jit

### debug

#### timing

Timing decorator:

    from decorators import timing
    @timing

#### count_calls

Count and print the amount of calls for a function:

    from decorators import CountCalls
    @CountCalls

#### debug

Print the function signature and return value:

    from decorators import debug
    @debug

### safety

#### shutdown

Shutdown cloud instance when training is done:

    from decorators import shutdown
    @shutdown(seconds=0)
    @shutdown

#### singleton

Make a class a Singleton class (only one instance)

    @singleton_class

Make a instance singleton

    @singleton_instance('instance_name')
    def fn():
        ...
        instance_name = ...