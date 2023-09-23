import tkinter as tk
from tkinter import messagebox

#Styles
screen_size = "280x470"
bg_color = "#8BE0FF"
black_color = "#0D0D0D"
border_color = "#A4E8FF"


#Events

def add_element(event=None):
    # Adiciona tarefas
    if entry_state.get() != "":
        new_element = entry_state.get()
        listbox.insert(tk.END, new_element)
        entry_state.set("")
        return
    messagebox.showerror("Atenção", "Você não digitou nenhuma tarefa!")
        

def del_element():
    # Excluí e adiciona os itens excluídos no rodo_taks
    selected_index = listbox.curselection()
    if selected_index:
        removed_item = listbox.get(selected_index)
        listbox.delete(selected_index) 
        storage.append(removed_item)
        print(f"Item excluído: {removed_item}")
    else:
        messagebox.showinfo("Atenção", "Nenhum item selecionado.")

def reverse_element():
    # Guarda todas tarefas excluídos 
    if storage:
        last_item = storage.pop()
        listbox.insert(tk.END, last_item)
    else:
        print("A lista de tarefas excluídas está vazia.")


storage = [] # Armazena os itens excluídos

#Window
root = tk.Tk()
root.title("Lista de Tarefas")
root.geometry(screen_size)
root.resizable(width=False, height=False)
root.configure(background= bg_color)


container_hero = tk.Frame(root, background= bg_color, width=230, height=130)
container_hero.pack(fill="both", expand= False, padx= 10)

title_img_hero = tk.PhotoImage(file= "images/hero-img.png")

title_hero = tk.Label(container_hero,
    image=title_img_hero,
    background= bg_color    
).pack(pady= 10, anchor="w")

subtitle_img = tk.PhotoImage(file= "images/title_img.png")

subtitle_hero = tk.Label(container_hero,
    image=subtitle_img,
    background= bg_color    
).pack(pady= 5, anchor="w")

taks_title_img = tk.PhotoImage(file= "images/taks_title_img.png")

taks_img_hero = tk.Label(container_hero,
    image=taks_title_img,
    background= bg_color    
).pack(pady= 10, anchor="w")

entry_state = tk.StringVar()
taks_user_hero = tk.Entry(container_hero, 
    textvariable= entry_state, 
    width=230, 
    background= bg_color,
    font="Arial 10 bold"
)

taks_user_hero.pack(pady=5, ipady=5, anchor="center")
taks_user_hero.bind("<Return>", add_element) #Activate enter key


#===================================#


container_list = tk.Frame(root, background= bg_color, width=280, height=150)
container_list.pack(fill="both", expand= False, padx= 10)

listbox = tk.Listbox(container_list, width=210, height=15, background=bg_color, font="Arial 9 bold")
listbox.grid(row=0, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(container_list)
scrollbar.grid(row=0, column=1, sticky="ns")

container_list.grid_rowconfigure(0, weight=1)
container_list.grid_columnconfigure(0, weight=1)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
 

#===================================#


container_buttons = tk.Frame(root, background= bg_color, width=230, height=90)
container_buttons.pack(fill="both", expand=False, padx= 10)

add_button_img = tk.PhotoImage(file="images/button_add_img.png")

add_button = tk.Button(container_buttons,
    command=add_element,
    image=add_button_img,
    bg=bg_color,
    bd=0,
    highlightthickness=0,
    highlightcolor=bg_color,
    relief=tk.FLAT
)

del_button_img = tk.PhotoImage(file="images/delete_button_img.png")

delete_button = tk.Button(container_buttons,
    command=del_element,
    image=del_button_img,
    bg=bg_color,
    bd=0,
    highlightthickness=0,
    highlightcolor=bg_color,
    relief=tk.FLAT
)

reverse_button_img = tk.PhotoImage(file="images/Button_reverse.png")

reverse_button = tk.Button(container_buttons,
    command=reverse_element,
    image=reverse_button_img,
    bg=bg_color,
    bd=0,
    highlightthickness=0,
    highlightcolor=bg_color,
    relief=tk.FLAT
)

add_button.grid(row=0, column=0, pady=15)
delete_button.grid(row=0, column=1, pady=15, padx=10)
reverse_button.grid(row=0, column=2, pady=15)


root.mainloop()