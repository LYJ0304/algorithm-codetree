n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
cnt = []
for _ in range(n):
    cnt.append(0)

for i, j in commands:
    for z in range(i-1, j):
        cnt[z] += 1

ans = max(cnt)
print(ans)