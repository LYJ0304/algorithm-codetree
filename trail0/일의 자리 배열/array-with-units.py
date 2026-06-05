a = list(map(int, input().split()))

for i in range(1, 9):
    if a[i-1] + a[i] >= 10:
        a.append((a[i-1] + a[i]) - 10)
    else:
        a.append(a[i-1] + a[i])

for j in a:
    print(int(j), end=" ")