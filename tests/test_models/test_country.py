#!/usr/bin/python3
import unittest
from models.country import Country
from models.state import State
import models
from os import getenv

class TestCountry(unittest.TestCase):
    def setUp(self):
        """Set up test cases"""

        self.storage_t = getenv('HBNB_TYPE_STORAGE')
        self.country = Country(name="Testland")

    def tearDown(self):
        """Clean up storage"""

        models.storage.delete(self.country)
        models.storage.save()

    def test_country_creation(self):
        """Test creating a Country instance"""

        self.assertIsInstance(self.country, Country)
        self.assertEqual(self.country.name, "Testland")
        self.assertIsNotNone(self.country.id)
        self.assertIsNotNone(self.country.created_at)
        self.assertIsNotNone(self.country.updated_at)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "DB storage only")
    def test_country_relationship(self):
        """Test states relationship in DB storage"""

        state = State(name="Test State", country_id=self.country.id)
        models.storage.new(state)
        models.storage.save()
        self.assertIn(state, self.country.states)
        models.storage.delete(state)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "File storage only")
    def test_country_states_property(self):
        """Test states property in file storage"""

        state = State(name="Test State", country_id=self.country.id)
        models.storage.new(state)
        models.storage.save()
        self.assertIn(state, self.country.states)
        models.storage.delete(state)

if __name__ == "__main__":
    unittest.main()
