import PySimpleGUI as sg

LENGTH_MEMORY = []
SEEN_INPUT = set()
OK_COUNTER = 0

AVG_LENGTH_TEXT = "Average DISTINCT input length so far from input text above is %d"
VIEW_IN_TAB1_TEXT = "This is content from tab2 %s"
OK_COUNTER_TEXT = "OK clicked %d times"


def handle_ok(window: sg.Window, values: dict) -> None:
    """

    :param window: pysimplegui window object
    :param values: dict of input key and value of the pysimplegui input value
    :return:
    """
    global OK_COUNTER  # need to define global variable if modified

    OK_COUNTER += 1
    window.Element("ok-click-counter").update(value=OK_COUNTER_TEXT % OK_COUNTER)

    if "view-in-tab1" in values:
        window.Element("updatable-from-tab2").update(value=VIEW_IN_TAB1_TEXT % values["view-in-tab1"])

    if "count-length" in values and (curr := values["count-length"]) not in SEEN_INPUT and curr != '':
        print(curr)
        SEEN_INPUT.add(curr)
        LENGTH_MEMORY.append(len(curr))
        print(LENGTH_MEMORY)
        window.Element("average-length").update(value=AVG_LENGTH_TEXT % (sum(LENGTH_MEMORY) / len(LENGTH_MEMORY)))


def main():
    sg.theme("LightBlue")  # Add a touch of color
    # All the stuff inside your window.

    tab1_layout = [
        [sg.Text('Some text on Row 1')],
        [sg.Text("We keep track of rounded average length of DISTINCT input here"), sg.InputText(key="count-length")],
        [sg.Text(AVG_LENGTH_TEXT % 0, key="average-length")],
        [sg.Text('This is content from tab2', key="updatable-from-tab2")],
    ]

    tab2_layout = [[sg.Text("Enter Here for view in tab1"), sg.InputText(key="view-in-tab1")]]
    tab3_layout = [[sg.Text("OK clicked 0 times", key="ok-click-counter")]]

    layout = [
        [
            sg.TabGroup(
                [[
                    sg.Tab("Tab1", tab1_layout),
                    sg.Tab("Tab2", tab2_layout),
                    sg.Tab("Tab3", tab3_layout)]]
            )
        ],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]
    ok_counter = 0
    # Create the Window
    window = sg.Window('Score Input Interface', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

        if event == "Ok":
            handle_ok(window, values)

    window.close()


if __name__ == "__main__":
    main()
