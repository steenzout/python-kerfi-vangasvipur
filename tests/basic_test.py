import tests


class ATestCase(tests.BaseTestCase):

    def test_logging_configuration_loaded(self):
        self.assertTrue(self.logger is not None)

    def test_configuration_loaded(self):
        self.assertTrue(self.configuration is not None)

    def test_configuration_contents(self):
        self.assertTrue('kerfi.package' in self.configuration)
        self.assertTrue('key' in self.configuration['kerfi.package'])
        self.assertEquals(self.configuration['kerfi.package']['key'], 'value')
