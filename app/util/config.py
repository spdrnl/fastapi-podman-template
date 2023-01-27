import os
import logging
import logging.config
from dotenv import dotenv_values
import tomli

__all__ = ["env", "settings"]


def _get_env():
    """Load the environment variables either from the .env file of from the command line settings.

    Returns:
        dict: A dict with the enviromental settings"

    """

    logging.info("Loading the environment variables.")

    env = {
        **dotenv_values(".env"),  # load variables for this system
        **os.environ,  # override loaded values with environment variables
    }

    # Apply default settings
    env["env"] = env.get("env", "dev")
    env["settings"] = env.get("settings", "settings.toml")
    env["logging"] = env.get("logging", "logging.conf")

    return env


def _get_settings(env):
    """Reads the settings from a TOML file.

    Returns:
        dict: A dict with the settings

    """

    logger.info("Reading the settings.")

    settings_path = env["settings"]

    # Read the settings file and return the settings
    try:
        with open(settings_path, "rb") as f:
            return tomli.load(f)
    except tomli.TOMLDecodeError:
        logger.error(
            f"The settings file {settings_path} is not a valid TOML file."
        )
    except FileNotFoundError:
        logger.error(
            f"The path {settings_path} for the settings file is not valid."
        )

    exit(1)

# Bootstrap logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialise the application
env = _get_env()
settings = _get_settings(env)
logging.config.fileConfig(env['logging'])
