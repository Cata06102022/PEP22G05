# String and String methods
my_var = 'Emanuel'

my_str = u"abcd {} \n" #unicode string
print(my_str)

my_str = f"My name is {my_var}" #formated string
print(my_str)

my_str = r"abcd {1} \n \{2} \" " #raw string
print(my_str)

result = my_str.capitalize() #salvam string-ul intr-o variabila
print(result)

result = my_str.split('\\') #imparte string-ul dupa linii noi, spatiu etc.
print(type(result))
print(result)

result = my_str.format('x', 'y', 'z')
print(result)

result = my_str.center(80)
print(result)

result = 'abdc'.center(6, '#')
print(result)

txt = "Hello my friends"
x = txt.upper()
print(x)

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
