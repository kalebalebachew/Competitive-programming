# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

merged = []
l = 0  
r = 0  
while l < n and r < m:
    if arr1[l] <= arr2[r]:
        merged.append(arr1[l])
        l += 1
    else:
        merged.append(arr2[r])
        r += 1
while l < n:
    merged.append(arr1[l])
    l += 1

while r < m:
    merged.append(arr2[r])
    r += 1

print(*merged)