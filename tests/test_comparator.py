import unittest
from altpkg.comparator import (
    existence_packages,
    single_compare_version,
    version_comparison,
)

class TestComparator(unittest.TestCase):

    def setUp(self):
        
        self.sis_data = {
            "packages": [
                {"name": "pkg1", "version": "1.0", "release": "1", "arch": "x86_64"},
                {"name": "pkg2", "version": "2.0", "release": "1", "arch": "x86_64"},
                {"name": "pkg3", "version": "1.5", "release": "2", "arch": "x86_64"}
            ]
        }
        self.p10_data = {
            "packages": [
                {"name": "pkg2", "version": "2.0", "release": "1", "arch": "x86_64"},
                {"name": "pkg3", "version": "1.0", "release": "1", "arch": "x86_64"},
                {"name": "pkg4", "version": "3.0", "release": "1", "arch": "x86_64"}
            ]
        }

    def test_existence_packages(self):
        
        result = existence_packages(self.sis_data, self.p10_data)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "pkg1")

    def test_single_compare_version(self):
        # Тест сравнения двух версий
        self.assertGreater(
            single_compare_version("2.0", "1", "1.5", "2"), 0
        )
        self.assertEqual(
            single_compare_version("1.0", "1", "1.0", "1"), 0
        )
        self.assertLess(
            single_compare_version("1.0", "1", "2.0", "1"), 0
        )

    def test_version_comparison(self):
        
        result = version_comparison(self.sis_data, self.p10_data)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "pkg3")
        self.assertEqual(result[0]["version"], "1.5")
        self.assertEqual(result[0]["release"], "2")


if __name__ == "__main__":
    unittest.main()
