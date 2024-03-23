class Hospital:
    def __init__(self, dct=None):
        self.name: str = None
        self.location: str = None
        self.patients: list = None
        self.curr_donations: int = None
        self.donation_goal: int = None
        if dct:
            self.set_serial(dct)

    def get_serial(self):
        return {
            "name": self.name,
            "location": self.location,
            "patients": self.patients,
            "curr_donations": self.curr_donations,
            "donation_goal": self.donation_goal
        }

    def set_serial(self, dct):
        self.name = dct["name"]
        self.location = dct["location"]
        self.patients = dct["patients"]
        self.curr_donations = dct["curr_donations"]
        self.donation_goal = dct["donation_goal"]