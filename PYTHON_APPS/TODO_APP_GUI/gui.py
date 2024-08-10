import PySimpleGUI as gui

label = gui.Text("TODO")
input_box = gui.InputText(tooltip="Enter your Todo")
add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
complete_button = gui.Button('Done')
exit_button = gui.Button('Exit')

app_window = gui.Window('My Todo App',layout=[[label],[input_box,add_button],[edit_button , complete_button, exit_button]])
app_window.read()
print('app loaded done')
app_window.close()
