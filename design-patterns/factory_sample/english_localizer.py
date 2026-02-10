class EnglishLocalizer:
    def __init__(self):
        self.language = 'English'
        self.translations = {"car": "car", "bike": "bike",
                             "cycle":"cycle"}

    def localize(self, word):
        return word