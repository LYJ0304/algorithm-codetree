n = int(input())
name = []
korean = []
english = []
math = []

class Subject:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here
subjects = []
for i in range(n):
    subjects.append(Subject(name[i], korean[i], english[i], math[i]))

subjects.sort(key=lambda x: (-x.korean, -x.english, -x.math))
for subject in subjects:
    print(subject.name, subject.korean, subject.english, subject.math)