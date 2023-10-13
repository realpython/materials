greeting_template = "{greeting} Pythonista!"

greeting_en = "Good Morning!"
greeting_es = "¡Buenos días!"
greeting_fr = "Bonjour!"

for greeting in (greeting_en, greeting_es, greeting_fr):
    print(greeting_template.format(greeting=greeting))
