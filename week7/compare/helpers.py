def lines(a, b):
    """Return lines in both a and b"""

    l1 = a.split("\n")
    l2 = b.split("\n")
    lines = []
    for line1 in l1:
        for line2 in l2:
            if line1 == line2:
                lines.append(line1)
            else:
                lines.append([])

    return lines


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    return []


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    return []
