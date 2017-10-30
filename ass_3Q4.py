import module
from module import revComp



test_good = "TTTTCGCGATCGAGAGAAAAAA"
test_bad = "ATGATAGAGAGAILMCNCNTAGT"

revComp(test_good)
revComp(test_bad)

sequence = raw_input("Enter a DNA sequence: ")
revComp(sequence)
