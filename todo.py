# 
# Todo App
# 
# Masivi https://mape.gov.lv/catalog/materials/6501426F-B6EC-44B3-8B93-DC553DAE8886/view?preview=7A90D16F-0A8A-4840-A2E3-5EA4F6D4E194
# Arrays https://www.w3schools.com/python/python_arrays.asp
# 

def add(list, item):
  list.append(item)


def remove(list, index):
  list.pop(index)
  pass


def clear(list):
  list.clear()
  pass


def print_list(list):
  for i in range(len(list)):    
    print(i, " ", list[i])
  pass


list = []
print("List of guests is empty now, what you want to do?")
while True:
  choice = int(input("1. Add a guest\n2. Remove a guest\n3. Clear the list\n4. Print the list\n"))
  if choice == 1:
    item = input("What you want to add?\n")
    add(list, item)
    print_list(list)
  elif choice == 2:
    if not list:
      print("There is nothing to remove in the list\n")
    else:
      index = int(input("What you want to remove?\n"))
      remove(list, index)
      print_list(list)
  elif choice == 3:
    if not list:
      print("The list is already clear\n")
    else:
      clear(list)
      print_list(list)
  elif choice == 4:
    if not list:
      print("There is nothing in list\n")
    else:
      print_list(list)
  else:
    print("Invalid input")

