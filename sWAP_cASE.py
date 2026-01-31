def swap_case(s):
    ans = ""
    for ch in s:
        if ch.isupper():
            ans += ch.lower()
        else:
            ans += ch.upper()
    return ans