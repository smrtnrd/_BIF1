import re
import sys

def  search_seq(short_dna, sequence):
    regex = "r\"("+short_dna+")G\""
    s = re.search(regex, sequence, flags=0)
    if s : # if search() found the motif
        dna_1 = "The motif ".format(short_dna)
        seq_1 = " is found in ".format(sequence)
        print dna_1 + seq_1

short_dna = input("The short dna: ")
print "Thank you "
sequence = input("Sequence: ")
print "Thank you "
