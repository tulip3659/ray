"""
This is a simple function used to practice pytest.
"""


def capitalize_this(x):
    if not isinstance(x, str):
        raise TypeError("Incorrect input type. Use Strings!")
    return x.capitalize()
