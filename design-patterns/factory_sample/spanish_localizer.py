class SpanishLocalizer:
    def __init__(self):
        self.language = 'Spanish'
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}
    
    def localize(self, word):
        return self.translations.get(word, word)