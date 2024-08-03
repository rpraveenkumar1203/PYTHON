todos =[]

while True:
    user_input=input("Do you need a ADD show edit or exit : \n")

    match user_input:
        case 'add':
            todo = input('Enter a Todo : \n')
            todos.append(todo)
        case 'show':
            for todo in todos:
                print( todos.index(todo) +1 ,'.',todo)
        case 'edit':
            number = int(input("Enter a number of which todo to be edited "))
            number = number -1
            todo = input('enter a new todo : \n')
            todos[number] = todo
        case 'exit':
            break
        case _:
            print('you have entered a invalid parameter ,Please enter add remove edit or exit ')

print("bye")

