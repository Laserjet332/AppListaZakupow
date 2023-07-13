import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

import obsluga_plikow as fp

tab_list = []

def add_list(notebook, list_entry):
    if str(list_entry) == list_entry:
        list_name = str(list_entry)
    else:
        list_name = list_entry.get("1.0", tk.END).strip()
        list_entry.delete("1.0", tk.END)
    if not list_name:
        list_name = "None"
    tab_list.append(list_name)

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
        if str(elem_entry) == elem_entry:
            elem_name = str(elem_entry)
        else:
            elem_name = elem_entry.get()
            elem_entry.delete(0, tk.END)
        if not elem_name:
            elem_name = "None"
        current_tab = notebook.select()
        frame = notebook.nametowidget(current_tab)
        listbox = frame.winfo_children()[0]
        listbox.insert(tk.END, elem_name)

        elem_name_var = tk.IntVar()
        tk.Checkbutton(listbox, text=elem_name, variable=elem_name_var, anchor="w").pack(side="top", fill="both")


def remove_elem(notebook):
    current_tab = notebook.select()
    frame = notebook.nametowidget(current_tab)
    listbox = frame.winfo_children()[0]
    index = listbox.curselection()
    if index:
        listbox.delete(index)


def search_list(notebook, list_entry):
    search_query = ""
    if type(list_entry) is not str:
        search_query = list_entry.get("1.0", tk.END).strip()
    else:
        search_query = list_entry
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

def save_list(notebook):
    if not notebook.select():
        return 0

    list_name = tab_list[notebook.index(notebook.select())]
    list_name += ":"
    listbox = notebook.nametowidget(notebook.select()).winfo_children()[0]
    products_list = listbox.get(0, tk.END)

    file = filedialog.asksaveasfile(defaultextension=".txt")
    file.write(list_name)
    file.write("\n")
    for el in products_list:
        file.write(el)
        file.write("\n")
    file.close()

def load_list(notebook):
    path = filedialog.askopenfilename()
    file = open(path,'r')
    list = file.read()
    name = ""
    product = ""
    for el in list:
        if el == ':':
            break
        name += el
    add_list(notebook,name)
    new_list = list[len(name)+2:]
    search_list(notebook,name)
    for el in new_list:
        if el == '\n':
            add_elem(notebook,product)
            product = ""
        product += el


def saving_lists_into(notebook, path):
    if not path:
        path = None
    fp.zapis_do_pliku(
        notebook.tab(notebook.select(), "text"),
        notebook.nametowidget(notebook.select()).winfo_children()[0].get(0, tk.END),
        path
    )

def read_list_from(notebook, path_name) -> None:
    if "\\" not in path_name and "/" not in path_name:
        new_list = fp.odczyt_z_pliku(path_name)
    else:
        if ".txt" not in path_name:
            path_name = path_name + ".txt"
        if '\\' in path_name:  # zmiana \ na / aby nie dzialala funkcja Path
            for x in path_name:
                if x == '\\':
                    x = '/'

        name_of_file = ""
        for x in list(reversed(range(0, len(path_name)))):
            if path_name[x] == '\\':
                name_of_file = path_name[x + 1:]
                path_name = path_name[:x]
                break
        new_list = fp.odczyt_z_pliku(name_of_file, path_name)
    if ".txt" in name_of_file:  # usuniecie .txt z nazwy listy
        name_of_file = name_of_file[:-4]
    add_list(notebook, name_of_file)
    notebook.select(notebook.tabs()[-1])  # ustawienie zapisu elementow na nowa ostania liste
    for x in new_list:  # dodawanie elementow do listy
        if "\n" in x:  # usuniecie '\n' z elementow listy
            x = x[:-1]
        add_elem(notebook, x)


def main():
    window = tk.Tk()
    logo = tk.PhotoImage(file='logo.png')
    window.geometry("750x550")
    window.minsize(width=750, height=550)
    window.maxsize(width=750, height=550)
    window.title("AppListaZakupow")
    window.iconphoto(True, logo)

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
    add_elem_button = tk.Button(window, text="Dodaj element do aktualnej listy",
                                command=lambda: add_elem(notebook, elem_entry))
    remove_elem_button.pack(side=tk.BOTTOM)
    add_elem_button.pack(side=tk.BOTTOM)
    elem_entry.pack(side=tk.BOTTOM)

    save_list_as_txt = tk.Button(window, text="Zapisz liste",
                                 command=lambda: save_list(notebook))
    read_list_from_txt = tk.Button(window, text="Odczytaj liste",
                                   command=lambda: load_list(notebook))
    read_list_from_txt.pack(side=tk.RIGHT)

    save_list_as_txt.pack(side=tk.LEFT)

    window.mainloop()


if __name__ == "__main__":
    main()



