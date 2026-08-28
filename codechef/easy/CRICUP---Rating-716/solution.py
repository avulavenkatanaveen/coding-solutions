# cook your dish here
t=int(input())
for _ in range(t):
    x,y,d=map(int,input().split())
    a=abs(x-y)
    if a<=d:
        print("YES")
    else:
        print("NO")
    
