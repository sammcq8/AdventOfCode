"""

"""
from math import trunc
import sys
def countFuel(mass):
    return trunc(mass/3) - 2

def fileread(filename):
    arr = []
    with open(filename) as file:
        for line in file:
            arr.append(int(line.strip()))
    return arr

def main():
    filename = sys.argv[1]
    arr = fileread(filename)
    sum = 0
    for item in arr:
        sum += countFuel(item)
    print(sum)

if __name__ == "__main__":
    main()