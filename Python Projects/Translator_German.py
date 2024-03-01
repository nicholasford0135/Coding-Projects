from googletrans import Translator

def translate_text(text, source_lang='en', target_lang='de'):
    translator = Translator()
    translated_text = translator.translate(text, src=source_lang, dest=target_lang)
    return translated_text.text

def main():
    print("English to German")
    while True:
        text = input("Enter text: ")
        if text.lower() == "exit":
            break
        translated_text = translate_text(text)
        print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()