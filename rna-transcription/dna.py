def to_rna(dna):

    to_rna_dict = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    rna = ''
    for nucleotide in dna:
        rna += to_rna_dict[nucleotide]
    return rna