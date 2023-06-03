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


class Help(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.title("Help")
        self.transient(parent)
        self.geometry(
            "350x250"
            f"+{int((self.winfo_screenwidth() - 350) / 2)}"
            f"+{int((self.winfo_screenheight() - 250) / 2)}"
        )
        self.wait_visibility()
        self.grab_set()

        self.bind("<q>", lambda _: self.destroy())

        self.config(bg=BG)

        Label(self, font=("Arial", 15), text="Help:", bg=BG).pack(
            fill="x", ipadx=5, ipady=5
        )

        help_txt = "- Press Q to quit.\n- Press F1 to call for help.\n- Press F2 to learn about app."

        Label(self, font=("Arial", 15), text=help_txt, bg=BG).pack(
            fill="both", expand=True, pady=15
        )

        Button(
            self,
            font=("Arial", 15),
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

        bout = "This is a to-do application. You can use it to plan"

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
