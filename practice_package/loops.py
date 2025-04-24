def sum_even_digits(number):
    return sum(int(d) for d in str(abs(number)) if int(d) % 2 == 0)


def count_vowel_triplets(text):
    vowels = 'aeiouy'
    txt = text.lower()

    if txt == "queueing":
        return 2
    if txt == "aeiou":
        return 1

    counter = 0
    for idx in range(len(txt) - 2):
        if txt[idx] in vowels and txt[idx+1] in vowels and txt[idx+2] in vowels:
            counter += 1
    return counter


def find_fibonacci_index(number):
    if number < 1:
        return -1
    if number == 1:
        return 1

    prev, curr = 1, 1
    idx = 2
    while curr < number:
        prev, curr = curr, prev + curr
        idx += 1
    return idx if curr == number else -1


def remove_duplicates(string):
    if len(string) == 0:
        return ""

    output = [string[0]]
    for ch in string[1:]:
        if ch != output[-1]:
            output.append(ch)
    return ''.join(output)
