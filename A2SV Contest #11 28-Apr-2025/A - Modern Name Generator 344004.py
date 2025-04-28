# Problem: A - Modern Name Generator - https://codeforces.com/gym/605795/problem/A

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b, c = input().split()
    print(a[0] + b[0] + c[0])
