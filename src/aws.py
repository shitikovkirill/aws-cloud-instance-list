import boto3
import requests


def get_token():
    token = requests.put(
        "http://169.254.169.254/latest/api/token",
        headers={"X-aws-ec2-meconds": "21600"}
    )
    return token


def get_instance_detail():
    token = get_token()
    data = requests.get(
        "http://169.254.169.254/latest/dynamic/instance-identity/document",
        headers={"X-aws-ec2-metadata-token": token}
    )
    return data
