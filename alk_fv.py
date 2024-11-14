def ossz_fiz(dolgozo_lista):
        osszes:float=0
        for i in range(0, len(dolgozo_lista),1):
            osszes+=dolgozo_lista[i].fizetes
        return osszes
    
def legidosebb(dolgozo_lista):
        legtobb_hely=0
        for i in range(0, len(dolgozo_lista),1):
            if(dolgozo_lista[legtobb_hely].kor < dolgozo_lista[i].kor):
                legtobb_hely=i   
        return legtobb_hely
    