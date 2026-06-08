three = 0
five = 0

for i in range(10):

    a = int(input())
    if a % 3 == 0 and a % 5 == 0:
        three += 1
        five += 1
    elif a % 3 == 0:
        three += 1
    elif a % 5 == 0:
        five += 1
    
    else:
        continue

print(three, end=" ")
print(five)

