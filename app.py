"""Main code of the application"""

from tkinter import Tk, Frame, Toplevel, Button, Label
from importlib import reload

import ui

WIDTH, HEIGHT = 850, 650
FONT = ("Arial", 25)
ABG = "#d7d7d7"
BG = "#c7c7c7"


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
        self.bind("<F1>", lambda _: Help(self))
        self.bind("<F2>", lambda _: About(self))
        self.bind("<F5>", lambda _: self.hotload())  # dev only! or repurpose
        self.bind("<r>", lambda _: self.hotload())  # dev only! or repurpose

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


class Help(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.title("Help")
        self.transient(parent)
        self.geometry(
            "335x260"
            f"+{int((self.winfo_screenwidth() - 335) / 2)}"
            f"+{int((self.winfo_screenheight() - 260) / 2)}"
        )
        self.wait_visibility()
        self.grab_set()

        self.bind("<q>", lambda _: self.destroy())

        self.config(bg=BG)

        Label(self, font=15, text="Help:", bg=BG).pack(pady=(5, 0))

        help_txt = (
            "- Press Q to close application.\n"
            "- Press F1 to 'call for help'.\n"
            "- Press F2 to learn about app.\n\n"
            "- Click on '+ New task' to start.\n"
            "- Click on '' to complete task.\n"
            "- Click on '' to remove task."
        )

        Label(self, font=15, text=help_txt, bg=BG).pack(pady=15)

        Button(
            self,
            font=15,
            command=self.destroy,
            text="OK",
            bg=BG,
            activebackground=ABG,
        ).pack(side="bottom", ipady=5)


class About(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.transient(parent)
        self.wait_visibility()
        self.grab_set()
        self.geometry(
            "313x254"
            f"+{int((self.winfo_screenwidth() - 313) / 2)}"
            f"+{int((self.winfo_screenheight() - 254) / 2)}"
        )
        self.resizable(0, 0)
        self.title("About")

        self.bind("<q>", lambda _: self.destroy())

        self.config(bg=BG)

        Label(self, text="About:", font=15, pady=5, bg=BG).pack()

        bout = (
            "This is a to-do application.\n"
            "You can use it to plan something.\n"
            "Has basic features of to-do app.\n"
            "Designed to be used on Linux but supports other OSs.\n\n"
            "Made by Boiiterra for Boiiterra.\nYou can use it too. :D"
        )

        Label(self, text=bout, font=15, pady=5, bg=BG, wraplength=313).pack()

        Button(
            self,
            text="OK",
            font=15,
            command=self.destroy,
            width=7,
            bg=BG,
            activebackground=ABG,
        ).pack(side="bottom", pady=10)


if __name__ == "__main__":
    App().mainloop()
