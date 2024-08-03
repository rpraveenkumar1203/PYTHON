todos =[]

while True:
    user_input=input("Do you need a ADD show edit or exit : \n")
    user_input= user_input.strip()

    match user_input:
        case 'add':
            todo = input('Enter a Todo : \n')
            todos.append(todo)
        case 'show':
            for index,todo in enumerate(todos):
                user_output = f"{index +1}-{todo}"
                print(user_output)
        case 'edit':
            number = int(input("Enter a number of which todo to be edited : \n "))
            number = number -1
            todo = input('enter a new todo : \n')
            todos[number] = todo
        case 'done':
            number = int(input("Enter a number of which todo to be mark as completed : \n"))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print('you have entered a invalid parameter ,Please enter add remove edit or exit ')

print("bye")