from typing import Callable
import random
import functools


def log(*dec_args) -> Callable:
    assert len(dec_args) <= 1, "Максимум один параметр у декоратора"
    non_arg_dec = callable(dec_args[0]) and len(dec_args) == 1

    def outer_wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):
            func(*args, **kwargs)
            t = random.randint(0, 5)
            if non_arg_dec:
                print(f'{func.__name__} - {t} с')
            else:
                print(dec_args[0].format(t))
        return inner_wrapper

    if non_arg_dec:
        return outer_wrapper(dec_args[0])
    else:
        return outer_wrapper
