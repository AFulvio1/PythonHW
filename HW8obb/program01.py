
'''
    Data una matrice di caratteri ed una parola, diciamo che la  parola e' presente
    nella matrice se e' possibile ottenerla collezionando i caratteri
    che si incontrano con una serie di spostamenti tra celle adiacenti.
    I soli spostamenti permessi sono:
    a) da una cella alla cella adiacente a destra (D)
    b) da una cella alla cella in basso (B)
    la parola, se presente nella matrice, e'  individuata dalle coordinate
    di riga e colonna della cella da cui si parte e dalla stringa di 'D' e 'B'
    che denota la sequenza di spostamenti da effettuare per collezionare i suoi caratteri.

    Si consideri ad esempio la matrice

      ANTANDBER
      LNOANRLNT
      EIOSGEARO
      SSUNALSIC
      AANDEOAAO

    in questa matrice:
    'ANGELO' e' presente ed e' individuata da (1,3) e 'DGDGG'
    'ANDREA' e' presente ed e' individuata da (0,3) e 'DDGGD'
    'ENRICO' e' presente ed e' individuata da (0,7) e 'GGGDG'
    'ALESSANDRO', 'ANTONIO' e 'ALBERTO' sono parole non presenti.

    Abbiamo una matrice ed una lista di parole e vogliamo sapere quali sono presenti
    nella matrice e quali no.

    Progettare una funzione es1(ftesto) che preso l'indirizzo di un file
    di testo in cui e' registrata la matrice e la lista di parole da ricercare e
    restituisce una lista.
    Nella lista restituita all'i-esimo posto troviamo:
    - -1 se la parola non e' presente nella matrice.
    - la posizione dell'i-esima parola della lista nella matrice
      (vale a dire la terna (riga,colonna,s) con (riga,colonna) coordinate iniziali
      della cella d'inizio degli spostamenti ed s stringa che denota gli spostamenti).
      Nel caso la parola sia presente piu' volte nella matrice deve essere restituita
      la posizione piu' in alto  a sinistra in cui compare e nel caso compaia
      piu' volte a partire dalla stessa casella delle diverse stringhe che
      la individuano va presa quella che precede le altre lessicograficamente.

    Ad esempio, Per la matrice vista  sopra e la lista
    ['ALBERTO','ALESSANDRO','ANDREA', 'ANGELO', 'ANTONIO', 'ENRICO']
    la funzione es1 restituira' la lista
    [-1,-1,(0,3, 'DDGGD'),(1,3, 'DGDGG'),-1,(0,7, 'GGGDG')]

    Il file ftesto  contiene  la matrice  e, di seguito  l'elenco delle parole.
    Una serie di 1 o piu'  linee vuote precede la reppresentazione della matrice,
    separa il diagramma dall'elenco delle parole e segue l'elenco delle parole.
    La matrice  e' registrata per righe (una riga per linea e in linee consecutive) gli
    elementi di ciascuna riga sono adiacenti a formare una stringa.
    La lista delle parole occupa  invece linee consecutive con  una o piu' parole o
    separate da spazi per ciascuna linea.
    Per un esempio si veda il file esempio_Disney.pdf

    NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

    NOTA: almeno una delle funzioni realizzate DEVE essere ricorsiva, ad esempio
    potete scandire la matrice iterativamente e le lettere della parola cercata ricorsivamente.

    NON usate nessuna libreria.

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)

'''

def es1(ftesto):
    risultato = []
    matrice,lista = decoder(ftesto)
    for nome in lista:
        cont = 0
        for y in range(len(matrice)):
            if nome[0] in matrice[y]:
                lista_iniziali = [ i for i,e in enumerate(matrice[y]) if nome[0] == e ]
                for x in lista_iniziali:
                    spostamenti = ''
                    spostamenti_finali = verifica_presenze(matrice, nome[1:], y, x, spostamenti)
                    if len(spostamenti_finali) == len(nome)-1:
                        risultato.append((y,x,spostamenti_finali))
                        cont += 1
                        break
                    else:
                        continue
                if cont == 1:
                    break
        if cont == 0:
            risultato.append(-1)
    return risultato

        
def verifica_presenze(matrice, nome, y, x, spostamenti):
    if not nome == '' and x+2 < len(matrice[y]) and y+2 < len(matrice):
        if len(nome) > 1 and nome[0] == matrice[y][x+1] == matrice[y+1][x]:
            if nome[1] == matrice[y][x+2] or nome [1] == matrice[y+1][x+1]:
                spostamenti += 'D'
                return verifica_presenze(matrice, nome[1:], y, x+1, spostamenti)
            elif nome[1] == matrice[y+1][x+1] or nome[1] == matrice[y+2][x]:
                spostamenti += 'G'
                return verifica_presenze(matrice, nome[1:], y+1, x, spostamenti)
        elif nome[0] == matrice[y][x+1]:
            spostamenti += 'D'
            return verifica_presenze(matrice, nome[1:], y, x+1, spostamenti)
        elif nome[0] == matrice[y+1][x]:
            spostamenti += 'G'
            return verifica_presenze(matrice, nome[1:], y+1, x, spostamenti)
    elif not nome == '' and x+1 < len(matrice[y]):
        if nome[0] == matrice[y][x+1]:
            spostamenti += 'D'
            return verifica_presenze(matrice, nome[1:], y, x+1, spostamenti)
        elif y+1 < len(matrice):
            if nome[0] == matrice[y+1][x]:
                spostamenti += 'G'
                return verifica_presenze(matrice, nome[1:], y+1, x, spostamenti)
    elif not nome == '' and y+1 < len(matrice):
        if nome[0] == matrice[y+1][x]:
            spostamenti += 'G'
            return verifica_presenze(matrice, nome[1:], y+1, x, spostamenti)
        elif x+1 < len(matrice[y]):
            if nome[0] == matrice[y][x+1]:
                spostamenti += 'D'
                return verifica_presenze(matrice, nome[1:], y, x+1, spostamenti)
    return spostamenti
    

def decoder(ftesto):
    with open(ftesto) as f:
        testo = f.read()
    matrice,lista = [],[]
    testo = testo.split('\n\n')
    while '' in testo:
        [ testo.remove(i) for i in testo if i == '' ]
    testo[0],testo[1] = testo[0].split('\n'),testo[1].split('\n')
    for j in testo[1]:
        if j == '':
            continue
        else:
            if ' ' in j:
                appoggio = j.split()
                for k in appoggio:
                    lista.append(k)
            else:
                lista.append(j)
    for p in testo[0]:
        if p != '':
            matrice.append(p)
    return matrice,lista
        
    

if __name__ == '__main__':
    es1('esempio1.txt')
    # inserite qui i vostri test