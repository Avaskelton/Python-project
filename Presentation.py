# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 09:58:14 2025

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
# Plot types
plot_types = ["Scatterplot", "Boxplot", "Heatmap"]
# scatter plot function
def generate_plot():
    global canvas_widget
    selected_indices = listbox.curselection()
    plot_choice = plot_type_var.get()
    # Destroy previous plot
    if canvas_widget is not None:
        canvas_widget.get_tk_widget().destroy()
    # Scatterplot and boxplot require exactly 2 questions
    if plot_choice in ["Scatterplot", "Boxplot"] and len(selected_indices) != 2:
        messagebox.showwarning("Selection Error", 
                               f"Please select exactly TWO questions for a {plot_choice}.")
        return
    fig, ax = plt.subplots(figsize=(6, 5))
    if plot_choice == "Scatterplot":
        q1 = listbox.get(selected_indices[0])
        q2 = listbox.get(selected_indices[1])
        subset = df[[q1, q2]].dropna()
        corr_value = subset[q1].corr(subset[q2])
        sns.regplot(data=subset, x=q1, y=q2, ax=ax, ci=None)
        ax.set_title(f"{q1} vs {q2}\nCorrelation = {corr_value:.3f}")
        ax.set_xlabel(q1)
        ax.set_ylabel(q2)
    elif plot_choice == "Boxplot":
        q1 = listbox.get(selected_indices[0])
        q2 = listbox.get(selected_indices[1])
        subset = df[[q1, q2]].dropna()
        sns.boxplot(data=subset, ax=ax)
        ax.set_title(f"Boxplot for {q1} and {q2}")
    elif plot_choice == "Heatmap":
        
        corr_matrix = df.corr()
        sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        ax.set_title("Correlation Matrix for All Questions")
    # Embed plot in Tkinter
    canvas_widget = FigureCanvasTkAgg(fig, master=root)
    canvas_widget.draw()
    canvas_widget.get_tk_widget().pack(pady=10)
# GUI Layout 

tk.Label(root, text="Question 6 is about body weight choose that to compare to the other questions").pack()
tk.Label(root, text="Select ANY TWO questions to compare:").pack()
listbox = tk.Listbox(root, selectmode="multiple", width=50)
for col in df.columns:
    listbox.insert(tk.END, col)
listbox.pack()
# Dropdown for plot
plot_type_var = tk.StringVar(value="Scatterplot")
tk.OptionMenu(root, plot_type_var, *plot_types).pack(pady=5)
# Button to create plot
tk.Button(root, text="Generate Plot", command=generate_plot).pack(pady=5)
# Text box for correlation info
text_box = tk.Text(root, height=6, width=60)
text_box.pack()
root.mainloop()