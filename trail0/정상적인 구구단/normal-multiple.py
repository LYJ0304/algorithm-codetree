N = int(input())

for i in range(1, N + 1):
    for j in range(1, N+1):
        if j == N:
            print("{0} * {1} = {2}".format(i, j, i*j))
        else:
            print("{0} * {1} = {2}".format(i, j, i*j), end=", ")