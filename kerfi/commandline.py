"""
.. module:: kerfi.commandline
    :platform: Unix
    :synopsis: Module that implements command-line functionality.

.. moduleauthor:: Pedro Salgado <steenzout@ymail.com>
"""

import sys

import kerfi


AUTO = 'auto'
RAW = 'raw'
XML = 'xml'


def print_properties(stream, properties, format=AUTO):
    if format != AUTO:
        fmt = format
    else:
        fmt = None

    for line in stream.readlines():
        if fmt is None:
            if line.startswith('<?xml'):
                fmt = XML
            else:
                fmt = RAW

        print '%s : %s' % (fmt, line)


def print_version():
    """
    Prints the kerfi package version to stdout.
    """
    sys.stdout.write('kerfi-vangasvipur %s\n' % kerfi.__version__)
