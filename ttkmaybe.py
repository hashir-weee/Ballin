import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

root = tk.Tk()
root.title("Tkinter Widgets with ttkbootstrap")

# Create a ttkbootstrap style
style = Style("lumen")

# Label
label = ttk.Label(root, text="Label")
label.pack(padx=10, pady=10)

# Button
button = ttk.Button(root, text="Button")
button.pack(padx=10, pady=10)

# Entry
entry = ttk.Entry(root)
entry.pack(padx=10, pady=10)

# Checkbutton
checkbutton = ttk.Checkbutton(root, text="Checkbutton")
checkbutton.pack(padx=10, pady=10)

# Radiobutton
radiobutton = ttk.Radiobutton(root, text="Radiobutton")
radiobutton.pack(padx=10, pady=10)

# Combobox
combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.pack(padx=10, pady=10)

# Spinbox
spinbox = ttk.Spinbox(root, from_=0, to=10)
spinbox.pack(padx=10, pady=10)

# Progressbar
progressbar = ttk.Progressbar(root, mode="indeterminate")
progressbar.start()
progressbar.pack(padx=10, pady=10)

# Scale
scale = ttk.Scale(root, from_=0, to=10, orient="horizontal")
scale.pack(padx=10, pady=10)

# Notebook
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(padx=10, pady=10)

# Treeview
treeview = ttk.Treeview(root, columns=("Column 1", "Column 2"))
treeview.heading("#1", text="Column 1")
treeview.heading("#2", text="Column 2")
treeview.insert("", "end", text="Item 1", values=("Value 1", "Value 2"))
treeview.pack(padx=10, pady=10)

# Listbox
listbox = tk.Listbox(root)
listbox.insert("end", "Item 1")
listbox.insert("end", "Item 2")
listbox.pack(padx=10, pady=10)

# Text
text = tk.Text(root)
text.pack(padx=10, pady=10)

# Canvas
canvas = tk.Canvas(root, width=200, height=100, bg="white")
canvas.pack(padx=10, pady=10)

# Frame
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Separator
separator = ttk.Separator(root, orient="horizontal")
separator.pack(padx=10, pady=10)

# Progressbar (determinate)
progressbar_determinate = ttk.Progressbar(root, mode="determinate")
progressbar_determinate["value"] = 30
progressbar_determinate.pack(padx=10, pady=10)

# Scale (vertical)
scale_vertical = ttk.Scale(root, from_=0, to=10, orient="vertical")
scale_vertical.pack(padx=10, pady=10)

# Menubutton
menubutton = ttk.Menubutton(root, text="Menubutton")
menu = tk.Menu(menubutton)
menu.add_command(label="Option 1")
menu.add_command(label="Option 2")
menubutton["menu"] = menu
menubutton.pack(padx=10, pady=10)

# Panedwindow
panedwindow = ttk.Panedwindow(root, orient="horizontal")
pane1 = ttk.Frame(panedwindow)
pane2 = ttk.Frame(panedwindow)
panedwindow.add(pane1)
panedwindow.add(pane2)
panedwindow.pack(padx=10, pady=10)

# Frame with LabelFrame
label_frame = ttk.LabelFrame(root, text="Label Frame")
label_frame.pack(padx=10, pady=10)
label = ttk.Label(label_frame, text="Label inside LabelFrame")
label.pack()

# Set the ttk style for all widgets
style.configure("TButton", padding=(10, 10))

root.mainloop()
