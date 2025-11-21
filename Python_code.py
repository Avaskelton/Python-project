import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#loading data
# clean_lines = []
# with open('Yssrb_data.txt', 'r') as f:
#     for line in f:
#         clean_line = line.replace(',', '')  # remove commas
#         clean_lines.append(clean_line)

# # Optionally save cleaned data
# with open('Yssrb_data_clean.txt', 'w') as f:
#     f.writelines(clean_lines)
df = pd.read_csv('Yssrb_data.txt', delimiter=',', header = 0)
df.head()




print(df.head())

#df = df.replace(',', '', regex=True)
# for line in df:
#     parts = line.strip().split(',')

