import click
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s ",
)
from app.util.config import get_env_config


logger = logging.getLogger(__name__)


@click.command()
@click.option("--count", default=1, help="number of greetings")
@click.argument("name")
def hello(count, name):
    """A simple greeting function."""

    env = get_env_config()
    logger.info(f"The current system is: {env.get('system', 'dev')}")
    
    for x in range(count):
        click.echo(f"Hello {name}!")


# The hello function is registered as script in pyproject.toml
# if __name__ == "__main__":
#     hello()
