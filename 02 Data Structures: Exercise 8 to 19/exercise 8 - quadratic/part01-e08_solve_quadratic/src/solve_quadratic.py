#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    d = math.sqrt((b**2 - (4*a*c)))

    x1 = (-b + d)/(2*a)
    x2 = (-b - d)/(2*a)
    x1 = float(x1)
    x2 = float(x2)
    return (x1,x2)


def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))
    print(solve_quadratic(-2.000000,2.000000,1))

    #pass


if __name__ == "__main__":
    main()
