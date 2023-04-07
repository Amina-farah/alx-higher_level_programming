#!/usr/bin/python3
"""define a locked class."""

class LockedClass:
    """
    prevent's user from instantiating new LockedClass attribute for attributes called 'first_name'
    """

    _slot_ = ["first_name"]
