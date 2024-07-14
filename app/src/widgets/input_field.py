import customtkinter as ctk
from typing import Optional, Callable


class InputField(ctk.CTkEntry):
    def __init__(
        self,
        master: ctk.CTk,
        textvariable: ctk.StringVar,
        font: ctk.CTkFont,
        width: int = 140,
        height: int = 28,
        validatecommand: Optional[Callable] = None,
        state: str = "normal",
    ) -> None:
        kwargs = {
            "master": master,
            "state": state,
            "width": width,
            "height": height,
            "textvariable": textvariable,
            "font": font,
            "justify": "right",
            "validate": "key",
        }
        if validatecommand:
            kwargs["validatecommand"] = validatecommand

        super().__init__(**kwargs)
