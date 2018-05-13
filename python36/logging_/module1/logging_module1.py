import logging

logger = logging.getLogger(__name__)


def run() -> None:
    logger.warning("Running module1: Warning")
    logger.info('Running module1: Info')
    logger.debug("Running module1: Debug")


def run_with_args(a1: int, a2: int) -> None:
    logger.debug(locals())
