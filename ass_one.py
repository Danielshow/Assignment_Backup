def reverse_str(word):
  # an iterator function that returns a list in reverse 
  word = reversed(word)
  # join is a function that joins a list
  return ''.join(word)


print(reverse_str('yes'))

#word: is the parameter
#yes in the function call is the argument

### Example 2
# Using a value
reverse_str('daniel')
# Using a variable
x = 'excellent'
reverse_str(x)
# Using an expression
reverse_str('word' + 'excellent')


### Example 3
## Area of a circle 
def circle_area(radius):
  pi = 3.142
  return pi * radius * radius

print(pi)

## Using a local variable outsides a function returns NameError because a local variable can only be used inside the function it is defined
# NameError: name 'pi' is not defined


### Example 4
def area_rectangle(length, breadth):
  return length * breadth

print(length)
#### Using the parameter outside the function returns NameError also, the sma eas Example 3

### Example 5
x = 3
def add_5(var):
  x = 5
  return var + x

#### A variable inside a function can only be used inside the function. As the function runs it only sees the local variable insides it
