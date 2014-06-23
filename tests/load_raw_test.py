import kerfi

import tests


class LoadRawTestCase(tests.BaseTestCase):
    """
    Test cases for kerfi.load_raw() function.
    """

    def test(self):
        expected = {
            'Accessibility.Accessibility_Information.Cursor_Magnification': 'Off',
            'Applications.Installer.Version': '9.0.11',
            'Applications.Console.Version': '10.9',
            'Locations.Automatic.Active_Location': 'Yes',
            'Locations.Automatic.Services.Bluetooth_DUN.Type': 'PPP',
            'Locations.Automatic.Services.USB_Ethernet.Type': 'Ethernet'}

        with open('tests/input.txt', 'r') as f:
            result = kerfi.load_raw(f)

        self.logger.debug('result = %s', result)

        for key, value in expected.iteritems():
            self.logger.debug('checking %s', key)
            self.assertTrue(key in result)
            self.logger.debug('%s found.', key)
            self.assertEquals(value, result[key])
            self.logger.debug('%s value is equal.', key)
