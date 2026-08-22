# cook your dish here
t=int(input())
for _ in range(t):
    s,x,y,z=map(int,input().split())
    f=s-(x+y)
    if z<=f:
        print(0)
    elif z<=f+max(x,y):
        print(1)
    else:
        print(2)