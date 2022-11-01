my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = 1, 2, 3
print(type(my_tuple))

my_tuple = 1,   # este un tuple
print(type(my_tuple))

a = 5
b = 3
a, b = b, a # a, b = (b, a) or (a, b) = b, a
print(a, b)


# unpack variables in tuple
a = 5
b = 3
c = 7
d = 11
# f = 13
# a, b, c, d = d, c, b, a
# print (a, b, c, d)

a, *var, d = d, c, b, a
print(a, d)
print(var)

def test_function(*args, **kwargs):
    print('Args:', args)
    print('Kwargs:', kwargs)

test_function(1, 2, 3, 4, 5, {1: 2}, end='\n', next = (123,), )
test_function(1, 2, 3, 4, 5, *(6, 7), **{'a': 2}, end='\n', next = (123,))