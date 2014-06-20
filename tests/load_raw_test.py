import kerfi

import tests


class LoadRawTestCase(tests.BaseTestCase):
    """
    Test cases for kerfi.load_raw() function.
    """

    def test(self):
        expected = {
            'Accessibility.Accessibility_Information.Cursor_Magnification': 'Off',
            'Applications.Installer.Version': '9.0.11'}

        with open('tests/input.txt', 'r') as f:
            result = kerfi.load_raw(f)

        self.logger.debug('result = %s', result)

        for key, value in expected.iteritems():
            self.assertTrue(key in result)
            self.assertEquals(value, result[key])
