from getch import getch
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
import os

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
        if key == '\x1b' and getch() == '[':
            key = getch()
            if key == 'A':
                if self.current_option > 0:
                    self.current_option -= 1
                os.system(cls)
                self.print_menu(self.justify_menu)
                self.print_options(self.justify_options)

            elif key == 'B':
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