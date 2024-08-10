import modules.functions as functions
import time 

print_time = time.strftime("%H:%M:%S %Y") 

print('Hi ' + print_time)

while True:
    user_input = input("Do you need to add , show , edit , complete ,or exit the todo app : ")
    user_input = user_input.strip()

    if user_input.startswith('add'):

        todo = user_input[4:] 

        old_todos = functions.read_todos("todos.txt")
         
        
        old_todo_bool = any(todo == old_todo for old_todo in old_todos)

        # Need to rework on this 
        if todo != "" and old_todo_bool == False :
            todos = functions.read_todos("todos.txt")
            todos.append(todo + '\n')
            functions.write_todos("todos.txt",todos)
        else:
            print("No Null entries and same entrie not allowed , if need to add secind time please spwecify")
            continue
    
    elif user_input.startswith('show'):

        todos = functions.read_todos("todos.txt")
        
        for index, todo in enumerate(todos):
            todos = f"{index +1}-{todo}"
            print(todos)
            
    elif user_input.startswith('edit'):
        
        try:

            item_num = int(input("Enter number of which Todo should be Edited :"))
            item_num = item_num -1

            updated_todo = input('Enter the new todo : ')

            todos = functions.read_todos("todos.txt")
            
            todos[item_num] = updated_todo + '\n'

            functions.write_todos("todos.txt",todos)

        except ValueError:

            print('your command is not valid ')
            continue


    elif user_input.startswith('complete'):

        try:

            user_input = int(input("Enter a number of the todo , which to be marked as complete :"))
            user_input = user_input - 1 

            todos = functions.read_todos("todos.txt")

            todos.pop(user_input)

            functions.write_todos("todos.txt",todos)

        except IndexError:
            print("Enter a number less than number of total do's !")
            continue

    elif user_input.startswith('exit'):
        print("Have a Nice day ...!")
        break

    else:
        print('invalid input ...!')