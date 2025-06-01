# Theory of Computation
# Assignment 2

Test environment in my computer:
```
5.15.153.1-microsoft-standard-WSL2
Python 3.12.7 
```

No other libraries are included in these source codes.

Introduction of each file:
- `dfa.py`: contains the implementation of the deterministic finite automaton.
- `test.py1`: test file in assignment 1.
- `test.py2`: test file in assignment 2.

To test, use the following command in your terminal(Windows, or Mac OS):
```
python test2.py
```

If you are using Linux (Ubuntu), simply run:
```
python3 test2.py
```
in your terminal.

You will see the following result for assignment 2.
```sh
NFA1
0101 is accepted
1101 is accepted
01 is accepted
000 is not accepted
0110 is not accepted
1011 is not accepted
NFA2
0101 is accepted
1101 is accepted
10 is accepted
000 is not accepted
111 is not accepted
1 is not accepted
NFA3
aaba is accepted
aaab is accepted
ab is accepted
aabbaaa is not accepted
bba is not accepted
aaa is not accepted
DFA1
0101 is accepted
1101 is accepted
01 is accepted
000 is not accepted
0110 is not accepted
1011 is not accepted
DFA2
0101 is accepted
1101 is accepted
10 is accepted
000 is not accepted
111 is not accepted
1 is not accepted
DFA3
aaba is accepted
aaab is accepted
ab is accepted
aabbaaa is not accepted
bba is not accepted
aaa is not accepted
The visualization of each DFA:
DFA1
(frozenset({'q0', 'q1'}), '1') frozenset({'q2', 'q0'})
(frozenset({'q0', 'q1'}), '0') frozenset({'q0', 'q1'})
(frozenset({'q0'}), '1') frozenset({'q0'})
(frozenset({'q0'}), '0') frozenset({'q0', 'q1'})
(frozenset({'q2', 'q0'}), '1') frozenset({'q0'})
(frozenset({'q2', 'q0'}), '0') frozenset({'q0', 'q1'})
DFA2
(frozenset({'q0', 'q1'}), '1') frozenset({'q2', 'q0', 'q3'})
(frozenset({'q0', 'q1'}), '0') frozenset({'q0', 'q1'})
(frozenset({'q0'}), '1') frozenset({'q2', 'q0'})
(frozenset({'q0'}), '0') frozenset({'q0', 'q1'})
(frozenset({'q2', 'q0', 'q3'}), '1') frozenset({'q2', 'q0', 'q3'})
(frozenset({'q2', 'q0', 'q3'}), '0') frozenset({'q0', 'q3', 'q1'})
(frozenset({'q0', 'q3', 'q1'}), '1') frozenset({'q2', 'q0', 'q3'})
(frozenset({'q0', 'q3', 'q1'}), '0') frozenset({'q0', 'q3', 'q1'})
(frozenset({'q2', 'q0'}), '1') frozenset({'q2', 'q0'})
(frozenset({'q2', 'q0'}), '0') frozenset({'q0', 'q3', 'q1'})
DFA3
(frozenset({'q2'}), 'a') frozenset({'q2'})
(frozenset({'q0', 'q1'}), 'a') frozenset({'q0', 'q1'})
(frozenset({'q0', 'q1'}), 'b') frozenset({'q2'})
(frozenset({'q0'}), 'a') frozenset({'q0', 'q1'})
```
Note that DFAi is corresponding DFAs of NFAs(i=1, 2, 3), 
