# binary chars

# 10 = 0000 1010
# 10 =
# 1010, sunt 4 biti, 2^4=16 caractere pot fi stocate in 4 biti.
# 10 = 0    A
# 10 = 0    01234567    10 11 12

a_number = ord('a')
# a_number = ord('\200b')
A_number = ord('A')
# bin(A_number)
# print(a_number.to_bytes(8))
print(bin(A_number))
print(bin(a_number))


print(max('abcd'))  # d are valoarea numerica cea mai mare, in ASCII code
print(max('AabcdZ!'))


letter1 = chr(70)
# a_number = ord('\200b')
letter2 = chr(33)   #32 este spatiu, 33 este !
print(letter1, letter2)

print('10 xor 10', 10 ^ 10)

# 0000 1010 ^
# 0000 1000 = 8
# 0000 0010 ^
# 0000 1000 = 8
# 0000 1010

print('10 xor 10', (10 ^ 150)^150)

print(80*"#")   #print # de 80 de ori
my_message = "This is my message."
encrypted_result = ''
for letter in my_message:
    encrypted_result +=chr(ord(letter) ^ 48)
print(encrypted_result)

decrypted_result = ""
for letter in encrypted_result:
    decrypted_result += chr(ord(letter) ^48)
print(decrypted_result)




