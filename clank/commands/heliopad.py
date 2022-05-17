import click


@click.group()
def heliopad():
    pass


@heliopad.command()
@click.option("--t", "-text", "text", default="Hello", help="Choose text")
@click.option("--n", "--count", "count", default="3", help="Pick loop count")
def looper(text, count):
    for i in range(int(count)):
        click.echo(f'{text} #{i + 1}')
