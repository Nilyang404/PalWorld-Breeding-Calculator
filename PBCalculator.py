#!/usr/bin/env python3
# #############################################
# By Neil
# 2024/01/23
# #############################################
import pandas as pd
import json

class PBCalculator:
    def __init__(self):
        self.data = pd.read_csv("data.csv")
        self.unique_combo = pd.read_csv("unique_combo.csv")
        with open("full_combo.json", "r") as file:
            self.full_combo = json.load(file)


# general search info
    def name_cn_to_no(self,name):
        return self.data.loc[self.data['name_cn'] == name, "NO"].iloc[0]

    def name_en_to_no(self,name):
        return self.data.loc[self.data['name_en'] == name, "NO"].iloc[0]

    def no_to_name_cn(self,no):
        return self.data.loc[self.data['NO'] == no, "name_cn"].iloc[0]

    def no_to_name_en(self,no):
        return self.data.loc[self.data['NO'] == no, "name_en"].iloc[0]
    def get_power_by_no(self,no):
        return self.data.loc[self.data['NO'] == no, "power"].iloc[0]

    def is_unique_parent(self,no_1,no_2):
       df = self.unique_combo
       parent_1 = self.no_to_name_en(no_1)
       parent_2 = self.no_to_name_en(no_2)
       return any((df['parent_1'] == parent_1) & (df['parent_2'] == parent_2)) or \
           any((df['parent_1'] == parent_2) & (df['parent_2'] == parent_1))
    def get_unique_child(self,no_1,no_2):
        df = self.unique_combo
        parent_1 = self.no_to_name_en(no_1)
        parent_2 = self.no_to_name_en(no_2)
        condition = ((df['parent_1'] == parent_1) & (df['parent_2'] == parent_2)) | \
                    ((df['parent_1'] == parent_2) & (df['parent_2'] == parent_1))
        matching_children = df[condition]['child']
        return matching_children.iloc[0]
    def is_unique_combo(self,no_1,no_2,result):
        parent_1 = self.no_to_name_en(no_1)
        parent_2 = self.no_to_name_en(no_2)
        child_name = self.no_to_name_en(result)
        df = self.unique_combo
        # if child in unique list with specific parents combo
        if child_name in self.unique_combo['child'].values:
            child_row = df[df["child"] == child_name]
            return any((child_row['parent_1'] == parent_1) & (child_row['parent_2'] == parent_2)) or \
                any((child_row['parent_1'] == parent_2) & (child_row['parent_2'] == parent_1))
        else:
            return False
    def get_breed_result(self,no_1,no_2):
        if no_1 == no_2:
            return no_1
        elif self.is_unique_parent(no_1,no_2):
            result = self.name_en_to_no(self.get_unique_child(no_1,no_2))
            return result
        else:
            name_en_1 = self.no_to_name_en(no_1)
            name_en_2 = self.no_to_name_en(no_2)
            combo = (name_en_1,name_en_2)

            power_1 = int(self.get_power_by_no(no_1))
            power_2 = int(self.get_power_by_no(no_2))
            # avg of parent
            power_avg = (power_1 + power_2)/2
            self.data['abs_diff'] = self.data['power'].apply(lambda x: abs(x -power_avg))
            df_sorted = self.data.sort_values(by=['abs_diff',"id"])
            result = df_sorted.iloc[0]["NO"]
            child_name = self.no_to_name_en(result)

            # when child in unique list but parent are not, use the second result
            index = 0
            while child_name in self.unique_combo['child'].values:
                if not self.is_unique_combo(no_1, no_2, result):
                    index += 1
                    result = df_sorted.iloc[index]["NO"]
                    child_name = self.no_to_name_en(result)
                    #print(result)
            # if child_name in self.unique_combo['child'].values:
            #     if not self.is_unique_combo(no_1, no_2 ,result):
            #         result = df_sorted.iloc[1]["NO"]


            # debug info
            # print(df_sorted)
            # print(power_1," + ", power_2," = ", power_avg,"   ",end="")
            # print(no_1," + ", no_2," = ",result,self.no_to_name_cn(result),self.no_to_name_en(result))
            return result
    def get_breed_result_by_name_cn(self,name_cn_1,name_cn_2):
        no_1 = self.name_cn_to_no(name_cn_1)
        no_2 = self.name_cn_to_no(name_cn_2)
        no = self.get_bread_result(no_1,no_2)
        return self.no_to_name_cn(no)
    def get_breed_result_by_name_en(self,name_en_1,name_en_2):
        no_1 = self.name_en_to_no(name_en_1)
        no_2 = self.name_en_to_no(name_en_2)
        no = self.get_bread_result(no_1,no_2)
        return self.no_to_name_en(no)
    def get_parents_by_child(self,no):
        return self.full_combo[no]

if __name__ == '__main__':

    cal = PBCalculator()
    print(cal.get_breed_result("1","111"))
    # for i in cal.data["NO"]:
    #     cal.get_breed_result("3", str(i))
    #print(cal.get_parents_by_child("111"))
