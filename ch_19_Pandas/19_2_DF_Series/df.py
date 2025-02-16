import pandas as pd

data = {
    "Name" : ["Alice", "Bob", "Cathy", "Robert"],
    "Age" : [25, 35, 28, 39],
    "City" : ["New-York", "Boston", "California", "Chicago"]
}

df = pd.DataFrame(data)

print(f"DF из dict:\n{df}")

data_2 = [
    ["Alice", 28, "New-York"],
    ["Michael", 36, "Boston"],
    ["Kate", 26, "California"],
    ["Robert", 38, "Chicago"],
]

df_from_list = pd.DataFrame(data_2, columns=["Name", "Age", "City"])
print(f"DF из list:\n{df_from_list}")