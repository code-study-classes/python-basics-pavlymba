def extract_file_name(full_file_name):
    last_part = full_file_name.split('/')[-1]
    if last_part.startswith('.'):
        return last_part
    split_name = last_part.split('.', 1)
    return split_name[0] if len(split_name) > 1 else last_part


def encrypt_sentence(sentence):
    a, b = [], []
    for i in range(len(sentence)):
        if i % 2:
            a.append(sentence[i])
        else:
            b.append(sentence[i])
    return ''.join(a + b[::-1])


def check_brackets(expression):
    opens = 0
    closes = 0
    pos = 0
    for ch in expression:
        if ch != ' ':
            pos += 1
        if ch == '(':
            opens += 1
        elif ch == ')':
            closes += 1
        if closes > opens:
            return pos
    return -1 if opens > closes else 0


def reverse_domain(domain):
    return '.'.join(domain.split('.')[::-1])


def count_vowel_groups(word):
    vowels = set('aeiouy')
    word = word.lower()
    count = 0
    flag = False
    for ch in word:
        if ch in vowels:
            if not flag:
                count += 1
                flag = True
        else:
            flag = False
    return count