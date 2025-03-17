# Problem: B - The Time Heist’s Single-Shot Maneuver - https://codeforces.com/gym/596004/problem/B

t = int(input())
res=[]
for _ in range(t):
  n,m=map(int,input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))

  b1=b[0]
  possible=True
  prev=-float('inf')

  for ai in a:
    c1=ai
    c2=b1-ai
    candidates=[]
    if c1>=prev:
      candidates.append(c1)
    if c2>=prev:
      candidates.append(c2)
    if not candidates:
      possible=False
      break
    prev=min(candidates)

  res.append("YES" if possible else "NO")
print("\n".join(res))