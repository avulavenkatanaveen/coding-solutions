# cook your dish here
T = int(input())

for _ in range(T):
    x = int(input())
   
    if x % 3 == 0:
        print("NORMAL")
    elif x % 3 == 1:
        print("HUGE")
    else:
        print("SMALL")