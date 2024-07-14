import os
import customtkinter as ctk
from PIL import Image
from src.widgets.c_button import CButton
from src.widgets.input_field import InputField
from src.widgets.c_label import CLabel
from src.widgets.c_image import CImage
from src.constants.c_fonts import CFont


class App(ctk.CTk):
    script_dir = os.path.dirname(__file__)
    assets_dir = os.path.join(script_dir, "../assets")
    dark_image_path = os.path.join(assets_dir, "converting_arrow_dark.png")
    light_image_path = os.path.join(assets_dir, "converting_arrow_light.png")

    def convert_currency(self):
        if self.var1.get() == "":
            self.var1.set(0)
        self.var2.set(f"{int(self.var1.get()) * 20}")

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
        self.var1 = ctk.StringVar(name="entry1 var")
        self.var2 = ctk.StringVar(name="entry2 var")

        # ? Images
        self.dark_image = Image.open(App.dark_image_path)
        self.light_image = Image.open(App.light_image_path)
        self.image = CImage(
            light_image=self.light_image, dark_image=self.dark_image, size=(35, 35)
        )

        # @ Custom Functions

        @staticmethod
        def validate_numeric_input(input_str):
            if input_str.isdigit() or input_str == "":
                return True
            return False

        # @ Custom Fields
        # ? Title Heading
        self.head_title = CLabel(
            self,
            text="Currency\nConverter",
            font=CFont.label_font(),
            text_color="#8080ff",
        )
        self.head_title.pack()

        # ? Validatio Command
        vcmd = (self.register(validate_numeric_input), "%P")

        # ? Input Entry
        self.entry1 = InputField(
            master=self,
            width=100,
            height=30,
            state="normal",
            textvariable=self.var1,
            font=CFont.font_large(),
            validatecommand=vcmd,
        )

        # ? Output Entry
        self.entry2 = InputField(
            master=self,
            width=100,
            height=30,
            state="readonly",
            textvariable=self.var2,
            font=CFont.font_large(),
        )

        # ? Convert Button
        self.convert_button = CButton(
            master=self,
            text="Convert",
            command=self.convert_currency,
            font=CFont.font_med(),
        )

        # @ Convert Logo
        self.logo = ctk.CTkLabel(self, image=self.image, text="")

        #! All Widgets Packing
        self.entry1.pack(fill="both", pady=30, padx=16)
        self.logo.pack()
        self.entry2.pack(fill="both", pady=30, padx=16)
        self.convert_button.pack()
