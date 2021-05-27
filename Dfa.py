from fsmdot.dfa import Dfa
from fsmdot.nfa import Nfa
from graphviz import render

Q = {'q0','q1', 'q2', 'q3'}
S = {Nfa.EPSILON, 'a', 'b'}
d = {
    'q0': {
        'b': {'q1','q2'},
    },
    'q1': {
        'b': {'q3'}
    },
    'q2': {
        'b': {'q1','q3'},
    },
    'q3': {
        'a': {'q3'}
    }
}
q0 = 'q0'
F = {'q3'}
def Display(Q, S, d, q0, F):
    try :
        a = Dfa(Q, S, d, q0, F)
        print("deterministe")
        a.print_table()
        G = a.dot_graph()
        G.write('dfa.dot')
        render('dot', 'png', 'dfa.dot')
        return True
    except:
        a = Nfa(Q, S, d, q0, F)
        print("non deterministe")
        G = a.dot_graph()
        G.write('nfa.dot')
        render('dot', 'png', 'nfa.dot')
        return False
def Determiniser(Q, S, d, q0, F):
    a = Nfa(Q, S, d, q0, F)
    a.print_table()    
    dfa = a.to_dfa()
    G2 = dfa.dot_graph()
    G2.write('NfatoDfa.dot')
    render('dot', 'png', 'NfatoDfa.dot')
def Accepte(Q, S, d, q0, F,s):
    try :
        a = Dfa(Q, S, d, q0, F)
    except:
        a = Nfa(Q, S, d, q0, F)
        a = a.to_dfa()
    print(a.accept(s))  
    return (a.accept(s))  



