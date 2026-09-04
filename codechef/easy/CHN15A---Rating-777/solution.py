# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    values=list(map(int,input().split()))
    c=0
    for x in values:
        if (x+k)%7==0:
            c+=1
    print(c)