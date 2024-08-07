#!/usr/bin/env python3
"""
defines safely_get_value() function
"""
from typing import Union, Any, TypeVar, Mapping


R = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[R, None] = None) -> Union[Any, R]:
    """
    Add type annotations to function
    safely_get_value
    """
    if key in dct:
        return dct[key]
    else:
        return default
