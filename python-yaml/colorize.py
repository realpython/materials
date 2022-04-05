# colorize.py

import sys

import yaml


def colorize(text):
    colors = {
        yaml.KeyToken: lambda x: f"\033[34;1m{x}\033[0m",
        yaml.ValueToken: lambda x: f"\033[36m{x}\033[0m",
        yaml.TagToken: lambda x: f"\033[31m{x}\033[0m",
    }

    for start, end, token in reversed(list(tokenize(text))):
        color = colors.get(type(token), lambda text: text)
        text = text[:start] + color(text[start:end]) + text[end:]

    return text


def tokenize(text, loader=yaml.SafeLoader):
    last_token = yaml.ValueToken(None, None)
    for token in yaml.scan(text, loader):
        start = token.start_mark.index
        end = token.end_mark.index
        if isinstance(token, yaml.TagToken):
            yield start, end, token
        elif isinstance(token, yaml.ScalarToken):
            yield start, end, last_token
        elif isinstance(token, (yaml.KeyToken, yaml.ValueToken)):
            last_token = token


if __name__ == "__main__":
    print(colorize("".join(sys.stdin.readlines())))
