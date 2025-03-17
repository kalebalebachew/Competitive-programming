# Problem: D - The Snap of Fury - https://codeforces.com/gym/596004/problem/D

n = int(input())
l = list(map(int, input().split()))
diff  = [0] * (n+1)


for i in range(n):
    s = max(0, i - l[i])
    diff[s] += 1
    diff[i] -= 1
    
el = 0
sr = 0

for i in range(n):
    el += diff[i]
    if el == 0:
        sr += 1
print(sr)

    