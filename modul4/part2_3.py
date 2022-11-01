# exception

# print(1/0)

def div(number1, number2):
    result = 'infinit'
    try:
        result = number1 / number2
    except TypeError:
        print('not possible for string')
        # return None
        result = None
    except ZeroDivisionError:
        print('not possible do divide by 0')
    except:
        raise
    return result

# div(1, 0)
print(div(1, 0))
print(div('1', 10))
