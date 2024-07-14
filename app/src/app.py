import customtkinter as ctk
from src.widgets.input_field import InputField
from src.constants.c_fonts import CFont


class App(ctk.CTk):
    def __init__(
        self,
        title: str = "App",
        width: int = 400,
        height: int = 500,
        resizable: bool = True,
    ) -> None:
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(resizable, resizable)

        # @ Custom Variables
        self.var1 = ctk.StringVar()
        self.var2 = ctk.StringVar()

        # @ Custom Fields
        self.entry1 = InputField(
            master=self,
            width=100,
            height=30,
            # state="normal",
            textvariable=self.var1,
            font=CFont.font_large(),
        )
        self.entry1.place(x=40, y=200)

        self.entry2 = InputField(
            master=self,
            width=100,
            height=30,
            textvariable=self.var2,
            font=CFont.font_large(),
        )
        self.entry2.place(x=200, y=200)
