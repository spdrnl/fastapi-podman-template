import click


@click.command()
@click.option("--count", default=1, help="number of greetings")
@click.argument("name")
def hello(count, name):
    """A simple greeting function."""
    for x in range(count):
        click.echo(f"Hello {name}!")


# The hello function is registered as script in pyproject.toml
# if __name__ == "__main__":
#     hello()
