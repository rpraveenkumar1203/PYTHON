todos =[]

# intiating the loop 

while True:
    user_action = input("Enter add or show or exit")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo action : ")
            todo = todo.title()
            todos.append(todo)
        case 'show' | 'display':
            for items in todos:
                print(items)
        case 'exit':
            break                
        case _ :
            print('Enter show or add or display or exit the program')
print('Bye')


