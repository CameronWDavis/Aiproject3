import math
import tkinter as tk
import random
from tkinter import ttk, filedialog, CENTER, BOTTOM, RIGHT
from tkinter.ttk import Scrollbar

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


def updateOne():
    import preferences as ck
    possibleobj_text.delete('1.0', tk.END)
    x = 1
    for i in ck.models:
        possibleobj_text.insert(tk.END, f"{x}-   ")
        possibleobj_text.insert(tk.END, i)
        possibleobj_text.insert(tk.END, '\n')
        x = x + 1


def showExemplificaiton():
    import preferences as dk
    penalty_text.delete('1.0', tk.END)
    possibilic_text.delete('1.0', tk.END)
    qualitative_text.delete('1.0', tk.END)
    exemplificaiton_text.delete('1.0', tk.END)
    tableDisplay(penalty_text, dk.t_normal, 2)

    tableDisplay(possibilic_text, dk.k_normal, 2)

    # tableDisplayQualitative(qualitative_text, dk.n)
    tableDisplay(qualitative_text, dk.n, 1)

    displayExemplification(dk.models, dk.t, dk.k, dk.n)
    # exemplificaiton_text.insert(tk.END, "This is the exemptButton")


def displayExemplification(models, t, k, n):
    # exemplification tow random feasible object
    s = random.sample(models, 2)
    #
    print(models.index(s[0]), models.index(s[0]) + 1)
    print(models.index(s[1]), models.index(s[1]) + 1)
    # print(s)
    print()
    for z in t:
        for f in t:
            if z["model"] == s[0] and f['model'] == s[1]:
                if z["Total"] < f["Total"]:
                    exemplificaiton_text.insert(tk.END,
                                                f"Object {models.index(s[0]) + 1} is preferred to Object  {models.index(s[1]) + 1} according to penalty Logic.\n")
                    # print(f"{s[0]} is preferred to {s[1]} according to penalty Logic.")
                elif z["Total"] > f["Total"]:
                    exemplificaiton_text.insert(tk.END,
                                                f"Object {models.index(s[1]) + 1} is preferred to Object {models.index(s[0]) + 1} according to penalty Logic.\n")
                    # print(f"{s[1]} is preferred to {s[0]} according to penalty Logic.")
                else:
                    exemplificaiton_text.insert(tk.END,
                                                f"Object {models.index(s[0]) + 1} is equally preferred to Object {models.index(s[1]) + 1} according to penalty Logic.\n")
                    # print(f"{s[0]} is equally preferred to {s[1]} according to penalty Logic.", z["Total"], f["Total"])

    print()

    for z in k:
        for f in k:
            if z["model"] == s[0] and f['model'] == s[1]:
                if z["Total"] > f["Total"]:
                    exemplificaiton_text.insert(tk.END,
                                                f"Object {models.index(s[0]) + 1} is preferred to Object {models.index(s[1]) + 1} according to possibilistic Logic.\n")
                    # print(f"{s[0]} is preferred to {s[1]} according to possibilistic Logic.")
                elif z["Total"] < f["Total"]:
                    exemplificaiton_text.insert(tk.END,
                                                f"Object {models.index(s[1]) + 1} is preferred to Object {models.index(s[0]) + 1} according to possibilistic Logic.\n")
                    # print(f"{s[1]} is preferred to {s[0]} according to possibilistic Logic.")
                else:
                    exemplificaiton_text.insert(tk.END,
                                                f"Object {models.index(s[0]) + 1} is equally preferred to Object {models.index(s[1]) + 1} according to possibilistic Logic.\n")
                    # print(f"{s[0]} is equally preferred to {s[1]} according to possibilistic Logic.")

    print()

    val1, val2 = 0, 0
    for z in n:
        for f in n:
            if z["model"] == s[0] and f['model'] == s[1]:
                for key1, key2 in zip(z, f):
                    # Skip the 'model' key since we already printed its value
                    if key1 == 'model' or key2 == 'model':
                        continue
                    if z[key1] == math.inf and f[key2] == math.inf:
                        continue
                    if z[key1] != math.inf and f[key2] == math.inf:
                        val1 += 1
                    if z[key1] == math.inf and f[key2] != math.inf:
                        val2 += 1
                    if z[key1] < f[key2]:
                        val1 += 1
                    if z[key1] > f[key2]:
                        val2 += 1

    if val1 < val2:
        exemplificaiton_text.insert(tk.END,
                                    f"Object {models.index(s[1]) + 1} is preferred to Object {models.index(s[0]) + 1} according to qualitative Logic.\n")
        # print(f"{s[1]} is preferred to {s[0]} according to qualitative Logic.")
    elif val1 > val2:
        exemplificaiton_text.insert(tk.END,
                                    f"Object {models.index(s[0]) + 1} is preferred to Object {models.index(s[1]) + 1} according to qualitative Logic.\n")
        # print(f"{s[0]} is preferred to {s[1]} according to qualitative Logic.")
    elif val1 == val2:
        exemplificaiton_text.insert(tk.END,
                                    f"Object {models.index(s[0]) + 1} is equally preferred to Object {models.index(s[1]) + 1} according to qualitative Logic.\n")
        # print(f"{s[0]} is equally preferred to {s[1]} according to qualitative Logic.", val1, val2)
    else:
        exemplificaiton_text.insert(tk.END,
                                    f"Object {models.index(s[0]) + 1} and Object {models.index(s[1]) + 1} are incomparable according to qualitative Logic.\n")
        # print(f"{s[0]} and {s[1]} are incomparable according to qualitative Logic.")


