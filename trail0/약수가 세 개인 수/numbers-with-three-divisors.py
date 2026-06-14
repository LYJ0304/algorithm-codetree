start, end = map(int, input().split())

# Please write your code here.
sum = 0
for i in range(start, end+1):
    a = 0
    for j in range(1, i+1):
        if i % j == 0:
            a += 1
    if a == 3:
        sum += 1


print(sum)