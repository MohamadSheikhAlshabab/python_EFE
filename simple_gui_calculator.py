import PySimpleGUI as gui

def simple_calculator():
    gui.theme('dark grey 9')
    gui.Print()
    print_gui = gui.Print

    layout = [  [gui.Text("Insert the first number :")],
                [gui.Input()],
                [gui.Text("Insert the second number :")],
                [gui.Input()],
                [gui.Text("Result :")],
                [gui.Input(key='_RESULT_')],
                [gui.Button('Add'),gui.Button('Subtract')] 
            ]

    window = gui.Window("Calculator",layout)

    try:
        while True:
            event , values = window.read()
            if event in (None,"Exit"):
                break

            if event == 'Add':
                sum = int(values[0]) + int(values[1])
                print("the first num: ",values[0],"the second num: ",values[1])
                print("the result of add = ",sum)
                window['_RESULT_'].Update(value=sum)
                print_gui("the first num: ",values[0],"the second num: ",values[1])
                print_gui("the result of add = ",sum)
                gui.Popup(f'''
the first num: {values[0]}
the second num: {values[1]}
the result of add = {sum}
                ''', keep_on_top=True)

            if event == 'Subtract':
                sub = int(values[0]) - int(values[1])
                print("the first num: ",values[0],"the second num: ",values[1])
                print("the result of subtract = ",sub)
                window['_RESULT_'].Update(value=sub)
                print_gui("the first num: ",values[0],"the second num: ",values[1])
                print_gui("the result of subtract = ",sub)
                gui.Popup(f'''
the first num: {values[0]}
the second num: {values[1]}
the result of subtract = {sub}
                ''', keep_on_top=True)

    except Exception as e:
        gui.popup_error_with_traceback(f'An error happened.  Here is the info:', e)


if __name__ == '__main__':
    simple_calculator()
