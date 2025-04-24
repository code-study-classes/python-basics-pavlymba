def count_char_occurrences(text):
    counts = {}
    for ch in text.lower():
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1
    return counts


def merge_dicts(dict1, dict2, conflict_resolver):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] = conflict_resolver(key, merged[key], value)
        else:
            merged[key] = value
    return merged


def invert_dictionary(original_dict):
    inverted = {}
    for key, value in original_dict.items():
        inverted.setdefault(value, []).append(key)
    return inverted


def dict_to_table(data_dict, columns):
    header = [col.upper() for col in columns]
    rows = []
    col_widths = {col: len(col) for col in header}
    for entry in data_dict.values():
        row = []
        for col in columns:
            value = str(entry.get(col, 'N/A'))
            col_widths[col.upper()] = max(col_widths[col.upper()], len(value))
            row.append(value)
        rows.append(row)
    header_line = "|" + "|".join(f" {col.ljust(col_widths[col])} " for col in header) + "|"
    separator = "|" + "|".join("-" * (col_widths[col] + 2) for col in header) + "|"
    row_lines = []
    for row in rows:
        row_line = "|" + "|".join(
            f" {val.ljust(col_widths[col.upper()])} " for val, col in zip(row, columns)
        ) + "|"
        row_lines.append(row_line)
    return "\n".join([header_line, separator] + row_lines)


def deep_update(base_dict, update_dict):
    import copy
    base_copy = copy.deepcopy(base_dict)
    for key, value in update_dict.items():
        if key in base_copy and isinstance(base_copy[key], dict) and isinstance(value, dict):
            base_copy[key] = deep_update(base_copy[key], value)
        elif key in base_copy:
            base_copy[key] = value
    return base_copy
