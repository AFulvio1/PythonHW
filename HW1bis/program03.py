'''
Data una lista di parole ed un testo, vogliamo trovare un anagramma del testo.
L'anagramma da trovare deve essere formato esattamente da 3 parole di almeno 2 caratteri,
diverse tra loro, tra quelle fornite, se esiste (altrimenti tornate None).
Nel confrontare i caratteri ignorate la differenza tra minuscole e maiuscole.
Ignorate inoltre differenze nel numero di spazi presenti.
Potete assumere che le lettere del testo e delle parole siano tutte alfabetiche (oppure spazio nel testo).

Definite la funzione es3(parole, testo) che torna la tupla delle tre parole diverse 
che formano l'ultimo anagramma in ordine alfabetico.
NOTA: la lista delle parole non deve essere modificata dalla funzione.

Esempio: la terna corrispondente all'ultimo anagramma di 3 parole dei testi seguenti,
ottenuto usando le 60000 parole italiane contenute nel file allegato, è:
    "Andrea Sterbini"       -> ('treni', 'sia', 'brande')
    "Angelo Monti"          -> ('toni', 'nego', 'mal')
    "Angelo Spognardi"      -> ('sragion', 'pend', 'lago')
    "Ha da veni Baffone"    -> ('video', 'beh', 'affanna')

ATTENZIONE: non è permesso usare librerie aggiuntive

ATTENZIONE: sono vietate le variabili globali

ATTENZIONE: prima di consegnare assicuratevi che il file del programma sia nell'encoding UTF8, 
ad esempio editandolo in Notepad++ oppure Spyder.

'''

def es3(parole, testo):
    risultato = ()
    parola_corr = ''
    testo = senzaspazi(testo)
    meno_parole = menoparole(parole,testo)
    risultato += (meno_parole[0],)    
    for i in meno_parole[0]:
        testo = testo.replace(i,'',1)
    for parola in meno_parole:
        testo1 = testo
        for car in parola:
            if car in testo1:
                parola_corr += car
                testo1 = testo1.replace(car,'',1)
            else:
                parola_corr = ''
                break
        if parola_corr:
            risultato += (parola_corr,)
            for j in parola_corr:
                testo = testo.replace(j,'',1)
            parola_corr = ''
    return risultato
            
    
    
def senzaspazi(testo):
    testo1 = ''
    for i in testo:
        if i.isalpha():
            testo1 += i
    return testo1.lower()

def menoparole(parole,testo):
    risultato = []
    parola_corr = ''
    for parola in parole:
        testo1 = testo
        for car in parola:
            if car in testo1:
                parola_corr += car
                testo1 = testo1.replace(car,'',1)
            else:
                parola_corr = ''
                break
        if parola_corr and len(parola_corr) > 1:
            risultato.append(parola_corr)
            parola_corr = ''
        else:
            parola_corr = ''
    return sorted(risultato, reverse=True)

# le righe seguenti non vengono eseguite se si importa questo modulo
if __name__ == '__main__':
    # inserite qui i vostri test personali
    pass
