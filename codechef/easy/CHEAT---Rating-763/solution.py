# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    if n<2:
        print(0)
    else:
        print((n-2)//7+1)