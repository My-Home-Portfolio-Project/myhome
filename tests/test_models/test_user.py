#!/usr/bin/python3
import unittest
from models.user import User
import models
from os import getenv

class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up test cases"""
        self.storage_t = getenv('HBNB_TYPE_STORAGE')
        self.user = User(email="testuser@example.com")
        self.user.set_password("securepassword123")
        models.storage.new(self.user)
        models.storage.save()

    def tearDown(self):
        """Clean up storage"""
        models.storage.delete(self.user)
        models.storage.save()

    def test_user_creation(self):
        """Test creating a User instance"""
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertIsNotNone(self.user.password_hash)

    def test_password_hashing(self):
        """Test that password is hashed correctly"""
        self.assertNotEqual(self.user.password_hash, "securepassword123")

    def test_check_password(self):
        """Test password verification"""
        self.assertTrue(self.user.check_password("securepassword123"))
        self.assertFalse(self.user.check_password("wrongpassword"))

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "DB storage only")
    def test_user_email_uniqueness_db(self):
        """Test email uniqueness in database storage"""
        duplicate_user = User(email="testuser@example.com")
        duplicate_user.set_password("anotherpassword")
        models.storage.new(duplicate_user)
        with self.assertRaises(Exception):
            models.storage.save()  # Should raise an exception due to unique constraint
        models.storage.delete(duplicate_user)

    def test_login_process(self):
        """Simulate a login process"""
        email = "testuser@example.com"
        password = "securepassword123"

        user = next((u for u in models.storage.all('User').values() if u.email == email), None)
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password(password))

if __name__ == "__main__":
    unittest.main()
