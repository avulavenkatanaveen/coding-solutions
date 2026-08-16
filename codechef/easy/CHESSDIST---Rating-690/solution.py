# cook your dish here
t=int(input())
for _ in range(t):
    x1,x2,y1,y2=map(int,input().split())
    a=abs(x1-y1)
    b=abs(x2-y2)
    print(max(a,b))
    