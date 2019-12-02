


def readNewLine(filename):
    arr = []
    with open(filename) as file:
        for line in file:
            arr.append(int(line.strip()))
    return arr

def readComma(filename):
    with open(filename) as file:
        return str(file).split(",")
