# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    twos=n//2
    ones=n%2
    cost=(twos*30)+(ones*20)
    print(cost)