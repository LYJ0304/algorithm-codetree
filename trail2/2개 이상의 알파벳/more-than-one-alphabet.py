A = input()

# Please write your code here.
def find_str(str):
    set_num = set(str)
    if len(set_num) >=  2:
        return True
    else:
        return False


if find_str(A):
    print("Yes")
else:
    print("No")