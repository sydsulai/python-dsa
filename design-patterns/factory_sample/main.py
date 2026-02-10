from factory_class import FactoryLocalizer

if __name__ == "__main__":
    language = input("Enter the language code (en, es, fr): ")
    factory = FactoryLocalizer(language)
    localizer = factory.create_localizer_instance()

    word = input("Enter a word to localize (car, bike, cycle): ")
    localized_word = localizer.localize(word)
    print(f"The localized word for '{word}' in {localizer.language} is: '{localized_word}'")

"""
Factory Pattern is a design pattern that provides an interface for creating objects in a superclass, 
but allows subclasses to alter the type of objects that will be created. 
In this example, we have a FactoryLocalizer class that creates instances of different localizer classes (EnglishLocalizer, SpanishLocalizer, FrenchLocalizer) based on the language code provided by the user. 
Each localizer class has its own implementation of the localize method, which translates words into the respective language. 
This pattern helps in decoupling the client code from the specific classes that need to be instantiated, making it easier to add new localizers in the future without modifying existing code.
"""