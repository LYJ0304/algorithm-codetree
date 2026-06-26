a, b = map(int, input().split())

# Please write your code here.
cnt = 0
def find_prime_num(a):
    if a < 2:
        return False
    
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

    
def find_num_sum(a):
    ten_num = a // 10
    one_num = a % 10
    sum_num = ten_num + one_num
    if sum_num % 2 == 0:
        return True
    else:
        return False
         


while a <= b:

    if find_prime_num(a) and find_num_sum(a):
        cnt += 1
        a += 1
    else:
        a += 1

print(cnt)