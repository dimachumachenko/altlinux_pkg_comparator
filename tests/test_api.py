import unittest
from altpkg.api import fetch_packages


class TestAPI(unittest.TestCase):
	def test_fetch_packages(self):
		data = fetch_packages("sisyphus")
		self.assertIsInstance(ddata, list)
		self.assertTrue(len(data) > 0)

if __name__ == "__main__":
    unittest.main()