n = int(input())

# Please write your code here.
def print_num(n) -> int:
    cnt = 0
    for i in range(1, n + 1):
        cnt += i

    return cnt // 10

print(print_num(n))