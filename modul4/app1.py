# def num_there(string):
#     for letter in string:
#         if letter.isnumeric():
#                 return True
#
# def num_special(string: str):
#     for letter in string:
#         if not letter.isalnum():
#             return True
#
# def login():
#     a = input("Introduceti o parola care sa contina minim 7 caractere, contine o cifra si una dintre urmatoarele caractere: !, @, %.")
#     ask_again = False
#     while True:
#         if (len(a)) < 7:
#             print ('Parola prea scurta.')
#             ask_again = True
#         if num_there(a) != True:
#             print('Parola nu are cifra!')
#             ask_again = True
#         if num_special(a) != True:
#             print('Parola nu are caractere speciale!')
#             ask_again = True
#         if a != a.capitalize():
#             print('Prima litera nu este mare!')
#         if ask_again == False:
#             break
#         else:
#             a = input("Introduceti o parola care sa contina minim 7 caractere, contine o cifra si una dintre urmatoarele caractere: !, @, %.")
#
# result = login()
# print(result)

def num_there(string: str):
    for letter in string:
        if letter.isnumeric():
            return True

def num_special(string: str):
    for letter in string:
        if not letter.isalnum():
            return True

def login():
    a = input('Introducti o parola')
    while True:
        ask_again = False
        if (len(a)) < 7:
            print('Parola prea scurta')
            ask_again = True
        if num_there(a) != True:
            print('parola nu are cifra')
            ask_again = True
        if num_special(a) != True:
            print('parola nu are caractere speciale')
            ask_again = True
        if a != a.capitalize():
            print('prima litera nu este mare')
            ask_again = True
        if not a[0].isalpha():
            print('Prima litera nu este mare!')
        if ask_again == False:
            break
        else:
            a = input('Introducti o parola')

result = login()
print(result)