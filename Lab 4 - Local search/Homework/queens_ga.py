import random
import queens_fitness

p_mutation = 0.2
num_of_generations = 30

def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        print_population(population, fitness_fn)

        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child1, child2 = reproduce(mother, father)

            if random.uniform(0, 1) < p_mutation:
                child1 = mutate(child1)
            if random.uniform(0, 1) < p_mutation:
                child2 = mutate(child2)

            new_population.add(child1)
            new_population.add(child2)

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = population.union(new_population)

        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    '''
    Reproduce two individuals with single-point crossover
    Return the child individual
    '''

    individual_length = len(mother)
    child1 = []
    child2 = []

    crossover_point = random.randint(0, individual_length)
    for i in range(0, individual_length):
        if i >= crossover_point:
            child1.append(father[i])
            child2.append(mother[i])
        else:
            child1.append(mother[i])
            child2.append(father[i])

    return (tuple(child1), tuple(child2))


def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''

    mutation = list(individual)
    choosen_bit = random.randint(0, len(individual)-1)
    mutation[choosen_bit] = random.randint(0, len(individual)-1)

    return tuple(mutation)


def random_selection(population, fitness_fn):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """

    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.
    ordered_population = list(population)

    mother = None
    father = None

    total_fitness = 0
    for individual in population:
        fitness = fitness_fn(individual)
        total_fitness += fitness

    mother_num = random.randint(total_fitness, 0)
    father_num = random.randint(total_fitness, 0)

    acc_fitness = 0
    for individual in population:
        fitness = fitness_fn(individual)
        acc_fitness += fitness
        if acc_fitness <= mother_num and mother == None:
            mother = individual
        if acc_fitness <= father_num and father == None:
            father = individual
        if mother != None and father != None:
            break

    selected = (mother, father)
    return selected


def fitness_function(individual):
    '''
    Computes the decimal value of the individual
    Return the fitness level of the individual
    '''
    fitness = queens_fitness.fitness_fn_negative(individual)
    return fitness


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    '''
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    '''
    return set([
        tuple(random.randint(0, n-1) for _ in range(n))
        for _ in range(count)
    ])


def main():
    minimal_fitness = 0

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary
    initial_population = {
        (0,1,2,3),
        (3,2,1,0)
    }

    #initial_population = get_initial_population(8, 4)

    fittest = genetic_algorithm(
        initial_population, fitness_function, minimal_fitness)
    print('Fittest Individual: ' + str(fittest) + " = " + str(fitness_function(fittest)))


if __name__ == '__main__':
    #pass
    main()
