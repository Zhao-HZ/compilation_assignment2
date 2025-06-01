from dfa import DFiniteAutomaton
from collections import deque

class NFiniteAutomaton:
    """
    Members of this class
    @member_states: set of all states. Each element must be of string type.<br>
    @member_initialState: the initial state which belongs to states.<br>
    @member_finalStates: set of all final states which must be the subset of states.<br>
    @member_alphabet: alphabet of the set form. Every letter from alphabet must have only single character!<br>
    @member_tFunction: the tFunction is in dictionary form. Key is of the form (state, letter), Value is the set of state.<br>
    @member_oStates: set of possible output of the transition function.
    @member_iStates: set of possible states input of the transition function.
    @member_iLetters: set of possible letter from alphabet of the transition function.
    """
    """
    @param_states: set of all states. Each element must be of string type.<br>
    @param_initialState: the initial state which belongs to states.<br>
    @param_finalStates: set of all final states which must be the subset of states.<br>
    @param_alphabet: alphabet of the set form. Every letter from alphabet must have only single character!<br>
    @param_tFunction: the tFunction in dictionary form. Key is of the form (state, letter), Value is state.<br>
    note that state is in states, letter is in alphabet.
    """
    def __init__(self, states:set, initialState:str, finalStates:set, alphabet:set, tFunction:dict):
        # Aim to initialize and assign to each member variables
        self.states = states
        # Initial state must in states.
        assert initialState in initialState, "Initial state is not in states!"
        self.initialState = initialState
        # final states must be a subset of states
        assert finalStates.issubset(states), "set of final states is not the subset of states."
        self.finalStates = finalStates
        self.alphabet = alphabet 
        # set of possible output of the transition function,
        # which must be the subset of states.
        oStates = set({})
        for each_set in list(tFunction.values()):
            for elem in each_set:
                oStates.add(elem)
        self.oStates = oStates
        assert oStates.issubset(states), "oStates is not the subset of states." 
        # set of possible states input of the transition function,
        # which must be the subset of states/
        iStates = set(map(lambda x : x[0], set(tFunction.keys())))
        # set of possible letter from alphabet input of the transition function,
        # which must be the subset of alphabet.
        iLetters = set(map(lambda x : x[1], set(tFunction.keys()))) 
        assert iStates.issubset(states), "iStates is not in states."
        assert iLetters.issubset(alphabet), "iLetters is not in alphabet."
        self.iStates = iStates
        self.iLetters = iLetters
        self.tFunction = tFunction 

    """
    Check if a tring is accepted by the finite automaton machine.<br>
    @param_string: string need to check. It cannot be empty!<br>
    @return: returns true if the string is accepted, Otherwise it returns false.
    """
    def accepts(self, string) -> bool:
        # Set current state to initial state intially.
        current_state = self.initialState
        return self.__search_NFA(current_state, string)
    
    """
    Auxiliary function used to check if a string is accepted recursively.
    @param_current_state: the current state the function processes.
    @param_string: the current string(whose initial letter may be removed before)
    """
    def __search_NFA(self, current_state, string) -> bool:
        flag = False
        # Base case of the recursion (the string is empty).
        if len(string) == 0:
            # If search is over, check if the current state
            if current_state in self.finalStates:
                return True
            else:
                return False
        # Recursive step.
        else:
            # processes the first letter 
            init_letter = string[0]
            # and then removes it.
            tail_string = string[1:]
            # Check the current state and the letter needed to process are
            # in the set of the keys, otherwise, returns false
            if (current_state, init_letter) in self.tFunction:
                new_states = self.tFunction[(current_state, init_letter)]
                # if the new states is a empty set, current state cannot be moved
                # to the next state, so we reject the string.
                if len(new_states) == 0:
                    return False
                # Otherwise, iterate all states from new_states.
                # If we have found at least one path that makes the string accpeted, we are done!
                for each_state in new_states:
                    flag = flag or self.__search_NFA(each_state, tail_string)
                    # avoid repeated searches.
                    if flag:
                        break
                return flag
            else:
                return False
    """
    This function shows the transition function of this NFA.
    """ 
    def show_transition_function(self):
        for item in self.tFunction:
            print(item, end=" ")
            print(self.tFunction[item]) 

    """
    This functions converts NFA into DFA.
    """
    def transfer_to_DFA(self) -> DFiniteAutomaton:
        states = self.lazy_construction()
        finalStates = set()
        tFunction = dict()
        for state in states:
            if bool(state & self.finalStates):
                finalStates.add(state)
        for state in states:
            for letter in self.alphabet:
                if (state, letter) not in tFunction:
                    tFunction[(state, letter)] = frozenset()
                for elem in state:
                    if (elem, letter) in self.tFunction:
                        tFunction[(state, letter)] |= frozenset(self.tFunction[(elem, letter)])
                if not bool(tFunction[(state, letter)]): # If the value is empty
                    tFunction.pop((state, letter))
        # Used for test
        # return tFunction
        return DFiniteAutomaton(
            states,
            frozenset({self.initialState}),
            finalStates,
            self.alphabet,
            tFunction 
        )

    """
    Auxiliary function used to generate set of states for DFA
    """
    def lazy_construction(self) -> set:
        Qp = {frozenset({self.initialState})}
        Qpp = set()
        queue = deque()
        queue.append(frozenset({self.initialState}))
        while queue:
            qp = queue.popleft()
            if qp not in Qpp:
                for letter in self.alphabet:
                    next_state = set()
                    for state in qp:
                        if (state, letter) in self.tFunction:
                            next_state |= self.tFunction[(state, letter)]
                    next_state = frozenset(next_state)
                    if next_state not in Qp and len(next_state) != 0:
                        Qp.add(next_state)
                        queue.append(next_state)
            else:
                continue
            Qpp.update([qp])
        return Qp                    
