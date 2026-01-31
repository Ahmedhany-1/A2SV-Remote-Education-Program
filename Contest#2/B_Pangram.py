m = int(input())
n = input()
if m < 26:
    print("NO")
else:
    new_n = n.lower()
    set_n = set(new_n)
    if len(set_n) == 26:
        print("YES")
    else:
        print("NO")