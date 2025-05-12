# Problem: Josephus Problem - https://www.geeksforgeeks.org/josephus-problem/

def Josephus(n, k):
    i = 1
    ans = 0
    while(i <= n):
        ans = (ans + k) % i
        i += 1
    return ans + 1
n = 14
k = 2
result = Josephus(n, k)
print(result)
