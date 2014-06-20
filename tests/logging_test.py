import kerfi.logging

import mock

import pytest

import unittest


from kerfi.logging import DEFAULT_CONFIG_FILE


class LoadLoggingConfigurationTestCase(unittest.TestCase):
    """
    Tests for the kerfi.logging.load_configuration() function.
    """

    def setUp(self):
        # mock of logging.RootLogger
        self.patch_get_logger = mock.patch('kerfi.logging.logging.getLogger', autospec=True)
        self.mock_get_logger = self.patch_get_logger.start()

        self.patch_root_logger = mock.patch('kerfi.logging.logging.RootLogger', autospec=True)
        self.mock_root_logger = self.patch_root_logger.start()
        self.mock_get_logger.return_value = self.mock_root_logger

        self.patch_path_exists = mock.patch('os.path', autospec=True)
        self.mock_path = self.patch_path_exists.start()

        self.patch_fileConfig = mock.patch('kerfi.logging.logging.config.fileConfig', autospec=True)
        self.mock_fileConfig = self.patch_fileConfig.start()

    def tearDown(self):
        self.patch_get_logger.stop()
        self.patch_root_logger.stop()
        self.patch_path_exists.stop()
        self.patch_fileConfig.stop()

    def test(self):
        """
        Test kerfi.logging.logging.load_configuration().
        """
        self.mock_path.exists.return_value = True
        self.mock_path.isfile.return_value = True
        self.mock_fileConfig.return_value = None

        kerfi.logging.logging.load_configuration()

        self.mock_path.exists.assert_called_once_with(DEFAULT_CONFIG_FILE)
        self.mock_path.isfile.assert_called_once_with(DEFAULT_CONFIG_FILE)
        self.mock_fileConfig.assert_called_with(DEFAULT_CONFIG_FILE, disable_existing_loggers=False)

        self.assertTrue(self.mock_get_logger.called)
        self.mock_root_logger.info.assert_called_once_with('%s configuration file was loaded.', DEFAULT_CONFIG_FILE)

    def test_nofile(self):
        """
        Test kerfi.logging.logging.load_configuration() when the configuration file doesn't exist.
        """
        self.mock_path.exists.return_value = True
        self.mock_path.isfile.return_value = False

        with pytest.raises(ValueError):
            kerfi.logging.logging.load_configuration()

        self.mock_path.exists.assert_called_once_with(DEFAULT_CONFIG_FILE)
        self.mock_path.isfile.assert_called_once_with(DEFAULT_CONFIG_FILE)
        self.assertFalse(self.mock_fileConfig.called)

        self.assertTrue(self.mock_get_logger.called)
        self.mock_root_logger.error.assert_called_once_with((
            '%s configuration file does not exist!', DEFAULT_CONFIG_FILE))

    def test_errors(self):
        """
        Test kerfi.logging.logging.load_configuration() when errors are raised.
        """
        self.mock_path.exists.return_value = True
        self.mock_path.isfile.return_value = True
        self.mock_fileConfig.side_effect = ValueError('fake error')

        with pytest.raises(ValueError):
            kerfi.logging.logging.load_configuration()

        self.mock_path.exists.assert_called_once_with(DEFAULT_CONFIG_FILE)
        self.mock_path.isfile.assert_called_once_with(DEFAULT_CONFIG_FILE)
        self.assertTrue(self.mock_fileConfig.called)

        self.assertTrue(self.mock_get_logger.called)
        self.mock_root_logger.error.assert_called_once_with(
            'Failed to load configuration from %s!', DEFAULT_CONFIG_FILE)
        self.mock_root_logger.debug.assert_called_once_with(
            str(ValueError('fake error')), exc_info=True)
