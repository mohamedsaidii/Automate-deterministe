# from automata.base.automaton import Automaton
# from automata.fa.dfa import DFA
# # DFA which matches all binary strings ending in an odd number of '1's
# dfa = DFA(
#     states={'q0', 'q1', 'q2'},
#     input_symbols={'0', '1'},
#     transitions={
#         'q0': {'1': 'q1'},
#         'q1': {'0': 'q0', '1': 'q2'},
#         'q2': {'0': 'q2', '1': 'q1'}
#     },
#     initial_state='q0',
#     final_states={'q1'}
# )
# if dfa.accepts_input("1110101001"):
#     print('accepted')
# else:
#     print('rejected')
