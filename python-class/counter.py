class ObjectCounter:
    num_instances = 0

    def __init__(self):
        type(self).num_instances += 1
