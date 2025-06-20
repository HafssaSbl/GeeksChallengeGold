import random


class Gene:
    def __init__(self, value=None):
        if value is None:
            value = random.choice([0, 1])
        self.value = value

    def mutate(self):
        self.value = 1 - self.value

    def __str__(self):
        return str(self.value)

    def is_one(self):
        return self.value == 1


class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:  
                gene.mutate()

    def is_all_ones(self):
        return all(gene.is_one() for gene in self.genes)

    def __str__(self):
        return ''.join(str(g) for g in self.genes)



class Dna:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)] 

    def mutate(self):
        for chromosome in self.chromosomes:
            chromosome.mutate()

    def is_all_ones(self):
        return all(chromosome.is_all_ones() for chromosome in self.chromosomes)

    def __str__(self):
        return '\n'.join(str(c) for c in self.chromosomes)



class Organism:
    def __init__(self, environment):
        self.dna = Dna()
        self.environment = environment  

    def mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()

    def is_perfect(self):
        return self.dna.is_all_ones()

    def __str__(self):
        return str(self.dna)



if __name__ == "__main__":
    organism = Organism(environment=0.9)
    generation = 0
    max_generations = 1000

    while not organism.is_perfect() and generation < max_generations:
        organism.mutate()
        generation += 1

    if organism.is_perfect():
        print(f"ADN parfait trouvé en {generation} générations !")
    else:
        print("Limite atteinte sans ADN parfait.")
    
    print(organism)
