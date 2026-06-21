n, m = map(int, input().split())

# Please write your code here.
def min_same(a, b):
    i = 1

    while (a * i) % b != 0:
        i += 1
    print(a * i)

min_same(n, m)