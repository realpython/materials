html_tag = "<p>premium content</p>"

# Removes the set of the characters <, p, and >
print(html_tag.strip("<p>"))

# Removes prefix and suffix character sequences
print(html_tag.removeprefix("<p>").removesuffix("</p>"))
