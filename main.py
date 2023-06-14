import tkinter as tk
from tkinter import ttk


def add_list(notebook, list_entry):

    list_name = list_entry.get()
    if not list_name:
        list_name = "None"
    list_entry.delete(0, tk.END)
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=list_name)


def remove_list(notebook):

    if notebook.tabs():
        current_tab = notebook.select()
        notebook.forget(current_tab)

"""
def main():

    # main window
    window = tk.Tk()
    window.geometry("750x500")
    window.minsize(width=750, height=500)
    window.maxsize(width=750, height=500)
    window.title("AppListaZakupow")

    list_entry = tk.Entry(window, width=30)
    list_entry.pack()

    add_list_button = tk.Button(window, text="Dodaj listę", command=lambda: add_list(notebook, list_entry))
    add_list_button.pack()

    remove_list_button = tk.Button(window, text="Usuń listę", command=lambda: remove_list(notebook))
    remove_list_button.pack()

    notebook = ttk.Notebook(window)
    notebook.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
"""