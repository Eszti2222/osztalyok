class Etel:
    def __init__(self,nev:str="",ar:int=1000):
        '''konstruktor, feladata: létrehozni a konkrét példányt a konkrét adatokkal a tervrajzból
        beállítása az adattagokat- objektum
        tulajdonságok értékei'''

        self.nev=nev
        self.ar=ar
        self.allapot="folyamatban"
    
    def keszul(self):
        self.allapot="kesz"

    def __str__(self):
        return f"Étel neve: {self.nev}, Ár: {self.ar}, Állapot: {self.allapot}"