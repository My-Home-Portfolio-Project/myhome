#!/usr/bin/python3
import unittest
from models.apartment import Apartment
from models.country import Country
import models
from os import getenv

class TestApartment(unittest.TestCase):
    def setUp(self):
        """Set up test cases"""
        self.storage_t = getenv('HBNB_TYPE_STORAGE')
        self.country = Country(name="Testland")
        models.storage.new(self.country)
        models.storage.save()
        self.apartment = Apartment(name="Test Apartment", country_id=self.country.id)
        models.storage.new(self.apartment)
        models.storage.save()

    def tearDown(self):
        """Clean up storage"""
        models.storage.delete(self.apartment)
        models.storage.delete(self.country)
        models.storage.save()

    def test_apartment_creation(self):
        """Test creating an Apartment instance"""
        self.assertIsInstance(self.apartment, Apartment)
        self.assertEqual(self.apartment.name, "Test Apartment")
        self.assertEqual(self.apartment.country_id, self.country.id)
        self.assertIsNotNone(self.apartment.id)
        self.assertIsNotNone(self.apartment.created_at)
        self.assertIsNotNone(self.apartment.updated_at)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "DB storage only")
    def test_apartment_country_relationship_db(self):
        """Test relationship between Apartment and Country in DB storage"""
        self.assertEqual(self.apartment.country, self.country)
        self.assertIn(self.apartment, self.country.apartments)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "File storage only")
    def test_apartment_country_relationship_file(self):
        """Test relationship between Apartment and Country in file storage"""
        self.assertEqual(self.apartment.country, self.country)
        self.assertIn(self.apartment, self.country.apartments)

if __name__ == "__main__":
    unittest.main()
