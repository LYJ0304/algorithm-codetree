MAX_N = 5

class valid_nums:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append(valid_nums(codename, int(score)))

# Please write your code here.
min_user = min(users, key=lambda user: user.score)
print(min_user.codename, min_user.score)

