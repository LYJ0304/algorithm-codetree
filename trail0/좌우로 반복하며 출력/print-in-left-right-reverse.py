N = int(input())

for i in range(N):
    row = []
    cnt = 1
    for j in range(N):
        row.append(cnt)
        cnt += 1
    if i % 2 == 1:
        row.reverse()
    for j in range(N):
        print(row[j], end="")
    print()
        