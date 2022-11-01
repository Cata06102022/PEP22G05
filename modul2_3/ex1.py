cnp = input("introduceti primele 7 cifre din cnp:")
cnp_an = int(cnp[1:3])
cnp_luna = int(cnp[3:5])
cnp_zi = int(cnp [5:7])
azi_zi = 20
azi_luna = 10
azi_an = 2022
if cnp_an >45:
    cnp_an = 1900+cnp_an
else:
    cnp_an= 2000 +cnp_an
if((2022- cnp_an)>18):
    print("Felicitari ai 18 ani!")
elif (2022-cnp_an ==18):
    if(cnp_luna < 10):
        print("Felicitari ai implinit 18 ani anul acesta!")
    elif(cnp_luna == 10):
        if(cnp_zi <=20):
            print("Felicitari ai implinit 18 ani luna acesta!")
        else:
            print("Imi pare rau nu ai implinit 18 ani!")
    else:
        print("Imi pare rau nu ai implinit 18 ani!")
else:
    print("Imi pare rau nu ai implinit 18 ani!")
print(cnp_an, cnp_luna, cnp_zi)

