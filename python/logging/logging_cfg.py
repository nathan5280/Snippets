import os
import json
import logging.config

def setup_logging(path='logging_cfg.json', default_level=logging.INFO):
    ''' Setup the logging by loading the configuration file.'''
    if os.path.exists(path):
        with open(path) as f:
            config = json.load(f)
        logging.config.dictConfig(config)
        print('Loading logging cfg')
    else:
        logging.basicConfig(level=default_level)
        print('Default logging cfg')
