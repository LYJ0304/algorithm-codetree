n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def sum_num(n, m, arr, queries):

    results = []
    for i in queries:
        cnt = 0
        a, b = i
        for j in range(a, b+1):
            cnt += arr[j-1]
        results.append(cnt)
    return results

for res in sum_num(n, m, arr, queries):
    print(res)