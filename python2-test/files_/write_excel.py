import os
import numpy as np
import pandas as pd

filepath = os.path.abspath(".")
filename = "df.xlsx"
files = os.path.join(filepath, filename)
print(files)

data = pd.DataFrame(np.arange(200).reshape(50,4))
print(data)

print(data.to_excel(files, sheet_name="Sheet1", header=True, index=True, index_label="id", startrow=1, startcol=1))

