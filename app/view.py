from tkinter import Tk, Frame, Entry, Button, PhotoImage


class View(Tk):

    def __init__(self):
        super().__init__()

        self.events = {}
        self.main_container = None

        self.title("Magnet Finder")
        self.geometry("340x480")

    def run(self, events):
        self.events = events

        self.initialize_main_container()

    def initialize_main_container(self):
        self.main_container = Main(master=self)
        self.main_container.run()


class Main(Frame):

    def __init__(self, master):
        super().__init__(master=master)

        self.header_container = None

    def run(self):
        self.initialize_header_container()

        self.pack(padx=4, pady=4)

    def initialize_header_container(self):
        self.header_container = Header(master=self)
        self.header_container.run()


class Header(Frame):

    def __init__(self, master):
        super().__init__(master=master)

        self.search_input = None
        self.search_button = None
        self.search_button_icon = None

    def run(self):
        self.initialize_search_input()
        self.initialize_search_button()

        self.pack(padx=4)

    def initialize_search_input(self):
        cnf, pack = {}, {}

        cnf['width'] = 16
        cnf['bd'] = 2
        cnf['fg'] = 'white'
        cnf['font'] = ('Helvetica', 18, 'normal')

        pack['padx'] = 2
        pack['ipadx'] = 4
        pack['ipady'] = 2
        pack['side'] = 'left'

        self.search_input = Entry(master=self, cnf=cnf)
        self.search_input.pack(cnf=pack)

    def initialize_search_button(self):
        cnf, pack = {}, {}
        self.search_button_icon = PhotoImage(file="app/assets/find-icon.png")

        cnf['bd'] = 0
        cnf['image'] = self.search_button_icon

        pack['padx'] = 2
        pack['side'] = 'right'

        self.search_button = Button(master=self, cnf=cnf)
        self.search_button.pack(cnf=pack)
