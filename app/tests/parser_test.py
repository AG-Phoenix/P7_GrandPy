import pytest
from app.utils import Parser


def test_parse_text():
    user_text = "Salut Grandpy! Tu connais l'adresse de OpenClassrooms?"
    parser = Parser(user_text)
    assert parser.parsed_text == "openclassrooms"


def test_location_or_address():
    user_text = "Salut Grandpy! Tu connais l'adresse de OpenClassrooms?"
    parser = Parser(user_text)
    assert parser.location is True
    assert parser.address is False
