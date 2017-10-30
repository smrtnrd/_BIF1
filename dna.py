def revComp(sequence):
    warning = "This sequence is not valid"
    isValid = re.search(r'^[atcg]+$', sequence, re.I)
    complement = {'A':'T', 'C':'G', 'G':'T', 'T':'A'}
    if isValid:
        result =[]
        for i in sequence:
            result.append(complement[i])
        rev_comp = ''.join(result[::-1])
        print "The sequence: {}".format(sequence)
        print "The rev complement: {}".format(rev_comp)
    else:
        print warning
