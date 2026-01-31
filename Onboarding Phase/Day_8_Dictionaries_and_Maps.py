N=int(input())
phoneBook={}

for _ in range(N):
    name,contact=input().split()
    phoneBook[name]=contact

try:
    while(True):
        check=str(input())
        if check in phoneBook:
            print(check+"="+phoneBook[check])
        else:
            print('Not found')

except(EOFError):
    pass
   