import re

from src.aws import get_instance_detail, get_token


def test_get_token():
    regex = re.compile(r'(?:\w+\s+)([a-zA-Z_][a-zA-Z0-9]+)\b')
    token = get_token()
    assert re.search(regex, token)


def test_instance_detail():
    assert get_instance_detail() == ""
