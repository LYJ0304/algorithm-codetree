n = int(input())

# Please write your code here.
def print_num(n):
    if n == 0:
        return
    print_num(n-1)
    print("HelloWorld")

print_num(n)