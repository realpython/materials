# tree.py

import sys

import yaml


def html_tree(stream, loader=yaml.SafeLoader):
    body = visit(yaml.compose(stream, loader))
    return (
        "<!DOCTYPE html>"
        "<html>"
        "<head>"
        '  <meta charset="utf-8">'
        "  <title>YAML Tree Preview</title>"
        '  <link href="https://fonts.googleapis.com/css2'
        '?family=Roboto+Condensed&display=swap" rel="stylesheet">'
        "  <style>"
        "    * { font-family: 'Roboto Condensed', sans-serif; }"
        "    ul { list-style: none; }"
        "    ul.sequence { list-style: '- '; }"
        "    .key { font-weight: bold; }"
        "    .multiline { white-space: pre; }"
        "  </style>"
        "</head>"
        f"<body>{body}</body></html>"
    )


def visit(node):
    if isinstance(node, yaml.ScalarNode):
        return cast(node.value, node.tag)
    elif isinstance(node, yaml.SequenceNode):
        return html_list(node)
    elif isinstance(node, yaml.MappingNode):
        return html_map(node)


def cast(value, tag):
    match tag.split(":")[-1]:
        case "binary":
            return f'<img src="data:image/png;base64, {value}" />'
        case _:
            if "\n" in value:
                return f'<div class="multiline">{value}</div>'
            else:
                return f"<span>{value}</span>"


def html_list(node):
    items = "".join(f"<li>{visit(child)}</li>" for child in node.value)
    return f'<ul class="sequence">{items}</ul>'


def html_map(node):
    pairs = "".join(
        (
            f'<li><span class="key">{visit(key)}:</span> {visit(value)}</li>'
            if isinstance(value, yaml.ScalarNode)
            else (
                "<li>"
                "<details>"
                f'<summary class="key">{visit(key)}</summary> {visit(value)}'
                "</details>"
                "</li>"
            )
        )
        for key, value in node.value
    )
    return f"<ul>{pairs}</ul>"


if __name__ == "__main__":
    print(html_tree("".join(sys.stdin.readlines())))
