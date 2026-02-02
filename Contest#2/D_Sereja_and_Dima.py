n = int(input())
a = list(map(int, input().split()))

ans_a = 0
ans_b = 0

i = 0 
j = n - 1

f_turn = True 

while i <= j:
    x = 0
    if a[i] >= a[j]:
        x = a[i]
        i += 1
    else:
        x = a[j]
        j -= 1
    
    # print(x)
    if f_turn:
        ans_a += x
    else:
        ans_b += x 

    f_turn = not f_turn


print(ans_a, ans_b)

"""
n = int(input())
a = list(map(int, input().split()))

ans_a = 0
ans_b = 0

f_turn = True 

for i in range(n):
    if(a[0] > a[-1]):
        value = a[0]
        a.remove(a[0])
    else:
        value = a[-1]
        a.remove(a[-1])
  
    if f_turn:
        ans_a += value
    else:
        ans_b += value
    
    f_turn = not f_turn
 
print(ans_a, ans_b)

"""