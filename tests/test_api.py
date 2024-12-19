import unittest
from altpkg.api import fetch_packages

class TestAPI(unittest.TestCase):
    def test_fetch_packages_valid_branch(self):
        
        data = fetch_packages("sisyphus")
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)
        for pkg in data:
            self.assertIn("name", pkg)
            self.assertIn("version", pkg)
            self.assertIn("release", pkg)
            self.assertIn("arch", pkg)

    def test_fetch_packages_with_arch(self):
        
        data = fetch_packages("sisyphus", arch="x86_64")
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)
        for pkg in data:
            self.assertEqual(pkg["arch"], "x86_64")

    def test_fetch_packages_invalid_branch(self):
        
        with self.assertRaises(ValueError) as context:
            fetch_packages("invalid_branch")
        self.assertIn("Error fetching packages", str(context.exception))

    def test_fetch_packages_p10(self):
        
        data = fetch_packages("p10")
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)

if __name__ == "__main__":
    unittest.main()
