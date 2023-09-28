from googletrans import Translator, LANGUAGES


def TransLate(text, lang):
    try:
        # Перевірка, чи вказана мова підтримується
        lang = lang.lower()  # Переводимо введену мову в маленькі літери
        # Якщо введено ISO-639 код мови, виконуємо переклад
        if lang in LANGUAGES:
            # Створення об'єкту класу Translator
            translator = Translator()

            # Переклад тексту на вказану мову
            translated_text = translator.translate(text, src='auto', dest=lang)

            return translated_text.text
        else:
            # Якщо введено назву мови з маленької літери, перетворюємо на велику і виконуємо переклад
            lang = lang.capitalize()  # Перетворюємо першу літеру на велику
            translator = Translator()
            translated_text = translator.translate(text, src='auto', dest=lang)
            return translated_text.text
    except :
            return "Помилка в назві мови"

def LangDetect(txt):
    try:
        # Визначення мови тексту
        translator = Translator()
        result = translator.detect(txt)

        # Вибір детектированої мови та confidence
        detected_lang = result.lang
        confidence = result.confidence

        return detected_lang, confidence
    except :
        return "Не вдалося визначити мову", 0.0


# Функція для перекладу назви мови в код мови та навпаки
def CodeLang(lang):
    # Створіть екземпляр класу Translator
    translator = Translator()
    lang = lang.lower()
    # Перевіримо, чи lang є кодом мови
    if lang in LANGUAGES:
        # Якщо так, перекладемо код мови на назву мови
        language_name = LANGUAGES[lang]
        return language_name.capitalize()
    else:
        # Якщо не знайдено, спробуємо знайти код мови за назвою
        try:
            # Перекладемо назву мови на код мови
            translation = translator.translate(lang, src='en', dest='en')
            for code, name in LANGUAGES.items():
                if name.lower() == translation.text.lower():
                    return code
            # Назва мови не знайдена
            return "Не знайдено мову"
        except Exception as e:
            # Обробити помилки, якщо такі є (наприклад, відсутність з'єднання)
            print(f"Помилка: {e}")
            return None



txt = "Доброго дня. Як справи?"
lang = "SERBIAN"

print(txt)
print(LangDetect(txt))
print(TransLate(txt, lang))
print(CodeLang(lang))