def tableDisplay(penalty_text, t, valu4):
    game_scroll_y = tk.Scrollbar(penalty_text)
    game_scroll_y.grid(row=0, column=1, sticky='ns')

    game_scroll_x = tk.Scrollbar(penalty_text, orient='horizontal')
    game_scroll_x.grid(row=1, column=0, sticky='ew')

    my_game = ttk.Treeview(penalty_text, yscrollcommand=game_scroll_y.set, xscrollcommand=game_scroll_x.set, height=7)

    my_game.grid(row=0, column=0, sticky='nsew')

    game_scroll_y.config(command=my_game.yview)
    game_scroll_x.config(command=my_game.xview)

    print('length', len(t[0]))

    h = len(t[0]) - valu4

    # my_game['columns'] = ("model", "modelPref1", "modelPref2", "modelPref3", "modelPref4", "modelPref5",
    #                       "modelPref6", "modelPref7", "modelPref8", "modelPref9", "total")

    # model_cols = tuple(f"modelPref{x}" for x in range(h))
    # my_game_cols = ("model",) + model_cols + ("total",)
    # my_game['columns'] = my_game_cols
    if valu4 == 2:
        my_game['columns'] = ("model", *[f"modelPref{x}" for x in range(1, h + 1)], "total")
    else:
        my_game['columns'] = ("model", *[f"modelPref{x}" for x in range(1, h + 1)])

    print(my_game)
    # my_game['columns'] = ("model", f"{modelPref + str(x) if x in range(h)}", "total")

    # my_game.column("#0", width=0)
    # my_game.column("model", anchor=tk.CENTER, width=80)
    # my_game.column("modelPref1", anchor=tk.CENTER, width=80)
    # my_game.column("modelPref2", anchor=tk.CENTER, width=80)
    # my_game.column("modelPref3", anchor=tk.CENTER, width=80)
    # my_game.column("modelPref4", anchor=tk.CENTER, width=80)
    # my_game.column("modelPref5", anchor=tk.CENTER, width=80)
    # my_game.column("modelPref6", anchor=tk.CENTER, width=80)
    # my_game.column("modelPref7", anchor=tk.CENTER, width=80)
    # my_game.column("modelPref8", anchor=tk.CENTER, width=80)
    # my_game.column("modelPref9", anchor=tk.CENTER, width=80)
    # my_game.column("total", anchor=tk.CENTER, width=100)
    #
    # my_game.heading("#0", text="", anchor=tk.CENTER)
    # my_game.heading("model", text="Obj", anchor=tk.CENTER)
    # my_game.heading("modelPref1", text="Pref1", anchor=tk.CENTER)
    # my_game.heading("modelPref2", text="Pref2", anchor=tk.CENTER)
    # my_game.heading("modelPref3", text="Pref3", anchor=tk.CENTER)
    # my_game.heading("modelPref4", text="Pref4", anchor=tk.CENTER)
    # my_game.heading("modelPref5", text="Pref5", anchor=tk.CENTER)
    # my_game.heading("modelPref6", text="Pref6", anchor=tk.CENTER)
    # my_game.heading("modelPref7", text="Pref7", anchor=tk.CENTER)
    # my_game.heading("modelPref8", text="Pref8", anchor=tk.CENTER)
    # my_game.heading("modelPref9", text="Pref9", anchor=tk.CENTER)
    # my_game.heading("total", text="Total", anchor=tk.CENTER)
    # x = 1
    #
    # for i in t:
    #     values_list = []
    #     for v in i.values():
    #         values_list.append(v)
    #     values_list.pop(0)
    #
    #     my_game.insert(parent='', index='end', iid=str(x), text='',
    #                    values=(x, *values_list))
    #     x = x + 1

    # my_game.insert(parent='', index='end', iid=0, text='',
    #                values=('1', 'Ninja', '101', 'Oklahoma', 'Moore', 'Moore', 'Moore', 'Moore', 'Moore', 20))

    my_game.column("#0", width=0)
    my_game.column("model", anchor=tk.CENTER, width=80)
    for i in range(1, h + 1):
        my_game.column(f"modelPref{i}", anchor=tk.CENTER, width=80)
    if valu4 == 2:
        my_game.column("total", anchor=tk.CENTER, width=100)

    my_game.heading("#0", text="", anchor=tk.CENTER)
    my_game.heading("model", text="Obj", anchor=tk.CENTER)
    for i in range(1, h + 1):
        my_game.heading(f"modelPref{i}", text=f"Pref{i}", anchor=tk.CENTER)
    if valu4 == 2:
        my_game.heading("total", text="Total", anchor=tk.CENTER)

    # for f in t:
    #     my_game.insert(parent="", index="end", text="", values=(f["model"], *[f[x] for x in range( h + 2)]))

    x = 1
    for i in t:
        values_list = []
        for v in i.values():
            values_list.append(v)
        values_list.pop(0)

        my_game.insert(parent='', index='end', iid=str(x), text='',
                       values=(x, *values_list))
        x = x + 1


