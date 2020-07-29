import os
import numpy as np
import pandas as pd

filepath = os.path.abspath(".")
filename = "df.xlsx"
files = os.path.join(filepath, filename)
print(files)

# data = pd.read_excel(files, sheet_name="Sheet1", header=2, index_col="id")
data = pd.read_excel(files)
print(data)


