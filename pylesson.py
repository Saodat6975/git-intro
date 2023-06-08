class Human:
    barks = True
    legs = 2
    arms = 2
    fingers = 10 

    def __init__(self, old, name, nationality) -> None:
        self.old = old
        self.name = name
        self.nationality = nationality



class Employee:
    vacation_days = 30 

    def __init__(self, location, job_name) -> None:
        self.location = location
        self.job_name = job_name