from src.aws import get_instance_detail, get_token


def test_get_token():
    assert get_token() == ""


def test_instance_detail():
    assert get_instance_detail() == ""
