from oma_moodul import *
palgad=[]
inimesed=[]
palgad=loe_failist("palgad.txt")
print(palgad)


while True:
    v=int(input("0-Посмотреть данные, \n1-Вставить данные, 2-сохранить файл, \n3-Удалить имена и зарплаты, \n4-Посмотреть самую большую зарплату"))
    if v==0:
        inimesed=[]
        palgad=[]
        palgad=loe_failist("palgad.txt")
        inimesed=loe_failist("inimesed.txt")
        print(palgad)
        print(inimesed)
    elif v==1:
        palgad, inimesed=elem_list(palgad,inimesed)
        print(palgad)
        print(inimesed)
    elif v==2:
        list_salvesta(palgad, "palgad.txt")
        list_salvesta(inimesed, "inimesed.txt")
    elif v==3:
        palgad, inimesed=kustutamine(input("Введите имя"), palgad, inimesed)
    elif v==4:
        maksimaalne_palk(inimesed, palgad)