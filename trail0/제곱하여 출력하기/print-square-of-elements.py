N = int(input())
n_list = list(map(int, input().split()))

for i in range(N):
    print(n_list[i]**2, end=" ")