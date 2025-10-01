def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Return a list with a different imc.
    """
    list = []
    i = 0

    size = len(weight)
    if (len(height) < size):
        size = len(height)

    while (i < size):
        if not isinstance(weight[i], (int, float)):
            i += 1
            continue
        if not isinstance(height[i], (int, float)):
            i += 1
            continue
        list.append(weight[i] / (height[i] ** 2))
        i += 1

    return (list)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return a list with a resul is true or false if the limit exceeds.
    """
    list = []

    for elem in bmi:
        if not isinstance(elem, (int, float)):
            continue
        if elem < limit:
            list.append(True)
        else:
            list.append(False)

    return (list)
