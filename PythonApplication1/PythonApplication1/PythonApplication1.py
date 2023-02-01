from random import *
arv = randint(1,1000000)
while True:
    if arv>9999 and arv<100000:
        print(arv)
        break
    else:
        arv = randint(1,1000000)
random = randint(1,100000)
random1 = randint(1,100000)
while True:
    if random1<random:
        for arv in range(random1,random):
            if arv>9999 and arv<100000:
                print(arv)
                break
        break
    else:
        random = randint(1,100000)
        random1 = randint(1,100000)
x=0
hind = input("kui palju te tunnis saate? ")
while hind.replace(".","",1).isdigit()==False or float(hind)==0:
    hind = input("Palun proovi uuesti! Kui palju te tunnis saate? ")
päev= input("mitu päeva sa töötasid? ")
while päev.isdigit()==False or float(päev)==0:
    päev = input("Palun proovi uuesti! mitu päeva sa töötasid?  ")
for i in range(1,int(päev)+1):
    day = input("mitu tundi sa töötasid? ")
    while day.replace(".","",1).isdigit()==False or float(day)==0:
        day = input("Palun proovi uuesti! mitu tundi sa töötasid? ")
    kõik = float(hind) * float(day)
    x+=kõik
    print("te teenisite" ,i,"päeva jooksul" ,kõik,"$")
print("sinu palk: " ,round(x,2), "$")
x=0
i=1
hind = input("kui palju te tunnis saate? ")
while hind.replace(".","",1).isdigit()==False or float(hind)==0:
    hind = input("Palun proovi uuesti! Kui palju te tunnis saate? ")
päev= input("mitu päeva sa töötasid? ")
while päev.isdigit()==False or float(päev)==0:
    päev = input("Palun proovi uuesti! mitu päeva sa töötasid?  ")
while i in range(1,int(päev)+1):
    day = input("mitu tundi sa töötasid? ")
    while day.replace(".","",1).isdigit()==False or float(day)==0:
        day = input("Palun proovi uuesti! mitu tundi sa töötasid? ")
    kõik = float(hind) * float(day)
    x+=kõik
    i+=1
    print("te teenisite" ,i,"päeva jooksul" ,kõik,"$")
print("sinu palk: " ,round(x,2), "$")
#for x in range(1,101,1):
#    if x%5==0:
#        print(x, end="")
#try:
#    Num_horiz=int(input("Sisesta ruutude arv horisontaalselt =>> \n"))
#except:
#    print("Value Errror")
#    num_horiz=randint(1, 10000)
#try:
#    num_vert=int(input("Sisesta ruutude arv vertikallselt =>> \n"))
#except:
#    print("Value Error")
#    num_vert=randint(1,20)
#for y in range(num_vert):
#    for x in range(num_vert):
#        print("&", end=" ")
#    print("")
