"""
Simplest logging configuration to make sure everything loads correctly.
"""
import logging
import logging_cfg
import module1.logging_module1 as m1

logging_cfg.setup_logging()
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Start reading data')
    m1.run()
    logger.info('End reading data')
