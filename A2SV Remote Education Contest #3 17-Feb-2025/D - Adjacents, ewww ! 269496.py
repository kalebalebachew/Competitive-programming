# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 2:
        print(-1)
        continue
    if n == 1:
        print(1)
        continue
    
    tot = n * n
    
    ev = [num for num in range(1, tot + 1) if num % 2 == 0]
    od = [num for num in range(1, tot + 1) if num % 2 == 1]
    
    nums = ev + od
    
    mat = []
    idx = 0
    for i in range(n):
        row = []
        for j in range(n):
            row.append(nums[idx])
            idx += 1
        mat.append(row)
    
    for row in mat:
        print(" ".join(map(str, row)))
