numar = range(int(input("Input utilizator:")))
for i in numar:
    result = i % 2
    if result == 0:
        print(i)

numar = range(int(input("Input utilizator:")))
for i in numar:
    result = i % 2
    if result != 1:
        print(i)
