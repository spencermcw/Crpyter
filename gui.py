import crpyter
import PySimpleGUI as sg

layout = [
    [
        sg.Column([
            [sg.Text('Password', size=(8,1), justification='r')],
            [sg.Text('Salt', size=(8,1), justification='r')],
        ]),
        sg.Column([
            [sg.Input('', enable_events=True, key='-PASSWORD-', password_char='*', size=(50,1))],
            [sg.Input('', enable_events=True, key='-SALT-', password_char='*', size=(50,1))],
        ]),
    ],
    [
        sg.Column([
            [sg.Text('Input')],
            [sg.Multiline(size=(30, 15), key='-INPUT-')],
        ]),
        sg.Column([
            [sg.Button('ENCODE', key='-ENCODE-', size=(10,1))],
            [sg.Button('DECODE', key='-DECODE-', size=(10,1))],
            [sg.Button('< COPY', key='-COPY-OUTPUT-', size=(10,1))],
        ]),
        sg.Column([
            [sg.Text('Output')],
            [sg.Multiline(size=(30, 15), key='-OUTPUT-')],
        ]),
    ],
]

window = sg.Window('Crpyter', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break

    if event in ['-ENCODE-', '-DECODE-']:
        window['-OUTPUT-'].update('')
        output = crpyter.execute(
            password=values['-PASSWORD-'],
            salt=values['-SALT-'],
            inText=values['-INPUT-'],
            op=({
                '-ENCODE-': crpyter.Operation.ENCODE,
                '-DECODE-': crpyter.Operation.DECODE
            }[event])
        )
        window['-OUTPUT-'].update(output)

    elif event == '-COPY-OUTPUT-':
        window['-INPUT-'].update(values['-OUTPUT-'])


window.close()
