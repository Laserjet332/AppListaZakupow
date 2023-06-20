import tkinter as tk
from tkinter import ttk


def add_list(notebook, list_entry):

    list_name = list_entry.get()
    if not list_name:
        list_name = "None"
    list_entry.delete(0, tk.END)
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=list_name)
    listbox = tk.Listbox(frame, width=75, height=20)
    listbox.pack()


def remove_list(notebook):

    if notebook.tabs():
        current_tab = notebook.select()
        notebook.forget(current_tab)


def add_elem(notebook, elem_entry):

    if notebook.tabs():
        elem_name = elem_entry.get()
        if not elem_name:
            elem_name = "None"
        elem_entry.delete(0, tk.END)
        current_tab = notebook.select()
        frame = notebook.nametowidget(current_tab)
        listbox = frame.winfo_children()[0]
        listbox.insert(tk.END, elem_name)


def remove_elem(notebook):

    current_tab = notebook.select()
    frame = notebook.nametowidget(current_tab)
    listbox = frame.winfo_children()[0]
    index = listbox.curselection()
    if index:
        listbox.delete(index)


"""
def main():

    window = tk.Tk()
    window.geometry("750x500")
    window.minsize(width=750, height=500)
    window.maxsize(width=750, height=500)
    window.title("AppListaZakupow")

    list_entry = tk.Entry(window, width=30)
    add_list_button = tk.Button(window, text="Dodaj listę", command=lambda: add_list(notebook, list_entry))
    remove_list_button = tk.Button(window, text="Usuń listę", command=lambda: remove_list(notebook))
    list_entry.pack()
    add_list_button.pack()
    remove_list_button.pack()

    notebook = ttk.Notebook(window)
    notebook.pack()

    elem_entry = tk.Entry(window, width=30)
    remove_elem_button = tk.Button(window, text="Usuń element z aktualnej listy", command=lambda: remove_elem(notebook))
    add_elem_button = tk.Button(window, text="Dodaj element do aktualnej listy", command=lambda: add_elem(notebook, elem_entry))
    remove_elem_button.pack(side=tk.BOTTOM)
    add_elem_button.pack(side=tk.BOTTOM)
    elem_entry.pack(side=tk.BOTTOM)

    window.mainloop()


if __name__ == "__main__":
    main()
"""
