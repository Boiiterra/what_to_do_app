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

        frame_collection = (WelcomePage, MainPage, SettingsPage)

        for frame in frame_collection:
            current_frame = frame(container, self)
            self.frames[frame] = current_frame
            current_frame.grid(row=0, column=0, sticky="nsew")

        self.show_page(WelcomePage)

        self.bind("<Control-q>", lambda _: self.destroy())  # Quit app event

    def show_page(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]


class WelcomePage(Frame):  # First page that users will see

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        welcome_text = "Here you can store your plans."

        welcome_phrase = Label(self, text=welcome_text, font=("Times New Roman", 35))
        welcome_phrase.pack(side="top", fill="both", expand=True)

        to_main_page_btn = Button(self, text="My plans", font=("Arial", 45), command=lambda: controller.show_page(MainPage),
                              bd=0)
        to_main_page_btn.pack(fill='both', pady=2, expand=True)

        to_settings_page_btn = Button(self, text="Settings", font=("Arial", 45), command=lambda: controller.show_page(SettingsPage),
                              bd=0)
        to_settings_page_btn.pack(fill='both', pady=2, expand=True)


class MainPage(Frame):  # Main page + ability to scroll down

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        top_container = Frame(self, )
        top_container.pack(side="top", fill="x", pady=4, padx=4)

        home_btn = Button(top_container, text="Home", command=lambda: controller.show_page(WelcomePage), font=("Arial", 25), bd=0.5)
        home_btn.pack(side="left")

        canvas = Canvas(self)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview, width=20, bg="#898989", bd=1, troughcolor="#a9a9a9", elementborderwidth=2,
                              activebackground="#696969", highlightthickness=0)
        scrollbar.pack(side="right", fill="y")

        canvas.config(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda _: canvas.config(scrollregion=canvas.bbox("all")))

        ui = Frame(canvas) # User Interface
        canvas.create_window((0, 0), window=ui, anchor="nw")


class SettingsPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        back_btn = Button(self, text="Back", font=("Arial", 35), bd=0, command=lambda: self.controller.show_page(WelcomePage))
        back_btn.pack(side="bottom", fill="both", expand=True)


if __name__ == "__main__":
    MainAppBody().mainloop()