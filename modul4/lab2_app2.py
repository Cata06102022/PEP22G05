# Se da urmatorul schelet de cod:
# def suma(lista: list):
# pass
# def medie(lista: list):
# pass
# def putere(lista: list):
# pass
# meniu = {
# "1": medie,
# "2": suma,
# "3": putere
# }
# Se cere:
# a. Input de la utilizator cu numere, care se vor aduna într-o listă cu elemente de tip
# float. Numerele trebuie sa fie valide. Cand utilizatorul nu mai are numere de
# introdus, va scrie x.
# Introduceti numere. Cand sunteti gata, introduceti x.
# Numar: 3
# Numar: 5
# Numar: 18.8
# Numar: 2
# Numar: 4
# Numar: x
# b. După introducerea numerelor, se va afișa un meniu cu 4 opțiuni: medie, suma,
# puterea numerelor din lista, iesire. În funcție de ce introduce utilizatorul, se va
# calcula rezultatul cu ajutorul funcțiilor din scheletul de mai sus și se va afișa.
# Meniu:
# 1. Media numerelor
# 2. Suma numerelor
# 3. Puterea numerelor din lista de numere
# 4. Iesire
# Introduceti optiunea dvs: 1
# Rezultatul: 6.56

def function():
    my_numbers = []
    print('Introduceti numere. Cand sunteti gata, introduceti x.')
    while True:
        try:
            data = int(input('Numar:'))
            my_numbers.append(data)
        except ValueError:
            break
    option = input("""Meniu:
1. Media numerelor
2. Suma numerelor
3. Puterea numerelor din lista de numere
4. Iesire
Introduceti optiunea dvs: """)

    def suma(lista: list):
        pass


    def medie(lista: list):
        pass


    def putere(lista: list):
        pass

    meniu = {
        "1": medie,
        "2": suma,
        "3": putere
    }
    result = meniu[option](my_numbers)
    print(f'Rezultatul: {result}')
function()