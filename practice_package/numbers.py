calculate_distance = lambda x1, x2: (x2 - x1) if x2 >= x1 else (x1 - x2)

calculate_segments = lambda length_a, length_b: length_a // length_b

calculate_digit_sum = lambda number: sum(int(ch) for ch in str(abs(number)))


def calculate_rect_area(x1, y1, x2, y2):
    return (x2 - x1 if x2 > x1 else x1 - x2) * (y2 - y1 if y2 > y1 else y1 - y2)


def round_to_multiple(number, multiple):
    return multiple * round(number / multiple)
