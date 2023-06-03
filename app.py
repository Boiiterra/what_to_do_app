"""Main code of the application"""

from tkinter import Tk, Frame
from importlib import reload

import ui

WIDTH, HEIGHT = 850, 650
FONT = ("Arial", 25)


class App(Tk):
    """Core of the application with page switch"""

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("What to do?")

        self.geometry(
            f"{WIDTH}x{HEIGHT}"
            f"+{int((self.winfo_screenwidth() - WIDTH) / 2)}+"
            f"{int((self.winfo_screenheight() - HEIGHT) / 2)}"
        )  # Middle pos on the screen
        self.maxsize(self.winfo_screenwidth(), self.winfo_screenheight() - 31)
        self.minsize(800, 600)
        self.resizable(0, 0)

        self.bind("<q>", lambda _: self.destroy())
        self.bind("<F1>", lambda _: ui.Help(self))
        self.bind("<F2>", lambda _: ui.About(self))
        self.bind("<F5>", lambda _: self.hotload())  # dev only! or repurpose

        self.ch_page(ui.MainPage)

        # Windows mouse wheel event
        self.bind("<MouseWheel>", self.mouse_wheel)
        # Linux mouse wheel event (Up)
        self.bind("<Button-4>", self.mouse_wheel)
        # Linux mouse wheel event (Down)
        self.bind("<Button-5>", self.mouse_wheel)

    def hotload(self):
        """Usesed to live test changes"""
        reload(ui)
        self.ch_page(ui.MainPage, self.pack_slaves()[0])

    def mouse_wheel(self, event):
        """Mouse wheel as scroll bar"""
        direction = 0
        # respond to Linux or Windows wheel event
        if event.num == 5 or event.delta == -120:
            direction = 1
        if event.num == 4 or event.delta == 120:
            direction = -1
        if "AutoScrollbar" in str(self.top.pack_slaves()):
            self.canvas.yview_scroll(direction, "units")

    def ch_page(self, new: Frame, prev: Frame = None):
        """Change page from previous to new, if no previous switch to new"""
        if prev is not None:
            prev.pack_forget()
        new(self).pack(fill="both", expand=True)


if __name__ == "__main__":
    App().mainloop()
