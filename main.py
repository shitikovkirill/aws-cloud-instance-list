import click

from aws import get_instance_detail, get_instance_vpc, get_instances_from_vpc


@click.command()
def info():
    """Get instances from vpc"""
    detail = get_instance_detail()
    vpc = get_instance_vpc(detail["instanceId"], detail["region"])
    instances = get_instances_from_vpc(vpc, detail["region"])


if __name__ == '__main__':
    info()
