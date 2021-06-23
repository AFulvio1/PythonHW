
''' 
    Data una lista ls ed una lista lmosse della stessa lunghezza di ls e contenente 
    tutti gli interi tra 0 e len(ls)-1, una trasformazione rispetto a lmosse e' 
    la lista che   si ottiene spostando simultaneamnete ciascun elemento  di ls   
    dalla sua posizione i alla posizione lmosse[i].
    
    Definire una funzione es2(ls,lmosse, k) che date:
    - una  lista ls di interi,  una lista lmosse (della stessa lunghezza di ls 
    e contenente tutti gli interi  tra 0 e len(ls)-1) ed un intero k.
    - restituisce la lista che si ottiene  applicando ad ls in sequenza k trasformazioni 
    rispetto ad lmosse.
     
   Ad esempio:
     Per ls=[1, 2, 3, 4, 5, 6, 7, 8, 9], lmosse=[1, 0, 5, 2, 8, 4, 3, 7, 6] e k=5
     la funzione deve restituire  la lista  [2, 1, 6, 3, 9, 5, 4, 8, 7]
     infatti  applicando alla lista  ls la trasformazione per 5 volte 
     si ottengono nell'ordine le liste: 
     1 [2, 1, 4, 7, 6, 3, 9, 8, 5]
     2 [1, 2, 7, 9, 3, 4, 5, 8, 6]
     3 [2, 1, 9, 5, 4, 7, 6, 8, 3]
     4 [1, 2, 5, 6, 7, 9, 3, 8, 4]
     5 [2, 1, 6, 3, 9, 5, 4, 8, 7]
    se k=370 la funzione deve restituire la lista [1, 2, 5, 6, 7, 9, 3, 8, 4]

    ATTENZIONE: Al termine della funzione le liste ls ed lmosse non devono risultare modificate. 
   
    ATTENZIONE: non sono permesse librerie aggiuntive.

    ATTENZIONE: sono vietate le variabili globali.
   
    NOTA: il timeout previsto per questo esercizio è di 0.5 secondi per ciascun test

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
    (ad esempio editatelo dentro Spyder)
'''

def es2(ls,lmosse,k):
    risultato = [ 0*j for j in lmosse ]
    lscopia = ls.copy()
    cont = 0
    cont2 = 0
    while k != cont:
        for i,e in enumerate(lmosse):
            risultato[e] = lscopia[i]
        lscopia = risultato.copy()
        cont += 1
        if risultato == ls:
            break
    ricorsività = k % cont
    while ricorsività != cont2:
        for i,e in enumerate(lmosse):
            risultato[e] = lscopia[i]
        lscopia = risultato.copy()
        cont2 += 1
    return risultato
    pass


# le righe seguenti non vengono eseguite quando si importa questo modulo
if __name__ == '__main__':
    # inserite qui il vostro codice di test personale
    pass