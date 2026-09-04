secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class info:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

information = info(secret_code, meeting_point, time)
print("secret code : " + information.secret_code)
print("meeting point : " + information.meeting_point)
print("time : " + str(information.time))