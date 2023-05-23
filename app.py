from tkinter import Tk, Frame, Button, Entry, Scrollbar, Canvas, Label

WIDTH, HEIGHT = 850, 650
FONT = ("Arial", 25)


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

        bottom = Frame(self, height=100, bg="#02d2d2")
        bottom.pack(fill="both")

        top = Frame(self)
        top.pack(side="bottom", expand=True, fill="both")
        self.top = top

        self.bind("<q>", lambda _: self.destroy())

        cnv = Canvas(top)
        cnv.pack(side="left", fill="both", expand=True)
        self.canvas = cnv

        scrollbar = AutoScrollbar(top, orient="vertical", command=cnv.yview, width=20)

        cnv.config(yscrollcommand=scrollbar.set)
        cnv.bind("<Configure>", lambda _: cnv.config(scrollregion=cnv.bbox("all")))

        # Windows mouse wheel event
        self.bind("<MouseWheel>", self.mouse_wheel)
        # Linux mouse wheel event (Up)
        self.bind("<Button-4>", self.mouse_wheel)
        # Linux mouse wheel event (Down)
        self.bind("<Button-5>", self.mouse_wheel)

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
