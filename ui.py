"""This file is made for hot reloading in order to test changes in UI/UX"""

from tkinter import Scrollbar, Frame, Label, Toplevel, Button, Canvas, Entry, Text
from tkinter.messagebox import showinfo

FONT = ("Arial", 20)
ABG = "#d7d7d7"
BG = "#c7c7c7"

tasks = []  # Will prob use


class AutoScrollbar(Scrollbar):
    """Scrollbar that appears when needed"""

    def set(self, low, high):
        if float(low) <= 0.0 and float(high) >= 1.0:
            self.pack_forget()
        else:
            self.pack(side="right", fill="y")
        Scrollbar.set(self, low, high)


class NewTask(Toplevel):
    """Must be reworked for this project"""

    def __init__(self, parent, _location: list):
        Toplevel.__init__(self, parent, bg="#bbb")
        view = Frame(self)
        view.pack(pady=10, padx=10, fill="both", expand=True)
        self.title("Add task")
        h = 290
        w = 360
        self.geometry(
            f"{w}x{h}"
            f"+{(self.winfo_screenwidth() - w) // 2}"
            f"+{(self.winfo_screenheight() - h) // 2}"
        )
        self.resizable(0, 0)
        self.transient(parent)
        self.wait_visibility()
        self.grab_set()

        def cancel():
            self.destroy()

        def add():
            _name = tname.get()
            _descr = tdescr.get(0.0, "end")
            if _name != "" and _descr != "":
                tname.delete(0, "end")
                tdescr.delete(0.0, "end")
            else:
                showinfo(
                    "Data is missing",
                    "Error: Not enough data entered.\n"
                    "Please fill all empty boxes with some text.",
                )

        Label(view, text="Task's name:", font=15).pack(pady=5)
        tname = Entry(view, width=40, font=15)
        tname.pack()

        Label(view, text="Description:", font=15).pack(pady=(10, 5))
        tdescr = Text(view, width=45, height=6, font=15)
        tdescr.pack()

        btn_cont = Frame(view)
        btn_cont.pack(side="bottom", pady=5)

        Button(btn_cont, text="Add task", command=add).grid(
            row=0, column=0, padx=10, pady=5
        )
        Button(btn_cont, text="Cancel", command=cancel).grid(
            row=0, column=1, padx=10, pady=5
        )

        self.bind("<q>", lambda _: self.destroy())


class TaskRemWarn:
    pass


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

        Button(
            bottom,
            text="+ New task",
            font=FONT,
            bd=0,
            bg=BG,
            activebackground=ABG,
            highlightthickness=0,
            command=lambda: NewTask(parent, None),
        ).pack(side="left", pady=(5, 0), padx=(25, 0))

        top = Frame(self)
        top.pack(side="bottom", expand=True, fill="both")
        self.top = top

        cnv = Canvas(top)
        cnv.pack(side="left", fill="both", expand=True)
        self.canvas = cnv

        parent.bind("<i>", lambda _: NewTask(parent, None))

        scrollbar = AutoScrollbar(top, orient="vertical", command=cnv.yview, width=20)

        cnv.config(yscrollcommand=scrollbar.set)
        cnv.bind("<Configure>", lambda _: cnv.config(scrollregion=cnv.bbox("all")))

        parent.canvas = cnv
        parent.top = top
