N = int(input())
ans = 1

for i in range(1, N+1):
    for j in range(i):
        print(ans, end=" ")
        ans += 1

    print()

        
         