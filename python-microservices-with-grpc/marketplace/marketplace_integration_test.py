from marketplace import render_homepage


def test_render_homepage():
    homepage_html = render_homepage()
    assert "<title>Online Books For You</title>" in homepage_html
    assert homepage_html.count("<li>") == 3
