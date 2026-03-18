import pandas as pd 

#------------------- Data Frames ---------------------#
# DataFrame = A tabular data structure with rows AND columns. (2 Dimensional)
#             Similar to an Excel spreadsheet

data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "Age":  [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
print(df)
print()
print(df.loc["Employee 3"])
print()
print(df.iloc[1])
print()

# Add a new column 
df["Job"] = ["Cook", "N/A", "Cashier"]
print(df)
print()

# Add new row
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                        {"Name": "Eugene", "Age": 60, "Job": "Manager"}],
                        index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_row])
print(df)

#----------------------- Importing -------------------#
df1 = pd.read_csv("Day 6\pokemon.csv")
print(df1)
print()
print(df1.to_string())

# read json file:
# df2 = pd.read_jason("data.json")