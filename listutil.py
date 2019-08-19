def unique(list):
    """Return a list containing only the first occurence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        list: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(['b','a','a','b','b','b','a','a'])
    ['b', 'a']
    >>> unique([])
    []
    >>> unique(['isp', 'isp', 'isp', 'isp', 'isp'])
    ['isp']
    >>> unique([1, 1, True, 1])
    [1, True]
    >>> unique()
    """
    uniqued_list = []

    for input_element in list:
        for uniqued_list_element in uniqued_list:
            is_same_type = type(input_element) == type(uniqued_list_element)
            is_same_value = input_element == uniqued_list_element

            if is_same_type and is_same_value:
                break
        else:
            uniqued_list.append(input_element)

    return uniqued_list


if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