# def tableDisplayQualitative(penalty_text, t):
#     game_scroll_y = tk.Scrollbar(penalty_text)
#     game_scroll_y.grid(row=0, column=1, sticky='ns')
#
#     game_scroll_x = tk.Scrollbar(penalty_text, orient='horizontal')
#     game_scroll_x.grid(row=1, column=0, sticky='ew')
#
#     my_game = ttk.Treeview(penalty_text, yscrollcommand=game_scroll_y.set, xscrollcommand=game_scroll_x.set, height=7)
#
#     my_game.grid(row=0, column=0, sticky='nsew')
#
#     game_scroll_y.config(command=my_game.yview)
#     game_scroll_x.config(command=my_game.xview)
#
#     my_game['columns'] = ("model", "modelPref1", "modelPref2", "modelPref3", "modelPref4",)
#
#     my_game.column("#0", width=0)
#     my_game.column("model", anchor=tk.CENTER, width=80)
#     my_game.column("modelPref1", anchor=tk.CENTER, width=80)
#     my_game.column("modelPref2", anchor=tk.CENTER, width=80)
#     my_game.column("modelPref3", anchor=tk.CENTER, width=80)
#     my_game.column("modelPref4", anchor=tk.CENTER, width=80)
#
#     my_game.heading("#0", text="", anchor=tk.CENTER)
#     my_game.heading("model", text="Obj", anchor=tk.CENTER)
#     my_game.heading("modelPref1", text="Pref1", anchor=tk.CENTER)
#     my_game.heading("modelPref2", text="Pref2", anchor=tk.CENTER)
#     my_game.heading("modelPref3", text="Pref3", anchor=tk.CENTER)
#     my_game.heading("modelPref4", text="Pref4", anchor=tk.CENTER)
#
#     x = 1
#
#     for i in t:
#         values_list = []
#         for v in i.values():
#             values_list.append(v)
#         values_list.pop(0)
#
#         my_game.insert(parent='', index='end', iid=str(x), text='',
#                        values=(x, *values_list))
#         x = x + 1
#
#     # my_game.insert(parent='', index='end', iid=0, text='',
#     #                values=('1', 'Ninja', '101', 'Oklahoma', 'Moore', 'Moore', 'Moore', 'Moore', 'Moore', 20))


