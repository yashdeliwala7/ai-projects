import pandas as pd

df = pd.DataFrame({
 "Name": ["A","B","C","D","E"],
 "Dept": ["IT","HR","IT","HR","IT"],
 "Salary": [50000,60000,None,65000,70000],
 "Experience": [2,5,3,7,None]
})

df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print(df)
df["Experience"]=df["Experience"].fillna(0)
print(df)
new=df.groupby("Dept")["Salary"].mean()
print(new)
print(df.groupby("Dept")["Salary"].sum())
print(df.groupby("Dept")["Salary"].agg(["mean", "sum", "count"]))