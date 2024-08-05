while True:
    user_input = input("Do you need to add , show , edit , complete ,or exit the todo app : ")
    user_input = user_input.strip()

    if 'add' in user_input:

        todo = user_input[4:] 

        with open('todos.txt','r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todos.txt','w') as file:
            file.writelines(todos)
    
    elif 'show' in user_input:

        with open('todos.txt','r') as file:
            todos = file.readlines()
        
        for index, todo in enumerate(todos):
            todos = f"{index +1}-{todo}"
            print(todos)
            
    elif 'edit' in user_input:

        item_num = int(input("Enter number of which Todo should be Edited :"))
        item_num = item_num -1

        updated_todo = input('Enter the new todo : ')

        with open('todos.txt','r') as file:
            todos = file.readlines()
        
        todos[item_num] = updated_todo + '\n'

        with open('todos.txt','w') as file:
            file.writelines(todos)

    elif 'complete' in user_input:

        user_input = int(input("Enter a number of the todo , which to be marked as complete :"))
        user_input = user_input - 1 

        with open('todos.txt','r') as file :
            todos = file.readlines()

        todos.pop(user_input)

        with open('todos.txt','w') as file:
            file.writelines(todos)

    elif 'exit' in user_input:
        print("Have a Nice day ...!")
        break

    else:
        print('invalid input ...!')



        



     