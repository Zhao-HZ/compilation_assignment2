class DFiniteAutomaton:
    """
    Members of this class
    @member_states: set of all states. Each element must be of string type.<br>
    @member_initialState: the initial state which belongs to states.<br>
    @member_finalStates: set of all final states which must be the subset of states.<br>
    @member_alphabet: alphabet of the set form. Every letter from alphabet must have only single character!<br>
    @member_tFunction: the tFunction is in dictionary form. Key is of the form (state, letter), Value is state.<br>
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
        oStates = set(tFunction.values())
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
    Check if a tring is acceptable by the finite automaton machine.<br>
    @param_string: string need to check. It cannot be empty!<br>
    @return: returns true if the string is accepted, Otherwise it returns false.
    """
    def accepts(self, string):
        # assert len(string) != 0, "Empty strings are not allowed!"
        current_state = self.initialState # set the current state to be the initial state
        flag = False # determines if string is acceptable.
        for letter in string: # iterates each character from string.
            # current_state and letters from the string must be valid
            # in terms of the transition function.
            if current_state in self.iStates and letter in self.iLetters: 
                # compute the new state using transition function.
                new_state = self.tFunction[(current_state, letter)]
                # and assign to current_state
                current_state = new_state
            else:
                # if they are not valid, the automaton will be halted.
                # in this case, it returns false.
                return flag
        # if current state is final state, the string is acceptable, thereby returning true.
        # otherwise, it returns false.
        if current_state in self.finalStates:
            flag = True
        return flag
    
            
