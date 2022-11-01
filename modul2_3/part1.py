a = 100
b = 100
if a > b:
    print('a is larger')
elif a > 50:
    print('a is grater then 50')
elif a > 60:
    print('a is grater then 60')
else:
    print('b is larger')

a = "101"
if a > '100':
    print('success >')
elif a == '100':
    print('success ==')

# chr() and ord()

print(ord('0'))
print(ord('1'))
print(ord('a'))
print(ord('A'))
print(chr(65))

# Thrueish

a = "101"
print(a> '100')

if True:
    print('this will always be true')
if a:
    print('this will always be true')

a = "" # string care nu contine caracter, este False, cel care contine minim un carater este True
if a:
    print('this will always be false')
else:
    print('a is False')

a = -2
if a:
    print('a is True')
else:
    print('a is False')


for i in result:
    print(i)
