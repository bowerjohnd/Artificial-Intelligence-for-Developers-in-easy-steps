from Flatworld import *

N = 0
S = 1
E = 2
W = 3

class Fuzzy :
    def __init__(self, value=0) :
        self.value = max(0, min(1, value))

    def __and__(self, other) :
        return Fuzzy(self.value * other.value)

    def __invert__(self) :
        return Fuzzy(1 - self.value)

    def __or__(self, other) :
        return ~((~self) & (~other))

    def __gt__(self, other) :
        return self.value > other.value

    def __lt__(self, other) :
        return self.value < other.value

    def __str__(self) :
        return str(self.value)

    def __repr__(self) :
        return str(self.value)

    def closeTo(dist) :
        return Fuzzy(1 / (max(1, dist)/20) ** 2)

    if __name__ == '__main__' :

        ticks = mainLoop(
                    initialSpawns = {
                        Red: 4,
                        FuzzyLogicBot: 10,
                        Grass: 60},
                    spawnInterval = 30,
                    periodicSpawns = {Grass: 4},
                    boardSize = (750.500), playerType = Blue)

        print('That game lasted', ticks, 'ticks')
        pygame.quit()

class Spot :
    def __init__(self, position, thing) :
        self.distance, self.bearing = vector.as_polar()

# ---------------------------------------
#            Left off Here
# ---------------------------------------
