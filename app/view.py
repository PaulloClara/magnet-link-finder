from tkinter import Tk, Frame


class View(Tk):

    def __init__(self):
        super().__init__()

        self.events = {}
        self.main_window = None

        self.title("Magnet Finder")
        self.geometry("340x480")

    def run(self, events):
        self.events = events
        self.main_window = Main(master=self)


class Main(Frame):

    def __init__(self, master):
        super().__init__(master=master)

        self.pack()
