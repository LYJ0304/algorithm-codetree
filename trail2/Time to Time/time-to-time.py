a, b, c, d = map(int, input().split())

# Please write your code here.
b += a * 60
d += c * 60

ans = d - b
print(ans)