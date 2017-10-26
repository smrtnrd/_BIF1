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
