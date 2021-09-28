# third_party/serializers/xml.py

import xml.etree.ElementTree as et


class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={"id": object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def __str__(self):
        return et.tostring(self._element, encoding="unicode")
