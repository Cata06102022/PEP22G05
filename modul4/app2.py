def ridicare_la_putere(a, b):
    return int(a)**int(b)     #a la puterea b
def putere():
    while True:
        data = input('Please insert numbers!')
        if data == 'q':
            break       # daca apesi "q", se opreste rularea programului, altfel cere sa introduci cifrele la infinit
        a, b = data.split(',')
        print('Result is a la puterea b.', ridicare_la_putere(a, b))
putere()

