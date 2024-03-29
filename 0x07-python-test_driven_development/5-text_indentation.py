#!/usr/bin/python3
"""contains a text_indentation function
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these chars: ., ? and :
    Args:
        text: string to be printed
    """
    chars = ".?:"
    if type(text) is not str:
        raise TypeError("text must be a string")

    res = split_and_strip([text], chars)
    s = "\n\n".join(res)
    if s[-1] in chars:
        s = s + "\n\n"

    print(s, end="")


def split_and_strip(lst, sep):
    """splits and strips all the strings in the list
    Args:
        lst: list of strings
        sep: separator to split the string
    Return:
        a list of splitted and stripped strings
    Test:
    >>> split_and_strip(["qwe?rty. daniel : ? "], ".?:")
    ['qwe?', 'rty.', 'daniel :', '?']
    """
    if not (lst and sep):
        return lst

    res = []
    for s in lst:
        temp = s.split(sep[0])
        for i, e in enumerate(temp):
            if i == len(temp) - 1:
                break

            res.append((e + sep[0]).strip())

        res.append(temp[-1].strip())

    ret = split_and_strip(res, sep[1:])
    if not ret[-1]:
        del(ret[-1])

    return ret
