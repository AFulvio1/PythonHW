# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:33:34 2019

@author: anton
"""

def verifica_presenze(matrice, nome, y, x, i_nome, spostamenti):
    print('chiamata della funzione: ',nome,y,x,spostamenti,i_nome)
    if x < len(matrice[y])-1:
        if matrice[y][x+1] == nome[i_nome]:
            spostamenti += 'D'
            verifica_presenze(matrice, nome, y, x+1, i_nome+1, spostamenti)
        elif y < len(matrice)-1:
            if matrice[y+1][x] == nome[i_nome]:
                spostamenti += 'G'
                verifica_presenze(matrice, nome, y+1, x, i_nome+1, spostamenti)
    elif y < len(matrice)-1:
            if matrice[y+1][x] == nome[i_nome]:
                spostamenti += 'G'
                verifica_presenze(matrice, nome, y+1, x, i_nome+1, spostamenti)
            elif x < len(matrice[y])-1:
                if matrice[y][x+1] == nome[i_nome]:
                    spostamenti += 'D'
                    verifica_presenze(matrice, nome, y, x+1, i_nome+1, spostamenti)
    print('ritorno locale 1: ',spostamenti)
    return spostamenti