import pandas as pd


df1 = pd.DataFrame({
 "Name": ["A","B","C"],
 "Dept": ["IT","HR","IT"]
})

df2 = pd.DataFrame({
 "Dept": ["IT"],
 "Manager": ["X"]
})

print(pd.merge(df1, df2, on="Dept",how="left"))