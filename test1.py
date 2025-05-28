from dfa import DFiniteAutomaton

# Example 1: check if a 01-string has an odd number of 1s.
states1 = {"q0", "q1"}
initialState1 = "q0"
finalStates1 = {"q1"}
alphabet1 = {"0", "1"}
tFunction1 = {
    ("q0", "0"): "q0",
    ("q0", "1"): "q1",
    ("q1", "0"): "q1",
    ("q1", "1"): "q0"
}
dfa1 = DFiniteAutomaton(states1, initialState1, finalStates1, alphabet1, tFunction1) 

# Example 2: check if a 01-string has an even number of 0s.
states2 = {"q0", "q1"}
initialState2 = "q0"
finalStates2 = {"q0"}
alphabet2 = {"0", "1"}
tFunction2 = {
    ("q0", "1"): "q0",
    ("q0", "0"): "q1",
    ("q1", "0"): "q0",
    ("q1", "1"): "q1" 
}
dfa2 = DFiniteAutomaton(states2, initialState2, finalStates2, alphabet2, tFunction2) 

# Example 3: check if a 01-string has an even number of 0s and an even nmber of 1s.
states3 = {"q0", "q1", "q2", "q3"}
initialState3 ="q0"
finalStates3 = {"q0"}
alphabet3 = {"0", "1"}
tFunction3 = {
    ("q0", "0"): "q2",
    ("q0", "1"): "q1",
    ("q1", "0"): "q3",
    ("q1", "1"): "q0",
    ("q2", "0"): "q0",
    ("q2", "1"): "q3",
    ("q3", "0"): "q1",
    ("q3", "1"): "q2",
}
dfa3 = DFiniteAutomaton(states3, initialState3, finalStates3, alphabet3, tFunction3) 

# Example 4: check if a 01-string ends with 01 and does not contain 11 as a substring.
states4 = {"q0", "q1", "q2", "q3", "qdead"}
initialState4 = "q0"
finalStates4 = {"q2"}
alphabet4 = {"0", "1"}
tFunction4 = {
    ("q0", "0"): "q1",
    ("q0", "1"): "q3",
    ("q1", "0"): "q1",
    ("q1", "1"): "q2",
    ("q2", "0"): "q1",
    ("q2", "1"): "qdead",
    ("q3", "0"): "q1",
    ("q3", "1"): "qdead",
    ("qdead", "0"): "qdead",
    ("qdead", "1"): "qdead"
}

dfa4 = DFiniteAutomaton(states4, initialState4, finalStates4, alphabet4, tFunction4) 

if __name__ == '__main__':
    print("DF1") # Test of example 1
    ex1_strs = ["0111", "1101", "1", "000", "0110", "101"] 
    for str in ex1_strs:
        print(str, end="")
        print(" is accepted" if dfa1.accepts(str) else " is not accepted")

    print("DF2") # Test of example 2
    ex2_strs = ["111", "010", "10101010", "10", "10001", "1101"]
    for str in ex2_strs:
        print(str, end="")
        print(" is accepted" if dfa2.accepts(str) else " is not accepted")

    print("DF3") # Test of example 3
    ex3_strs = ["1100", "0101010111", "0110", "11100", "110", "11111000"]
    for str in ex3_strs:
        print(str, end="")
        print(" is accepted" if dfa3.accepts(str) else " is not accepted")

    print("DF4") # Test of example 4
    ex4_strs = ["101", "00001", "001", "0110", "1101", "00101011"]
    for str in ex4_strs:
        print(str, end="")
        print(" is accepted" if dfa4.accepts(str) else " is not accepted")
    