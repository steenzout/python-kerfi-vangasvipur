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
    levels = [0]
    for line in stream.readlines():
        LOGGER.debug('line = %s', line)
        try:
            if line != '\n':
                prop, value = line.split(':', 1)
                lenprop1 = len(prop)
                prop = cleanup_property(prop)
                lenprop2 = len(prop)
                thislevel = lenprop1 - lenprop2
                value = value.strip()

                if thislevel == 0:
                    namespace = [cleanup_property(prop)]
                    levels = [0]
                else:
                    while thislevel <= levels[-1]:
                        namespace.pop()
                        levels.pop()
                    namespace.append(cleanup_property(prop))
                    levels.append(thislevel)

                if value != '':
                    o['.'.join(namespace)] = value

            LOGGER.debug('namespace = %s', namespace)
            LOGGER.debug('levels = %s', levels)

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


def version():
    """
    Kerfi version.

    :return: the package version.
    :rtype: str
    """
    return __version__
