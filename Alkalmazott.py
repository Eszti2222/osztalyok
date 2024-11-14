from datetime import datetime


class Alkalmazott:
    def __init__(self,nev:str="",szul_datum:int=0,fizetes:int=0,pozicio:str="",kor:int=0):
        self.nev=nev
        self.szul_datum=szul_datum
        self.fizetes=fizetes
        self.pozicio=pozicio
        self.kor=self.korbeallit()

    
    def korbeallit(self):
        idei_ev= datetime.now().year
        self.kor= idei_ev-self.szul_datum
        return self.kor
        
    def __str__(self):
        return f"Név: {self.nev}, Születési dátum: {self.szul_datum}, fizetése: {self.fizetes}, pozicíója: {self.pozicio}, életkora: {self.kor}"
    