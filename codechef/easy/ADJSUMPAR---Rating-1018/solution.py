from collections import Counter

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        freq = Counter(a)
        if max(freq.values()) >= 3:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    solve()