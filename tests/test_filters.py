# tests/test_filters.py

import unittest
from get_papers.filters import extract_non_academic_authors

class TestFilters(unittest.TestCase):
    def test_non_academic_detection(self):
        authors = ["Alice Smith", "Bob Johnson", "Dr. Evil"]
        affiliations = [
            "Department of Computer Science, University of Somewhere",
            "Global Biotech Inc.",
            "EvilCorp Pharmaceuticals, Inc."
        ]

        non_ac_authors, companies = extract_non_academic_authors(authors, affiliations)

        self.assertIn("Bob Johnson", non_ac_authors)
        self.assertIn("Global Biotech Inc.", companies)
        self.assertIn("Dr. Evil", non_ac_authors)
        self.assertNotIn("Alice Smith", non_ac_authors)

if __name__ == "__main__":
    unittest.main()
