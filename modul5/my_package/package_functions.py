def factorial(limit):
    result = 1
    for i in range(1, limit+1):
        result *= i
    return result

my_imported_var = 'Imported'


print(__name__)
print(__package__)
if __name__ == "__name__":
    print('Print from module', factorial(5))