def distance(strand_a, strand_b):
    if len(strand_a) == 0 and len(strand_b) != 0:
        raise ValueError("left strand must not be empty.")
    elif len(strand_a) != 0 and len(strand_b) == 0:
        raise ValueError("right strand must not be empty.")
    if len(strand_a) != len(strand_b):
        raise ValueError("leftStrand and rightStrand must be of equal length.")
    count = 0
    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            count = count + 1
    return count
