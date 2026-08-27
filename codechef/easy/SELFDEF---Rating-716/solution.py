# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    ages=list(map(int,input().split()))
    c=0
    for age in ages:
        if 10<= age <= 60:
            c+=1
    print(c)