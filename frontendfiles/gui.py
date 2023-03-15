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


def update_output_text():
    output_text.delete('1.0', tk.END)  # clear the text field
    output_text.insert(tk.END, "output")


# Add some widgets to the second tab
tk.Button(tab2, text="Update Text", command=update_output_text).pack()


output_text = tk.Text(tab2, height=10)
output_text.pack(fill='both', expand=True, padx=5, pady=5)
output_text.insert(tk.END, "HEllo my name is lol")

# Start the main loop
root.mainloop()
