import customtkinter as ctk

class InputField(ctk.CTkEntry):
    def __init__(
        self,
        master: ctk.CTk,
        textvariable: ctk.StringVar,
        font: ctk.CTkFont,
        width: int = 140,
        height: int = 28,
        state: str = "normal",
    ) -> None:
        super().__init__(
            master=master,
            state=state,
            width=width,
            height=height,
            textvariable=textvariable,
            font=font,
            justify="right",
        )
