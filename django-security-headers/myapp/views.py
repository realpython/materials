from django.http import HttpResponse


def index(request):
    return HttpResponse(
        """\
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8"><title>My secure app</title>
    <link rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/normalize.css@8.0.1/normalize.css"
    >
  </head>
  <body><p>Now this is some sweet HTML!</p></body>
</html>"""
    )
