"""This file is made for hot reloading in order to test changes in UI/UX"""

from tkinter import Scrollbar, Frame, Label, Toplevel, Button, Canvas, Entry
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
        self.geometry(
            "320x250"
            f"+{(self.winfo_screenwidth() - 320) // 2}"
            f"+{(self.winfo_screenheight() - 250) // 2}"
        )
        self.resizable(0, 0)
        self.transient(parent)
        self.wait_visibility()
        self.grab_set()

        def cancel():
            self.destroy()

        def add():
            _name = tname.get()
            _descr = tdescr.get()
            if _name != "" and _descr != "":
                tname.delete(0, "end")
                tdescr.delete(0, "end")
            else:
                showinfo("Data is missing", "error")

        Label(view, text="Add new task", font=15).pack()

        class_cont = Frame(view)
        class_cont.pack(pady=10)

        Label(class_cont, text="New task:", font=15).grid(row=0, column=0)
        tname = Entry(class_cont, width=2, font=15)
        tname.grid(row=0, column=1)  # Number
        tdescr = Entry(class_cont, width=2, font=15)
        tdescr.grid(row=0, column=2)  # Letter

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
