#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: February 12, 2025
# This program performs basic math operations

import math


def main():
    print(
        "For a rectangle with an length of pi meters, and a height of Avagadros constant meters: "
    )
    print()
    print("The area is {}cm^2".format(math.pi * 6.02214076 * (10**-23)))
    print("The perimeter is {}cm".format((math.pi * 2) + (2 * 6.02214076 * (10**-23))))


if __name__ == "__main__":
    main()
