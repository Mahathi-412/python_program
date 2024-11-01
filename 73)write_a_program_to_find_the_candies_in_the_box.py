T = int(input())
N = int(input())
C = list(map(int,input().split()))
l = []
s = C[0]
for i in range(1,N):
    s = s+C[i]
    l.append(s)
print(sum(l))
