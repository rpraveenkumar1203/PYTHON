import PySimpleGUI as gui
from modules import functions

# Welcome note

welcome_label = gui.Text("ToDo-app")

# input box and list Box
input_box = gui.InputText(tooltip="Enter the To-Do",key='todo')
list_box = gui.Listbox(values=functions.get_todos(),key='todos'
                       ,enable_events=True, size=[45,20])

# decalring buttons 
add_button = gui.Button('add')
edit_button = gui.Button('edit')
done_button = gui.Button('done')
exit_button = gui.Button('exit')

# Creating the app_window 

app_window = gui.Window(title="Todo-APP",
                        layout=[[welcome_label],[input_box,add_button],[edit_button],[done_button],[exit_button]],font=('timesnewroman', 20))




while True:
    event,values = app_window.read()
    match event:
        case "add":
            stored_todo = functions.get_todos()
            todo_to_be_added = values['todo']            
            stored_todo.append(todo_to_be_added)
            functions.write_todos(stored_todo)
            #app_window['todos'].update(values=stored_todo)
            
        case "edit":
            todo_to_be_edited = values['todos'][0]
            edited_todo = values['todo']
            all_todos = functions.get_todos()
            index_of_edited_todo = all_todos.index(todo_to_be_edited)
            all_todos[index_of_edited_todo] = edited_todo
            functions.write_todos(all_todos)
            app_window['todos'].update(values=all_todos)

        case "todos":
            app_window['todo'].update(value=values['todos'][0])

        #case "done":
        #case "exit":
        case gui.WIN_CLOSED:
            break

app_window.close()