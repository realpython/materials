def fill_order_template(lang, name, order_id, date):
    templates = {
        "en": t"Thank you, {name}! Your order #{order_id} will arrive on {date}.",
        "es": t"Gracias, {name} Su orden No. {order_id} arribará el próximo {date}.",
        "fr": t"Merci, {name}! Votre commande n° {order_id} arrivera le {date}.",
    }
    return templates.get(lang, templates["en"])


def generate_order_email(template):
    parts = []
    for item in template:
        if isinstance(item, str):
            parts.append(item)
        else:
            parts.append(str(item.value))
    return "".join(parts)


template = fill_order_template("en", "Alice", 12345, "June 10")
email = generate_order_email(template)
print(email)
