from tkinter import Tk, Frame, Canvas, Entry, Label, Button, Scrollbar, PhotoImage


class View(Tk):

    def __init__(self):
        super().__init__()

        self.events = {}
        self.main_container = None

        self.title('Magnet Finder')
        self.geometry('340x480')
        self.resizable(0, 0)

        self.wm_iconphoto(True, PhotoImage(file='app/assets/icons/window.png'))

    def run(self, events):
        self.events = events

        self.initialize_main_container()

    def initialize_main_container(self):
        self.main_container = Main(master=self)
        self.main_container.run()


class Main(Frame):

    def __init__(self, master):
        super().__init__(master=master)

        self.body_container = None
        self.header_container = None

    def run(self):
        self.initialize_header_container()
        self.initialize_body_container()

        self.pack(padx=4)

    def initialize_body_container(self):
        self.body_container = Body(master=self)
        self.body_container.run()

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
        self.search_button_icon = PhotoImage(file='app/assets/icons/find.png')

        self.initialize_search_input()
        self.initialize_search_button()

        self.search_input.focus()

        self.pack(pady=4, side='top')

    def initialize_search_input(self):
        cnf = {}

        cnf['bd'] = 4
        cnf['bg'] = '#606060'
        cnf['relief'] = 'ridge'
        cnf['highlightcolor'] = 'grey'
        cnf['selectbackground'] = 'grey'
        cnf['fg'] = 'white'
        cnf['justify'] = 'center'
        cnf['insertbackground'] = 'white'
        cnf['font'] = ('Helvetica', 18, 'normal')

        self.search_input = Entry(master=self, cnf=cnf)
        self.search_input.pack(ipadx=4, ipady=2, side='left')

    def initialize_search_button(self):
        cnf = {}

        cnf['bd'] = 0
        cnf['image'] = self.search_button_icon

        self.search_button = Button(master=self, cnf=cnf)
        self.search_button.pack(ipadx=2, side='right')


class Body(Frame):

    def __init__(self, master):
        super().__init__(master=master, bd=2, bg='grey')

        self.canvas = None
        self.viewport = None
        self.scrollbar = None

        self.item_button_icon = None

    def run(self):
        self.item_button_icon = PhotoImage(file='app/assets/icons/copy.png')

        self.initialize_canvas()
        self.initialize_viewport()
        self.initialize_scrollbar()

        self.config_scrollview()

        for i in range(20):
            self.create_item(text=f'Label Label Label {i}')

        self.pack(pady=4, side='bottom')

    def create_item(self, text):
        cnf = {}

        cnf['bd'] = 2
        cnf['bg'] = 'darkgreen'
        cnf['relief'] = 'raised'

        item = Frame(master=self.viewport, cnf=cnf)

        cnf = {}

        cnf['text'] = text
        cnf['bg'] = 'darkgreen'
        cnf['fg'] = 'white'
        cnf['font'] = ('Helvetica', 14, 'normal')

        label = Label(master=item, cnf=cnf)
        label.pack(ipadx=10, fill='y', side='left')

        cnf = {}

        cnf['bd'] = 2
        cnf['bg'] = 'green'
        cnf['activebackground'] = 'green'
        cnf['image'] = self.item_button_icon

        button = Button(master=item, cnf=cnf)
        button.pack(side='right')

        item.pack(fill='x')

    def config_scrollview(self):
        self.scrollbar.configure(command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)

        self.canvas_window = self.canvas.create_window(
            (4, 4), window=self.viewport, anchor='nw', tags='self.viewport')

        self.canvas.bind('<Configure>', lambda event: self.canvas.itemconfig(
            self.canvas_window, width=event.width))
        self.viewport.bind('<Configure>', lambda event: self.canvas.configure(
            scrollregion=self.canvas.bbox('all')))

    def initialize_canvas(self):
        cnf = {}

        cnf['height'] = 420
        cnf['bd'] = 2
        cnf['bg'] = 'grey'

        self.canvas = Canvas(master=self, cnf=cnf)

    def initialize_viewport(self):
        cnf = {}

        self.viewport = Frame(master=self.canvas, cnf=cnf)

    def initialize_scrollbar(self):
        cnf = {}

        cnf['width'] = 14
        cnf['bd'] = 4
        cnf['bg'] = 'grey'
        cnf['relief'] = 'raised'

        self.scrollbar = Scrollbar(master=self, cnf=cnf)
