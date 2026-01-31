s = input()
n = int(input())

f_ch = s[0]
l_ch = s[-1]

ok_1 = False
ok_2 = False
ok_3 = False

for _ in range(n):
    curr_s = input()
    if(curr_s[-1] == f_ch):
        ok_1 = True
    if(curr_s[0] == l_ch):
        ok_2 = True
    if(curr_s == s):
        ok_3 = True

if (ok_1 and ok_2) or ok_3:
    print("YES")
else:
    print("NO")