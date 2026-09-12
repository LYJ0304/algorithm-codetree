N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here
cnt = []
for i in range(N):
    if command[i] == "push_back":
        cnt.append(num[i])

    elif command[i] == "pop_back":
        cnt.pop()
    
    elif command[i] == "size":
        print(len(cnt))
    
    elif command[i] == "get":
        print(cnt[num[i]-1])