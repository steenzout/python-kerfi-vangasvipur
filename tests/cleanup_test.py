import kerfi

import tests


class CleanupPropertyTestCase(tests.BaseTestCase):
    """
    Test cases for kerfi.cleanup_property() function.
    """

    def test(self):
        """
        Tests the kerfi.cleanup_property() function.
        """
        self.assertEquals('key_key', kerfi.cleanup_property(' key key: '))
