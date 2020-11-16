from dataclasses import dataclass
from typing import Union


@dataclass
class Planet:
    name: str
    orbitedBy: Union[None, list, 'Planet']
    def __hash__(self):
        return hash(self.name)


def readFile(filename):
    planets = dict()
    with open(filename) as file:
        for line in file:
            line = line.strip().split(")")
            name = line[0]
            orbitedByPlanet = line[1]
            if name not in planets:
                planets[name] = Planet(name, [orbitedByPlanet])
            else:
                planets[name].orbitedBy.append(orbitedByPlanet)

    fixDict(planets)
    return planets



def fixDict(stuff):
    for planet in stuff.values():
        orbitingPlanetsFixed = []
        unaddedPlanet = []
        for orbitingPlanet in planet.orbitedBy:
            if orbitingPlanet in stuff:
                orbitingPlanetsFixed.append( stuff[orbitingPlanet])
            else:
                unaddedPlanet.append(orbitingPlanet)
        planet.orbitedBy = orbitingPlanetsFixed

    for planet in unaddedPlanet:
        stuff[planet] = Planet(planet, None)
        orbitingPlanetsFixed.append(stuff[orbitingPlanet])


def countOrbits(planet):
    if planet == "COM":
        return 0
    else:
        return 1 + countOrbits(planet.orbiting)

def findPath(planet, wantedPlanet, pathSet= set()):

    if planet.name == wantedPlanet:
        return pathSet
    if planet.orbitedBy is None:
        return None
    for node in planet.orbitedBy:
        if node is None:
            continue
        else:
            pathSet.add(planet.name)
            foundPath = findPath(node, wantedPlanet, pathSet)
            if foundPath is not None:
                return pathSet
            else:
                return None
            
def comparePaths(path1, path2):
    intersection = path1 & path2
    return intersection
        
def main():
    filename = "day6/input.txt"
    treeDict = readFile(filename)
    comNode = treeDict["COM"]
    """orbits = 0
    for planet in treeDict.values():
        orbits += countOrbits(planet)
    print(orbits)"""
    path = findPath(treeDict, "YOU")
    print(path)
    



if __name__ == "__main__":
    main()
