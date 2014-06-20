import kerfi

import tests


class CleanupPropertyTestCase(tests.BaseTestCase):
    """
    Test cases for kerfi.cleanup() function.
    """

    def test(self):
        """
        Tests the kerfi.cleanup() function.
        """
        self.assertEquals('key_key', kerfi.cleanup_property(' key key '))
