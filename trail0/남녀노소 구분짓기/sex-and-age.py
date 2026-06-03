gen = int(input())
age = int(input())

if gen == 0:
    if age >= 19:
        print("MAN")
    else:
        print("BOY")
elif gen == 1:
    if age >= 19:
        print("WOMAN")
    else:
        print("GIRL")