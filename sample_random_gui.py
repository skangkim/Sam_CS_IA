import PySimpleGUI as sg

# Global variables.
STRING_LIST = []  # A list of input strings.
TAB1_ROW1_INPUT_KEY = "tab1-string"
TAB1_ROW2_DISPLAY_KEY = "tab1-average-length"
TAB1_ROW3_DISPLAY_KEY = "tab1-string-from-tab2"
TAB2_ROW1_INPUT_KEY = "tab2-string"

# Prefix of the text in Tab1.
TAB1_ROW2_PREFIX = "Average length of strings so far: "
TAB1_ROW3_PREFIX = "Content from Tab 2: "


def update_tab1(window: sg.Window, values: dict) -> None:
    """
    :param window: pysimplegui window object
    :param values: dict of input key and value of the pysimplegui input value
    :return: None.

    Updates Tab1's texts in:
        - 2nd row (average length)
        - 3rd row (string from tab2)
    """

    # ----- Update 2nd row --------------
    input_string = values[TAB1_ROW1_INPUT_KEY]  # Get string from Tab 1
    # Only calculate if...
    # 1. the string is not empty (if it's empty, user did not provide one) AND
    # 2. the string has not been seen before.
    if input_string != "" and input_string not in STRING_LIST:
        STRING_LIST.append(input_string)

        # Let's calculate average length of the strings we've seen so far.
        length_sum = 0 # Compute the total length of all the strings.
        for s in STRING_LIST:
            length_sum += len(s)
        avg_length = length_sum / len(STRING_LIST)  # avg length = total length / number of strings

        # Update the displayed text
        updated_row2_text = TAB1_ROW2_PREFIX + str(avg_length)
        window.Element(TAB1_ROW2_DISPLAY_KEY).update(value=updated_row2_text)

    # ----- Update 3rd row --------------
    # Get the value from top row in Tab 2.
    # Update the bottom row in Tab 1 with the value.
    updated_row3_text = TAB1_ROW3_PREFIX + values[TAB2_ROW1_INPUT_KEY]
    window.Element(TAB1_ROW3_DISPLAY_KEY).update(value=updated_row3_text)


def create_layout() -> list:
    """
    :return: list.

    Create a layout for PySimpleGUI Window
    """
    # Set up layout for Tab 1
    tab1_layout = [
        [sg.Text(text="Input String: "), sg.InputText(key=TAB1_ROW1_INPUT_KEY)],  # Row 1
        [sg.Text(key=TAB1_ROW2_DISPLAY_KEY, text=TAB1_ROW2_PREFIX)],  # Row 2
        [sg.Text(key=TAB1_ROW3_DISPLAY_KEY, text=TAB1_ROW3_PREFIX)],  # Row 3
    ]
    # Set up layout for Tab 2
    tab2_layout = [[sg.Text(text="Enter here to view in Tab 1: "), sg.InputText(key=TAB2_ROW1_INPUT_KEY)]]  # Row 1
    # Set up layout of the program
    layout = [
        # Set up tabs
        [
            sg.TabGroup(
                [[
                    sg.Tab("Tab1", tab1_layout),
                    sg.Tab("Tab2", tab2_layout)]]
            )
        ],
        # Set up common buttons for all tabs
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    return layout


def run_program(window_layout: list) -> None:
    """
    :param window_layout: layout for PySmipleGui window.
    :return: None.

    Create a window and run GUI.
    """
    window = sg.Window('Score Input Interface', window_layout)  # Create a window

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

        if event == "Ok":  # When OK button is clicked:
            update_tab1(window, values)

    window.close()


# ---------- Setup --------
sg.theme("LightBlue")  # Add a touch of color
layout = create_layout()  # Create a layout
# ---------- Run --------
run_program(layout)
