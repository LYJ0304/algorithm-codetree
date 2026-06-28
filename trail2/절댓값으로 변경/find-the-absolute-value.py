n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def print_abs(arr):
    for i in arr:
        print(abs(i), end=" ")

print_abs(arr)