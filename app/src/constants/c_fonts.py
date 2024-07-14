import customtkinter as ctk


class CFont:
    @staticmethod
    def font_small() -> ctk.CTkFont:
        return ctk.CTkFont(family="", size=18, weight="bold")

    @staticmethod
    def font_med() -> ctk.CTkFont:
        return ctk.CTkFont(family="", size=25, weight="bold")

    @staticmethod
    def font_large() -> ctk.CTkFont:
        return ctk.CTkFont(family="", size=35, weight="bold")

    @staticmethod
    def font_xl() -> ctk.CTkFont:
        return ctk.CTkFont(family="", size=46, weight="bold")

    @staticmethod
    def label_font() -> ctk.CTkFont:
        return ctk.CTkFont(family="Courier", size=38, weight="bold")
