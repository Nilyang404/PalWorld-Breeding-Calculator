import pandas as pd
df = pd.read_csv("data.csv")
df2 = pd.read_csv("index.csv")


merged_df = pd.merge(df, df2[['name_en', 'id']], on='name_en', how='left')

print(merged_df)
# df = pd.read_csv("data.csv")
merged_df = merged_df.drop('index', axis=1)
merged_df.to_csv("data.csv",index=False)
#
#
# #df.to_csv(("data.csv"))
# print(df)