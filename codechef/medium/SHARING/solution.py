# cook your dish here
a,b=map(int,input().split())
c=a+b
if c%2==0:
    t=c//2
    print(a-t)
else:
    print("-1")
