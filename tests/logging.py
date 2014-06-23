"""
.. module:: tests.logging
    :platform: Unix
    :synopsis: Logging utilities.

.. moduleauthor:: Pedro Salgado <steenzout@ymail.com>

   Copyright 2014 Pedro Emanuel de Castro Faria Salgado

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import


import logging
import logging.config as config

import os


DEFAULT_CONFIG_FILE = 'tests/logging.conf'


def load_configuration(config_file=DEFAULT_CONFIG_FILE):
    """
    Loads logging configuration from the given configuration file.

    :param config_file: the configuration file (default=tests/logging.conf)
    :type config_file: str
    """
    if not os.path.exists(config_file) or not os.path.isfile(config_file):
        msg = '%s configuration file does not exist!', config_file
        logging.getLogger(__name__).error(msg)
        raise ValueError(msg)

    try:
        config.fileConfig(config_file, disable_existing_loggers=False)
        logging.getLogger(__name__).info('%s configuration file was loaded.', config_file)
    except StandardError as error:
        logging.getLogger(__name__).error('Failed to load configuration from %s!', config_file)
        logging.getLogger(__name__).debug(str(error), exc_info=True)
        raise error
