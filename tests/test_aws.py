from src.aws import get_instance_detail


def test_instance_detail():
    assert get_instance_detail()
