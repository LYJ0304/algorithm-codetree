A = input()

# Please write your code here.
def find_pel(str):
    pel = ""
    for i in str:
        pel = i + pel
    if str == pel:
        return True
    else:
        return False
    

if find_pel(A):
    print("Yes")
else:
    print("No")