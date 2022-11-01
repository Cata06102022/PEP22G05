# 1.Se cere un script care sa calculeze media de varsta a unor participanți la un sondaj deopinie.
# Cerinte:a.Se cere input de la utilizator numărul de participanți. Dacă utilizatorul introduceun răspuns invalid, se va trata eroarea cu ajutorul excepțiilor
# și i se va cere în mod repetat numărul de participanți pana cand acesta este unul valid.
# b.Pentru fiecare participant, se va cere varsta. Dacă varsta nu a fost introdusăcorect, i se va cere din nou varsta pentru același participant.
# c.Media varstelor se va face printr-o funcția dedicată acestui lucru, prin pasareaunei liste care contine toate varstele ca parametru.
# Exemplu output:Cati participanti avem la sondaj?4Introduceti varsta participantului
# 1:22Introduceti varsta participantului 2:tNu ati introdus un format valid la participantul
# 2.Introduceti varsta participantului 2:34Introduceti varsta participantului
# 3:45Introduceti varsta participantului 4:22tNu ati introdus un format valid la participantul
# 4.Introduceti varsta participantului 4:45Media de varsta a participantilor la sondajul de opinie este: 36.5

def sondaj():
    varste_participanti = []
    nr_part = int(input(f'Introduceti numar participanti:'))
    for nr in range(1, nr_part + 1):
        try:
            var_part = int(input(f'Introduceti varsta participantului, {nr}'))
        except ValueError:
            print('Valoarea introdusa este incorecta.')
            var_part = int(input(f'Introduceti varsta participantului, {nr}'))
            varste_participanti.append(var_part)
    print('Media de varsta este:', sum(varste_participanti) / len(varste_participanti))

sondaj()