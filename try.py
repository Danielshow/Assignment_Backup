def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

print(any_lowercase1("Daniel"))
### Output: False

### This function returns incorrect result because it will loop through the the word input and will only take the first letter into consideration
### if the first letter is lowercase it will return true if not it will return false, the first letter is the determinant of this function.

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

print(any_lowercase2("Text"))
#### Output: True

### This function will return an incorrect result, The function is looping through the word but it not iusing any of the letters but it is using letter 'c'
### to check if it is lower or not. The function is also not returning True or False as a Boolean but as a string which is not what is expected. This function
### will always return 'True' as a string

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

print(any_lowercase3("TexT"))
### Output: False

### This function will yield an incorrect answer because the result is based on the last letter in the word (parameter) giving. It will loop through each word and
### will change the variable flag always, flag will result to true if the last letter is a lowercase and false if it is an upper case letter

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

print(any_lowercase4("TTaaa"))
## Output: True

#### This function will yield the correct result, it will loop through the input provided and assign the result of calling islower to flag but will also consider the last input
#### Using or will make sure if any of the letters is true, flag will always remain true till the end of the computation.

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase5("aT"))
## output: False

#### THis function will return an incorrect result, it will loop through the input, if one of the input is an upper case letter, it will return False. If none of the letter of the input
#### is a upper case letter it will return true.
