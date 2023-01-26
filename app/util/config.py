import os
import logging
from dotenv import dotenv_values


logger = logging.getLogger(__name__)


def get_env_config():
    logger.info("Loading environmental variables.")

    conf = {
        **dotenv_values(".env"),  # load variables for this system
        **dotenv_values(".env.shared"),  # load shared development variables
        **dotenv_values(".env.secret"),  # load sensitive variables
        **os.environ,  # override loaded values with environment variables
    }

    return conf
