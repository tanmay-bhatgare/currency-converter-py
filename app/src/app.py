import os
import customtkinter as ctk
from PIL import Image
from src.widgets.c_option_menu import COptionMenu
from src.widgets.c_button import CButton
from src.widgets.c_input_field import InputField
from src.widgets.c_label import CLabel
from src.widgets.c_image import CImage
from src.constants.c_fonts import CFont
from src.utils.fetch_data import fetch_currency_data


class App(ctk.CTk):
    script_dir: str = os.path.dirname(__file__)
    assets_dir: str = os.path.join(script_dir, "../assets")
    dark_image_path: str = os.path.join(assets_dir, "converting_arrow_dark.png")
    light_image_path: str = os.path.join(assets_dir, "converting_arrow_light.png")

    def convert_currency(self) -> None:
        currency_rate: float = fetch_currency_data(self.from_currency.get())[
            self.to_currency.get()
        ]
        self.to_output.set(f"{int(self.from_input.get()) * currency_rate}")

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
        self.from_input: ctk.Variable = ctk.StringVar(value=0, name="entry1 var")
        self.to_output: ctk.Variable = ctk.StringVar(value=0, name="entry2 var")
        # *
        self.from_currency: ctk.Variable = ctk.StringVar(value="inr", name="from currency variable")
        self.to_currency: ctk.Variable = ctk.StringVar(value="usd", name="to currency variable")
        # *
        self.from_currencies_list: list = list(
            fetch_currency_data(currency=self.from_currency.get()).keys()
        )
        self.to_currencies_list: list = list(
            fetch_currency_data(currency=self.to_currency.get()).keys()
        )

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
            textvariable=self.from_input,
            font=CFont.font_large(),
            validatecommand=vcmd,
        )

        # ? Output Entry
        self.entry2 = InputField(
            master=self,
            width=100,
            height=30,
            state="readonly",
            textvariable=self.to_output,
            font=CFont.font_large(),
        )

        # ? Convert Button
        self.convert_button = CButton(
            master=self,
            text="Convert",
            command=self.convert_currency,
            font=CFont.font_med(),
        )

        # ? From Option Menu
        self.from_currency_menu = COptionMenu(
            master=self, values=self.from_currencies_list, variable=self.from_currency
        )
        self.from_currency_menu.place(x=16, y=100)

        # ? TO Option Menu
        self.to_currency_menu = COptionMenu(
            master=self, values=self.to_currencies_list, variable=self.to_currency
        )
        self.to_currency_menu.place(x=16, y=278)

        # @ Convert Logo
        self.logo = ctk.CTkLabel(self, image=self.image, text="")

        #! All Widgets Packing
        self.entry1.pack(fill="both", padx=16, pady=45)
        self.logo.pack()
        self.entry2.pack(fill="both", padx=16, pady=50)
        self.convert_button.pack()
