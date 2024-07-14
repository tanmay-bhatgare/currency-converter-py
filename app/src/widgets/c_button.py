import customtkinter as ctk


class CButton(ctk.CTkButton):
    def __init__(
        self,
        master: ctk.CTk,
        command,
        text: str = "CButton",
        bg_color: str = "transparent",
        text_color: str = "black",
        height: int = 28,
        font: ctk.CTkFont = None,
    ) -> None:
        super().__init__(
            master=master,
            text=text,
            height=height,
            bg_color=bg_color,
            text_color=text_color,
            command=command,
            font=font,
        )
