#import os
#os.chdir(r"C:\Users\willi\OneDrive\Desktop\porject repo\Python-project")
#os.getcwd()

#If you type a line of code update the repo

import pandas as pd
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

 #delimiter=',', header = 0
# importing data 
df = pd.read_excel('Data.xlsx')
df = df.apply(pd.to_numeric, errors='coerce')

# converting any string types into numeric values
corr = df.corr()
print(corr)

def calculate_correlation():
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("no selection, please select at least one question.")
        return
    selected_questions = [listbox.get(i) for i in selected_indices]
    subset = df[selected_questions]
    corr = subset.corr 
    
    # clear previous results
    text_box.delete("1.0", tk.END)
    
# looping throrugh every pair of columns to check if they correlate
for i, col1 in enumerate(corr.columns):
    for j, col2 in enumerate(corr.columns):
        if j <= i:
            continue # skips self  correlations
        value = corr.iloc[i, j]
        # Organizing correlations
        if abs(value) > 0.8:
            print(f'{col1} and {col2}: VERY STRONG correlation ({value: .2f})')
        elif abs(value) > 0.5:
           print(f'{col1} and {col2}: STRONG correlation ({value: .2f})') 
        elif abs(value) > 0.3:
            print(f'{col1} and {col2}: MODERATE correlation ({value: .2f})')
        else:
            print(f'{col1} and {col2}: WEAK correlation ({value: .2f})')
        
#Creating the heat map image 
plt.figure(figsize=(12, 12))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='BuPu', square=True)
plt.title("Correlation of Survey Questions")
plt.show()

# GUI setup
root = tk.Tk()
root.title("Survey Correlation Analyzer")

tk.Label(root, text="Select questions to analyze:").pack()

listbox = tk.Listbox(root, selectmode="multiple", width=50)
for col in df.columns:
    listbox.insert(tk.END, col)
listbox.pack()

tk.Button(root, text="Calculate Correlations", command=calculate_correlation).pack(pady=10)

text_box = tk.Text(root, height=15, width=70)
text_box.pack()

root.mainloop()


