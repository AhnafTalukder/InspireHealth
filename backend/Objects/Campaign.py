class Campaign:
    def __init__(self, dct=None):
        self.attrs = ["start", "end", "name", "description", "hospital_name", "pledge_amount", "city", "country",
                      "contact_email", "paypal", "image_link", "video_link", "id"]
        self.start: str = None
        self.end: str = None
        self.name: str = None
        self.description: str = None
        self.hospital_name: str = None
        self.pledge_amount: str = None
        self.city: str = None
        self.country: str = None
        self.contact_email: str = None
        self.paypal: str = None
        self.image_link: str = None
        self.video_link: str = None
        self.id: str = None
        if dct:
            self.set_serial(dct)

    def get_serial(self):
        res = {}

        for attr in self.attrs:
            res[attr] = getattr(self, attr)

        return res

    def set_serial(self, dct):
        for attr in self.attrs:
            setattr(self, attr, dct[attr])