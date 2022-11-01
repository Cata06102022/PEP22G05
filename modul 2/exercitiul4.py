# Se cere input de la utilizator cu venit net pe luna. Din acesta, calculati regula 50/30/20:
# - 50% din venit acordat necesităților (cumparaturi, intretinere, chirie, etc)
# - 30% din venit acordat scopurilor recreative
# - 20% din venit acordat datoriilor și economiilor
# Venit: 2875
# Recomandarile noastre:
# Cheltuieli uzuale: 1437.5
# Recreere: 862.5
# Economii si datorii: 575.0


a = int(input('venitul net'))
b = a * 50/100
print('cheltuieli necesar' , b)
c= a * 30/100
print('Recreative' ,c)
d= a * 20/100
print ('Economii', d)