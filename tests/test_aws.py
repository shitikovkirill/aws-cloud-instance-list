import re

from src.aws import get_instance_detail, get_token


def test_get_token():
    regex = re.compile(r'([a-zA-Z0-9_-]+)')
    token = get_token()
    result = re.match(regex, token)
    assert result.group(0)


def test_instance_detail():
    assert get_instance_detail() == ""
