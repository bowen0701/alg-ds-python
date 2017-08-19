"""Anagram detecting problem.

Two strings are anagram if one is simply a rearrangement of the other.
"""

def check_anagram(s1, s2):
    """Anagram by naive check."""
    l2 = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(l2) and not found:
            if s1[pos1] == l2[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            l2[pos2] = None
        else:
            still_ok = False

        pos1 += 1

    return still_ok 


def sort_anagram(s1, s2):
    """Anagram by sorting."""
    l1 = list(s1)
    l2 = list(s2)

    l1.sort()
    l2.sort()
    
    pos = 0
    match_bool = True
    
    while pos < len(s1) and match_bool:
        if l1[pos] == l2[pos]:
            pos = pos + 1
        else:
            match_bool = False
    
    return match_bool


def count_anagram(s1, s2):
    """Anagram by counting."""
    c1 = [0] * 26
    c2 = [0] * 26
    
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    
    j = 0
    still_ok = True
    
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    
    return still_ok
