from genepool import Genepool
from gene import *
import random


def main():
    pool = Genepool()
    for i in range(0, 100):
        pool.add_gene(Gene({'a': random.random(), 'b': random.random(), 'c': random.random()}))
    correct_tests = [{'answer': 1, 'values_dict': {'a': 1, 'b': 2, 'c': 3}}]
    pool.select_for_fitness(10, correct_tests)
    for i in range(0, 10):
        pool.breed(100)
        pool.select_for_fitness(50, correct_tests)
    pool.breed(100)
    pool.select_for_fitness(50, correct_tests)
    for i in range(0, 10):
        print pool.genes[i].alleles

if __name__ == "__main__":
    main()