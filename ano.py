alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"]
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

## Part 1
def has_duplicates(letter):
    letter = histogram(letter)
    for i in letter:
        if letter[i] > 1:
            return True
    return False

for string in test_dups:
    if has_duplicates(string):
        print(string + ' has duplicates')
    else:
        print(string + ' has no duplicates')


## Part 2
def missing_letters(string):
    string = histogram(string)
    answer = ''
    for i in alphabet:
        if i not in string:
            answer += i
    return answer

for letter in test_miss:
    if len(missing_letters(letter)) > 0:
        print(letter + ' is missing letters ' + missing_letters(letter))
    else:
        print(letter + ' uses all the letters')
