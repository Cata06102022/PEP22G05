# 3! = 1*2*3
def factorial(number, limit): # functia factorial, iar in paranteze avem un argument
    print(number) #argumentul devine variabila
    result = 1
    for i in range(1, number + 1):
        if result > limit:
            return result   # this stops function execution
        result *= i
    return result #result este declarat in interiorul functiei

result = factorial(100, 1000)
print('Result is: ', result)