a = [list(map(int, input().split())) for _ in range(4)]
cnt = 0

for i in range(4):
    for j in range(0, i+1):
        cnt += a[i][j]
        
print(cnt)