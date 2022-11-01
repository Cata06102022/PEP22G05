# """"
# Create app that is able to respond with the provided name
#
# Hi Bob,
# >>> My name is Jhon:
# Hi Jhon!
#
# All of this will be in a function
#
# """

# def functie():
#     print('Hi Bob, ')
#     name = input ('My name is ')
#     print('Hi ', name)




def robot():
    name = 'Bob'
    def functie():
        nonlocal name
        print('Hi', name)
        name = input('My name is ')
        print('Hi ', name)

    functie()

    def weather():
        vreme = input('How is the weather')
        print("For ", name, "the weather is ", vreme.split()[-1])
    weather()

robot()