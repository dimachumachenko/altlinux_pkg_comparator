import unittest
from unittest.mock import patch, MagicMock
import requests
from altpkg.api import perform_get_request, parse_json_structures, find_arch

BASE_URL = "https://rdb.altlinux.org/api/export/branch_binary_packages"


class TestAPIWithAltLinux(unittest.TestCase):
    def test_perform_get_request_sisyphus(self):
        
        branch = "sisyphus"
        url = f"{BASE_URL}/{branch}"
        response = perform_get_request(url)
        data = parse_json_structures(response)

        self.assertIn("packages", data)
        self.assertIsInstance(data["packages"], list)
        self.assertGreater(len(data["packages"]), 0)

    def test_perform_get_request_p10(self):
       
        branch = "p10"
        url = f"{BASE_URL}/{branch}"
        response = perform_get_request(url)
        data = parse_json_structures(response)

        self.assertIn("packages", data)
        self.assertIsInstance(data["packages"], list)
        self.assertGreater(len(data["packages"]), 0)

    def test_find_arch_sisyphus(self):
        
        branch = "sisyphus"
        url = f"{BASE_URL}/{branch}"
        response = perform_get_request(url)
        arch_list = find_arch(response)

        self.assertIsInstance(arch_list, list)
        self.assertGreater(len(arch_list), 0)

    def test_find_arch_p10(self):
     
        branch = "p10"
        url = f"{BASE_URL}/{branch}"
        response = perform_get_request(url)
        arch_list = find_arch(response)

        self.assertIsInstance(arch_list, list)
        self.assertGreater(len(arch_list), 0)


if __name__ == "__main__":
    unittest.main()
