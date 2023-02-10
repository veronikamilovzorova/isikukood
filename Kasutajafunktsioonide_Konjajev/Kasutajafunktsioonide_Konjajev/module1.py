from math import *
def season(n:int)->str:
    if n==12 or 1 <= n <=2:
        print("Talv")
    elif 3<= n <=5:
        print("Kevad")
    elif 6<= n <=8:
        print("Suvi")
    elif 9<= n <=11:
        print("Sügis")
    return n

def square(a:float)->int:
   """
   """
   p=a*4
   s=a*a 
   d=(a**2)/2 
   return p,s,d

def is_year_leap(aasta:int)->bool:
    """Aastat
    """
    if aasta%4==0:
        v=True
    else:
        v=False 
    return v 

def arithmetic(a:float,c:str,b:float)->any:
    """kalkulaator
    """
    if c=="+":
        v=a+b
    elif c=="-":
        v=a-b
    elif c=="*":
        v=a*b
    elif c=="/":
        if b==0:
            v="DIV0"
        else:
            v=a/b
    else:
        v="Неизвестная операция"
    return v

