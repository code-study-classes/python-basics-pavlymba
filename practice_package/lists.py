def square_odds(numbers):
    return list(map(lambda n: n * n, filter(lambda x: x % 2 == 1, numbers)))


def normalize_names(names):
    return [n[:1].upper() + n[1:].lower() if n else '' for n in names]


def remove_invalid_emails(emails):
    valid = []
    for e in emails:
        if e.count('@') == 1 and len(e) >= 5 and not (e.startswith('@') or e.endswith('@')):
            valid.append(e)
    return valid


def filter_palindromes(words):
    result = []
    for w in words:
        lowered = w.lower()
        if lowered == lowered[::-1]:
            result.append(w)
    return result


def calculate_factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def find_common_prefix(strings):
    if len(strings) == 0:
        return ""
    base = strings[0]
    for other in strings[1:]:
        while not other.startswith(base):
            base = base[:-1]
            if base == "":
                return ""
    return base
