import random


def game():
    states = {'p': 'piatra', 'f': 'foarfeca', 'h': 'hartie'}  # dictionar cu stari
    results = {'piatra-foarfeca': True, 'foarfeca-hartie': True, 'hartie-piatra': True, }

    options = list(states.keys())
    name = input('Introduceti numele: ')
    option = input('Introduceti optiunea [p (piatra),f (foarfeca) ,h (hartie), q pentru a iesi]: ')

    if option == 'q':
        print('Ati parasit jocul!')
        quit()
    else:
        selection = random.randint(0, 2)

        selected = options[selection]
        print(selected)
    if option not in options:
        print('Eroare, nu ai selectat optiunea!')
    print(f'> {name}:  {states[option]}')
    print(f'> Server:  {states[selected]}')
    if states[option] == states[selected]:
        print('Optiuni identice, incearca inca o data!')
        return None

    try:
        results[f'{states[option]}--{states[selected]}']
        print('Ai castigat!')
    except:
        print('Serverul a castigat!')


game()

""""Folosind modulul random, creați un script care sa simuleze jocul piatra-foarfeca-hartie.
Faceți scriptul într-un mod cat mai creativ, ca acesta sa para cat mai real. Sugestie de
output:
Introduceti numele: Ana
Introduceti optiunea [p (piatra),f (foarfeca) ,h (hartie), q
pentru a iesi]: f
> Ana: foarfeca
> Server: hartie
Ai castigat!
Introduceti optiunea [p (piatra),f (foarfeca) ,h (hartie), q
pentru a iesi]: f
> Ana: foarfeca
> Server: piatra
Serverul a castigat!
Introduceti optiunea [p (piatra),f (foarfeca) ,h (hartie), q
pentru a iesi]: h
> Ana: hartie
> Server: piatra
Ai castigat!
Introduceti optiunea [p (piatra),f (foarfeca) ,h (hartie), q
pentru a iesi]:"""
