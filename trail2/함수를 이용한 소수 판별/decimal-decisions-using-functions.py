a, b = map(int, input().split())
ans = 0
# Please write your code here.
def find_num(i):
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            return False

    return True
    

for i in range(a, b+1):
    if find_num(i):
        ans += i

print(ans)
                 

