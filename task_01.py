#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module converts temperatures."""

from decimal import Decimal

ABSOLUTE_DIFFERENCE = Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """This function converts from fahrenheit to celsius.

    Args:
        degrees (float): Number of degress.

    Returns:
        float: temperature as a decimal in degrees Celsius.

    Examples:

        >>> fahrenheit_to_celsius(212)
        Decimal('100')

        >>> celsius_to_kelvin(100)
        Decimal('373.15')

        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')>>>
    """
    deg = Decimal((float(degrees)) - 32)
    cel = (deg * 5) / 9
    return Decimal(cel)


def celsius_to_kelvin(degrees):
    """This function converts from celsius to kelvin.

    Args:
        degrees (float): Number of degress.

    Returns:
        float: temperature as a decimal in degrees Kelvin.

    Examples:

        >>> fahrenheit_to_celsius(212)
        Decimal('100')

        >>> celsius_to_kelvin(100)
        Decimal('373.15')

        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')>>>
    """
    kel = (ABSOLUTE_DIFFERENCE) + degrees
    return Decimal(kel)


def fahrenheit_to_kelvin(degrees):
    """This function converts from fahrenheit to kelvin.

    Args:
        degrees (float): Number of degress.

    Returns:
        float: temperature as a number in degrees Kelvin.

    Examples:

        >>> fahrenheit_to_celsius(212)
        Decimal('100')

        >>> celsius_to_kelvin(100)
        Decimal('373.15')

        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')>>>
    """
    ftokel = celsius_to_kelvin(fahrenheit_to_celsius(degrees))
    return Decimal(ftokel)

print fahrenheit_to_celsius(212)
print float(celsius_to_kelvin(100))
print fahrenheit_to_kelvin(212)
