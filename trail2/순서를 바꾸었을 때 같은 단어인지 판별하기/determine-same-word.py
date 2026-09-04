word1 = input()
word2 = input()

# Please write your code here.
def valid_word(a, b):
    sorted_a = ''.join(sorted(a))
    sorted_b = ''.join(sorted(b))
    if sorted_a == sorted_b:
        return True
    else:
        return False

if valid_word(word1, word2):
    print("Yes")
else:
    print("No")