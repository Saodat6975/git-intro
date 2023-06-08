class Bank:

    def __init__(self, personal_information, account_nummber) -> None:
        self.personal_information = personal_information
        self.account_number = account_nummber


Saodat = Bank('Saodat Saydirasulova', 138273928)

print(Saodat.account_number)