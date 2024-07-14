import customtkinter as ctk
from ..constants import c_fonts


class CLabel(ctk.CTkLabel):
    def __init__(
        self,
        master: ctk.CTk,
    ) -> None:
        super().__init__(
            master=master,
            width=2,
            height=2,
            bg_color="",
            text_color="",
            font=c_fonts.font_xl,
        )
