unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class bomb:
    def __init__(self, unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

bomb_1 = bomb(unlock_code, wire_color, seconds)
print("code :", bomb_1.unlock_code)
print("color :", bomb_1.wire_color)
print("second :", bomb_1.seconds)