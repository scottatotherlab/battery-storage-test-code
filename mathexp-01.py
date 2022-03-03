from itertools import combinations
sample_list = ['1','2','3','4']
list_combinations = list()
for n in range(len(sample_list) + 1):
    list_combinations += list(combinations(sample_list, n))
print(list_combinations)
