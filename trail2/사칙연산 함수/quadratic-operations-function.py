a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def cal_num(a, o, c):
    if o == "+":
        return a + c
    elif o == "-":
        return a - c
    elif o == "/":
        return a // c
    elif o == "*":
        return a * c
    else:
        return None

ans = cal_num(a, o, c)
if ans is None:
    print("False")
else:
    print(f"{a} {o} {c} = {ans}")