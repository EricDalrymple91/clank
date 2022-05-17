import click
from clank.constants.colors import COLORS, GREEN, WHITE
import random


class RandomColorSpitter(object):

    def __init__(self, preferred_color=GREEN):
        self.preferred_color = preferred_color

    @classmethod
    def random_color(cls):
        return random.choice(COLORS)


@click.group()
@click.pass_context
def clank(ctx):
    ctx.obj = RandomColorSpitter()


@clank.command()
@click.argument("text")
@click.pass_context
def texter(ctx, text):
    click.echo(click.style(text, fg=ctx.obj.random_color()))


@clank.command()
@click.argument("text")
@click.pass_context
def blinker(ctx, text):
    click.echo(click.style(text, fg=ctx.obj.random_color(), blink=True))


@clank.command()
@click.argument("text")
@click.pass_context
def underliner(ctx, text):
    click.echo(click.style(text, fg=ctx.obj.random_color(), underline=True))


@clank.command()
@click.argument("text")
@click.pass_context
def bolder(ctx, text):
    click.echo(click.style(text, fg=ctx.obj.random_color(), bold=True))


@clank.command()
@click.argument("text")
@click.option("--c", "--color", "color", default=WHITE, type=click.Choice(COLORS), help="Choose a text color")
@click.pass_context
def chooser(ctx, text, color):
    click.echo(click.style(text, fg=color, bg=ctx.obj.preferred_color, bold=True))





