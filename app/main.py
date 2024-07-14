from src.app import App

def main():
    app = App(title="Currency Converter", width=300, height=450, resizable=True)
    app.mainloop()

if __name__ == '__main__':
    main()