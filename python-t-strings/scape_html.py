import html


def render_safe_html(template):
    parts = []
    for item in template:
        if isinstance(item, str):
            parts.append(item)
        else:
            parts.append(html.escape(item.value))
    return "".join(parts)


# Uncomment in Python 3.14+
# username = "<script>alert('Hacked!')</script>"
# template = t"<p>Hello, {username}!</p>"

# safe_html = render_safe_html(template)
# print(safe_html)
