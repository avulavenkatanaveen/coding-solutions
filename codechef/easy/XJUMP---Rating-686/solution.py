t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    c=(x//y)+(x%y)
    print(c)
