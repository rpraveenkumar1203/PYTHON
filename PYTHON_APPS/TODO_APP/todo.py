while True:

    user_input=input("Do you need a ADD show edit done or exit : \n")
    user_input= user_input.strip()

    

    match user_input:

        case 'add':

            user_input = input("Enter the todo needed to added : \n") + "\n"

            with open('todos.txt','r') as file:
                todos = file.readlines()

            todos.append(user_input)
                
            with open('todos.txt','w') as file:
                todos = file.writelines(todos)
                
        case 'show':

            with open('todos.txt','r') as file:
                todos = file.readlines()
                
            for index,todo in enumerate(todos):
                print(f"{index + 1}-{todo}")


        case 'edit':

            number = int(input("Enter a number of which todo to be edited : \n "))
            number = number -1
            
            with open('todos.txt','r') as file:
                todos = file.readlines()
            
            new_todo = input('enter a new todo : \n')
            todos[number] = new_todo + "\n"

            with open ('todos.txt','w') as file:
                file.writelines(todos)


        case 'done':

            number = int(input("Enter a number of which todo to be mark as completed : "))
            with open('todos.txt','r') as file:
                todos = file.readlines()
            
            index = number-1

            print(f"{todos[index]} is marked as completed ")
            
            todos.pop(index)

            with open('todos.txt','w') as file:
                file.writelines(todos)         
                            

        case 'exit':

            break
        
        case _:

            print('you have entered a invalid parameter ,Please enter add remove edit or exit ')

print("bye")