M, D = map(int, input().split())

# Please write your code here.
# 31 => 1, 3, 5, 7, 8, 10, 12
def validate_month(M, D):
    if M in [1, 3, 5, 7, 8, 10, 12]:
        if D > 31:
            return False

    elif M in [4, 6, 9, 11]:
        if D > 30:
            return False
    elif M == 2:
        if D > 28:
            return False
    else:
        return False
    return True


if validate_month(M, D):
    print("Yes")
else:
    print("No")