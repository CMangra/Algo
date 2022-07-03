import sys  # provides getsizeof function


def code_fragment_5_1():
    data = []
    for k in range(10):
        a = len(data)  # number of elements
        b = sys.getsizeof(data)  # actual size in bytes
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(" ")  # increase length by one
    return data


def pop_element():
    data = code_fragment_5_1()
    for k in range(len(data)-1, -2, -1):
        a = len(data)  # number of elements
        b = sys.getsizeof(data)  # actual size in bytes
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        if k != -1:
            data.pop(k)  # decrease length by one


pop_element()
