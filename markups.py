from telegram import  KeyboardButton, ReplyKeyboardMarkup

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        for i in footer_buttons:
            menu.append([i])
    return menu


def get_details():
    button_list = [
        KeyboardButton("Get information")
    ]
    return ReplyKeyboardMarkup([button_list], resize_keyboard=True)
