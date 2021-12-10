from abc import ABC, abstractmethod
from xml.dom.minidom import parseString
from json import dumps
from dataclasses import asdict

from dicttoxml import dicttoxml


class SerializerInterface(ABC):
    """Interface for all serializers"""
    @staticmethod
    @abstractmethod
    def serialize(data: list) -> str:
        pass


class XMLSerializer(SerializerInterface):
    """Class for serializing xml"""
    @staticmethod
    def serialize(data: list) -> str:
        data_dicts = [asdict(i) for i in data]
        xml = dicttoxml(data_dicts, custom_root="rooms")
        result = parseString(xml).toprettyxml()
        return result


class JSONSerializer(SerializerInterface):
    """Class for serializing xml"""
    @staticmethod
    def serialize(data: list) -> str:
        data_dicts = [asdict(i) for i in data]
        result = dumps(data_dicts, indent=2)
        return result
