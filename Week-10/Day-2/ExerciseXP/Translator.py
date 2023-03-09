from googletrans import Translator
translator = Translator()
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
result = {}
for word in french_words:
    result[word] = translator.translate(word, src='fr').text

print(result)