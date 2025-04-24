check_between_numbers = lambda A, B, C: (A < B and B < C) or (A > B and B > C)  # noqa E731

check_odd_three = lambda number: (99 < abs(number) < 1000) and (number % 2 == 1)  # noqa E731

check_unique_digits = lambda number: (99 < abs(number) < 1000) and len({*str(abs(number))}) == 3  # noqa E731


def check_palindrome_number(number):  # noqa E731
    digits = str(abs(number))
    return digits == digits[::-1]


check_ascending_digits = lambda number: (99 < abs(number) < 1000) and \
    (lambda digits: digits[0] < digits[1] < digits[2])(
        list(map(int, str(abs(number))))
    )  # noqa E731
