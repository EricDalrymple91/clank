import click
from clank.commands.clanker import clank
from clank.commands.heliopad import heliopad


@click.group()
def cli():
    """
    Clank!
    """
    pass


cli.add_command(clank)
cli.add_command(heliopad)


if __name__ == '__cli__':
    cli()
