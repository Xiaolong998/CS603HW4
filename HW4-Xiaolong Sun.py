# -*- coding: utf-8 -*-
"""
Created on Thu May 27 00:57:58 2021

@author: xiaol
"""


# input of nfa is a dictionary
# with key as state and 

# Input
total_num_states = 3 # total number of states
start_state = '0'
nfa1 = {'0':[['0','1'], ['3']],\
       '1':[['0'], ['1','3']],\
       '2':[[''],['0','2']],\
       '3':[['0','1','2'],['1']]   
       }
    
    
nfa2 = {'0':[['0','1'], ['0']],\
       '1':[[''], ['2']],\
       '2':[[''],['']]   
       }
    
nfa3 = {'0':[['0'], ['0','1']],\
        '1':[['2'],['2']],\
        '2':[[""],[""]]}
    
nfa =  nfa1
    
# Output
dfa = {}

def merge_state(list_states:list):
    """
    for given state and input, if there are multiple output states,
    merge them into one.
    
    e.g. ['0','1'] --> ['01']

    Parameters
    ----------
    list_states : list
        a list of output states.

    Returns
    -------
    combined states

    """
    if len(list_states) > 1:
        combined = "".join(set(list_states))
        combined = sorted(combined)
        combined = "".join(combined)
        return [combined]
    else:
        return list_states

def get_dfa_output_state(current_state, input_string ,nfa):
    """
    given the current state and input, find all output_state for dfa from nfa.

    Parameters
    ----------
    current_state : string
        e.g. s0 current state is '012'
    input_string : string
        0 or 1
    nfa : dict
        the description of a non determinstic machine.

    Returns
    -------
    a string that shows output state

    """
    list_output_nfa = []
    for s in current_state[0]:
        output_nfa = nfa[s][int(input_string)]
        output_nfa = merge_state(output_nfa)
        list_output_nfa.append(output_nfa[0])
    combined = "".join(set(list_output_nfa))
    combined = "".join(set(combined))
    combined = sorted(combined)
    list_output_nfa = "".join(combined)
    return list_output_nfa
    
    

# Driver Script

queue = []
        
# start with the start state 0
output_state0 = nfa[start_state][0]
output_state0 = merge_state(output_state0)
output_state1 = nfa[start_state][1]
output_state1 = merge_state(output_state1)

# if output state is not in queue,
for output_state in [output_state0,output_state1]:
    if output_state not in queue:
        queue.append(output_state)

dfa[start_state] = [output_state0,output_state1]

while len(queue) != 0:
    print(queue)
    current_state = queue.pop(0)
    if current_state[0] not in dfa.keys():
        dfa_output_states = [] 
        dfa_output_states.append([get_dfa_output_state(current_state,0,nfa)])
        dfa_output_states.append([get_dfa_output_state(current_state,1,nfa)])
        dfa[current_state[0]] = dfa_output_states
        if dfa_output_states[0] not in queue:
            queue.append(dfa_output_states[0])
        if dfa_output_states[1] not in queue:
            queue.append(dfa_output_states[1])
print(dfa)

# End of Driver Script