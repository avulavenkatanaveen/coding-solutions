# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    d=max(a,b,c)
    print(d)