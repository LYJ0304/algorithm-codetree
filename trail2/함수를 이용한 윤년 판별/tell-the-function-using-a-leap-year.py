y = int(input())

# Please write your code here.
def find_4(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        else:
            return True
    else:
        return False

if find_4(y):
    print("true")
else:
    print("false")
