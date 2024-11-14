
def etlap(lista):
    """Itt írjuk ki az ételek neveit"""

    for i in range (0, len(lista), 1):
        print (f"**{lista[i].nev} {lista[i].ar:>10} Ft**")

def atlag_ar(lista):
    osszeg:float = 0
    for i in range (0, len(lista),1):
        osszeg+=lista[i].ar
    return osszeg/len(lista)

def legdragabb(lista):
    max_index=0
    for i in range(0, len(lista),1):
        if (lista[i].ar>lista[max_index].ar):
            max_index = 1
    return max_index