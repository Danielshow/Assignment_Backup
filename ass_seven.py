dic = open('input.txt')

for line in dic:
    d = eval(line)

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for item in val:
          if item not in inverse:
            inverse[item] = [key]
          else:
            inverse[item].append(key)
    open('new.txt', 'w').write(str(inverse))
    return inverse

print(invert_dict(d))

try:
    dic = open('iput.txt')
except:
    print('File does not exists')

try:
  d = open('input.txt')
  d.write('dddd')
except:
  print('Cannot write to this file')
