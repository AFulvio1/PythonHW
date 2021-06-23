# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:39:28 2019

@author: anton
"""

def verifica_presenze(matrice, nome, y, x, spostamenti):
    print('chiamata della funzione: ',len(nome),nome,y,x,spostamenti)
    if not nome == '' and x+1 < len(matrice[y]):
        if nome[0] == matrice[y][x+1]:
            spostamenti += 'D'
            verifica_presenze(matrice, nome[1:], y, x+1, spostamenti)
        elif y+1 < len(matrice):
            if nome[0] == matrice[y+1][x]:
                spostamenti += 'G'
                verifica_presenze(matrice, nome[1:], y+1, x, spostamenti)
    elif not nome == '' and y+1 < len(matrice):
        if nome[0] == matrice[y+1][x]:
            spostamenti += 'G'
            verifica_presenze(matrice, nome[1:], y+1, x, spostamenti)
        elif x+1 < len(matrice[y]):
            if nome[0] == matrice[y][x+1]:
                spostamenti += 'D'
                verifica_presenze(matrice, nome[1:], y, x+1, spostamenti)
    print('ritorno locale: ',len(nome),spostamenti)
    return spostamenti
