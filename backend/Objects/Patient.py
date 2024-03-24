class Patient:
    def __init__(self, dct=None):
        self.id: str = None
        self.name: str = None
        self.illness: str = None
        self.curr_donations: int = None
        self.donation_goal: int = None
        self.image_url: str = None
        self.video_url: str = None
        if dct:
            self.set_serial(dct)

    def get_serial(self):
        return {
            "id": self.id,
            "name": self.name,
            "illness": self.illness,
            "curr_donations": self.curr_donations,
            "donation_goal": self.donation_goal,
            "image_url": self.image_url,
            "video_url": self.video_url
        }

    def set_serial(self, dct):
        self.id = dct["id"]
        self.name = dct["name"]
        self.illness = dct["illness"]
        self.curr_donations = dct["curr_donations"]
        self.donation_goal = dct["donation_goal"]
        self.image_url = dct["image_url"]
        self.video_url = dct["video_url"]
