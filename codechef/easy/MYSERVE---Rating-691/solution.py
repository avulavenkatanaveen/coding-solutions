t=int(input())
for _ in range(t):
    p,q=map(int,input().split())
    if p==q:
        print("Alice")
    else:
        print("Bob")