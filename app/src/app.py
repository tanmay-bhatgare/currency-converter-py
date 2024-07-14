import os
import customtkinter as ctk
from PIL import Image
from src.widgets.input_field import InputField
from src.widgets.c_image import CImage
from src.constants.c_fonts import CFont


class App(ctk.CTk):
    script_dir = os.path.dirname(__file__)
    assets_dir = os.path.join(script_dir, "../assets")
    dark_image_path = os.path.join(assets_dir, "converting_arrow_dark.png")
    light_image_path = os.path.join(assets_dir, "converting_arrow_light.png")

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

        # ? Images
        self.dark_image = Image.open(App.dark_image_path)
        self.light_image = Image.open(App.light_image_path)
        self.image = CImage(
            light_image=self.light_image, dark_image=self.dark_image, size=(22, 22)
        )

        # @ Custom Functions
        # @staticmethod
        # def show_values():
        #     print(self.var1.get(), self.var2.get())

        # @ Custom Fields
        # ? Input Entry
        self.entry1 = InputField(
            master=self,
            width=100,
            height=30,
            state="normal",
            textvariable=self.var1,
            font=CFont.font_large(),
        )
        self.entry1.place(x=16, y=100)

        # ? Output Entry
        self.entry2 = InputField(
            master=self,
            width=100,
            height=30,
            state="readonly",
            textvariable=self.var2,
            font=CFont.font_large(),
        )
        self.entry2.place(x=184, y=100)

        # @ Convert Logo
        self.logo = ctk.CTkLabel(self, image=self.image, text="")
        self.logo.place(x=(400 // 2) - 60, y=110)
