n = int(input())

# Please write your code here.
def magic_num(n):
    ten_num = n // 10
    one_num = n - (ten_num * 10)
    cnt = ten_num + one_num
    if n % 2 == 0 and cnt % 5 == 0:
        return True
    else:
        return False

if magic_num(n):
    print("Yes")
else:
    print("No")