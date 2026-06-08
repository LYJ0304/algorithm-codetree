N = int(input())
num = 0
ans = 0
for i in range(1, 101):
    num += i
    
    if num >= N:
        ans = i
        break
        

print(ans)
    
