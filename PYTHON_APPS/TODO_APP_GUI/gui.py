# importing modules 
import PySimpleGUI as gui
import time
from modules import functions


# setting theme
gui.theme('black')

# adding Widgets 
label = gui.Text("TODO")
clock = gui.Text('',key='clock')

# elements list

input_box = gui.InputText(tooltip="Enter your Todo",key='todo')
list_box = gui.Listbox(values= functions.get_todos('todos.txt'),key='todos',enable_events=True,size=[45,10])

#Buttons
add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
complete_button = gui.Button('Done')
exit_button = gui.Button('Exit')


# creating windows 
app_window = gui.Window('My Todo App',layout=[[clock],[label],[input_box,add_button],[list_box,edit_button,complete_button ],[exit_button]],font=('Helvetica', 20))


# prgram 
while True:
    event,values = app_window.read(timeout=10)
    app_window['clock'].update(value= time.strftime('%b %D %Y %H:%M:%S'))
    # print(1,event)
    # print(2,values)
    # print(3,event,values)
    match event:

        
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            #app_window['todos'].update(values= [todo.strip() for todo in todos])
            todos = functions.get_todos()
            #todos=[todo.strip() for todo in todos]            
            app_window['todos'].update(values=todos)


        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                #todos=[todo.strip() for todo in todos]
                index = todos.index(todo_to_edit)
                todos[index] = new_todo 
                functions.write_todos(todos)
                todos = functions.get_todos()
                #todos=[todo.strip() for todo in todos]
                app_window['todos'].update(values=todos)
            except IndexError:
                gui.popup("Please select a todo to edit ")


        case "Done":
            try:                    
                todo_to_edit = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_edit)
                functions.write_todos(todos)
                app_window['todos'].update(values=todos)
                app_window['todo'].update(value='')
            except IndexError:
                gui.popup("Please select a todo to mark as completed ")


        case 'todos':
            
            app_window['todo'].update(value=values['todos'][0])

        case 'Exit':
            #gui.popup('thanks')
            gui.popup_auto_close('Thanks for using ',auto_close_duration=2)
            break
            
        case gui.WIN_CLOSED:
            break





app_window.close()


