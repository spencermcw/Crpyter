import crpyter
import PySimpleGUI as sg

layout = [
    [
        sg.Column([
            [
                sg.Text('Password'),
                sg.Input('', enable_events=True, key='-PASSWORD-'),
            ],
            [
                sg.Text('Salt'),
                sg.Input('', enable_events=True, key='-SALT-'),
            ],
        ]),
    ],
    [
        sg.Column([
            [sg.Text('Input')],
            [sg.Multiline(size=(45, 25), key='-INPUT-')],
        ]),
        sg.Column([
            [sg.Button('ENCODE', key='-ENCODE-', size=(10,1))],
            [sg.Button('DECODE', key='-DECODE-', size=(10,1))],
            [sg.Button('< COPY', key='-COPY-OUTPUT-', size=(10,1))],
        ]),
        sg.Column([
            [sg.Text('Output')],
            [sg.Multiline(size=(45, 25), key='-OUTPUT-')],
        ]),
    ],
]

window = sg.Window('Crpyter', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break

    # print('Event:', event)
    # print('Values:', values)

    if event in ['-ENCODE-', '-DECODE-']:
        output = crpyter.execute(
            password=values['-PASSWORD-'],
            salt=values['-SALT-'],
            inText=values['-INPUT-'],
            op=({
                '-ENCODE-': crpyter.Operation.ENCODE,
                '-DECODE-': crpyter.Operation.DECODE
            }[event])
        )
        # print(output)
        window['-OUTPUT-'].update(output)

    elif event == '-COPY-OUTPUT-':
        window['-INPUT-'].update(values['-OUTPUT-'])


window.close()
