import click
from tabulate import tabulate

from aws import get_instance_detail, get_instance_vpc, get_instances_from_vpc


@click.command()
def info():
    """Get instances from vpc"""
    detail = get_instance_detail()
    vpc = get_instance_vpc(detail["instanceId"], detail["region"])
    instances = get_instances_from_vpc(vpc, detail["region"])
    table = []
    headers = ["Ip", "Name"]
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            private_ip_addr = instance['PrivateIpAddress']
            table.append([
                private_ip_addr,
                [inst['Value'] for inst in instance['Tags']
                 if inst['Key'] == 'Name'][0]
            ])
    print(tabulate(table, headers, tablefmt="grid"))


if __name__ == '__main__':
    info()
