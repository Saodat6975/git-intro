class BasePage:

    def __init__(self, get, name, password) -> None:
        self.get = get
        self.name = name
        self.password = password