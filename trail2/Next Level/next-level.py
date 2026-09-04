user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class user_info:
    def __init__(self, id, level):
        self.id = id
        self.level = level

user2_info = user_info("codetree", 10)
print("user " + user2_info.id + " lv " + str(user2_info.level))
user3 = user_info(user2_id, user2_level)
print("user " + user3.id + " lv " + str(user3.level))
