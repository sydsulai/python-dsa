from factory_class import FactoryLocalizer

if __name__ == "__main__":
    language = input("Enter the language code (en, es, fr): ")
    factory = FactoryLocalizer(language)
    localizer = factory.create_localizer_instance()

    word = input("Enter a word to localize (car, bike, cycle): ")
    localized_word = localizer.localize(word)
    print(f"The localized word for '{word}' in {localizer.language} is: '{localized_word}'")