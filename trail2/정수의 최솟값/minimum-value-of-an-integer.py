a, b, c = map(int, input().split())

# Please write your code here.
def min_num(a, b, c):
    if a >= b and c >= b:
        return b
    elif a >= c and b >= c:
        return c
    elif b >= a and c >= a:
        return a


print(min_num(a, b, c))