n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def find_even(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num

for nums in arr:
    print(find_even(nums), end=" ")
    