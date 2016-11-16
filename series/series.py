def slices(digits, n):
    if n < 1:
        raise ValueError("Length argument must be greater than zero. Please\
                         enter a different value.")
    if n > len(digits):
        raise ValueError("Length argument must be the same size or smaller than\
                         the string of digits.")
    digitsArray = map(int, digits)
    series = []
    for i in range(len(digitsArray)):
        if i < (len(digitsArray) - (n - 1)):
            subSeries = digitsArray[i:n + i]
            series.append(subSeries)
    return series