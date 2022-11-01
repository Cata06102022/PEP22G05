# my_list = ["Masa", 5, "Scaun", 4.5, [5,6,7], 8]
# for obj in my_list:
#     print(obj)

# # ex6
# cuvant = input("spune-mi un cuvant")
# x = cuvant[0].lower()
# y = 0
# for i in cuvant:
#     if x == i:
#         y += 1
# print(x, "Apare de", y, "ori")

cuvant = input ("Introduceti un cuvant fara majuscule:")
x = list(cuvant)
y = x.count(x[0])
print(y)


# for i in x:
#     if i ==x[0]
#         n+=1
#         print(f"{x} apare de {n} ori")