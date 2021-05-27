#!/usr/bin/env python
#! -*- coding:utf-8 -*-
import tkinter as tk
from PIL import Image
from Automate import Automate
etats = "q0,q1,q2,q3"
alphabet = "a,b"
#  "(0,a,1)  (1,a,2)  (1,b,1)  (2,c,3)"
transitions = "q0,b,q1 q0,:e:,q2 q2,b,q1 q1,:e:,q3 q2,b,q3 q3,a,q3"
etatsFinaux = "q3"
etatInit = 'q0'
def main(transitions,alphabet,etats,etatInit,etatsFinaux):
    etats = etats.split(',')
    alphabet = alphabet.split(',')
    monAutomate = Automate(etats,alphabet )
    tabTransitions = transitions.split(' ')

    # ToDo : Fix ajout transitions
    dict = {}
    
    for tr in tabTransitions:
        list = tr.split(',')
        # validate list items
        arrow = str(list[0])+","+str(list[1])
        if arrow not in dict:
            dict[arrow]= [list[2]]
        else :
            dict[arrow].append(list[2])
    print(dict)
    for item in dict :
        l = item.split(',')
        monAutomate.ajouterTransition(l[0],l[1],dict[item])
    monAutomate.fixerEtatInitial(etatInit)

    for etat in etatsFinaux.split(','):
        monAutomate.fixerEtatsFinaux(etat)
    monAutomate.afficher()
    
    val = monAutomate.determiniser()
    print("AFD.py --->",val)
    if val == False :
        monAutomate.afficherAFD()
        return False
    else:
        print("Okeyyyyyyyyyyyy !")
        tk.messagebox.showinfo("Info","Cet automate est déjà déterministe")
        return True
    



if __name__ == '__main__' :
    main(transitions,alphabet,etats,etatInit,etatsFinaux)
