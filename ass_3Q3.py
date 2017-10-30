import re
import sys

def search_seq(short_dna, sequence):
    s = re.search( short_dna, sequence, re.I)
    if s : # if search() found the motif
        dna_1 = "The motif {}".format(short_dna)
        seq_1 = " is found in {}".format(sequence)
        print dna_1 + seq_1
    else:
        dna_1 = "The motif {}".format(short_dna)
        seq_1 = " is NOT found in {}".format(sequence)
        print dna_1 + seq_1

#good test
short_dna = "TTT"
sequence = "aaaaaTTTTaaaTTTTaaat"
search_seq(short_dna, sequence)


#bad test
short_dna = "TIT"
sequence = "aaaaaTTTTaaaTTTTaaat"
search_seq(short_dna, sequence)

#test
#short_dna = raw_input("The short dna: ")
#sequence = raw_input("Sequence: ")
#search_seq(short_dna, sequence)
