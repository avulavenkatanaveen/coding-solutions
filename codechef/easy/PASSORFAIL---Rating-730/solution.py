# cook your dish here
t=int(input())
for _ in range(t):
    n,x,p=map(int,input().split())
    a=x*3
    b=n-x
    c=a-b
    if c>=p:
        print("")
    