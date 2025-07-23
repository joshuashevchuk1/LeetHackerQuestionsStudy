from functools import wraps
from collections import OrderedDict

def cache(limits):
    if not isinstance(limits, dict):
        raise ValueError("limits must be a dictionary of {arg_index: max_value}")

    def decorator(func):
        local_cache = OrderedDict()
        MAX_CACHE_SIZE = 256
        func_name = func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            for index, max_val in limits.items():
                if index < len(args):
                    val = args[index]
                    if isinstance(val, int) and val > max_val:
                        call_args = ", ".join(repr(a) for a in args)
                        raise ValueError(
                            f"{func_name}({call_args}) is too high to calculate"
                        )

            key = (args, frozenset(kwargs.items()))
            if key in local_cache:
                local_cache.move_to_end(key)
                return local_cache[key]

            result = func(*args, **kwargs)
            local_cache[key] = result
            if len(local_cache) > MAX_CACHE_SIZE:
                local_cache.popitem(last=False)
            return result
        return wrapper
    return decorator
