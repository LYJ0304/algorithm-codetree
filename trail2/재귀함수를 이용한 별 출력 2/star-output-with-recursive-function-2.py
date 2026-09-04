n = int(input())

# Please write your code here.
def print_star(n):
    if n < 1:
        return
    print("* " * n)
    print_star(n-1)
    print("* " * n)

print_star(n)