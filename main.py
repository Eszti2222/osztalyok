'''hozz létre egy osztáylzatok listát és
osztályzatok_lista=[3,4,5,2,3,4,5,4]
nevek=["Béla", "Jenő, "Ági", "Rozi"]
nevek és a nevekhez tartozó osztályzatok összetartoznak

Új adatszerkezet- ami egy tudja kezelni az összetartozó adatokat
szemely= {nev:"Béla", osztályzat:3}

objektumok - tulajdonságokkal(főnevek) és viselkedéssel(cselekvés) bíró adatszerkezet

Készítünk egy sablont, ami alapján le tudjuk gyártani a konkrét egyedeket.
OSZTÁLY-sablon- tervrajz
OBJEKTUM-konkrét egyedek-konkrét termék'''

from Etel import Etel
from Alkalmazott import Alkalmazott
import fuggvenyek
import alk_fv
'''2. lépés: létrehozzuk a konkrét példányt a tervrajz alapján
'''
etel1=Etel("húsleves",1234)
etel2=Etel("krumplis",2345)
etel3=Etel("Ránotott hús",1230)
#etel4=Etel("Palacsinta",1080)

etel_lista=[]
etel_lista.append(etel1)
etel_lista.append(etel2)
etel_lista.append(etel3)
etel_lista.append(Etel("Palacsinta",1080)) # így is lehet append-olni




'''etel1.keszul()
print("Szia én vagyok a "+etel1.nev+ ". Az állapotom: "+etel1.allapot)
print("Szia én vagyok a "+etel2.nev+ ". Az állapotom: "+etel2.allapot)'''

print(f"Szia én vagyok a "+ etel_lista[0].nev ,". Az állapotom: "+etel_lista[0].allapot)
      
'''Írj metódust, amewly paraméteében megkapja a listát és kiirja '''
fuggvenyek.etlap(etel_lista)

''' Írj metódosut , ... , megmondja a ételek átlagárát!'''
atlagar= fuggvenyek.atlag_ar(etel_lista)
print(f"Az ételek átlagára: {atlagar}")


''' Írj metódosut , ... , megmondja a legdrágább étel nevét!'''
max_i= fuggvenyek.legdragabb(etel_lista)
print(f"A legdrágább étel neve és ára: {etel_lista[max_i].nev}, {etel_lista[max_i].ar} Ft")

print(etel_lista[0])

'''Hozz létre egy Alkalmazott osztályt, amleyikben az alábbi infókat tudod tárolni egy cég dolgozóiról:
nev
szul_datum
fizetes
pozicio
kor
Készíts kor metódust, ami megmondja az adott ember korát
__str__

Hozz létre legalább 5 embert, tedd bele őket liostába
-mennyi az össz fizetés?
-Hány éves a legidősebb ember?
-Hány ember van 'beosztott' pozícióban?
-kinek a legalacsonyabb a fizetése?

++ az osztálynak legyen egy fizetésemelés metódusa,amelyik a fiztést megemeli a paraméterében amegadott százalék értékkel.
a legkisebb fiztésű ember fizetését  emeld meg 20%-kal!'''
dolgozo_lista=[]
d1=Alkalmazott("Anna",1996,550000,"Üzletvezető",kor=Alkalmazott.korbeallit)
d2=Alkalmazott("Béla",1980,490000,"Másodhelyettes",kor=Alkalmazott.korbeallit)
d3=Alkalmazott("Ádám",2000,390000,"Műszakvezető",kor=Alkalmazott.korbeallit)
d4=Alkalmazott("Ákos",2001,300000,"Dolgozó",kor=Alkalmazott.korbeallit)
d5=Alkalmazott("Fanni",2002,300000,"Dolgozó",kor=Alkalmazott.korbeallit)

dolgozo_lista.append(d1)
dolgozo_lista.append(d2)
dolgozo_lista.append(d3)
dolgozo_lista.append(d4)
dolgozo_lista.append(d5)

print(dolgozo_lista[0])
osszes=alk_fv.ossz_fiz(dolgozo_lista)
print(f"Az összes fizetés: {osszes}")
legtobb_hely=alk_fv.legidosebb(dolgozo_lista)
print(f"A legidősebb dolgozó: {dolgozo_lista[legtobb_hely].kor} éves.")



