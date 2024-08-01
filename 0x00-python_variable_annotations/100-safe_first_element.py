#!/usr/bin/env python3
"""defines safe_first_element() function"""

from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ duck typing """
    if lst:
        return lst[0]
    else:
        return None
