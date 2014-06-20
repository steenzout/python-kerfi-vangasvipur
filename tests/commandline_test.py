import kerfi

import mock

import tests


from kerfi import commandline


class PrintPropertiesTestCase(tests.BaseTestCase):
    """
    Test cases for kerfi.commandline.print_properties() function.
    """

    @mock.patch('sys.stdout.write', autospec=True)
    @mock.patch('kerfi.load_raw')
    def test_auto(self, mock_load_raw, mock_stdout):
        """
        Tests kerfi.commandline.print_properties() writes the expected message to stdout.
        """
        mock_load_raw.return_value = {
            'other_prop': '0', 'prop1': '1', 'prop2': '2', 'single': 3}

        with open('tests/input.txt', 'r') as f:
            commandline.print_properties(f, ['single', 'prop.*', 'none'])

            mock_load_raw.assert_called_once(f)

        mock_stdout.assert_has_calls([
            mock.call('prop1\t1\n'),
            mock.call('prop2\t2\n'),
            mock.call('single\t3\n')], any_order=True)


    @mock.patch('sys.stdout.write', autospec=True)
    @mock.patch('kerfi.load_xml')
    def test_xml(self, mock_load_xml, mock_stdout):
        """
        Tests kerfi.commandline.print_properties() writes the expected message to stdout.
        """
        mock_load_raw.return_value = {
            'other_prop': '0', 'prop1': '1', 'prop2': '2', 'single': 3}

        with open('tests/input.txt', 'r') as f:
            commandline.print_properties(f, ['single', 'prop.*', 'none'], format=kerfi.commandline.XML)

            mock_load_xml.assert_called_once(f)

        mock_stdout.assert_has_calls([
            mock.call('prop1\t1\n'),
            mock.call('prop2\t2\n'),
            mock.call('single\t3\n')], any_order=True)


class PrintVersionTestCase(tests.BaseTestCase):
    """
    Test cases for kerfi.commandline.print_version() function.
    """

    @mock.patch('kerfi.commandline.sys.stdout.write', autospec=True)
    def test(self, mock_stdout):
        """
        Tests if kerfi.commandline.print_version() writes the expected message in stdout.

        :param mock_stdout: mock for sys.stdout.write().
        """
        commandline.print_version()

        mock_stdout.assert_called_once_with('kerfi-vangasvipur %s\n' % kerfi.__version__)
