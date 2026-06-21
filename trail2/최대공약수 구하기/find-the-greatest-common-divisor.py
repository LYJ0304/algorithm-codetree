n, m = map(int, input().split())

# Please write your code here.
def print_gcd(m, n):
    cnt = 0
    a = 0
    for i in range(m+1, cnt, -1):
        if m % i == 0 and n % i == 0:
            a = i
            break

    print(a)

print_gcd(m, n)
