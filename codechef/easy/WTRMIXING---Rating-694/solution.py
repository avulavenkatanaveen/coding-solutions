# cook your dish here
t = int(input())
for _ in range(t):
    a,b,x,y = map(int, input().split())
    if a <= b and (b - a) <= x:
        print("YES")
    elif a > b and (a - b) <= y:
        print("YES")
    else:
        print("NO")