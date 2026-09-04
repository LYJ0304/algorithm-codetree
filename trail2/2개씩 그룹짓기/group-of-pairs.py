n = int(input())
nums = list(map(int, input().split()))

# Please write your code here
def sort_num(n, nums):
    cnt = []
    nums.sort()
    for i in range(len(nums)):
        cnt.append(nums[i]+nums[len(nums)-i-1])
    return max(cnt)



print(sort_num(n, nums))