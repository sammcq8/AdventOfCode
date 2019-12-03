
import turtle as tt

def readfile(filename):
    with open(filename) as file:
        red_wire = file.readline().split(",")
        green_wire = file.readline().split(",")
    return red_wire, green_wire


def chart_path(wire_list):
    x = 0
    y = 0
    seen_squares = set()
    for movement in wire_list:
        direction = movement[0]
        distance = int(movement[1:])
        if direction == "D" or direction == "L":
            for i in range(distance):

                if direction == "D":
                    y -= 1
                elif direction == "L":
                    x -= 1
                print(x, y)
                seen_squares.add((x, y))

        if direction == "U" or direction == "R":
            for i in range(distance):

                if direction == "U":
                    y += 1
                elif direction == "R":
                    x += 1
                
                seen_squares.add((x, y))



            
    return seen_squares


def chart_path_ls(wire_list):
    x = 0
    y = 0
    steps = 0
    seen_squares = dict()
    for movement in wire_list:
        direction = movement[0]
        distance = int(movement[1:])
        if direction == "D" or direction == "L":
            for i in range(distance):
                steps +=1
                if direction == "D":
                    y -= 1
                elif direction == "L":
                    x -= 1

                seen_squares[(x, y)] = steps

        if direction == "U" or direction == "R":
            for i in range(distance):
                steps += 1
                if direction == "U":
                    y += 1
                elif direction == "R":
                    x += 1

                seen_squares[(x, y)] = steps

    return seen_squares


def find_intersections_ls(wires):
    red_wire = chart_path_ls(wires[0])
    green_wire = chart_path_ls(wires[1])

    intersections = red_wire.keys() & green_wire.keys()
    closest = None
    best_intersection = None
    for intersection in intersections:
        steps = red_wire[intersection] + green_wire[intersection]
        if closest is None or closest > steps:
            closest = steps
            best_intersection = intersection
    return closest


def chart_path(wire_list):
    x = 0
    y = 0
    seen_squares = set()
    for movement in wire_list:
        direction = movement[0]
        distance = int(movement[1:])
        if direction == "D" or direction == "L":
            for i in range(distance):

                if direction == "D":
                    y -= 1
                elif direction == "L":
                    x -= 1

                seen_squares.add((x, y))

        if direction == "U" or direction == "R":
            for i in range(distance):

                if direction == "U":
                    y += 1
                elif direction == "R":
                    x += 1
                
                seen_squares.add((x, y))



            
    return seen_squares

    

def find_intersections(wires):
    red_wire = chart_path(wires[0])
    green_wire = chart_path(wires[1])

    intersections = red_wire.intersection(green_wire)
    closest = None
    for intersection in intersections:
        dist = abs(intersection[0]) + abs(intersection[1])
        if closest is None or closest > dist:
            closest = dist
    return closest
            

def find_intersections(wires):
    red_wire = chart_path(wires[0])
    green_wire = chart_path(wires[1])

    intersections = red_wire.intersection(green_wire)
    closest = None
    for intersection in intersections:
        dist = abs(intersection[0]) + abs(intersection[1])
        if closest is None or closest > dist:
            closest = dist
    return closest
            

def ttdraw(wire_list):
    x = 0
    y = 0
    seen_squares = set()
    for movement in wire_list:
        direction = movement[0]
        distance = int(movement[1:])/10
        if direction == "D" or "L":
            distance = -distance

        if direction == "L" or "R":
            tt.right(90)
            tt.fd(distance)
           
        else:
            tt.fd(distance)
            




def main():

    wires = readfile("day3/input.txt")
    tt.tracer(0)
    tt.color("red")
    ttdraw(wires[0])
    tt.setpos(0,0)
    tt.setheading(0)
    tt.color("green")
    ttdraw(wires[1])
    tt.done()
    print(find_intersections_ls(wires))



if __name__ == "__main__":
    main()
