#!/usr/bin/env python3
# #############################################
# By Neil
# 2024/01/23
# #############################################
import pandas as pd

class PBCalculator:
    def __init__(self):
        self.data = pd.read_csv("data.csv")

# general search info
    def name_cn_to_no(self,name):
        return self.data.loc[self.data['name_cn'] == name, "NO"].iloc[0]

    def name_en_to_no(self,name):
        return self.data.loc[self.data['name_en'] == name, "NO"].iloc[0]

    def no_to_name_cn(self,no):
        return self.data.loc[self.data['NO'] == no, "name_cn"].iloc[0]

    def no_to_name_en(self,no):
        return self.data.loc[self.data['NO'] == no, "name_en"].iloc[0]
    def get_power(self,no):
        return self.data.loc[self.data['NO'] == no, "power"].iloc[0]

if __name__ == '__main__':
    # test_case_1
    # cal = PBCalculator()
    # print(cal.name_en_to_no("Mammorest Cryst"))