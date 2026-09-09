# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=input().strip()
    b=input().strip()
    
    cA_a=a.count('a')
    cA_b=a.count('b')
    cB_a=b.count('a')
    cB_b=b.count('b')
    
    if cA_a==cB_b and cA_b==cB_a:
        print("YES")
    else:
        print("NO")