from abc import ABC, abstractmethod
from xml.dom.minidom import parseString
from json import dumps

from dicttoxml import dicttoxml


class SerializerInterface(ABC):
    """Interface for all serializers"""
    @staticmethod
    @abstractmethod
    def serialize(data: list[dict]) -> str:
        pass


class XMLSerializer(SerializerInterface):
    """Class for serializing xml"""
    @staticmethod
    def serialize(data: list[dict]) -> str:
        xml = dicttoxml(data, custom_root="rooms")
        result = parseString(xml).toprettyxml()
        return result


class JSONSerializer(SerializerInterface):
    """Class for serializing xml"""
    @staticmethod
    def serialize(data: list[dict]) -> str:
        result = dumps(data, indent=2)
        return result
