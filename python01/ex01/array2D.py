def new_x(start: int, end: int, len: int) -> str:
    if (start >= 0 and start < len and end > start):
        return (f"{end - start}")
    if ((start < 0 and end >= 0) or (end < 0 and start >= 0)):
        return ("1")


def slice_me(family: list, start: int, end: int) -> list:
    if (len(family) == 0 or len(family[0]) == 0):
        return

    column = len(family[0])
    for elem in family:
        if (len(elem) != column or not isinstance(elem, list)):
            return

    print(f"My shape is : ({len(family)}, {column})")
    print(f"My new shape is : ({new_x(start, end, len(family))}, {column})")
    return (family[start:end])
