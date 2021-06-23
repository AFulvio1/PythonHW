# -*- coding: utf-8 -*-
''' 
    In un immagine a sfondo nero  e' disegnata  una griglia  
    dove  alcuni segmenti che ne connettono i nodi in orizzontale 
    o in verticale sono stati cancellati (i nodi della griglia sono in 
    verde mentre i segmenti sono in rosso).
    La dimensione del lato dei quadrati della griglia non è data.

    Si veda ad esempio la figura foto_1.png.
    Progettare la funzione es1(fimm, k) che prende in input l'indirizzo 
    dell'immagine contenente la griglia ed un intero k e restituisce un intero. 
    L'intero restituito e' il numero di 
    quadrati rossi (con pixel verdi) di lato k (steps della griglia) che sono presenti nell'immagine.
    Ad esempio  es1(foto_1.png,2) deve restituire 2 (i due quadrati rossi presenti nella 
    sottogriglia hanno il vertice in alto a sinistra con coordinate (3,0) e 
    (4,2) nelle coordinate della griglia, rispettivamente)

    Per caricare e salvare  file PNG si possono usare load e save della libreria immagini allegata.

    NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
    (ad esempio editatelo dentro Spyder)

'''
import immagini as im

def es1(fimm,k):
    risultato = 0
    verde,nero = (0,255,0),(0,0,0)
    img = im.load(fimm)
    ascisse,ordinate,y_corr,x_corr,step,width = trova_griglia(img, verde, k)
    for y in ordinate:
        y_fine = y+width
        for x in ascisse:
            x_fine = x+width
            if nero in img[y][x:x_fine+1]:
                continue
            else:
                risultato += controllo(img, y, x, x_fine, y_fine, nero)
    return risultato
    pass


def trova_griglia(img, verde, k):
    cont = 0
    ascisse = []
    ordinate = []
    for i,e in enumerate(img):
        if verde in e and cont == 0:
            a = e.index(verde)
            vertice = [i,a]
            cont += 1
        elif verde in e and cont == 1:
            step = len(img[vertice[0]:i])
            width = step*k
            break
        else:
            continue
    y_corr,x_corr = vertice[0],vertice[1]
    for x in range(x_corr, len(img[y_corr]), step):
        if img[y_corr][x] == verde and x+width < len(img[y_corr]):
            ascisse.append(x)
    for y in range(y_corr, len(img), step):
        if img[y][x_corr] == verde and y+width < len(img):
            ordinate.append(y)      
    return ascisse,ordinate,y_corr,x_corr,step,width

def controllo(img, y, x, x_fine, y_fine, nero):
    cont1 = 0
    cont2 = 0
    for j in range(y, y_fine+1):
        cont1 += 1
        if img[j][x] == nero or img[j][x_fine] == nero:
            break
        else:
            cont2 += 1
    for i in range(x, x_fine+1):
        cont1 += 1
        if img[y_fine][i] == nero:
            break
        else:
            cont2 += 1
    if cont1 == cont2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    pass
    # inserisci qui i tuoi test
