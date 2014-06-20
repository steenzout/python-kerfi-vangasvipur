"""
.. module:: kerfi.commandline
    :platform: Unix
    :synopsis: Module that implements command-line functionality.

.. moduleauthor:: Pedro Salgado <steenzout@ymail.com>
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

    for key, value in data.iteritems():
        LOGGER.debug('key %s in properties (%s)? %s', key, properties, key in properties)

        if key in properties:
            LOGGER.debug('key:value = %s:%s', key, value)
            sys.stdout.write('%s\t%s\n' % (key, value))
        else:
            for prop in properties:
                LOGGER.debug('re.match %s matches %s? %s', prop, key, re.match(prop, key) is not None)

                if re.match(prop, key):
                    LOGGER.debug('sys.stdout.write(\'%s\t%s\n\')', key, value)
                    LOGGER.debug('key:value = %s:%s', key, value)
                    sys.stdout.write('%s\t%s\n' % (key, value))


def print_version():
    """
    Prints the kerfi package version to stdout.
    """
    sys.stdout.write('kerfi-vangasvipur %s\n' % kerfi.__version__)
