while True:
    user_input=input("Do you need a ADD show edit done or exit : \n")
    user_input= user_input.strip()

    match user_input:
        case 'add':

            user_input = input("Enter the todo needed to added : \n") + "\n"

            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()

            todos.append(user_input)

            file = open('todos.txt','w')
            todos = file.writelines(todos)
            file.close()



        case 'show':

            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()

            for index,todo in enumerate(todos):
                print(f"{index + 1}-{todo}")

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