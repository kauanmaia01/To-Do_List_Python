import os

def add_taks(new_taks):
  # Adiciona tarefas
  date = new_taks
  taks_list.append(date)
  return

def delete_taks(main_list, storage):
  # Excluí e adiciona os itens excluídos no rodo_taks
  del_taks = main_list.pop()
  storage.append(del_taks)
  print(f"A tarefa {del_taks} foi excluida com sucesso")
  print()
  return 

def rodo_taks(main_list, storage):
  # Guarda todas tarefas excluídos 
  rodo = storage.pop()
  main_list.append(rodo)
  print("Certo!")
  print()



taks_list = []
remake = []

while True:
  print("to-do list".title())
  print("""Comandos: 
  
      [a]dicionar 
      [m]ostrar 
      [e]xcluir 
      [r]efazer 
      [s]air
  """)
  option = input("Digite um comando: ").lower()
  print()

  if option == "a":
    taks = input("Digite uma tarefa: ")
    print()
    add_taks(taks)
    continue
    
  if option == "m":
    print("Suas tarefas: ")
    print()
    for dates in taks_list:
      print(f" > {dates}")
    print()
    continue
    
  elif option == "e":
    if taks_list == []:
      print("Não tem tarefas para excluir!")
      print()
      continue
    delete_taks(taks_list, remake)
    continue
    
  elif option == "r":
    if remake == []:
      print("Não tem tarefas para refazer!")
    else:
      rodo_taks(taks_list, remake)
    print()
    continue
    
  elif option == "clear":
    os.system("clear")
    
  else:
    print("Sistema encerrado")
    exit()