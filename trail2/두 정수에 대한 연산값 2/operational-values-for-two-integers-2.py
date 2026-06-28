a, b = map(int, input().split())

# Please write your code here.
def big_num(big):
    return big * 2

def small_num(small):
    return small + 10

if a > b:
    print(big_num(a), end=" ")
    print(small_num(b))
else:
    print(small_num(a), end=" ")
    print(big_num(b))