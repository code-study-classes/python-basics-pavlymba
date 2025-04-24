def is_weekend(day):
    return day in {6, 7}


def get_discount(amount):
    if amount >= 5000:
        return round(amount * 0.1, 2)
    if amount >= 1000:
        return round(amount * 0.05, 2)
    return 0


def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"

    if n == 0 or (1 <= n <= 9):
        digit = "однозначное"
    elif 10 <= n <= 99:
        digit = "двузначное"
    else:
        digit = "трехзначное"

    return f"{parity} {digit} число"


def convert_to_meters(unitNumber, lengthInUnits):
    conversion = {
        1: 0.1,
        2: 1000,
        3: 1,
        4: 0.001,
        5: 0.01
    }
    return lengthInUnits * conversion.get(unitNumber, 0)


def describe_age(age):
    tens = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
        10: "сто"
    }

    units = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
    }

    last_digit = age % 10
    last_two_digits = age % 100

    if last_digit == 1 and last_two_digits != 11:
        word = "год"
    elif 2 <= last_digit <= 4 and not 11 <= last_two_digits <= 19:
        word = "года"
    else:
        word = "лет"

    if age < 20:
        return f"{units.get(age, str(age))} {word}"
    if last_digit == 0:
        return f"{tens[age // 10]} {word}"
    return f"{tens[age // 10]} {units[last_digit]} {word}"
