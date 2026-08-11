# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    e=max(a,b)
    f=max(c,d)
    print(e+f)