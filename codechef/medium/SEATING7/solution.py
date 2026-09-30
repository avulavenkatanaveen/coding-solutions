# cook your dish here
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    lst=set(map(int,input().split()))
    r=[]
    s=1
    for _ in range(k):
        while s in lst:
            s+=1
            r.append(s)
            lst.add(s)
            s+=1
    print(*r)