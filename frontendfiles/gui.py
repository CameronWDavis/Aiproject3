import tkinter as tk
from tkinter import ttk, filedialog

# Define a dictionary to store the file paths and their corresponding file fields
file_paths = {}


# Define a function to be called when a "Browse" button is clicked
def browse_file(output_field, file_field):
    file_path = filedialog.askopenfilename()
    if file_path:
        # Add the file path to the dictionary with the corresponding file field as the key
        file_paths[file_field] = file_path
        with open(file_path, 'r') as file:
            file_contents = file.read()
            output_field.config(state='normal')  # enable the output field
            output_field.delete('1.0', tk.END)  # clear the output field
            output_field.insert(tk.END, file_contents)
            output_field.config(state='disabled')  # disable the output field


# Create the main window and set its size
root = tk.Tk()
root.title("Preference APP")
root.geometry("600x400")

# Create a notebook widget to hold the tabs
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Create the first tab and add it to the notebook
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Input")

# Create the first file browse button and output field
file_label1 = tk.Label(tab1, text="Attributes")
file_label1.pack(side=tk.LEFT, padx=5)
browse_button1 = tk.Button(tab1, text="Browse", command=lambda: browse_file(output_text1, 'file1'))
browse_button1.pack(side=tk.LEFT, padx=5)
output_text1 = tk.Text(tab1, height=10, width=20, state='disabled')
output_text1.pack(side=tk.LEFT, fill='x', expand=True, padx=5, pady=5)

# Create the second file browse button and output field
file_label2 = tk.Label(tab1, text="Constrains")
file_label2.pack(side=tk.LEFT, padx=5)
browse_button2 = tk.Button(tab1, text="Browse", command=lambda: browse_file(output_text2, 'file2'))
browse_button2.pack(side=tk.LEFT, padx=5)
output_text2 = tk.Text(tab1, height=10, width=20, state='disabled')
output_text2.pack(side=tk.LEFT, fill='x', expand=True, padx=5, pady=5)

# Create the third file browse button and output field
file_label3 = tk.Label(tab1, text="Penalty logic")
file_label3.pack(side=tk.LEFT, padx=5)
browse_button3 = tk.Button(tab1, text="Browse", command=lambda: browse_file(output_text3, 'file3'))
browse_button3.pack(side=tk.LEFT, padx=5)
output_text3 = tk.Text(tab1, height=10, width=20, state='disabled')
output_text3.pack(side=tk.LEFT, fill='x', expand=True, padx=5, pady=5)

# Create the fourth file browse button and output field
file_label4 = tk.Label(tab1, text="Possibility logic")
file_label4.pack(side=tk.LEFT, padx=5, pady=5)
browse_button4 = tk.Button(tab1, text="Browse", command=lambda: browse_file(output_text4, 'file4'))
browse_button4.pack(side=tk.LEFT, padx=5, pady=5)
output_text4 = tk.Text(tab1, height=10, width=20, state='disabled')
output_text4.pack(side=tk.LEFT, fill='x', expand=True, padx=5, pady=5)

# Create the fifth file browse button and output field
file_label5 = tk.Label(tab1, text="Qualitative logic")
file_label5.pack(side=tk.LEFT, padx=5, pady=5)
browse_button5 = tk.Button(tab1, text="Browse", command=lambda: browse_file(output_text5, 'file5'))
browse_button5.pack(side=tk.LEFT, padx=5, pady=5)
output_text5 = tk.Text(tab1, height=10, width=20, state='disabled')
output_text5.pack(side=tk.LEFT, fill='x', expand=True, padx=5, pady=5)

# Create the second tab and add it to the notebook
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Output")







#this is a label and text box for the possible object
possibleobj_label = tk.Label(tab2,text="Possible Object").grid(row=1,column=1)
possibleobj_text = tk.Text(tab2, height=20, width=20)
possibleobj_text.grid(row=2,column=1, padx=15, pady=15)





#this is a label and text box for the penalty object
penalty_label = tk.Label(tab2,text="Penalty Object").grid(row=1,column=2)

penalty_text = tk.Text(tab2, height=20, width=20)
penalty_text.grid(row=2,column=2, padx=15, pady=15)





