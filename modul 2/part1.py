# Output functions
print('Hello world')

# Input functions
# input('Say Hello: ')

# Variables
my_name = 'Emanuel'
print(my_name)
my_number = 1_000_000
print(my_number)

# type function
result = type(10)
print (result)

# return of print
result = print('example')
print(result)

# return of input
result = input('Say Hello: ')
print(result)

# print multiple args
print('Emanuel', 'Ion', 'Illia')


# casting
result = 'abcd'

result = str(result)
print(result)

result = 10
result = str(result)
print(type(result))

# Operatii

# comparation
a = 100
b = 100
print(a == b)
print('ID of a is:' , id(a))
print('ID of b is:' , id(b))
print(a is b)

c = "/abcd"
d = "/abcd"
print(c == d) #ca valoare
print('ID of c is:' , id(c))
print('ID of d is:' , id(d))
print(c is d) #ca identitate

# slice
a = 'my_text'
print(a[1]) #se printeaza caracterul "y", incepem de la 0, Y este al doilea caracter
print(a[1])
print(a[1:3])
print(a[1:6])
print(a[1:7])
print(a[1:])
print(a[:6])
print(a[:6:2]) #step de 2 (m_e)

#  -7-6-5-4-3-2-1
#a 'm y _ t e x t'
a = 'my_text'
print(a[-1])
print(a[-6:-1])
print(a[-1:-6:-1]) #pas negativ

b = 'This is my reverse text'
print(b[::-1]) #cu un pas negativ, il parcurgem de la dreapta la stanga


print('aaabcaaa'.strip('a')) # afiseaza bc
print('aaabcaaa a'.strip('a')) # afiseaza bcaaa
print('  ab  '.strip(' ')) #sterge spatiile din sir






