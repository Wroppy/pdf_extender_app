from typing import Union

def to_two_decimals(number: Union[str, int, float]) -> str:
    """
    Given a number in string, integer, or float form, returns a string of the number
    rounded to 2 decimal places
    """

    return str(round(number, 2))
    