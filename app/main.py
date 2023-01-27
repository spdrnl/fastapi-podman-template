import click
import logging
from app.config.config import env, settings


logger = logging.getLogger(__name__)


@click.command()
@click.option("--count", default=1, help="number of greetings")
@click.argument("name")
def hello(count, name):
    """A simple greeting function."""

    logger.info(f"The current env is: {env['env']}")
    logger.info(f"The value of b is : {settings['app']['b']}")

    for x in range(count):
        click.echo(f"Hello {name}!")


# The hello function is registered as script in pyproject.toml
# if __name__ == "__main__":
#     hello()
