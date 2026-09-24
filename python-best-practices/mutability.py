# Avoid this:
# def add_tag(tag, tags=[]):
#     tags.append(tag)
#     return tags


# add_tag("python")
# add_tag("best-practices")


# Favor this:
def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


add_tag("python")
add_tag("best-practices")
