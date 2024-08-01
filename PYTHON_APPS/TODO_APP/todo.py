# prompt message variable 
user_input = "Enter the todo ! "

#declaring the list to store all the todos 

todos = []

#implementing the while loop 
while True:
    todo = input(user_input)
    todos.append(todo)
    print(todos)
