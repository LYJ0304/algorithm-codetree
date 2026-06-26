Y, M, D = map(int, input().split())

# Please write your code here.
def find_leap_year(Y):
    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                return True
            else:
                return False
        return True
        
    else:
        return False

def find_season(M):
    if M in [3, 4, 5]:
        return "Spring"
    elif M in [6, 7, 8]:
        return "Summer"
    elif M in [9, 10, 11]:
        return "Fall"
    elif M in [1, 2, 12]:
        return "Winter"
    else:
        return 0

def validate_date(Y, M, D):
    if M in [1, 3, 5, 7, 8, 10, 12]:
        if D > 31:
            return False
        else:
            return True
    elif M in [4, 6, 9, 11]:
        if D > 30:
            return False
        return True
    elif M == 2:
        if find_leap_year(Y):
            if D > 29:
                return False
            else: 
                return True
        else:
            if D > 28:
                return False
            else:
                True
    else:
        return False

if validate_date(Y, M, D):
    print(find_season(M))
else:
    print(-1)