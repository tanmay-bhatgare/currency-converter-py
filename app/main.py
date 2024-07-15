from src.app import App

def main():
    app = App(title="Currency Converter", width=300, height=470, resizable=False)
    app.mainloop()

if __name__ == '__main__':
    main()