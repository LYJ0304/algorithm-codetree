a, b = map(int, input().split())

# Please write your code here.
def big_num(big):
    big_num = big + 25
    return big_num
    
def small_num(small):
    small_num = small * 2
    return small_num

if a > b:
    print(big_num(a), end=" ")
    print(small_num(b))
else:
    print(small_num(a), end=" ")
    print(big_num(b))
    