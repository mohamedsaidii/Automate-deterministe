from fsmdot.dfa import Dfa
from fsmdot.dfa import Dfa
from graphviz import render


Q = {'S1', 'S2'}
S = {'0', '1'}
d = {
    'S1': {
        '0': 'S2',
        '1': 'S1'
    },
    'S2': {
        '0': 'S1',
        '1': 'S2'
    }
}
q0 = 'S1'
F = {'S1'}
try :
    a = Dfa(Q, S, d, q0, F)
    print("deterministe")
except:
    a = Nfa(Q, S, d, q0, F)
    print("noooooo ")
    
a.print_table()
G = a.dot_graph()
G.write('graph1_dfa.dot')
render('dot', 'png', 'graph1_dfa.dot')

