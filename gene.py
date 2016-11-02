import random


#  Expects to be passed a properties object comprised of a dictionary object
class Gene(object):

    def __init__(self, alleles):
        self.alleles = alleles

    def breed(self, other, strategy="inherit"):
        #  compare to make sure all properties match
        #  if not, error
        #  if so, combine alleles
        if self.alleles.keys() != other.alleles.keys():
            raise ValueError("The two genes do not have the same alleles and are incompatible.")

        if strategy == "inherit":
            new_gene_alleles = {}
            for k, v in self.alleles.items():
                new_gene_alleles[k] = random.choice([v, other.alleles[k]])
            return Gene(new_gene_alleles)

    def get_fitness(self, values_dict, answer):
        #  pair alleles with corresponding values from values_dict and determine distance from answer
        if self.alleles.keys() != values_dict.keys():
            raise ValueError("The gene and the value dictionary do not match and are incompatible.")

        sum = 0
        for k, v in self.alleles.items():
            sum += v*values_dict[k]
        return abs(sum-answer)
