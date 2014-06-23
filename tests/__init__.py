"""
.. module:: tests
    :platform: Unix
    :synopsis:

.. moduleauthor:: Pedro Salgado <steenzout@ymail.com>
"""

from __future__ import absolute_import


import logging

import tests.logging

import unittest


tests.logging.load_configuration()


class Basic(object):
    """
    Basic functionality to enhance test cases.
    """

    def setup_configuration(self):
        """
        Setup test configuration.
        It will also load (once) the test configuration.
        """
        logging.getLogger('%s.%s' % (__name__, 'Basic')).info('setup_configuration()')

        self.configuration = None

    def setup_logger(self):
        """
        Setup test logger.
        It will also load (once) the test logging configuration.
        """
        logging.getLogger('%s.%s' % (__name__, 'Basic')).info('setup_logger()')

        self.logger = logging.getLogger('%s.%s' % (__name__, self.__class__.__name__))


class BaseTestCase(unittest.TestCase, Basic):
    """
    Base test case.
    """

    __slots__ = ('configuration', 'logger')

    def __init__(self, methodName):
        """
        Initializes a BaseTestCase instance.

        :param methodName: the test method to be executed.
        :type methodName: str
        """
        super(BaseTestCase, self).__init__(methodName)

        self.setup_logger()
        self.setup_configuration()

    def setUp(self):
        """
        Setup test resources.
        """
        self.logger.info('setUp()')

    def tearDown(self):
        """
        Tear down test resources.
        """
        self.logger.info('tearDown()')
