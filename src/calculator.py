import numbers
"""ATCS Unit 0 demonstration calculator.

This program is intentionally simple so students can focus on
professional software-engineering workflow rather than syntax.
"""
a = ""
b = ""
while not isinstance(a, numbers.Number):
    try:
        a = float(input("Input a number for A: "))
    except ValueError:
        continue

while not isinstance(b, numbers.Number):
    try:
        b = float(input("Input a number for B: "))
    except ValueError:
        continue


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return b subtracted from a."""
    return a - b


def main():
    print("Engineering Calculator")
    print(a," + ",b," =", add(a, b))
    print(a," + ",b," =", subtract(a, b))


if __name__ == "__main__":
    main()
