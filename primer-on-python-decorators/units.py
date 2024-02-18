import functools

import pint


def set_unit(unit):
    """Register a unit on a function"""

    def decorator_set_unit(func):
        func.unit = unit
        return func

    return decorator_set_unit


def use_unit(unit):
    """Have a function return a Quantity with given unit"""
    use_unit.ureg = pint.UnitRegistry()

    def decorator_use_unit(func):
        @functools.wraps(func)
        def wrapper_use_unit(*args, **kwargs):
            value = func(*args, **kwargs)
            return value * use_unit.ureg(unit)

        return wrapper_use_unit

    return decorator_use_unit
