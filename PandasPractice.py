# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("myexcel.csv", index_col="Name")

# retrieving columns by indexing operator
first = data[["Age","Team"]]

print(first)
# dropping passed values
data.drop(["Avery Bradley", "John Holland", "R.J. Hunter",
           "R.J. Hunter"], inplace=False)

# display
print(data)
data1 = pd.read_csv("myexcel.csv", index_col="Name")
print(data1)

