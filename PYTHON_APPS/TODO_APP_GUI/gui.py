import PySimpleGUI as gui
from modules import functions

label = gui.Text("TODO")

input_box = gui.InputText(tooltip="Enter your Todo",key='todo')
list_box = gui.Listbox(values= functions.read_todos('todos.txt'),key='todos',enable_events=True,size=[45,10])

#Buttons
add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
complete_button = gui.Button('Done')
exit_button = gui.Button('Exit')



app_window = gui.Window('My Todo App',layout=[[label],[input_box,add_button],[list_box,edit_button ],[complete_button, exit_button]],font=('Helvetica', 20))


while True:
    event,values = app_window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            #app_window['todos'].update(values= [todo.strip() for todo in todos])
            app_window['todos'].update(values=todos)


        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo 
            functions.write_todos(todos)
            app_window['todos'].update(values=todos)

        case 'todos':
            app_window['todo'].update(value=values['todos'][0])
            
        case gui.WIN_CLOSED:
            break





app_window.close()


