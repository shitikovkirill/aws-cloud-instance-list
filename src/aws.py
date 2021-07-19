import boto3
import requests


def get_token():
    response = requests.put(
        "http://169.254.169.254/latest/api/token",
        headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"}
    )
    return response.text


def get_instance_detail():
    token = get_token()
    response = requests.get(
        "http://169.254.169.254/latest/dynamic/instance-identity/document",
        headers={"X-aws-ec2-metadata-token": token}
    )
    return response.json()
