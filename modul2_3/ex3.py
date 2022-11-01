cappucino = 4
espresso = 3.5
print(f'1. Cappucino...{cappucino} lei')
print(f'2. Expresso...{espresso} lei')
optiune = input("Ce optiune alegeti? [1,2]").strip()
optiune = int(input ('Selecteaza 1 sau 2.'))
while not 1 <= optiune <= 2:
    optiune = int(input('Select 1 or 2.'))
bancnota = int(input("Introduceti o bancnota [5 lei, 10 lei]"))
print(optiune)
if optiune == 1:
    rezultat = bancnota - cappucino
elif optiune == 2:
    rezultat = bancnota - espresso
else:
    rezultat = bancnota
print(f"Vei primi restul de {rezultat}")
print('Produsul se livreaza...')

