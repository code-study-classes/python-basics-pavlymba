def find_common_elements(set1, set2):
    return {i for i in set1 if i in set2}


def is_superset(set_a, set_b):
    return all(x in set_a for x in set_b)


def remove_duplicates(items):
    result = []
    memory = set()
    for val in items:
        if val not in memory:
            memory.add(val)
            result.append(val)
    return result


def count_unique_words(text):
    return len(set(word.lower() for word in text.split()))


def find_shared_items(*sets):
    if len(sets) == 0:
        return set()
    shared = sets[0].copy()
    for s in sets[1:]:
        shared &= s
    return shared
