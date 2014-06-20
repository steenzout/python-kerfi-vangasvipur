"""
.. module:: kerfi
    :platform: Unix
    :synopsis: Kerfi package.

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


from kerfi.version import __version__


LOGGER = logging.getLogger(__name__)


def cleanup_property(key):
    """
    Cleans the given key by removing whitespace from beginning/end of it and
    replacing any other whitespace by the underscore character.

    :param key: the key.
    :return: a cleaned up key.
    :rtype: str
    """
    return key.split(':')[0].strip().replace(' ', '_')


def load_raw(stream):
    """
    Loads the system profiler raw content into a data structure.

    :param stream: the input stream.
    :return: the system profiler data structure.
    :rtype: dict
    """
    o = {}
    namespace = []
    for line in stream.readlines():
        LOGGER.debug('line = %s', line)
        try:
            if line == '\n':
                # blank line
                continue

            elif line[0] != ' ':
                namespace = [line.split(':')[0]]

            elif line[0:6] == '      ':
                prop, value = line.split(':')
                prop = cleanup_property(prop)
                value = value.strip()
                o['%s.%s' % ('.'.join(namespace), prop)] = value

            elif line[0:4] == '    ':
                namespace = [namespace[0], cleanup_property(line)]

        except StandardError:
            LOGGER.error('Error processing line %s!', line, exc_info=True)

    return o


def load_xml(stream):
    """
    Loads the system profiler XML content into a data structure.

    :param stream: the input stream.
    :return: the system profiler data structure.
    :rtype: dict
    """
    return None
