"""This file is made for hot reloading in order to test changes in UI/UX"""

from tkinter import Scrollbar, Frame, Label, Toplevel, Button, Canvas

FONT = ("Arial", 25)
ABG = "#d7d7d7"
BG = "#c7c7c7"


class AutoScrollbar(Scrollbar):
    """Scrollbar that appears when needed"""

    def set(self, low, high):
        if float(low) <= 0.0 and float(high) >= 1.0:
            self.pack_forget()
        else:
            self.pack(side="right", fill="y")
        Scrollbar.set(self, low, high)


class Task(Frame):
    def __init__(self, master, name):
        Frame.__init__(self, master)

        Label(self, font=FONT, text=name).pack()


class MainPage(Frame):
    """Main page, the one you interact with"""

    def __init__(self, parent):
        Frame.__init__(self, parent)

        bottom = Frame(self, height=100, bg="#02d2d2")
        bottom.pack(fill="both")

        top = Frame(self)
        top.pack(side="bottom", expand=True, fill="both")
        self.top = top

        cnv = Canvas(top)
        cnv.pack(side="left", fill="both", expand=True)
        self.canvas = cnv

        scrollbar = AutoScrollbar(top, orient="vertical", command=cnv.yview, width=20)

        cnv.config(yscrollcommand=scrollbar.set)
        cnv.bind("<Configure>", lambda _: cnv.config(scrollregion=cnv.bbox("all")))

        parent.canvas = cnv
        parent.top = top
