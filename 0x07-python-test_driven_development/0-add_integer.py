#!usr/bin/python3
""defines an integer addition function""


def add_integer(a, b=98):
    ""Return the integer addition of a and b.
    float arguments are typecasted to ints before addition is performed
    Raises:
        TypeError:if either of a or b is a non-integer and non-float
        ""
        if ((not isinstance(a, int) and not isinstance(a, float))):
            raise TypeError("a must be an integer")
        if ((not isinstances(b, int) and not isinstance(b, float)):
                Raise TypeError("b, must be an integer")
                return(int(a)+int(b))
