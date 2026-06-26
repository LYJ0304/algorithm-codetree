a, b = map(int, input().split())

# Please write your code here.
def find_num(a, b):
    cnt = 0
    while a <= b:
        if a % 2 != 0:
            if a % 10 != 5:
                if a % 3 != 0 or a % 9 == 0:
                    a += 1
                    cnt += 1
                else:
                    a += 1
            else:
                a += 1
        else:
            a += 1
    return cnt

print(find_num(a, b))
