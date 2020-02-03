string = "Daniel is a Javascript Programmer who loves to play with code."
string = string.split()

# Delete word using remove
string.remove('who')
## Delete word uing pop
string.pop()
### Delete using keyword delete
del string[0]

## Sort list
string.sort()

## Add new words to the list
string.append("show")
string + ["tolu"]
string.insert(1, "daniel")

## Turn the list into words
string = " ".join(string)

print(string)
### output: Javascript daniel Programmer a is loves play to with show



##Part 2
# Nested List: [[1,2,3], [4,5,6],[7,8,9]]
# * Operator
print(3 * [1,2,3])
#list slices
a_list = "Daniel"
print(a_list[0:3])

#output: Dam

# += operator
a = [1,2,3]
a += [4]
print(a)
#output [1,2,3,4]


## A list filter
a = [1, 0, -9, 8, 0, -1]

def removeNegative(number):
    if number < 0:
        return False
    return True

newlist = filter(removeNegative, a)
for i in newlist:
    print(i)

### Legal but does the wrong this
new_copy = [1,3,4,5,6]
another_list = []
for i in new_copy:
    if i < 5:
       another_list = new_copy.pop(i)
print(another_list)

## THsi will return error, the opration is legal but pop usings index of a list so if the number is higher than the lenght if will throw index out of range error
