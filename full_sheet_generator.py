import pandas as pd
from PBCalculator import PBCalculator
from itertools import combinations_with_replacement
import json

if __name__ == '__main__':
    cal = PBCalculator()
    df = cal.data

results_dict = {}

for no_1, no_2 in list(combinations_with_replacement(df['NO'], 2)):
    result = cal.get_breed_result(no_1, no_2)
    print(no_1, no_2, result)
    if result in results_dict:
        results_dict[result].append((no_1,no_2))
    else:
        results_dict[result] = [(no_1, no_2)]

with open("full_combo.json","w") as file:
    json.dump(results_dict, file)

# def query_results(no):
#     combinations = results_dict(no)
#     print(combinations)

