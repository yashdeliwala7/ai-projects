import pandas as pd  
data = {
 "Name": ["A","B","C","D"],
 "Age": [20,25,30,22],
 "Marks": [80,90,85,70]
}

df=pd.DataFrame(data)
print(df)
print(df[df["Marks"] > 80]) 
print(df[(df["Marks"] > 80) & (df["Age"] > 21)])
