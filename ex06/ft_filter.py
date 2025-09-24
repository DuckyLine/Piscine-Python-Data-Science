def ft_filter(function, iterrable):
    """
    Recode filter function.
    """
    ft_list = []

    for elem in iterrable:
        if (function(elem)):
            ft_list += elem

    return (iter(ft_list))
