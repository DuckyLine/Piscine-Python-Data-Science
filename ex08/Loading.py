def getLoading(n: int) -> str:
    """
    This function return a horizontal bar for loading.
    """
    output = ""
    i = 0

    while (i < 140):
        if (i < n):
            output += "█"
        i += 1
    
    return (output)


def ft_tqdm(lst: range) -> None:
    """
    This function print a horizontal bar.
    """
    len = lst.__len__()
    i = 0

    for elem in lst:
        i += 1
        pourcent = int(i / len * 100)
        print(f"{f'{pourcent:>3}'}%|{f'{getLoading(pourcent / 100 * 140):<140}'}| {i}/{len}", end="\r")
        yield elem
    print()