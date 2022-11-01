# functions

# 3! = 1*2*3
def factorial(number): # functia factorial, iar in paranteze avem un argument
    print(number) #argumentul devine variabila
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result #result este declarat in interiorul functiei

# factorial(10)
# # print(result)  # does not exist outside function

result = factorial(10)
print('Result is: ', result)