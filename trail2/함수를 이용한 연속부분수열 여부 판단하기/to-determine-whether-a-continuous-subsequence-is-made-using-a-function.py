n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def define_seq(a, b):
    for i in range(n1-n2+1):
        if a[i:i+n2] == b:
            return True
    return False

if define_seq(a, b):
    print("Yes")
else:
    print("No")
                
    

