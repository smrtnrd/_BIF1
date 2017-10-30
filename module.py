import re

def revComp(sequence):
    sequence = sequence.upper()
    valid_dna = re.match(r'^[CAGT]+$', sequence, re.I)
    if valid_dna :
        complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
        result = []
        for i in reversed(sequence):
            result.append(complement[i])
        print "Your sequence:  {}".format(sequence)
        print "The complement: {}".format(''.join(result))
    else :
        print "your sequence is not a valid"
        print "Your sequence must be compose of A,T,C or G"

