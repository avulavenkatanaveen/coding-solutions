# cook your dish here
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    i=21-(a+b)
    if 1<=i<=10:
        print(i)
    else:
        print(-1)
