class Population:

    def __init__(self, initial_count):
        self.count = initial_count

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Population(self.count * other)
        return str(Population(self.count * other.count))


population_1 = Population(100)
population_2 = Population(5)

new_population = population_1 * 5
print(new_population)
