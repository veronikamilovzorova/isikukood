def loe_failist(file:str)->list:
    fail=open(file, "r", encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close() 
    return mas

def list_salvesta(mas:list,file:str):
    f=open(file,"w",encoding="utf-8-sig")
    for item in mas:
        f.write(item+"\n")
    f.close()

def elem_list(p:list,i:list):
    n=int(input(f"Сколько человек вы хотите добавить? \n"))
    for j in range(n):
        nimi=input("Введите имя: \n")
        i.append(nimi)
        palk=input("Palk: ")
        p.append(palk)
    return p,i

def kustutamine(nimi:str, p:list, i:list):
    n=i.count(nimi)
    p=0
    for j in range(n):
        ind=i.index(nimi,p)
        p=ind+1
        i.remove(nimi)
        p.pop(ind)
    return p,i

def maksimaalne_palk(inimesed, palgad):
    max_palk=max(palgad)
    index = palgad.index(max_palk)
    nimi=inimesed[index]
    print(f"{nimi} самая большая зарплата")