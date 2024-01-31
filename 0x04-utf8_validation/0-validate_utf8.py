#!/usr/bin/python3
''' UTF-8 Validation
'''


def validUTF8(data):
    ''' determines if a given data set
        represents a valid UTF-8 encoding
    '''
    if not data or not isinstance(data, list) or\
            not all([isinstance(n, int) for n in data]):
        return False
    binary_list = [format(decimal_number, '08b') for decimal_number in data]
    i = 0
    while i < len(binary_list):
        byt = binary_list[i]
        if byt.startswith('0'):
            i = i + 1
        elif byt.startswith('110'):
            if not binary_list[i + 1].startswith('10'):
                return False
            i = i + 2
        elif byt.startswith('1110'):
            for j in range(i + 1, i + 3):
                if not binary_list[j].startswith('10'):
                    return False
            i = i + 3
        elif byt.startswith('11110'):
            for j in range(i + 1, i + 4):
                if not binary_list[j].startswith('10'):
                    return False
            i = i + 4
        else:
            return False
    return True
