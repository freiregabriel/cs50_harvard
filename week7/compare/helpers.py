from nltk.tokenize import sent_tokenize


def _get_similarities(l1, l2):
    """Compare two lists and return the elements that appear on both of them
        a = [1, 2, 3]
        b = [2, 3, 4, 5]
        c = _get_similarities(a, b)
        # c == [2, 3]
    """
    eq = []
    for t in l1:
        for k in l2:
            if t == k and t not in eq:
                eq.append(t)
    return eq


def lines(a, b):
    """Return lines in both a and b"""
    l1 = a.split("\n")
    l2 = b.split("\n")
    sim = _get_similarities(l1, l2)
    return sim


def sentences(a, b):
    """Return sentences in both a and b"""
    tk1 = sent_tokenize(a)
    tk2 = sent_tokenize(b)
    sim = _get_similarities(tk1, tk2)
    return sim


def _extract_substrs(st, n):
    """ Return substrings of length N from string
        a = "Gabriel Freire"
        b = _extract_substr(a, 3)
        # b == ['Gab', 'abr', 'bri', 'rie', 'iel', 'el ', 'l F', ' Fr', 'Fre', 'rei', 'eir', 'ire']
    """
    substr_list = []
    st_n = len(st)
    if n > st_n:
        return []

    for i in range(0, st_n):
        j = i + n
        if j > st_n:
            break
        substr_list.append(st[i:j])
    return substr_list


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    word_list_f = _extract_substrs(a, n)
    word_list_s = _extract_substrs(b, n)
    if not word_list_f or not word_list_s:
        return []
    sim = _get_similarities(word_list_f, word_list_s)
    return sim
