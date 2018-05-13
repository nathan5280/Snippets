"""
Simplest logging configuration to make sure everything loads correctly.
"""
import logging
import logging.config
from typing import Dict

import logging_.module1.logging_module1 as m1

logging_cfg = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {
            "format": "\t%(name)s:%(funcName)s:%(lineno)s - %(levelname)s - %(message)s"
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        }
    },

    "loggers": {
        "logging_.module1.logging_module1": {
            "level": "WARN",
            "handlers": ["console"],
            "propagate": False
        }
    },

    "root": {
        "level": "WARN",
        "handlers": ["console"]
    }
}


def setup_logging(cfg: Dict) -> None:
    """
    Setup the logging by loading the configuration file.
    """

    logging.config.dictConfig(cfg)


def warning_level():
    print(f"\n{__file__}:warning_level")
    logging_cfg["loggers"] = {
        "logging_.module1.logging_module1": {
            "level": "WARN",
            "handlers": ["console"],
            "propagate": False
        }
    }

    setup_logging(logging_cfg)

    m1.run()
    m1.run_with_args(1, 2)


def debug_level():
    print(f"\n{__file__}:debug_level")
    logging_cfg["loggers"] = {
        "logging_.module1.logging_module1": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False
        }
    }

    setup_logging(logging_cfg)

    m1.run()
    m1.run_with_args(1, 2)


def log_main():
    # Note that if this module runs as main then __name__ == __main__.
    # To turn on logging in the module the logger name is __main__ not the name of the file.
    print(f"\n{__file__}:log_main")
    logging_cfg["loggers"] = {
        "logging_.module1.logging_module1": {
            "level": "WARN",
            "handlers": ["console"],
            "propagate": False
        },
        "__main__": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False
        }
    }

    setup_logging(logging_cfg)
    logger = logging.getLogger(__name__)

    logger.debug("Logging from main.")


if __name__ == '__main__':
    warning_level()
    debug_level()
    log_main()
