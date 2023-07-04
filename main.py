import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def add_list(notebook, list_entry):
    list_name = list_entry.get("1.0", tk.END).strip()
    if not list_name:
        list_name = "None"
    list_entry.delete("1.0", tk.END)
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


def search_list(notebook, list_entry):
    search_query = list_entry.get("1.0", tk.END).strip()
    if notebook.tabs():
        found = False
        for tab in notebook.tabs():
            tab_name = notebook.tab(tab, option="text")
            if search_query.lower() in tab_name.lower():
                notebook.select(tab)
                found = True
                break

        if not found:
            messagebox.showinfo("Search Result", "No matching list found.")
    else:
        messagebox.showinfo("Search Result", "No lists available.")


def main():
    window = tk.Tk()
    window.geometry("750x500")
    window.minsize(width=750, height=500)
    window.maxsize(width=750, height=500)
    window.title("AppListaZakupow")

    entry_frame = tk.Frame(window)
    entry_frame.pack()

    list_entry = tk.Text(entry_frame, width=30, height=2)
    list_entry.pack(side=tk.BOTTOM)

    add_list_button = tk.Button(entry_frame, text="Dodaj listę", command=lambda: add_list(notebook, list_entry))
    add_list_button.pack(side=tk.RIGHT)

    remove_list_button = tk.Button(entry_frame, text="Usuń listę", command=lambda: remove_list(notebook))
    remove_list_button.pack(side=tk.LEFT)

    search_frame = tk.Frame(window)
    search_frame.pack()

    search_label = tk.Label(search_frame)
    search_label.pack(side=tk.LEFT)

    search_button = tk.Button(search_frame, text="Szukaj", command=lambda: search_list(notebook, list_entry))
    search_button.pack(side=tk.RIGHT)

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

