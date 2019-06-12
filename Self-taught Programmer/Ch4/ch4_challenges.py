# 1.
def squared(x):
    """
    Returns the square of x.
    :param x: int.
    :return: int square of x.
    """
    return x**2

print(squared(2))

# 2.
def printString(string):
    """
    Prints string.
    :param string: str.
    """
    print(string)

printString("printing String")

# 3.
def req_opt_params(x, y, z, a=1, b=2):
    """
    Returns the sum of x, y, z, a & b.
    :param x: int.
    :param y: int.
    :param z: int.
    :param a: int.
    :param b: int.
    :return: int sum of x, y, z, a & b.
    """
    return x + y + z + a + b

print(req_opt_params(1, 1, 1))

# 4.
def firstFunction(x):
    """
    Returns x divided by 2.
    :param x: int.
    :return: int x divided by 2.
    """
    return x/2
def secondFunction(y):
    """
    Returns the y times 4.
    :param y: int.
    :return: int y times 4.
    """
    return y * 4

print(secondFunction(firstFunction(1)))

# 5.
def string_to_float(string):
    """
    Returns the string as a float.
    :param string: str.
    :return: float string as float.
    """
    try:
        return float(string)
    except ValueError:
        print("value can not be converted to float for:  " + string)

print(string_to_float("1.25"))
print(string_to_float("1"))
print(string_to_float("I am not a float"))

# 6.
# Add a docstring to challenges 1 thru 5
