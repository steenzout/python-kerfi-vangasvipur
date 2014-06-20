import kerfi

import mock

import tests


from kerfi import commandline


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
