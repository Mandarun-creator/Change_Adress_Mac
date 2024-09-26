
import unittest
from changeadressmac import get_mac_address, change_mac_address

class TestChangeAddressMac(unittest.TestCase):
    def test_get_mac_address(self):
        interfaces = get_mac_address()
        self.assertIsInstance(interfaces, dict)

    def test_change_mac_address(self):
        result = change_mac_address('eth0', '00:11:22:33:44:55')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
