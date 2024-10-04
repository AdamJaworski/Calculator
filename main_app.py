import tkinter
import customtkinter as ctk
import numpy as np

GREY = '#1c1c1c'
LIGHT_GREY = '#3b3b3b'
ORANGE = '#c25d0a'
APP_WIDTH = 300
APP_HEIGHT = 500
FONT = ('Roboto', 40)

SYMBOLS = {
    1: '+',
    2: '-',
    3: '*',
    4: '/',
    None: ''
}

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        display_height = int(APP_HEIGHT/5)
        button_height = int((APP_HEIGHT - display_height) / 4)
        button_width = int(APP_WIDTH/4)

        self.first_number = ''
        self.second_number = ''
        self.symbol = None

        center_x = int(self.winfo_screenwidth() / 2 - int(APP_WIDTH / 2))
        center_y = int(self.winfo_screenheight() / 2 - int(APP_HEIGHT / 2))

        self.geometry(f'{APP_WIDTH}x{APP_HEIGHT}+{center_x}+{center_y}')
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.display_var = tkinter.StringVar()

        self.display_label = ctk.CTkLabel(self, text='0', bg_color=GREY, height=display_height, font=FONT)
        self.display_label.grid(row=0, column=0, columnspan=4, sticky='we')

        for i in range(9):
            button = ctk.CTkButton(self, command=lambda x=i+1:self.input(x), font=FONT, corner_radius=0,
                                   fg_color=ORANGE, height=button_height, width=button_width, text=str(i + 1))

            button.grid(row=int(i / 3) + 1, column=i % 3, pady=(1,0))

        ctk.CTkButton(self, command=lambda x=1: self.set_symbol(x), font=FONT, corner_radius=0,
                      fg_color=LIGHT_GREY, height=button_height, width=button_width, text='+').grid(row=1, column=3, pady=(1,0))

        ctk.CTkButton(self, command=lambda x=2: self.set_symbol(x), font=FONT, corner_radius=0,
                      fg_color=LIGHT_GREY, height=button_height, width=button_width, text='-').grid(row=2, column=3, pady=(1,0))

        ctk.CTkButton(self, command=lambda x=3: self.set_symbol(x), font=FONT, corner_radius=0,
                      fg_color=LIGHT_GREY, height=button_height, width=button_width, text='*').grid(row=3, column=3, pady=(1,0))

        ctk.CTkButton(self, command=self.calc, font=FONT, corner_radius=0,
                      fg_color=LIGHT_GREY, height=button_height, width=button_width, text='=').grid(row=4, column=3, pady=(1,0))

        ctk.CTkButton(self, command=self.change_current_number_symbol, font=FONT, corner_radius=0,
                      fg_color=LIGHT_GREY, height=button_height, width=button_width, text='+/-').grid(row=4, column=0, pady=(1,0))

        ctk.CTkButton(self, command=lambda x=0:self.input(x), font=FONT, corner_radius=0,
                      fg_color=ORANGE, height=button_height, width=button_width, text='0').grid(row=4, column=1, pady=(1,0))

        ctk.CTkButton(self, command=lambda x=4: self.set_symbol(x), font=FONT, corner_radius=0,
                      fg_color=LIGHT_GREY, height=button_height, width=button_width, text='/').grid(row=4, column=2, pady=(1,0))

        self.mainloop()

    def update_display(self):
        self.display_var.set(f'{self.first_number}{SYMBOLS[self.symbol]}{self.second_number}')
        self.display_label.configure(text=self.display_var.get())

    def input(self, input):
        if self.symbol is None:
            self.first_number += str(input)
        else:
            self.second_number += str(input)

        self.update_display()

    def set_symbol(self, symbol):
        if self.first_number == '':
            return
        if self.symbol is None:
            self.symbol = symbol
        self.update_display()

    def change_current_number_symbol(self):
        pass

    def calc(self):
        if self.second_number == '':
            self.second_number = self.first_number

        match self.symbol:
            case 1:
                result = np.add(float(self.first_number), float(self.second_number))
            case 2:
                result = np.subtract(float(self.first_number), float(self.second_number))
            case 3:
                result = np.multiply(float(self.first_number), float(self.second_number))
            case 4:
                result = np.divide(float(self.first_number), float(self.second_number))
            case _:
                return

        self.first_number = ''
        self.second_number = ''
        self.symbol = None
        self.display_label.configure(text=str(result))

if __name__ == "__main__":
    App()