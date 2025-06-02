import json
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TemplateMessage:
    def __init__(self, template):
        self.template = template

    @property
    def message(self):
        parts = []
        for item in self.template:
            if isinstance(item, str):
                parts.append(item)
            else:
                parts.append(str(item.value))
        return "".join(parts)

    @property
    def values_dict(self):
        values = {}
        for item in self.template:
            if not isinstance(item, str):
                values[item.expression] = item.value
        return values

    def __str__(self):
        return f"{self.message} >>> {json.dumps(self.values_dict)}"


# Uncomment in Python 3.14+
# action, amount, item = "refund", 7, "keyboard"
# msg_template = TemplateMessage(t"Process {action}: {amount:.2f} {item}")
# logging.info(msg_template)
