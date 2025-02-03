def make_appender():
    items = []

    def appender(new_item):
        items.append(new_item)
        return items

    return appender
