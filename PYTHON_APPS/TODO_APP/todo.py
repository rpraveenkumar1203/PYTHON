def read_todos():
    with open('todos.txt','r') as file:
        todos = file.readlines()
        return todos

def write_todos(filepath,todos):
    with open(filepath,'w') as file:
        file.writelines(todos)


while True:
    user_input = input("Do you need to add , show , edit , complete ,or exit the todo app : ")
    user_input = user_input.strip()

    if user_input.startswith('add'):

        todo = user_input[4:] 

        if todo != "":
            todos = read_todos()
            todos.append(todo + '\n')
            write_todos("todos.txt",todos)
        else:
            print("No Null entries ")
            continue
    
    elif user_input.startswith('show'):

        todos = read_todos()
        
        for index, todo in enumerate(todos):
            todos = f"{index +1}-{todo}"
            print(todos)
            
    elif user_input.startswith('edit'):
        
        try:

            item_num = int(input("Enter number of which Todo should be Edited :"))
            item_num = item_num -1

            updated_todo = input('Enter the new todo : ')

            todos = read_todos()
            
            todos[item_num] = updated_todo + '\n'

            write_todos("todos.txt",todos)

        except ValueError:

            print('your command is not valid ')
            continue


    elif user_input.startswith('complete'):

        try:

            user_input = int(input("Enter a number of the todo , which to be marked as complete :"))
            user_input = user_input - 1 

            todos = read_todos()

            todos.pop(user_input)

            write_todos("todos.txt",todos)

        except IndexError:
            print("Enter a number less than number of total do's !")
            continue

    elif user_input.startswith('exit'):
        print("Have a Nice day ...!")
        break

    else:
        print('invalid input ...!')