def showOptimization():
    import preferences as dk

    Optimalpenalty_text.delete('1.0', tk.END)
    optimal_possibilic_text.delete('1.0', tk.END)
    optimal_qualitative_text.delete('1.0', tk.END)

    Optimalpenalty_text.insert(tk.END, f"{dk.t[0]['model']}")

    optimal_possibilic_text.insert(tk.END, f"{dk.k[0]['model']}")

    optimal_qualitative_text.insert(tk.END, f"{dk.best_set_optimal[0]}")


def show_omni_optimizaiton():
    import preferences as dk
    Optimalpenalty_text.delete('1.0', tk.END)
    optimal_possibilic_text.delete('1.0', tk.END)
    optimal_qualitative_text.delete('1.0', tk.END)

    optimalPen = dk.t[0]['Total']
    print(optimalPen)

    for z in dk.t:

        # for f in z:
        print(z)
        print(type(z))
        if int(z['Total']) == int(optimalPen):
            Optimalpenalty_text.insert(tk.END, f" {z['model']}\n")
            print(z['model'])

    optimalPoss = dk.k[0]['Total']

    for z in dk.k:
        # for f in z:
        if int(z['Total']) == int(optimalPoss):
            optimal_possibilic_text.insert(tk.END, f"{z['model']}\n")
            # print(z['model'])

    # optimal_possibilic_text.insert(tk.END, "This is the omni-ptimization")

    for z in dk.best_set_optimal:
        optimal_qualitative_text.insert(tk.END, f"{z}\n")
        print("here, z")



# Create the main window and set its size
root = tk.Tk()
root.title("Preference APP")
root.geometry("1650x985")

# Create a notebook widget to hold the tabs
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Create the first tab and add it to the notebook
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Input")
# create a new frame for the buttons
buttonFrame = tk.Frame(root)

# add the buttons to the frame with the grid geometry manager
exempButton = tk.Button(buttonFrame, text='Exemplification', bd=5, command=showExemplificaiton)
exempButton.grid(row=0, column=1, pady=15, padx=15)

existenceButton = tk.Button(buttonFrame, text='Existence', bd=5, command=updateOne)
existenceButton.grid(row=0, column=0, padx=15, pady=15)

optimizationButton = tk.Button(buttonFrame, text='Optimization', bd=5, command=showOptimization)
optimizationButton.grid(row=0, column=2, padx=15, pady=15)

omniOptimizationButton = tk.Button(buttonFrame, text='Omni-Optimization', bd=5, command=show_omni_optimizaiton)
omniOptimizationButton.grid(row=0, column=3, padx=15, pady=5)

# add the frame to the root window with the pack geometry manager
buttonFrame.pack()

# Set the column widths
tab1.columnconfigure(0, weight=1, minsize=50)
tab1.columnconfigure(1, weight=1, minsize=150)
tab1.columnconfigure(2, weight=1, minsize=150)
tab1.columnconfigure(3, weight=1, minsize=150)

# Create the first file browse button and output field
file_label1 = tk.Label(tab1, text="Attributes")
file_label1.grid(row=1, column=1, pady=10)
browse_button1 = tk.Button(tab1, text="Browse", command=lambda: browse_file(output_text1, 'file1'))
browse_button1.grid(row=2, column=1, pady=10)
output_text1 = tk.Text(tab1, height=10, width=50, state='disabled')
output_text1.grid(row=3, column=1, pady=10)

