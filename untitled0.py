# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 12:45:43 2025

@author: avask
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load data
df = pd.read_excel("Data.xlsx")
df = df.apply(pd.to_numeric, errors="coerce")

# Main GUI window
root = tk.Tk()
root.title("Survey Correlation Analyzer")

# Global placeholder for canvas so we can destroy old graphs
canvas_widget = None


# scatter plot function
def calculate_correlation():
    global canvas_widget

    selected_indices = listbox.curselection()

    # Must pick exactly TWO questions
    if len(selected_indices) != 2:
        messagebox.showwarning("Selection Error",
                               "Please select exactly TWO questions to generate a scatterplot.")
        return

    q1 = listbox.get(selected_indices[0])
    q2 = listbox.get(selected_indices[1])

    subset = df[[q1, q2]].dropna()
    corr_value = subset[q1].corr(subset[q2])

    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, f"Correlation between {q1} and {q2}: {corr_value:.3f}\n")

    # Create scatterplot
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.regplot(data=subset, x=q1, y=q2, ax=ax, ci=None)
    ax.set_title(f"{q1} vs {q2}\nCorrelation = {corr_value:.3f}")
    ax.set_xlabel(q1)
    ax.set_ylabel(q2)

    # Destroy previous plot
    if canvas_widget is not None:
        canvas_widget.get_tk_widget().destroy()

    # Embed new plot
    canvas_widget = FigureCanvasTkAgg(fig, master=root)
    canvas_widget.draw()
    canvas_widget.get_tk_widget().pack(pady=10)


# Full coreleation matrix
def show_full_correlation():
    global canvas_widget

    corr_matrix = df.corr()

    # Create heatmap
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Matrix for All Questions")

    # Destroy old plot
    if canvas_widget is not None:
        canvas_widget.get_tk_widget().destroy()

    # Embed heatmap
    canvas_widget = FigureCanvasTkAgg(fig, master=root)
    canvas_widget.draw()
    canvas_widget.get_tk_widget().pack(pady=10)


# GUI Layout
tk.Label(root, text="Select ANY TWO questions to compare:").pack()

listbox = tk.Listbox(root, selectmode="multiple", width=50)
for col in df.columns:
    listbox.insert(tk.END, col)
listbox.pack()

# button to create scatter plot
tk.Button(root, text="Generate Scatterplot", command=calculate_correlation).pack(pady=5)

# button for full corelation
tk.Button(root, text="Show Full Correlation Matrix", command=show_full_correlation).pack(pady=5)

text_box = tk.Text(root, height=6, width=60)
text_box.pack()

root.mainloop()