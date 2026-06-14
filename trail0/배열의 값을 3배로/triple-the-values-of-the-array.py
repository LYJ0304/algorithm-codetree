a = []
for _ in range(3):
    b = list(map(int, input().split()))
    a.append(b)

for i in range(3):
    for j in range(3):
        print(a[i][j] * 3, end=" ")
    print()