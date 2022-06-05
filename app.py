from tkinter import Tk, Frame, Button, Scrollbar, Canvas, Label, Button
from platform import system


_version_ = "0.1"


class MainAppBody(Tk):  # App's body

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title(f"What To Do - {_version_}")
        if system().lower() == "windows": ...
            # self.iconbitmap("icon.ico")
        self.geometry(f"800x600+{(self.winfo_screenwidth() - 800 ) // 2}+{(self.winfo_screenheight() - 600) // 2}")
        self.maxsize(self.winfo_screenwidth(), self.winfo_screenheight() - 31)
        self.minsize(800, 600)

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame_collection = (WelcomePage, MainPage)

        for frame in frame_collection:
            current_frame = frame(container, self)
            self.frames[frame] = current_frame
            current_frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

        self.bind("<Control-q>", lambda _: self.destroy())  # Quit app event

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]


class WelcomePage(Frame):  # First page that users will see

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        switch_pages = Button(self, text="To MainPage", font=("Arial", 45), command=lambda: controller.show_frame(MainPage))
        switch_pages.pack(fill='both', pady=2, expand=True)


class MainPage(Frame):  # Main page + ability to scroll down

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="black")
        self.controller = controller

        canvas = Canvas(self)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview, width=20, bg="#898989", bd=1, troughcolor="#a9a9a9", elementborderwidth=2,
                              activebackground="#696969", highlightthickness=0)
        scrollbar.pack(side="right", fill="y")

        canvas.config(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda _: canvas.config(scrollregion=canvas.bbox("all")))

        user_interface = Frame(canvas)
        ui = user_interface
        canvas.create_window((0, 0), window=ui, anchor="nw")


if __name__ == "__main__":
    MainAppBody().mainloop()