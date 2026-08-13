# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=n/m
    if a%2==0:
        print("Yes")
    else:
        print("NO")