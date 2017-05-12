import copy
import random


class Genepool(object):

    def __init__(self):
        self.genes = []

    def add_gene(self, to_add):
        self.genes.append(to_add)

    def remove_gene(self, to_remove):
        self.genes.remove(to_remove)

    def calculate_fitnesses(self, values_dict, answer):
        fitness = []
        for gene in self.genes:
            fitness.append({"gene": gene, "fitness": gene.get_fitness(values_dict, answer)})
        return fitness

    # tests should contain an array of dicts
    # dicts should contain an answer and a values dictionary
    def select_for_fitness(self, keep_num, tests, strategy="closest"):
        for test in tests:
            fitnesses = self.calculate_fitnesses(test["values_dict"], test["answer"])
            if strategy == "closest":
                fitnesses = sorted(fitnesses, key=lambda k: k['fitness'], reverse=True)

        while len(self.genes) > keep_num:
            self.remove_gene(fitnesses[0]['gene'])
            fitnesses.remove(fitnesses[0])

    def breed(self, desired_count, discard_old=True, strategy="uniform", breeding_strategy="inherit"):
        if discard_old:
            new_genes = []
        else:
            new_genes = self.genes

        if strategy == "uniform":
            unbred_genes = copy.deepcopy(self.genes)
            while len(new_genes) < desired_count:
                if len(unbred_genes) < 2:
                    unbred_genes = copy.deepcopy(self.genes)
                mates = random.sample(set(unbred_genes), 2)
                unbred_genes.remove(mates[0])
                unbred_genes.remove(mates[1])
                new_genes.append(mates[0].breed(mates[1], strategy=breeding_strategy))
            self.genes = new_genes
        elif strategy == "random":
            gene_set = set(self.genes)
            while len(new_genes) < desired_count:
                mates = random.sample(gene_set, 2)
                new_genes.append(mates[0].breed(mates[1], strategy=breeding_strategy))
            self.genes = new_genes
