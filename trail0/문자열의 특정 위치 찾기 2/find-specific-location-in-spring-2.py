a = input()
aa = ["apple", "banana", "grape", "blueberry", "orange"]
num = 0
for i in aa:
    if i[2] == a or i[3] == a:
        num += 1
        print(i)


print(num)