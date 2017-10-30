<<<<<<< HEAD
import module
from module import revComp



test_good = "TTTTCGCGATCGAGAGAAAAAA"
test_bad = "ATGATAGAGAGAILMCNCNTAGT"

revComp(test_good)
revComp(test_bad)

sequence = raw_input("Enter a DNA sequence: ")
revComp(sequence)
=======
import re
import dna
from dna import revComp

good_seq = "ATGGGGACGAGTGCC"
bad_seq = "CCATGAGATGAKLKAMNAA"

revComp(good_seq)
revComp(bad_seq)

prmpts = "Hello, type your dna seq: "

good_seq = raw_input(prmpts)
revComp(good_seq)

bad_seq = raw_input(prmpts)
revComp(bad_seq)
>>>>>>> 1c351b27496c868d7fb6367dfadf2f01503b34e2
