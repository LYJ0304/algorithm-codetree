n = int(input())

# Please write your code here.

def zero(n):
    if n == 0:
        return
    zero(n-1)
    print(n, end=" ")

def one(n):
    if n == 0:
        return
    print(n, end=" ")
    one(n-1)

zero(n)
print()
one(n)