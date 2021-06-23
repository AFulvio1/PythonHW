
''' 
Abbiamo una stringa S contenente una sequenza di interi non-negativi separati da virgole
ed un intero positivo m.

Progettare una funzione es1(S,m) che prende in input  la stringa S e l'intero m e
restituisce il numero di sottostringhe di S la somma dei cui valori e' m.

Ad esempio, per S='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e m=9 la funzione deve restituire 7.

Infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1,0'_____________
 _'0,4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)
'''

def es1(S,m):
    risultato = 0
    a = 0
    cont = 0
    sequenza = decoder(S)
    while True:
        for i in sequenza[a:]:
            cont += i
            if cont < m:
                continue
            elif cont == m:
                risultato += 1
            elif cont > m:
                a += 1
                cont = 0
                break
        if sum(sequenza[a:]) < m:
            break
    return risultato
    pass
        
def decoder(S):
    risultato = []
    numeri = S.split(',')
    for i in numeri:
        risultato.append(int(i))
    return risultato


if __name__ == '__main__':
    # inserisci qui i tuoi test
    pass
