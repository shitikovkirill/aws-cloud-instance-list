import click


@click.command()
@click.option('--instance-id', type=str, required=True, help='Instance id.')
def info(instance_id):
    """Get instances from vpc"""
    click.echo(f"Hello {instance_id}!")


if __name__ == '__main__':
    info()
