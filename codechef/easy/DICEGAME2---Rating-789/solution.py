# cook your dish here
t=int(input())
for _ in range(t):
    a1,a2,a3,b1,b2,b3=map(int,input().split())
    c=min(a1,a2,a3)
    d=min(b1,b2,b3)
    a=a1+a2+a3-c
    b=b1+b2+b3-d
    if a>b:
        print("Alice")
    elif a==b:
        print("Tie")
    else:
        print("Bob")