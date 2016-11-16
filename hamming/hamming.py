def distance(dna1, dna2):

    hammingDistance = 0
    for idx, item in enumerate(dna1):
        if dna1[idx] != dna2[idx]:
            hammingDistance += 1    
    return hammingDistance