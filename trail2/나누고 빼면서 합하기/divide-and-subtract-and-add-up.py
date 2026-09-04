n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def valid_num(n, m, A):
    cnt = 0
    while True:
        if m == 1:
            cnt += A[m-1]
            break
        else:
            if m % 2 == 0:
                cnt += A[m+-1]
                m = m//2
            elif m % 2 != 0:
                cnt += A[m-1]
                m -= 1
    return cnt
print(valid_num(n, m, A))