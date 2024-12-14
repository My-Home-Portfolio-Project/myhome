import unittest
from models.base_model import BaseModel
import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        self.base_model = BaseModel()

    def test_instance_creation(self):
        """Test if the instance is created successfully."""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertTrue(uuid.UUID(self.base_model.id))  # Valid UUID
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_save_method(self):
        """Test the `save` method updates the `updated_at` attribute."""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, old_updated_at)
        self.assertTrue(self.base_model.updated_at > old_updated_at)

    def test_to_dict(self):
        """Test the `to_dict` method returns a dictionary with correct values."""
        base_dict = self.base_model.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["id"], self.base_model.id)
        self.assertEqual(
            base_dict["created_at"],
            self.base_model.created_at.strftime("%d-%m-%Y %H:%M:%S")
        )
        self.assertEqual(
            base_dict["updated_at"],
            self.base_model.updated_at.strftime("%d-%m-%Y %H:%M:%S")
        )

    def test_delete_method(self):
        """Test the `delete` method interacts with storage."""
        # Mock the `models.storage.delete` method for testing
        class MockStorage:
            def __init__(self):
                self.deleted_objects = []

            def delete(self, obj):
                self.deleted_objects.append(obj)

        mock_storage = MockStorage()
        models.storage = mock_storage

        self.base_model.delete()
        self.assertIn(self.base_model, mock_storage.deleted_objects)

    def test_init_with_kwargs(self):
        """Test initializing with kwargs."""
        kwargs = {
            "id": str(uuid.uuid4()),
            "created_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now()
        }
        base_model = BaseModel(**kwargs)
        self.assertEqual(base_model.id, kwargs["id"])
        self.assertEqual(base_model.created_at, kwargs["created_at"])
        self.assertEqual(base_model.updated_at, kwargs["updated_at"])

if __name__ == "__main__":
    unittest.main()
