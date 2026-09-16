# cook your dish here
a,b=map(int,input().split())
c=a+b
if c%2==0:
    c=c/2
    print(c//2)
else:
    print("-1")
