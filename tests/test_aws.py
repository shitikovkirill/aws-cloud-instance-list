import re

from src.aws import get_instance_detail, get_token, get_instance_vpc


def test_get_token():
    token = get_token()
    regex = re.compile(r'([a-zA-Z0-9_-]+)')
    result = re.match(regex, token)
    assert result.group(0)


def test_instance_detail():
    assert "instanceId" in get_instance_detail().keys()
    assert "region" in get_instance_detail().keys()


def test_get_instance_vpc():
    detail = get_instance_detail()
    vpc = get_instance_vpc(detail["instanceId"], detail["region"])
    assert vpc
