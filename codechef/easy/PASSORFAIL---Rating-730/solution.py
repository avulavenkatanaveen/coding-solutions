# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if (a>=b and a<=c) or (a<=b and a>=c):
        second=a
    elif (b>=a and b<=c) or (b<=a and b>=c):
        second=b
    else:
        second=c
    print(second)
        