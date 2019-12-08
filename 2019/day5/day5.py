"""
19690720
"""

import sys


def read_intcode(arr):
    
    pos = 0
    while True:
        if arr[pos] == 99:
            break
        else:
            code = str(arr[pos])
            instruction = int(code[-2:])
            modes = code[:-2]
            while len(modes) < 3:
                modes = "0"+modes
            if instruction == 1:
                saveVal = arr[pos+3]
                a = PARAMETER_MODES[modes[-1]](arr[pos+1], pos, arr)
                b = PARAMETER_MODES[modes[-2]](arr[pos+2], pos, arr)
                arr[saveVal] = a + b
                pos+=4
            elif instruction == 2:
                saveVal = arr[pos+3]

                a = PARAMETER_MODES[modes[-1]](arr[pos+1], pos, arr)
                b = PARAMETER_MODES[modes[-2]](arr[pos+2], pos, arr)
                arr[saveVal] = a * b
                pos+=4
            elif instruction == 3:
                saveVal = arr[pos+1]
                arr[arr[pos+1]] = inputVal()
                pos+=2
            elif instruction == 4:
                output(PARAMETER_MODES[modes[-1]](arr[pos+1],pos, arr))
                pos+=2
            
            elif instruction == 5:
                a = PARAMETER_MODES[modes[-1]](arr[pos+1], pos, arr)
                b = PARAMETER_MODES[modes[-2]](arr[pos+2], pos, arr)
                if a != 0:
                    pos = b
                else:
                    pos += 3
            elif instruction == 6:
                a = PARAMETER_MODES[modes[-1]](arr[pos+1], pos, arr)
                b = PARAMETER_MODES[modes[-2]](arr[pos+2], pos, arr)
                if a == 0:
                    pos = b
                else:
                    pos +=3
            elif instruction == 7:
                saveVal = arr[pos+3]
                a = PARAMETER_MODES[modes[-1]](arr[pos+1], pos, arr)
                b = PARAMETER_MODES[modes[-2]](arr[pos+2], pos, arr)
                if a < b:
                    arr[saveVal] = 1
                else:
                    arr[saveVal] = 0
                pos += 4
            elif instruction == 8:
                saveVal = arr[pos+3]
                a = PARAMETER_MODES[modes[-1]](arr[pos+1], pos, arr)
                b = PARAMETER_MODES[modes[-2]](arr[pos+2], pos, arr)
                if a == b:
                    arr[saveVal] = 1
                else:
                    arr[saveVal] = 0
                pos += 4
            else:
                raise Exception
    return arr[0]

def position(a, pos, lst):
    return lst[a]

def immediate(a,pos, lst):
    return a


def multiply(a, b):
    return a*b

def add(a, b):
    return a+b

def inputVal():
    return int(input(":"))

def output(a):
    print(a)


PARAMETER_MODES = {
    '0': position,
    '1': immediate
}

FUCNTIONS = {
    1: multiply,
    2: add,
    3: inputVal,
    4: output
}

def readComma(filename):
    with open(filename) as file:
        lst = file.read().split(',')
        new_lst = []
        for item in lst:
            new_lst.append(int(item.strip()))
        return new_lst


def find_params(arr, want):
    for i in range(100):
        arr[1] = i
        for j in range(100):
            arr[2] = j
            if read_intcode(arr.copy()) == want:
                return 100*i+j


def main():
    arr = readComma("day5/input.txt")
    read_intcode(arr)



if __name__ == "__main__":
    main()