# Create the second file browse button and output field
file_label2 = tk.Label(tab1, text="Constraints")
file_label2.grid(row=1, column=2, pady=10)
browse_button2 = tk.Button(tab1, text="Browse", command=lambda: browse_file(output_text2, 'file2'))
browse_button2.grid(row=2, column=2, pady=10)
output_text2 = tk.Text(tab1, height=10, width=50, state='disabled')
output_text2.grid(row=3, column=2, pady=10)

# Create the third file browse button and output field
file_label3 = tk.Label(tab1, text="Penalty logic")
file_label3.grid(row=1, column=3, pady=10)
browse_button3 = tk.Button(tab1, text="Browse", command=lambda: browse_file(output_text3, 'file3'))
browse_button3.grid(row=2, column=3, pady=10)
output_text3 = tk.Text(tab1, height=10, width=50, state='disabled')
output_text3.grid(row=3, column=3, pady=10)

# Create the fourth file browse button and output field
file_label4 = tk.Label(tab1, text="Possibility logic")
file_label4.grid(row=4, column=1, pady=10)
browse_button4 = tk.Button(tab1, text="Browse", command=lambda: browse_file(output_text4, 'file4'))
browse_button4.grid(row=5, column=1, pady=10)
output_text4 = tk.Text(tab1, height=10, width=50, state='disabled')
output_text4.grid(row=6, column=1, pady=10)

# Create the fifth file browse button and output field
file_label5 = tk.Label(tab1, text="Qualitative logic")
file_label5.grid(row=4, column=2, pady=10)
browse_button5 = tk.Button(tab1, text="Browse", command=lambda: browse_file(output_text5, 'file5'))
browse_button5.grid(row=5, column=2, pady=10)
output_text5 = tk.Text(tab1, height=10, width=50, state='disabled')
output_text5.grid(row=6, column=2, pady=10)

# Create the second tab and add it to the notebook
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Output")

# this is a label and text box for the possible object
possibleobj_label = tk.Label(tab2, text="Possible Object").grid(row=1, column=1)
possibleobj_text = tk.Text(tab2, height=10, width=85)
possibleobj_text.grid(row=2, column=1, padx=15, pady=15)

# this is a label and text box for the penalty object
penalty_label = tk.Label(tab2, text="Penalty Object").grid(row=1, column=2)

penalty_text = tk.Text(tab2, height=10, width=85)
penalty_text.grid(row=2, column=2, padx=15, pady=15)

# this is a label and text box for the optimal object penalty
Optimalpenalty_label = tk.Label(tab2, text="Optimal Object Penalty").grid(row=3, column=1)

Optimalpenalty_text = tk.Text(tab2, height=10, width=85)
Optimalpenalty_text.grid(row=4, column=1, padx=15, pady=15)

# this is a label and text box for the possibilistic  logic
possibilic_label = tk.Label(tab2, text="Possibilistic  logic").grid(row=3, column=2)

possibilic_text = tk.Text(tab2, height=10, width=85)
possibilic_text.grid(row=4, column=2, padx=15, pady=15)

# this is a label and text box for the Optimal Object possibilistic  logic
optimal_possibilic_label = tk.Label(tab2, text="Optimal Object Possibilistic").grid(row=5, column=1)
optimal_possibilic_text = tk.Text(tab2, height=10, width=85)
optimal_possibilic_text.grid(row=6, column=1, pady=15, padx=15)

# this is a label and text box for the Qualitative logic
qualitative_label = tk.Label(tab2, text="Qualitative Logic").grid(row=5, column=2)
qualitative_text = tk.Text(tab2, height=10, width=85)
qualitative_text.grid(row=6, column=2, pady=15, padx=15)

# this is a label and text box for the Optimal Object Qualitative logic
optimal_qualitative_label = tk.Label(tab2, text="Optimal Object Qualitative").grid(row=7, column=1)
optimal_qualitative_text = tk.Text(tab2, height=10, width=85)
optimal_qualitative_text.grid(row=8, column=1, pady=15, padx=15)

# this is a label and text box for the exemplification
exemplification_label = tk.Label(tab2, text="Exemplification").grid(row=7, column=2)
exemplificaiton_text = tk.Text(tab2, height=10, width=100)
exemplificaiton_text.grid(row=8, column=2, pady=15, padx=15)

# Start the main loop
root.mainloop()
