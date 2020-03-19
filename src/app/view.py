from src import FIND_ICON_PATH, COPY_ICON_PATH, WINDOW_ICON_PATH, WINDOW_WIDTH, WINDOW_HEIGHT
from tkinter import Tk, Frame, Canvas, Entry, Label, Button, Scrollbar, PhotoImage


class View(Tk):

    def __init__(self):
        super().__init__()

        self.title('Magnet Finder')
        self.wm_iconphoto(True, PhotoImage(file=WINDOW_ICON_PATH))

        posx = self.winfo_screenwidth() // 2 - WINDOW_WIDTH // 2
        posy = self.winfo_screenheight() // 2 - WINDOW_HEIGHT // 2
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{posx}+{posy}')

        self.resizable(0, 0)

        self.events = {}
        self.container = None

    def run(self, events):
        self.events = events

        self.initialize_container()

    def initialize_container(self):
        self.container = Container(master=self)
        self.container.run()


class Container(Frame):

    def __init__(self, master):
        super().__init__(master=master)

        self.main = None
        self.header = None

    def run(self):
        self.initialize_header()
        self.initialize_main()

        self.pack(padx=4)

    def initialize_main(self):
        self.main = Main(master=self)
        self.main.run(self.master.events['main'])

    def initialize_header(self):
        self.header = Header(master=self)
        self.header.run(self.master.events['header'])


class Header(Frame):

    def __init__(self, master):
        super().__init__(master=master)

        self.search_input = None
        self.search_button = None
        self.search_button_icon = None

        self.events = {}

    def run(self, events):
        self.events = events
        self.search_button_icon = PhotoImage(file=FIND_ICON_PATH)

        self.initialize_search_input(command=events['search_link'])
        self.initialize_search_button(command=events['search_link'])

        self.search_input.focus()

        self.pack(pady=4, side='top')

    def initialize_search_input(self, command):
        cnf = {}

        cnf['bd'] = 2
        cnf['bg'] = '#606060'
        cnf['relief'] = 'ridge'
        cnf['highlightcolor'] = 'grey'
        cnf['selectbackground'] = 'grey'
        cnf['fg'] = 'white'
        cnf['justify'] = 'center'
        cnf['insertbackground'] = 'white'
        cnf['font'] = ('Helvetica', 18, 'normal')

        self.search_input = Entry(master=self, cnf=cnf)
        self.search_input.bind('<Return>', command)

        self.search_input.pack(ipadx=6, ipady=2, side='left')

    def initialize_search_button(self, command):
        cnf = {}

        cnf['bd'] = 0
        cnf['image'] = self.search_button_icon

        self.search_button = Button(master=self, cnf=cnf)
        self.search_button.bind('<Button-1>', command)

        self.search_button.pack(ipadx=4, side='right')


class Main(Frame):

    def __init__(self, master):
        super().__init__(master=master, bd=2, bg='grey')

        self.canvas = None
        self.viewport = None
        self.scrollbar = None

        self.items = []

        self.events = {}
        self.item_button_icon = None

    def run(self, events):
        self.events = events

        self.initialize_canvas()
        self.initialize_viewport()
        self.initialize_scrollbar()

        self.configure_scrollview()
        self.pack(pady=4, side='bottom')

    def load_items(self, links):
        self.destroy_items()

        for link in links:
            self.create_item(text=link, command=self.events['copy_link'])

    def destroy_items(self):
        for item in self.items:
            item.destroy()

    def create_item(self, text, command):
        item = Item(master=self.viewport)
        item.run(text=text, command=command)

        self.items.append(item)

    def configure_scrollview(self):
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

        self.canvas = Canvas(master=self, cnf=cnf)

    def initialize_viewport(self):
        cnf = {}

        self.viewport = Frame(master=self.canvas, cnf=cnf)

    def initialize_scrollbar(self):
        cnf = {}

        cnf['width'] = 14
        cnf['bd'] = 2
        cnf['bg'] = 'grey'
        cnf['relief'] = 'raised'

        self.scrollbar = Scrollbar(master=self, cnf=cnf)


class Item(Frame):

    def __init__(self, master):
        cnf = {}

        cnf['bd'] = 1
        cnf['bg'] = 'darkgreen'
        cnf['relief'] = 'solid'

        super().__init__(master=master, cnf=cnf)

        self.label = None
        self.button = None
        self.button_icon = None

        self.link = ''

    def run(self, text, command):
        self.link = text
        self.button_icon = PhotoImage(file=COPY_ICON_PATH)

        self.initialize_label(text=text)
        self.initialize_button(command=command)

        self.pack(fill='x')

    def initialize_label(self, text):
        cnf = {}

        cnf['text'] = text if len(text) < 25 else f'{text[:22]}...'
        cnf['bg'] = 'darkgreen'
        cnf['fg'] = 'white'
        cnf['font'] = ('Helvetica', 14, 'normal')

        self.label = Label(master=self, cnf=cnf)
        self.label.pack(ipadx=10, fill='y', side='left')

    def initialize_button(self, command):
        cnf = {}

        cnf['bd'] = 2
        cnf['bg'] = 'green'
        cnf['activebackground'] = 'green'
        cnf['image'] = self.button_icon

        self.button = Button(master=self, cnf=cnf)
        self.button.bind('<Button-1>',
                         lambda event: command(event, self.link))

        self.button.pack(side='right')