#this is a label and text box for the optimal object penalty
Optimalpenalty_label = tk.Label(tab2,text="Optimal Object Penalty").grid(row=1, column=3)

Optimalpenalty_text = tk.Text(tab2, height=20, width=20)
Optimalpenalty_text.grid(row=2,column=3,padx=15, pady=15)


#this is a label and text box for the possibilistic  logic
possibilic_label = tk.Label(tab2,text="Possibilistic  logic").grid(row=1,column=4)

possibilic_text = tk.Text(tab2, height=20, width=20)
possibilic_text.grid(row=2,column=4,padx=15,pady=15)



#this is a label and text box for the Optimal Object possibilistic  logic
optimal_possibilic_label = tk.Label(tab2,text="Optimal Object Possibilistic").grid(row=3,column=1)
optimal_possibilic_text = tk.Text(tab2, height=20, width=20)
optimal_possibilic_text.grid(row=4,column=1,pady=15,padx=15)


#this is a label and text box for the Qualitative logic
qualitative_label = tk.Label(tab2,text="Qualitative Logic").grid(row=3,column=2)
qualitative_text = tk.Text(tab2, height=20, width=20)
qualitative_text.grid(row=4,column=2,pady=15,padx=15)

#this is a label and text box for the Optimal Object Qualitative logic
optimal_qualitative_label = tk.Label(tab2,text="Optimal Object Qualitative").grid(row=3,column=3)
optimal_qualitative_text = tk.Text(tab2, height=20, width=20)
optimal_qualitative_text.grid(row=4,column=3,pady=15,padx=15)


#this is a label and text box for the exemplification
exemplification_label = tk.Label(tab2,text="Exemplification").grid(row=3,column=4)
exemplificaiton_text = tk.Text(tab2, height=20, width=20)
exemplificaiton_text.grid(row=4,column=4,pady=15,padx=15)


def updateOne():
    possibleobj_text.delete('1.0', tk.END)
    possibleobj_text.insert(tk.END, "This is connected to the existence text box ")


def showExemplificaiton():
    penalty_text.delete('1.0', tk.END)
    possibilic_text.delete('1.0', tk.END)
    qualitative_text.delete('1.0', tk.END)
    exemplificaiton_text.delete('1.0', tk.END)
    penalty_text.insert(tk.END, "This is the exemptButton")
    possibilic_text.insert(tk.END, "This is the exemptButton")
    qualitative_text.insert(tk.END, "This is the exemptButton")
    exemplificaiton_text.insert(tk.END, "This is the exemptButton")

def showOptimization():
    Optimalpenalty_text.delete('1.0', tk.END)
    optimal_possibilic_text.delete('1.0', tk.END)
    optimal_qualitative_text.delete('1.0', tk.END)
    Optimalpenalty_text.insert(tk.END, "This is the optimization")
    optimal_possibilic_text.insert(tk.END, "This is the optimization")
    optimal_qualitative_text.insert(tk.END, "This is the optimization")

def show_omni_optimizaiton():
    Optimalpenalty_text.delete('1.0', tk.END)
    optimal_possibilic_text.delete('1.0', tk.END)
    optimal_qualitative_text.delete('1.0', tk.END)
    Optimalpenalty_text.insert(tk.END, "This is the omni-optimization")
    optimal_possibilic_text.insert(tk.END, "This is the omni-ptimization")
    optimal_qualitative_text.insert(tk.END, "This is the omni-optimization")

#this is the button and label for the exemplification output
exempButton = tk.Button(tab2, text= 'Exemplification', bd = 5,command=showExemplificaiton).grid(row=5,column=2,pady=15,padx=15)


#this is the existance button
existenceButton = tk.Button(tab2, text= 'Existance', bd = 5,command=updateOne).grid(row=5,column=1,padx=15,pady=15)

#this is the optimization button
optimizationButton = tk.Button(tab2, text= 'Optimization', bd = 5,command=showOptimization).grid(row=5,column=3,padx=15,pady=15)

#this is the Omni-Optimization
omniOptimizationButton = tk.Button(tab2, text= 'Omni-Optimizaiton', bd = 5,command=show_omni_optimizaiton).grid(row=5,column=4,padx=15,pady=5)





# Start the main loop
root.mainloop()
