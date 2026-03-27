import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Age": [20, 21, 22,],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)
print(df)
print(df[df["Marks"] >  85])
print(df[(df["Marks"] > 80) & (df["Age"] > 21)])
print(df[["Name", "Marks"]])