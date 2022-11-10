# Creați un script pentru profesori pentru a calcula notele studentilor:
# - Se ia input de la utilizator cu numele studentului
# Introdueti numele elevului: Ana Popescu
# - Se ia input de la utilizator cu un șir de note separate prin virgulă și se transforma
# într-o listă
# Introduceti notele elevului separate prin virgula: 5.5,8.3,9
# ['5.5', '8.3', '9']
# - În cazul în care utilizatorul nu a introdus nici o nota, se va afișa o eroare cu
# ajutorul cuvantului cheie assert, si se va termina programul
# - Tratați toate erorile care ar putea sa apara în timpul rulării programului
# - Dacă media calculata este mai mare de 5, se va afisa:
# Media este: 6.8
# Ana Popescu a trecut clasa.
# - Dacă media calculata este mai mica de 5, se va afisa:
# Media este: 4.34
# Ana Popescu a picat clasa.
# Sample output:
# Introdueti numele elevului: Ana Popescu
# Introduceti notele elevului separate prin virgula: 5.6,4.2,8,7.6
# Media este: 6.35
# Ana Popescu a trecut clasa.

nume = input("Introduceti numele:")
str_note = input("Introduceti notele elevului separate prin virgula:")
str_note = str_note.replace(" ", "")
assert str_note, "Nu ai dat nicio nota!"    # verifica daca str_note is True-ish
note = str_note.split(",")
lista_note =[]
for nota in note:
    try:
        lista_note.append(int(nota))
    except ValueError:
        print("introduceti note 1-10!")
print(lista_note)
media = sum(lista_note)/len(lista_note)
print("media = ", media)
if media>=5:
    print(f"{nume} a trecut clasa!")
else:
    print(f"{nume} nu a trecut clasa!")