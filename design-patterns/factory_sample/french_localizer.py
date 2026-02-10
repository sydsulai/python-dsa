class FrenchLocalizer:
    def __init__(self):
        self.language = 'French'
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}
    
    def localize(self, word):
        return self.translations.get(word, word)