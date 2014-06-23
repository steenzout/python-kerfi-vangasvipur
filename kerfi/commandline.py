"""
.. module:: kerfi.commandline
    :platform: Unix
    :synopsis: Module that implements command-line functionality.

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


import sys

import kerfi

import logging

import re


AUTO = 'auto'
RAW = 'raw'
XML = 'xml'

LOGGER = logging.getLogger(__name__)


def print_properties(stream, properties, input_format=AUTO):
    """
    Prints the given system_profiler properties to stdout.

    :param stream: the input stream.
    :param properties: the system properties to be printed.
    :type properties: list
    :param input_format: the input format (auto, raw or xml).
    :type input_format: str
    """

    if input_format == AUTO:
        header = stream.readline(5)
        stream.seek(0)
        if header.startswith('<?xml'):
            fmt = XML
        else:
            fmt = RAW
    else:
        fmt = input_format

    if fmt == RAW:
        data = kerfi.load_raw(stream)
    else:
        data = kerfi.load_xml(stream)

    LOGGER.debug('input_format=%s fmt=%s', input_format, fmt)

    found = False
    for key, value in data.iteritems():
        LOGGER.debug('key %s in properties (%s)? %s', key, properties, key in properties)

        if key in properties:
            LOGGER.debug('key:value = %s:%s', key, value)
            sys.stdout.write('%s\t%s\n' % (key, value))
            found = True
        else:
            for prop in properties:
                LOGGER.debug('re.match %s matches %s? %s', prop, key, re.match(prop, key) is not None)

                if re.match(prop, key):
                    LOGGER.debug('sys.stdout.write(\'%s\t%s\n\')', key, value)
                    LOGGER.debug('key:value = %s:%s', key, value)
                    sys.stdout.write('%s\t%s\n' % (key, value))
                    found = True

    if not found:
        sys.stdout.write('\n')


def print_version():
    """
    Prints the kerfi package version to stdout.
    """
    sys.stdout.write('kerfi-vangasvipur %s\n' % kerfi.__version__)
