n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
for j in nums:
    print(j, end=" ")
print()
nums.sort(reverse=True)
for i in nums:
    print(i, end=" ")
