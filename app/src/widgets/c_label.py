import customtkinter as ctk
from ..constants.c_fonts import CFont


class CLabel(ctk.CTkLabel):
    def __init__(
        self,
        master: ctk.CTk,
        width: int = 0,
        height: int = 28,
        bg_color: str = "transparent",
        text_color: str = "white",
    ) -> None:
        super().__init__(
            master=master,
            width=2,
            height=2,
            bg_color="",
            text_color="",
            font=CFont.font_xl(),
        )
