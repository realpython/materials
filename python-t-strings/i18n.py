name = input("Enter your name please: ")

translations = {
    "en": t"Hello, {name}! Welcome back!",  # noqa
    "es": t"¡Hola, {name}! ¡Bienvenido de vuelta!",  # noqa
    "fr": t"Bonjour, {name}! Bon retour!"  # noqa
}


def get_localized_greeting(lang):
    template = translations.get(lang, translations["en"])
    parts = []
    for item in template:
        if isinstance(item, str):
            parts.append(item)
        else:
            parts.append(item.value)
    return "".join(parts)


print(get_localized_greeting("en"))
print(get_localized_greeting("es"))
print(get_localized_greeting("fr"))
