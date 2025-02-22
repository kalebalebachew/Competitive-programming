# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

matrix = []
for i in range(5):
    matrix.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            print(abs(i - 2) + abs(j - 2))
            break