#!/usr/bin/env python
#! -*- coding:utf-8 -*-

from Automate import Automate
etats = "0,1,2"
alphabet = "a,b"
#  "(0,a,1)  (1,a,2)  (1,b,1)  (2,c,3)"
transitions = "0,a,1 0,a,2 1,:e:,2 2,b,1"
etatsFinaux = "1,2"
etatInit = '0'
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
    # if not monAutomate.isDeterministe :
    #     monAutomate.determiniser()
    #     monAutomate.afficherAFD
    # else:
    #     print("Okeyyyyyyyyyyyy !")
    



if __name__ == '__main__' :
    main(transitions,alphabet,etats,etatInit,etatsFinaux)
