def number_length(num):
    length = 0
    while num != 0:
        num //= 10
        length += 1
    return length