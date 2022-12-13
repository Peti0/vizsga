def Hoe(a):
    b=False
    if a > 150:
        b=True
        return b 


cim=(input("cím: "))
while(cim!=""):
    oldal=int(input("Add meg az oldalainak számát!:"))
    old=Hoe(oldal)
    if old:
        print("A könyv hosszú terjedelmű")
    else:
        print("A könyv rövid terjedelmű")
    cim=(input("Add meg a könyv címét: "))
