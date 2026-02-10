from french_localizer import FrenchLocalizer
from spanish_localizer import SpanishLocalizer
from english_localizer import EnglishLocalizer

class FactoryLocalizer:
    def __init__(self, language):
        self.language = language

    def create_localizer_instance(self):
        localizer_classes = {
            'en': EnglishLocalizer,
            'es': SpanishLocalizer,
            'fr': FrenchLocalizer
        }
        try:
            return localizer_classes[self.language]()
        except KeyError:
            raise ValueError(f"Unsupported language: {self.language}")