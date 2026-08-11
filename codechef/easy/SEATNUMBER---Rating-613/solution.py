# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    if n<=10:
        print("Lower Double")
    elif n<=15:
        print("Lower Single")
    elif n<=25:
        print("Upper Double")
    else:
        print("Upper Single")