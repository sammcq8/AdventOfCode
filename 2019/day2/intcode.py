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
            position_int1 = arr[pos+1]
            position_int2 = arr[pos+2]
            end_loc_pos = arr[pos+3]
            if arr[pos] == 1:
                arr[end_loc_pos] = arr[position_int1] + arr[position_int2]
            elif arr[pos] == 2:
                arr[end_loc_pos] = arr[position_int1] * arr[position_int2]
            else:
                raise Exception
            pos += 4
    return arr[0]
            

def readComma(filename):
    with open(filename) as file:
        lst =  file.read().split(',')
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
    arr = readComma(sys.argv[1])
    print(find_params(arr, 19690720))


if __name__ == "__main__":
    main()
