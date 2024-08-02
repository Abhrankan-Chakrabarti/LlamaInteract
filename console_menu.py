from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
import os
if os.name == 'nt':
    from msvcrt import getch
else:
    from getch import getch

cls = 'cls' if os.name == 'nt' else 'clear'


class Menu:
    def __init__(self, text, options, console):
        self.text = text
        self.options = options
        self.current_option = 0
        self.console = console

    def print_menu(self, justify="center"):
        self.justify_menu = justify
        self.console.print(Panel(self.text, width=64), justify=justify)

    def print_options(self, justify="center"):
        self.justify_options = justify
        current_option_key = list(self.options.keys())[self.current_option]
        options_text = ""
        for option in self.options:
            if option == current_option_key:
                options_text += "> " + self.options[option] + " <\n"
            else:
                options_text += self.options[option] + "\n"
        options_text = options_text.rstrip("\n")

        self.console.print(
            Panel(Text(options_text, justify=justify), box=box.SIMPLE, width=64),
            justify=justify,
        )

    def on_press(self, key):
        if os.name == 'nt':
            arrow_key_pressed = key == b'\xe0'
            up_key = b'H'
            down_key = b'P'

        else:
            arrow_key_pressed = key == '\x1b' and getch() == '['
            up_key = 'A'
            down_key = 'B'

        if arrow_key_pressed:
            key = getch()
            if key == up_key:
                if self.current_option > 0:
                    self.current_option -= 1
                os.system(cls)
                self.print_menu(self.justify_menu)
                self.print_options(self.justify_options)

            elif key == down_key:
                if self.current_option < len(self.options) - 1:
                    self.current_option += 1
                os.system(cls)
                self.print_menu(self.justify_menu)
                self.print_options(self.justify_options)

        elif key == '\n':
            os.system(cls)
            return False

        else:
            os.system(cls)
            self.print_menu(self.justify_menu)
            self.print_options(self.justify_options)

    def choice(self, listener=''):
        while listener != '\n':
            listener = getch()
            self.on_press(listener)

        return list(self.options.keys())[self.current_option]