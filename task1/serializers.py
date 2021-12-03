from xml.dom.minidom import parseString
from json import dumps

from dicttoxml import dicttoxml


class XMLSerializer:
    """Class for serializing xml"""
    @staticmethod
    def serialize(data: list[dict]) -> str:
        xml = dicttoxml(data, custom_root="rooms")
        result = parseString(xml).toprettyxml()
        return result


class JSONSerializer:
    """Class for serializing xml"""
    @staticmethod
    def serialize(data: list[dict]) -> str:
        result = dumps(data, indent=2)
        return result
