def ft_filter(function, itera):
    """filter the iterable """
    if function is None:
        return iter([item for item in itera if item])
    return iter([item for item in itera if function(item)])
