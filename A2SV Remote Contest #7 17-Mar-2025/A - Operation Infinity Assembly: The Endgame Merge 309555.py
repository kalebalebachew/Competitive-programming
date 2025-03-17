# Problem: A - Operation Infinity Assembly: The Endgame Merge - https://codeforces.com/gym/596004/problem/A

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(input().strip())
    b = list(input().strip())
    a.sort()
    b.sort()
    c = []
    ca = 0  
    cb = 0  
    while a and b:
        if (a[0] < b[0] and ca < k) or cb == k:
            c.append(a.pop(0))
            ca += 1
            cb = 0  
        else:
            c.append(b.pop(0))
            cb += 1
            ca = 0  
    print("".join(c))
