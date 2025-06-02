name = input("Enter your name please: ")

# Uncomment in Python 3.14+
# translations = {
#     "en": t"Hello, {name}! Welcome back!",
#     "es": t"¡Hola, {name}! ¡Bienvenido de vuelta!",
#     "fr": t"Bonjour, {name}! Bon retour!"
# }


def get_localized_greeting(lang):
    "Uncomment in Python 3.14+"
    # template = translations.get(lang, translations["en"])
    # parts = []
    # for item in template:
    #     if isinstance(item, str):
    #         parts.append(item)
    #     else:
    #         parts.append(item.value)
    # return "".join(parts)


print(get_localized_greeting("en"))
print(get_localized_greeting("es"))
print(get_localized_greeting("fr"))
