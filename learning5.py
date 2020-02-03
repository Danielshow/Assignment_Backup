prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if (letter == 'Q' or letter == 'O'):
       print(letter + 'u' + suffix)
    else:
       print(letter + suffix)



def firstFive(word):
    return word[0:5]

print(firstFive("Daniel"))


def transformFirstLetter(word):
    return word[0].upper() + word[1:]

print(transformFirstLetter("d"))


def find_first_letter_position(word, letter):
    position  = 1
    for i in word:
        if i.lower() == letter.lower():
            return position
        position += 1
    return (letter + " is not in " + word)


print(find_first_letter_position("daniel", "D"))
