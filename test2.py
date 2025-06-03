from ndfa import NFiniteAutomaton

# Example 1: checks if a string has a suffix 01.
states1 = {"q0", "q1", "q2"}
initialState1 = "q0"
finalStates1 = {"q2"}
alphabet1 = {"0", "1"}
tFunction1 = {
    ("q0", "0"): {"q0", "q1"},
    ("q0", "1"): {"q0"},
    ("q1", "1"): {"q2"}
}
nfa1 = NFiniteAutomaton(states1, initialState1, finalStates1, alphabet1, tFunction1)

# Example 2: accepts all strings over {0, 1} that contains
# either the substring "01" or "10".
states2 = {"q0", "q1", "q2", "q3"}
initialState2 = "q0"
finalStates2 = {"q3"}
alphabet2 = {"0", "1"}
tFunction2 = {
    ("q0", "0"): {"q0", "q1"},
    ("q0", "1"): {"q0", "q2"},
    ("q1", "1"): {"q3"},
    ("q2", "0"): {"q3"},
    ("q3", "0"): {"q3"},
    ("q3", "1"): {"q3"},
}
nfa2 = NFiniteAutomaton(states2, initialState2, finalStates2, alphabet2, tFunction2)

# Example 3: equivalent to the RE: a+ba*.
states3 = {"q0", "q1", "q2"}
initialState3 = "q0"
finalStates3 = {"q2"}
alphabet3 = {'a', 'b'}
tFunction3 = {
    ("q0", "a"): {"q0", "q1"},
    ("q1", "b"): {"q2"},
    ("q2", "a"): {"q2"}
}
nfa3 = NFiniteAutomaton(states3, initialState3, finalStates3, alphabet3, tFunction3)



if __name__ == '__main__':
    print("NFA1")
    ex1_strs = ["0101", "1101", "01", "000", "0110", "1011"] 
    for str in ex1_strs:
        print(str, end="")
        print(" is accepted" if nfa1.accepts(str) else " is not accepted")
    
    print("NFA2")
    ex2_strs = ["0101", "1101", "10", "000", "111", "1"] 
    for str in ex2_strs:
        print(str, end="")
        print(" is accepted" if nfa2.accepts(str) else " is not accepted")
    
    print("NFA3")
    ex3_strs = ["aaba", "aaab", "ab", "aabbaaa", "bba", "aaa"] 
    for str in ex3_strs:
        print(str, end="")
        print(" is accepted" if nfa3.accepts(str) else " is not accepted")

    # Used for test
    # print("nfa1")
    # print(nfa1.transfer_to_DFA())
    # print("nfa2")
    # print(len(nfa2.transfer_to_DFA()))
    # print("nfa3")
    # print(nfa3.transfer_to_DFA())
    # print("DFA1")
    dfa1 = nfa1.transfer_to_DFA()
    # dfa1.show_transition_function()
    # print("DFA2")
    dfa2 = nfa2.transfer_to_DFA()
    # dfa2.show_transition_function()
    # print("DFA3")
    dfa3 = nfa3.transfer_to_DFA()
    # dfa3.show_transition_function()

    print("DFA1")
    # ex1_strs = ["0101", "1101", "01", "000", "0110", "1011"] 
    for str in ex1_strs:
        print(str, end="")
        print(" is accepted" if dfa1.accepts(str) else " is not accepted")
    
    print("DFA2")
    # ex2_strs = ["0101", "1101", "10", "000", "111", "1"] 
    for str in ex2_strs:
        print(str, end="")
        print(" is accepted" if dfa2.accepts(str) else " is not accepted")
    
    print("DFA3")
    # ex3_strs = ["aaba", "aaab", "ab", "aabbaaa", "bba", "aaa"] 
    for str in ex3_strs:
        print(str, end="")
        print(" is accepted" if dfa3.accepts(str) else " is not accepted")
    print("The visualization of each DFA:")
    print("DFA1")
    dfa1.show_transition_function()
    print("DFA2")
    dfa2.show_transition_function()
    print("DFA3")
    dfa3.show_transition_function()