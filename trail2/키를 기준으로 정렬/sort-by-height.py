n = int(input())
name = []
height = []
weight = []

class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
student1 = []
for i in range(n):
    student1.append(Student(name[i], height[i], weight[i]))
    

student1.sort(key=lambda x: x.height)

for student in student1:
    print(student.name, student.height, student.weight)