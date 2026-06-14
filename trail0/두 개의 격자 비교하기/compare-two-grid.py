N, M = map(int, input().split())
list_a = [list(map(int, input().split())) for _ in range(N)]
list_b = [list(map(int, input().split())) for _ in range(N)]

ans = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if list_a[i][j] == list_b[i][j]:
            ans[i][j] = 0
            print(ans[i][j], end=" ")
        elif list_a[i][j] != list_b[i][j]:
            ans[i][j] = 1
            print(ans[i][j], end=" ")
    print()
   


