def swap_case(s):
    swap = ''
    for ch in s:
        if ch.isupper():
            swap += ch.lower()
        else:
            swap += ch.upper()
    return swap